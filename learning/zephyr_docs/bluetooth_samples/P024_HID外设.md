---
id: learning.zephyr-docs.bluetooth-samples.page-24
title: HID外设
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/peripheral_hids/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="ble_peripheral_hids"></a>

# 第24章\_HID外设

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/peripheral_hids/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

[浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/bluetooth/peripheral_hids)。

> 译注——命令前提：以下构建命令从读者自己的Zephyr源码根目录执行，终端采用该工作区已配置的Shell；需先具备相应工具链、模块和目标板支持。烧录还需要对应开发板及烧录工具。占位符按实际目标替换，原文指定的型号属于该分支示例。BlueZ或外部控制器的环境说明见[官方工具译文](../bluetooth/P008_蓝牙开发工具.md)。本批未执行构建、烧录或无线测试。

<a id="overview"></a>

## 24.1\_概览（Overview）

本应用类似[基础外设示例](P005_基础蓝牙外设.md#ble_peripheral)，但专门提供人机接口设备（Human Interface Device，HID）的通用属性配置文件（Generic Attribute Profile，GATT）服务。所用报告映射（Report Map）描述一个通用鼠标。

默认配置使用口令认证（Passkey Authentication）：外设显示一个代码，配对时必须在主机输入。访问GATT特征（Characteristic）要求链路已经过认证。若要禁用认证而只使用加密信道，可用 `CONFIG_SAMPLE_BT_USE_AUTHENTICATION=n` 构建示例。

> 译注——认证与加密：这个配置取消的是上述认证要求，原文仍要求加密信道；不能把它解释为完全不加密的连接。

<a id="requirements"></a>

## 24.2\_要求（Requirements）

主机运行BlueZ，或者使用支持低功耗蓝牙（Bluetooth Low Energy，LE）的开发板。

<a id="building-and-running"></a>

## 24.3\_构建与运行（Building and Running）

将 `<board>` 替换为目标板，构建并烧录：

```bash
west build -b <board> samples/bluetooth/peripheral_hids
west flash
```

烧录后，设备以HID外设身份广播。将它与主机配对：口令显示在外设控制台上，必须在主机输入。配对完成后，操作系统应将设备识别为通用鼠标。

<a id="see-also"></a>

## 24.4\_另请参阅（See also）

[通用属性配置文件（GATT）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html)、[蓝牙API](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)。


对应官方文档源码：[samples/bluetooth/peripheral_hids/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/peripheral_hids/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/bluetooth/peripheral_hids/README.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。


[上一章](P023_仅安全连接外设.md) · [返回大纲](大纲.md) · [下一章](P025_设备信息服务外设.md)
