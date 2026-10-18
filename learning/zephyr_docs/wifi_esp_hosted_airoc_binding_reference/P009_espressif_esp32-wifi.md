---
id: learning.zephyr-docs.wifi-esp-hosted-airoc-binding-reference.page-9
title: espressif_esp32-wifi
kind: reference
status: maintained
domains: [zephyr, devicetree, wifi]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/wifi/espressif,esp32-wifi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第9章\_espressif_esp32-wifi

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/wifi/espressif,esp32-wifi.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="espressif-esp32-wifi"></a>
<a id="dtbinding-espressif-esp32-wifi"></a>
<a id="std-dtcompatible-espressif-esp32-wifi"></a>

兼容字符串（Compatible String）：`espressif,esp32-wifi`。厂商：[ Espressif Systems ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-espressif)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=espressif,esp32-wifi)。

驱动源码（Driver Source）：[drivers/wifi/esp32/src/esp_wifi_drv.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/wifi/esp32/src/esp_wifi_drv.c)。

<a id="description"></a>

ESP32 SoC的Wi-Fi设备。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 9.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

---

[上一章](P008_espressif_esp-hosted.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_infineon_airoc-wifi-spi.md)
