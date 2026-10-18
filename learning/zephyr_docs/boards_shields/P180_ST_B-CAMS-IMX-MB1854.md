---
id: learning.zephyr-docs.boards-shields.page-180
title: ST B-CAMS-IMX-MB1854
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/st_b_cams_imx_mb1854/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="st-b-cams-imx-mb1854"></a>

<a id="id1"></a>

# 第180章\_ST B-CAMS-IMX-MB1854摄像头模块

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/st_b_cams_imx_mb1854/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

B-CAMS-IMX摄像头模块为多种计算机视觉场景及用途提供硬件，具有500万像素高分辨率RGB CMOS图像传感器、惯性运动单元及飞行时间（Time-of-Flight）传感器。它可用于任何具有22针FFC连接器的MIPI CSI-2®接口的STM32开发板，便于在STM32微控制器及微处理器上实现完整计算机视觉功能。

<a id="id2"></a>

[![官方原图：B-CAMS-IMX-MB1854](images/st_b_cams_imx_mb1854.webp)](images/st_b_cams_imx_mb1854.webp)

B-CAMS-IMX MB1854图片，来源：STMicroelectronics。

<a id="requirements"></a>

## 前置要求（Requirements）

该摄像头模块套件兼容所有具有22针FFC连接器的STM32 Discovery及Evaluation开发板，例如STM32N6570_DK Discovery套件。

<a id="usage"></a>

## 用途（Usage）

对于具备所需设备树节点标签的开发板，将SHIELD设为st_b_cams_imx_mb1854，即可在任意应用中使用此扩展板。

调用west build时设置--shield "st_b_cams_imx_mb1854"，例如：

```text
# From the root of the zephyr repository
west build -b stm32n6570_dk --shield st_b_cams_imx_mb1854 samples/subsys/video/capture
```

<a id="stm32mp257f-dk"></a>

### STM32MP257F-DK

在STM32MP257F-DK上，摄像头模块通过i2c2控制，该总线与LVDS触摸面板及HDMI桥共享，默认由Cortex-A35上的Linux管理。因此，在Cortex-M33上运行Zephyr应用前，必须在Linux设备树中禁用i2c2；之后Linux将无法使用触摸面板及HDMI输出。

```text
# From the root of the zephyr repository
west build -b stm32mp257f_dk/stm32mp257fxx/m33 --shield st_b_cams_imx_mb1854 samples/subsys/video/capture
```

<a id="references"></a>

## 参考资料（References）


- [产品页面（Product Page）](https://www.st.com/en/evaluation-tools/b-cams-imx.html)
- [产品简介（Databrief）](https://www.st.com/resource/en/data_brief/b-cams-imx.pdf)
- [用户手册（User Manual）](https://www.st.com/resource/en/user_manual/um3354-camera-module-bundle-for-stm32-boards-stmicroelectronics.pdf)

## 译注

STM32MP257F-DK上使用摄像头前须从Linux释放i2c2；Linux触摸与HDMI随后不可用。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [b-cams-imx.html](https://www.st.com/en/evaluation-tools/b-cams-imx.html)：HTTP Error 567: Unknown Status。
- [b-cams-imx.pdf](https://www.st.com/resource/en/data_brief/b-cams-imx.pdf)：HTTP Error 567: Unknown Status。
- [um3354-camera-module-bundle-for-stm32-boards-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/um3354-camera-module-bundle-for-stm32-boards-stmicroelectronics.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P179_ST87MXX_shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P181_ST_B-CAMS-OMV-MB1683.md)
