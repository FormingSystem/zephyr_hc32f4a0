---
id: learning.zephyr-docs.boards-shields.page-187
title: ST STM32F4DIS-CAM
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/st_stm32f4dis_cam/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="st-stm32f4dis-cam"></a>

<a id="id1"></a>

# 第187章\_ST STM32F4DIS-CAM摄像头板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/st_stm32f4dis_cam/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

STM32F4DIS-CAM摄像头板集成130万像素OV9655传感器及30针FFC连接器，用于提供DVP摄像头接口的部分STM32 Discovery套件，例如STM32L4R9I-disco。

<a id="requirements"></a>

## 前置要求（Requirements）

此摄像头模块套件兼容具有30针FFC连接器的STM32 Discovery及Evaluation开发板，例如STM32F4 Discovery及STM32L4R9I Discovery套件。

<a id="usage"></a>

## 用途（Usage）

对于具备所需设备树节点标签的开发板，将SHIELD设为st_stm32f4dis_cam，即可在任意应用中使用此扩展板。

调用west build时设置--shield "st_stm32f4dis_cam"，例如：

```text
# From the root of the zephyr repository
west build -b stm32l4r9i_disco --shield st_stm32f4dis_cam samples/subsys/video/capture
```

---

[上一章](P186_ST_MB1897_CAM.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P188_HL78xx_Auto_Baud_Rate_Switching.md)
