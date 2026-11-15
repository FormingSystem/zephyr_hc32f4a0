---
id: learning.zephyr-docs.bluetooth-samples.page-12
title: 中心设备GATT写入
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/central_gatt_write/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="ble_central_gatt_write"></a>

# 第12章\_中心设备GATT写入

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/central_gatt_write/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

[浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/bluetooth/central_gatt_write)。

> 译注——命令前提：以下构建命令从读者自己的Zephyr源码根目录执行，终端采用该工作区已配置的Shell；需先具备相应工具链、模块和目标板支持。烧录还需要对应开发板及烧录工具。占位符按实际目标替换，原文指定的型号属于该分支示例。BlueZ或外部控制器的环境说明见[官方工具译文](../bluetooth/P008_蓝牙开发工具.md)。本批未执行构建、烧录或无线测试。

<a id="overview"></a>

## 12.1\_概览（Overview）

本应用类似[中心设备示例](P006_基础蓝牙中心设备.md#ble_central)，区别是使用通用属性配置文件的无需响应写入（GATT Write Without Response）。GATT全称Generic Attribute Profile。

<a id="requirements"></a>

## 12.2\_要求（Requirements）

主机上运行BlueZ，或使用支持低功耗蓝牙（Bluetooth Low Energy，LE）的开发板。

<a id="building-and-running"></a>

## 12.3\_构建与运行（Building and Running）

构建和烧录如下，将 `<board>` 替换为目标开发板。

```bash
west build -b <board> samples/bluetooth/central_gatt_write
west flash
```

烧录后，示例扫描附近LE设备，连接找到的第一个设备，并持续发送无需响应的GATT写入命令。在第二块板上运行[外设GATT写入示例](P013_外设GATT写入.md#ble_peripheral_gatt_write)作为对端。

<a id="see-also"></a>

## 12.4\_另请参阅（See also）

[蓝牙API](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)。


对应官方文档源码：[samples/bluetooth/central_gatt_write/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/central_gatt_write/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/bluetooth/central_gatt_write/README.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。


[上一章](P011_MTU更新.md) · [返回大纲](大纲.md) · [下一章](P013_外设GATT写入.md)
