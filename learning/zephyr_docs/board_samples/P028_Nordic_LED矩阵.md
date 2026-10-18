---
id: learning.zephyr-docs.board-samples.page-28
title: Nordic_LED矩阵
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nordic/nrf_led_matrix/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nrf_led_matrix"></a>

# 第28章\_LED 矩阵（LED matrix）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nordic/nrf_led_matrix/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nordic/nrf_led_matrix/README.rst/..)

<a id="overview"></a>

## 28.1 概述（Overview）

这是一个简单应用，用于展示 nRF LED 矩阵显示驱动（LED matrix display driver）的运行效果，同时作为测试，确保该驱动能针对 [micro:bit V2](https://docs.zephyrproject.org/latest/boards/bbc/microbit_v2/doc/index.html#bbc_microbit_v2) 与 micro:bit 开发板构建。 相关链接：[micro:bit](https://docs.zephyrproject.org/latest/boards/bbc/microbit/doc/index.html#bbc_microbit)。

<a id="requirements"></a>

## 28.2 前提条件（Requirements）

原示例已在 bbc_microbit_v2 与 bbc_microbit 开发板上测试；也可以移植到任何具有 nRF SoC、且有足够 GPIO 驱动 LED 矩阵的开发板。为此，需要添加包含 `"nordic,nrf-led-matrix"` 兼容节点的覆盖文件。

> 译注——验证归属：这句话描述官方原文的测试情况，不代表本次进行了构建或实板验证。LED 矩阵（Light-Emitting Diode matrix）驱动依赖实际行列 GPIO 与板级配置，不能将不同 micro:bit 版本的引脚定义混用。

<a id="building-and-running"></a>

## 28.3 构建与运行（Building and Running）

> 译注——执行前提：除本页另有说明的目录外，west 命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先准备[入门指南](../getting_started/大纲.md)所需的主机工具、west 工作区、模块与目标工具链；应用、配置及 overlay 为官方源码，构建目录由工具生成。构建成功后再按目标板文档烧录，失败时返回构建输出或板文档检查；下方日志是官方预期示例，本次未执行硬件步骤。

代码位于 [samples/boards/nordic/nrf_led_matrix](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/nordic/nrf_led_matrix)。

构建并烧录应用：

```text
west build -b bbc_microbit_v2 samples/boards/nordic/nrf_led_matrix
west flash
```

> 译注——实现入口：[samples/boards/nordic/nrf_led_matrix/src/main.c](../../../samples/boards/nordic/nrf_led_matrix/src/main.c)与[samples/boards/nordic/nrf_led_matrix/prj.conf](../../../samples/boards/nordic/nrf_led_matrix/prj.conf)。仓库源码仅作参照，版本可能与本次官方页面不同；本地链接按文档位置相对解析。

对应官方文档源码：[samples/boards/nordic/nrf_led_matrix/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/nrf_led_matrix/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nordic/nrf_led_matrix/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P027_Nordic_IronSide_SE固件更新.md) · [返回大纲](大纲.md) · [下一章](P029_nRF系统事件.md)
