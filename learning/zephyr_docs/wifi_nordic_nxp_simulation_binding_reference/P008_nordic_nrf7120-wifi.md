---
id: learning.zephyr-docs.wifi-nordic-nxp-simulation-binding-reference.page-8
title: nordic_nrf7120-wifi
kind: reference
status: maintained
domains: [zephyr, devicetree, wifi]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/wifi/nordic,nrf7120-wifi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第8章\_nordic_nrf7120-wifi

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/wifi/nordic,nrf7120-wifi.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nordic-nrf7120-wifi"></a>
<a id="dtbinding-nordic-nrf7120-wifi"></a>
<a id="std-dtcompatible-nordic-nrf7120-wifi"></a>

兼容字符串（Compatible String）：`nordic,nrf7120-wifi`。厂商：[ Nordic Semiconductor ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nordic)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nordic,nrf7120-wifi)。

<a id="description"></a>

nRF7120 Wi-Fi与蓝牙组合SoC的Wi-Fi域（Wi-Fi Domain）。

译注术语：HT为高吞吐量（High Throughput），VHT为甚高吞吐量（Very High Throughput），HE为高效率（High Efficiency），MCS为调制与编码方案（Modulation and Coding Scheme）；数字20、40、80、160表示相应信道带宽。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 8.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `nordic,wifi-xo-freq-offset` | `int` | 晶体振荡器（Crystal Oscillator，XO）频率偏移微调，由Wi-Fi固件用于与频率、温度和电压相关的校准。这是取决于所用晶体的板级参数，典型默认值为0；固件按8位有符号值解释。；默认值：`0` |
| `wifi-max-tx-pwr-2g-dsss` | `int` | 2.4 GHz频段使用直接序列扩频／补码键控（DSSS/CCK）速率时允许的最大发射功率。；默认值：`18` |
| `wifi-max-tx-pwr-2g-mcs0` | `int` | 2.4 GHz频段使用调制编码方案0（Modulation and Coding Scheme 0，MCS0）时允许的最大发射功率。；默认值：`14` |
| `wifi-max-tx-pwr-2g-mcs7` | `int` | 2.4 GHz频段使用调制编码方案7（MCS7）时允许的最大发射功率。；默认值：`14` |
| `wifi-max-tx-pwr-5g-low-mcs0` | `int` | 5 GHz低子频段使用MCS0时允许的最大发射功率。；默认值：`10` |
| `wifi-max-tx-pwr-5g-low-mcs7` | `int` | 5 GHz低子频段使用MCS7时允许的最大发射功率。；默认值：`10` |
| `wifi-max-tx-pwr-5g-mid-mcs0` | `int` | 5 GHz中子频段使用MCS0时允许的最大发射功率。；默认值：`10` |
| `wifi-max-tx-pwr-5g-mid-mcs7` | `int` | 5 GHz中子频段使用MCS7时允许的最大发射功率。；默认值：`10` |
| `wifi-max-tx-pwr-5g-high-mcs0` | `int` | 5 GHz高子频段使用MCS0时允许的最大发射功率。；默认值：`10` |
| `wifi-max-tx-pwr-5g-high-mcs7` | `int` | 5 GHz高子频段使用MCS7时允许的最大发射功率。；默认值：`10` |
| `wifi-max-tx-pwr-6g-band1-mcs0` | `int` | 6 GHz频段1使用MCS0时允许的最大发射功率（Maximum TX Power）。；默认值：`10` |
| `wifi-max-tx-pwr-6g-band1-mcs7` | `int` | 6 GHz频段1使用MCS7时允许的最大发射功率（Maximum TX Power）。；默认值：`10` |
| `wifi-max-tx-pwr-6g-band2-mcs0` | `int` | 6 GHz频段2使用MCS0时允许的最大发射功率（Maximum TX Power）。；默认值：`10` |
| `wifi-max-tx-pwr-6g-band2-mcs7` | `int` | 6 GHz频段2使用MCS7时允许的最大发射功率（Maximum TX Power）。；默认值：`10` |
| `wifi-max-tx-pwr-6g-band3-mcs0` | `int` | 6 GHz频段3使用MCS0时允许的最大发射功率（Maximum TX Power）。；默认值：`10` |
| `wifi-max-tx-pwr-6g-band3-mcs7` | `int` | 6 GHz频段3使用MCS7时允许的最大发射功率（Maximum TX Power）。；默认值：`10` |
| `wifi-max-tx-pwr-6g-band4-mcs0` | `int` | 6 GHz频段4使用MCS0时允许的最大发射功率（Maximum TX Power）。；默认值：`10` |
| `wifi-max-tx-pwr-6g-band4-mcs7` | `int` | 6 GHz频段4使用MCS7时允许的最大发射功率（Maximum TX Power）。；默认值：`10` |
| `wifi-max-tx-pwr-6g-band5-mcs0` | `int` | 6 GHz频段5使用MCS0时允许的最大发射功率（Maximum TX Power）。；默认值：`10` |
| `wifi-max-tx-pwr-6g-band5-mcs7` | `int` | 6 GHz频段5使用MCS7时允许的最大发射功率（Maximum TX Power）。；默认值：`10` |
| `wifi-max-tx-pwr-6g-band6-mcs0` | `int` | 6 GHz频段6使用MCS0时允许的最大发射功率（Maximum TX Power）。；默认值：`10` |
| `wifi-max-tx-pwr-6g-band6-mcs7` | `int` | 6 GHz频段6使用MCS7时允许的最大发射功率（Maximum TX Power）。；默认值：`10` |
| `nordic,wifi-ant-gain-2g` | `int` | 2.4 GHz频段的净天线增益（Net Antenna Gain），单位dB，步长1 dB，有效范围−8～7。此值等于天线增益减去通往天线的射频路径损耗；路径损耗大于天线增益的开发板应填写负值。；默认值：`0` |
| `nordic,wifi-ant-gain-5g-band1` | `int` | 5 GHz频段1（5150～5350 MHz）的净天线增益（Net Antenna Gain），单位dB，步长1 dB，有效范围−8～7。此值等于天线增益减去通往天线的射频路径损耗；路径损耗大于天线增益的开发板应填写负值。；默认值：`0` |
| `nordic,wifi-ant-gain-5g-band2` | `int` | 5 GHz频段2（5470～5730 MHz）的净天线增益（Net Antenna Gain），单位dB，步长1 dB，有效范围−8～7。此值等于天线增益减去通往天线的射频路径损耗；路径损耗大于天线增益的开发板应填写负值。；默认值：`0` |
| `nordic,wifi-ant-gain-5g-band3` | `int` | 5 GHz频段3（5730～5895 MHz）的净天线增益（Net Antenna Gain），单位dB，步长1 dB，有效范围−8～7。此值等于天线增益减去通往天线的射频路径损耗；路径损耗大于天线增益的开发板应填写负值。；默认值：`0` |
| `nordic,wifi-ant-gain-6g-band1` | `int` | 6 GHz频段1（5935～6015 MHz）的净天线增益（Net Antenna Gain），单位dB，步长1 dB，有效范围−8～7。此值等于天线增益减去通往天线的射频路径损耗；路径损耗大于天线增益的开发板应填写负值。；默认值：`0` |
| `nordic,wifi-ant-gain-6g-band2` | `int` | 6 GHz频段2（6035～6115 MHz）的净天线增益（Net Antenna Gain），单位dB，步长1 dB，有效范围−8～7。此值等于天线增益减去通往天线的射频路径损耗；路径损耗大于天线增益的开发板应填写负值。；默认值：`0` |
| `nordic,wifi-ant-gain-6g-band3` | `int` | 6 GHz频段3（6135～6215 MHz）的净天线增益（Net Antenna Gain），单位dB，步长1 dB，有效范围−8～7。此值等于天线增益减去通往天线的射频路径损耗；路径损耗大于天线增益的开发板应填写负值。；默认值：`0` |
| `nordic,wifi-ant-gain-6g-band4` | `int` | 6 GHz频段4（6235～6315 MHz）的净天线增益（Net Antenna Gain），单位dB，步长1 dB，有效范围−8～7。此值等于天线增益减去通往天线的射频路径损耗；路径损耗大于天线增益的开发板应填写负值。；默认值：`0` |
| `nordic,wifi-ant-gain-6g-band5` | `int` | 6 GHz频段5（6335～6415 MHz）的净天线增益（Net Antenna Gain），单位dB，步长1 dB，有效范围−8～7。此值等于天线增益减去通往天线的射频路径损耗；路径损耗大于天线增益的开发板应填写负值。；默认值：`0` |
| `nordic,wifi-ant-gain-6g-band6` | `int` | 6 GHz频段6（6435～6475 MHz）的净天线增益（Net Antenna Gain），单位dB，步长1 dB，有效范围−8～7。此值等于天线增益减去通往天线的射频路径损耗；路径损耗大于天线增益的开发板应填写负值。；默认值：`0` |
| `nordic,wifi-2g-lower-edge-ceiling-dsss` | `int` | 2.4 GHz频段（2412～2484 MHz）下边缘使用DSSS/CCK速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-2g-lower-edge-ceiling-ht` | `int` | 2.4 GHz频段（2412～2484 MHz）下边缘使用HT/VHT速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-2g-lower-edge-ceiling-he` | `int` | 2.4 GHz频段（2412～2484 MHz）下边缘使用HE速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-2g-upper-edge-ceiling-dsss` | `int` | 2.4 GHz频段（2412～2484 MHz）上边缘使用DSSS/CCK速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-2g-upper-edge-ceiling-ht` | `int` | 2.4 GHz频段（2412～2484 MHz）上边缘使用HT/VHT速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-2g-upper-edge-ceiling-he` | `int` | 2.4 GHz频段（2412～2484 MHz）上边缘使用HE速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-1-lower-edge-ceiling-ht` | `int` | UNII-1频段（5160～5240 MHz）下边缘使用HT/VHT速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-1-lower-edge-ceiling-he` | `int` | UNII-1频段（5160～5240 MHz）下边缘使用HE速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-1-upper-edge-ceiling-ht` | `int` | UNII-1频段（5160～5240 MHz）上边缘使用HT/VHT速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-1-upper-edge-ceiling-he` | `int` | UNII-1频段（5160～5240 MHz）上边缘使用HE速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-2a-lower-edge-ceiling-ht` | `int` | UNII-2A频段（5260～5340 MHz）下边缘使用HT/VHT速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-2a-lower-edge-ceiling-he` | `int` | UNII-2A频段（5260～5340 MHz）下边缘使用HE速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-2a-upper-edge-ceiling-ht` | `int` | UNII-2A频段（5260～5340 MHz）上边缘使用HT/VHT速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-2a-upper-edge-ceiling-he` | `int` | UNII-2A频段（5260～5340 MHz）上边缘使用HE速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-2c-lower-edge-ceiling-ht` | `int` | UNII-2C频段（5480～5720 MHz）下边缘使用HT/VHT速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-2c-lower-edge-ceiling-he` | `int` | UNII-2C频段（5480～5720 MHz）下边缘使用HE速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-2c-upper-edge-ceiling-ht` | `int` | UNII-2C频段（5480～5720 MHz）上边缘使用HT/VHT速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-2c-upper-edge-ceiling-he` | `int` | UNII-2C频段（5480～5720 MHz）上边缘使用HE速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-3-lower-edge-ceiling-ht` | `int` | UNII-3频段（5745～5825 MHz）下边缘使用HT/VHT速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-3-lower-edge-ceiling-he` | `int` | UNII-3频段（5745～5825 MHz）下边缘使用HE速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-3-upper-edge-ceiling-ht` | `int` | UNII-3频段（5745～5825 MHz）上边缘使用HT/VHT速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-3-upper-edge-ceiling-he` | `int` | UNII-3频段（5745～5825 MHz）上边缘使用HE速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-4-lower-edge-ceiling-ht` | `int` | UNII-4频段（5845～5885 MHz）下边缘使用HT/VHT速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-4-lower-edge-ceiling-he` | `int` | UNII-4频段（5845～5885 MHz）下边缘使用HE速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-4-upper-edge-ceiling-ht` | `int` | UNII-4频段（5845～5885 MHz）上边缘使用HT/VHT速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-4-upper-edge-ceiling-he` | `int` | UNII-4频段（5845～5885 MHz）上边缘使用HE速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-5-lower-edge-ceiling-ht` | `int` | UNII-5频段（5935～6415 MHz）下边缘使用HT/VHT速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-5-lower-edge-ceiling-he` | `int` | UNII-5频段（5935～6415 MHz）下边缘使用HE速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-5-upper-edge-ceiling-ht` | `int` | UNII-5频段（5935～6415 MHz）上边缘使用HT/VHT速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-5-upper-edge-ceiling-he` | `int` | UNII-5频段（5935～6415 MHz）上边缘使用HE速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-6-lower-edge-ceiling-ht` | `int` | UNII-6频段（6435～6735 MHz）下边缘使用HT/VHT速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-6-lower-edge-ceiling-he` | `int` | UNII-6频段（6435～6735 MHz）下边缘使用HE速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-6-upper-edge-ceiling-ht` | `int` | UNII-6频段（6435～6735 MHz）上边缘使用HT/VHT速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |
| `nordic,wifi-unii-6-upper-edge-ceiling-he` | `int` | UNII-6频段（6435～6735 MHz）上边缘使用HE速率时允许的最大发射功率（Maximum TX Power），单位dBm，步长1 dBm，有效范围0～31。默认31表示在该频段既有发射功率上限之外不再附加限制。；默认值：`31` |

本页没有已弃用的节点专用属性。

---

[上一章](P007_nordic_nrf7002-spi.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P009_nordic_wlan.md)
