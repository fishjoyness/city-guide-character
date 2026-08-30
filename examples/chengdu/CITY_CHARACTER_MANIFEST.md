# 成都 — 城市导览人物

状态：PRODUCTION V1  
研究访问日期：2026-08-30

```yaml
city: 成都
cityType: relaxed-creative-park-city
temperament: 松弛、热情、行动感强、熟悉街巷与公园
visualKeywords: [公园城市, 街巷漫游, 当代创意, 山水门户, 日常茶馆]
hairstyle: 高度适中的短马尾配自然侧分碎发，年轻女性，轮廓利落而亲切
outfitStyle: 当代城市轻旅行；低饱和砖橙短夹克、米白内搭、深青绿色宽松长裤
primaryColors: [砖橙, 公园深绿, 米白, 炭灰]
accentColor: 手机壳使用少量雾蓝
poseTendency: 一手向侧前方做清晰但克制的指路动作，另一手在胯侧单手拿手机
prop: 手机
poseSignature:
  faceOrientation: SLIGHT_RIGHT
  bodyOrientation: SLIGHT_LEFT
  gestureFamily: POINTING
  leftHand: 在身体左侧向画面左前方轻微指路
  rightHand: 在右侧胯旁自然单手拿手机
  handPoseSignature: left-directional-point + right-phone-at-hip
  stance: WEIGHT_RIGHT
  weightDistribution: right
  footwear: retro-sneakers
  silhouetteNote: 短马尾、侧向指路手臂与宽松长裤形成横向展开的导览剪影
localFeature: [公园深绿对应成都公园城市环境, 砖橙呼应城市街巷与工业创意空间的温暖材质, 松弛但主动的指路动作]
avoid: [熊猫装饰, 川剧脸谱, 火锅道具, 民俗符号堆叠, 双手胸前拿物, 与苏州斜挎包姿态重复]
mapRole: MAP_VIEWPORT_OVERLAY
styleVersion: pen-travel-v0.2
```

## 研究依据

- 成都的代表旅行体验同时覆盖公园、街巷、现代商业、工业创意空间和都江堰—青城山山水门户，人物不使用单一熊猫或川剧标签。
- 角色以当代街巷向导身份设计，配色来自公园绿、砖墙暖色和现代日常服饰。

## Pose QA

- `POSE_SIGNATURE_LOCKED_BEFORE_GENERATION = PASS`
- `handPoseSignature = left-directional-point + right-phone-at-hip`
- 指路手势、右腿承重和复古运动鞋组合不与现有正式角色重复。
