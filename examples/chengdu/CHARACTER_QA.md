# Chengdu Character QA

- Manifest and city research: PASS
- `POSE_SIGNATURE` locked before generation: PASS
- First candidate: FAIL — face pointed left instead of locked `SLIGHT_RIGHT`
- Targeted orientation repair: PASS — face right, torso subtly left, pointing hand remains left
- Gesture diversity: PASS — directional point + phone at hip
- Stance diversity: PASS — right-leg weight
- Footwear diversity: PASS — retro sneakers
- 1024 × 1024 RGBA, alpha, safe margin, detail, and 14% map preview: PASS
- Cross-city pose review: PASS against current formal set / final 30-city review pending

`handPoseSignature = left-directional-point + right-phone-at-hip`
