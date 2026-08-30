# City Guide Character Prompt Template v0.1

Fill every bracket. Keep the shared style lock verbatim across attraction and character prompts.

```text
ASSET STATUS:
CITY CHARACTER STYLE TEST — NOT A PRODUCTION ASSET

ASSET:
City: [CITY_NAME]
Character role: lightweight corner guide for a travel sticker map
Candidate: [CANDIDATE_ID]

REFERENCE ROLES:
- Images [A...] are approved STYLE_REFERENCE version [STYLE_VERSION]. Use them for pen texture, line weight, wobble, open gaps, flat-fill behavior, saturation, negative space, border, shadow, simplification, and approved character proportion only.
- Images [B...] are CITY_CUE_REFERENCE. Use them only to verify [EXACT CUE]. Do not copy people, brands, text, clothing identity, architecture, or photographic composition.
- Image [C], if supplied, is MAP_LAYOUT_REFERENCE. Use it only to plan scale and corner fit; do not render the map into the transparent character master.

ORIGINAL CHARACTER LOCK:
Create one original fictional young traveler. Do not reproduce a real person or a character from any reference. [BASE CHARACTER VERSION: exact approved face simplification, head/body ratio, hairstyle family, default outfit geometry, palette roles, and fixed traits.]

SHARED STYLE LOCK [STYLE_VERSION] — COPY VERBATIM FROM ATTRACTION SYSTEM:
[APPROVED SHARED STYLE LOCK]

CITY_CHARACTER_MANIFEST:
City: [EXACT CITY]
City type: [RESEARCHED TYPE]
Temperament: [PRIMARY CITY-CHARACTER FEELING]
Visual keywords: [THREE TO FIVE]
Hairstyle: [SILHOUETTE DIRECTION]
Outfit style: [MODERN DAILY DIRECTION]
Primary colors: [TWO TO FOUR SOFTENED RESEARCHED COLORS]
Accent color: [ONE OR NONE]
Pose tendency: [ONE SIMPLE TRAVEL BEHAVIOR]
Prop: [ONE MAIN PROP OR NONE]
Local feature: [ZERO TO TWO VERIFIED LIGHTWEIGHT DETAILS]
Avoid: [EXACT COMPLEXITY / CLICHÉ / STEREOTYPE RISKS]
Map role: MAP_VIEWPORT_OVERLAY
Style version: [SHARED STYLE VERSION]

Express three to five coordinated character differences while preserving the shared visual system. Temperament leads and appearance supports it. Do not clone another city character by recoloring it, and do not drift into a different art system.

POSE:
[ONE SIMPLE ACTION: read map / gentle point / face reader / sit / light wave / hold camera or small bag]. Keep the silhouette calm and compact. At most one main prop.

COMPOSITION:
Exact 1:1, 1024×1024 transparent PNG master. Complete character visible with approved safe margin and measurable alpha bounds. No crop, scenery, map, corner panel, text, or UI. The character will later be displayed as a viewport-fixed corner overlay whose visible width defaults to 14% of the map viewport.

VISUAL HIERARCHY:
Lightweight supporting decoration, lower detail and visual force than selected attraction markers. No dramatic gesture, high-contrast aura, oversized prop, dense clothing detail, or central-hero presentation.

APPEAL:
CUTE, PRETTY, GENTLE, FRIENDLY, LIGHTWEIGHT, CLEAN, SOFT. Use compact Q-style proportions, simple black handmade lines, small facial features, and soft color blocks. Avoid generic blandness, glossy commercial mascot polish, preschool exaggeration, realism, or heavy visual information.

PEN STYLE LOCK:
CHARACTER_PEN_STYLE_LOCK = true. Preserve non-mechanical hand-drawn pen lines, restrained natural wobble, rare light secondary-contour breaks, slight naive asymmetry, soft flat fills, optional tiny registration drift, and travel-sketch whitespace. Do not increase appeal through commercial-vector smoothness, complex shading, glossy highlights, 3D, or extra facial detail.

BODY SYSTEM:
Use the shared 4–4.5-head compact Q-style family, common hand/foot simplification, eye scale, nose/mouth reduction, face grammar, and limb line language.

STICKER EDGE:
[EXACT APPROVED WHITE BORDER DECISION]

SHADOW:
[EXACT APPROVED SHADOW DECISION]

TEXT:
NONE. Do not add a city name, caption, map labels, signage, logo, watermark, or invented letters.

BACKGROUND:
Genuine transparency. No white square, checkerboard drawing, map screenshot, skyline, landmark collage, room, street, or decorative scene.

OUTPUT:
One candidate only. No turnaround, expression sheet, multiple outfits, animation frame, contact sheet, mockup, or automatic city batch.
```

## Targeted repair: too dominant

```text
Preserve identity and shared style. Reduce only visual dominance: simplify secondary clothing/prop detail, lower the city accent contrast, calm the gesture, and preserve generous transparent margin. Do not make the line or fill style weaker than the attraction set.
```

## Targeted repair: style mismatch

```text
Preserve the accepted pose and city cue. Restore the exact shared [STYLE_VERSION] line weight, wobble, open-gap pattern, flat-fill registration, saturation, white border, and shadow. Do not change base-character proportions or add detail.
```

## Targeted repair: map collision

```text
Do not redraw the character master. Update only placement: try [ALTERNATE CORNER], then approved reduced scale. If either still overlaps markers or controls, set visible=false.
```
