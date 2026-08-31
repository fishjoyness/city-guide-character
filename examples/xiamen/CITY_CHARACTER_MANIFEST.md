# 厦门 — 城市导览人物

状态：ASSET LIBRARY / REVIEW
研究访问日期：2026-08-31

```yaml
city: 厦门
cityType: modern-metropolis
temperament: 轻松、亲海、开放、适合慢行
visualKeywords: [海岛步行, 骑行休闲, 近代建筑, 海风, 当代日常]
hairstyle: 草帽下的深色低发髻，帽带与发髻形成清晰侧向轮廓
outfitStyle: 现代海滨休闲；奶油色短开衫、柔和蓝绿色上衣、简洁中长 A 字裙
primaryColors: [海水青绿, 奶油白, 柔和珊瑚, 暖灰]
accentColor: 小面积珊瑚色
poseTendency: 一手调整肩带，另一手自然下垂，准备沿海步行
prop: 小型帆布托特包
poseSignature:
  faceOrientation: SLIGHT_RIGHT
  bodyOrientation: SLIGHT_LEFT
  gestureFamily: STRAP_BAG_INTERACTION
  leftHand: 扶住肩侧托特包带
  rightHand: 自然垂在身侧
  handPoseSignature: left-tote-strap + right-relaxed
  stance: WEIGHT_RIGHT
  weightDistribution: right
  footwear: simple-sandals
  silhouetteNote: 4–4.5 头身紧凑比例；草帽、肩侧包带、单侧承重与露脚踝凉鞋形成海滨步行轮廓
localFeature: [厦门文旅资料中的海岸休闲与步行/骑行行为, 海水青绿与珊瑚色的克制海滨配色]
avoid: [闽南仪式服饰泛化, 鼓浪屿建筑堆叠, 海浪道具, 食物道具, logo, 第二件道具]
mapRole: MAP_VIEWPORT_OVERLAY
styleVersion: pen-travel-v0.1
```

## 研究依据

- [厦门市文化和旅游局：文旅资源](https://wlj.xm.gov.cn/whly/)：确认城市文旅资源由官方文旅系统统一管理。
- [厦门市文化和旅游局：2024厦门暑期研学游市场热度高](https://wlj.xm.gov.cn/zwgk/bmdt/202408/t20240814_2865574.htm)：支持历史文化、科技创新与学习型城市旅行行为。
- [厦门市文化和旅游局：环东浪漫线](https://wlj.xm.gov.cn/zwgk/bmdt/202512/t20251212_2971577.htm)：支持海岸、沙滩、体育与休闲服务的当代海滨 cue。

- `CITY_RESEARCH_BEFORE_GENERATION = PASS`
- `CHARACTER_DIFFERENTIATION = HIGH`
- `STYLE_DIFFERENTIATION = LOW`
- `POSE_SIGNATURE_LOCKED_BEFORE_GENERATION = PASS`
- `USER_STYLE_REFERENCE_MATCH = PASS` — 2026-08-31 按用户确认的桂林/南京/北京人物系统定向修复。
- `PRODUCTION_CANDIDATE = xiamen_character_transparent.png` — 已提升为 v3；旧写实版与中间 v2 保存在 `recovery/`。
