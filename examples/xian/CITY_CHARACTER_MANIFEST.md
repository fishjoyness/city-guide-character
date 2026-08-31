# 西安 — 城市导览人物

状态：ASSET LIBRARY / REVIEW
研究访问日期：2026-08-31

```yaml
city: 西安
cityType: historical-cultural
temperament: 沉静、好奇、适合慢行观察
visualKeywords: [古都漫步, 博物馆观察, 城墙步行, 丝路起点, 当代日常]
hairstyle: 高束发髻配短飘带，轮廓与既有城市角色区分
outfitStyle: 现代轻旅行穿搭；砖红短外套、米色宽腿长裤、深靛围巾
primaryColors: [低饱和砖红, 温暖砂色, 深靛蓝, 米白]
accentColor: 围巾与发带的一小块砖红蓝色关系
poseTendency: 一手持折叠城市地图，另一手向前做温和介绍
prop: 小型折叠城市地图册
poseSignature:
  faceOrientation: THREE_QUARTER_LEFT
  bodyOrientation: SLIGHT_RIGHT
  gestureFamily: CASUAL_GUIDE
  leftHand: 低位单手持折叠地图册
  rightHand: 做温和的开掌介绍手势
  handPoseSignature: left-map-low + right-open-palm
  stance: ONE_FOOT_FORWARD
  weightDistribution: balanced-with-foot-lead
  footwear: retro-sneakers
  silhouetteNote: 左侧低位地图、右侧开掌、右脚前引形成非对称导览轮廓
localFeature: [由古城墙砖色与秦岭/丝路深蓝关系提取的克制配色, 博物馆与旧城步行行为]
avoid: [古装, 唐风 cosplay, 飞檐贴身, 兵马俑道具, 食物堆叠, 城市 logo, 第二件道具]
mapRole: MAP_VIEWPORT_OVERLAY
styleVersion: pen-travel-v0.1
```

## 研究依据

- [西安市人民政府：西安市A级旅游景区信息表](https://www.xa.gov.cn/ztzl/ztzl/lzledc/ywdc/1824366329290301442.html)：支持秦始皇帝陵博物院、城墙、陕西历史博物馆、大明宫等稳定文旅识别。
- [西安市发展和改革委员会：西安市十四五产业发展规划](https://xadrc.xa.gov.cn/xxgk/ghjh/zcqfzgh/6204d979f8fd1c0bdc7f3e4e.html)：支持“世界古都、丝路起点、博物馆之城”等城市文化识别。
- [西安市文化和旅游局：5·19中国旅游日](https://wlj.xa.gov.cn/ztzl/zglyr/2056273313018253313.html)：支持当代城市观光、唐诗文化体验与步行游览行为；人物不采用历史服饰化表达。

角色以现代游客的观察与介绍行为表达西安。移除地方 cue 后仍是完整的轻量导览人物。

## 差异化与风险控制

- `CITY_RESEARCH_BEFORE_GENERATION = PASS`
- `CHARACTER_DIFFERENTIATION = HIGH`
- `STYLE_DIFFERENTIATION = LOW`
- `LOCAL_FEATURE_INTEGRATION = PASS`
- `STEREOTYPE_RISK_CONTROL = PASS`
- `POSE_SIGNATURE_LOCKED_BEFORE_GENERATION = PASS`
- `handPoseSignature = left-map-low + right-open-palm`
