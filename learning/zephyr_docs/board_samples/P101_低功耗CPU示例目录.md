---
id: learning.zephyr-docs.board-samples.page-101
title: 低功耗CPU示例目录
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/espressif/ulp/lp_core/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="low-power-cpu-lp-core"></a>

# 第101章\_低功耗 CPU（Low-Power CPU，LP CORE）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/espressif/ulp/lp_core/index.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

这些示例演示 Espressif SoC 中低功耗核（LP Core）的用法。

> 译注——两个处理器：这里 HP 指高性能核（High-Performance Core），LP 指低功耗核（Low-Power Core）。本组五个正文示例的构建命令均选择 ESP32-C6 DevKitC 的 hpcore，由 Sysbuild 追加 lpcore 子应用；不是把一份 ELF 同时烧到两个核。

- [低功耗核调试（Debug ULP）](P102_低功耗核调试.md#debug-ulp)：调试 ESP32-C6 的低功耗核。

- [低功耗核串口回显（Echo ULP）](P103_低功耗核串口回显.md#echo-ulp)：通过 Zephyr UART API 使用 ESP32-C6 低功耗核上的低功耗串口。

- [主核中断低功耗核（Interrupt ULP）](P105_主核中断低功耗核.md#interrupt-ulp)：高性能核向低功耗核发出中断。

- [低功耗核 GPIO 唤醒（LP GPIO Wakeup）](P104_低功耗核GPIO唤醒.md#lp-gpio-wakeup)：低功耗 GPIO 电平变化时，由低功耗核把高性能核从深度睡眠中唤醒。

- [低功耗核定时器唤醒（LP Timer Wakeup）](P106_低功耗核定时器唤醒.md#lp-timer-wakeup)：低功耗核使用低功耗定时器，周期性地把高性能核从深度睡眠中唤醒。

对应官方文档源码：[samples/boards/espressif/ulp/lp_core/index.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/espressif/ulp/lp_core/index.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/espressif/ulp/lp_core/index.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、调试或执行硬件实验。

[上一章](P100_ULP协处理器示例目录.md) · [返回大纲](大纲.md) · [下一章](P102_低功耗核调试.md)
