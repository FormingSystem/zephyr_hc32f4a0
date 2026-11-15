---
id: learning.zephyr-docs.intercore_reference.ipcremainder-189
title: 蓝牙HCI的IPC示例
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/hci_ipc/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="bluetooth_hci_ipc"></a>

# 第189章\_蓝牙HCI的IPC示例

原文：[HCI IPC](https://docs.zephyrproject.org/latest/samples/bluetooth/hci_ipc/README.html)。读取日期：2026-10-13，`latest`。

本示例通过处理器间通信（Inter-Processor Communication，IPC）子系统，将[蓝牙控制器（Bluetooth Controller）](../bluetooth/P020_蓝牙控制器接口.md#bluetooth-controller)能力提供给另一设备或中央处理器（Central Processing Unit，CPU）。HCI 指主机控制器接口（Host Controller Interface）。

[浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/bluetooth/hci_ipc)。

## 189.1\_要求

需要一块同时支持 IPC 子系统和低功耗蓝牙（Bluetooth Low Energy，Bluetooth LE）的开发板。

## 189.2\_构建与运行

在已配置 Zephyr 构建环境的 Bash 终端，从 Zephyr 源码根目录执行下面的官方命令。用目标板替换`<board>`，例如 [nRF5340 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf5340dk/doc/index.html#nrf5340dk) 的`nrf5340dk/nrf5340/cpunet`目标。示例目录为官方源码已有目录，构建输出由`west build`生成。

```bash
west build -b <board> samples/bluetooth/hci_ipc
west flash
```

测试需要另一个设备或 CPU，作为蓝牙 HCI IPC 对端（Peer）。本示例与 Zephyr 蓝牙核心提供的 [HCI 驱动（HCI Drivers）](../bluetooth/P013_HCI驱动.md#bt-hci-drivers)兼容，详见 [`CONFIG_BT_HCI_IPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_IPC)。

可能需要调整 Kconfig 构建配置（Build Configuration），使本示例与对端应用兼容。例如，[`CONFIG_BT_MAX_CONN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MAX_CONN)**必须等于对端应用支持的最大连接数**。构建或通信不符合预期时，先核对目标板和双方配置。

蓝牙示例的一般信息见[蓝牙示例目录](https://docs.zephyrproject.org/latest/samples/bluetooth/bluetooth.html#bluetooth)。

## 189.3\_另见

- [HCI 原始通道（HCI RAW Channel）](https://docs.zephyrproject.org/latest/doxygen/html/group__hci__raw.html)。
- [蓝牙应用程序编程接口（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)。

---

[上一章：蓝牙HCI的IPC设备树绑定](P188_蓝牙HCI的IPC设备树绑定.md) · [下一章：IEEE802154的RPMsg示例](P190_IEEE802154的RPMsg示例.md) · [返回大纲](大纲.md)
