---
id: learning.zephyr-docs.board-samples.page-36
title: microbit_LED矩阵显示
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/bbc/microbit/display/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bbc_microbit_display"></a>

# 第36章\_LED 矩阵显示（LED matrix display）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/bbc/microbit/display/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/bbc/microbit/display/README.rst/..)

<a id="overview"></a>

## 36.1 概述（Overview）

这个简单示例展示如何使用 BBC micro:bit 开发板上的 5×5 LED 矩阵显示屏（LED matrix display）。

> 译注——显示接口：示例使用 micro:bit 专用的 mb_display_get()、mb_display_print() 与 mb_display_image() API，5×5 是板上的物理 LED 像素阵列。图片帧由 C 源码中的 MB_IMAGE 数组提供，不是网页遗漏了需要下载的 GIF 或 WebP。

<a id="building"></a>

## 36.2 构建（Building）

> 译注——执行前提：west 命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工具、west 工作区、模块与目标工具链；应用和 overlay 为官方源码，构建目录由工具生成。选择与实物一致的板目标，构建成功后再烧录，失败时检查构建输出和板文档；本次没有执行构建、烧录或硬件实验。

本项目在 BBC micro:bit 显示屏上输出多种内容，可按以下方式构建：

```text
west build -b bbc_microbit samples/boards/bbc/microbit/display
```

<a id="sample-output"></a>

### 36.2.1 输出示例（Sample Output）

示例应用依次显示字符 9～0 的倒计数，逐个点亮全部像素，显示笑脸与一些动画，最后滚动显示文本“Hello Zephyr!”。

> 译注——顺序与异步调用：本次源码说明显示 API 异步执行，示例在各项演示之间调用 k_sleep() 以便依次观察。最后的 Hello Zephyr! 使用循环滚动标志；输出应在板上 LED 矩阵观察，不是要求串口打印这段文本。

> 译注——源码入口：[main.c](../../../samples/boards/bbc/microbit/display/src/main.c)；[prj.conf](../../../samples/boards/bbc/microbit/display/prj.conf)。本地链接以本文为基准相对解析，源码版本可能与本次网页不同。

对应官方文档源码：[samples/boards/bbc/microbit/display/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/bbc/microbit/display/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/bbc/microbit/display/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P035_Nordic示例目录.md) · [返回大纲](大纲.md) · [下一章](P037_microbit巡线机器人.md)
