---
id: learning.zephyr-docs.boards-shields.page-12
title: Adafruit DPS310 Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_dps310/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-dps310-shield"></a>

<a id="adafruit-dps310"></a>

# 第12章\_Adafruit DPS310扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_dps310/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit DPS310精密气压及高度传感器扩展板采用Infineon DPS310，带2个STEMMA QT连接器，用于测量气压及温度。（[Adafruit DPS310 精密气压及高度传感器 扩展板](https://learn.adafruit.com/adafruit-dps310-precision-barometric-pressure-sensor)；[Infineon DPS310 压力传感器](https://www.infineon.com/part/DPS310)）

<a id="id1"></a>

![官方原图：Adafruit DPS310 Shield](images/adafruit_dps310.webp)

Adafruit DPS310扩展板（Shield），图片来源：Adafruit

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
<td>SDI</td>
<td>DPS310 I2C数据线（SDA）</td>
</tr>
<tr>
<td>串行时钟（SCK）</td>
<td>DPS310 I2C时钟线（SCL）</td>
</tr>
<tr>
<td>串行数据输出（SDO）</td>
<td>DPS310 I2C地址调整</td>
</tr>
<tr>
<td>片选（CS）</td>
<td>I2C模式不使用</td>
</tr>
</table>

如何修改设备树见[infineon,dps310](../sensor_espressif_honeywell_invensense_binding_reference/P016_infineon_dps310.md#std-dtcompatible-infineon-dps310)绑定文档。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_dps310，例如运行气压与温度传感器轮询示例：（[气压及温度传感器轮询示例](../sensors/P022_气压温度传感器轮询示例.md#pressure_polling)）

```text
# From the root of the zephyr repository
west build -b adafruit_qt_py_rp2040 --shield adafruit_dps310 samples/sensor/pressure_polling
```

---

[上一章](P011_Adafruit_Data_Logger_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P013_Adafruit_DRV2605L_Shield.md)
