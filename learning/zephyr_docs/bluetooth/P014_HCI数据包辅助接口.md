---
id: learning.zephyr-docs.bluetooth.page-14
title: HCI数据包辅助接口
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/hci_pkt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="hci-packet-helpers"></a>
<a id="bt-hci-pkt"></a>

# 第14章\_HCI数据包辅助接口

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/hci_pkt.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

主机控制器接口（Host Controller Interface，HCI）数据包辅助接口用于在 [`net_buf_simple`](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf__simple.html) 缓冲区和数据包字节中组织HCI命令帧、解析命令响应。它们独立于蓝牙主机（Host）和HCI驱动接口。

此外还提供逐命令同步交互辅助接口（Lockstep Helper）：当HCI驱动通过自身传输与控制器交换HCI命令时使用，例如执行厂商专用控制器初始化。

两类辅助接口都包含在启用 [`CONFIG_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT) 的构建中。Lockstep辅助接口的头文件与HCI驱动API放在一起，位于 `include/zephyr/drivers/bluetooth/`。

这些不是通用应用API，预期使用者是HCI驱动和蓝牙协议栈内部代码。应用若要在Host运行期间同时发送HCI命令，应使用较高层的 [`bt_hci_cmd_alloc()`](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a974e6e9262601e73537cbdcba7a7c93c)、[`bt_hci_cmd_send()`](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#af2eed9d93da45185aad9c2edc0001a54) 和 [`bt_hci_cmd_send_sync()`](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a8d306b5b56afdece1cadbbf0eecfe5a7)；这些接口与Host的命令流控配合。

<a id="api-reference"></a>

## 14.1\_API参考（API Reference）

- [蓝牙HCI数据包辅助接口（Bluetooth HCI packet helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html)。
- [蓝牙HCI逐命令同步辅助接口（Bluetooth HCI lockstep command helper）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html)。
- [蓝牙H:4 UART驱动厂商扩展接口（Bluetooth H:4 UART driver vendor extension interface）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__h4.html)。

> 译注——版本边界：官方当前驱动目录中的 `hci_lockstep.h` 和 `h4.h` 不在本仓库现有参照版本中，不能将同名旧接口当作本页实现。按上面的官方API与来源记录跟踪对应版本；本页未增加驱动或回移植接口。


对应官方文档源码：[doc/services/connectivity/bluetooth/api/hci_pkt.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/hci_pkt.rst)。

> 译注——源码版本：本仓库参照版本尚无该文档，请按上方官方来源跟踪相应版本；本批仅翻译和核对文档。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：HCI驱动](P013_HCI驱动.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：HCI原始通道](P015_HCI原始通道.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P013_HCI驱动.md) · [返回大纲](大纲.md) · [下一章](P015_HCI原始通道.md)

</details>

<!-- reading-navigation:end -->
