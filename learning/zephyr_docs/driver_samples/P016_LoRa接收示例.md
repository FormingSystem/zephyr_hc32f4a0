---
id: learning.zephyr-docs.driver_samples.page-16
title: LoRa接收示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/lora/receive/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lora-receive"></a>

# 第16章\_LoRa接收示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/lora/receive/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 16.1\_概览（Overview）

本例演示使用LoRa无线电驱动，以同步（Synchronous）和异步（Asynchronous）方式接收分组（Packet）。

要接收消息，需要在通信范围内的另一块板上构建并烧录配套[LoRa发送示例](P017_LoRa发送示例.md#lora-send)。

本例接收有限数量的分组后会无限期休眠，因此设备复位后应立即查看控制台输出。

<a id="building-and-running"></a>

## 16.2\_构建与运行（Building and Running）

按下列方式构建和烧录；将b_l072z_lrwan1替换为实际开发板，该板的设备树必须提供 `lora0` 别名。

```bash
west build -b b_l072z_lrwan1 samples/drivers/lora/receive
west flash
```

> 译注——操作与接收条件：从Zephyr源码根执行，先准备工具链、模块、支持的无线电和设备树配置。发送板与接收板需要一致的频率及调制参数。只完成构建不代表无线通信成功；先接通控制台，再复位接收板，以免错过有限次数的接收输出。

<a id="sample-output"></a>

### 16.2.1\_示例输出（Sample Output）

```text
[00:00:00.235,000] <inf> lora_receive: Synchronous reception
[00:00:00.956,000] <inf> lora_receive: LoRa RX RSSI: -60dBm, SNR: 7dB
[00:00:00.956,000] <inf> lora_receive: LoRa RX payload
                                       68 65 6c 6c 6f 77 6f 72  6c 64 20 30             |hellowor ld 0
[00:00:02.249,000] <inf> lora_receive: LoRa RX RSSI: -57dBm, SNR: 9dB
[00:00:02.249,000] <inf> lora_receive: LoRa RX payload
                                       68 65 6c 6c 6f 77 6f 72  6c 64 20 31             |hellowor ld 1
[00:00:03.541,000] <inf> lora_receive: LoRa RX RSSI: -57dBm, SNR: 9dB
[00:00:03.541,000] <inf> lora_receive: LoRa RX payload
                                       68 65 6c 6c 6f 77 6f 72  6c 64 20 32             |hellowor ld 2
[00:00:04.834,000] <inf> lora_receive: LoRa RX RSSI: -55dBm, SNR: 9dB
[00:00:04.834,000] <inf> lora_receive: LoRa RX payload
                                       68 65 6c 6c 6f 77 6f 72  6c 64 20 33             |hellowor ld 3
[00:00:04.834,000] <inf> lora_receive: Asynchronous reception
[00:00:06.127,000] <inf> lora_receive: LoRa RX RSSI: -55dBm, SNR: 9dB
[00:00:06.127,000] <inf> lora_receive: LoRa RX payload
                                       68 65 6c 6c 6f 77 6f 72  6c 64 20 34             |hellowor ld 4
[00:00:07.419,000] <inf> lora_receive: LoRa RX RSSI: -55dBm, SNR: 9dB
[00:00:07.419,000] <inf> lora_receive: LoRa RX payload
                                       68 65 6c 6c 6f 77 6f 72  6c 64 20 35             |hellowor ld 5
[00:00:08.712,000] <inf> lora_receive: LoRa RX RSSI: -55dBm, SNR: 9dB
[00:00:08.712,000] <inf> lora_receive: LoRa RX payload
                                       68 65 6c 6c 6f 77 6f 72  6c 64 20 36             |hellowor ld 6
[00:00:10.004,000] <inf> lora_receive: LoRa RX RSSI: -55dBm, SNR: 9dB
[00:00:10.004,000] <inf> lora_receive: LoRa RX payload
                                       68 65 6c 6c 6f 77 6f 72  6c 64 20 37             |hellowor ld 7
[00:00:11.297,000] <inf> lora_receive: LoRa RX RSSI: -55dBm, SNR: 9dB
[00:00:11.297,000] <inf> lora_receive: LoRa RX payload
                                       68 65 6c 6c 6f 77 6f 72  6c 64 20 38             |hellowor ld 8
[00:00:12.590,000] <inf> lora_receive: LoRa RX RSSI: -55dBm, SNR: 9dB
[00:00:12.590,000] <inf> lora_receive: LoRa RX payload
                                       68 65 6c 6c 6f 77 6f 72  6c 64 20 39             |hellowor ld 9
[00:00:13.884,000] <inf> lora_receive: LoRa RX RSSI: -55dBm, SNR: 9dB
[00:00:13.884,000] <inf> lora_receive: LoRa RX payload
                                       68 65 6c 6c 6f 77 6f 72  6c 64 20 30             |hellowor ld 0
[00:00:15.177,000] <inf> lora_receive: LoRa RX RSSI: -55dBm, SNR: 9dB
[00:00:15.177,000] <inf> lora_receive: LoRa RX payload
                                       68 65 6c 6c 6f 77 6f 72  6c 64 20 31             |hellowor ld 1
[00:00:16.470,000] <inf> lora_receive: LoRa RX RSSI: -55dBm, SNR: 9dB
[00:00:16.470,000] <inf> lora_receive: LoRa RX payload
                                       68 65 6c 6c 6f 77 6f 72  6c 64 20 32             |hellowor ld 2
[00:00:17.762,000] <inf> lora_receive: LoRa RX RSSI: -55dBm, SNR: 9dB
[00:00:17.762,000] <inf> lora_receive: LoRa RX payload
                                       68 65 6c 6c 6f 77 6f 72  6c 64 20 33             |hellowor ld 3
[00:00:17.762,000] <inf> lora_receive: Stopping packet receptions
```

> 译注——日志顺序：原例先打印4次同步接收，再打印10次异步接收，最后Stopping packet receptions表示停止接收。RSSI是接收信号强度指示（Received Signal Strength Indicator），SNR是信噪比（Signal-to-Noise Ratio）；十六进制与右侧字符展示收到的载荷。停止后没有新输出是该示例的预期终止行为，不能只据此判定无线电故障。所有数值和时间戳属于官方原日志，本批未实测。

<a id="see-also"></a>

## 16.3\_相关接口（See also）

[LoRa接口参考](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html)。


对应官方文档源码：[samples/drivers/lora/receive/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/lora/receive/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/lora/receive/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/lora/receive/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P015_LoRa占空比示例.md) · [返回大纲](大纲.md) · [下一章](P017_LoRa发送示例.md)
