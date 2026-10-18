---
id: learning.zephyr-docs.usb.page-136
title: 旧版USB网络设备示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/netusb/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第136章\_旧版USB网络设备示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/netusb/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 136.1\_概述

使用 USB 通信设备类（Communication Device Class，CDC）的以太网仿真模型（Ethernet Emulation Model，EEM）、以太网控制模型（Ethernet Control Model，ECM），或远程网络驱动接口规范（Remote Network Driver Interface Specification，RNDIS）实现，与运行 Zephyr RTOS 的设备建立网络连接。

> 原文注：此示例演示已弃用的 [USB 设备支持](P008_旧版USB设备支持.md#usb-device-stack)。

## 136.2\_运行要求

此项目需要 USB 设备驱动；Zephyr 支持的多种开发板具有这类驱动。

## 136.3\_构建与运行

```shell
west build -b reel_board samples/subsys/usb/legacy/netusb
west flash
```

> 译注：命令在已准备依赖与工具链的 Zephyr 源码根目录执行，构建成功后再烧录官方 `reel_board`。网页列出 EEM、ECM 与 RNDIS 三种实现，但当前 `prj.conf` 默认启用 `CONFIG_USB_DEVICE_NETWORK_ECM`；这不表示三种协议同时启用。示例先调用 `usb_enable(NULL)`，再调用 `net_config_init_app()`；当前配置给出 IPv4 `192.0.2.1` 和 IPv6 `2001:db8::1`。这些是示例网络配置，USB 枚举本身不等于主机网络已配置或网络服务已可达。原页未给出主机端地址配置和连通性测试命令。

## 136.4\_另见

- [网络配置库（Network Configuration Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html)。
- [USB 设备核心 API](P155_旧版USB设备栈核心API.md)。


译注核对来源：[samples/subsys/usb/legacy/netusb/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/netusb/src/main.c)、[samples/subsys/usb/legacy/netusb/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/netusb/prj.conf)。

本仓库的[对应源码](../../../samples/subsys/usb/legacy/netusb/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="legacy-netusb"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="see-also"></a>

[上一章](P135_旧版USB大容量存储示例.md) · [返回大纲](大纲.md) · [下一章](P137_旧版USB蓝牙控制器示例.md)
