# 昆明 — 城市导览人物

状态：DONE  
研究访问日期：2026-08-31

```yaml
city: 昆明
cityType: highland-lake-garden-city
temperament: 清爽、从容、亲近自然，兼具历史街区与多民族文化的开放感
visualKeywords: [春城步行, 高原湖泊, 城市花木, 文博体验, 轻户外]
hairstyle: 低马尾配自然侧分碎发，轮廓简洁，不使用民族头饰
outfitStyle: 轻薄针织开衫、圆领内搭、高腰宽松直筒裤，适合高原城市日间步行
primaryColors: [暖米白, 雾蓝, 鼠尾草绿, 浅卡其]
accentColor: 小面积低饱和山茶红
poseTendency: 身体侧向前行，一手在腰侧握细窄折叠导览册，另一手自然抬起做开放式引导
prop: 细窄折叠导览册
poseSignature:
  faceOrientation: PROFILE_RIGHT
  bodyOrientation: RIGHT_WALKING
  gestureFamily: OPEN_PALM_GUIDE
  leftHand: 在左腰外侧握一册闭合的细窄折叠导览册
  rightHand: 向右前方自然抬起，掌心微开，不指点
  handPoseSignature: left-guide-fold-at-hip + right-open-palm-forward
  stance: MID_STEP
  weightDistribution: right
  footwear: simple-walking-shoes
  silhouetteNote: 低马尾、向右开放手臂、腰侧窄册与左脚后收形成清晰行进轮廓
localFeature: [NONE]
avoid: [民族服饰拼贴, 孔雀羽毛, 鲜花头冠, 食物道具, 城市名称文字, 第二件道具, 历史服装]
mapRole: MAP_VIEWPORT_OVERLAY
styleVersion: pen-travel-v0.1
```

## 研究依据

- [云南省人民政府：云南省“十四五”文化和旅游发展规划](https://www.yn.gov.cn/ztgg/jdbytjwhjc/cyh/zczd/202205/t20220527_242589.html)：昆明以滇池、石林、世博园等自然与城市文旅资源共同构成国际旅游中心。
- [云南省人民政府：昆明都市圈发展规划](https://www.yn.gov.cn/zwgk/zcwj/zxwj/202606/t20260615_327863.html)：强调历史文化名城、滇池湖滨、西山与石林等山水人文格局。
- [昆明信息港：昆明文旅融合](https://www.kunming.cn/news/c/2026-01-22/14012526.shtml)：支持滇池、大翠湖人文圈、石林与城市街区相结合的轻松旅行气质。

- `CITY_RESEARCH_BEFORE_GENERATION = PASS`
- `CHARACTER_PEN_STYLE_LOCK = true`
- `POSE_SIGNATURE_LOCKED_BEFORE_GENERATION = PASS`
- `CROSS_CITY_POSE_REVIEW = PASS`（与长沙 POINTING / ONE_FOOT_FORWARD 不同；当前使用 PROFILE_RIGHT / OPEN_PALM_GUIDE / MID_STEP）
