---
id: learning.zephyr-docs.boards-shields.page-144
title: P3T1755DP Arduino Shield Evaluation Board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/p3t1755dp_ard_i2c/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="p3t1755dp-arduino-shield-evaluation-board"></a>

<a id="p3t1755dp-ard-i2c-shield"></a>

# 第144章\_P3T1755DP Arduino扩展评估板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/p3t1755dp_ard_i2c/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

P3T1755DP是精度±0.5 °C的温度数字转换器，范围−40～125 °C。

![官方原图：P3T1755DP ARD](images/p3t1755dp_ard.webp)

<a id="requirements"></a>

## 前置要求（Requirements）

温度寄存器始终保存12位二进制补码，分辨率0.0625 °C。可配置连续转换、单次转换或关断模式，支持双线串行I3C最高12.5 MHz及I2C最高3.4 MHz。

更多P3T1755DP-ARD信息见以下NXP资料：


- [P3T1755DP-ARD评估板入门指南](https://www.nxp.com/document/guide/getting-started-with-the-p3t1755dp-ard-evaluation-board:GS-P3T1755DP-ARD)
- [P3T1755DP-ARD评估板用户手册](https://www.nxp.com/docs/en/user-manual/UM11834.pdf)

<a id="hardware-connection"></a>

## 硬件连接（Hardware Connection）

p3t1755dp_ard扩展板的I3C模式


- J10、J11及J12连接3-5；原文I3C地址写0x4800000236152a0090，按来源保留。
- JP2及JP3连接1-2
- I3C从J13引出
- Arduino提供3.3 V VDD，JP1连接2-3

p3t1755dp_ard扩展板的I2C模式


- J10、J11及J12连接3-5，I2C地址0x48
- JP2及JP3连接2-3
- I2C来自Arduino J5第9脚SCL_ARD及第10脚SDA_ARD
- Arduino提供3.3 V VDD，JP1连接2-3

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield p3t1755dp_ard_i3c，例如：

```text
# From the root of the zephyr repository
west build -b mimxrt1180_evk/mimxrt1189/cm33 --shield p3t1755dp_ard_i3c samples/sensor/thermometer
```

## 译注

原文I3C地址0x4800000236152a0090照录，未当作已核实的常规动态地址。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [UM11834.pdf](https://www.nxp.com/docs/en/user-manual/UM11834.pdf)：HTTP Error 404: Not Found。
- [getting-started-with-the-p3t1755dp-ard-evaluation-board:GS-P3T1755DP-ARD](https://www.nxp.com/document/guide/getting-started-with-the-p3t1755dp-ard-evaluation-board:GS-P3T1755DP-ARD)：HTTP Error 404: Not Found。

---

[上一章](P143_OpenThread_RCP_over_Arduino_header.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P145_Digilent_Pmod_ACL.md)
