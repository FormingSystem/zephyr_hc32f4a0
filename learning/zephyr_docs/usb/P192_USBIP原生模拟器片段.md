---
id: learning.zephyr-docs.usb.page-192
title: USBIP原生模拟器片段
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/snippets/usbip-native-sim/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第192章\_USBIP原生模拟器片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/usbip-native-sim/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 192.1\_使用方式

USB/IP 原生模拟器配置片段（USB/IP on Native Simulator Snippet）的名称为 `usbip-native-sim`。原文调用形式：

```bash
west build -S usbip-native-sim [...]
```

译注：`[...]` 表示需要补充的构建参数，不是可以原样执行的参数；使用已有 Zephyr 源码、原生模拟器构建环境和适用的应用，在源码根目录构建。片段（Snippet）用于向应用追加配置，不能独立替代完整应用与目标板选择。

## 192.2\_概览（Overview）

此片段在原生模拟器（Native Simulator）上启用 USB/IP 支持。使用它构建时，需要通过 `EXTRA_DTC_OVERLAY_FILE` 参数提供设备树覆盖文件（Devicetree Overlay）。

此片段属于实验性功能（Experimental），行为可能在不另行通知的情况下改变。

译注（源码核对）：当前 `snippet.yml` 已自动向 `EXTRA_CONF_FILE` 追加 `usbip-native-sim.conf`，并向 `EXTRA_DTC_OVERLAY_FILE` 追加 `usbip-native-sim.overlay`。因此应同时看原页要求和当前片段内容，不能误以为读者必须手工创建这份同名随附文件；应用需要额外覆盖时，再提供相应文件。

随附覆盖文件删除原来的 `zephyr_udc0` 节点，建立虚拟 USB 主机控制器（USB Host Controller，UHC），并在其下挂接虚拟 USB 设备控制器（USB Device Controller，UDC），设置 8 个双向端点和高速能力。配置文件启用 IPv4、TCP、套接字（Sockets）、USB 主机栈和 USB/IP，示例本端／对端地址分别为 `192.0.2.1` 与 `192.0.2.2`。

该片段提供的是主机栈、虚拟控制器及网络配置；USB/IP 连接和应用运行流程继续参阅[USB/IP 协议支持](P006_USBIP协议支持.md)。本页不把“选择片段并成功编译”等同于“远端主机已成功接入”。



译注核对来源：[snippets/usbip-native-sim/snippet.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/usbip-native-sim/snippet.yml)、[snippets/usbip-native-sim/usbip-native-sim.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/usbip-native-sim/usbip-native-sim.conf)、[snippets/usbip-native-sim/usbip-native-sim.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/usbip-native-sim/usbip-native-sim.overlay)。

本仓库的[对应源码](../../../snippets/usbip-native-sim/snippet.yml)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-ip-on-native-simulator-snippet-usbip-native-sim"></a>
<a id="snippet-usbip-native-sim"></a>
<a id="overview"></a>

[上一章](P191_MCTPUSB端点示例.md) · [返回大纲](大纲.md)
