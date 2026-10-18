---
id: learning.zephyr-docs.board-samples.page-44
title: ADI示例目录
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/adi/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="adi"></a>

# 第44章\_ADI

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/adi/index.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

这些示例展示如何在 Zephyr 中使用 ADI 开发板。

> 译注——目录范围：GPIO 唤醒示例以按钮逐项触发并可长按关机，Power Modes 示例则按计时循环尝试各状态。两种观察方法不同，分别按正文准备唤醒源、计数器和设备树。

- [ADI MAX32 的 GPIO 唤醒（ADI MAX32 GPIO Wakeup）](P042_ADI_MAX32的GPIO唤醒.md#adi-gpio-wakeup)：使用 GPIO 将系统从低功耗状态唤醒。

- [ADI 电源模式（ADI Power Modes）](P043_ADI电源模式.md#adi-pm)：运行指定 SoC 的各种电源模式。

对应官方文档源码：[samples/boards/adi/index.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/adi/index.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/adi/index.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P043_ADI电源模式.md) · [返回大纲](大纲.md) · [下一章](P045_Renesas事件链接控制器.md)
