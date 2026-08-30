# 桂林 — 城市人物风格测试

状态：EXPERIMENTAL / NOT FOR PRODUCTION
研究访问日期：2026-08-30

```yaml
city: 桂林
cityType: landscape-nature
temperament: 松弛、自然、温和、好奇探索
visualKeywords: [山水旅行, 清爽, 户外散步, 观察型, 轻盈]
hairstyle: 短而轻微卷曲，侧向碎发形成不对称自然轮廓
outfitStyle: 现代轻户外；简化短外套与宽松长裤，领口只保留一条窄织纹细节
primaryColors: [漓江雾蓝, 喀斯特柔绿, 岩灰, 米白]
accentColor: 低饱和靛蓝
poseTendency: 准备继续步行，一手把旅行本自然垂在身侧，另一只手随步伐轻摆
prop: 一本小旅行记录本
poseSignature:
  faceOrientation: FRONT
  bodyOrientation: SLIGHT_LEFT
  gestureFamily: WALKING_READY
  leftHand: 在左侧自然垂下并握住合上的旅行本
  rightHand: 轻微后摆并自然放松
  handPoseSignature: left-notebook-at-side + right-relaxed-swing
  stance: WALKING_READY
  weightDistribution: left-with-right-foot-leading
  footwear: walking-shoes
  silhouetteNote: 一脚前伸和两臂错开形成轻微行走轮廓
localFeature: [领口一条经核实的广西壮锦几何织纹语言，面积很小且现代化]
avoid: [整套民族盛装, 复杂头饰, 多民族元素混搭, 专业登山广告感, 山峰贴在人身上, 第二件道具]
mapRole: MAP_VIEWPORT_OVERLAY
styleVersion: pen-travel-v0.1
```

## 研究依据

- [广西自然资源厅：漓江山水与喀斯特生态](https://dnr.gxzf.gov.cn/xwzx/zrzx/t24327202.shtml)：支持江雾蓝、柔和绿、岩灰配色和松弛的自然旅行气质。
- [广西政府国土空间规划：桂林所在桂东北的喀斯特峰林与漓江山水](https://www.gxzf.gov.cn/html/zwgk/zfxxgkzl_84988/fdzdgknr/zdmsxx/zfbz_182764/ydjh915_182772/t19113220.shtml)：支持山水自然型城市分类。
- [文化和旅游部：壮族织锦技艺](https://zhuanti.mct.gov.cn/xcss2024_nlhwzzxc/guangxi/detail/8194.html)：核实壮锦是广西真实文化来源。角色只使用一条现代化窄纹样，不暗示所有桂林居民共享同一种服饰。

角色仍然是现代桂林旅行者。地域织物暗示经过研究、面积很小，而且移除后仍不影响角色成立。

## Pose QA

- `POSE_SIGNATURE_LOCKED_BEFORE_GENERATION = PASS`
- `handPoseSignature = left-notebook-at-side + right-relaxed-swing`
