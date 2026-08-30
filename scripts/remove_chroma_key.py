#!/usr/bin/env python3
"""Remove a uniform green generation background while preserving sticker whites."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageFilter


KEY = (0, 255, 0)


def remove_key(
    source: Path,
    output: Path,
    inner: float,
    outer: float,
    min_alpha: int,
    white_fringe: bool,
    foreground_has_no_green: bool,
    edge_band: int,
) -> None:
    image = Image.open(source).convert("RGBA")
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            red, green, blue, _ = pixels[x, y]
            distance = ((red - KEY[0]) ** 2 + (green - KEY[1]) ** 2 + (blue - KEY[2]) ** 2) ** 0.5
            dominance = green - max(red, blue)
            if dominance <= 35 or distance >= outer:
                alpha = 255
            elif distance <= inner:
                alpha = 0
            else:
                alpha = round(255 * (distance - inner) / (outer - inner))

            if alpha <= min_alpha:
                alpha = 0
            elif min_alpha:
                alpha = round(255 * (alpha - min_alpha) / (255 - min_alpha))

            if 0 < alpha < 255:
                coverage = alpha / 255
                red = round(red / coverage)
                green = round((green - KEY[1] * (1 - coverage)) / coverage)
                blue = round(blue / coverage)
                red = max(0, min(255, red))
                green = max(0, min(255, green))
                blue = max(0, min(255, blue))
            pale_fringe = red > 150 and blue > 150
            if white_fringe and alpha > 0 and green > red + 8 and green > blue + 8 and (pale_fringe or foreground_has_no_green):
                red, green, blue = 255, 255, 255
            pixels[x, y] = (red, green, blue, alpha)

    if edge_band:
        alpha = image.getchannel("A")
        binary = alpha.point(lambda value: 255 if value else 0)
        eroded = binary.filter(ImageFilter.MinFilter(edge_band * 2 + 1))
        edge_pixels = image.load()
        for y in range(image.height):
            for x in range(image.width):
                if binary.getpixel((x, y)) and not eroded.getpixel((x, y)):
                    red, green, blue, alpha_value = edge_pixels[x, y]
                    if green > red + 8 and green > blue + 8:
                        edge_pixels[x, y] = (255, 255, 255, alpha_value)

    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, "PNG", optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--inner", type=float, default=18)
    parser.add_argument("--outer", type=float, default=105)
    parser.add_argument("--min-alpha", type=int, default=0, help="Drop faint generated mattes after keying (0-254).")
    parser.add_argument("--white-fringe", action="store_true", help="Neutralize residual green fringe to the sticker's white edge.")
    parser.add_argument(
        "--foreground-has-no-green",
        action="store_true",
        help="Allow full green-spill neutralization only when the character design contains no green.",
    )
    parser.add_argument(
        "--edge-band",
        type=int,
        default=0,
        help="Neutralize green spill only within this many pixels of the outer alpha edge.",
    )
    args = parser.parse_args()
    if not 0 <= args.min_alpha < 255:
        parser.error("--min-alpha must be between 0 and 254")
    if not 0 <= args.edge_band <= 32:
        parser.error("--edge-band must be between 0 and 32")
    remove_key(
        args.input,
        args.output,
        args.inner,
        args.outer,
        args.min_alpha,
        args.white_fringe,
        args.foreground_has_no_green,
        args.edge_band,
    )


if __name__ == "__main__":
    main()
