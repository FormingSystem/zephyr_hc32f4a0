---
id: learning.zephyr-docs.hardware.adcvendor-1
title: Renesas_ADC_B通道选择
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第473章\_Renesas_ADC_B通道选择

原文：[group__renesas__adc__b__channels](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html)。读取日期：2026-10-13，`latest`。

## 473.1\_用途与头文件

本页列出 Renesas（瑞萨）RA 系列 ADC_B 控制器的**物理模拟输入通道（Physical Analog Input Channel）**标识符。ADC 为模数转换器（Analog-to-Digital Converter）。

```c
#include <zephyr/dt-bindings/adc/renesas-adc-b.h>
```

## 473.2\_在设备树中选择输入

将这些常量用于设备树通道节点的 `zephyr,input-positive` 属性，选择虚拟通道（Virtual Channel）实际采样的物理输入。

## 473.3\_通道常量

下面完整列出 0—22 的物理输入标识及其值。

| 宏 | 值 | 含义 |
| --- | --- | --- |
| [`RENESAS_ADC_B_CH0`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#gae3fccb66f3f204be77091606f2ba815b) | `0` | 物理模拟输入通道 0 |
| [`RENESAS_ADC_B_CH1`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#ga3070bebb15fa1d59fe5259737399ef39) | `1` | 物理模拟输入通道 1 |
| [`RENESAS_ADC_B_CH2`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#ga2e60dc6c7eee95d3384ea8d6e6555a7c) | `2` | 物理模拟输入通道 2 |
| [`RENESAS_ADC_B_CH3`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#ga1d5c59cb0b95ef52293b563974c5dcd1) | `3` | 物理模拟输入通道 3 |
| [`RENESAS_ADC_B_CH4`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#ga60e4c5eaaed261f7abda06cc62b72eda) | `4` | 物理模拟输入通道 4 |
| [`RENESAS_ADC_B_CH5`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#ga851cdbdc1d519d04c4357ff13f71c5cc) | `5` | 物理模拟输入通道 5 |
| [`RENESAS_ADC_B_CH6`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#gaadebd120eff7b7413edf92585835c37d) | `6` | 物理模拟输入通道 6 |
| [`RENESAS_ADC_B_CH7`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#gad9cb2ac0406c8ffa812cc64185dffc7a) | `7` | 物理模拟输入通道 7 |
| [`RENESAS_ADC_B_CH8`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#gae26dffcabcd28617d835a949010f47ff) | `8` | 物理模拟输入通道 8 |
| [`RENESAS_ADC_B_CH9`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#ga8ec4eca2df08d1911a9dade850ef7552) | `9` | 物理模拟输入通道 9 |
| [`RENESAS_ADC_B_CH10`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#gab9f15f8b48e6ad471af6560515e5516d) | `10` | 物理模拟输入通道 10 |
| [`RENESAS_ADC_B_CH11`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#ga00594235aa6ee1f7769869adae058b1f) | `11` | 物理模拟输入通道 11 |
| [`RENESAS_ADC_B_CH12`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#ga79ee547b1230a079b9f949e5aa8e118b) | `12` | 物理模拟输入通道 12 |
| [`RENESAS_ADC_B_CH13`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#ga2a4cb686ebf6a4f337aab72f4135ce69) | `13` | 物理模拟输入通道 13 |
| [`RENESAS_ADC_B_CH14`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#ga83bbaa0fb6f0b3fc4f9bf370cf7b12c8) | `14` | 物理模拟输入通道 14 |
| [`RENESAS_ADC_B_CH15`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#ga9a2c0bae6bff5723208d2467c3db0fd9) | `15` | 物理模拟输入通道 15 |
| [`RENESAS_ADC_B_CH16`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#ga826665fbbbf2353d66f88148eb5faa6b) | `16` | 物理模拟输入通道 16 |
| [`RENESAS_ADC_B_CH17`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#gafd4456c4ea4ddc9ae826a66fda26425e) | `17` | 物理模拟输入通道 17 |
| [`RENESAS_ADC_B_CH18`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#ga8f822dae3f6fcc990cebf4a49cabaca4) | `18` | 物理模拟输入通道 18 |
| [`RENESAS_ADC_B_CH19`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#gaee1c1a9acba7f80114119dd808858204) | `19` | 物理模拟输入通道 19 |
| [`RENESAS_ADC_B_CH20`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#ga6cc5f0f92c77439fb71a41c0349f9af9) | `20` | 物理模拟输入通道 20 |
| [`RENESAS_ADC_B_CH21`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#gaac460ba32ba67e9036b91a5e992a850e) | `21` | 物理模拟输入通道 21 |
| [`RENESAS_ADC_B_CH22`](https://docs.zephyrproject.org/latest/doxygen/html/group__renesas__adc__b__channels.html#ga9d255c29dc37c919dbd6e0cd978115eb) | `22` | 物理模拟输入通道 22 |

---

[上一章：ADS126X驱动接口](P472_ADS126X驱动接口.md) · [下一章：设备仿真与模拟](P474_设备仿真与模拟.md) · [返回大纲](大纲.md)
