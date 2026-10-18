---
id: learning.zephyr-docs.boards-shields.page-212
title: X-NUCLEO-IKS02A1 MEMS Inertial and Environmental Multi sensor shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_iks02a1/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="x-nucleo-iks02a1-mems-inertial-and-environmental-multi-sensor-shield"></a>

<a id="x-nucleo-iks02a1"></a>

# 第212章\_X-NUCLEO-IKS02A1：MEMS惯性及环境多传感器扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_iks02a1/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

X-NUCLEO-IKS02A1是面向STM32 Nucleo、满足工业应用需求的运动MEMS扩展板，采用Arduino UNO R3连接器布局，集成ISM330DHCX三轴加速度计及陀螺仪、IIS2MDC三轴磁力计、IIS2DLPC三轴加速度计及IMP34DT05数字麦克风。

X-NUCLEO-IKS02A1通过I2C引脚与STM32微控制器连接，可更改默认I2C端口。

![官方原图：X-NUCLEO-IKS02A1](images/x-nucleo-iks02a1.jpg)

<a id="id2"></a>

更多信息见X-NUCLEO-IKS02A1网站[注1](#id1)。（[X-NUCLEO-IKS02A1 网站](https://www.st.com/en/ecosystems/x-nucleo-iks02a1.html)）

<a id="hardware-description"></a>

## 硬件说明（Hardware Description）

X-NUCLEO-IKS02A1主要特性：

> - ISM330DHCX：MEMS三轴加速度计，±2／±4／±8／±16 g；三轴陀螺仪，±125／±250／±500／±1000／±2000 dps
> - IIS2MDC：MEMS三轴磁力计，±50高斯
> - IIS2DLPC：低功耗MEMS三轴加速度计，±2／±4／±8／±16 g
> - IMP34DT05：MEMS数字全向麦克风，灵敏度−26 dBFS，偏差±3 dB
> - DIL24插座，用于额外MEMS适配器及其他传感器，可配置I2C或SPI
> - 可使用ISM330DHCX的I2C传感器集线器功能
> - 兼容STM32 Nucleo开发板
> - 配备Arduino UNO R3连接器
> - 符合RoHS
> - 符合WEEE

<a id="hardware-configuration"></a>

## 硬件配置（Hardware Configuration）

X-NUCLEO-IKS02A1将各设备连接到2条独立I2C总线：


- IIS2DLPC及ISM330DHCX位于I2C2。
- IIS2MDC位于I2C1。

X-NUCLEO-IKS02A1可配置为模式1及模式2两种硬件模式，用JP7／JP8改变I2C1总线连接对象。

<a id="mode-1-standard-mode"></a>

### 模式1：标准模式（Standard Mode）

标准I2C模式下，两条总线连在一起，因此扩展板上的所有设备都在同一I2C总线上，主板MCU可直接访问。

启用该模式的跳线配置为：


- JP7连接1-2及3-4，I2C1 = I2C2，I2Cx = GND
- JP8连接1-2及3-4，I2C1 = I2C2，I2Cx = GND

<a id="mode-2-sensorhub-mode"></a>

### 模式2：传感器集线器模式（SensorHub Mode）

SensorHub模式下，ISM330DHCX及IIS2DLPC连接I2C2，主板MCU可直接访问。IIS2MDC则仅通过ISM330DHCX的SCx／SDX，即I2Cx引脚，连接到该传感器。

启用该模式的跳线配置为：


- JP7连接2-3，I2C1 = I2Cx
- JP8连接2-3，I2C1 = I2Cx

<a id="id4"></a>

X-NUCLEO-IKS02A1配置模式详情见其用户手册[注2](#id3)。（[X-NUCLEO-IKS02A1 用户手册](https://www.st.com/resource/en/user_manual/DM00651686.pdf)）

<a id="programming"></a>

## 编程（Programming）

为x-nucleo-iks02a1扩展板提供3个示例：


- X-NUCLEO-IKS02A1标准模式1应用，适用于Standard Mode。（[X-NUCLEO-IKS02A1 扩展板 - 标准模式1](../shield_samples/P016_IKS02A1标准模式.md#x-nucleo-iks02a1-std)）
- X-NUCLEO-IKS02A1传感器集线器模式2应用，适用于SensorHub Mode。（[X-NUCLEO-IKS02A1 扩展板 - 传感器集线器模式2](../shield_samples/P017_IKS02A1传感器集线器模式.md#x-nucleo-iks02a1-shub)）
- X-NUCLEO-IKS02A1 MEMS麦克风应用，用于从板载PDM麦克风采集数据。（[X-NUCLEO-IKS02A1 扩展板 - MEMS麦克风](../hardware/P082_扩展板MEMS麦克风示例.md#x-nucleo-iks02a1-mic)）

更多说明另见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.st.com/en/ecosystems/x-nucleo-iks02a1.html](https://www.st.com/en/ecosystems/x-nucleo-iks02a1.html)

<a id="id3"></a>

〔[2](#id4)〕 [https://www.st.com/resource/en/user_manual/DM00651686.pdf](https://www.st.com/resource/en/user_manual/DM00651686.pdf)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [x-nucleo-iks02a1.html](https://www.st.com/en/ecosystems/x-nucleo-iks02a1.html)：HTTP Error 567: Unknown Status。
- [DM00651686.pdf](https://www.st.com/resource/en/user_manual/DM00651686.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P211_X-NUCLEO-IKS01A3_MEMS_Inertial_and_Environmental_Multi_sensor_shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P213_X-NUCLEO-IKS4A1_MEMS_Inertial_and_Environmental_Multi_sensor_shield.md)
