---
id: learning.zephyr-docs.boards-shields.page-198
title: Waveshare Pico UPS-B shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/waveshare_ups/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="waveshare-pico-ups-b-shield"></a>

<a id="id1"></a>

# 第198章\_Waveshare Pico UPS-B不间断电源扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/waveshare_ups/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Waveshare Pico UPS-B是为树莓派Pico设计的不间断电源（UPS）模块，采用Texas Instruments INA219电流／功率监测器，通过I2C与Pico通信。

<a id="id2"></a>

![官方原图：Waveshare Pico UPS-B shield](images/waveshare_pico_ups_b.jpg)

Waveshare Pico UPS-B不间断电源扩展板（Shield）

<a id="hardware"></a>

### 硬件（Hardware）


- INA219

  > - 测量0～26 V总线电压
  > - 报告电流、电压及功率
  > - 16个可编程地址
  > - SOT23-8及SOIC-8封装
  > - 校准寄存器
- ETA6003

  > - 带电源路径管理的开关充电器
  > - DC-DC效率最高95%
  > - 电源路径MOSFET为0 mΩ，按原文保留
  > - 最大充电电流2.5 A
- 连接能力（Connectivity）

  > - 兼容树莓派Pico，I2C接口
  > - 用于锂聚合物电池的2针JST接头
- 电源（Power Supply）

  > - 3.3～5 V
- 组件（Components）

  > - 电源开关
  > - 电源LED
  > - 充电LED

Waveshare Pico UPS-B的更多信息：


- [Waveshare Pico UPS网站](https://www.waveshare.com/wiki/Pico-UPS-B)
- [INA219数据手册](https://www.ti.com/lit/ds/symlink/ina219.pdf)
- [ETA6003数据手册](https://www.waveshare.com/w/upload/3/3f/ETA6003.pdf)

<a id="programming"></a>

## 编程（Programming）

在Zephyr应用中调用west build或cmake时设置--shield waveshare_pico_ups_b，例如：

```text
# From the root of the zephyr repository
west build -b rpi_pico --shield waveshare_pico_ups_b samples/sensor/ina219
west flash
```

## 译注

原文电源路径MOSFET标为0 mΩ，照录并注明来源。

---

[上一章](P197_Waveshare_1.3inch_OLED_Display_Module_for_Raspberry_Pi_Pico.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P199_WeAct_Studio_MiniSTM32H7xx_OV2640_Camera_Sensor.md)
