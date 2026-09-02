# City Guide Character System v0.2

This is provisional. The user-approved shared `STYLE_REFERENCE` remains the final visual authority.

## Product role

The guide character is a quiet traveling companion at the map edge. It provides warmth and city memory while attraction markers remain the first read and the only selection targets.

## Shared visual DNA with attractions

Freeze these fields in the approved travel-illustration style card. If the optional `city-sticker` Skill is also installed, use the same values in both Skills:

- `styleVersion`
- pen medium, weight family, wobble, pressure variation, and open-gap logic
- flat-fill behavior, color count logic, saturation, and optional misregistration
- overall looseness versus polish
- white-border treatment
- shadow treatment
- transparent background and no-text policy

Do not merely use similar adjectives. Copy the accepted style block verbatim.

## Character-specific lock

Add these fields without changing shared style:

```yaml
baseCharacterVersion: guide-base-v0.1
identityType: original-fictional-traveler
perceivedAge: young-adult-by-default-with-future-light-age-variation
genderPresentation: inclusive-female-male-or-gender-neutral
headToBodyRatio: 4-to-4.5-heads
faceSimplification: shared-small-feature-system-with-simple-eyes-minimal-nose-mouth
defaultOutfit: modern-light-travelwear-with-city-specific-variation
defaultTravelProps:
  - folded-map
poseComplexity: simple-subtle-diversity
cityCueLimit: 2
text: none
background: transparent
```

These system fields stay fixed across cities. City identity comes from the manifest layer, not a different anatomy or rendering grammar.

## Mandatory three-character reference check

For every image-generation call, attach `../assets/reference-character-style-20260902-no-shanghai.png` as an input-only visual calibration board. It is not optional inspiration. The Guilin, Nanjing and Beijing examples establish the exact small dot-eye construction, compact 4–4.5-head proportion, thin hand-drawn dark contour, matte low-saturation flat fill, cheek blush, whitespace and full-body visual scale. The board itself must never be regenerated, composited into, or delivered with the new city character.

Reject a candidate when it adds a new eye design, eye highlights, lashes, glossy anime features, a different outline family, a taller/shorter proportion system, or a more rendered/shaded surface. Pose, hairstyle, outfit, footwear and one prop may vary; the base drawing grammar may not.

## Provisional visual direction

- Young, relaxed, friendly, and travel-oriented.
- Q-style compact proportions, simple black hand-drawn contours, small facial features, soft flat colors, and a cute, pretty, gentle expression.
- Clean and appealing without glossy commercial mascot polish, exaggerated cartoon emotion, or a hero-poster presence.
- Rough-enough handmade contours, restrained wobble, natural pauses, and low information density.
- One calm action and at most one main prop.
- Complete silhouette, generous transparent margin, no scenery panel.
- No glossy anime, polished commercial mascot, refined 3D, vector-perfect linework, dense accessories, or dramatic lighting.

## Pen style lock

`CHARACTER_PEN_STYLE_LOCK = true`.

- Keep the shared travel-sketch pen line: non-mechanical, slightly wobbly, mildly naive, not perfectly symmetric, with rare light breaks or incomplete closure on secondary contours.
- Keep soft flat color blocks, optional tiny hand-drawn registration drift, measured whitespace, and no heavy gradients, 3D, plastic highlights, or smooth commercial-cartoon outlining.
- Character design may become prettier through better hair, outfit, palette, expression, pose, and proportion decisions. The drawing language itself does not become more polished.
- Compare beside attraction stickers. Line-weight logic, pen feel, fill texture, saturation, whitespace, handmade imperfection, and lightweight presence must remain one visual world.

## Shared body proportion

- Use a 4–4.5-head compact Q-style family for all city characters.
- Freeze hand/foot simplification, small-feature face grammar, eye scale, nose/mouth reduction, limb line language, and overall visual density.
- Allow only minor natural variation; do not use body ratio as the primary city differentiator.

## Pose grammar

- Lock face orientation independently from body orientation.
- Use `FRONT`, `SLIGHT_LEFT`, `THREE_QUARTER_LEFT`, `SLIGHT_RIGHT`, or `THREE_QUARTER_RIGHT` for the face; profile is exceptional.
- Use `FRONT`, `SLIGHT_LEFT`, or `SLIGHT_RIGHT` for the torso.
- Choose one gesture family: two-hand hold, one-hand hold, pointing, strap/bag interaction, pocket, camera action, casual guide, or walking ready.
- Choose one stance: neutral parallel, weight left/right, one foot forward, slight open, or walking ready.
- Choose contemporary footwear that supports outfit and silhouette without becoming a regional costume cue.
- Record all decisions in `poseSignature` before generation.

Avoid running, jumping, dancing, crouching, back-facing poses, extreme profiles, exaggerated reaction poses, or gestures that need motion effects. `TWO_HAND_HOLD` remains valid but must not become a repeated batch template.

## City differentiation budget

Use three to five differences per city, selected from:

1. hairstyle silhouette: length, fringe, tied/loose, curl/straight, or outer contour;
2. main palette tendency within the shared muted saturation system;
3. modern outfit language: light travel, literary, campus, urban casual, or clean light sport;
4. friendly temperament: quiet, lively, relaxed, serious, or curious/exploratory;
5. pose signature: face/body orientation, gesture family, hand interaction, stance, weight, silhouette, and footwear;
6. one main prop: camera, folded map, small guidebook, backpack, ticket/travel card, or light water bottle.

Keep the same proportion family, face grammar, line, fill, border, shadow, simplification depth, and placement system. Use no more than one main prop and at most one or two restrained city cues. The goal is a series of different roles, not one recolored character and not unrelated art styles.

Hair, prop, or pose alone never satisfies differentiation. Across comparison characters, at least three to four of face orientation, body orientation, gesture family, stance, silhouette, and footwear must visibly differ, coordinated with outfit/palette/temperament.

## City-type strategies

### Modern metropolis

Examples: Shanghai, Beijing, Shenzhen, Guangzhou, Hangzhou.

- Prefer clean contemporary styling, quieter designed palettes, natural posture, and one modern activity cue.
- Shanghai may read as refined, urban, and exhibition/photography-oriented without using the Oriental Pearl Tower as a shortcut.
- Beijing may feel composed and culturally curious through a museum/book/notebook direction while staying light and cute.

### Historical and cultural city

Examples: Nanjing, Xi'an, Luoyang, Suzhou.

- Prefer a gentle, calm, literary, museum-walk, or city-stroll temperament.
- Keep clothing modern; use color, a postcard, a map, or one small booklet rather than costume cosplay.

### Distinctive regional, ethnic, or landscape context

Examples: cities in Guizhou, Guangxi, and Yunnan.

- Research an official cultural source before selecting any regional detail.
- Translate only one or two verified cues into daily wear: a narrow pattern trim, material relationship, tiny jewelry-scale accent, restrained headwear silhouette, or palette relationship.
- Keep the role lightweight and modern. Reject ceremonial dress, dense embroidery everywhere, face typing, invented ethnic mixtures, and tourism-poster staging.

## Required design record

Every city defines:

- `city`
- `cityType`
- `temperament`
- `visualKeywords`
- `hairstyle`
- `outfitStyle`
- `primaryColors`
- `accentColor`
- `poseTendency`
- `prop`
- `poseSignature.faceOrientation`
- `poseSignature.bodyOrientation`
- `poseSignature.gestureFamily`
- `poseSignature.leftHand`
- `poseSignature.rightHand`
- `poseSignature.handPoseSignature`
- `poseSignature.stance`
- `poseSignature.weightDistribution`
- `poseSignature.footwear`
- `poseSignature.silhouetteNote`
- `localFeature`
- `avoid`
- `mapRole`
- `styleVersion`

Before filling the record, save a compact research basis: source URL, source owner, access date, supported city-temperament/color/clothing/cultural claim, and any rejected stereotype. When a local cultural detail is used, name the exact verified tradition rather than a generic regional label.

Examples are direction only, not locked stereotypes:

- Nanjing: quieter, literary/historical mood; restrained warm or ink-like accent.
- Chengdu: relaxed posture; one leisure cue.
- Xi'an: exploratory posture; one subtle historical cue without costume cosplay.
- Shanghai: cleaner urban accent; one compact modern travel prop.

Research before using a symbol. Do not cover the character with city icons or turn food, costume, dialect, ethnicity, or history into caricature.

## Reference-project translation

From人物参考图, inherit line texture, fill method, palette behavior, negative space, saturation, looseness, and shadow. For this Skill, character proportion and face simplification may also be studied only after the user approves them as the base-character anchor.

Never inherit a reference person's identity, hair, clothes, face, or signature palette by default. The guide must be an original fictional traveler.

## Set consistency

- Use the same base-character version across cities until the user approves a new family.
- Keep head/body ratio family, face-construction grammar, line, fill, border/shadow, and rendering stable.
- Allow hairstyle silhouette, outfit language, palette tendency, temperament, action, and one prop to vary within the city differentiation budget.
- Compare the city character beside two accepted attraction stickers at the same map scale.
- Reject a character that looks more saturated, detailed, polished, outlined, or dimensional than the attraction set.
- Reject `CLONE` and `SYSTEM_DRIFT`; record `CITY_CHARACTER_DIFFERENTIATION = PASS | FAIL` with comparison evidence.
- Final comparison target: `CHARACTER_DIFFERENTIATION = HIGH` and `STYLE_DIFFERENTIATION = LOW`.
- For sets of three or more, run `CROSS_CITY_POSE_REVIEW`. No exact face direction may exceed 70%; repeated chest-centered hands, parallel-leg silhouettes, generic footwear, or identical prop handling are blocking failures.
