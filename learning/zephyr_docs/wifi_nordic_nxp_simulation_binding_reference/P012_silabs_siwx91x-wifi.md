---
id: learning.zephyr-docs.wifi-nordic-nxp-simulation-binding-reference.page-12
title: silabs_siwx91x-wifi
kind: reference
status: maintained
domains: [zephyr, devicetree, wifi]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/wifi/silabs,siwx91x-wifi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第12章\_silabs_siwx91x-wifi

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/wifi/silabs,siwx91x-wifi.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="silabs-siwx91x-wifi"></a>
<a id="dtbinding-silabs-siwx91x-wifi"></a>
<a id="std-dtcompatible-silabs-siwx91x-wifi"></a>

兼容字符串（Compatible String）：`silabs,siwx91x-wifi`。厂商：[ Silicon Laboratories ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-silabs)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=silabs,siwx91x-wifi)。

驱动源码（Driver Source）：[drivers/wifi/siwx91x/siwx91x_wifi.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/siwx91x/siwx91x_wifi.c)。

<a id="description"></a>

Silicon Labs SiWx91x SoC的Wi-Fi设备。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 12.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `wifi-max-tx-pwr-scan` | `int` | Wi-Fi扫描时使用的最大发射功率（Maximum TX Power），单位dBm；实际输出可能受法规或硬件约束限制。注意：SiWx91x固件**不支持按速率分别设置功率（Per-Rate Power）**。；默认值：`31` |
| `wifi-max-tx-pwr-join` | `int` | 加入Wi-Fi网络时使用的最大发射功率（Maximum TX Power），单位dBm；实际输出可能受法规或硬件约束限制。注意：SiWx91x固件**不支持按速率分别设置功率（Per-Rate Power）**。；默认值：`31` |

本页没有已弃用的节点专用属性。

---

[上一章](P011_realtek_ameba-wifi.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P013_st_st67w611m1.md)
