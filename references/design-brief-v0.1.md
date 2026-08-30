# City Guide Character Skill Brief v0.1

## Qualification

- Decision: **A — Create one separate Skill**.
- Evidence: guide characters and attraction stickers have different inputs, outputs, failure modes, and definitions of done. Character generation needs pose/proportion and placement rules; landmark generation needs factual-appearance research.
- Existing Skill overlap: `ip-illustration-character-system` supplies useful anchor and consistency methods but is a broad personal-IP system with eleven output routes.
- Recommendation: make a narrow, independently written adaptation. Do not vendor the reference repository's files or images; its repository currently exposes no explicit license file.

## Core contract

When a city map needs warmth without losing usability, this Skill helps the product owner design one optional corner guide character that shares the attraction-sticker style and can be hidden safely.

## Why two Skills

| Concern | `city-sticker` | `city-guide-character` |
|---|---|---|
| Primary subject | Real landmark or landscape | Original lightweight traveler |
| Truth source | Official landmark imagery | Shared style lock + restrained city cues |
| Key fidelity | Silhouette and structures | Proportions, face, outfit, pose |
| Product role | Selectable POI marker | Decorative corner atmosphere |
| Interaction | Tap target | Non-interactive |
| Failure fallback | Generic marker later | Hide silently |

The two Skills share a `styleVersion`, not one oversized workflow.

## Adaptation from the reference character Skill

### Keep

- Distinguish user instructions, identity/content references, style references, and layout references.
- Freeze one accepted anchor and repeat a compact lock.
- Use the smallest reference set in fixed order.
- Plan a manifest before generating.
- Validate geometry, identity/style, content, and output constraints in order.
- Keep passing outputs and repair one failed dimension at a time.

### Remove

- User-photo identity transfer, face/hair fidelity to a real person, pets, species anatomy, and personal signature outfit.
- Eleven asset routes, turnaround sheets, expression packs, memes, stationery, photo fusion, and animation-like complexity.
- Large central character composition and reactions designed to dominate a chat thumbnail.
- Automatic themed costumes and high-density props.

### Add

- One original neutral traveler per city.
- One shared visual DNA with the attraction system.
- Zero to two light city cues.
- Four-corner placement, collision avoidance, scale limit, non-interactive behavior, and hidden fallback.
- Map-composite QA where the character must lose visual competition against selected attraction markers.

## Scope

### IN SCOPE

- One character concept per city.
- Simple pose and travel prop.
- City mood adjustment with evidence.
- Review-only prompt/candidate package.
- Placement/data/resource contract.

### OUT OF SCOPE

- Personal IP, story universe, dialogue, animation, multiple outfits, complex city personification.
- Production runtime code in v0.1.
- Bulk city character generation.

## Representative requests

1. “为南京设计一个右上角看地图的轻量导览角色，只出 Prompt。”
2. “沿用景点 style-v1，做一个成都城市人物 STYLE TEST。”
3. “检查这个人物是否挡住景点、是否比 Marker 更抢眼。”

## Open decisions for review

- Whether all cities share one base character or use a controlled family of base silhouettes.
- Default perceived age range and gender presentation.
- Head-to-body ratio and face simplification.
- Default outfit and allowable seasonal variation.
- White border and shadow treatment.
- Maximum displayed map width/height and scale range.
- Default corner priority and responsive breakpoints.
- Whether the guide is always non-interactive or may later open a city overview.
