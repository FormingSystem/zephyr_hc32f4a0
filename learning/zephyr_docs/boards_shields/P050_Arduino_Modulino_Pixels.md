---
id: learning.zephyr-docs.boards-shields.page-50
title: Arduino Modulino Pixels
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/arduino_modulino_pixels/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="arduino-modulino-pixels"></a>

<a id="id1"></a>

# 第50章\_Arduino Modulino像素灯模块（Pixels）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/arduino_modulino_pixels/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Arduino Modulino Pixels兼容Qwiic，带8个可寻址LED。

![官方原图：Arduino Modulino Pixels](images/arduino_modulino_pixels.webp)

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield arduino_modulino_pixels，LED通过LED灯带子系统访问。

例如：

```text
# From the root of the zephyr repository
west build -b arduino_uno_r4@wifi --shield arduino_modulino_pixels samples/drivers/led/led_strip
```

---

[上一章](P049_Arduino_Modulino_Movement.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P051_Arduino_Modulino_Thermo.md)
