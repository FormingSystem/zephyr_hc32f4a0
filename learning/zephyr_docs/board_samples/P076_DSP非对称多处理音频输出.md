---
id: learning.zephyr-docs.board-samples.page-76
title: DSP非对称多处理音频输出
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nxp/adsp/rtxxx/amp_audio_output/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="amp_audio_output"></a>

# 第76章\_音频输出 AMP 示例（Audio output AMP sample）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nxp/adsp/rtxxx/amp_audio_output/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nxp/adsp/rtxxx/amp_audio_output/README.rst/..)

<a id="overview"></a>

## 76.1 概述（Overview）

本示例展示如何在非对称多处理（Asymmetric Multiprocessing，AMP）场景中使用受支持 NXP i.MX RTxxx 平台的 DSP 域。Cortex-M 域和 DSP 域各有独立工程，通过 Sysbuild 一起构建为最终的单一镜像。Cortex-M 域负责设置 DSP 域，包括时钟、电源、代码加载和启动；DSP 域向开发板选定的控制台 UART 输出“hello world”消息，初始化音频播放硬件，并播放周期音频信号。

> 译注——波形与时长：本次 DSP 使用 64 点正弦表，在 48 kHz、16 位、双声道配置下输出，理想重复频率为 750 Hz；右声道相对左声道偏移四分之一周期，幅值按缓冲块作衰减。代码按固定次数发送后请求排空并停止，不是无限持续播放。

<a id="building-and-running"></a>

## 76.2 构建与运行（Building and Running）

> 译注——执行前提：west 构建命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工作区、工具链、模块与具体板；下载按板文档核对。主机网络和模型转换步骤另按相应小节的执行环境处理。本次未构建、烧录或运行硬件实验。

可按以下方式在受支持的开发板上构建并启动示例：

> 译注——原始命令参数：<board> 要替换为正文支持的完整 Cortex-M 板目标。本次 west build 的 -o／--build-opt 需要一个传给构建工具的参数；原文孤立的 -o 没有给值，应按当前语法去掉该 -o 并保留 --sysbuild。原始命令在下方完整保留，不能把这个 -o 解释为“输出镜像”或“打开系统构建”。

```text
west build -b <board> -o --sysbuild samples/boards/nxp/adsp/rtxxx/amp_audio_output
west flash -r jlink
```

当前支持的开发板为：`mimxrt685_evk/mimxrt685s/cm33`。

建议使用运行 J-Link 固件的板载调试探针，或独立 J-Link 探针，因为 J-Link 能够直接调试基于 Xtensa 的 DSP 内核。

> 译注——双域构建：本次 sysbuild 将 remote 标为 BUILD_ONLY，公共 CMake 脚本从 DSP ELF 提取 reset／text／data 分段，再嵌入 Cortex-M 应用并由其启动 DSP。不是主机分别手动执行两次 west flash 就自动形成相同依赖；这里“单一镜像”仍包含两个独立域的构建结果。

<a id="sample-output"></a>

### 76.2.1 输出示例（Sample output）

> 译注——日志阶段：Will start playback 在启动触发之前打印，Playback stopped 在请求 DRAIN 后打印。排空（Drain）表示发送完已排队数据再停止，日志不是示波器或音频设备确认结果。波形由源码数组产生，本页没有独立音频附件。

```text
*** Booting Zephyr OS build v4.1.0-1858-gab989bfb4894 ***
Hello World! mimxrt685_evk/mimxrt685s/cm33
[ARM] Starting DSP...
*** Booting Zephyr OS build v4.1.0-1858-gab989bfb4894 ***
[DSP] Hello World! mimxrt685_evk/mimxrt685s/hifi4
[DSP] Will start playback.
[DSP] Playback stopped.
```

> 译注——源码入口：仓库相对参照：[src/main.c](../../../samples/boards/nxp/adsp/rtxxx/amp_audio_output/src/main.c)；[CMakeLists.txt](../../../samples/boards/nxp/adsp/rtxxx/amp_audio_output/CMakeLists.txt)；[remote/src/main.c](../../../samples/boards/nxp/adsp/rtxxx/amp_audio_output/remote/src/main.c)；[sysbuild.cmake](../../../samples/boards/nxp/adsp/rtxxx/amp_audio_output/sysbuild.cmake)；[scripts/west_commands/build.py](../../../scripts/west_commands/build.py)。本地版本可能与网页不同。

对应官方文档源码：[samples/boards/nxp/adsp/rtxxx/amp_audio_output/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nxp/adsp/rtxxx/amp_audio_output/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nxp/adsp/rtxxx/amp_audio_output/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P075_DSP非对称多处理音频回环.md) · [返回大纲](大纲.md) · [下一章](P077_DSP非对称多处理闪灯.md)
