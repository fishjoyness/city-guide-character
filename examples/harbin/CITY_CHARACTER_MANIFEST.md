# 哈尔滨 — 城市导览人物

状态：READY_FOR_GENERATION  
研究访问日期：2026-09-01

```yaml
city: 哈尔滨
cityType: northern-ice-snow-heritage-city
temperament: 清爽、稳重、亲切，带有寒地城市步行与音乐气质
visualKeywords: [冰雪城市, 欧陆街区, 松花江, 冬日步行, 音乐之城]
hairstyle: 短而蓬松的深色侧分发，针织帽下露出不对称额发
outfitStyle: 现代寒地通勤轻户外；短款羽绒夹克、细针织衫、直筒裤
primaryColors: [暖灰白, 雾霾蓝, 深炭灰, 浅燕麦]
accentColor: 小面积低饱和酒红
poseTendency: 身体略向右，一手抬到耳侧调整耳罩，另一手插在外套侧袋，双脚错位站立
prop: NONE
poseSignature:
  faceOrientation: THREE_QUARTER_LEFT
  bodyOrientation: SLIGHT_RIGHT
  gestureFamily: ADJUST_EARMUFF
  leftHand: 抬到左耳侧轻触佩戴式耳罩
  rightHand: 插入右侧外套口袋
  handPoseSignature: left-earmuff-touch + right-pocket
  stance: OFFSET_FEET_TOE_OUT
  weightDistribution: right
  footwear: simple-winter-boots
  silhouetteNote: 针织帽、耳侧抬臂、单手插袋与外撇前脚构成紧凑但非对称的冬日轮廓
localFeature: [NONE]
avoid: [俄式民族服装, 军大衣, 毛皮帽刻板印象, 冰雕背景, 食物道具, 文字, 城市名称, 第二件道具]
mapRole: MAP_VIEWPORT_OVERLAY
styleVersion: pen-travel-v0.1
```

## 研究依据

- [哈尔滨市旅游协会线路](https://hrbcredit.harbin.gov.cn/creditMess.do?conId=5e8ace9b004c4ebbace30661c16f93b5&method=thirdPage)：支持中央大街、索菲亚广场、松花江、太阳岛等寒地城市步行语境。
- [黑龙江省文旅厅：哈尔滨十线百景](https://wlt.hlj.gov.cn/wlt/c114254/202608/c00_31964291.shtml)：支持冰雪、音乐、欧陆建筑与现代城市文化并置。

- `CITY_RESEARCH_BEFORE_GENERATION = PASS`
- `CHARACTER_PEN_STYLE_LOCK = true`
- `POSE_SIGNATURE_LOCKED_BEFORE_GENERATION = PASS`
- `CROSS_CITY_POSE_REVIEW = PASS`（不同于 POINTING、OPEN_PALM_GUIDE、SHADE_EYES、SEA_BREEZE_STEP；使用 ADJUST_EARMUFF / OFFSET_FEET_TOE_OUT）

