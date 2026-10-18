---
id: learning.zephyr-docs.boards-shields.page-48
title: Arduino Modulino Latch Relay
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/arduino_modulino_latch_relay/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="arduino-modulino-latch-relay"></a>

<a id="id1"></a>

# 第48章\_Arduino Modulino磁保持继电器模块（Latch Relay）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/arduino_modulino_latch_relay/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Arduino Modulino Latch Relay兼容Qwiic，包含一个磁保持继电器。

![官方原图：Arduino Modulino Latch Relay module](images/modulino_latch_relay.webp)

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield arduino_modulino_latch_relay，即可在应用中使用继电器。

例如：

```text
# From the root of the zephyr repository
west build -b arduino_nano_matter --shield arduino_modulino_latch_relay samples/regulator/regulator_shell
```

---

[上一章](P047_Arduino_Modulino_Buttons.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P049_Arduino_Modulino_Movement.md)
