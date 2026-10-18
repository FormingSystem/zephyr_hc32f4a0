---
id: learning.zephyr-docs.boards-shields.page-47
title: Arduino Modulino Buttons
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/arduino_modulino_buttons/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="arduino-modulino-buttons"></a>

<a id="id1"></a>

# 第47章\_Arduino Modulino按键模块（Buttons）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/arduino_modulino_buttons/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Arduino Modulino Buttons兼容Qwiic，包含3个按键及3个LED。

![官方原图：Arduino Modulino Buttons module](images/arduino_modulino_buttons.webp)

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield arduino_modulino_buttons，按键通过输入子系统访问，LED通过LED子系统访问。

例如：

```text
# From the root of the zephyr repository
west build -b arduino_uno_r4@wifi --shield arduino_modulino_buttons samples/subsys/input
```

---

[上一章](P046_Arduino_GIGA_Display_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P048_Arduino_Modulino_Latch_Relay.md)
