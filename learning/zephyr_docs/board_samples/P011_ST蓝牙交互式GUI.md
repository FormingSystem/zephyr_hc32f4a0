---
id: learning.zephyr-docs.board-samples.page-11
title: ST蓝牙交互式GUI
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/st/bluetooth/interactive_gui/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="st_bluetooth_interactive_gui"></a>

<a id="samples-boards-stm32-bluetooth-interactive-gui"></a>

# 第11章\_蓝牙：ST 交互式图形界面（Bluetooth: ST Interactive GUI）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/st/bluetooth/interactive_gui/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/bluetooth/interactive_gui/README.rst/..)

<a id="overview"></a>

## 11.1 概述（Overview）

本例通过 UART 向 PC 提供蓝牙网络协处理器接口，供 ST BlueNRG 图形界面应用（GUI）使用。此时主 MCU 充当中间转发层，在主机 PC 与控制器之间传递数据。

> 译注——主机与控制器：此例将 PC 作为蓝牙主机操作端，板上 MCU 转发 HCI 及 ST 扩展数据；它与在 MCU 内运行普通 GATT 外设应用不同。示例配置启用 `CONFIG_BT_HCI_RAW` 并关闭常规串口控制台，因此不要将该传输 UART 当成普通文本 Shell 终端。

<a id="requirements"></a>

## 11.2 前提条件（Requirements）

- 一块基于 BlueNRG BLE 模块的开发板，例如 [Disco L475 IOT01（B-L475E-IOT01A）](https://docs.zephyrproject.org/latest/boards/st/disco_l475_iot1/doc/index.html#disco_l475_iot1)。

- PC 上安装 [BlueNRG GUI](https://www.st.com/en/embedded-software/stsw-bnrgui.html) 应用。

<a id="default-uart-settings"></a>

## 11.3 默认 UART 设置（Default UART settings）

设置取决于板级 DTS 属性 `zephyr,bt-c2h-uart` 的默认配置。UART 默认参数如下：

> 译注——UART 来源：`zephyr,bt-c2h-uart` 是设备树 chosen 中指向 UART 节点的选择项，源码通过 `DT_CHOSEN(zephyr_bt_c2h_uart)` 取得设备。115200、8N1 是原文默认值，应同时核对板级 UART、引脚和 PC GUI 端配置，不能按别的板的串口号照搬。

- 波特率：115200 bps。

- 8 个数据位、无奇偶校验、1 个停止位。

<a id="building-and-running"></a>

## 11.4 构建与运行（Building and Running）

> 译注——官方原页内容：此节在本次网页与 RST 快照中只有标题，没有给出具体构建命令。原样保留空节，不将推导出的命令冒充官方正文。实际构建可按[应用开发指南](../application/P001_应用开发.md)与所用板文档，使用官方应用目录 `samples/boards/st/bluetooth/interactive_gui`，先核对 BlueNRG 控制器与 HCI UART 条件；本次没有构建或验证 GUI 通信。

<a id="see-also"></a>

## 11.5 另请参阅（See also）

[BlueNRG HCI 驱动扩展 API（BlueNRG HCI driver extended API）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluenrg__hci__driver.html)

[蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)

> 译注——源码入口：本仓库[samples/boards/st/bluetooth/interactive_gui/src/main.c](../../../samples/boards/st/bluetooth/interactive_gui/src/main.c)与[samples/boards/st/bluetooth/interactive_gui/prj.conf](../../../samples/boards/st/bluetooth/interactive_gui/prj.conf)使用相对路径，可随仓库移动。本地源码版本可能与官方快照不同。

对应官方文档源码：[samples/boards/st/bluetooth/interactive_gui/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/st/bluetooth/interactive_gui/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/st/bluetooth/interactive_gui/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P010_STM32示例目录.md) · [返回大纲](大纲.md) · [下一章](P012_ST蓝牙低功耗传感器演示.md)
