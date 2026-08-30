#!/usr/bin/env python3
"""Normalize a guide character and build its detail and 14% map previews."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw


CANVAS = 1024
CHARACTER_HEIGHT = 700
VIEWPORT = (780, 1380)
WIDTH_RATIO = 0.14
SAFE_INSET = 22
BOTTOM_CARD_TOP = 1130


def alpha_crop(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    bounds = rgba.getchannel("A").getbbox()
    if not bounds:
        raise ValueError("input image has no visible alpha content")
    return rgba.crop(bounds)


def normalize(source: Path) -> tuple[Image.Image, tuple[int, int, int, int]]:
    art = alpha_crop(Image.open(source))
    ratio = CHARACTER_HEIGHT / art.height
    size = (round(art.width * ratio), CHARACTER_HEIGHT)
    art = art.resize(size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))
    x = (CANVAS - art.width) // 2
    y = (CANVAS - art.height) // 2
    canvas.alpha_composite(art, (x, y))
    bounds = canvas.getchannel("A").getbbox()
    if not bounds:
        raise ValueError("normalized image has no visible alpha content")
    return canvas, bounds


def draw_map_background() -> Image.Image:
    image = Image.new("RGB", VIEWPORT, "#FFFFFF")
    draw = ImageDraw.Draw(image)
    road = "#E6E2DC"
    park = "#EEF5EA"
    water = "#EAF6FA"

    draw.rounded_rectangle((35, 265, 280, 600), radius=42, fill=park)
    draw.rounded_rectangle((530, 535, 746, 875), radius=42, fill=park)
    draw.polygon([(0, 858), (195, 806), (410, 860), (780, 760), (780, 920), (400, 1010), (190, 956), (0, 1016)], fill=water)

    roads = [
        [(120, 0), (210, 250), (176, 520), (250, 760), (70, 1060)],
        [(700, 0), (500, 170), (390, 390), (285, 660), (560, 1050)],
        [(0, 220), (210, 360), (420, 315), (780, 440)],
        [(0, 650), (210, 700), (470, 665), (780, 565)],
    ]
    for points in roads:
        draw.line(points, fill=road, width=13, joint="curve")
        draw.line(points, fill="#FFFFFF", width=5, joint="curve")

    for x, y in [(155, 370), (600, 470), (320, 730), (560, 820), (200, 995)]:
        draw.ellipse((x - 10, y - 10, x + 10, y + 10), fill="#6A9B84")
        draw.ellipse((x - 4, y - 4, x + 4, y + 4), fill="#FFFFFF")

    draw.ellipse((400, 365, 430, 395), fill="#F27760")
    draw.ellipse((408, 373, 422, 387), fill="#FFFFFF")
    draw.ellipse((413, 378, 417, 382), fill="#F27760")

    draw.rounded_rectangle((45, 40, 735, 130), radius=32, fill="#FFFFFF", outline=road, width=3)
    draw.ellipse((73, 66, 103, 96), outline="#9A9A96", width=4)
    draw.line((97, 92, 116, 111), fill="#9A9A96", width=4)
    draw.rounded_rectangle((665, 160, 735, 235), radius=22, fill="#FFFFFF", outline=road, width=3)
    draw.ellipse((685, 180, 715, 210), outline="#789085", width=4)

    draw.rounded_rectangle((25, BOTTOM_CARD_TOP, 755, 1360), radius=34, fill="#FFFFFF", outline=road, width=3)
    draw.rounded_rectangle((65, 1175, 405, 1202), radius=14, fill="#E6E2DC")
    draw.rounded_rectangle((65, 1220, 610, 1247), radius=14, fill="#EEECE8")
    draw.rounded_rectangle((520, 1285, 700, 1332), radius=24, fill="#F27760")
    return image


def build(source: Path, output_dir: Path, slug: str, corner: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    master, bounds = normalize(source)
    master_path = output_dir / f"{slug}_character_transparent.png"
    master.save(master_path, "PNG", optimize=True)

    detail = Image.new("RGB", (CANVAS, CANVAS), "#FFFFFF")
    detail.paste(master, mask=master.getchannel("A"))
    detail.save(output_dir / f"{slug}_character_detail.png", "PNG", optimize=True)

    left, top, right, bottom = bounds
    content_bounds = {
        "asset": master_path.name,
        "canvas": {"width": CANVAS, "height": CANVAS},
        "contentBounds": {"x": left, "y": top, "width": right - left, "height": bottom - top},
        "CHARACTER_VISIBLE_BOUNDS": "PASS",
    }
    (output_dir / f"{slug}_content_bounds.json").write_text(
        json.dumps(content_bounds, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    viewport = draw_map_background()
    art = master.crop(bounds)
    target_width = round(VIEWPORT[0] * WIDTH_RATIO)
    ratio = target_width / art.width
    art = art.resize((target_width, round(art.height * ratio)), Image.Resampling.LANCZOS)

    if corner.endswith("right"):
        x = VIEWPORT[0] - SAFE_INSET - art.width
    else:
        x = SAFE_INSET
    if corner.startswith("bottom"):
        y = BOTTOM_CARD_TOP - SAFE_INSET - art.height
    else:
        y = 155
    viewport.paste(art, (x, y), art)
    preview_path = output_dir / f"{slug}_map_scale_14.png"
    viewport.save(preview_path, "PNG", optimize=True)

    preview_manifest = {
        "asset": master_path.name,
        "preview": preview_path.name,
        "viewport": {"width": VIEWPORT[0], "height": VIEWPORT[1]},
        "corner": corner,
        "characterViewportWidthRatio": WIDTH_RATIO,
        "visibleCharacterWidthPx": target_width,
        "viewportSafeMarginPx": SAFE_INSET,
        "viewportFixed": True,
        "mapZoomIndependent": True,
        "interaction": "none",
        "pointerEvents": "none",
        "fallback": "hidden",
    }
    (output_dir / f"{slug}_map_scale_14.json").write_text(
        json.dumps(preview_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument(
        "--corner",
        choices=["top-left", "top-right", "bottom-left", "bottom-right"],
        default="bottom-right",
    )
    args = parser.parse_args()
    build(args.source, args.output_dir, args.slug, args.corner)


if __name__ == "__main__":
    main()
