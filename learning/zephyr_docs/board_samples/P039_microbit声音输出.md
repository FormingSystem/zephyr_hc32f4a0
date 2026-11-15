---
id: learning.zephyr-docs.board-samples.page-39
title: microbit声音输出
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/bbc/microbit/sound/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bbc_microbit_sound"></a>

# 第39章\_声音输出（Sound）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/bbc/microbit/sound/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/bbc/microbit/sound/README.rst/..)

<a id="overview"></a>

## 39.1 概述（Overview）

本示例展示如何使用连接到 BBC micro:bit v1 边缘连接器 P0 端口的压电蜂鸣器，或 BBC micro:bit v2 的板载蜂鸣器。

<a id="requirements"></a>

## 39.2 前提条件（Requirements）

使用 BBC micro:bit v1 时，必须另接一个压电蜂鸣器。例如，MI:Power 扩展板同时带有压电蜂鸣器和纽扣电池；通过网络搜索可以较容易找到该扩展板的经销商。

升级后的 BBC micro:bit v2 无需外接蜂鸣器，其背面已内置一个蜂鸣器，标记为“speaker”（扬声器）。

> 译注——硬件选择：v1 的外接 P0 蜂鸣器与 v2 板载 speaker 是不同连接方式，下面两条构建命令分别选择 bbc_microbit 与 bbc_microbit_v2。按实际板版本选一条，不把两条连续执行当作单一安装流程。

<a id="building-and-running"></a>

## 39.3 构建与运行（Building and running）

> 译注——执行前提：west 命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工具、west 工作区、模块与目标工具链；应用和 overlay 为官方源码，构建目录由工具生成。选择与实物一致的板目标，构建成功后再烧录，失败时检查构建输出和板文档；本次没有执行构建、烧录或硬件实验。

可以按以下方式构建示例：

<a id="building-for-a-bbc-micro-bit-v1"></a>

### 39.3.1 为 BBC micro:bit v1 构建

```text
west build -b bbc_microbit samples/boards/bbc/microbit/sound
west flash
```

<a id="building-for-a-bbc-micro-bit-v2"></a>

### 39.3.2 为 BBC micro:bit v2 构建

```text
west build -b bbc_microbit_v2 samples/boards/bbc/microbit/sound
west flash
```

<a id="sample-output"></a>

#### 39.3.2.1 输出示例（Sample Output）

> 译注——观察位置：频率显示在板上的 5×5 LED，并可从串口看到 A pressed／B pressed（按下 A／B）、Period（周期）等调试文本。源码输出的 us 为微秒、Hz 为赫兹；实际听感与蜂鸣器及可听频率范围有关，不能把无明显声音直接等同于程序未运行。

本示例根据两个主按钮的按键操作，通过压电蜂鸣器输出声音。每次按键后，5×5 LED 显示屏都会显示当前输出频率。

> 译注——频率与周期：本次源码以 PWM（脉宽调制，Pulse Width Modulation）驱动蜂鸣器。A 增加周期、降低频率，B 减少周期、提高频率；f=1/T，代码把纳秒周期换算为 Hz 后显示。每次声音约 60 ms，随后静音 50 ms，发声忙碌期间的按键会被忽略。

<a id="see-also"></a>

## 39.4 另请参阅（See also）

脉宽调制（Pulse Width Modulation，[PWM](../hardware/P255_PWM公共接口.md)）

> 译注——源码入口：[main.c](../../../samples/boards/bbc/microbit/sound/src/main.c)；[prj.conf](../../../samples/boards/bbc/microbit/sound/prj.conf)；[bbc_microbit.overlay](../../../samples/boards/bbc/microbit/sound/boards/bbc_microbit.overlay)；[bbc_microbit_v2.overlay](../../../samples/boards/bbc/microbit/sound/boards/bbc_microbit_v2.overlay)。本地链接以本文为基准相对解析，源码版本可能与本次网页不同。

对应官方文档源码：[samples/boards/bbc/microbit/sound/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/bbc/microbit/sound/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/bbc/microbit/sound/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P038_microbit_Pong游戏.md) · [返回大纲](大纲.md) · [下一章](P040_BBC_microbit示例目录.md)
