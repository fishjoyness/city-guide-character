# 大理 — 城市导览人物

状态：DONE  
研究访问日期：2026-08-31

```yaml
city: 大理
cityType: highland-lake-heritage-town
temperament: 松弛、清朗、亲近山水，兼具古城步行与轻户外气质
visualKeywords: [苍山洱海, 古城慢行, 湖岸骑游, 日照清朗, 白族建筑语境]
hairstyle: 中短自然卷发，额前碎发随风形成不对称轮廓
outfitStyle: 现代轻户外；薄衬衫式外套、简单内搭、宽松九分裤
primaryColors: [暖米白, 苍山蓝灰, 洱海浅蓝, 亚麻卡其]
accentColor: 小面积低饱和砖红
poseTendency: 一手将软檐遮阳帽垂在身侧，另一手抬到眉上遮光远望
prop: 软檐遮阳帽
poseSignature:
  faceOrientation: THREE_QUARTER_RIGHT
  bodyOrientation: SLIGHT_RIGHT
  gestureFamily: SHADE_EYES
  leftHand: 松握软檐遮阳帽并垂在左腿外侧
  rightHand: 抬至眉上做遮光远望动作
  handPoseSignature: left-sunhat-down + right-shade-eyes
  stance: CROSS_ANKLE
  weightDistribution: right
  footwear: simple-canvas-shoes
  silhouetteNote: 卷发、额前遮光手臂、下垂软帽和交叠脚踝构成清晰的高低错位轮廓
localFeature: [NONE]
avoid: [白族传统服装拼贴, 扎染纹样臆造, 花冠, 风花雪月文字, 食物道具, 第二件道具, 城市名称]
mapRole: MAP_VIEWPORT_OVERLAY
styleVersion: pen-travel-v0.1
```

## 研究依据

- [大理州人民政府：洱海](https://www.dali.gov.cn/dlzrmzf/c101724/pc/content/1968886945315655680/content_1968886945315655680.html)：支持苍山洱海、双廊、湖岸游览与开阔清朗的旅行行为。
- [大理州人民政府：2023 年政府工作报告](https://www.dali.gov.cn/dlzrmzf/c101526/pc/content/1968879954111336448/content_1968879954111336448.html)：支持苍洱世界级旅游度假、喜洲、沙溪与慢行康旅气质。
- [云南省体育局：大理徒步旅游节](https://tyj.yn.gov.cn/tyzx/tycy/202310/t20231021_3417324.html)：支持崇圣寺三塔、古城与山水徒步相结合的轻户外语境。

- `CITY_RESEARCH_BEFORE_GENERATION = PASS`
- `CHARACTER_PEN_STYLE_LOCK = true`
- `POSE_SIGNATURE_LOCKED_BEFORE_GENERATION = PASS`
- `CROSS_CITY_POSE_REVIEW = PASS`（不同于长沙 POINTING 与昆明 OPEN_PALM_GUIDE；使用 SHADE_EYES / CROSS_ANKLE）
