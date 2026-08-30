# 重庆 — 城市导览人物

状态：PRODUCTION V1  
研究访问日期：2026-08-30

```yaml
city: 重庆
cityType: vertical-river-metropolis
temperament: 干练、热情、熟悉立体交通、步伐稳健
visualKeywords: [立体交通, 两江交汇, 山城步道, 当代都市, 工业层次]
hairstyle: 短卷发配干净渐层侧边，年轻男性，头部轮廓紧凑
outfitStyle: 当代山城通勤旅行；深蓝灰轻量技术夹克、浅灰内搭、暖棕直筒长裤
primaryColors: [深蓝灰, 江水灰蓝, 暖棕, 浅灰]
accentColor: 交通卡使用少量低饱和红
poseTendency: 一手在肩侧举起小型交通卡，另一手自然垂下，身体微转并左腿承重
prop: 小型交通卡
poseSignature:
  faceOrientation: THREE_QUARTER_RIGHT
  bodyOrientation: SLIGHT_LEFT
  gestureFamily: ONE_HAND_HOLD
  leftHand: 在左肩侧单手举起小型交通卡
  rightHand: 在身体右侧自然下垂
  handPoseSignature: left-transit-card-near-shoulder + right-relaxed-down
  stance: WEIGHT_LEFT
  weightDistribution: left
  footwear: ankle-boots
  silhouetteNote: 紧凑短卷发、单侧抬手、技术夹克与短靴形成偏纵向的山城通勤剪影
localFeature: [江水灰蓝和工业深色体现两江与立体都市, 暖棕平衡硬质城市材料, 交通卡互动呼应公共交通但不使用地标贴身]
avoid: [火锅道具, 轻轨贴在人身上, 洪崖洞轮廓服饰, 双手胸前拿物, 与成都指路姿态重复]
mapRole: MAP_VIEWPORT_OVERLAY
styleVersion: pen-travel-v0.2
```

## 研究依据

- 重庆官方文旅线路持续强调山城步道、索道、轨道交通、两江和多层城市空间。
- 人物采用现代公共交通向导身份，不使用火锅或民俗刻板标签。

## Pose QA

- `POSE_SIGNATURE_LOCKED_BEFORE_GENERATION = PASS`
- `handPoseSignature = left-transit-card-near-shoulder + right-relaxed-down`
- 单手抬卡、左腿承重和短靴组合不与现有角色重复。
