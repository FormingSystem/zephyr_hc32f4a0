---
id: learning.zephyr-docs.api-fota-storage-topic-reference.page-9
title: 视频控制 ID（Video Control IDs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_视频控制 ID（Video Control IDs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频控制 ID（Video Control IDs）

<a id="details"></a>

视频控制标识符（Video Control IDs，CIDs）。自（Since）4.4 起提供，版本（Version）0.0.1。视频控制 ID 使用与 Linux V4L2 子系统相同的名称，并归入相同的类。这便于 Linux 与 Zephyr 之间的互操作及设备端到端调试。此列表与 `linux/include/uapi/linux/v4l2-controls.h` 中的 Linux 内核定义保持兼容。

<a id="header-files"></a>
<a id="files"></a>

## 9.1\_文件（Files）

<a id="r_controls_2Eh"></a>

```c
file controls.h
```

相关声明：[controls.h](../api_file_usb_network_reference/P005_zephyr__video__controls.h_文件参考.md)。

视频控制ID（Video Control IDs）定义的主头文件。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 9.2\_基本类控制标识符（Base Class Control IDs）

<a id="r_ga9db809ab56484b4b5b1a047a97e6920a"></a>

```c
enum video_power_line_frequency { VIDEO_CID_POWER_LINE_FREQUENCY_DISABLED = 0 , VIDEO_CID_POWER_LINE_FREQUENCY_50HZ = 1 , VIDEO_CID_POWER_LINE_FREQUENCY_60HZ = 2 , VIDEO_CID_POWER_LINE_FREQUENCY_AUTO = 3 }
```

相关声明：[video_power_line_frequency](#ga9db809ab56484b4b5b1a047a97e6920a)、[VIDEO_CID_POWER_LINE_FREQUENCY_DISABLED](#gga9db809ab56484b4b5b1a047a97e6920aa596b3bec6771ef15392bfcee9fc47f93)、[VIDEO_CID_POWER_LINE_FREQUENCY_50HZ](#gga9db809ab56484b4b5b1a047a97e6920aad47b0f6914d0e949d17faa61b9fc2c10)、[VIDEO_CID_POWER_LINE_FREQUENCY_60HZ](#gga9db809ab56484b4b5b1a047a97e6920aad34ec7a0db40ee5b1dbfc6de79834796)、[VIDEO_CID_POWER_LINE_FREQUENCY_AUTO](#gga9db809ab56484b4b5b1a047a97e6920aa817468b493999a2ba979a249bc0cffe0)。

视频电源线频率（Video Power Line Frequency）。

<a id="r_ga99f4b6cf21c8baaf510fbcfccb645960"></a>

```c
enum video_colorfx { VIDEO_COLORFX_NONE = 0 , VIDEO_COLORFX_BW = 1 , VIDEO_COLORFX_SEPIA = 2 , VIDEO_COLORFX_NEGATIVE = 3 , VIDEO_COLORFX_EMBOSS = 4 , VIDEO_COLORFX_SKETCH = 5 , VIDEO_COLORFX_SKY_BLUE = 6 , VIDEO_COLORFX_GRASS_GREEN = 7 , VIDEO_COLORFX_SKIN_WHITEN = 8 , VIDEO_COLORFX_VIVID = 9 , VIDEO_COLORFX_AQUA = 10 , VIDEO_COLORFX_ART_FREEZE = 11 , VIDEO_COLORFX_SILHOUETTE = 12 , VIDEO_COLORFX_SOLARIZATION = 13 , VIDEO_COLORFX_ANTIQUE = 14 }
```

相关声明：[video_colorfx](#ga99f4b6cf21c8baaf510fbcfccb645960)、[VIDEO_COLORFX_NONE](#gga99f4b6cf21c8baaf510fbcfccb645960a9960e8b54cf9070c04664246e67f3237)、[VIDEO_COLORFX_BW](#gga99f4b6cf21c8baaf510fbcfccb645960a52f62a92f6f0e158b1797719efb79735)、[VIDEO_COLORFX_SEPIA](#gga99f4b6cf21c8baaf510fbcfccb645960a483faa51fb4728b89c1a8da60b139a37)、[VIDEO_COLORFX_NEGATIVE](#gga99f4b6cf21c8baaf510fbcfccb645960ac9367e073eef47865d90ba9ae6eb98a0)、[VIDEO_COLORFX_EMBOSS](#gga99f4b6cf21c8baaf510fbcfccb645960aae3d42f32c4f14e371343a32e8132cc0)、[VIDEO_COLORFX_SKETCH](#gga99f4b6cf21c8baaf510fbcfccb645960a789155f47a0302661a71155c1e6045fc)、[VIDEO_COLORFX_SKY_BLUE](#gga99f4b6cf21c8baaf510fbcfccb645960a09b5346a7431c2c0e7415037ee5a6f8b)、[VIDEO_COLORFX_GRASS_GREEN](#gga99f4b6cf21c8baaf510fbcfccb645960abd0ddf263af2224bebe12da19711c6a1)、[VIDEO_COLORFX_SKIN_WHITEN](#gga99f4b6cf21c8baaf510fbcfccb645960a3d4856179a0279a23f1597c3c0a615ef)、[VIDEO_COLORFX_VIVID](#gga99f4b6cf21c8baaf510fbcfccb645960a5e77aa2b5530062aaaf1156a340e3826)、[VIDEO_COLORFX_AQUA](#gga99f4b6cf21c8baaf510fbcfccb645960adb9e16ef9511c8eec1d6dbead4843a4c)、[VIDEO_COLORFX_ART_FREEZE](#gga99f4b6cf21c8baaf510fbcfccb645960a00faf2d7d366f0109d64568839416ccd)、[VIDEO_COLORFX_SILHOUETTE](#gga99f4b6cf21c8baaf510fbcfccb645960a1c93819be559612ccea3a2781cbb7d25)、[VIDEO_COLORFX_SOLARIZATION](#gga99f4b6cf21c8baaf510fbcfccb645960a2f6f282e1e195bdc29aa6a351c2bc715)、[VIDEO_COLORFX_ANTIQUE](#gga99f4b6cf21c8baaf510fbcfccb645960a71acc838d9197b671accab7763c5388b)。

视频色彩效果（Video Color Effects）。

<a id="r_ga4b56ce06ae4f6ca5b7ac9fd5a7b21319"></a>

```c
#define VIDEO_CID_BASE 0x00980900
```

相关声明：[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

<a id="r_ga1529eeb7c36bfe53e3916dbd9c6f5b1e"></a>

```c
#define VIDEO_CID_BRIGHTNESS (VIDEO_CID_BASE + 0)
```

相关声明：[VIDEO_CID_BRIGHTNESS](#ga1529eeb7c36bfe53e3916dbd9c6f5b1e)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

图像亮度（Brightness），更准确地说是黑电平（Black Level）。

<a id="r_ga9ca85f6b1d9add05eacb008dc4ccb2e4"></a>

```c
#define VIDEO_CID_CONTRAST (VIDEO_CID_BASE + 1)
```

相关声明：[VIDEO_CID_CONTRAST](#ga9ca85f6b1d9add05eacb008dc4ccb2e4)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

图像对比度（Contrast），即亮度增益（Luma Gain）。

<a id="r_ga200017c2141f5c90ade652224d1d4364"></a>

```c
#define VIDEO_CID_SATURATION (VIDEO_CID_BASE + 2)
```

相关声明：[VIDEO_CID_SATURATION](#ga200017c2141f5c90ade652224d1d4364)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

图像色彩饱和度（Color Saturation），即色度增益（Chroma Gain）。

<a id="r_ga588a1206d5046a7b9e8415db725cae81"></a>

```c
#define VIDEO_CID_HUE (VIDEO_CID_BASE + 3)
```

相关声明：[VIDEO_CID_HUE](#ga588a1206d5046a7b9e8415db725cae81)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

色调（Hue）或色彩平衡（Color Balance）。

<a id="r_ga7e2ce049ed534e1c29ac47d33013e180"></a>

```c
#define VIDEO_CID_AUTO_WHITE_BALANCE (VIDEO_CID_BASE + 12)
```

相关声明：[VIDEO_CID_AUTO_WHITE_BALANCE](#ga7e2ce049ed534e1c29ac47d33013e180)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

自动白平衡（Automatic White Balance），用于摄像头。

<a id="r_gab534e6263a6b5caae48543346ba2f7ef"></a>

```c
#define VIDEO_CID_RED_BALANCE (VIDEO_CID_BASE + 14)
```

相关声明：[VIDEO_CID_RED_BALANCE](#gab534e6263a6b5caae48543346ba2f7ef)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

红色色度平衡（Red Chroma Balance），表示为相对于绿色通道的比值。

<a id="r_gaf4d38f5eed6feb9ef9509c1747a332b8"></a>

```c
#define VIDEO_CID_BLUE_BALANCE (VIDEO_CID_BASE + 15)
```

相关声明：[VIDEO_CID_BLUE_BALANCE](#gaf4d38f5eed6feb9ef9509c1747a332b8)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

蓝色色度平衡（Blue Chroma Balance），表示为相对于绿色通道的比值。

<a id="r_ga4e38bb3fcb80b2d28fa88186b65e4fea"></a>

```c
#define VIDEO_CID_GAMMA (VIDEO_CID_BASE + 16)
```

相关声明：[VIDEO_CID_GAMMA](#ga4e38bb3fcb80b2d28fa88186b65e4fea)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

伽马调整（Gamma Adjust）。

<a id="r_ga24e259a6466537377b7bb8a151311ae1"></a>

```c
#define VIDEO_CID_EXPOSURE (VIDEO_CID_BASE + 17)
```

相关声明：[VIDEO_CID_EXPOSURE](#ga24e259a6466537377b7bb8a151311ae1)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

图像传感器曝光时间（Image Sensor Exposure Time）。

<a id="r_gac1c1d3580b7ff84b6a461cea0b3942e8"></a>

```c
#define VIDEO_CID_AUTOGAIN (VIDEO_CID_BASE + 18)
```

相关声明：[VIDEO_CID_AUTOGAIN](#gac1c1d3580b7ff84b6a461cea0b3942e8)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

自动增益控制（Automatic Gain Control）。

<a id="r_ga36259be44d9d08b149fd35dd28bbaf50"></a>

```c
#define VIDEO_CID_GAIN (VIDEO_CID_BASE + 19)
```

相关声明：[VIDEO_CID_GAIN](#ga36259be44d9d08b149fd35dd28bbaf50)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

增益控制（Gain Control）。

<a id="r_ga59aa47b6f558ef5ae64a67f4a7ac7e31"></a>

```c
#define VIDEO_CID_HFLIP (VIDEO_CID_BASE + 20)
```

相关声明：[VIDEO_CID_HFLIP](#ga59aa47b6f558ef5ae64a67f4a7ac7e31)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

水平翻转（Horizontal Flip）图像：左侧变为右侧。

<a id="r_ga16651a6825b619399a333ed39e802dfc"></a>

```c
#define VIDEO_CID_VFLIP (VIDEO_CID_BASE + 21)
```

相关声明：[VIDEO_CID_VFLIP](#ga16651a6825b619399a333ed39e802dfc)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

垂直翻转（Vertical Flip）图像：上方变为下方。

<a id="r_ga762a6c2b0fb032b9ebdfeff5ed15c3de"></a>

```c
#define VIDEO_CID_POWER_LINE_FREQUENCY (VIDEO_CID_BASE + 24)
```

相关声明：[VIDEO_CID_POWER_LINE_FREQUENCY](#ga762a6c2b0fb032b9ebdfeff5ed15c3de)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

需要补偿的电源线频率（Power Line Frequency）。

<a id="r_ga9c0df146e6064169a89bd88b10085cec"></a>

```c
#define VIDEO_CID_HUE_AUTO (VIDEO_CID_BASE + 25)
```

相关声明：[VIDEO_CID_HUE_AUTO](#ga9c0df146e6064169a89bd88b10085cec)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

启用设备的自动色调控制（Automatic Hue Control）。

<a id="r_ga0670d89542dc532a9c775e8e9c2638b1"></a>

```c
#define VIDEO_CID_WHITE_BALANCE_TEMPERATURE (VIDEO_CID_BASE + 26)
```

相关声明：[VIDEO_CID_WHITE_BALANCE_TEMPERATURE](#ga0670d89542dc532a9c775e8e9c2638b1)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

以开尔文（Kelvin）色温表示的白平衡设置（White Balance Settings）。

<a id="r_gab0509f0d3106bca07658e7cfcb1883cf"></a>

```c
#define VIDEO_CID_SHARPNESS (VIDEO_CID_BASE + 27)
```

相关声明：[VIDEO_CID_SHARPNESS](#gab0509f0d3106bca07658e7cfcb1883cf)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

调整摄像头的锐化滤波器（Sharpness Filter）。

<a id="r_ga2f22b11b526154e66440eca74ec5bd66"></a>

```c
#define VIDEO_CID_BACKLIGHT_COMPENSATION (VIDEO_CID_BASE + 28)
```

相关声明：[VIDEO_CID_BACKLIGHT_COMPENSATION](#ga2f22b11b526154e66440eca74ec5bd66)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

调整摄像头的背光补偿（Backlight Compensation）。

<a id="r_ga3fe7778ddb5c3f945b7649379a13321e"></a>

```c
#define VIDEO_CID_COLORFX (VIDEO_CID_BASE + 31)
```

相关声明：[VIDEO_CID_COLORFX](#ga3fe7778ddb5c3f945b7649379a13321e)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

选择色彩效果（Color Effect）。

<a id="r_ga46bb41b012b1a2240270817b9ce57637"></a>

```c
#define VIDEO_CID_AUTOBRIGHTNESS (VIDEO_CID_BASE + 32)
```

相关声明：[VIDEO_CID_AUTOBRIGHTNESS](#ga46bb41b012b1a2240270817b9ce57637)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

启用自动亮度（Automatic Brightness）。

<a id="r_ga5d2c02644e26f6a7f9887d5879231106"></a>

```c
#define VIDEO_CID_BAND_STOP_FILTER (VIDEO_CID_BASE + 33)
```

相关声明：[VIDEO_CID_BAND_STOP_FILTER](#ga5d2c02644e26f6a7f9887d5879231106)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

开启或关闭摄像头传感器的带阻滤波器（Band-stop Filter），或指定其强度。

<a id="r_gae7f2add167e46dffb19f33393c839c57"></a>

```c
#define VIDEO_CID_ROTATE (VIDEO_CID_BASE + 34)
```

相关声明：[VIDEO_CID_ROTATE](#gae7f2add167e46dffb19f33393c839c57)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

旋转控制（Rotate Control）。

<a id="r_ga78dcca8b4c8b29f23e983974b861f157"></a>

```c
#define VIDEO_CID_ALPHA_COMPONENT (VIDEO_CID_BASE + 41)
```

相关声明：[VIDEO_CID_ALPHA_COMPONENT](#ga78dcca8b4c8b29f23e983974b861f157)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

设置 Alpha 颜色分量（Alpha Color Component）。

<a id="r_ga829221ec6ea7348e743173ce5e6bd635"></a>

```c
#define VIDEO_CID_LASTP1 (VIDEO_CID_BASE + 44)
```

相关声明：[VIDEO_CID_LASTP1](#ga829221ec6ea7348e743173ce5e6bd635)、[VIDEO_CID_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

最后一个基本控制标识符（Base CID）加 1。

## 9.3\_摄像头类控制标识符（Camera Class Control IDs）

<a id="r_ga167cf84b8f4259e6cdd333748deafaf6"></a>

```c
enum video_exposure_type { VIDEO_EXPOSURE_AUTO = 0 , VIDEO_EXPOSURE_MANUAL = 1 , VIDEO_EXPOSURE_SHUTTER_PRIORITY = 2 , VIDEO_EXPOSURE_APERTURE_PRIORITY = 3 }
```

相关声明：[video_exposure_type](#ga167cf84b8f4259e6cdd333748deafaf6)、[VIDEO_EXPOSURE_AUTO](#gga167cf84b8f4259e6cdd333748deafaf6ab77bff3e8a2abd1c823dbb4324e8499b)、[VIDEO_EXPOSURE_MANUAL](#gga167cf84b8f4259e6cdd333748deafaf6a66ab6044a5961bc14e1ab718d1a91224)、[VIDEO_EXPOSURE_SHUTTER_PRIORITY](#gga167cf84b8f4259e6cdd333748deafaf6ac92a826dee7a328bb0b43857d6c09c61)、[VIDEO_EXPOSURE_APERTURE_PRIORITY](#gga167cf84b8f4259e6cdd333748deafaf6a8abeb9fbd3156edf9f3057692829cbcd)。

视频曝光类型（Video Exposure Type）。

<a id="r_ga1fb4e9981b362010439b9419691ac2af"></a>

```c
enum video_camera_orientation { VIDEO_CAMERA_ORIENTATION_FRONT = 0 , VIDEO_CAMERA_ORIENTATION_BACK = 1 , VIDEO_CAMERA_ORIENTATION_EXTERNAL = 2 }
```

相关声明：[video_camera_orientation](#ga1fb4e9981b362010439b9419691ac2af)、[VIDEO_CAMERA_ORIENTATION_FRONT](#gga1fb4e9981b362010439b9419691ac2afa76b044aa6d822af9844632761fefbaef)、[VIDEO_CAMERA_ORIENTATION_BACK](#gga1fb4e9981b362010439b9419691ac2afa831cc750dfcb43f74eb3a7ee59b33072)、[VIDEO_CAMERA_ORIENTATION_EXTERNAL](#gga1fb4e9981b362010439b9419691ac2afafcc44933e74389bef0e1f20b7998f594)。

视频摄像头朝向（Video Camera Orientation）。

<a id="r_ga0a6e2c6287a67e8aa174bb0130fe4c26"></a>

```c
#define VIDEO_CID_CAMERA_CLASS_BASE 0x009a0900
```

相关声明：[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

<a id="r_gab83ae3ca7fa3da66243431d489be37bd"></a>

```c
#define VIDEO_CID_EXPOSURE_AUTO (VIDEO_CID_CAMERA_CLASS_BASE + 1)
```

相关声明：[VIDEO_CID_EXPOSURE_AUTO](#gab83ae3ca7fa3da66243431d489be37bd)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

启用曝光时间（Exposure Time）和／或光圈孔径（Iris Aperture）的自动调整。

<a id="r_ga036f78623bcae18ea9627d45d1209245"></a>

```c
#define VIDEO_CID_EXPOSURE_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 2)
```

相关声明：[VIDEO_CID_EXPOSURE_ABSOLUTE](#ga036f78623bcae18ea9627d45d1209245)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

确定摄像头传感器的曝光时间（Exposure Time）。

<a id="r_gaa5f2ebd1e1aef2da68be4742941c1f50"></a>

```c
#define VIDEO_CID_EXPOSURE_AUTO_PRIORITY (VIDEO_CID_CAMERA_CLASS_BASE + 3)
```

相关声明：[VIDEO_CID_EXPOSURE_AUTO_PRIORITY](#gaa5f2ebd1e1aef2da68be4742941c1f50)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

设备是否可以在自动曝光（Auto-exposure）的影响下动态改变帧率（Frame Rate）。适用于将 `VIDEO_CID_EXPOSURE_AUTO` 设为 `VIDEO_EXPOSURE_AUTO` 或 `VIDEO_EXPOSURE_APERTURE_PRIORITY` 的情况。

<a id="r_ga23ed465d76fc54680d1e22422b66c829"></a>

```c
#define VIDEO_CID_PAN_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 4)
```

相关声明：[VIDEO_CID_PAN_RELATIVE](#ga23ed465d76fc54680d1e22422b66c829)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此只写控制（Write-only Control）使摄像头沿水平方向转动指定的量。

<a id="r_ga7c51639505c7b97fb1953ade5fc72534"></a>

```c
#define VIDEO_CID_TILT_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 5)
```

相关声明：[VIDEO_CID_TILT_RELATIVE](#ga7c51639505c7b97fb1953ade5fc72534)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此只写控制（Write-only Control）使摄像头沿垂直方向转动指定的量。

<a id="r_ga3b45437f606b8717dcadc22d56a706da"></a>

```c
#define VIDEO_CID_PAN_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 8)
```

相关声明：[VIDEO_CID_PAN_ABSOLUTE](#ga3b45437f606b8717dcadc22d56a706da)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此控制（Control）使摄像头沿水平方向转到指定位置。

<a id="r_gae474209914926f2bd38c99e020224b9c"></a>

```c
#define VIDEO_CID_TILT_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 9)
```

相关声明：[VIDEO_CID_TILT_ABSOLUTE](#gae474209914926f2bd38c99e020224b9c)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此控制（Control）使摄像头沿垂直方向转到指定位置。

<a id="r_ga9ce95d3c135a9221a8d0431d9df9836b"></a>

```c
#define VIDEO_CID_FOCUS_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 10)
```

相关声明：[VIDEO_CID_FOCUS_ABSOLUTE](#ga9ce95d3c135a9221a8d0431d9df9836b)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此控制将摄像头焦点（Focal Point）设置到指定位置。

<a id="r_ga4137146c348efdcc8088f6be1274b164"></a>

```c
#define VIDEO_CID_FOCUS_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 11)
```

相关声明：[VIDEO_CID_FOCUS_RELATIVE](#ga4137146c348efdcc8088f6be1274b164)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此只写控制（Write-only Control）使摄像头焦点（Focal Point）移动指定的量。

<a id="r_ga031525e88a6c0f915903f5c9068589f4"></a>

```c
#define VIDEO_CID_FOCUS_AUTO (VIDEO_CID_CAMERA_CLASS_BASE + 12)
```

相关声明：[VIDEO_CID_FOCUS_AUTO](#ga031525e88a6c0f915903f5c9068589f4)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

启用连续自动对焦调整（Continuous Automatic Focus Adjustments）。

<a id="r_ga1033858d5515c2016a0cc6ac06fd8b91"></a>

```c
#define VIDEO_CID_ZOOM_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 13)
```

相关声明：[VIDEO_CID_ZOOM_ABSOLUTE](#ga1033858d5515c2016a0cc6ac06fd8b91)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

以绝对值指定物镜焦距（Objective Lens Focal Length）。

<a id="r_ga40e76f27e97549a779a6581bd210b0f4"></a>

```c
#define VIDEO_CID_ZOOM_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 14)
```

相关声明：[VIDEO_CID_ZOOM_RELATIVE](#ga40e76f27e97549a779a6581bd210b0f4)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此只写控制（Write-only Control）相对于当前值设置物镜焦距（Objective Lens Focal Length）。

<a id="r_ga1a79541da7b7a37d9358fb1a3c42a1b7"></a>

```c
#define VIDEO_CID_ZOOM_CONTINUOUS (VIDEO_CID_CAMERA_CLASS_BASE + 15)
```

相关声明：[VIDEO_CID_ZOOM_CONTINUOUS](#ga1a79541da7b7a37d9358fb1a3c42a1b7)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

启动连续变焦运动（Continuous Zoom Movement）。

<a id="r_ga452858d6adfec3b58db6b26c96638fb2"></a>

```c
#define VIDEO_CID_IRIS_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 17)
```

相关声明：[VIDEO_CID_IRIS_ABSOLUTE](#ga452858d6adfec3b58db6b26c96638fb2)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此控制将摄像头光圈（Aperture）设为指定值。

<a id="r_ga8d1452dfe9c190f6e28e5e3dd35c52cc"></a>

```c
#define VIDEO_CID_IRIS_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 18)
```

相关声明：[VIDEO_CID_IRIS_RELATIVE](#ga8d1452dfe9c190f6e28e5e3dd35c52cc)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此只写控制（Write-only Control）使摄像头光圈（Aperture）改变指定的量。

<a id="r_gaa29e9e368d07a22593ef01b91cf1e0b7"></a>

```c
#define VIDEO_CID_AUTO_EXPOSURE_BIAS (VIDEO_CID_CAMERA_CLASS_BASE + 19)
```

相关声明：[VIDEO_CID_AUTO_EXPOSURE_BIAS](#gaa29e9e368d07a22593ef01b91cf1e0b7)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

自动曝光补偿（Automatic Exposure Compensation）。

<a id="r_ga9d224bc93e5c23317f9ccf89713a18d6"></a>

```c
#define VIDEO_CID_WIDE_DYNAMIC_RANGE (VIDEO_CID_CAMERA_CLASS_BASE + 21)
```

相关声明：[VIDEO_CID_WIDE_DYNAMIC_RANGE](#ga9d224bc93e5c23317f9ccf89713a18d6)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

启用或禁用摄像头的宽动态范围（Wide Dynamic Range）功能。

<a id="r_ga99996bce4091e4223130d9ae5e1024cd"></a>

```c
#define VIDEO_CID_PAN_SPEED (VIDEO_CID_CAMERA_CLASS_BASE + 32)
```

相关声明：[VIDEO_CID_PAN_SPEED](#ga99996bce4091e4223130d9ae5e1024cd)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此控制使摄像头以指定速度沿水平方向转动。

<a id="r_ga3bfeedcd519191bcf1d684fd983ca9bc"></a>

```c
#define VIDEO_CID_TILT_SPEED (VIDEO_CID_CAMERA_CLASS_BASE + 33)
```

相关声明：[VIDEO_CID_TILT_SPEED](#ga3bfeedcd519191bcf1d684fd983ca9bc)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此控制使摄像头以指定速度沿垂直方向转动。

<a id="r_ga57e5c3f562683a2b7ea1f96a58f633be"></a>

```c
#define VIDEO_CID_CAMERA_ORIENTATION (VIDEO_CID_CAMERA_CLASS_BASE + 34)
```

相关声明：[VIDEO_CID_CAMERA_ORIENTATION](#ga57e5c3f562683a2b7ea1f96a58f633be)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此只读控制（Read-only Control）描述摄像头在设备上的位置，即摄像头在设备上的安装位置（Mounting Position）。

<a id="r_ga0d48a910e8d6797842dc25b33fc3f187"></a>

```c
#define VIDEO_CID_CAMERA_SENSOR_ROTATION (VIDEO_CID_CAMERA_CLASS_BASE + 35)
```

相关声明：[VIDEO_CID_CAMERA_SENSOR_ROTATION](#ga0d48a910e8d6797842dc25b33fc3f187)、[VIDEO_CID_CAMERA_CLASS_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此只读控制（Read-only Control）描述传感器在设备中的朝向（Orientation）。

## 9.4\_有状态编解码器控制标识符（Stateful Codec Control IDs）

<a id="r_gadf37e306a8d73cec4674422e74ffc85e"></a>

```c
#define VIDEO_CID_CODEC_CLASS_BASE 0x00990900
```

相关声明：[VIDEO_CID_CODEC_CLASS_BASE](#gadf37e306a8d73cec4674422e74ffc85e)。

## 9.5\_摄像头闪光灯类控制标识符（Camera Flash Class Control IDs）

<a id="r_ga9e0c8dc67fab1a80f81cd4be2e875954"></a>

```c
#define VIDEO_CID_FLASH_CLASS_BASE 0x009c0900
```

相关声明：[VIDEO_CID_FLASH_CLASS_BASE](#ga9e0c8dc67fab1a80f81cd4be2e875954)。

## 9.6\_JPEG 类控制标识符（JPEG Class Control IDs）

<a id="r_ga9281f5a61120a6de015a9bbc75ee8b91"></a>

```c
#define VIDEO_CID_JPEG_CLASS_BASE 0x009d0900
```

相关声明：[VIDEO_CID_JPEG_CLASS_BASE](#ga9281f5a61120a6de015a9bbc75ee8b91)。

<a id="r_ga883c2a761ea0f00e83c884a5b4b45eee"></a>

```c
#define VIDEO_CID_JPEG_COMPRESSION_QUALITY (VIDEO_CID_JPEG_CLASS_BASE + 3)
```

相关声明：[VIDEO_CID_JPEG_COMPRESSION_QUALITY](#ga883c2a761ea0f00e83c884a5b4b45eee)、[VIDEO_CID_JPEG_CLASS_BASE](#ga9281f5a61120a6de015a9bbc75ee8b91)。

JPEG 算法的质量因子（Quality Factor，Q）；提高该值也会增大数据量。

## 9.7\_图像源类控制标识符（Image Source Class Control IDs）

<a id="r_ga3cc32750dec0096ea873ea13e83d202e"></a>

```c
#define VIDEO_CID_IMAGE_SOURCE_CLASS_BASE 0x009e0900
```

相关声明：[VIDEO_CID_IMAGE_SOURCE_CLASS_BASE](#ga3cc32750dec0096ea873ea13e83d202e)。

<a id="r_ga41b451aace98fb81633983a413d2724f"></a>

```c
#define VIDEO_CID_ANALOGUE_GAIN (VIDEO_CID_IMAGE_SOURCE_CLASS_BASE + 3)
```

相关声明：[VIDEO_CID_ANALOGUE_GAIN](#ga41b451aace98fb81633983a413d2724f)、[VIDEO_CID_IMAGE_SOURCE_CLASS_BASE](#ga3cc32750dec0096ea873ea13e83d202e)。

模拟增益控制（Analogue Gain Control）。

## 9.8\_图像处理类控制标识符（Image Processing Class Control IDs）

<a id="r_ga0329342731999405d1f8d6c89470dff7"></a>

```c
#define VIDEO_CID_IMAGE_PROC_CLASS_BASE 0x009f0900
```

相关声明：[VIDEO_CID_IMAGE_PROC_CLASS_BASE](#ga0329342731999405d1f8d6c89470dff7)。

<a id="r_ga2142e2819c445b70d82067a3cfb193c8"></a>

```c
#define VIDEO_CID_LINK_FREQ (VIDEO_CID_IMAGE_PROC_CLASS_BASE + 1)
```

相关声明：[`VIDEO_CID_LINK_FREQ`（链路频率）。](#ga2142e2819c445b70d82067a3cfb193c8)、[VIDEO_CID_IMAGE_PROC_CLASS_BASE](#ga0329342731999405d1f8d6c89470dff7)。

链路频率（Link Frequency），适用于基于 CSI2 的设备。

<a id="r_ga6f6eaed7defdbb5f440874c7c6d0a6eb"></a>

```c
#define VIDEO_CID_PIXEL_RATE (VIDEO_CID_IMAGE_PROC_CLASS_BASE + 2)
```

相关声明：[`VIDEO_CID_PIXEL_RATE`（像素速率）。](#ga6f6eaed7defdbb5f440874c7c6d0a6eb)、[VIDEO_CID_IMAGE_PROC_CLASS_BASE](#ga0329342731999405d1f8d6c89470dff7)。

设备像素阵列（Pixel Array）的像素速率（Pixel Rate），单位为像素／秒。

<a id="r_gad1ce88a5c071eaeb8d5db9dc722a2cd4"></a>

```c
#define VIDEO_CID_TEST_PATTERN (VIDEO_CID_IMAGE_PROC_CLASS_BASE + 3)
```

相关声明：[VIDEO_CID_TEST_PATTERN](#gad1ce88a5c071eaeb8d5db9dc722a2cd4)、[VIDEO_CID_IMAGE_PROC_CLASS_BASE](#ga0329342731999405d1f8d6c89470dff7)。

选择要显示的测试图案类型（Test Pattern Type）。

<a id="r_gaf60ad41dc4fdffde0a60e53f624e7978"></a>

```c
#define VIDEO_CID_DIGITAL_GAIN (VIDEO_CID_IMAGE_PROC_CLASS_BASE + 5)
```

相关声明：[VIDEO_CID_DIGITAL_GAIN](#gaf60ad41dc4fdffde0a60e53f624e7978)、[VIDEO_CID_IMAGE_PROC_CLASS_BASE](#ga0329342731999405d1f8d6c89470dff7)。

数字增益控制（Digital Gain Control）。

## 9.9\_厂商特定类控制标识符（Vendor-specific Class Control IDs）

<a id="r_ga05e2fe16eafe259061af62ac31dfaeca"></a>

```c
#define VIDEO_CID_PRIVATE_BASE 0x08000000
```

相关声明：[VIDEO_CID_PRIVATE_BASE](#ga05e2fe16eafe259061af62ac31dfaeca)。

## 9.10\_查询标志，与控制标识符按位或（Query Flags, ORed with the Control ID）

<a id="r_ga6fc7bcd4b280b4598ea3a03108881b5c"></a>

```c
#define VIDEO_CTRL_FLAG_NEXT_CTRL 0x80000000
```

相关声明：[VIDEO_CTRL_FLAG_NEXT_CTRL](#ga6fc7bcd4b280b4598ea3a03108881b5c)。

## 9.11\_详细说明（Detailed Documentation）

<a id="ga78dcca8b4c8b29f23e983974b861f157"></a>

### `VIDEO_CID_ALPHA_COMPONENT`

```c
#define VIDEO_CID_ALPHA_COMPONENT (VIDEO_CID_BASE + 41)
```

```c
#include <zephyr/video/controls.h>
```

设置 Alpha 颜色分量（Alpha Color Component）。

某些设备产生的数据带有用户可控的透明度分量（Alpha Component）。此项设置应用于每个输出像素 Alpha 通道的值。

<a id="ga41b451aace98fb81633983a413d2724f"></a>

### `VIDEO_CID_ANALOGUE_GAIN`

```c
#define VIDEO_CID_ANALOGUE_GAIN (VIDEO_CID_IMAGE_SOURCE_CLASS_BASE + 3)
```

```c
#include <zephyr/video/controls.h>
```

模拟增益控制（Analogue Gain Control）。

模拟增益（Analogue Gain）影响像素矩阵中的所有颜色分量。增益操作在模数转换（A/D Conversion）之前的模拟域中执行。

<a id="gaa29e9e368d07a22593ef01b91cf1e0b7"></a>

### `VIDEO_CID_AUTO_EXPOSURE_BIAS`

```c
#define VIDEO_CID_AUTO_EXPOSURE_BIAS (VIDEO_CID_CAMERA_CLASS_BASE + 19)
```

```c
#include <zephyr/video/controls.h>
```

自动曝光补偿（Automatic Exposure Compensation）。

决定自动曝光补偿（Automatic Exposure Compensation）。仅当 `VIDEO_CID_EXPOSURE_AUTO` 控制项设为 `AUTO`、`SHUTTER_PRIORITY` 或 `APERTURE_PRIORITY` 时有效。以曝光值（Exposure Value，EV）表示；驱动应将数值解释为以 0.001 EV 为单位，例如 1000 表示 +1 EV。

增大曝光补偿值（Exposure Compensation Value）等价于降低曝光值（EV），会增加图像传感器接收到的光量。相机通过调整绝对曝光时间和／或光圈来实现曝光补偿。

<a id="ga7e2ce049ed534e1c29ac47d33013e180"></a>

### `VIDEO_CID_AUTO_WHITE_BALANCE`

```c
#define VIDEO_CID_AUTO_WHITE_BALANCE (VIDEO_CID_BASE + 12)
```

```c
#include <zephyr/video/controls.h>
```

自动白平衡（Automatic White Balance），用于摄像头。

<a id="ga46bb41b012b1a2240270817b9ce57637"></a>

### `VIDEO_CID_AUTOBRIGHTNESS`

```c
#define VIDEO_CID_AUTOBRIGHTNESS (VIDEO_CID_BASE + 32)
```

```c
#include <zephyr/video/controls.h>
```

启用自动亮度（Automatic Brightness）。

<a id="gac1c1d3580b7ff84b6a461cea0b3942e8"></a>

### `VIDEO_CID_AUTOGAIN`

```c
#define VIDEO_CID_AUTOGAIN (VIDEO_CID_BASE + 18)
```

```c
#include <zephyr/video/controls.h>
```

自动增益控制（Automatic Gain Control）。

<a id="ga2f22b11b526154e66440eca74ec5bd66"></a>

### `VIDEO_CID_BACKLIGHT_COMPENSATION`

```c
#define VIDEO_CID_BACKLIGHT_COMPENSATION (VIDEO_CID_BASE + 28)
```

```c
#include <zephyr/video/controls.h>
```

调整摄像头的背光补偿（Backlight Compensation）。

最小值会禁用背光补偿（Backlight Compensation）。

<a id="ga5d2c02644e26f6a7f9887d5879231106"></a>

### `VIDEO_CID_BAND_STOP_FILTER`

```c
#define VIDEO_CID_BAND_STOP_FILTER (VIDEO_CID_BASE + 33)
```

```c
#include <zephyr/video/controls.h>
```

开启或关闭摄像头传感器的带阻滤波器（Band-stop Filter），或指定其强度。

例如，可以使用此类带阻滤波器（Band-Stop Filters）滤除荧光灯成分。

<a id="ga4b56ce06ae4f6ca5b7ac9fd5a7b21319"></a>

### `VIDEO_CID_BASE`

```c
#define VIDEO_CID_BASE 0x00980900
```

```c
#include <zephyr/video/controls.h>
```

<a id="gaf4d38f5eed6feb9ef9509c1747a332b8"></a>

### `VIDEO_CID_BLUE_BALANCE`

```c
#define VIDEO_CID_BLUE_BALANCE (VIDEO_CID_BASE + 15)
```

```c
#include <zephyr/video/controls.h>
```

蓝色色度平衡（Blue Chroma Balance），表示为相对于绿色通道的比值。

<a id="ga1529eeb7c36bfe53e3916dbd9c6f5b1e"></a>

### `VIDEO_CID_BRIGHTNESS`

```c
#define VIDEO_CID_BRIGHTNESS (VIDEO_CID_BASE + 0)
```

```c
#include <zephyr/video/controls.h>
```

图像亮度（Brightness），更准确地说是黑电平（Black Level）。

<a id="ga0a6e2c6287a67e8aa174bb0130fe4c26"></a>

### `VIDEO_CID_CAMERA_CLASS_BASE`

```c
#define VIDEO_CID_CAMERA_CLASS_BASE 0x009a0900
```

```c
#include <zephyr/video/controls.h>
```

<a id="ga57e5c3f562683a2b7ea1f96a58f633be"></a>

### `VIDEO_CID_CAMERA_ORIENTATION`

```c
#define VIDEO_CID_CAMERA_ORIENTATION (VIDEO_CID_CAMERA_CLASS_BASE + 34)
```

```c
#include <zephyr/video/controls.h>
```

此只读控制（Read-only Control）描述摄像头在设备上的位置，即摄像头在设备上的安装位置（Mounting Position）。

此控制项对朝向明确的设备尤其有意义，例如手机、笔记本电脑和便携设备，因为它表示相对于设备预期使用朝向的位置。原文后一句缺少主语，仅保留了“, or ,”，并指出这些对象属于 `VIDEO_CAMERA_ORIENTATION_EXTERNAL` 朝向（Orientation）。

<a id="ga0d48a910e8d6797842dc25b33fc3f187"></a>

### `VIDEO_CID_CAMERA_SENSOR_ROTATION`

```c
#define VIDEO_CID_CAMERA_SENSOR_ROTATION (VIDEO_CID_CAMERA_CLASS_BASE + 35)
```

```c
#include <zephyr/video/controls.h>
```

此只读控制（Read-only Control）描述传感器在设备中的朝向（Orientation）。

该值表示图像采集到内存后需要施加的逆时针旋转校正角度，单位为度（Degrees），用于补偿相机传感器的安装旋转。

<a id="gadf37e306a8d73cec4674422e74ffc85e"></a>

### `VIDEO_CID_CODEC_CLASS_BASE`

```c
#define VIDEO_CID_CODEC_CLASS_BASE 0x00990900
```

```c
#include <zephyr/video/controls.h>
```

<a id="ga3fe7778ddb5c3f945b7649379a13321e"></a>

### `VIDEO_CID_COLORFX`

```c
#define VIDEO_CID_COLORFX (VIDEO_CID_BASE + 31)
```

```c
#include <zephyr/video/controls.h>
```

选择色彩效果（Color Effect）。

<a id="ga9ca85f6b1d9add05eacb008dc4ccb2e4"></a>

### `VIDEO_CID_CONTRAST`

```c
#define VIDEO_CID_CONTRAST (VIDEO_CID_BASE + 1)
```

```c
#include <zephyr/video/controls.h>
```

图像对比度（Contrast），即亮度增益（Luma Gain）。

<a id="gaf60ad41dc4fdffde0a60e53f624e7978"></a>

### `VIDEO_CID_DIGITAL_GAIN`

```c
#define VIDEO_CID_DIGITAL_GAIN (VIDEO_CID_IMAGE_PROC_CLASS_BASE + 5)
```

```c
#include <zephyr/video/controls.h>
```

数字增益控制（Digital Gain Control）。

数字增益（Digital Gain）是所有颜色分量乘以的系数。通常实际应用的数字增益等于控制值除以某个值，例如 `0x100`；这意味着若不需要数字增益，控制值必须设为 `0x100`。无增益配置通常也是默认值。

<a id="ga24e259a6466537377b7bb8a151311ae1"></a>

### `VIDEO_CID_EXPOSURE`

```c
#define VIDEO_CID_EXPOSURE (VIDEO_CID_BASE + 17)
```

```c
#include <zephyr/video/controls.h>
```

图像传感器曝光时间（Image Sensor Exposure Time）。

<a id="ga036f78623bcae18ea9627d45d1209245"></a>

### `VIDEO_CID_EXPOSURE_ABSOLUTE`

```c
#define VIDEO_CID_EXPOSURE_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 2)
```

```c
#include <zephyr/video/controls.h>
```

确定摄像头传感器的曝光时间（Exposure Time）。

曝光时间（Exposure Time）受帧间隔（Frame Interval）限制。驱动应将数值解释为以 100 µs 为单位：1 表示 1/10000 秒，10000 表示 1 秒，100000 表示 10 秒。

<a id="gab83ae3ca7fa3da66243431d489be37bd"></a>

### `VIDEO_CID_EXPOSURE_AUTO`

```c
#define VIDEO_CID_EXPOSURE_AUTO (VIDEO_CID_CAMERA_CLASS_BASE + 1)
```

```c
#include <zephyr/video/controls.h>
```

启用曝光时间（Exposure Time）和／或光圈孔径（Iris Aperture）的自动调整。

不处于 `VIDEO_EXPOSURE_MANUAL` 时，手动更改曝光或光圈的行为未定义（Undefined）。驱动应忽略此类请求。

<a id="gaa5f2ebd1e1aef2da68be4742941c1f50"></a>

### `VIDEO_CID_EXPOSURE_AUTO_PRIORITY`

```c
#define VIDEO_CID_EXPOSURE_AUTO_PRIORITY (VIDEO_CID_CAMERA_CLASS_BASE + 3)
```

```c
#include <zephyr/video/controls.h>
```

设备是否可以在自动曝光（Auto-exposure）的影响下动态改变帧率（Frame Rate）。适用于将 `VIDEO_CID_EXPOSURE_AUTO` 设为 `VIDEO_EXPOSURE_AUTO` 或 `VIDEO_EXPOSURE_APERTURE_PRIORITY` 的情况。

默认禁用：帧率（Frame Rate）必须保持恒定。

<a id="ga9e0c8dc67fab1a80f81cd4be2e875954"></a>

### `VIDEO_CID_FLASH_CLASS_BASE`

```c
#define VIDEO_CID_FLASH_CLASS_BASE 0x009c0900
```

```c
#include <zephyr/video/controls.h>
```

<a id="ga9ce95d3c135a9221a8d0431d9df9836b"></a>

### `VIDEO_CID_FOCUS_ABSOLUTE`

```c
#define VIDEO_CID_FOCUS_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 10)
```

```c
#include <zephyr/video/controls.h>
```

此控制将摄像头焦点（Focal Point）设置到指定位置。

单位未定义。正值使焦点更靠近相机，负值使其朝无穷远（Infinity）方向移动。

<a id="ga031525e88a6c0f915903f5c9068589f4"></a>

### `VIDEO_CID_FOCUS_AUTO`

```c
#define VIDEO_CID_FOCUS_AUTO (VIDEO_CID_CAMERA_CLASS_BASE + 12)
```

```c
#include <zephyr/video/controls.h>
```

启用连续自动对焦调整（Continuous Automatic Focus Adjustments）。

启用此控制项（设为 1）时，手动调焦（Manual Focus Adjustment）的行为未定义。驱动应忽略此类请求。

<a id="ga4137146c348efdcc8088f6be1274b164"></a>

### `VIDEO_CID_FOCUS_RELATIVE`

```c
#define VIDEO_CID_FOCUS_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 11)
```

```c
#include <zephyr/video/controls.h>
```

此只写控制（Write-only Control）使摄像头焦点（Focal Point）移动指定的量。

单位未定义。正值使焦点向相机靠近，负值使其朝无穷远（Infinity）方向移动。

<a id="ga36259be44d9d08b149fd35dd28bbaf50"></a>

### `VIDEO_CID_GAIN`

```c
#define VIDEO_CID_GAIN (VIDEO_CID_BASE + 19)
```

```c
#include <zephyr/video/controls.h>
```

增益控制（Gain Control）。

多数设备仅使用此控制项控制数字增益（Digital Gain）。区分数字增益与模拟增益（Analogue Gain）的设备使用 `VIDEO_CID_DIGITAL_GAIN` 和 `VIDEO_CID_ANALOGUE_GAIN`。

<a id="ga4e38bb3fcb80b2d28fa88186b65e4fea"></a>

### `VIDEO_CID_GAMMA`

```c
#define VIDEO_CID_GAMMA (VIDEO_CID_BASE + 16)
```

```c
#include <zephyr/video/controls.h>
```

伽马调整（Gamma Adjust）。

<a id="ga59aa47b6f558ef5ae64a67f4a7ac7e31"></a>

### `VIDEO_CID_HFLIP`

```c
#define VIDEO_CID_HFLIP (VIDEO_CID_BASE + 20)
```

```c
#include <zephyr/video/controls.h>
```

水平翻转（Horizontal Flip）图像：左侧变为右侧。

<a id="ga588a1206d5046a7b9e8415db725cae81"></a>

### `VIDEO_CID_HUE`

```c
#define VIDEO_CID_HUE (VIDEO_CID_BASE + 3)
```

```c
#include <zephyr/video/controls.h>
```

色调（Hue）或色彩平衡（Color Balance）。

<a id="ga9c0df146e6064169a89bd88b10085cec"></a>

### `VIDEO_CID_HUE_AUTO`

```c
#define VIDEO_CID_HUE_AUTO (VIDEO_CID_BASE + 25)
```

```c
#include <zephyr/video/controls.h>
```

启用设备的自动色调控制（Automatic Hue Control）。

启用自动色调控制（Automatic Hue Control）时，设置 `VIDEO_CID_HUE` 的行为未定义。驱动应忽略此类请求。

<a id="ga0329342731999405d1f8d6c89470dff7"></a>

### `VIDEO_CID_IMAGE_PROC_CLASS_BASE`

```c
#define VIDEO_CID_IMAGE_PROC_CLASS_BASE 0x009f0900
```

```c
#include <zephyr/video/controls.h>
```

<a id="ga3cc32750dec0096ea873ea13e83d202e"></a>

### `VIDEO_CID_IMAGE_SOURCE_CLASS_BASE`

```c
#define VIDEO_CID_IMAGE_SOURCE_CLASS_BASE 0x009e0900
```

```c
#include <zephyr/video/controls.h>
```

<a id="ga452858d6adfec3b58db6b26c96638fb2"></a>

### `VIDEO_CID_IRIS_ABSOLUTE`

```c
#define VIDEO_CID_IRIS_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 17)
```

```c
#include <zephyr/video/controls.h>
```

此控制将摄像头光圈（Aperture）设为指定值。

单位未定义。较大值使光圈（Iris）开得更大，较小值使其收小。

<a id="ga8d1452dfe9c190f6e28e5e3dd35c52cc"></a>

### `VIDEO_CID_IRIS_RELATIVE`

```c
#define VIDEO_CID_IRIS_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 18)
```

```c
#include <zephyr/video/controls.h>
```

此只写控制（Write-only Control）使摄像头光圈（Aperture）改变指定的量。

单位未定义。正值使光圈（Iris）进一步打开一档，负值使其进一步关闭一档。

<a id="ga9281f5a61120a6de015a9bbc75ee8b91"></a>

### `VIDEO_CID_JPEG_CLASS_BASE`

```c
#define VIDEO_CID_JPEG_CLASS_BASE 0x009d0900
```

```c
#include <zephyr/video/controls.h>
```

<a id="ga883c2a761ea0f00e83c884a5b4b45eee"></a>

### `VIDEO_CID_JPEG_COMPRESSION_QUALITY`

```c
#define VIDEO_CID_JPEG_COMPRESSION_QUALITY (VIDEO_CID_JPEG_CLASS_BASE + 3)
```

```c
#include <zephyr/video/controls.h>
```

JPEG 算法的质量因子（Quality Factor，Q）；提高该值也会增大数据量。

<a id="ga829221ec6ea7348e743173ce5e6bd635"></a>

### `VIDEO_CID_LASTP1`

```c
#define VIDEO_CID_LASTP1 (VIDEO_CID_BASE + 44)
```

```c
#include <zephyr/video/controls.h>
```

最后一个基本控制标识符（Base CID）加 1。

<a id="ga2142e2819c445b70d82067a3cfb193c8"></a>

### `VIDEO_CID_LINK_FREQ`

```c
#define VIDEO_CID_LINK_FREQ (VIDEO_CID_IMAGE_PROC_CLASS_BASE + 1)
```

```c
#include <zephyr/video/controls.h>
```

链路频率（Link Frequency），适用于基于 CSI2 的设备。

<a id="ga3b45437f606b8717dcadc22d56a706da"></a>

### `VIDEO_CID_PAN_ABSOLUTE`

```c
#define VIDEO_CID_PAN_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 8)
```

```c
#include <zephyr/video/controls.h>
```

此控制（Control）使摄像头沿水平方向转到指定位置。

正值使相机向右转动（从上方观察为顺时针），负值使其向左转动。驱动应将数值解释为角秒（Arc Seconds），有效范围为 `-180 * 3600` 至 `+180 * 3600`，包含两个端点。

<a id="ga23ed465d76fc54680d1e22422b66c829"></a>

### `VIDEO_CID_PAN_RELATIVE`

```c
#define VIDEO_CID_PAN_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 4)
```

```c
#include <zephyr/video/controls.h>
```

此只写控制（Write-only Control）使摄像头沿水平方向转动指定的量。

单位未定义。正值使相机向右转动（从上方观察为顺时针），负值使其向左转动。零值不会引起运动。

<a id="ga99996bce4091e4223130d9ae5e1024cd"></a>

### `VIDEO_CID_PAN_SPEED`

```c
#define VIDEO_CID_PAN_SPEED (VIDEO_CID_CAMERA_CLASS_BASE + 32)
```

```c
#include <zephyr/video/controls.h>
```

此控制使摄像头以指定速度沿水平方向转动。

单位未定义。正值使相机向右转动（从上方观察为顺时针），负值使其向左转动。零值会停止正在进行的运动；若没有运动，则无影响。

<a id="ga6f6eaed7defdbb5f440874c7c6d0a6eb"></a>

### `VIDEO_CID_PIXEL_RATE`

```c
#define VIDEO_CID_PIXEL_RATE (VIDEO_CID_IMAGE_PROC_CLASS_BASE + 2)
```

```c
#include <zephyr/video/controls.h>
```

设备像素阵列（Pixel Array）的像素速率（Pixel Rate），单位为像素／秒。

此控制项为只读（Read-Only）。

<a id="ga762a6c2b0fb032b9ebdfeff5ed15c3de"></a>

### `VIDEO_CID_POWER_LINE_FREQUENCY`

```c
#define VIDEO_CID_POWER_LINE_FREQUENCY (VIDEO_CID_BASE + 24)
```

```c
#include <zephyr/video/controls.h>
```

需要补偿的电源线频率（Power Line Frequency）。

避免人工照明引起的闪烁（Flicker）。

<a id="ga05e2fe16eafe259061af62ac31dfaeca"></a>

### `VIDEO_CID_PRIVATE_BASE`

```c
#define VIDEO_CID_PRIVATE_BASE 0x08000000
```

```c
#include <zephyr/video/controls.h>
```

<a id="gab534e6263a6b5caae48543346ba2f7ef"></a>

### `VIDEO_CID_RED_BALANCE`

```c
#define VIDEO_CID_RED_BALANCE (VIDEO_CID_BASE + 14)
```

```c
#include <zephyr/video/controls.h>
```

红色色度平衡（Red Chroma Balance），表示为相对于绿色通道的比值。

<a id="gae7f2add167e46dffb19f33393c839c57"></a>

### `VIDEO_CID_ROTATE`

```c
#define VIDEO_CID_ROTATE (VIDEO_CID_BASE + 34)
```

```c
#include <zephyr/video/controls.h>
```

旋转控制（Rotate Control）。

将图像旋转给定角度，例如 90、180 或 270 度。

<a id="ga200017c2141f5c90ade652224d1d4364"></a>

### `VIDEO_CID_SATURATION`

```c
#define VIDEO_CID_SATURATION (VIDEO_CID_BASE + 2)
```

```c
#include <zephyr/video/controls.h>
```

图像色彩饱和度（Color Saturation），即色度增益（Chroma Gain）。

<a id="gab0509f0d3106bca07658e7cfcb1883cf"></a>

### `VIDEO_CID_SHARPNESS`

```c
#define VIDEO_CID_SHARPNESS (VIDEO_CID_BASE + 27)
```

```c
#include <zephyr/video/controls.h>
```

调整摄像头的锐化滤波器（Sharpness Filter）。

最小值会禁用滤波器（Filters），较高值产生更锐利的图像。

<a id="gad1ce88a5c071eaeb8d5db9dc722a2cd4"></a>

### `VIDEO_CID_TEST_PATTERN`

```c
#define VIDEO_CID_TEST_PATTERN (VIDEO_CID_IMAGE_PROC_CLASS_BASE + 3)
```

```c
#include <zephyr/video/controls.h>
```

选择要显示的测试图案类型（Test Pattern Type）。

<a id="gae474209914926f2bd38c99e020224b9c"></a>

### `VIDEO_CID_TILT_ABSOLUTE`

```c
#define VIDEO_CID_TILT_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 9)
```

```c
#include <zephyr/video/controls.h>
```

此控制（Control）使摄像头沿垂直方向转到指定位置。

正值使相机向上转动，负值使其向下转动。驱动应将数值解释为角秒（Arc Seconds），有效范围为 `-180 * 3600` 至 `+180 * 3600`，包含两个端点。

<a id="ga7c51639505c7b97fb1953ade5fc72534"></a>

### `VIDEO_CID_TILT_RELATIVE`

```c
#define VIDEO_CID_TILT_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 5)
```

```c
#include <zephyr/video/controls.h>
```

此只写控制（Write-only Control）使摄像头沿垂直方向转动指定的量。

单位未定义。正值使相机向上转动，负值使其向下转动。零值不会引起运动。

<a id="ga3bfeedcd519191bcf1d684fd983ca9bc"></a>

### `VIDEO_CID_TILT_SPEED`

```c
#define VIDEO_CID_TILT_SPEED (VIDEO_CID_CAMERA_CLASS_BASE + 33)
```

```c
#include <zephyr/video/controls.h>
```

此控制使摄像头以指定速度沿垂直方向转动。

单位未定义。正值使相机向上转动，负值使其向下转动。零值会停止正在进行的运动；若没有运动，则无影响。

<a id="ga16651a6825b619399a333ed39e802dfc"></a>

### `VIDEO_CID_VFLIP`

```c
#define VIDEO_CID_VFLIP (VIDEO_CID_BASE + 21)
```

```c
#include <zephyr/video/controls.h>
```

垂直翻转（Vertical Flip）图像：上方变为下方。

<a id="ga0670d89542dc532a9c775e8e9c2638b1"></a>

### `VIDEO_CID_WHITE_BALANCE_TEMPERATURE`

```c
#define VIDEO_CID_WHITE_BALANCE_TEMPERATURE (VIDEO_CID_BASE + 26)
```

```c
#include <zephyr/video/controls.h>
```

以开尔文（Kelvin）色温表示的白平衡设置（White Balance Settings）。

驱动应至少覆盖从 2800（白炽灯，Incandescent）到 6500（日光，Daylight）的范围。

<a id="ga9d224bc93e5c23317f9ccf89713a18d6"></a>

### `VIDEO_CID_WIDE_DYNAMIC_RANGE`

```c
#define VIDEO_CID_WIDE_DYNAMIC_RANGE (VIDEO_CID_CAMERA_CLASS_BASE + 21)
```

```c
#include <zephyr/video/controls.h>
```

启用或禁用摄像头的宽动态范围（Wide Dynamic Range）功能。

此功能可在场景中照明强度差异明显、即同时存在极暗和极亮区域的情况下获得清晰图像。相机通常通过合并曝光时间不同的两个连续帧来实现它。

<a id="ga1033858d5515c2016a0cc6ac06fd8b91"></a>

### `VIDEO_CID_ZOOM_ABSOLUTE`

```c
#define VIDEO_CID_ZOOM_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 13)
```

```c
#include <zephyr/video/controls.h>
```

以绝对值指定物镜焦距（Objective Lens Focal Length）。

变焦（Zoom）单位由驱动决定，其值应为正整数。

<a id="ga1a79541da7b7a37d9358fb1a3c42a1b7"></a>

### `VIDEO_CID_ZOOM_CONTINUOUS`

```c
#define VIDEO_CID_ZOOM_CONTINUOUS (VIDEO_CID_CAMERA_CLASS_BASE + 15)
```

```c
#include <zephyr/video/controls.h>
```

启动连续变焦运动（Continuous Zoom Movement）。

以指定速度移动物镜组，直到到达设备的物理限位，或收到明确的停止运动请求。正值使变焦镜组朝长焦（Telephoto）方向移动，零值停止变焦镜组运动，负值使其朝广角（Wide-Angle）方向移动。变焦速度单位由驱动决定。

<a id="ga40e76f27e97549a779a6581bd210b0f4"></a>

### `VIDEO_CID_ZOOM_RELATIVE`

```c
#define VIDEO_CID_ZOOM_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 14)
```

```c
#include <zephyr/video/controls.h>
```

此只写控制（Write-only Control）相对于当前值设置物镜焦距（Objective Lens Focal Length）。

正值使变焦镜组朝长焦（Telephoto）方向移动，负值使其朝广角（Wide-Angle）方向移动。变焦单位由驱动决定。

<a id="ga6fc7bcd4b280b4598ea3a03108881b5c"></a>

### `VIDEO_CTRL_FLAG_NEXT_CTRL`

```c
#define VIDEO_CTRL_FLAG_NEXT_CTRL 0x80000000
```

```c
#include <zephyr/video/controls.h>
```

<a id="ga1fb4e9981b362010439b9419691ac2af"></a>

### `video_camera_orientation`

```c
enum video_camera_orientation
```

```c
#include <zephyr/video/controls.h>
```

视频摄像头朝向（Video Camera Orientation）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VIDEO_CAMERA_ORIENTATION_FRONT` | 安装在手机／平板电脑／笔记本电脑面向用户一侧的相机（User-Facing Camera）。 |
| `VIDEO_CAMERA_ORIENTATION_BACK` | 安装在背离用户一侧的相机（Camera on the Opposite Side）。 |
| `VIDEO_CAMERA_ORIENTATION_EXTERNAL` | 未直接固定于设备、或可以自由移动的相机传感器（Camera Sensors）。 |

<a id="ga99f4b6cf21c8baaf510fbcfccb645960"></a>

### `video_colorfx`

```c
enum video_colorfx
```

```c
#include <zephyr/video/controls.h>
```

视频色彩效果（Video Color Effects）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VIDEO_COLORFX_NONE` | 无颜色效果（No Color Effect）。 |
| `VIDEO_COLORFX_BW` | 黑白效果（Black and White）。 |
| `VIDEO_COLORFX_SEPIA` | 棕褐色调效果（Sepia Tone）。 |
| `VIDEO_COLORFX_NEGATIVE` | 负片效果（Negative Image）。 |
| `VIDEO_COLORFX_EMBOSS` | 浮雕效果（Emboss）。 |
| `VIDEO_COLORFX_SKETCH` | 素描／绘画效果（Sketch/Drawing）。 |
| `VIDEO_COLORFX_SKY_BLUE` | 天蓝色调效果（Sky Blue Tint）。 |
| `VIDEO_COLORFX_GRASS_GREEN` | 草绿色调效果（Grass Green Tint）。 |
| `VIDEO_COLORFX_SKIN_WHITEN` | 皮肤美白效果（Skin Whitening）。 |
| `VIDEO_COLORFX_VIVID` | 鲜艳／明亮色彩效果（Vivid/Bright Color）。 |
| `VIDEO_COLORFX_AQUA` | 水蓝（蓝绿色）效果（Aqua）。 |
| `VIDEO_COLORFX_ART_FREEZE` | 艺术冻结／风格化效果（Art Freeze/Stylized）。 |
| `VIDEO_COLORFX_SILHOUETTE` | 剪影效果（Silhouette）。 |
| `VIDEO_COLORFX_SOLARIZATION` | 中途曝光效果（Solarization）。 |
| `VIDEO_COLORFX_ANTIQUE` | 仿古／复古效果（Antique/Vintage）。 |

<a id="ga167cf84b8f4259e6cdd333748deafaf6"></a>

### `video_exposure_type`

```c
enum video_exposure_type
```

```c
#include <zephyr/video/controls.h>
```

视频曝光类型（Video Exposure Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VIDEO_EXPOSURE_AUTO` | 自动曝光（Automatic Exposure）。 |
| `VIDEO_EXPOSURE_MANUAL` | 手动曝光（Manual Exposure）。 |
| `VIDEO_EXPOSURE_SHUTTER_PRIORITY` | 快门优先（Shutter Priority）。 |
| `VIDEO_EXPOSURE_APERTURE_PRIORITY` | 光圈优先（Aperture Priority）。 |

<a id="ga9db809ab56484b4b5b1a047a97e6920a"></a>

### `video_power_line_frequency`

```c
enum video_power_line_frequency
```

```c
#include <zephyr/video/controls.h>
```

视频电源线频率（Video Power Line Frequency）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VIDEO_CID_POWER_LINE_FREQUENCY_DISABLED` | 禁用电源频率（Power Line Frequency）设置。 |
| `VIDEO_CID_POWER_LINE_FREQUENCY_50HZ` | 电源频率（Power Line Frequency）为 50 Hz。 |
| `VIDEO_CID_POWER_LINE_FREQUENCY_60HZ` | 电源频率（Power Line Frequency）为 60 Hz。 |
| `VIDEO_CID_POWER_LINE_FREQUENCY_AUTO` | 自动选择电源频率（Automatic Power Line Frequency）。 |


## 9.12\_原页交叉引用（Cross References）

- [controls.h](../api_file_usb_network_reference/P005_zephyr__video__controls.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga1fb4e9981b362010439b9419691ac2afa76b044aa6d822af9844632761fefbaef"></a>
<a id="gga1fb4e9981b362010439b9419691ac2afa831cc750dfcb43f74eb3a7ee59b33072"></a>
<a id="gga1fb4e9981b362010439b9419691ac2afafcc44933e74389bef0e1f20b7998f594"></a>
<a id="gga99f4b6cf21c8baaf510fbcfccb645960a9960e8b54cf9070c04664246e67f3237"></a>
<a id="gga99f4b6cf21c8baaf510fbcfccb645960a52f62a92f6f0e158b1797719efb79735"></a>
<a id="gga99f4b6cf21c8baaf510fbcfccb645960a483faa51fb4728b89c1a8da60b139a37"></a>
<a id="gga99f4b6cf21c8baaf510fbcfccb645960ac9367e073eef47865d90ba9ae6eb98a0"></a>
<a id="gga99f4b6cf21c8baaf510fbcfccb645960aae3d42f32c4f14e371343a32e8132cc0"></a>
<a id="gga99f4b6cf21c8baaf510fbcfccb645960a789155f47a0302661a71155c1e6045fc"></a>
<a id="gga99f4b6cf21c8baaf510fbcfccb645960a09b5346a7431c2c0e7415037ee5a6f8b"></a>
<a id="gga99f4b6cf21c8baaf510fbcfccb645960abd0ddf263af2224bebe12da19711c6a1"></a>
<a id="gga99f4b6cf21c8baaf510fbcfccb645960a3d4856179a0279a23f1597c3c0a615ef"></a>
<a id="gga99f4b6cf21c8baaf510fbcfccb645960a5e77aa2b5530062aaaf1156a340e3826"></a>
<a id="gga99f4b6cf21c8baaf510fbcfccb645960adb9e16ef9511c8eec1d6dbead4843a4c"></a>
<a id="gga99f4b6cf21c8baaf510fbcfccb645960a00faf2d7d366f0109d64568839416ccd"></a>
<a id="gga99f4b6cf21c8baaf510fbcfccb645960a1c93819be559612ccea3a2781cbb7d25"></a>
<a id="gga99f4b6cf21c8baaf510fbcfccb645960a2f6f282e1e195bdc29aa6a351c2bc715"></a>
<a id="gga99f4b6cf21c8baaf510fbcfccb645960a71acc838d9197b671accab7763c5388b"></a>
<a id="gga167cf84b8f4259e6cdd333748deafaf6ab77bff3e8a2abd1c823dbb4324e8499b"></a>
<a id="gga167cf84b8f4259e6cdd333748deafaf6a66ab6044a5961bc14e1ab718d1a91224"></a>
<a id="gga167cf84b8f4259e6cdd333748deafaf6ac92a826dee7a328bb0b43857d6c09c61"></a>
<a id="gga167cf84b8f4259e6cdd333748deafaf6a8abeb9fbd3156edf9f3057692829cbcd"></a>
<a id="gga9db809ab56484b4b5b1a047a97e6920aa596b3bec6771ef15392bfcee9fc47f93"></a>
<a id="gga9db809ab56484b4b5b1a047a97e6920aad47b0f6914d0e949d17faa61b9fc2c10"></a>
<a id="gga9db809ab56484b4b5b1a047a97e6920aad34ec7a0db40ee5b1dbfc6de79834796"></a>
<a id="gga9db809ab56484b4b5b1a047a97e6920aa817468b493999a2ba979a249bc0cffe0"></a>

---

[上一章](P008_系统管理总线（SMBus）.md) · [返回大纲](大纲.md)
