# 苏州 — 城市导览人物

状态：PRODUCTION V1  
研究访问日期：2026-08-30

```yaml
city: 苏州
cityType: classical-modern-water-city
temperament: 清爽、细致、安静但不拘谨、善于步行探索
visualKeywords: [园林尺度, 水巷步行, 当代设计, 克制雅致, 古今并置]
hairstyle: 清爽短发，侧分并保留自然碎发，男性青年轮廓，与既有长发或卷发角色显著区分
outfitStyle: 当代轻旅行；灰绿色短款工装衬衫叠穿米白 T 恤，深灰九分直筒裤，小型斜挎包
primaryColors: [园林灰绿, 粉墙米白, 瓦片炭灰, 木构暖棕]
accentColor: 斜挎包拉链与袜口使用少量低饱和砖红
poseTendency: 一手在肩侧轻扶斜挎包带，另一手自然下垂，一脚略向前
prop: 小型斜挎旅行包
poseSignature:
  faceOrientation: SLIGHT_LEFT
  bodyOrientation: SLIGHT_RIGHT
  gestureFamily: STRAP_BAG_INTERACTION
  leftHand: 在左肩附近轻扶斜挎包带
  rightHand: 在身体右侧自然下垂，手指放松
  handPoseSignature: left-shoulder-strap + right-relaxed-down
  stance: ONE_FOOT_FORWARD
  weightDistribution: back-right
  footwear: canvas-sneakers
  silhouetteNote: 短发男性轮廓、斜向包带、一脚前置形成不对称但克制的步行剪影
localFeature: [从粉墙黛瓦提取米白与炭灰, 从园林植被提取低饱和灰绿, 通过当代轻旅行剪裁连接苏州博物馆式现代感]
avoid: [汉服, 长衫刻板印象, 扇子刺绣等符号堆叠, 园林建筑贴在人身上, 双手胸前拿物, 两腿平行站立, 与南京角色换装]
mapRole: MAP_VIEWPORT_OVERLAY
styleVersion: pen-travel-v0.2
```

## 研究依据

- [苏州市政府古城旅行交通资料](https://www.suzhou.gov.cn/szsrmzf/mszx/202505/0ad6ad26c7b54888b651a6259c4dfc2f.shtml)：支持以步行、轨道和小尺度街区探索为主的导览行为。
- [苏州市园林局园林资料](https://ylj.suzhou.gov.cn/szsylj/ryxz/nav_list.shtml)：支持粉墙、黛瓦、园林植被与克制尺度构成的城市色彩关系。
- [苏州市文广旅局导览景点范围](https://wglj.suzhou.gov.cn/szwhgdhlyj/tzgg/202408/c82f79206f7445cba3ee827f0e61dd65.shtml)：古典园林、水巷、博物馆和古镇共同构成城市旅行体验，人物不应被单一传统符号概括。

人物使用现代短发男性轻旅行者，不穿传统服装。城市感来自灰绿、米白与炭灰的配色、细致简洁的穿搭和适合步行的斜挎包互动，而不是把园林或水乡符号直接贴到人物身上。

## Pose QA

- `POSE_SIGNATURE_LOCKED_BEFORE_GENERATION = PASS`
- `handPoseSignature = left-shoulder-strap + right-relaxed-down`
- 与北京、上海、桂林、南京现有正式角色的手势、站姿和鞋型签名不重复。
