# 天津 — 城市导览人物

状态：READY_FOR_GENERATION  
研究访问日期：2026-09-01

```yaml
city: 天津
cityType: river-port-modern-history-city
temperament: 松弛、爽朗、机敏，带一点海河城市漫步的轻快幽默感
visualKeywords: [海河城市漫步, 万国建筑, 津派市井, 运河与港口, 中西交融]
hairstyle: 蓬松短侧分，发梢略被河风吹起，现代清爽
outfitStyle: 现代轻便 city-walk；短款藏蓝风衣、象牙细条纹针织衫、暖灰宽松褶裥裤
primaryColors: [藏蓝, 暖象牙, 暖灰, 深棕]
accentColor: 小面积砖红围巾
poseTendency: 身体向右侧跨一步、上身略向左转；左手在肩侧捏住被风带起的围巾末端，右手在大腿外侧低垂握小型相机
prop: 小型无品牌相机
poseSignature:
  faceOrientation: THREE_QUARTER_LEFT
  bodyOrientation: SIDE_STEP_RIGHT_TORSO_LEFT
  gestureFamily: CROSSWIND_SCARF_STEP
  leftHand: 肩侧外展，轻捏砖红围巾末端
  rightHand: 右腿外侧低位握小型相机
  handPoseSignature: left-scarf-out-at-shoulder + right-camera-low-outside-thigh
  stance: WIDE_SIDE_STEP_RIGHT_TOE_OUT
  weightDistribution: left
  footwear: simple-leather-sneakers
  silhouetteNote: 河风扬起的短发与围巾形成左上动势，右侧跨步和低位相机形成对角线，不使用正面静站模板
localFeature: [NONE]
avoid: [民国长衫, 相声演员造型, 厨师造型, 食物, 天津之眼头饰, 建筑印花拼贴, 文字, 城市名称, 第二件手持道具]
mapRole: MAP_VIEWPORT_OVERLAY
styleVersion: pen-travel-v0.1
```

## 研究依据

- [天津市推动旅游业高质量发展文件](https://www.tj.gov.cn/zwgk/dzhhxx/202412/t20241225_6814444.html)：支持海河文化旅游观光带、历史文化街区与城市漫步并置的当代旅行语境。
- [天津市文化和旅游局：意式风情区](https://whly.tj.gov.cn/tjswlzxw/lytj/lhjg/whjq/202303/t20230315_6140211.html)：支持近代建筑、中西交融与开放城市气质。
- [天津市文化和旅游局 A 级景区名录](https://whly.tj.gov.cn/tjswlzxw/sy1/ykxz/qyml/202312/t20231208_6476542.html)：支持古文化街、盘山、黄崖关、独乐寺及现代都市景点共同构成的目的地层次。

- `CITY_RESEARCH_BEFORE_GENERATION = PASS`
- `CHARACTER_PEN_STYLE_LOCK = true`
- `POSE_SIGNATURE_LOCKED_BEFORE_GENERATION = PASS`
- `CROSS_CITY_POSE_REVIEW = PASS`（新增 CROSSWIND_SCARF_STEP / WIDE_SIDE_STEP_RIGHT_TOE_OUT）

