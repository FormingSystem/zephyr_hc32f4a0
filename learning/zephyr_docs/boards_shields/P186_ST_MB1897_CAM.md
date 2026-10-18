---
id: learning.zephyr-docs.boards-shields.page-186
title: ST MB1897 CAM
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/st_mb1897_cam/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="st-mb1897-cam"></a>

<a id="id1"></a>

# 第186章\_ST MB1897摄像头（ST_MB1897_CAM）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/st_mb1897_cam/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

STM32MP135F Discovery开发板随附CSI摄像头模块，通过15针FFC连接器连接STM32MP135F-DK。摄像头模块板MB1897集成Galaxycore GC2145 CSI传感器。

<a id="id2"></a>

![官方原图：ST-MB1897-CAM](images/st_mb1897_cam.webp)

MB1897图片，来源：STMicroelectronics。

<a id="requirements"></a>

## 前置要求（Requirements）

此摄像头模块套件兼容具有15针FFC连接器的STM32 Discovery及Evaluation开发板，例如STM32MP13 Discovery套件。

<a id="usage"></a>

## 用途（Usage）

对于具备所需设备树节点标签的开发板，将SHIELD设为st_mb1897_cam，即可在任意应用中使用此扩展板。

调用west build时设置--shield "st_mb1897_cam"，例如：

```text
# From the root of the zephyr repository
west build -b stm32mp135f_dk --shield st_mb1897_cam samples/subsys/video/capture
```

---

[上一章](P185_ST_LCD_DSI_MB1835.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P187_ST_STM32F4DIS-CAM.md)
