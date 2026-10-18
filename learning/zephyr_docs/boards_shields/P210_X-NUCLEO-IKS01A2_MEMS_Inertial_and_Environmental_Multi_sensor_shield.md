---
id: learning.zephyr-docs.boards-shields.page-210
title: X-NUCLEO-IKS01A2 MEMS Inertial and Environmental Multi sensor shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_iks01a2/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="x-nucleo-iks01a2-mems-inertial-and-environmental-multi-sensor-shield"></a>

<a id="x-nucleo-iks01a2"></a>

# 第210章\_X-NUCLEO-IKS01A2：MEMS惯性及环境多传感器扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_iks01a2/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

X-NUCLEO-IKS01A2是面向STM32 Nucleo的运动MEMS及环境传感器扩展板，采用Arduino UNO R3连接器布局，集成LSM6DSL三轴加速度计及陀螺仪、LSM303AGR三轴加速度计及磁力计、HTS221温湿度传感器及LPS22HB压力传感器。

X-NUCLEO-IKS01A2通过I2C引脚与STM32微控制器连接，可更改默认I2C端口。

![官方原图：X-NUCLEO-IKS01A2](images/x-nucleo-iks01a2.jpg)

<a id="id2"></a>

更多信息见X-NUCLEO-IKS01A2网站[注1](#id1)。（[X-NUCLEO-IKS01A2 网站](https://www.st.com/en/ecosystems/x-nucleo-iks01a2.html)）

<a id="hardware"></a>

## 硬件（Hardware）

X-NUCLEO-IKS01A2主要特性：

> - LSM6DSL：MEMS三轴加速度计，±2／±4／±8／±16 g；三轴陀螺仪，±125／±245／±500／±1000／±2000 dps
> - LM303AGR：MEMS三轴加速度计，±2／±4／±8／±16 g；三轴磁力计，±50高斯；型号拼写按原文保留
> - LPS22HB：MEMS压力传感器，260～1260 hPa绝对压力数字输出气压计
> - HTS221：电容式数字相对湿度及温度传感器
> - DIL24插座，用于额外MEMS适配器及其他传感器
> - 可使用LSM6DSL的I²C传感器集线器（Sensor Hub）功能
> - 配备Arduino UNO R3连接器
> - 符合RoHS

X-NUCLEO-IKS01A2的更多信息：


- <a id="id4"></a>

  X-NUCLEO-IKS01A2产品简介[注2](#id3)（[X-NUCLEO-IKS01A2 产品简介](https://www.st.com/resource/en/data_brief/x-nucleo-iks01a2.pdf)）

<a id="hardware-configuration"></a>

## 硬件配置（Hardware Configuration）

X-NUCLEO-IKS01A2将各设备连接到2条独立I2C总线：


- LSM6DL位于I2C2，型号拼写按原文保留。
- LSM303AGR、LPS22HB及HTS221位于I2C1。

X-NUCLEO-IKS01A2可配置为模式1或模式2。

<a id="mode-1-standard-mode"></a>

### 模式1：标准模式（Standard Mode）

标准I2C模式下，两条总线连在一起，因此扩展板上的所有设备都在同一I2C总线上，主板可通过I2C访问。

启用该模式的跳线配置为：


- JP7连接1-2及3-4，I2C1 = I2C2，I2Cx = GND
- JP8连接1-2及3-4，I2C1 = I2C2，I2Cx = GND

<a id="mode-2-sensorhub-mode"></a>

### 模式2：传感器集线器模式（SensorHub Mode）

SensorHub模式下，LSM6DSL连接I2C2，主板可直接访问。所有其他设备通过I2C1连接LSM6DSL主接口。

启用该模式的跳线配置为：


- JP7连接2-3，I2C1 = I2Cx
- JP8连接2-3，I2C1 = I2Cx

<a id="id5"></a>

X-NUCLEO-IKS01A2配置模式详情见其产品简介[注2](#id3)。（[X-NUCLEO-IKS01A2 产品简介](https://www.st.com/resource/en/data_brief/x-nucleo-iks01a2.pdf)）

<a id="programming"></a>

## 编程（Programming）

为x-nucleo-iks01a2扩展板提供2个示例：


- X-NUCLEO-IKS01A2标准模式1示例，适用于扩展板配置为Standard Mode时。（[X-NUCLEO-IKS01A2 扩展板 - 标准模式1](../shield_samples/P010_IKS01A2标准模式.md#x-nucleo-iks01a2-std)）
- X-NUCLEO-IKS01A2传感器集线器模式2示例，适用于扩展板配置为SensorHub Mode时。（[X-NUCLEO-IKS01A2 扩展板 - 传感器集线器模式2](../shield_samples/P011_IKS01A2传感器集线器模式.md#x-nucleo-iks01a2-shub)）

更多说明另见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.st.com/en/ecosystems/x-nucleo-iks01a2.html](https://www.st.com/en/ecosystems/x-nucleo-iks01a2.html)

<a id="id3"></a>

〔2〕 ([1](#id4),[2](#id5)) [https://www.st.com/resource/en/data_brief/x-nucleo-iks01a2.pdf](https://www.st.com/resource/en/data_brief/x-nucleo-iks01a2.pdf)

## 译注

原文LSM6DL、LM303AGR等型号拼写按来源保留；两种模式的跳线不能混用。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [x-nucleo-iks01a2.html](https://www.st.com/en/ecosystems/x-nucleo-iks01a2.html)：HTTP Error 567: Unknown Status。
- [x-nucleo-iks01a2.pdf](https://www.st.com/resource/en/data_brief/x-nucleo-iks01a2.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P209_X-NUCLEO-IKS01A1_MEMS_Inertial_and_Environmental_Multi_sensor_shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P211_X-NUCLEO-IKS01A3_MEMS_Inertial_and_Environmental_Multi_sensor_shield.md)
