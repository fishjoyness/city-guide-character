#!/usr/bin/env python3
"""Build the four-character horizontal pose-review showcase."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH, HEIGHT = 2400, 900
CARD_W, CARD_H = 540, 770
GAP = 38
LEFT = 63
TOP = 65

CHARACTERS = [
    ("上海 · SHANGHAI", "SLIGHT_LEFT · CAMERA_ACTION · WEIGHT_RIGHT", "shanghai/shanghai_character_transparent.png"),
    ("桂林 · GUILIN", "FRONT · WALKING_READY · ONE FOOT LEADS", "guilin/guilin_character_transparent.png"),
    ("南京 · NANJING", "THREE_QUARTER_RIGHT · CASUAL_GUIDE · WEIGHT_LEFT", "nanjing/nanjing_character_transparent.png"),
    ("北京 · BEIJING", "THREE_QUARTER_LEFT · POCKET · SLIGHT_OPEN", "beijing/beijing_character_transparent.png"),
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = "msyhbd.ttc" if bold else "msyh.ttc"
    return ImageFont.truetype(str(Path("C:/Windows/Fonts") / name), size)


def alpha_crop(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    bounds = rgba.getchannel("A").getbbox()
    if not bounds:
        raise ValueError("character has no visible alpha")
    return rgba.crop(bounds)


def build(examples_dir: Path, output: Path) -> None:
    canvas = Image.new("RGB", (WIDTH, HEIGHT), "#F3EFE8")
    draw = ImageDraw.Draw(canvas)
    title_font = font(26, True)
    note_font = font(16)

    for index, (title, note, relative) in enumerate(CHARACTERS):
        x = LEFT + index * (CARD_W + GAP)
        draw.rounded_rectangle((x, TOP, x + CARD_W, TOP + CARD_H), radius=34, fill="#FFFEFB", outline="#D8D0C5", width=3)
        draw.text((x + 28, TOP + 24), title, fill="#292723", font=title_font)
        draw.text((x + 28, TOP + 65), note, fill="#777067", font=note_font)

        art = alpha_crop(Image.open(examples_dir / relative))
        max_w, max_h = 430, 620
        ratio = min(max_w / art.width, max_h / art.height)
        art = art.resize((round(art.width * ratio), round(art.height * ratio)), Image.Resampling.LANCZOS)
        art_x = x + (CARD_W - art.width) // 2
        art_y = TOP + 115 + (620 - art.height) // 2
        canvas.paste(art, (art_x, art_y), art)

    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, "PNG", optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--examples-dir", type=Path, default=Path("examples"))
    parser.add_argument("--output", type=Path, default=Path("examples/character-system-showcase.png"))
    args = parser.parse_args()
    build(args.examples_dir, args.output)


if __name__ == "__main__":
    main()
