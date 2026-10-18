---
id: learning.zephyr-docs.usb.page-190
title: 蓝牙HCIUSB控制器示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/hci_usb/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第190章\_蓝牙HCIUSB控制器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/hci_usb/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 190.1\_概览（Overview）

本示例使用 Zephyr 将开发板变成 USB 蓝牙适配器（Bluetooth Dongle）。运行示例的板必须支持 USB 设备功能；例如 [nRF52840 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dk/doc/index.html#nrf52840dk) 同时支持低功耗蓝牙（Bluetooth Low Energy，Bluetooth LE）和 USB。

译注：这里的主机控制器接口（Host Controller Interface，HCI）连接主机上的蓝牙协议栈与设备上的蓝牙控制器。官方 `prj.conf` 启用 `CONFIG_BT_HCI_RAW`、`CONFIG_USB_DEVICE_STACK_NEXT` 和 `CONFIG_USBD_BT_HCI`；这不是仅凭 USB 接口就能为任意微控制器增加无线功能的示例。

## 190.2\_要求（Requirements）

- 主机上运行蓝牙协议栈，例如 BlueZ。
- 使用在 Zephyr 中同时支持蓝牙和 USB 的开发板。

## 190.3\_构建与运行（Building and Running）

按以下方式构建并烧录示例，把 `<board>` 替换为目标板，例如 [nRF52840 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dk/doc/index.html#nrf52840dk)：

```bash
west build -b <board> samples/bluetooth/hci_usb
west flash
```

译注（源码核对）：命令在已准备好模块与工具链的 Zephyr 源码根目录执行。当前官方 `tests.yaml` 的集成平台为 `nrf52840dk/nrf52840`；烧录前须确认所选板及烧录器可用，构建失败时先处理错误。示例通过 `sample_usbd_init_device()` 初始化新版 USB 设备栈，再调用 `usbd_enable()`；`prj.conf` 关闭串口与控制台，因此不能把未看到串口打印当作唯一失败依据。本页没有提供一份实测的枚举日志，也没有声称已在其他板上验证。

## 190.4\_另请参阅（See Also）

- [HCI 原始通道（HCI RAW Channel）](https://docs.zephyrproject.org/latest/doxygen/html/group__hci__raw.html)。
- [蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)。
- [USB 设备核心 API（USB Device Core API）](P015_USB设备核心API.md)。



译注核对来源：[samples/bluetooth/hci_usb/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/hci_usb/src/main.c)、[samples/bluetooth/hci_usb/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/hci_usb/prj.conf)、[samples/bluetooth/hci_usb/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/hci_usb/tests.yaml)。

本仓库的[对应源码](../../../samples/bluetooth/hci_usb/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="bluetooth_hci_usb"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="see-also"></a>

[上一章](P189_旧版DFU运行时描述符.md) · [返回大纲](大纲.md) · [下一章](P191_MCTPUSB端点示例.md)
