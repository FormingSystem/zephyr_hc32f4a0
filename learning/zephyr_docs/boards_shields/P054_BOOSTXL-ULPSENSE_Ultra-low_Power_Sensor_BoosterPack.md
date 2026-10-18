---
id: learning.zephyr-docs.boards-shields.page-54
title: BOOSTXL-ULPSENSE Ultra-low Power Sensor BoosterPack
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/boostxl_ulpsense/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="boostxl-ulpsense-ultra-low-power-sensor-boosterpack"></a>

<a id="boostxl-ulpsense"></a>

# 第54章\_BOOSTXL-ULPSENSE：超低功耗传感器BoosterPack

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/boostxl_ulpsense/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

BOOSTXL-ULPSENSE为TI LaunchPad开发套件增加模拟及数字传感器，包含电感式流量计测量电路、2个电容触摸按键、光传感器、簧片开关及超低功耗加速度计。

<a id="id2"></a>

更多信息见BOOSTXL_ULPSENSE网站[注1](#id1)。（[BOOSTXL_ULPSENSE 网站](http://www.ti.com/tool/BOOSTXL-ULPSENSE)）

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板可用于任意带BoosterPack连接器的TI LaunchPad开发套件。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield boostxl_ulpsense，例如：

```text
# From the root of the zephyr repository
west build -b cc1352r1_launchxl --shield boostxl_ulpsense samples/sensor/accel_polling/
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [http://www.ti.com/tool/BOOSTXL-ULPSENSE](http://www.ti.com/tool/BOOSTXL-ULPSENSE)

---

[上一章](P053_Atmel_AT86RF2XX_Transceivers.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P055_Buydisplay_2.8_TFT_Touch_Shield_with_Arduino_adapter.md)
