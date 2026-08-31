# 洛阳 — 城市导览人物

状态：READY_FOR_GENERATION  
研究访问日期：2026-09-01

```yaml
city: 洛阳
cityType: ancient-capital-archaeology-mountain-city
temperament: 从容、知性、温暖，兼具古都步行与博物馆探索气质
visualKeywords: [十三朝古都, 石窟寺, 隋唐中轴, 博物馆之都, 牡丹春色]
hairstyle: 低位松髻配不对称侧刘海，轮廓简洁现代
outfitStyle: 现代层次通勤；短款圆领外套、素色上衣、宽松直筒裤
primaryColors: [暖象牙, 低饱和陶土红, 鼠尾草绿, 深灰褐]
accentColor: 小面积牡丹粉
poseTendency: 向右迈步但上身回转向左回望，一手垂握薄导览册，另一手轻扶单肩包带
prop: 薄导览册
poseSignature:
  faceOrientation: LOOK_BACK_LEFT
  bodyOrientation: WALKING_RIGHT_HALF_TURN
  gestureFamily: WALK_AND_LOOK_BACK
  leftHand: 在左腿后侧垂握薄导览册
  rightHand: 在右肩附近轻扶单肩包带
  handPoseSignature: left-guidebook-back-down + right-strap-shoulder
  stance: WALKING_REAR_HEEL_LIFT
  weightDistribution: right
  footwear: simple-loafers
  silhouetteNote: 低髻、回望头部、身后低位导览册和抬起后脚跟构成有方向性的转身轮廓
localFeature: [NONE]
avoid: [汉服, 唐代发髻, 牡丹花冠, 传统服装拼贴, 扇子, 食物, 文字, 城市名称, 第二件道具]
mapRole: MAP_VIEWPORT_OVERLAY
styleVersion: pen-travel-v0.1
```

## 研究依据

- [洛阳市A级景区名录](https://oss.ly.gov.cn/upload-file/files/20241018/e3bc30071f1d49709e7d70e299c75de2.pdf)：支持石窟寺、古都遗址与山地景区并置的旅行语境。
- [洛阳市文旅局研学体系](https://oss.ly.gov.cn/lyswhgdhlyj/upload/20240909/297ed34a91bc35ac0191d5ec95a3001c.pdf)：支持博物馆之都、隋唐洛阳城、龙门和白马寺的知性探索气质。

- `CITY_RESEARCH_BEFORE_GENERATION = PASS`
- `CHARACTER_PEN_STYLE_LOCK = true`
- `POSE_SIGNATURE_LOCKED_BEFORE_GENERATION = PASS`
- `CROSS_CITY_POSE_REVIEW = PASS`（新增 WALK_AND_LOOK_BACK / WALKING_REAR_HEEL_LIFT）

