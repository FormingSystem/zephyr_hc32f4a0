---
id: learning.zephyr-docs.board-samples.page-30
title: nrfx外设驱动示例
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nordic/nrfx/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nrf_nrfx"></a>

# 第30章\_nrfx

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nordic/nrfx/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nordic/nrfx/README.rst/..)

<a id="overview"></a>

## 30.1 概述（Overview）

本示例展示如何在 Zephyr 中使用 nrfx 库，以 GPIOTE 和 DPPI/PPI 为 nrfx 驱动的示例。

> 译注——术语与路径：GPIOTE 是 GPIO 任务与事件模块（GPIO Tasks and Events）；PPI 是可编程外设互连（Programmable Peripheral Interconnect），DPPI 是分布式可编程外设互连（Distributed Programmable Peripheral Interconnect）。按钮事件通过硬件通路触发 LED 任务，CPU 中断回调主要用于观察该事件，两条路径不应混为由回调翻转 LED。

代码展示如何在 Zephyr 中初始化 GPIOTE 中断，使 nrfx_gpiote 驱动能够使用该中断。它还展示如何利用 DPPI/PPI 子系统连接 nRF 外设的任务（Task）与事件（Event），让外设在不需要 CPU 介入的情况下彼此交互。

示例禁用 Zephyr GPIO 驱动，避免该驱动为 GPIOTE 中断注册自己的处理程序。按钮 1 配置为按下时产生事件。该事件调用 `button_handler()` 回调，并触发 LED 1 引脚的 OUT 任务，随后 LED 翻转。

> 译注——资源归属：本次 prj.conf 设置 CONFIG_GPIO=n，并启用 nrfx 的 GPIOTE 与 GPPI 支持。直接使用 nrfx 时要保证同一中断和外设实例的唯一管理者，不能同时让 Zephyr GPIO 驱动与示例争用 GPIOTE。

注意，本示例没有对按钮进行去抖（Debouncing），因此按一次按钮可能产生多个事件。事件与任务之间的连接由硬件处理；如果事件到达得很快，甚至可能看不出 LED 曾经翻转。

<a id="requirements"></a>

## 30.2 前提条件（Requirements）

原示例已在 Nordic Semiconductor nRF9160 DK（nrf9160dk/nrf9160）与 nRF52840 DK（nrf52840dk/nrf52840）开发板上测试。

<a id="building-and-running"></a>

## 30.3 构建与运行（Building and Running）

> 译注——执行前提：除本页另有说明的目录外，west 命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先准备[入门指南](../getting_started/大纲.md)所需的主机工具、west 工作区、模块与目标工具链；应用、配置及 overlay 为官方源码，构建目录由工具生成。构建成功后再按目标板文档烧录，失败时返回构建输出或板文档检查；下方日志是官方预期示例，本次未执行硬件步骤。

代码位于 [samples/boards/nordic/nrfx](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/nordic/nrfx)。

构建并烧录应用：

```text
west build -b nrf9160dk/nrf9160 samples/boards/nordic/nrfx
west flash
```

按下按钮 1，翻转 LED 1。

连接串口，观察每次按下按钮时都会调用 `button_handler()` 函数。

关于 nrfx 的更多信息，请参阅 [nrfx_repository](https://github.com/NordicSemiconductor/nrfx)。

> 译注——实现入口：[samples/boards/nordic/nrfx/src/main.c](../../../samples/boards/nordic/nrfx/src/main.c)与[samples/boards/nordic/nrfx/prj.conf](../../../samples/boards/nordic/nrfx/prj.conf)。仓库源码仅作参照，版本可能与本次官方页面不同；本地链接按文档位置相对解析。

对应官方文档源码：[samples/boards/nordic/nrfx/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/nrfx/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nordic/nrfx/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P029_nRF系统事件.md) · [返回大纲](大纲.md) · [下一章](P031_nrfx外设资源共享.md)
