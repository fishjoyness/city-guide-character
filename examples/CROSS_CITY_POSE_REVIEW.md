# Cross-City Pose Review — Shanghai / Guilin / Nanjing / Beijing

Status: **PASS**  
Review date: 2026-08-30  
Showcase: [character-system-showcase.png](character-system-showcase.png)

## Why the previous set failed

The previous characters shared the same first-read template: mostly right-facing faces, front torsos, hands clustered around a chest-level prop, parallel upright legs, and minimally differentiated flat shoes. Hair, outfit, palette, and held object changed, but the body silhouette and prop interaction did not. Therefore `SAME_SYSTEM_DIFFERENT_CHARACTER = FAIL` and repeated `both-hands-center-hold` caused `POSE_REPETITION = FAIL`.

## Locked signatures

| City | Face / body | Gesture and hand signature | Stance | Footwear |
|---|---|---|---|---|
| Shanghai | `SLIGHT_LEFT` / `SLIGHT_RIGHT` | `CAMERA_ACTION`; strap adjustment + camera at hip | `WEIGHT_RIGHT` | simple flats |
| Guilin | `FRONT` / `SLIGHT_LEFT` | `WALKING_READY`; notebook at side + relaxed arm swing | `WALKING_READY` | walking shoes |
| Nanjing | `THREE_QUARTER_RIGHT` / `FRONT` | `CASUAL_GUIDE`; booklet at side + open guide gesture | `WEIGHT_LEFT` | Mary Jane |
| Beijing | `THREE_QUARTER_LEFT` / `SLIGHT_RIGHT` | `POCKET`; notebook at side + pocket hand | `SLIGHT_OPEN` | casual leather shoes |

## Blocking review

- `FACE_DIRECTION_DIVERSITY = PASS` — four distinct face directions; highest exact-direction share is 25%.
- `GESTURE_DIVERSITY = PASS` — no `both-hands-center-hold`; all four hand signatures differ.
- `STANCE_DIVERSITY = PASS` — right-weighted, walking-ready, left-weighted, and slight-open silhouettes are distinct.
- `FOOTWEAR_DIVERSITY = PASS` — flats, walking shoes, Mary Jane, and casual leather shoes remain readable at detail scale.
- `SILHOUETTE_DIVERSITY = PASS` — camera-side asymmetry, leading foot, open guide arm, and pocket/open stance remain distinct in the horizontal review.
- `PROP_INTERACTION_DIVERSITY = PASS` — camera adjusted/carried, notebook carried while walking, booklet paired with guiding, and notebook paired with pocket hand.
- `SAME_SYSTEM_DIFFERENT_CHARACTER = PASS` — proportions, face grammar, pen system, fill behavior, and visual weight remain shared while pose silhouettes differ.
- `POSE_REPETITION = PASS` — no repeated chest-centered two-hand hold.

## Map-scale review

All four 14% previews retain the intended low-occupancy role. The walking lead, guide hand, side-carried props, and asymmetric arm positions remain distinguishable without competing with map controls.

