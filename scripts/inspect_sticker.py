#!/usr/bin/env python3
"""Inspect a transparent landmark-sticker PNG and create a review thumbnail."""

from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check a 1024px transparent sticker master and report visible bounds."
    )
    parser.add_argument("--input", type=Path)
    parser.add_argument("--thumbnail", type=Path)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--canvas-size", type=int, default=1024)
    parser.add_argument("--thumbnail-size", type=int, default=128)
    parser.add_argument("--min-safe-margin", type=float, default=0.10)
    parser.add_argument("--max-footprint", type=float, default=0.80)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if not args.self_test and not args.input:
        parser.error("--input is required unless --self-test is used")
    return args


def inspect_image(
    input_path: Path,
    canvas_size: int,
    min_safe_margin: float,
    max_footprint: float,
) -> tuple[Image.Image, dict]:
    if input_path.suffix.lower() != ".png":
        raise SystemExit("input must be a PNG file")
    if not input_path.is_file():
        raise SystemExit(f"input not found: {input_path}")
    if not 0 <= min_safe_margin < 0.5:
        raise SystemExit("min-safe-margin must be between 0 and 0.5")
    if not 0 < max_footprint <= 1:
        raise SystemExit("max-footprint must be between 0 and 1")

    source = Image.open(input_path)
    has_alpha = "A" in source.getbands() or "transparency" in source.info
    image = source.convert("RGBA")
    alpha = image.getchannel("A")
    bbox = alpha.getbbox()

    checks: dict[str, dict[str, object]] = {
        "format": {"pass": source.format == "PNG", "actual": source.format},
        "canvas": {
            "pass": image.size == (canvas_size, canvas_size),
            "actual": list(image.size),
            "expected": [canvas_size, canvas_size],
        },
        "alpha_channel": {"pass": has_alpha, "actual": list(source.getbands())},
        "visible_pixels": {"pass": bbox is not None, "actual": list(bbox) if bbox else None},
    }

    margins = None
    footprint = None
    if bbox:
        left, top, right, bottom = bbox
        width, height = image.size
        margins = {
            "left": left / width,
            "top": top / height,
            "right": (width - right) / width,
            "bottom": (height - bottom) / height,
        }
        footprint = {"width": (right - left) / width, "height": (bottom - top) / height}
        checks["safe_margin"] = {
            "pass": min(margins.values()) >= min_safe_margin,
            "actual": margins,
            "minimum": min_safe_margin,
        }
        checks["footprint"] = {
            "pass": max(footprint.values()) <= max_footprint,
            "actual": footprint,
            "maximum": max_footprint,
        }
    else:
        checks["safe_margin"] = {"pass": False, "actual": None, "minimum": min_safe_margin}
        checks["footprint"] = {"pass": False, "actual": None, "maximum": max_footprint}

    alpha_extrema = alpha.getextrema()
    checks["transparent_background"] = {
        "pass": has_alpha and alpha_extrema[0] == 0,
        "actual_alpha_range": list(alpha_extrema),
    }

    report = {
        "input": str(input_path.resolve()),
        "status": "PASS" if all(bool(item["pass"]) for item in checks.values()) else "FAIL",
        "checks": checks,
        "visibleBounds": list(bbox) if bbox else None,
        "margins": margins,
        "footprint": footprint,
        "semanticChecksRequired": [
            "character and landmark sticker style coherence",
            "four to four-and-a-half head body proportion",
            "city character differentiation",
            "fourteen-percent map-scale recognizability",
            "absence of background and text",
        ],
    }
    return image, report


def save_outputs(
    image: Image.Image,
    report: dict,
    thumbnail_path: Path | None,
    report_path: Path | None,
    thumbnail_size: int,
) -> None:
    if thumbnail_size <= 0:
        raise SystemExit("thumbnail-size must be positive")
    if thumbnail_path:
        thumbnail_path.parent.mkdir(parents=True, exist_ok=True)
        thumb = image.copy()
        thumb.thumbnail((thumbnail_size, thumbnail_size), Image.Resampling.LANCZOS)
        canvas = Image.new("RGBA", (thumbnail_size, thumbnail_size), (0, 0, 0, 0))
        position = ((thumbnail_size - thumb.width) // 2, (thumbnail_size - thumb.height) // 2)
        canvas.alpha_composite(thumb, dest=position)
        canvas.save(thumbnail_path, format="PNG", optimize=True)
        report["thumbnail"] = str(thumbnail_path.resolve())
    if report_path:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def self_test() -> None:
    with tempfile.TemporaryDirectory(prefix="city-sticker-inspect-") as directory:
        root = Path(directory)
        sample = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))
        draw = ImageDraw.Draw(sample)
        draw.rounded_rectangle((160, 180, 864, 844), radius=80, fill=(74, 123, 95, 255))
        input_path = root / "sample.png"
        thumb_path = root / "sample-128.png"
        report_path = root / "sample.json"
        sample.save(input_path, format="PNG")
        image, report = inspect_image(input_path, 1024, 0.10, 0.80)
        save_outputs(image, report, thumb_path, report_path, 128)
        if report["status"] != "PASS" or not thumb_path.is_file() or not report_path.is_file():
            raise SystemExit("self-test failed")
        print("self-test passed: PNG, alpha, bounds, safe margin, footprint, thumbnail")


def main() -> None:
    args = parse_args()
    if args.self_test:
        self_test()
        return
    image, report = inspect_image(
        args.input,
        args.canvas_size,
        args.min_safe_margin,
        args.max_footprint,
    )
    save_outputs(image, report, args.thumbnail, args.report, args.thumbnail_size)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
