# Suzhou Character QA

- Manifest and city research: PASS
- `POSE_SIGNATURE` locked before generation: PASS
- First generated candidate: FAIL — face pointed to canvas right instead of locked `SLIGHT_LEFT`
- Targeted edit candidate: FAIL — face direction remained right
- Final regenerated candidate: PASS — face points toward canvas left while torso remains subtly counter-oriented
- Gesture: PASS — left hand grips shoulder strap; right hand relaxed down; no chest-centered two-hand hold
- Stance: PASS — one foot forward with asymmetric weight distribution
- Footwear: PASS — canvas-sneaker silhouette
- 1024 × 1024 RGBA and transparency: PASS
- Safe margin and visible bounds: PASS
- Character detail: PASS
- 14% map-scale preview: PASS
- Cross-city pose comparison against Beijing, Shanghai, Guilin, and Nanjing: PASS / final 30-city review pending

`handPoseSignature = left-shoulder-strap + right-relaxed-down`
