# 上海 — 城市人物风格测试

状态：EXPERIMENTAL / NOT FOR PRODUCTION
研究访问日期：2026-08-30

```yaml
city: 上海
cityType: modern-metropolis
temperament: 利落、精致、自信、安静好奇
visualKeywords: [都市漫游, 轻时尚, 逛展, 摄影, 清爽]
hairstyle: 下颌长度的直短发，侧分刘海，轮廓利落
outfitStyle: 现代城市休闲；短夹克与直筒长裤，简洁叠穿
primaryColors: [低饱和灰蓝, 米白, 柔和灰紫]
accentColor: 少量深炭色
poseTendency: 在城市漫步中停下，相机挂在肩带上，以不对称动作准备取景
prop: 一台小型相机
poseSignature:
  faceOrientation: SLIGHT_LEFT
  bodyOrientation: SLIGHT_RIGHT
  gestureFamily: CAMERA_ACTION
  leftHand: 轻扶胸前相机肩带
  rightHand: 在右侧髋部单手提住相机
  handPoseSignature: left-adjusts-camera-strap + right-camera-at-hip
  stance: WEIGHT_RIGHT
  weightDistribution: right
  footwear: simple-flats
  silhouetteNote: 右侧相机与承重腿形成偏右重心，左臂上抬但不封闭胸前
localFeature: []
avoid: [东方明珠贴图, 摩天楼堆叠, 全身霓虹, 商业时装海报感, 第二件道具]
mapRole: MAP_VIEWPORT_OVERLAY
styleVersion: pen-travel-v0.1
```

## 研究依据

- [上海市政府：文博、美术、艺术与时尚相融合的 City Walk](https://www.shanghai.gov.cn/cmsres/22/22a4e60363b24b52951b1403e12f2c3d/601f63f9ee982fc55be73a1611322b1e.pdf)：支持都市、艺术观展和城市漫游气质。
- [上海市政府：精品线路与城市漫游](https://www.shanghai.gov.cn/nw17239/20250430/a3efe384da7544e38e8a74c10714f73b.html)：支持摄影、展览、建筑观察和现代城市漫游行为。

角色不使用摩天楼等直白符号。城市识别来自协调的气质、发型轮廓、现代穿搭、冷静配色和摄影行为。

## Pose QA

- `POSE_SIGNATURE_LOCKED_BEFORE_GENERATION = PASS`
- `handPoseSignature = left-adjusts-camera-strap + right-camera-at-hip`
