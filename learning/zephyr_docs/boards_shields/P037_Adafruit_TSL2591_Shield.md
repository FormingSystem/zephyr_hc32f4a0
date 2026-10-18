---
id: learning.zephyr-docs.boards-shields.page-37
title: Adafruit TSL2591 Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_tsl2591/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-tsl2591-shield"></a>

<a id="adafruit-tsl2591"></a>

# 第37章\_Adafruit TSL2591扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_tsl2591/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit TSL2591高动态范围数字光传感器扩展板采用欧司朗OSRAM TSL2591环境光传感器，带2个STEMMA QT连接器。（[Adafruit TSL2591 高动态范围数字光传感器 扩展板](https://learn.adafruit.com/adafruit-tsl2591)；[OSRAM TSL2591 环境光传感器](https://ams-osram.com/products/sensor-solutions/ambient-light-color-spectral-proximity-sensors/ams-tsl25911-ambient-light-sensor)）

<a id="id1"></a>

![官方原图：Adafruit TSL2591 Shield](images/adafruit_tsl2591.webp)

Adafruit TSL2591扩展板（Shield），图片来源：Adafruit

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
<td>串行数据线（SDA）</td>
<td>TSL2591 I2C数据线（SDA）</td>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>TSL2591 I2C时钟线（SCL）</td>
</tr>
<tr>
<td>中断（INT）</td>
<td>TSL2591中断输出</td>
</tr>
</table>

若要使用中断，须另接一根线，将扩展板连接到微控制器板GPIO；如何修改设备树见[ams,tsl2591](../sensor_ams_aosong_bosch_binding_reference/P009_ams_tsl2591.md#std-dtcompatible-ams-tsl2591)绑定文档。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_tsl2591，例如运行通用光照传感器轮询测量示例：（[通用光照传感器轮询（Generic Light Sensor Polling）](../sensors/P019_光照传感器轮询示例.md#light_sensor_polling)）

```text
# From the root of the zephyr repository
west build -b adafruit_qt_py_rp2040 --shield adafruit_tsl2591 samples/sensor/light_polling
```

---

[上一章](P036_Adafruit_SHT40_SHT41_and_SHT45_Shields.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P038_Adafruit_VCNL4040_Shield.md)
