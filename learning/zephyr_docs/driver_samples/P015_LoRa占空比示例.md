---
id: learning.zephyr-docs.driver_samples.page-15
title: LoRa占空比示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/lora/duty_cycle/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lora-duty-cycle"></a>

# 第15章\_LoRa占空比示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/lora/duty_cycle/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 15.1\_概览（Overview）

本例演示阻塞式（Blocking） `lora_recv_duty_cycle()` 和基于回调（Callback-based）的 `lora_recv_duty_cycle_async()`：无线电自主地在短接收窗口（RX Window）与休眠之间切换，仅在收到分组时唤醒微控制器（Microcontroller Unit，MCU）。

接收端先通过阻塞API接收4个分组，然后切换到异步API，再接收10个分组。

需要两块开发板，默认启动为接收端。在启动期间按住按钮0可选择发送端模式。发送端使用100个符号（Symbol）的长前导码（Preamble），让周期性开启接收窗口的接收端能够在某个窗口中检测到它。

> 译注——两端配置：所读[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/lora/duty_cycle/src/main.c)要求两块板均运行本示例，按钮来自sw0别名；没有该按钮配置时不能靠按键选择发送角色。源码将收发两端前导码长度都设为100，接收窗口50毫秒、休眠450毫秒。检测到前导码后还需等待同步字，不能把接收端前导码长度随意改短。原文的检测保证针对示例配置，不表示任意时序或信号条件下都能接收。

<a id="building-and-running"></a>

## 15.2\_构建与运行（Building and Running）

在两块具有 `lora0` 别名的开发板上构建并烧录，例如nucleo_wl55jc，或带SX1261扩展板（Shield）的nrf52840dk/nrf52840。

```bash
west build -b nucleo_wl55jc samples/drivers/lora/duty_cycle
west flash
```

> 译注——操作位置：命令从Zephyr源码根在已就绪的west与工具链环境中执行。上面只给出nucleo_wl55jc分支；选择另一块板时仍需按对应扩展板说明配置硬件与Shield，不能只改变板名就认为无线电已连接。接收占空比描述的是接收窗口与休眠，不应与发送时间占比混为一谈。本批未构建、烧录或发射无线信号。

<a id="sample-output-receiver"></a>

### 15.2.1\_接收端示例输出（Sample Output (receiver)）

```text
[00:00:00.235,000] <inf> lora_duty_cycle: Synchronous duty cycle reception (rx=50 ms, sleep=450 ms)
[00:00:01.456,000] <inf> lora_duty_cycle: RX 12 bytes, RSSI: -55 dBm, SNR: 9 dB
[00:00:01.456,000] <inf> lora_duty_cycle: payload
                                          64 75 74 79 63 79 63 6c  65 20 20 30  |dutycycle  0
...
[00:00:20.000,000] <inf> lora_duty_cycle: Asynchronous duty cycle reception
[00:00:25.000,000] <inf> lora_duty_cycle: RX 12 bytes, RSSI: -55 dBm, SNR: 9 dB
[00:00:25.000,000] <inf> lora_duty_cycle: payload
                                          64 75 74 79 63 79 63 6c  65 20 20 34  |dutycycle  4
```

> 译注——日志阅读：先显示同步接收窗口50毫秒、休眠450毫秒，之后进入异步接收。RX表示接收到的字节数；RSSI为接收信号强度指示（Received Signal Strength Indicator），单位dBm；SNR为信噪比（Signal-to-Noise Ratio），单位dB；payload为载荷。省略号、时间戳及十六进制数据均保留自原文。

<a id="sample-output-sender"></a>

### 15.2.2\_发送端示例输出（Sample Output (sender)）

```text
[00:00:00.235,000] <inf> lora_duty_cycle: Sender mode (preamble=100 symbols)
[00:00:00.235,000] <inf> lora_duty_cycle: Expected packet airtime: 1565 ms
[00:00:01.800,000] <inf> lora_duty_cycle: Sent packet 0
```

> 译注——预期空中时间：原日志的1565毫秒是分组空中时间（Airtime）示例；它不是接收窗口长度或当前板上的测量结果。观察不到接收时，先确认两端角色、频率、调制配置、前导码和接收窗口一致，再检查实际无线链路。

<a id="see-also"></a>

## 15.3\_相关接口（See also）

[LoRa接口参考](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html)。


对应官方文档源码：[samples/drivers/lora/duty_cycle/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/lora/duty_cycle/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/lora/duty_cycle/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/lora/duty_cycle/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P014_LoRa示例目录.md) · [返回大纲](大纲.md) · [下一章](P016_LoRa接收示例.md)
