---
id: learning.zephyr-docs.boards-shields.page-30
title: Adafruit MAX17048 Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_max17048/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-max17048-shield"></a>

<a id="adafruit-max17048"></a>

# 第30章\_Adafruit MAX17048扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_max17048/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit MAX17048电量计扩展板采用Analog Devices MAX17048，带2个STEMMA QT连接器，可测量单节锂离子或锂聚合物电池的电压及荷电状态（State of Charge）。（[Adafruit MAX17048 电量计 扩展板](https://learn.adafruit.com/adafruit-max17048-lipoly-liion-fuel-gauge-and-battery-monitor)；[Analog Devices MAX17048 电量计](https://www.analog.com/en/products/max17048.html)）

<a id="id1"></a>

![官方原图：Adafruit MAX17048 Shield](images/adafruit_max17048.webp)

Adafruit MAX17048扩展板（Shield），图片来源：Adafruit

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板可用于提供I2C连接器的开发板，例如STEMMA QT或Qwiic；目标板必须定义zephyr_i2c节点标签，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="pin-assignments"></a>

### 引脚分配（Pin Assignments）

<table>
<tr>
<th>扩展板引脚（Shield Pin）</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>I2C串行时钟（SCL）</td>
</tr>
<tr>
<td>串行数据线（SDA）</td>
<td>I2C串行数据（SDA）</td>
</tr>
<tr>
<td>中断（INT）</td>
<td>中断输出</td>
</tr>
<tr>
<td>QStart</td>
<td>快速启动复位输入（Quick-start Reset）</td>
</tr>
</table>

如何修改设备树见[maxim,max17048](../fuel_gauge_binding_reference/P004_maxim_max17048.md#std-dtcompatible-maxim-max17048)绑定文档。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_max17048，例如运行电量计[Fuel Gauge](../driver_samples/P028_电量计示例.md#fuel_gauge)示例：

```text
# From the root of the zephyr repository
west build -b adafruit_feather_canbus_rp2040 --shield adafruit_max17048 samples/drivers/fuel_gauge
west flash
```

---

[上一章](P029_Adafruit_LTR-329_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P031_Adafruit_MCP4728_Quad_DAC_Shield.md)
