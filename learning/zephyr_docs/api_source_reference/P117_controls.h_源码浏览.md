---
id: learning.zephyr-docs.api-source-reference.page-117
title: controls.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/controls_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第117章\_controls.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/controls_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/controls_8h.html)。

## 117.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="foldopen00098"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="foldopen00132"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00177"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00187"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="foldopen00203"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="foldopen00346"></a>
<a id="l00346"></a>
<a id="l00348"></a>
<a id="l00350"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00365"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00375"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00388"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00407"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00437"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00447"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="agroup__video__control__ids_html_ga167cf84b8f4259e6cdd333748deafaf6"></a>
<a id="agroup__video__control__ids_html_ga1fb4e9981b362010439b9419691ac2af"></a>
<a id="agroup__video__control__ids_html_ga99f4b6cf21c8baaf510fbcfccb645960"></a>
<a id="agroup__video__control__ids_html_ga9db809ab56484b4b5b1a047a97e6920a"></a>
<a id="agroup__video__control__ids_html_gga167cf84b8f4259e6cdd333748deafaf6a66ab6044a5961bc14e1ab718d1a91224"></a>
<a id="agroup__video__control__ids_html_gga167cf84b8f4259e6cdd333748deafaf6a8abeb9fbd3156edf9f3057692829cbcd"></a>
<a id="agroup__video__control__ids_html_gga167cf84b8f4259e6cdd333748deafaf6ab77bff3e8a2abd1c823dbb4324e8499b"></a>
<a id="agroup__video__control__ids_html_gga167cf84b8f4259e6cdd333748deafaf6ac92a826dee7a328bb0b43857d6c09c61"></a>
<a id="agroup__video__control__ids_html_gga1fb4e9981b362010439b9419691ac2afa76b044aa6d822af9844632761fefbaef"></a>
<a id="agroup__video__control__ids_html_gga1fb4e9981b362010439b9419691ac2afa831cc750dfcb43f74eb3a7ee59b33072"></a>
<a id="agroup__video__control__ids_html_gga1fb4e9981b362010439b9419691ac2afafcc44933e74389bef0e1f20b7998f594"></a>
<a id="agroup__video__control__ids_html_gga99f4b6cf21c8baaf510fbcfccb645960a00faf2d7d366f0109d64568839416ccd"></a>
<a id="agroup__video__control__ids_html_gga99f4b6cf21c8baaf510fbcfccb645960a09b5346a7431c2c0e7415037ee5a6f8b"></a>
<a id="agroup__video__control__ids_html_gga99f4b6cf21c8baaf510fbcfccb645960a1c93819be559612ccea3a2781cbb7d25"></a>
<a id="agroup__video__control__ids_html_gga99f4b6cf21c8baaf510fbcfccb645960a2f6f282e1e195bdc29aa6a351c2bc715"></a>
<a id="agroup__video__control__ids_html_gga99f4b6cf21c8baaf510fbcfccb645960a3d4856179a0279a23f1597c3c0a615ef"></a>
<a id="agroup__video__control__ids_html_gga99f4b6cf21c8baaf510fbcfccb645960a483faa51fb4728b89c1a8da60b139a37"></a>
<a id="agroup__video__control__ids_html_gga99f4b6cf21c8baaf510fbcfccb645960a52f62a92f6f0e158b1797719efb79735"></a>
<a id="agroup__video__control__ids_html_gga99f4b6cf21c8baaf510fbcfccb645960a5e77aa2b5530062aaaf1156a340e3826"></a>
<a id="agroup__video__control__ids_html_gga99f4b6cf21c8baaf510fbcfccb645960a71acc838d9197b671accab7763c5388b"></a>
<a id="agroup__video__control__ids_html_gga99f4b6cf21c8baaf510fbcfccb645960a789155f47a0302661a71155c1e6045fc"></a>
<a id="agroup__video__control__ids_html_gga99f4b6cf21c8baaf510fbcfccb645960a9960e8b54cf9070c04664246e67f3237"></a>
<a id="agroup__video__control__ids_html_gga99f4b6cf21c8baaf510fbcfccb645960aae3d42f32c4f14e371343a32e8132cc0"></a>
<a id="agroup__video__control__ids_html_gga99f4b6cf21c8baaf510fbcfccb645960abd0ddf263af2224bebe12da19711c6a1"></a>
<a id="agroup__video__control__ids_html_gga99f4b6cf21c8baaf510fbcfccb645960ac9367e073eef47865d90ba9ae6eb98a0"></a>
<a id="agroup__video__control__ids_html_gga99f4b6cf21c8baaf510fbcfccb645960adb9e16ef9511c8eec1d6dbead4843a4c"></a>
<a id="agroup__video__control__ids_html_gga9db809ab56484b4b5b1a047a97e6920aa596b3bec6771ef15392bfcee9fc47f93"></a>
<a id="agroup__video__control__ids_html_gga9db809ab56484b4b5b1a047a97e6920aa817468b493999a2ba979a249bc0cffe0"></a>
<a id="agroup__video__control__ids_html_gga9db809ab56484b4b5b1a047a97e6920aad34ec7a0db40ee5b1dbfc6de79834796"></a>
<a id="agroup__video__control__ids_html_gga9db809ab56484b4b5b1a047a97e6920aad47b0f6914d0e949d17faa61b9fc2c10"></a>
<a id="astdint_8h_html"></a>

```c
/*
 * Copyright (c) 2019 Linaro Limited.
 * Copyright (c) 2024 tinyVision.ai Inc.
 * Copyright 2025 NXP
 * SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_VIDEO_CONTROLS_H
#define ZEPHYR_INCLUDE_VIDEO_CONTROLS_H


#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

#define VIDEO_CID_BASE 0x00980900

#define VIDEO_CID_BRIGHTNESS (VIDEO_CID_BASE + 0)

#define VIDEO_CID_CONTRAST (VIDEO_CID_BASE + 1)

#define VIDEO_CID_SATURATION (VIDEO_CID_BASE + 2)

#define VIDEO_CID_HUE (VIDEO_CID_BASE + 3)

#define VIDEO_CID_AUTO_WHITE_BALANCE (VIDEO_CID_BASE + 12)

#define VIDEO_CID_RED_BALANCE (VIDEO_CID_BASE + 14)

#define VIDEO_CID_BLUE_BALANCE (VIDEO_CID_BASE + 15)

#define VIDEO_CID_GAMMA (VIDEO_CID_BASE + 16)

#define VIDEO_CID_EXPOSURE (VIDEO_CID_BASE + 17)

#define VIDEO_CID_AUTOGAIN (VIDEO_CID_BASE + 18)

#define VIDEO_CID_GAIN (VIDEO_CID_BASE + 19)

#define VIDEO_CID_HFLIP (VIDEO_CID_BASE + 20)

#define VIDEO_CID_VFLIP (VIDEO_CID_BASE + 21)

#define VIDEO_CID_POWER_LINE_FREQUENCY (VIDEO_CID_BASE + 24)

enum video_power_line_frequency {
        VIDEO_CID_POWER_LINE_FREQUENCY_DISABLED = 0,
        VIDEO_CID_POWER_LINE_FREQUENCY_50HZ = 1,
        VIDEO_CID_POWER_LINE_FREQUENCY_60HZ = 2,
        VIDEO_CID_POWER_LINE_FREQUENCY_AUTO = 3,
};

#define VIDEO_CID_HUE_AUTO (VIDEO_CID_BASE + 25)

#define VIDEO_CID_WHITE_BALANCE_TEMPERATURE (VIDEO_CID_BASE + 26)

#define VIDEO_CID_SHARPNESS (VIDEO_CID_BASE + 27)

#define VIDEO_CID_BACKLIGHT_COMPENSATION (VIDEO_CID_BASE + 28)

#define VIDEO_CID_COLORFX (VIDEO_CID_BASE + 31)

enum video_colorfx {
        VIDEO_COLORFX_NONE = 0,
        VIDEO_COLORFX_BW = 1,
        VIDEO_COLORFX_SEPIA = 2,
        VIDEO_COLORFX_NEGATIVE = 3,
        VIDEO_COLORFX_EMBOSS = 4,
        VIDEO_COLORFX_SKETCH = 5,
        VIDEO_COLORFX_SKY_BLUE = 6,
        VIDEO_COLORFX_GRASS_GREEN = 7,
        VIDEO_COLORFX_SKIN_WHITEN = 8,
        VIDEO_COLORFX_VIVID = 9,
        VIDEO_COLORFX_AQUA = 10,
        VIDEO_COLORFX_ART_FREEZE = 11,
        VIDEO_COLORFX_SILHOUETTE = 12,
        VIDEO_COLORFX_SOLARIZATION = 13,
        VIDEO_COLORFX_ANTIQUE = 14,
};

#define VIDEO_CID_AUTOBRIGHTNESS (VIDEO_CID_BASE + 32)

#define VIDEO_CID_BAND_STOP_FILTER (VIDEO_CID_BASE + 33)

#define VIDEO_CID_ROTATE (VIDEO_CID_BASE + 34)

#define VIDEO_CID_ALPHA_COMPONENT (VIDEO_CID_BASE + 41)

#define VIDEO_CID_LASTP1 (VIDEO_CID_BASE + 44)


#define VIDEO_CID_CODEC_CLASS_BASE 0x00990900


#define VIDEO_CID_CAMERA_CLASS_BASE 0x009a0900

#define VIDEO_CID_EXPOSURE_AUTO (VIDEO_CID_CAMERA_CLASS_BASE + 1)

enum video_exposure_type {
        VIDEO_EXPOSURE_AUTO = 0,
        VIDEO_EXPOSURE_MANUAL = 1,
        VIDEO_EXPOSURE_SHUTTER_PRIORITY = 2,
        VIDEO_EXPOSURE_APERTURE_PRIORITY = 3
};

#define VIDEO_CID_EXPOSURE_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 2)

#define VIDEO_CID_EXPOSURE_AUTO_PRIORITY (VIDEO_CID_CAMERA_CLASS_BASE + 3)

#define VIDEO_CID_PAN_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 4)

#define VIDEO_CID_TILT_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 5)

#define VIDEO_CID_PAN_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 8)

#define VIDEO_CID_TILT_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 9)

#define VIDEO_CID_FOCUS_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 10)

#define VIDEO_CID_FOCUS_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 11)

#define VIDEO_CID_FOCUS_AUTO (VIDEO_CID_CAMERA_CLASS_BASE + 12)

#define VIDEO_CID_ZOOM_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 13)

#define VIDEO_CID_ZOOM_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 14)

#define VIDEO_CID_ZOOM_CONTINUOUS (VIDEO_CID_CAMERA_CLASS_BASE + 15)

#define VIDEO_CID_IRIS_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 17)

#define VIDEO_CID_IRIS_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 18)

#define VIDEO_CID_AUTO_EXPOSURE_BIAS (VIDEO_CID_CAMERA_CLASS_BASE + 19)

#define VIDEO_CID_WIDE_DYNAMIC_RANGE (VIDEO_CID_CAMERA_CLASS_BASE + 21)

#define VIDEO_CID_PAN_SPEED (VIDEO_CID_CAMERA_CLASS_BASE + 32)

#define VIDEO_CID_TILT_SPEED (VIDEO_CID_CAMERA_CLASS_BASE + 33)

#define VIDEO_CID_CAMERA_ORIENTATION (VIDEO_CID_CAMERA_CLASS_BASE + 34)

enum video_camera_orientation {
        VIDEO_CAMERA_ORIENTATION_FRONT = 0,
        VIDEO_CAMERA_ORIENTATION_BACK = 1,
        VIDEO_CAMERA_ORIENTATION_EXTERNAL = 2,
};

#define VIDEO_CID_CAMERA_SENSOR_ROTATION (VIDEO_CID_CAMERA_CLASS_BASE + 35)


#define VIDEO_CID_FLASH_CLASS_BASE 0x009c0900


#define VIDEO_CID_JPEG_CLASS_BASE 0x009d0900

#define VIDEO_CID_JPEG_COMPRESSION_QUALITY (VIDEO_CID_JPEG_CLASS_BASE + 3)


#define VIDEO_CID_IMAGE_SOURCE_CLASS_BASE 0x009e0900

#define VIDEO_CID_ANALOGUE_GAIN (VIDEO_CID_IMAGE_SOURCE_CLASS_BASE + 3)


#define VIDEO_CID_IMAGE_PROC_CLASS_BASE 0x009f0900

#define VIDEO_CID_LINK_FREQ (VIDEO_CID_IMAGE_PROC_CLASS_BASE + 1)

#define VIDEO_CID_PIXEL_RATE (VIDEO_CID_IMAGE_PROC_CLASS_BASE + 2)

#define VIDEO_CID_TEST_PATTERN (VIDEO_CID_IMAGE_PROC_CLASS_BASE + 3)

#define VIDEO_CID_DIGITAL_GAIN (VIDEO_CID_IMAGE_PROC_CLASS_BASE + 5)


#define VIDEO_CID_PRIVATE_BASE 0x08000000


#define VIDEO_CTRL_FLAG_NEXT_CTRL 0x80000000


#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_VIDEO_CONTROLS_H */
```

## 117.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Linaro Limited.。

版权（Copyright）：© 2024 tinyVision.ai Inc.。

版权（Copyright）：2025 NXP。

SPDX 文件版权声明（FileCopyrightText）：Copyright The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 466 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_VIDEO_CONTROLS_H`。

## 117.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/controls_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [video_power_line_frequency](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga9db809ab56484b4b5b1a047a97e6920a)
- [VIDEO_CID_POWER_LINE_FREQUENCY_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga9db809ab56484b4b5b1a047a97e6920aa596b3bec6771ef15392bfcee9fc47f93)
- [VIDEO_CID_POWER_LINE_FREQUENCY_50HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga9db809ab56484b4b5b1a047a97e6920aad47b0f6914d0e949d17faa61b9fc2c10)
- [VIDEO_CID_POWER_LINE_FREQUENCY_60HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga9db809ab56484b4b5b1a047a97e6920aad34ec7a0db40ee5b1dbfc6de79834796)
- [VIDEO_CID_POWER_LINE_FREQUENCY_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga9db809ab56484b4b5b1a047a97e6920aa817468b493999a2ba979a249bc0cffe0)
- [video_colorfx](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga99f4b6cf21c8baaf510fbcfccb645960)
- [VIDEO_COLORFX_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a9960e8b54cf9070c04664246e67f3237)
- [VIDEO_COLORFX_BW](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a52f62a92f6f0e158b1797719efb79735)
- [VIDEO_COLORFX_SEPIA](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a483faa51fb4728b89c1a8da60b139a37)
- [VIDEO_COLORFX_NEGATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960ac9367e073eef47865d90ba9ae6eb98a0)
- [VIDEO_COLORFX_EMBOSS](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960aae3d42f32c4f14e371343a32e8132cc0)
- [VIDEO_COLORFX_SKETCH](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a789155f47a0302661a71155c1e6045fc)
- [VIDEO_COLORFX_SKY_BLUE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a09b5346a7431c2c0e7415037ee5a6f8b)
- [VIDEO_COLORFX_GRASS_GREEN](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960abd0ddf263af2224bebe12da19711c6a1)
- [VIDEO_COLORFX_SKIN_WHITEN](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a3d4856179a0279a23f1597c3c0a615ef)
- [VIDEO_COLORFX_VIVID](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a5e77aa2b5530062aaaf1156a340e3826)
- [VIDEO_COLORFX_AQUA](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960adb9e16ef9511c8eec1d6dbead4843a4c)
- [VIDEO_COLORFX_ART_FREEZE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a00faf2d7d366f0109d64568839416ccd)
- [VIDEO_COLORFX_SILHOUETTE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a1c93819be559612ccea3a2781cbb7d25)
- [VIDEO_COLORFX_SOLARIZATION](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a2f6f282e1e195bdc29aa6a351c2bc715)
- [VIDEO_COLORFX_ANTIQUE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a71acc838d9197b671accab7763c5388b)
- [video_exposure_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga167cf84b8f4259e6cdd333748deafaf6)
- [VIDEO_EXPOSURE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga167cf84b8f4259e6cdd333748deafaf6ab77bff3e8a2abd1c823dbb4324e8499b)
- [VIDEO_EXPOSURE_MANUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga167cf84b8f4259e6cdd333748deafaf6a66ab6044a5961bc14e1ab718d1a91224)
- [VIDEO_EXPOSURE_SHUTTER_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga167cf84b8f4259e6cdd333748deafaf6ac92a826dee7a328bb0b43857d6c09c61)
- [VIDEO_EXPOSURE_APERTURE_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga167cf84b8f4259e6cdd333748deafaf6a8abeb9fbd3156edf9f3057692829cbcd)
- [video_camera_orientation](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga1fb4e9981b362010439b9419691ac2af)
- [VIDEO_CAMERA_ORIENTATION_FRONT](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga1fb4e9981b362010439b9419691ac2afa76b044aa6d822af9844632761fefbaef)
- [VIDEO_CAMERA_ORIENTATION_BACK](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga1fb4e9981b362010439b9419691ac2afa831cc750dfcb43f74eb3a7ee59b33072)
- [VIDEO_CAMERA_ORIENTATION_EXTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga1fb4e9981b362010439b9419691ac2afafcc44933e74389bef0e1f20b7998f594)

---

[上一章](P116_tty.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P118_cpu_freq.h_源码浏览.md)
