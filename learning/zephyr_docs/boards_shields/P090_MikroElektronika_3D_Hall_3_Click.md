---
id: learning.zephyr-docs.boards-shields.page-90
title: MikroElektronika 3D Hall 3 Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_3d_hall_3_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-3d-hall-3-click"></a>

<a id="mikroe-3d-hall-3-click-shield"></a>

# 第90章\_MikroElektronika 3D Hall 3 Click三维霍尔扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_3d_hall_3_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

[3D Hall 3 Click](https://www.mikroe.com/3d-hall-3-click)是高精度磁场感测扩展板，用于测量三个相互垂直方向的磁场强度。

它采用低功耗三维磁传感器LIS2MDL，每个轴有独立霍尔感应元件，可精确可靠地测量三维磁场，为位置计算提供依据。LIS2MDL支持I2C及SPI，并带可编程中断引擎，便于优化固件。

<a id="id1"></a>

[![官方原图：3D Hall 3 Click](images/mikroe_3d_hall_3_click.webp)](images/mikroe_3d_hall_3_click.webp)

3D Hall 3 Click三维霍尔扩展板

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板只能用于提供mikroBUS插座，并为其I2C接口定义mikrobus_i2c节点标签的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置-DSHIELD=mikroe_3d_hall_3_click，例如：

```text
# From the root of the zephyr repository
west build -b mikroe_clicker_ra4m1/r7fa4m1ab3cfm --shield mikroe_3d_hall_3_click samples/sensor/magn_polling
```

LIS2MDL的其他绑定属性见[st,lis2mdl](../compatible_binding_reference/P085_st_lis2mdl.md#std-dtcompatible-st-lis2mdl)文档。

<a id="references"></a>

## 参考资料（References）


- [3D Hall 3 Click三维霍尔扩展板](https://www.mikroe.com/3d-hall-3-click)
- [3D Hall 3 Click原理图](https://download.mikroe.com/documents/add-on-boards/click/3d-hall-3/3d-hall-3-click-schematic-v100.pdf)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [3d-hall-3-click](https://www.mikroe.com/3d-hall-3-click)：HTTP Error 403: Forbidden。

---

[上一章](P089_Microchip_MCP2515_CAN_bus_shields.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P091_MikroElektronika_ACCEL_13_Click.md)
