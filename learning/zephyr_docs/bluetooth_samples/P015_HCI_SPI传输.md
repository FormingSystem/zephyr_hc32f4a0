---
id: learning.zephyr-docs.bluetooth-samples.page-15
title: HCI_SPI传输
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/hci_spi/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth_hci_spi"></a>

# 第15章\_HCI\_SPI传输

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/hci_spi/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

[浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/bluetooth/hci_spi)。

> 译注——命令前提：以下构建命令从读者自己的Zephyr源码根目录执行，终端采用该工作区已配置的Shell；需先具备相应工具链、模块和目标板支持。烧录还需要对应开发板及烧录工具。占位符按实际目标替换，原文指定的型号属于该分支示例。BlueZ或外部控制器的环境说明见[官方工具译文](../bluetooth/P008_蓝牙开发工具.md)。本批未执行构建、烧录或无线测试。

<a id="overview"></a>

## 15.1\_概览（Overview）

本示例通过串行外设接口（Serial Peripheral Interface，SPI），向另一台设备或另一个处理器提供蓝牙控制器（Bluetooth Controller）功能。传输采用Zephyr的SPI主机控制器接口（Host Controller Interface，HCI）协议，与BlueNRG的方式相似。

<a id="requirements"></a>

## 15.2\_要求（Requirements）

开发板需要具备SPI外设、通用输入输出（General-Purpose Input/Output，GPIO）及低功耗蓝牙（Bluetooth Low Energy，LE）支持。

<a id="building-and-running"></a>

## 15.3\_构建与运行（Building and Running）

确保[设备树（Devicetree）](../devicetree/P013_设备树文档入口.md#dt-guide)中为HCI SPI外设定义了节点，兼容标识（Compatible）为 [zephyr,bt-hci-spi-peripheral](../bluetooth_st_transport_binding_reference/P010_zephyr_bt-hci-spi-peripheral.md#std-dtcompatible-zephyr-bt-hci-spi-peripheral)。该节点设置通向主机的中断线，并指定应用使用的SPI总线。

示例目录中的 [boards/nrf51dk_nrf51822.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_spi/boards/nrf51dk_nrf51822.overlay) 是 [nRF51 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf51dk/doc/index.html#nrf51dk) 的设备树覆盖文件（Overlay）示例。

按下面方式构建并烧录，将 `<board>` 换成目标板。例如，[nRF51 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf51dk/doc/index.html#nrf51dk) 使用 `nrf51dk/nrf51822` 目标。

```bash
west build -b <board> samples/bluetooth/hci_spi
west flash
```

还需要另一颗芯片充当蓝牙HCI SPI控制端（SPI Controller）。本应用兼容Zephyr蓝牙HCI驱动核心提供的HCI SPI控制端驱动；详情见 [`CONFIG_BT_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SPI) 的帮助。

> 译注——两种“控制器”：此处承载蓝牙Controller的芯片在SPI总线上作为Peripheral，对端Host通过SPI Controller访问它。蓝牙协议栈角色与SPI总线角色分别命名，不能仅凭“控制器”一词把两者当成同一端。

通用说明见[蓝牙示例总览](https://docs.zephyrproject.org/latest/samples/bluetooth/bluetooth.html#bluetooth)；96Boards Carbon的具体说明见[为96b_carbon提供蓝牙功能](https://docs.zephyrproject.org/latest/boards/96boards/carbon/doc/nrf51822.html#b-carbon-nrf51-bluetooth)。

<a id="see-also"></a>

## 15.4\_另请参阅（See also）

[HCI原始通道（RAW Channel）](https://docs.zephyrproject.org/latest/doxygen/html/group__hci__raw.html)、[蓝牙API](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)、[SPI接口](../hardware/P318_SPI公共接口.md)。


对应官方文档源码：[samples/bluetooth/hci_spi/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/hci_spi/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/bluetooth/hci_spi/README.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。


[上一章](P014_外设接受列表.md) · [返回大纲](大纲.md) · [下一章](P016_HCI_UART传输.md)
