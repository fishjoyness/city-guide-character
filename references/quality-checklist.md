# City Guide Character Quality Checklist

## Output integrity — critical

- [ ] Exact 1024×1024 transparent PNG master.
- [ ] Complete character and props are visible; no crop.
- [ ] Safe margin and footprint match the shared style lock.
- [ ] `CHARACTER_VISIBLE_BOUNDS = PASS`: visible alpha/content bounds are recorded and valid; transparent canvas padding is excluded from scale calculations.
- [ ] No map, scenery, text, logo, watermark, UI, or extra character.
- [ ] Status is `CITY CHARACTER STYLE TEST` until approved.

## Shared visual system — critical

Compare beside at least two accepted attraction stickers:

- [ ] Same `styleVersion` and ordered style references.
- [ ] Same pen weight family, wobble, open-gap logic, and polish level.
- [ ] Same flat-fill behavior, saturation range, border, and shadow.
- [ ] Similar simplification depth and hand-drawn looseness.
- [ ] Character does not look glossier, more 3D, more vector-like, more refined, or more saturated than attractions.
- [ ] `CHARACTER_PEN_STYLE_LOCK = true`: light wobble, rare secondary breaks, naive asymmetry, soft fills, and travel-sketch whitespace remain visible.
- [ ] `STICKER_CHARACTER_STYLE_COHERENCE = PASS` beside attraction art at equivalent scale.

## Character design

- [ ] Original fictional traveler; no copied real or reference person.
- [ ] Young, relaxed, friendly, and travel-oriented without becoming childish.
- [ ] One simple pose with at most one main prop.
- [ ] Base proportions, face simplification, outfit, and palette follow the frozen character lock.
- [ ] Body remains inside the shared 4–4.5-head family with common face, hand/foot, and limb simplification.
- [ ] Character is cute, pretty, gentle, clean, soft, and appealing without becoming glossy, exaggerated, or visually dominant.
- [ ] No complex gesture, expression-pack exaggeration, animation pose, costume overload, or scene narrative.

## City cues — critical

- [ ] `CITY_RESEARCH_BEFORE_GENERATION = PASS`: city temperament, contemporary visual culture, color basis, and any local detail were researched before prompting.
- [ ] Research notes include source URL, owner, access date, and the exact design claim supported.
- [ ] All `CITY_CHARACTER_MANIFEST` fields are complete before generation.
- [ ] Three to five coordinated differences are visible across temperament, hairstyle, outfit, palette, pose, prop, local detail, or travel behavior.
- [ ] `CHARACTER_DIFFERENTIATION = HIGH` and `STYLE_DIFFERENTIATION = LOW` in side-by-side comparison.
- [ ] Any factual cue has a source and is visually restrained.
- [ ] No ethnic, regional, historical, food, fashion, or dialect stereotype.
- [ ] No unlicensed brand, logo, copied uniform, or public-figure likeness.
- [ ] Removing the cue still leaves a coherent guide character.
- [ ] `LOCAL_FEATURE_INTEGRATION = PASS`: no more than two researched regional cues are naturally integrated into a lightweight modern character.
- [ ] `STEREOTYPE_RISK_CONTROL = PASS`: no ceremonial-costume overload, face typing, caricature, invented mixture, or tourism-poster staging.

## Map placement — critical

- [ ] Character is in one supported corner, never the map center.
- [ ] Navigation, map controls, POI markers, callouts, bottom sheet, CTA, and gesture areas remain clear.
- [ ] Character is visually weaker than selected and unselected attraction markers.
- [ ] Character is non-interactive and rendered below marker/callout layers in the future policy.
- [ ] Width uses `characterViewportWidthRatio` with default `0.14`, normal `0.12–0.16`, hard limits `0.10–0.18`, and collision factor `0.85`.
- [ ] Pan and zoom leave the character fixed in the same viewport corner and at the same screen size.
- [ ] Overview, dense zoom, selected marker, expanded sheet, and narrow-device previews were checked.
- [ ] If no corner is safe, configuration uses `visible: false` without UI warning.

## QA record

```markdown
# QA — <city guide candidate>

- Status: CITY CHARACTER STYLE TEST
- PNG/alpha: PASS | FAIL — evidence
- Shared style: PASS | FAIL — comparison evidence
- Base character: PASS | FAIL — lock evidence
- City cues: PASS | FAIL — source and restraint evidence
- City research before generation: PASS | FAIL — source manifest evidence
- CITY_CHARACTER_DIFFERENTIATION: PASS | FAIL — city-specific differences plus retained system traits
- Visual hierarchy: PASS | FAIL — map preview evidence
- Preferred corner: <corner | NONE>
- Alternate corner: <corner | NONE>
- Reduced scale tested: <value | NOT APPLICABLE>
- Final visibility: true | false
- Blocking issue: NONE | exact issue
- Next action: ACCEPT FOR REVIEW | TARGETED REPAIR | HIDE | NEED USER DECISION
```

Do not pass a visually attractive character that obstructs selection or no longer looks like the attraction set.
