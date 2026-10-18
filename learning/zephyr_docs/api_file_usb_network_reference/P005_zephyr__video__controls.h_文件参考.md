---
id: learning.zephyr-docs.api-file-usb-network-reference.page-5
title: zephyr__video__controls.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/controls_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_video\_\_controls.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/controls_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频控制ID（Video Control IDs）定义的主头文件。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

视频控制ID（Video Control IDs）定义的主头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 有状态编解码器控制标识符（Stateful Codec Control IDs）

<a id="r_gadf37e306a8d73cec4674422e74ffc85e"></a>

```c
#define VIDEO_CID_CODEC_CLASS_BASE 0x00990900
```

相关声明：[VIDEO_CID_CODEC_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gadf37e306a8d73cec4674422e74ffc85e)。

<a id="define-members-1"></a>

### 摄像头闪光灯类控制标识符（Camera Flash Class Control IDs）

<a id="r_ga9e0c8dc67fab1a80f81cd4be2e875954"></a>

```c
#define VIDEO_CID_FLASH_CLASS_BASE 0x009c0900
```

相关声明：[VIDEO_CID_FLASH_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga9e0c8dc67fab1a80f81cd4be2e875954)。

<a id="define-members-2"></a>

### JPEG 类控制标识符（JPEG Class Control IDs）

<a id="r_ga9281f5a61120a6de015a9bbc75ee8b91"></a>

```c
#define VIDEO_CID_JPEG_CLASS_BASE 0x009d0900
```

相关声明：[VIDEO_CID_JPEG_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga9281f5a61120a6de015a9bbc75ee8b91)。

<a id="r_ga883c2a761ea0f00e83c884a5b4b45eee"></a>

```c
#define VIDEO_CID_JPEG_COMPRESSION_QUALITY (VIDEO_CID_JPEG_CLASS_BASE + 3)
```

相关声明：[VIDEO_CID_JPEG_COMPRESSION_QUALITY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga883c2a761ea0f00e83c884a5b4b45eee)、[VIDEO_CID_JPEG_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga9281f5a61120a6de015a9bbc75ee8b91)。

JPEG 算法的质量因子（Quality Factor，Q）；提高该值也会增大数据量。

<a id="define-members-3"></a>

### 图像源类控制标识符（Image Source Class Control IDs）

<a id="r_ga3cc32750dec0096ea873ea13e83d202e"></a>

```c
#define VIDEO_CID_IMAGE_SOURCE_CLASS_BASE 0x009e0900
```

相关声明：[VIDEO_CID_IMAGE_SOURCE_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga3cc32750dec0096ea873ea13e83d202e)。

<a id="r_ga41b451aace98fb81633983a413d2724f"></a>

```c
#define VIDEO_CID_ANALOGUE_GAIN (VIDEO_CID_IMAGE_SOURCE_CLASS_BASE + 3)
```

相关声明：[VIDEO_CID_ANALOGUE_GAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga41b451aace98fb81633983a413d2724f)、[VIDEO_CID_IMAGE_SOURCE_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga3cc32750dec0096ea873ea13e83d202e)。

模拟增益控制（Analogue Gain Control）。

<a id="define-members-4"></a>

### 图像处理类控制标识符（Image Processing Class Control IDs）

<a id="r_ga0329342731999405d1f8d6c89470dff7"></a>

```c
#define VIDEO_CID_IMAGE_PROC_CLASS_BASE 0x009f0900
```

相关声明：[VIDEO_CID_IMAGE_PROC_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0329342731999405d1f8d6c89470dff7)。

<a id="r_ga2142e2819c445b70d82067a3cfb193c8"></a>

```c
#define VIDEO_CID_LINK_FREQ (VIDEO_CID_IMAGE_PROC_CLASS_BASE + 1)
```

相关声明：[`VIDEO_CID_LINK_FREQ`（链路频率）。](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga2142e2819c445b70d82067a3cfb193c8)、[VIDEO_CID_IMAGE_PROC_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0329342731999405d1f8d6c89470dff7)。

链路频率（Link Frequency），适用于基于 CSI2 的设备。

<a id="r_ga6f6eaed7defdbb5f440874c7c6d0a6eb"></a>

```c
#define VIDEO_CID_PIXEL_RATE (VIDEO_CID_IMAGE_PROC_CLASS_BASE + 2)
```

相关声明：[`VIDEO_CID_PIXEL_RATE`（像素速率）。](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga6f6eaed7defdbb5f440874c7c6d0a6eb)、[VIDEO_CID_IMAGE_PROC_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0329342731999405d1f8d6c89470dff7)。

设备像素阵列（Pixel Array）的像素速率（Pixel Rate），单位为像素／秒。

<a id="r_gad1ce88a5c071eaeb8d5db9dc722a2cd4"></a>

```c
#define VIDEO_CID_TEST_PATTERN (VIDEO_CID_IMAGE_PROC_CLASS_BASE + 3)
```

相关声明：[VIDEO_CID_TEST_PATTERN](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gad1ce88a5c071eaeb8d5db9dc722a2cd4)、[VIDEO_CID_IMAGE_PROC_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0329342731999405d1f8d6c89470dff7)。

选择要显示的测试图案类型（Test Pattern Type）。

<a id="r_gaf60ad41dc4fdffde0a60e53f624e7978"></a>

```c
#define VIDEO_CID_DIGITAL_GAIN (VIDEO_CID_IMAGE_PROC_CLASS_BASE + 5)
```

相关声明：[VIDEO_CID_DIGITAL_GAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gaf60ad41dc4fdffde0a60e53f624e7978)、[VIDEO_CID_IMAGE_PROC_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0329342731999405d1f8d6c89470dff7)。

数字增益控制（Digital Gain Control）。

<a id="define-members-5"></a>

### 厂商特定类控制标识符（Vendor-specific Class Control IDs）

<a id="r_ga05e2fe16eafe259061af62ac31dfaeca"></a>

```c
#define VIDEO_CID_PRIVATE_BASE 0x08000000
```

相关声明：[VIDEO_CID_PRIVATE_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga05e2fe16eafe259061af62ac31dfaeca)。

<a id="define-members-6"></a>

### 查询标志，与控制标识符按位或（Query Flags, ORed with the Control ID）

<a id="r_ga6fc7bcd4b280b4598ea3a03108881b5c"></a>

```c
#define VIDEO_CTRL_FLAG_NEXT_CTRL 0x80000000
```

相关声明：[VIDEO_CTRL_FLAG_NEXT_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga6fc7bcd4b280b4598ea3a03108881b5c)。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 5.2\_基本类控制标识符（Base Class Control IDs）

<a id="r_ga4b56ce06ae4f6ca5b7ac9fd5a7b21319"></a>

```c
#define VIDEO_CID_BASE 0x00980900
```

相关声明：[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

<a id="r_ga1529eeb7c36bfe53e3916dbd9c6f5b1e"></a>

```c
#define VIDEO_CID_BRIGHTNESS (VIDEO_CID_BASE + 0)
```

相关声明：[VIDEO_CID_BRIGHTNESS](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga1529eeb7c36bfe53e3916dbd9c6f5b1e)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

图像亮度（Brightness），更准确地说是黑电平（Black Level）。

<a id="r_ga9ca85f6b1d9add05eacb008dc4ccb2e4"></a>

```c
#define VIDEO_CID_CONTRAST (VIDEO_CID_BASE + 1)
```

相关声明：[VIDEO_CID_CONTRAST](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga9ca85f6b1d9add05eacb008dc4ccb2e4)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

图像对比度（Contrast），即亮度增益（Luma Gain）。

<a id="r_ga200017c2141f5c90ade652224d1d4364"></a>

```c
#define VIDEO_CID_SATURATION (VIDEO_CID_BASE + 2)
```

相关声明：[VIDEO_CID_SATURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga200017c2141f5c90ade652224d1d4364)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

图像色彩饱和度（Color Saturation），即色度增益（Chroma Gain）。

<a id="r_ga588a1206d5046a7b9e8415db725cae81"></a>

```c
#define VIDEO_CID_HUE (VIDEO_CID_BASE + 3)
```

相关声明：[VIDEO_CID_HUE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga588a1206d5046a7b9e8415db725cae81)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

色调（Hue）或色彩平衡（Color Balance）。

<a id="r_ga7e2ce049ed534e1c29ac47d33013e180"></a>

```c
#define VIDEO_CID_AUTO_WHITE_BALANCE (VIDEO_CID_BASE + 12)
```

相关声明：[VIDEO_CID_AUTO_WHITE_BALANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga7e2ce049ed534e1c29ac47d33013e180)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

自动白平衡（Automatic White Balance），用于摄像头。

<a id="r_gab534e6263a6b5caae48543346ba2f7ef"></a>

```c
#define VIDEO_CID_RED_BALANCE (VIDEO_CID_BASE + 14)
```

相关声明：[VIDEO_CID_RED_BALANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gab534e6263a6b5caae48543346ba2f7ef)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

红色色度平衡（Red Chroma Balance），表示为相对于绿色通道的比值。

<a id="r_gaf4d38f5eed6feb9ef9509c1747a332b8"></a>

```c
#define VIDEO_CID_BLUE_BALANCE (VIDEO_CID_BASE + 15)
```

相关声明：[VIDEO_CID_BLUE_BALANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gaf4d38f5eed6feb9ef9509c1747a332b8)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

蓝色色度平衡（Blue Chroma Balance），表示为相对于绿色通道的比值。

<a id="r_ga4e38bb3fcb80b2d28fa88186b65e4fea"></a>

```c
#define VIDEO_CID_GAMMA (VIDEO_CID_BASE + 16)
```

相关声明：[VIDEO_CID_GAMMA](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4e38bb3fcb80b2d28fa88186b65e4fea)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

伽马调整（Gamma Adjust）。

<a id="r_ga24e259a6466537377b7bb8a151311ae1"></a>

```c
#define VIDEO_CID_EXPOSURE (VIDEO_CID_BASE + 17)
```

相关声明：[VIDEO_CID_EXPOSURE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga24e259a6466537377b7bb8a151311ae1)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

图像传感器曝光时间（Image Sensor Exposure Time）。

<a id="r_gac1c1d3580b7ff84b6a461cea0b3942e8"></a>

```c
#define VIDEO_CID_AUTOGAIN (VIDEO_CID_BASE + 18)
```

相关声明：[VIDEO_CID_AUTOGAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gac1c1d3580b7ff84b6a461cea0b3942e8)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

自动增益控制（Automatic Gain Control）。

<a id="r_ga36259be44d9d08b149fd35dd28bbaf50"></a>

```c
#define VIDEO_CID_GAIN (VIDEO_CID_BASE + 19)
```

相关声明：[VIDEO_CID_GAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga36259be44d9d08b149fd35dd28bbaf50)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

增益控制（Gain Control）。

<a id="r_ga59aa47b6f558ef5ae64a67f4a7ac7e31"></a>

```c
#define VIDEO_CID_HFLIP (VIDEO_CID_BASE + 20)
```

相关声明：[VIDEO_CID_HFLIP](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga59aa47b6f558ef5ae64a67f4a7ac7e31)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

水平翻转（Horizontal Flip）图像：左侧变为右侧。

<a id="r_ga16651a6825b619399a333ed39e802dfc"></a>

```c
#define VIDEO_CID_VFLIP (VIDEO_CID_BASE + 21)
```

相关声明：[VIDEO_CID_VFLIP](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga16651a6825b619399a333ed39e802dfc)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

垂直翻转（Vertical Flip）图像：上方变为下方。

<a id="r_ga762a6c2b0fb032b9ebdfeff5ed15c3de"></a>

```c
#define VIDEO_CID_POWER_LINE_FREQUENCY (VIDEO_CID_BASE + 24)
```

相关声明：[VIDEO_CID_POWER_LINE_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga762a6c2b0fb032b9ebdfeff5ed15c3de)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

需要补偿的电源线频率（Power Line Frequency）。

<a id="r_ga9c0df146e6064169a89bd88b10085cec"></a>

```c
#define VIDEO_CID_HUE_AUTO (VIDEO_CID_BASE + 25)
```

相关声明：[VIDEO_CID_HUE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga9c0df146e6064169a89bd88b10085cec)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

启用设备的自动色调控制（Automatic Hue Control）。

<a id="r_ga0670d89542dc532a9c775e8e9c2638b1"></a>

```c
#define VIDEO_CID_WHITE_BALANCE_TEMPERATURE (VIDEO_CID_BASE + 26)
```

相关声明：[VIDEO_CID_WHITE_BALANCE_TEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0670d89542dc532a9c775e8e9c2638b1)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

以开尔文（Kelvin）色温表示的白平衡设置（White Balance Settings）。

<a id="r_gab0509f0d3106bca07658e7cfcb1883cf"></a>

```c
#define VIDEO_CID_SHARPNESS (VIDEO_CID_BASE + 27)
```

相关声明：[VIDEO_CID_SHARPNESS](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gab0509f0d3106bca07658e7cfcb1883cf)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

调整摄像头的锐化滤波器（Sharpness Filter）。

<a id="r_ga2f22b11b526154e66440eca74ec5bd66"></a>

```c
#define VIDEO_CID_BACKLIGHT_COMPENSATION (VIDEO_CID_BASE + 28)
```

相关声明：[VIDEO_CID_BACKLIGHT_COMPENSATION](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga2f22b11b526154e66440eca74ec5bd66)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

调整摄像头的背光补偿（Backlight Compensation）。

<a id="r_ga3fe7778ddb5c3f945b7649379a13321e"></a>

```c
#define VIDEO_CID_COLORFX (VIDEO_CID_BASE + 31)
```

相关声明：[VIDEO_CID_COLORFX](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga3fe7778ddb5c3f945b7649379a13321e)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

选择色彩效果（Color Effect）。

<a id="r_ga46bb41b012b1a2240270817b9ce57637"></a>

```c
#define VIDEO_CID_AUTOBRIGHTNESS (VIDEO_CID_BASE + 32)
```

相关声明：[VIDEO_CID_AUTOBRIGHTNESS](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga46bb41b012b1a2240270817b9ce57637)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

启用自动亮度（Automatic Brightness）。

<a id="r_ga5d2c02644e26f6a7f9887d5879231106"></a>

```c
#define VIDEO_CID_BAND_STOP_FILTER (VIDEO_CID_BASE + 33)
```

相关声明：[VIDEO_CID_BAND_STOP_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga5d2c02644e26f6a7f9887d5879231106)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

开启或关闭摄像头传感器的带阻滤波器（Band-stop Filter），或指定其强度。

<a id="r_gae7f2add167e46dffb19f33393c839c57"></a>

```c
#define VIDEO_CID_ROTATE (VIDEO_CID_BASE + 34)
```

相关声明：[VIDEO_CID_ROTATE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gae7f2add167e46dffb19f33393c839c57)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

旋转控制（Rotate Control）。

<a id="r_ga78dcca8b4c8b29f23e983974b861f157"></a>

```c
#define VIDEO_CID_ALPHA_COMPONENT (VIDEO_CID_BASE + 41)
```

相关声明：[VIDEO_CID_ALPHA_COMPONENT](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga78dcca8b4c8b29f23e983974b861f157)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

设置 Alpha 颜色分量（Alpha Color Component）。

<a id="r_ga829221ec6ea7348e743173ce5e6bd635"></a>

```c
#define VIDEO_CID_LASTP1 (VIDEO_CID_BASE + 44)
```

相关声明：[VIDEO_CID_LASTP1](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga829221ec6ea7348e743173ce5e6bd635)、[VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)。

最后一个基本控制标识符（Base CID）加 1。

<a id="r_ga9db809ab56484b4b5b1a047a97e6920a"></a>

```c
enum video_power_line_frequency { VIDEO_CID_POWER_LINE_FREQUENCY_DISABLED = 0 , VIDEO_CID_POWER_LINE_FREQUENCY_50HZ = 1 , VIDEO_CID_POWER_LINE_FREQUENCY_60HZ = 2 , VIDEO_CID_POWER_LINE_FREQUENCY_AUTO = 3 }
```

相关声明：[video_power_line_frequency](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga9db809ab56484b4b5b1a047a97e6920a)、[VIDEO_CID_POWER_LINE_FREQUENCY_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga9db809ab56484b4b5b1a047a97e6920aa596b3bec6771ef15392bfcee9fc47f93)、[VIDEO_CID_POWER_LINE_FREQUENCY_50HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga9db809ab56484b4b5b1a047a97e6920aad47b0f6914d0e949d17faa61b9fc2c10)、[VIDEO_CID_POWER_LINE_FREQUENCY_60HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga9db809ab56484b4b5b1a047a97e6920aad34ec7a0db40ee5b1dbfc6de79834796)、[VIDEO_CID_POWER_LINE_FREQUENCY_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga9db809ab56484b4b5b1a047a97e6920aa817468b493999a2ba979a249bc0cffe0)。

视频电源线频率（Video Power Line Frequency）。

<a id="r_ga99f4b6cf21c8baaf510fbcfccb645960"></a>

```c
enum video_colorfx { VIDEO_COLORFX_NONE = 0 , VIDEO_COLORFX_BW = 1 , VIDEO_COLORFX_SEPIA = 2 , VIDEO_COLORFX_NEGATIVE = 3 , VIDEO_COLORFX_EMBOSS = 4 , VIDEO_COLORFX_SKETCH = 5 , VIDEO_COLORFX_SKY_BLUE = 6 , VIDEO_COLORFX_GRASS_GREEN = 7 , VIDEO_COLORFX_SKIN_WHITEN = 8 , VIDEO_COLORFX_VIVID = 9 , VIDEO_COLORFX_AQUA = 10 , VIDEO_COLORFX_ART_FREEZE = 11 , VIDEO_COLORFX_SILHOUETTE = 12 , VIDEO_COLORFX_SOLARIZATION = 13 , VIDEO_COLORFX_ANTIQUE = 14 }
```

相关声明：[video_colorfx](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga99f4b6cf21c8baaf510fbcfccb645960)、[VIDEO_COLORFX_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a9960e8b54cf9070c04664246e67f3237)、[VIDEO_COLORFX_BW](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a52f62a92f6f0e158b1797719efb79735)、[VIDEO_COLORFX_SEPIA](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a483faa51fb4728b89c1a8da60b139a37)、[VIDEO_COLORFX_NEGATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960ac9367e073eef47865d90ba9ae6eb98a0)、[VIDEO_COLORFX_EMBOSS](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960aae3d42f32c4f14e371343a32e8132cc0)、[VIDEO_COLORFX_SKETCH](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a789155f47a0302661a71155c1e6045fc)、[VIDEO_COLORFX_SKY_BLUE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a09b5346a7431c2c0e7415037ee5a6f8b)、[VIDEO_COLORFX_GRASS_GREEN](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960abd0ddf263af2224bebe12da19711c6a1)、[VIDEO_COLORFX_SKIN_WHITEN](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a3d4856179a0279a23f1597c3c0a615ef)、[VIDEO_COLORFX_VIVID](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a5e77aa2b5530062aaaf1156a340e3826)、[VIDEO_COLORFX_AQUA](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960adb9e16ef9511c8eec1d6dbead4843a4c)、[VIDEO_COLORFX_ART_FREEZE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a00faf2d7d366f0109d64568839416ccd)、[VIDEO_COLORFX_SILHOUETTE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a1c93819be559612ccea3a2781cbb7d25)、[VIDEO_COLORFX_SOLARIZATION](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a2f6f282e1e195bdc29aa6a351c2bc715)、[VIDEO_COLORFX_ANTIQUE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga99f4b6cf21c8baaf510fbcfccb645960a71acc838d9197b671accab7763c5388b)。

视频色彩效果（Video Color Effects）。

## 5.3\_摄像头类控制标识符（Camera Class Control IDs）

<a id="r_ga0a6e2c6287a67e8aa174bb0130fe4c26"></a>

```c
#define VIDEO_CID_CAMERA_CLASS_BASE 0x009a0900
```

相关声明：[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

<a id="r_gab83ae3ca7fa3da66243431d489be37bd"></a>

```c
#define VIDEO_CID_EXPOSURE_AUTO (VIDEO_CID_CAMERA_CLASS_BASE + 1)
```

相关声明：[VIDEO_CID_EXPOSURE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gab83ae3ca7fa3da66243431d489be37bd)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

启用曝光时间（Exposure Time）和／或光圈孔径（Iris Aperture）的自动调整。

<a id="r_ga036f78623bcae18ea9627d45d1209245"></a>

```c
#define VIDEO_CID_EXPOSURE_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 2)
```

相关声明：[VIDEO_CID_EXPOSURE_ABSOLUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga036f78623bcae18ea9627d45d1209245)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

确定摄像头传感器的曝光时间（Exposure Time）。

<a id="r_gaa5f2ebd1e1aef2da68be4742941c1f50"></a>

```c
#define VIDEO_CID_EXPOSURE_AUTO_PRIORITY (VIDEO_CID_CAMERA_CLASS_BASE + 3)
```

相关声明：[VIDEO_CID_EXPOSURE_AUTO_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gaa5f2ebd1e1aef2da68be4742941c1f50)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

设备是否可以在自动曝光（Auto-exposure）的影响下动态改变帧率（Frame Rate）。适用于将 `VIDEO_CID_EXPOSURE_AUTO` 设为 `VIDEO_EXPOSURE_AUTO` 或 `VIDEO_EXPOSURE_APERTURE_PRIORITY` 的情况。

<a id="r_ga23ed465d76fc54680d1e22422b66c829"></a>

```c
#define VIDEO_CID_PAN_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 4)
```

相关声明：[VIDEO_CID_PAN_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga23ed465d76fc54680d1e22422b66c829)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此只写控制（Write-only Control）使摄像头沿水平方向转动指定的量。

<a id="r_ga7c51639505c7b97fb1953ade5fc72534"></a>

```c
#define VIDEO_CID_TILT_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 5)
```

相关声明：[VIDEO_CID_TILT_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga7c51639505c7b97fb1953ade5fc72534)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此只写控制（Write-only Control）使摄像头沿垂直方向转动指定的量。

<a id="r_ga3b45437f606b8717dcadc22d56a706da"></a>

```c
#define VIDEO_CID_PAN_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 8)
```

相关声明：[VIDEO_CID_PAN_ABSOLUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga3b45437f606b8717dcadc22d56a706da)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此控制（Control）使摄像头沿水平方向转到指定位置。

<a id="r_gae474209914926f2bd38c99e020224b9c"></a>

```c
#define VIDEO_CID_TILT_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 9)
```

相关声明：[VIDEO_CID_TILT_ABSOLUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gae474209914926f2bd38c99e020224b9c)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此控制（Control）使摄像头沿垂直方向转到指定位置。

<a id="r_ga9ce95d3c135a9221a8d0431d9df9836b"></a>

```c
#define VIDEO_CID_FOCUS_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 10)
```

相关声明：[VIDEO_CID_FOCUS_ABSOLUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga9ce95d3c135a9221a8d0431d9df9836b)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此控制将摄像头焦点（Focal Point）设置到指定位置。

<a id="r_ga4137146c348efdcc8088f6be1274b164"></a>

```c
#define VIDEO_CID_FOCUS_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 11)
```

相关声明：[VIDEO_CID_FOCUS_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4137146c348efdcc8088f6be1274b164)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此只写控制（Write-only Control）使摄像头焦点（Focal Point）移动指定的量。

<a id="r_ga031525e88a6c0f915903f5c9068589f4"></a>

```c
#define VIDEO_CID_FOCUS_AUTO (VIDEO_CID_CAMERA_CLASS_BASE + 12)
```

相关声明：[VIDEO_CID_FOCUS_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga031525e88a6c0f915903f5c9068589f4)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

启用连续自动对焦调整（Continuous Automatic Focus Adjustments）。

<a id="r_ga1033858d5515c2016a0cc6ac06fd8b91"></a>

```c
#define VIDEO_CID_ZOOM_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 13)
```

相关声明：[VIDEO_CID_ZOOM_ABSOLUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga1033858d5515c2016a0cc6ac06fd8b91)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

以绝对值指定物镜焦距（Objective Lens Focal Length）。

<a id="r_ga40e76f27e97549a779a6581bd210b0f4"></a>

```c
#define VIDEO_CID_ZOOM_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 14)
```

相关声明：[VIDEO_CID_ZOOM_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga40e76f27e97549a779a6581bd210b0f4)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此只写控制（Write-only Control）相对于当前值设置物镜焦距（Objective Lens Focal Length）。

<a id="r_ga1a79541da7b7a37d9358fb1a3c42a1b7"></a>

```c
#define VIDEO_CID_ZOOM_CONTINUOUS (VIDEO_CID_CAMERA_CLASS_BASE + 15)
```

相关声明：[VIDEO_CID_ZOOM_CONTINUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga1a79541da7b7a37d9358fb1a3c42a1b7)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

启动连续变焦运动（Continuous Zoom Movement）。

<a id="r_ga452858d6adfec3b58db6b26c96638fb2"></a>

```c
#define VIDEO_CID_IRIS_ABSOLUTE (VIDEO_CID_CAMERA_CLASS_BASE + 17)
```

相关声明：[VIDEO_CID_IRIS_ABSOLUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga452858d6adfec3b58db6b26c96638fb2)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此控制将摄像头光圈（Aperture）设为指定值。

<a id="r_ga8d1452dfe9c190f6e28e5e3dd35c52cc"></a>

```c
#define VIDEO_CID_IRIS_RELATIVE (VIDEO_CID_CAMERA_CLASS_BASE + 18)
```

相关声明：[VIDEO_CID_IRIS_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga8d1452dfe9c190f6e28e5e3dd35c52cc)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此只写控制（Write-only Control）使摄像头光圈（Aperture）改变指定的量。

<a id="r_gaa29e9e368d07a22593ef01b91cf1e0b7"></a>

```c
#define VIDEO_CID_AUTO_EXPOSURE_BIAS (VIDEO_CID_CAMERA_CLASS_BASE + 19)
```

相关声明：[VIDEO_CID_AUTO_EXPOSURE_BIAS](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gaa29e9e368d07a22593ef01b91cf1e0b7)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

自动曝光补偿（Automatic Exposure Compensation）。

<a id="r_ga9d224bc93e5c23317f9ccf89713a18d6"></a>

```c
#define VIDEO_CID_WIDE_DYNAMIC_RANGE (VIDEO_CID_CAMERA_CLASS_BASE + 21)
```

相关声明：[VIDEO_CID_WIDE_DYNAMIC_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga9d224bc93e5c23317f9ccf89713a18d6)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

启用或禁用摄像头的宽动态范围（Wide Dynamic Range）功能。

<a id="r_ga99996bce4091e4223130d9ae5e1024cd"></a>

```c
#define VIDEO_CID_PAN_SPEED (VIDEO_CID_CAMERA_CLASS_BASE + 32)
```

相关声明：[VIDEO_CID_PAN_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga99996bce4091e4223130d9ae5e1024cd)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此控制使摄像头以指定速度沿水平方向转动。

<a id="r_ga3bfeedcd519191bcf1d684fd983ca9bc"></a>

```c
#define VIDEO_CID_TILT_SPEED (VIDEO_CID_CAMERA_CLASS_BASE + 33)
```

相关声明：[VIDEO_CID_TILT_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga3bfeedcd519191bcf1d684fd983ca9bc)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此控制使摄像头以指定速度沿垂直方向转动。

<a id="r_ga57e5c3f562683a2b7ea1f96a58f633be"></a>

```c
#define VIDEO_CID_CAMERA_ORIENTATION (VIDEO_CID_CAMERA_CLASS_BASE + 34)
```

相关声明：[VIDEO_CID_CAMERA_ORIENTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga57e5c3f562683a2b7ea1f96a58f633be)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此只读控制（Read-only Control）描述摄像头在设备上的位置，即摄像头在设备上的安装位置（Mounting Position）。

<a id="r_ga0d48a910e8d6797842dc25b33fc3f187"></a>

```c
#define VIDEO_CID_CAMERA_SENSOR_ROTATION (VIDEO_CID_CAMERA_CLASS_BASE + 35)
```

相关声明：[VIDEO_CID_CAMERA_SENSOR_ROTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0d48a910e8d6797842dc25b33fc3f187)、[VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)。

此只读控制（Read-only Control）描述传感器在设备中的朝向（Orientation）。

<a id="r_ga167cf84b8f4259e6cdd333748deafaf6"></a>

```c
enum video_exposure_type { VIDEO_EXPOSURE_AUTO = 0 , VIDEO_EXPOSURE_MANUAL = 1 , VIDEO_EXPOSURE_SHUTTER_PRIORITY = 2 , VIDEO_EXPOSURE_APERTURE_PRIORITY = 3 }
```

相关声明：[video_exposure_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga167cf84b8f4259e6cdd333748deafaf6)、[VIDEO_EXPOSURE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga167cf84b8f4259e6cdd333748deafaf6ab77bff3e8a2abd1c823dbb4324e8499b)、[VIDEO_EXPOSURE_MANUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga167cf84b8f4259e6cdd333748deafaf6a66ab6044a5961bc14e1ab718d1a91224)、[VIDEO_EXPOSURE_SHUTTER_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga167cf84b8f4259e6cdd333748deafaf6ac92a826dee7a328bb0b43857d6c09c61)、[VIDEO_EXPOSURE_APERTURE_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga167cf84b8f4259e6cdd333748deafaf6a8abeb9fbd3156edf9f3057692829cbcd)。

视频曝光类型（Video Exposure Type）。

<a id="r_ga1fb4e9981b362010439b9419691ac2af"></a>

```c
enum video_camera_orientation { VIDEO_CAMERA_ORIENTATION_FRONT = 0 , VIDEO_CAMERA_ORIENTATION_BACK = 1 , VIDEO_CAMERA_ORIENTATION_EXTERNAL = 2 }
```

相关声明：[video_camera_orientation](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga1fb4e9981b362010439b9419691ac2af)、[VIDEO_CAMERA_ORIENTATION_FRONT](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga1fb4e9981b362010439b9419691ac2afa76b044aa6d822af9844632761fefbaef)、[VIDEO_CAMERA_ORIENTATION_BACK](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga1fb4e9981b362010439b9419691ac2afa831cc750dfcb43f74eb3a7ee59b33072)、[VIDEO_CAMERA_ORIENTATION_EXTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga1fb4e9981b362010439b9419691ac2afafcc44933e74389bef0e1f20b7998f594)。

视频摄像头朝向（Video Camera Orientation）。


## 5.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P117_controls.h_源码浏览.md)
- [VIDEO_CID_CODEC_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gadf37e306a8d73cec4674422e74ffc85e)
- [VIDEO_CID_FLASH_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga9e0c8dc67fab1a80f81cd4be2e875954)
- [VIDEO_CID_JPEG_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga9281f5a61120a6de015a9bbc75ee8b91)
- [VIDEO_CID_JPEG_COMPRESSION_QUALITY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga883c2a761ea0f00e83c884a5b4b45eee)
- [VIDEO_CID_IMAGE_SOURCE_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga3cc32750dec0096ea873ea13e83d202e)
- [VIDEO_CID_ANALOGUE_GAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga41b451aace98fb81633983a413d2724f)
- [VIDEO_CID_IMAGE_PROC_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0329342731999405d1f8d6c89470dff7)
- [`VIDEO_CID_LINK_FREQ`（链路频率）。](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga2142e2819c445b70d82067a3cfb193c8)
- [`VIDEO_CID_PIXEL_RATE`（像素速率）。](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga6f6eaed7defdbb5f440874c7c6d0a6eb)
- [VIDEO_CID_TEST_PATTERN](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gad1ce88a5c071eaeb8d5db9dc722a2cd4)
- [VIDEO_CID_DIGITAL_GAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gaf60ad41dc4fdffde0a60e53f624e7978)
- [VIDEO_CID_PRIVATE_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga05e2fe16eafe259061af62ac31dfaeca)
- [VIDEO_CTRL_FLAG_NEXT_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga6fc7bcd4b280b4598ea3a03108881b5c)
- [VIDEO_CID_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)
- [VIDEO_CID_BRIGHTNESS](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga1529eeb7c36bfe53e3916dbd9c6f5b1e)
- [VIDEO_CID_CONTRAST](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga9ca85f6b1d9add05eacb008dc4ccb2e4)
- [VIDEO_CID_SATURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga200017c2141f5c90ade652224d1d4364)
- [VIDEO_CID_HUE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga588a1206d5046a7b9e8415db725cae81)
- [VIDEO_CID_AUTO_WHITE_BALANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga7e2ce049ed534e1c29ac47d33013e180)
- [VIDEO_CID_RED_BALANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gab534e6263a6b5caae48543346ba2f7ef)
- [VIDEO_CID_BLUE_BALANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gaf4d38f5eed6feb9ef9509c1747a332b8)
- [VIDEO_CID_GAMMA](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4e38bb3fcb80b2d28fa88186b65e4fea)
- [VIDEO_CID_EXPOSURE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga24e259a6466537377b7bb8a151311ae1)
- [VIDEO_CID_AUTOGAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gac1c1d3580b7ff84b6a461cea0b3942e8)
- [VIDEO_CID_GAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga36259be44d9d08b149fd35dd28bbaf50)
- [VIDEO_CID_HFLIP](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga59aa47b6f558ef5ae64a67f4a7ac7e31)
- [VIDEO_CID_VFLIP](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga16651a6825b619399a333ed39e802dfc)
- [VIDEO_CID_POWER_LINE_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga762a6c2b0fb032b9ebdfeff5ed15c3de)
- [VIDEO_CID_HUE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga9c0df146e6064169a89bd88b10085cec)
- [VIDEO_CID_WHITE_BALANCE_TEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0670d89542dc532a9c775e8e9c2638b1)
- [VIDEO_CID_SHARPNESS](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gab0509f0d3106bca07658e7cfcb1883cf)
- [VIDEO_CID_BACKLIGHT_COMPENSATION](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga2f22b11b526154e66440eca74ec5bd66)
- [VIDEO_CID_COLORFX](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga3fe7778ddb5c3f945b7649379a13321e)
- [VIDEO_CID_AUTOBRIGHTNESS](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga46bb41b012b1a2240270817b9ce57637)
- [VIDEO_CID_BAND_STOP_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga5d2c02644e26f6a7f9887d5879231106)
- [VIDEO_CID_ROTATE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gae7f2add167e46dffb19f33393c839c57)
- [VIDEO_CID_ALPHA_COMPONENT](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga78dcca8b4c8b29f23e983974b861f157)
- [VIDEO_CID_LASTP1](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga829221ec6ea7348e743173ce5e6bd635)
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
- [VIDEO_CID_CAMERA_CLASS_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0a6e2c6287a67e8aa174bb0130fe4c26)
- [VIDEO_CID_EXPOSURE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gab83ae3ca7fa3da66243431d489be37bd)
- [VIDEO_CID_EXPOSURE_ABSOLUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga036f78623bcae18ea9627d45d1209245)
- [VIDEO_CID_EXPOSURE_AUTO_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gaa5f2ebd1e1aef2da68be4742941c1f50)
- [VIDEO_EXPOSURE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga167cf84b8f4259e6cdd333748deafaf6ab77bff3e8a2abd1c823dbb4324e8499b)
- [VIDEO_EXPOSURE_APERTURE_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga167cf84b8f4259e6cdd333748deafaf6a8abeb9fbd3156edf9f3057692829cbcd)
- [VIDEO_CID_PAN_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga23ed465d76fc54680d1e22422b66c829)
- [VIDEO_CID_TILT_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga7c51639505c7b97fb1953ade5fc72534)
- [VIDEO_CID_PAN_ABSOLUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga3b45437f606b8717dcadc22d56a706da)
- [VIDEO_CID_TILT_ABSOLUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gae474209914926f2bd38c99e020224b9c)
- [VIDEO_CID_FOCUS_ABSOLUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga9ce95d3c135a9221a8d0431d9df9836b)
- [VIDEO_CID_FOCUS_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga4137146c348efdcc8088f6be1274b164)
- [VIDEO_CID_FOCUS_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga031525e88a6c0f915903f5c9068589f4)
- [VIDEO_CID_ZOOM_ABSOLUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga1033858d5515c2016a0cc6ac06fd8b91)
- [VIDEO_CID_ZOOM_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga40e76f27e97549a779a6581bd210b0f4)
- [VIDEO_CID_ZOOM_CONTINUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga1a79541da7b7a37d9358fb1a3c42a1b7)
- [VIDEO_CID_IRIS_ABSOLUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga452858d6adfec3b58db6b26c96638fb2)
- [VIDEO_CID_IRIS_RELATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga8d1452dfe9c190f6e28e5e3dd35c52cc)
- [VIDEO_CID_AUTO_EXPOSURE_BIAS](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gaa29e9e368d07a22593ef01b91cf1e0b7)
- [VIDEO_CID_WIDE_DYNAMIC_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga9d224bc93e5c23317f9ccf89713a18d6)
- [VIDEO_CID_PAN_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga99996bce4091e4223130d9ae5e1024cd)
- [VIDEO_CID_TILT_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga3bfeedcd519191bcf1d684fd983ca9bc)
- [VIDEO_CID_CAMERA_ORIENTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga57e5c3f562683a2b7ea1f96a58f633be)
- [VIDEO_CID_CAMERA_SENSOR_ROTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga0d48a910e8d6797842dc25b33fc3f187)
- [video_exposure_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga167cf84b8f4259e6cdd333748deafaf6)
- [VIDEO_EXPOSURE_MANUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga167cf84b8f4259e6cdd333748deafaf6a66ab6044a5961bc14e1ab718d1a91224)
- [VIDEO_EXPOSURE_SHUTTER_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga167cf84b8f4259e6cdd333748deafaf6ac92a826dee7a328bb0b43857d6c09c61)
- [video_camera_orientation](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga1fb4e9981b362010439b9419691ac2af)
- [VIDEO_CAMERA_ORIENTATION_FRONT](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga1fb4e9981b362010439b9419691ac2afa76b044aa6d822af9844632761fefbaef)
- [VIDEO_CAMERA_ORIENTATION_BACK](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga1fb4e9981b362010439b9419691ac2afa831cc750dfcb43f74eb3a7ee59b33072)
- [VIDEO_CAMERA_ORIENTATION_EXTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#gga1fb4e9981b362010439b9419691ac2afafcc44933e74389bef0e1f20b7998f594)

<a id="header-details"></a>

---

[上一章](P004_zephyr__dt-bindings__clock__amebag2_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__bluetooth__direction.h_文件参考.md)
