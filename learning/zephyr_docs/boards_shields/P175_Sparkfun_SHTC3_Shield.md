---
id: learning.zephyr-docs.boards-shields.page-175
title: Sparkfun SHTC3 Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/sparkfun_shtc3/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="sparkfun-shtc3-shield"></a>

<a id="sparkfun-shtc3"></a>

# 第175章\_Sparkfun SHTC3扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/sparkfun_shtc3/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Sparkfun SHTC3温湿度传感器扩展板具有Sensirion SHTC3温湿度传感器及2个Qwiic连接器，用于测量温度和湿度。（[Sparkfun SHTC3 温湿度传感器 扩展板](https://www.sparkfun.com/sparkfun-humidity-sensor-breakout-shtc3-qwiic.html)；[Sensirion SHTC3 湿度及温度传感器](https://sensirion.com/products/catalog/SHTC3)）

<a id="id1"></a>

![官方原图：Sparkfun SHTC3 Shield](images/sparkfun_shtc3.webp)

Sparkfun SHTC3扩展板，图片来源：Sparkfun

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
<td>SHTC3 I2C数据线（SDA）</td>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>SHTC3 I2C时钟线（SCL）</td>
</tr>
</table>

如需修改设备树文件，见[sensirion,shtcx](../sensor_realtek_rohm_sensirion_binding_reference/P026_sensirion_shtcx.md#std-dtcompatible-sensirion-shtcx)文档。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield sparkfun_shtc3，例如运行[通用数字温湿度传感器轮询](../sensors/P016_温湿度传感器轮询示例.md#dht_polling)示例：

```text
# From the root of the zephyr repository
west build -b adafruit_qt_py_rp2040 --shield sparkfun_shtc3 samples/sensor/dht_polling
```

---

[上一章](P174_Sparkfun_RV8803_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P176_SSD1306_128x64_32_pixels_generic_shield.md)
