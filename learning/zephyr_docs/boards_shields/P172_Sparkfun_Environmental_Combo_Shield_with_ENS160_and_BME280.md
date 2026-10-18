---
id: learning.zephyr-docs.boards-shields.page-172
title: Sparkfun Environmental Combo Shield with ENS160 and BME280
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/sparkfun_environmental_combo/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="sparkfun-environmental-combo-shield-with-ens160-and-bme280"></a>

<a id="sparkfun-environmental-combo"></a>

# 第172章\_Sparkfun ENS160及BME280环境组合扩展板（Environmental Combo Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/sparkfun_environmental_combo/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Sparkfun环境组合扩展板具有ScioSense ENS160数字金属氧化物多气体传感器、Bosch BME280湿度传感器及2个Qwiic连接器，用于测量温度、湿度、气压、CO2及挥发性有机化合物（VOC）。（[Sparkfun 环境组合 扩展板](https://www.sparkfun.com/sparkfun-environmental-combo-breakout-ens160-bme280-qwiic.html)；[ScioSense ENS160 数字金属氧化物多气体传感器](https://www.sciosense.com/wp-content/uploads/2023/12/ENS160-Datasheet.pdf)；[Bosch BME280 湿度传感器](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/)）

<a id="id1"></a>

![官方原图：Sparkfun Environmental Combo Shield](images/sparkfun_environmental_combo.webp)

Sparkfun环境组合扩展板，图片来源：Sparkfun

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
<td>ENS160及BME280 I2C数据SDA</td>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>ENS160及BME280 I2C时钟SCL</td>
</tr>
<tr>
<td>中断（INT）</td>
<td>ENS160中断输出</td>
</tr>
</table>

使用ENS160中断输出时，须另接导线，将扩展板INT输出接至微控制器板的合适GPIO，并修改设备树配置；选项见[sciosense,ens160](../compatible_binding_reference/P055_sciosense_ens160.md#std-dtcompatible-sciosense-ens160)。

BME280传感器另见[bosch,bme280](../compatible_binding_reference/P011_bosch_bme280.md#std-dtcompatible-bosch-bme280)。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield sparkfun_environmental_combo，例如运行BME280湿度及气压传感器示例：（[BME280湿度和压力传感器（Humidity and Pressure Sensor）](../sensors/P050_BME280温湿度与气压传感器示例.md#bme280)）

```text
# From the root of the zephyr repository
west build -b adafruit_qt_py_rp2040 --shield sparkfun_environmental_combo samples/sensor/bme280
```

也可使用传感器Shell示例：（[传感器Shell（Sensor Shell）](../sensors/P025_传感器Shell示例.md#sensor_shell)）

```text
# From the root of the zephyr repository
west build -b adafruit_qt_py_rp2040 --shield sparkfun_environmental_combo samples/sensor/sensor_shell
```

---

[上一章](P171_Sparkfun_SparkFun_MicroMod_Asset_Tracker_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P173_SparkFun_MAX3421E_Shield.md)
