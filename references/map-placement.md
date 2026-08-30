# Map Placement Rules

## Visual hierarchy

1. Selected attraction marker.
2. Unselected attraction marker.
3. Map controls and route interaction.
4. City guide character.
5. Decorative map texture.

The guide is not a tap target and must not teach the interface unless a future product requirement explicitly changes that role.

## Supported corners

- `top-left`
- `top-right`
- `bottom-left`
- `bottom-right`

Do not default to map center. Select a corner from actual layout occupancy, not city identity.

## Exclusion zones

Treat these as unavailable:

- navigation bar, back control, title, and safe-area inset
- zoom/location/layer controls and platform logo/attribution
- bottom action sheet, selected-count bar, or main CTA
- dense attraction clusters and expanded callouts
- current selected marker and its tap halo
- system gesture areas and rounded-screen cutouts

## Placement decision

Use this sequence:

1. Try the configured preferred corner.
2. Try the best alternate corner.
3. Reduce scale within the approved range.
4. Hide with `visible: false`.

Never move attraction markers to make room for the character.

## Scale and placement limits

These are the finished v0.1 rules:

- Primary scale field: `characterViewportWidthRatio`.
- Default: `0.14`; normal range: `0.12–0.16`; hard minimum: `0.10`; hard maximum: `0.18`.
- Compute the displayed width from the visible character alpha/content bounds. Transparent canvas padding does not count.
- The ratio tracks visible map viewport width. It is independent of latitude/longitude, map zoom, marker size, and PNG source pixels.
- At a 390px viewport, the default visible width is about 55px. A 2–2.5 height/width character will appear about 110–140px tall.
- The character must remain visually weaker than selected markers, unselected markers, attraction stickers, routes, and expanded callouts.
- Maintain a clear inset from screen and control boundaries.
- Keep the character non-interactive (`pointer-events: none` or equivalent future implementation).
- Render below interactive marker/callout layers.
- When a marker/callout, route, search entry, bottom card, map control, or safe-area exclusion overlaps: try the configured preferred corner, then alternate corners, then multiply the current ratio by `0.85`, continue no lower than `0.10`, then set `visible: false`.
- When the bottom card expands, treat both bottom corners as unavailable if its collision box reaches them.
- Never move, hide, shrink, or de-prioritize an attraction marker to preserve the character.

Do not exceed `0.18`, even on an empty map.

## Visible bounds

- Derive `visibleAlphaBounds` from pixels whose alpha exceeds the agreed visibility threshold, or read a validated `contentBounds` stored beside the production asset.
- Store bounds in source-image pixel coordinates as `{ x, y, width, height }`.
- Calculate the rendered image-box size so that the bounds width, not the full canvas width, equals `viewportWidth × characterViewportWidthRatio`.
- Record `CHARACTER_VISIBLE_BOUNDS = PASS | FAIL`. Missing, stale, or out-of-range bounds fail asset handoff.

## Placement manifest

```json
{
  "cityId": "nanjing",
  "position": "top-right",
  "characterViewportWidthRatio": 0.14,
  "visible": true,
  "preferredCorners": ["top-right", "bottom-left"],
  "avoidZones": ["top-navigation", "map-controls", "marker-clusters", "bottom-sheet"],
  "interaction": "none",
  "pointerEvents": "none",
  "fallback": "hidden"
}
```

## QA preview

Test at minimum:

- default city overview zoom
- one zoomed-in dense marker area
- one selected marker with callout
- bottom sheet collapsed and expanded
- narrow/short device viewport

The preview may composite the character temporarily over a map screenshot. Do not ship the screenshot or bake the map into the character PNG.
