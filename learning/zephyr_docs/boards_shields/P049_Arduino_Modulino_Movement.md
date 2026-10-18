---
id: learning.zephyr-docs.boards-shields.page-49
title: Arduino Modulino Movement
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/arduino_modulino_movement/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="arduino-modulino-movement"></a>

<a id="id1"></a>

# 第49章\_Arduino Modulino运动模块（Movement）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/arduino_modulino_movement/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Arduino Modulino Movement兼容Qwiic，采用意法半导体LSM6DSOXTR六轴IMU传感器。

该传感器可用设置见[st,lsm6dso](../compatible_binding_reference/P091_st_lsm6dso.md#std-dtcompatible-st-lsm6dso)。

![官方原图：Arduino Modulino Movement](images/arduino_modulino_movement.webp)

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield arduino_modulino_movement。

例如：

```text
# From the root of the zephyr repository
west build -b arduino_uno_r4@wifi --shield arduino_modulino_movement samples/sensor/accel_polling
```

---

[上一章](P048_Arduino_Modulino_Latch_Relay.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P050_Arduino_Modulino_Pixels.md)
