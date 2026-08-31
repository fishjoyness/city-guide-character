# 三亚 — 城市导览人物

状态：READY_FOR_GENERATION  
研究访问日期：2026-08-31

```yaml
city: 三亚
cityType: tropical-coast-island-resort
temperament: 轻快、松弛、明朗，带有海风中的步行感
visualKeywords: [热带海岸, 海风漫步, 椰林日落, 海岛轻旅行, 明亮低饱和]
hairstyle: 齐下巴自然短卷发，海风吹起一侧发尾
outfitStyle: 现代海滨轻装；短袖开领衬衫、素色内搭、宽松五分裤
primaryColors: [暖米白, 海沫浅蓝, 低饱和珊瑚橙, 沙滩卡其]
accentColor: 小面积深海蓝
poseTendency: 迎风向左轻快迈步，一手自然向后侧展开，另一手在腿侧垂握太阳镜
prop: 太阳镜
poseSignature:
  faceOrientation: THREE_QUARTER_LEFT
  bodyOrientation: WALKING_LEFT
  gestureFamily: SEA_BREEZE_STEP
  leftHand: 向身后外侧自然展开，手掌放松
  rightHand: 在右腿外侧垂握折叠太阳镜
  handPoseSignature: left-open-back + right-sunglasses-down
  stance: MID_STEP_TRAILING_FOOT
  weightDistribution: left
  footwear: simple-sandals
  silhouetteNote: 风吹短卷发、向后展开的左臂、腿侧太阳镜与后抬脚形成前进方向明确的非对称轮廓
localFeature: [NONE]
avoid: [黎苗传统服装拼贴, 椰子或冲浪板道具, 花环, 比基尼, 文字, 城市名称, 第二件道具, 地标背景]
mapRole: MAP_VIEWPORT_OVERLAY
styleVersion: pen-travel-v0.1
```

## 研究依据

- [三亚市政府：30 must-do things in Sanya](https://english.sanya.gov.cn/syen/entertainment/202409/e463d7974b594c688b58bb1b973f882c.shtml)：支持海岛、海湾、椰梦长廊、后海冲浪与轻松海滨旅行行为。
- [三亚市天涯区政府：清明假期畅游三亚](https://ty.sanya.gov.cn/tyqsite/jrty/202604/dbba77c214ad4980bfdb0f42ae40cb12.shtml)：支持山海人文并置、春夏轻装与明朗热带气质。

- `CITY_RESEARCH_BEFORE_GENERATION = PASS`
- `CHARACTER_PEN_STYLE_LOCK = true`
- `POSE_SIGNATURE_LOCKED_BEFORE_GENERATION = PASS`
- `CROSS_CITY_POSE_REVIEW = PASS`（不同于长沙 POINTING、昆明 OPEN_PALM_GUIDE、大理 SHADE_EYES；使用 SEA_BREEZE_STEP / MID_STEP_TRAILING_FOOT）

