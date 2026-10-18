---
id: learning.zephyr-docs.boards-shields.page-116
title: MikroElektronika Proximity 9 Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_proximity_9_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-proximity-9-click"></a>

<a id="mikroe-proximity-9-click-shield"></a>

# 第116章\_MikroElektronika Proximity 9 Click接近感测扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_proximity_9_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

[Proximity 9 Click](https://www.mikroe.com/proximity-9-click)采用集成Filtron技术的VCNL4040，提供精确可靠的接近感测PS及环境光感测ALS。

VCNL4040集成940 nm红外发射二极管IRED、低噪声模拟前端及PS／ALS感光元件。专有Filtron技术使响应接近人眼光谱，并消除背景光；可编程中断引擎便于优化固件，减轻MCU负载及功耗。

<a id="id1"></a>

[![官方原图：Proximity 9 Click](images/mikroe_proximity_9_click.webp)](images/mikroe_proximity_9_click.webp)

Proximity 9 Click接近感测扩展板

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板只能用于提供mikroBUS插座，并为其I2C接口定义mikrobus_i2c节点标签的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置-DSHIELD=mikroe_proximity_9_click，例如：

```text
# From the root of the zephyr repository
west build -b mikroe_clicker_ra4m1 --shield mikroe_proximity_9_click samples/sensor/proximity_polling
```

VCNL4040的其他绑定属性见[vishay,vcnl4040](../sensor_ti_vishay_wurth_sensing_binding_reference/P013_vishay_vcnl4040.md#std-dtcompatible-vishay-vcnl4040)文档。

<a id="references"></a>

## 参考资料（References）


- [Proximity 9 Click接近感测扩展板](https://www.mikroe.com/proximity-9-click)
- [Proximity 9 Click原理图](https://download.mikroe.com/documents/add-on-boards/click/proximity-9/proximity-9-click-schematic-v100.pdf)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [proximity-9-click](https://www.mikroe.com/proximity-9-click)：HTTP Error 403: Forbidden。

---

[上一章](P115_MikroElektronika_Pressure_3_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P117_MikroElektronika_RS485_Isolator_5_Click.md)
