---
id: learning.zephyr-docs.boards-shields.page-94
title: MikroElektronika Air Quality 3 Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_air_quality_3_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-air-quality-3-click"></a>

<a id="mikroe-air-quality-3-click-shield"></a>

# 第94章\_MikroElektronika Air Quality 3 Click空气质量扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_air_quality_3_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

[Air Quality 3 Click](https://www.mikroe.com/air-quality-3-click)可输出室内等效二氧化碳浓度及总挥发性有机物浓度（TVOC）。

扩展板采用ScioSense CCS811空气质量传感器，内置MCU及专门设计的金属氧化物MOX气体传感微热板，与其他MOX方案相比，具有高可靠性、较短测量周期及较低功耗；另配温度补偿元件提高精度。

<a id="id1"></a>

[![官方原图：Air Quality 3 Click](images/mikroe_air_quality_3_click.webp)](images/mikroe_air_quality_3_click.webp)

Air Quality 3 Click空气质量扩展板

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板只能用于提供mikroBUS插座，并为其I2C接口定义mikrobus_i2c节点标签的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置-DSHIELD=mikroe_air_quality_3_click，例如：

```text
# From the root of the zephyr repository
west build -b mikroe_clicker_ra4m1 --shield mikroe_air_quality_3_click samples/sensor/ccs811
```

<a id="references"></a>

## 参考资料（References）


- [Air Quality 3 Click空气质量扩展板](https://www.mikroe.com/air-quality-3-click)
- [Air Quality 3 Click原理图](https://download.mikroe.com/documents/add-on-boards/click/air-quality-3/air-quality-3-click-schematic-v100.pdf)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [air-quality-3-click](https://www.mikroe.com/air-quality-3-click)：HTTP Error 403: Forbidden。

---

[上一章](P093_MikroElektronika_ADC_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P095_MikroElektronika_Ambient_2_Click.md)
