---
id: learning.zephyr-docs.boards-shields.page-134
title: NXP Arduino WiFi and BT Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/nxp_arduino_wifi_bt/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nxp-arduino-wifi-and-bt-shield"></a>

<a id="nxp-arduino-wifi-bt"></a>

# 第134章\_NXP Arduino Wi-Fi及蓝牙扩展板（BT Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/nxp_arduino_wifi_bt/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

该扩展板采用NXP无线SoC模块及Arduino外形，为MCXN平台提供Wi-Fi与Bluetooth连接。

<a id="supported-shields"></a>

## 支持的扩展板（Supported Shields）

支持以下配置：


- nxp_arduino_aw510_wifi_bt：采用AW510模块IW416的Arduino Wi-Fi／蓝牙扩展板

<a id="requirements"></a>

## 前置要求（Requirements）


- Azurewave AW510模块
- Bluetooth HCI的UART接口
- Wi-Fi的SDIO接口

<a id="connections-and-ios"></a>

### 连接与输入输出（Connections and IOs）

扩展板使用以下接口：


- UART用于Bluetooth HCI通信
- SDIO用于Wi-Fi通信
- GPIO用于复位、电源及唤醒等控制

<a id="programming"></a>

## 编程（Programming）

构建应用时，将--shield <option>设为以下扩展板名称之一：


- nxp_arduino_aw510_wifi_bt：用于采用NXP IW416的Wi-Fi／Bluetooth示例

例如：

```text
# From the root of the zephyr repository
west build -b frdm_mcxn947/mcxn947/cpu0 --shield nxp_arduino_aw510_wifi_bt samples/bluetooth/peripheral_hr
```

<a id="references"></a>

## 参考资料（References）

---

[上一章](P133_NXP_ADTJA1101-RMII_Automotive_Ethernet_Adapter.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P135_NXP_BTB-44_OV5640_Camera_Module.md)
