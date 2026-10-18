---
id: learning.zephyr-docs.boards-shields.page-36
title: Adafruit SHT40 SHT41 and SHT45 Shields
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_sht4x/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-sht40-sht41-and-sht45-shields"></a>

<a id="adafruit-sht4x"></a>

# 第36章\_Adafruit SHT40、SHT41及SHT45扩展板（Shields）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_sht4x/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit SHT40、SHT41及SHT45扩展板采用Sensirion SHT4x温湿度传感器，带2个STEMMA QT连接器，用于测量温度及湿度，例如[SHT40传感器](https://sensirion.com/products/catalog/SHT40)。（[Adafruit SHT40、SHT41及SHT45扩展板（Shields）](https://learn.adafruit.com/adafruit-sht40-temperature-humidity-sensor)）

<a id="id2"></a>

![官方原图：Adafruit SHT40 Shield](images/adafruit_sht40.webp)

Adafruit SHT40扩展板，图片来源：Adafruit

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
<td>Sensor I2C数据线（SDA）</td>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>Sensor I2C时钟线（SCL）</td>
</tr>
</table>

可用设备树设置见[sensirion,sht4x](../sensor_realtek_rohm_sensirion_binding_reference/P025_sensirion_sht4x.md#std-dtcompatible-sensirion-sht4x)，例如测量速度与重复性之间的取舍。

此扩展板定义假定I2C地址为0x44。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_sht4x，例如运行[通用数字温湿度传感器轮询](../sensors/P016_温湿度传感器轮询示例.md#dht_polling)示例：

```text
# From the root of the zephyr repository
west build -b adafruit_feather_rp2040 --shield adafruit_sht4x samples/sensor/dht_polling
west flash
```

---

[上一章](P035_Adafruit_PCF8523_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P037_Adafruit_TSL2591_Shield.md)
