---
id: learning.zephyr-docs.board-samples.page-9
title: STM32的UART示例目录
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/st/uart/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="uart"></a>

# 第9章\_UART

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/st/uart/index.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

这些示例演示 STM32 开发板上 UART 的用法。

> 译注——目录范围：这里的单线／半双工与循环 DMA 是不同使用场景，两篇正文已分别译出；读者按接线方式、接收模式和目标板支持选择。

- [单线 UART（Single-wire UART）](P007_STM32单线UART.md#uart-stm32-single-wire)：使用 STM32 设备的单线／半双工 UART 功能。

- [UART 循环模式（UART circular mode）](P006_STM32的UART循环DMA.md#uart-circular-dma)：使用循环 DMA 配置读取控制台数据并回显。

对应官方文档源码：[samples/boards/st/uart/index.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/st/uart/index.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/st/uart/index.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P008_STM32的PWM示例目录.md) · [返回大纲](大纲.md) · [下一章](P010_STM32示例目录.md)
