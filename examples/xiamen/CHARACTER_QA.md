# Xiamen Character QA — repaired v3

Status: PASS

- Transparent full-body PNG and 14% map preview regenerated after user style review.
- Pose signature locked before generation: slight-right face, slight-left body, tote-strap interaction, right-weight stance and simple sandals.
- Technical inspect PASS: 1024×1024 RGBA PNG, transparent background, 10%+ safe margins, footprint under 80%.
- City research before generation PASS; modern coastal cue avoids costume and landmark personification.
- User style-reference match PASS: compact 4–4.5-head Q-style proportion, rounded small-feature face, simplified modern outfit, dark hand-drawn contour and soft flat fills now match the approved Guilin/Nanjing/Beijing character family.
- Character differentiation PASS; straw-hat/low-bun silhouette, shoulder-bag interaction and asymmetrical weight are distinct from existing city poses without leaving the shared system.
- `CHARACTER_VISIBLE_BOUNDS = PASS`
- `STICKER_CHARACTER_STYLE_COHERENCE = PASS` — shared pen/flat-fill language retained.
- `POSE_SIGNATURE_MATCH = PASS`
- `SAME_SYSTEM_DIFFERENT_CHARACTER = PASS` — approved by user on 2026-08-31.
- Legacy watercolor-fashion v1 and intermediate v2 are `OLD_OR_TEMP` under `recovery/`; they are excluded from production counts.
