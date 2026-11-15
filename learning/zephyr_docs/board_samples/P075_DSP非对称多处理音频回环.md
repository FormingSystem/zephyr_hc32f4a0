---
id: learning.zephyr-docs.board-samples.page-75
title: DSP非对称多处理音频回环
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nxp/adsp/rtxxx/amp_audio_loopback/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="amp_audio_loopback"></a>

# 第75章\_音频输出 AMP 示例（Audio output AMP sample）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nxp/adsp/rtxxx/amp_audio_loopback/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nxp/adsp/rtxxx/amp_audio_loopback/README.rst/..)

<a id="overview"></a>

## 75.1 概述（Overview）

本示例展示如何在非对称多处理（Asymmetric Multiprocessing，AMP）场景中使用受支持 NXP i.MX RTxxx 平台的 DSP 域。Cortex-M 域和 DSP 域各自拥有独立工程，通过 Sysbuild 一起构建为最终的单一镜像。Cortex-M 域负责设置 DSP 域，包括时钟、电源、代码加载和启动；DSP 域向开发板选定的控制台 UART 输出“hello world”消息，初始化音频播放与采集硬件，随后同时采集和播放音频，实现回声／回环（Echo／Loopback）。

> 译注——标题与数据流：官方标题仍是 Audio output AMP sample，本页实际目录和实现是音频回环，因此本册文件名标为“音频回环”。DSP 从 i2s-rx 读取采样块并交给 i2s-tx，Cortex-M 不逐块转发音频。这里的 DSP 为数字信号处理器（Digital Signal Processor），I2S 为芯片间音频串行总线（Inter-IC Sound）。

<a id="building-and-running"></a>

## 75.2 构建与运行（Building and Running）

> 译注——执行前提：west 构建命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工作区、工具链、模块与具体板；下载按板文档核对。主机网络和模型转换步骤另按相应小节的执行环境处理。本次未构建、烧录或运行硬件实验。

可按以下方式在受支持的开发板上构建并启动示例：

> 译注——原始命令参数：<board> 要替换为正文支持的完整 Cortex-M 板目标。本次 west build 的 -o／--build-opt 需要一个传给构建工具的参数；原文孤立的 -o 没有给值，应按当前语法去掉该 -o 并保留 --sysbuild。原始命令在下方完整保留，不能把这个 -o 解释为“输出镜像”或“打开系统构建”。

```text
west build -b <board> -o --sysbuild samples/boards/nxp/adsp/rtxxx/amp_audio_loopback
west flash -r jlink
```

当前支持的开发板为：`mimxrt685_evk/mimxrt685s/cm33`。

> 译注——音频参数：本次远端源码配置 48 kHz、16 位、双声道，单块含每声道 4800 个样本，合计 19200 字节、对应 100 ms 音频；启动前还预填四个静音块。块时长不等于完整端到端延迟，不能把注释中的 100 ms 当作实测指标。

建议使用运行 J-Link 固件的板载调试探针，或独立 J-Link 探针，因为 J-Link 能够直接调试基于 Xtensa 的 DSP 内核。

> 译注——双域构建：本次 sysbuild 将 remote 标为 BUILD_ONLY，公共 CMake 脚本从 DSP ELF 提取 reset／text／data 分段，再嵌入 Cortex-M 应用并由其启动 DSP。不是主机分别手动执行两次 west flash 就自动形成相同依赖；这里“单一镜像”仍包含两个独立域的构建结果。

<a id="sample-output"></a>

### 75.2.1 输出示例（Sample output）

> 译注——启动日志：Streams started 表示流启动调用成功，之后仍可能发生读写错误；它不证明模拟音频接线、回放质量或长时间无丢块。本页没有供下载的原始音频文件。

```text
*** Booting Zephyr OS build v4.1.0-1857-g5a39ed584d81 ***
Hello World! mimxrt685_evk/mimxrt685s/cm33
[ARM] Starting DSP...
*** Booting Zephyr OS build v4.1.0-1857-g5a39ed584d81 ***
Hello World! mimxrt685_evk/mimxrt685s/hifi4
[DSP] Streams started.
```

> 译注——源码入口：仓库相对参照：[src/main.c](../../../samples/boards/nxp/adsp/rtxxx/amp_audio_loopback/src/main.c)；[CMakeLists.txt](../../../samples/boards/nxp/adsp/rtxxx/amp_audio_loopback/CMakeLists.txt)；[remote/src/main.c](../../../samples/boards/nxp/adsp/rtxxx/amp_audio_loopback/remote/src/main.c)；[sysbuild.cmake](../../../samples/boards/nxp/adsp/rtxxx/amp_audio_loopback/sysbuild.cmake)；[scripts/west_commands/build.py](../../../scripts/west_commands/build.py)。本地版本可能与网页不同。

对应官方文档源码：[samples/boards/nxp/adsp/rtxxx/amp_audio_loopback/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nxp/adsp/rtxxx/amp_audio_loopback/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nxp/adsp/rtxxx/amp_audio_loopback/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P074_DSP优化库计算.md) · [返回大纲](大纲.md) · [下一章](P076_DSP非对称多处理音频输出.md)
