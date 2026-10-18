---
id: learning.zephyr-docs.boards-shields.page-211
title: X-NUCLEO-IKS01A3 MEMS Inertial and Environmental Multi sensor shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_iks01a3/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="x-nucleo-iks01a3-mems-inertial-and-environmental-multi-sensor-shield"></a>

<a id="x-nucleo-iks01a3"></a>

# 第211章\_X-NUCLEO-IKS01A3：MEMS惯性及环境多传感器扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_iks01a3/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

X-NUCLEO-IKS01A3是面向STM32 Nucleo的运动MEMS及环境传感器扩展板，采用Arduino UNO R3连接器布局，集成LSM6DSO三轴加速度计及陀螺仪、LIS2MDL三轴磁力计、LIS2DW12三轴加速度计、HTS221温湿度传感器、LPS22HH压力传感器及STTS751温度传感器。

X-NUCLEO-IKS01A3通过I2C引脚与STM32微控制器连接，可更改默认I2C端口。

![官方原图：X-NUCLEO-IKS01A3](images/x-nucleo-iks01a3.jpg)

<a id="id2"></a>

更多信息见X-NUCLEO-IKS01A3网站[注1](#id1)。（[X-NUCLEO-IKS01A3 网站](https://www.st.com/en/ecosystems/x-nucleo-iks01a3.html)）

<a id="hardware-description"></a>

## 硬件说明（Hardware Description）

X-NUCLEO-IKS01A3主要特性：

> - LSM6DO：MEMS三轴加速度计，±2／±4／±8／±16 g；三轴陀螺仪，±125／±250／±500／±1000／±2000 dps；型号拼写按原文保留
> - LIS2MDL：MEMS三轴磁力计，±50高斯
> - LIS2DW12：MEMS三轴加速度计，±2／±4／±8／±16 g
> - LPS22HH：MEMS压力传感器，260～1260 hPa绝对压力数字输出气压计
> - HTS221：电容式数字相对湿度及温度传感器
> - STTS751：温度传感器，−40～+125 °C
> - DIL24插座，用于额外MEMS适配器及其他传感器，可配置I2C或SPI
> - 可使用LSM6DSO的I2C传感器集线器功能
> - 兼容STM32 Nucleo开发板
> - 配备Arduino UNO R3连接器
> - 符合RoHS
> - 符合WEEE

<a id="hardware-configuration"></a>

## 硬件配置（Hardware Configuration）

X-NUCLEO-IKS01A3将各设备连接到2条独立I2C总线：


- LIS2DW12及LSM6DO位于I2C2，后者型号拼写按原文保留。
- LIS2MDL、LPS22HH、HTS221及STTS751位于I2C1。

X-NUCLEO-IKS01A3可配置为模式1或模式2。

<a id="mode-1-standard-mode"></a>

### 模式1：标准模式（Standard Mode）

标准I2C模式下，两条总线连在一起，因此扩展板上的所有设备都在同一I2C总线上，主板可通过I2C访问。

启用该模式的跳线配置为：


- JP7连接1-2及3-4，I2C1 = I2C2，I2Cx = GND
- JP8连接1-2及3-4，I2C1 = I2C2，I2Cx = GND

<a id="mode-2-sensorhub-mode"></a>

### 模式2：传感器集线器模式（SensorHub Mode）

SensorHub模式下，LSM6DSO及LIS2DW12连接I2C2，主板可直接访问。所有其他设备通过I2C1连接LSM6DSO主接口。

启用该模式的跳线配置为：


- JP7连接2-3，I2C1 = I2Cx
- JP8连接2-3，I2C1 = I2Cx

<a id="id4"></a>

X-NUCLEO-IKS01A3配置模式详情见其用户手册[注2](#id3)。（[X-NUCLEO-IKS01A3 用户手册](https://www.st.com/resource/en/user_manual/dm00601501.pdf)）

<a id="programming"></a>

## 编程（Programming）

为x-nucleo-iks01a3扩展板提供2个示例：


- X-NUCLEO-IKS01A3标准模式1示例，适用于扩展板配置为Standard Mode时。（[X-NUCLEO-IKS01A3 扩展板 - 标准模式1](../shield_samples/P013_IKS01A3标准模式.md#x-nucleo-iks01a3-std)）
- X-NUCLEO-IKS01A3传感器集线器模式2示例，适用于扩展板配置为SensorHub Mode时。（[X-NUCLEO-IKS01A3 扩展板 - 传感器集线器模式2](../shield_samples/P014_IKS01A3传感器集线器模式.md#x-nucleo-iks01a3-shub)）

更多说明另见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.st.com/en/ecosystems/x-nucleo-iks01a3.html](https://www.st.com/en/ecosystems/x-nucleo-iks01a3.html)

<a id="id3"></a>

〔[2](#id4)〕 [https://www.st.com/resource/en/user_manual/dm00601501.pdf](https://www.st.com/resource/en/user_manual/dm00601501.pdf)

## 译注

原文特性与总线段出现LSM6DO拼写，概述为LSM6DSO，差异已注明。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [x-nucleo-iks01a3.html](https://www.st.com/en/ecosystems/x-nucleo-iks01a3.html)：HTTP Error 567: Unknown Status。
- [dm00601501.pdf](https://www.st.com/resource/en/user_manual/dm00601501.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P210_X-NUCLEO-IKS01A2_MEMS_Inertial_and_Environmental_Multi_sensor_shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P212_X-NUCLEO-IKS02A1_MEMS_Inertial_and_Environmental_Multi_sensor_shield.md)
