---
id: learning.zephyr-docs.boards-shields.page-14
title: Adafruit DS2484 Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_ds2484/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-ds2484-shield"></a>

<a id="adafruit-ds2484"></a>

# 第14章\_Adafruit DS2484扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_ds2484/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit DS2484 I2C转单总线扩展板采用Analog Devices DS2484单总线主控制器（1-Wire Master），带2个STEMMA QT连接器。（[Adafruit DS2484 I2C转单总线适配器 扩展板](https://learn.adafruit.com/adafruit-ds2484-i2c-to-1-wire-bus-adapter-breakout)；[Analog Devices DS2484 单总线主控制器](https://www.analog.com/en/products/ds2484.html)）

<a id="id1"></a>

![官方原图：Adafruit DS2484 Shield](images/adafruit_ds2484.webp)

Adafruit DS2484扩展板（Shield），图片来源：Adafruit

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
<td>DS2484 I2C数据线（SDA）</td>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>DS2484 I2C时钟线（SCL）</td>
</tr>
<tr>
<td>1WIRE</td>
<td>连接单总线1-Wire设备</td>
</tr>
<tr>
<td>SLPZ</td>
<td>用于睡眠模式的数字输入</td>
</tr>
</table>

如何为睡眠模式等修改设备树，见[maxim,ds2484](../mux_w1_binding_reference/P009_maxim_ds2484.md#std-dtcompatible-maxim-ds2484)绑定文档。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_ds2484，例如运行单总线1-Wire扫描示例：（[单总线扫描器（1-Wire Scanner）](../driver_samples/P010_单总线扫描示例.md#w1-scanner)）

```text
# From the root of the zephyr repository
west build -b adafruit_qt_py_rp2040 --shield adafruit_ds2484 samples/drivers/w1/scanner
```

运行扫描示例前，将一个或多个1-Wire设备接到扩展板。

---

[上一章](P013_Adafruit_DRV2605L_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P015_Adafruit_FeatherWing_128x32_OLED_Shield.md)
