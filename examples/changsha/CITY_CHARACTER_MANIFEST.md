# 长沙 — 城市导览人物

状态：IN_PROGRESS  
研究访问日期：2026-08-31

```yaml
city: 长沙
cityType: modern-metropolis
temperament: 热情、利落、年轻、兼具历史文化与当代城市活力
visualKeywords: [湘江城市漫步, 青年活力, 文博体验, 当代休闲, 轻快引导]
hairstyle: 短而略蓬松的自然碎发，形成轻快不对称轮廓
outfitStyle: 现代城市轻旅行；短夹克、简洁内搭、九分直筒裤
primaryColors: [米白, 炭灰, 柔和橙红, 灰绿色]
accentColor: 小面积柔和橙红
poseTendency: 一手持折叠路线卡垂在身侧，另一手向地图方向轻点
prop: 折叠路线卡
poseSignature:
  faceOrientation: THREE_QUARTER_LEFT
  bodyOrientation: SLIGHT_LEFT
  gestureFamily: POINTING
  leftHand: 折叠路线卡自然垂在左腿外侧
  rightHand: 轻抬并向外侧做小幅指引动作
  handPoseSignature: left-route-card-down + right-gentle-point
  stance: ONE_FOOT_FORWARD
  weightDistribution: left
  footwear: retro-sneakers
  silhouetteNote: 短夹克、外侧指引手、下垂路线卡与右脚微向前形成开阔斜向轮廓
localFeature: [NONE]
avoid: [辣椒或食物道具, 霓虹夜店符号, 城市名称文字, 湘绣元素臆造, 历史服装, 第二件道具]
mapRole: MAP_VIEWPORT_OVERLAY
styleVersion: pen-travel-v0.1
```

## 研究依据

- [湖南省文化和旅游厅：长沙端午文旅线路](https://whhlyt.hunan.gov.cn/whhlyt/news/sxxw/202505/t20250529_33686252.html)：支持历史文化、文博艺术、青年休闲与山水城市漫步并存的城市气质。
- [湖南省文化和旅游厅：长沙文旅香港推广](https://whhlyt.hunan.gov.cn/whhlyt/news/sxxw/202409/t20240926_33463331.html)：支持传统与现代、文化与潮流并置的当代城市体验。
- [湖南省文化和旅游厅：长沙文旅新玩法](https://whhlyt.hunan.gov.cn/whhlyt/news/sxxw/202409/t20240926_33463338.html)：支持湘江、岳麓山、橘子洲、文化园区与步行街串联的城市旅行行为。

- `CITY_RESEARCH_BEFORE_GENERATION = PASS`
- `CHARACTER_PEN_STYLE_LOCK = true`
- `POSE_SIGNATURE_LOCKED_BEFORE_GENERATION = PASS`
