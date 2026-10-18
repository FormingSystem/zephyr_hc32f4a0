---
id: learning.zephyr-docs.board-samples.page-77
title: DSP非对称多处理闪灯
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nxp/adsp/rtxxx/amp_blinky/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="amp_blinky"></a>

# 第77章\_AMP 闪灯示例（Blinky AMP sample）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nxp/adsp/rtxxx/amp_blinky/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nxp/adsp/rtxxx/amp_blinky/README.rst/..)

<a id="overview"></a>

## 77.1 概述（Overview）

本示例展示如何在非对称多处理（Asymmetric Multiprocessing，AMP）场景中使用受支持 NXP i.MX RTxxx 平台的 DSP 域。Cortex-M 域和 DSP 域各有独立工程，通过 Sysbuild 一起构建为最终的单一镜像。Cortex-M 域负责设置 DSP 域，包括时钟、电源、代码加载和启动；DSP 域向开发板选定的控制台 UART 输出“hello world”消息，并使 LED 闪烁。按下关联按钮可关闭闪烁，借此演示 DSP 域上的中断服务和 GPIO 回调。

> 译注——按钮行为：本次远端代码使用 led1 与 sw0 别名，每 1000 ms 翻转 LED，完整亮灭周期约两秒。中断回调对 blink 取反，因此按钮可关闭也可重新启用闪烁；关闭后线程在下一轮把 LED 置为无效状态，不是直接终止 DSP。

<a id="building-and-running"></a>

## 77.2 构建与运行（Building and Running）

> 译注——执行前提：west 构建命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工作区、工具链、模块与具体板；下载按板文档核对。主机网络和模型转换步骤另按相应小节的执行环境处理。本次未构建、烧录或运行硬件实验。

可按以下方式在受支持的开发板上构建并启动示例：

> 译注——原始命令参数：<board> 要替换为正文支持的完整 Cortex-M 板目标。本次 west build 的 -o／--build-opt 需要一个传给构建工具的参数；原文孤立的 -o 没有给值，应按当前语法去掉该 -o 并保留 --sysbuild。原始命令在下方完整保留，不能把这个 -o 解释为“输出镜像”或“打开系统构建”。

```text
west build -b <board> -o --sysbuild samples/boards/nxp/adsp/rtxxx/amp_blinky
west flash -r jlink
```

当前支持的开发板为：`mimxrt685_evk/mimxrt685s/cm33`。

> 译注——中断与去抖：示例将按钮配置为有效沿触发，没有软件去抖，机械抖动可能造成多次翻转。它主要演示 DSP 域的 GPIO 回调，不应把按下一次必然产生一次状态变化当作通用按钮保证。

建议使用运行 J-Link 固件的板载调试探针，或独立 J-Link 探针，因为 J-Link 能够直接调试基于 Xtensa 的 DSP 内核。

> 译注——双域构建：本次 sysbuild 将 remote 标为 BUILD_ONLY，公共 CMake 脚本从 DSP ELF 提取 reset／text／data 分段，再嵌入 Cortex-M 应用并由其启动 DSP。不是主机分别手动执行两次 west flash 就自动形成相同依赖；这里“单一镜像”仍包含两个独立域的构建结果。

<a id="sample-output"></a>

### 77.2.1 输出示例（Sample output）

```text
*** Booting Zephyr OS build v4.1.0-1858-g6bd0a62b0bde ***
Hello World! mimxrt685_evk/mimxrt685s/cm33
[CM33] Starting HiFi4 DSP...
*** Booting Zephyr OS build v4.1.0-1858-g6bd0a62b0bde ***
[DSP] Hello World! mimxrt685_evk/mimxrt685s/hifi4
[DSP] Button pressed!
```

> 译注——源码入口：仓库相对参照：[src/main.c](../../../samples/boards/nxp/adsp/rtxxx/amp_blinky/src/main.c)；[CMakeLists.txt](../../../samples/boards/nxp/adsp/rtxxx/amp_blinky/CMakeLists.txt)；[remote/src/main.c](../../../samples/boards/nxp/adsp/rtxxx/amp_blinky/remote/src/main.c)；[sysbuild.cmake](../../../samples/boards/nxp/adsp/rtxxx/amp_blinky/sysbuild.cmake)；[scripts/west_commands/build.py](../../../scripts/west_commands/build.py)。本地版本可能与网页不同。

对应官方文档源码：[samples/boards/nxp/adsp/rtxxx/amp_blinky/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nxp/adsp/rtxxx/amp_blinky/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nxp/adsp/rtxxx/amp_blinky/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P076_DSP非对称多处理音频输出.md) · [返回大纲](大纲.md) · [下一章](P078_DSP非对称多处理OpenAMP通信.md)
