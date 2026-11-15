---
id: learning.zephyr-docs.board-samples.page-74
title: DSP优化库计算
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nxp/adsp/number_crunching/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="number_crunching"></a>

# 第74章\_使用优化库进行数值计算（Number crunching using optimized library）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nxp/adsp/number_crunching/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nxp/adsp/number_crunching/README.rst/..)

<a id="overview"></a>

## 74.1 概述（Overview）

本数值计算示例执行向量运算、快速傅里叶变换（Fast Fourier Transform，FFT）和滤波，演示如何将位于源码树外（Out of tree）的专有静态库加入 Zephyr 构建系统。

要在本示例中使用树外库，需要定义环境变量 `LIB_LOCATION`，该位置必须包含定义下列内容的 `CMakeLists.txt`：

> 译注——读取关系：本次 CMakeLists.txt 检查环境中的 LIB_LOCATION，再通过 add_subdirectory() 读取该库自己的 CMakeLists.txt，最后拼接 INCLUDE_DIR、LIB_DIR 和 LIB_NAME。它不是名为 LIB_LOCATION 的普通 -D 缓存选项；库文件名、头文件目录及目标架构须和实际库一致，不能把示例 proprietary_lib.a 当作已提供的文件。

```text
# Link with the external 3rd party library.
set(LIB_DIR         "lib"                   CACHE STRING "")
set(INCLUDE_DIR     "include"               CACHE STRING "")
set(LIB_NAME        "proprietary_lib.a"     CACHE STRING "")
```

如果未定义环境变量 `LIB_LOCATION`，则改用默认的 Zephyr API。

> 译注——默认后端：本次配置实际启用 CONFIG_CMSIS_DSP 并编译 cmsis_dsp_wrapper.c，因此“默认 Zephyr API”具体由 CMSIS-DSP 封装实现；定义 LIB_LOCATION 则切换到 NatureDSP 封装，不是仅替换一个链接文件就能适配任意数学库。

示例执行可用于音频处理的数学函数，例如用于滤波的快速傅里叶变换（FFT），以及用于回声消除的最小均方（Least Mean Square，LMS）滤波算法。

示例包含：

- `main.c`：调用通用数学函数。

- `math_ops.c`：执行数学函数、统计执行消耗的周期数并检查输出。

- `cmsis_dsp_wrapper.c`：当定义了 [`CONFIG_CMSIS_DSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CMSIS_DSP) 且未定义 `LIB_LOCATION` 时，调用 CMSIS-DSP 的对应数学函数。

- `nature_dsp_wrapper`：当定义了 `LIB_LOCATION` 且它指向包含 NatureDSP 库及头文件的树外位置时，调用 NatureDSP 库的对应数学函数。

要加入新后端，需要为该库或后端创建新的封装层（Wrapper）。

<a id="requirements"></a>

## 74.2 前提条件（Requirements）

CMSIS-DSP 是可选模块，需要显式加入 Zephyr 工作区：

> 译注——工作区操作：west config manifest.project-filter 会设置工作区的项目过滤配置；若已有过滤条件，应合并保留其他所需模块。west update cmsis-dsp 获取模块源码，并不下载或编译 NatureDSP 静态库。

```text
west config manifest.project-filter -- +cmsis-dsp
west update cmsis-dsp
```

NatureDSP 可从 GitHub 的 https://github.com/foss-xtensa/ndsplib-hifi4/tree/main 获取；编译方法按该仓库所述步骤执行。 相关链接：[NatureDSP 官方仓库](https://github.com/foss-xtensa/ndsplib-hifi4/tree/main)。

<a id="building-and-running"></a>

## 74.3 构建与运行（Building and Running）

> 译注——执行前提：west 构建命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工作区、工具链、模块与具体板；下载按板文档核对。主机网络和模型转换步骤另按相应小节的执行环境处理。本次未构建、烧录或运行硬件实验。

使用 `west` 为 NXP i.MX8M Plus 开发板的 HiFi4 DSP 核 `imx8mp_evk/mimx8ml8/adsp` 构建本示例，可运行：

```text
west build -b imx8mp_evk/mimx8ml8/adsp samples/boards/nxp/adsp/number_crunching/
west build -t run
```

CMSIS-DSP 的输出示例如下：

> 译注——结果与计时：DSP 为数字信号处理器（Digital Signal Processor）；IIR 为无限冲激响应（Infinite Impulse Response）滤波。end with 1 表示相应比较通过；本次源码只对部分向量测试显式比较结果，FFT、IIR、LMS 的 end 日志并非全部正确性的独立断言。周期由 k_cycle_get_32() 读取，包含封装层执行及其中打印开销，不能把两组日志直接当作所有硬件上的性能比例。

```text
*** Booting Zephyr OS build v3.7.0-2815-g9018e424d7a1 ***

Proprietary library example!

[Library Test] == Vector Sum test  ==
[Backend] CMSIS-DSP module
[Library Test] Vector Sum takes 6886 cycles
[Library Test] == Vector Sum test end with 1 ==

[Library Test] == Vector power sum test  ==
[Backend] CMSIS-DSP module
[Library Test] Vector power sum takes 6659 cycles
[Library Test] == Vector power sum test end with 1 ==

[Library Test] == Vector power sum test  ==
[Backend] CMSIS-DSP module
[Library Test] Vector power sum takes 3681 cycles
[Library Test] == Vector power sum test end ==

[Library Test] == Fast Fourier Transform on Real Data test  ==
[Backend] CMSIS-DSP module
[Library Test] Fast Fourier Transform on Real Data takes 67956 cycles
[Library Test] == Fast Fourier Transform on Real Data test end ==

[Library Test] == Bi-quad Real Block IIR test  ==
[Backend] CMSIS-DSP module
[Library Test] Bi-quad Real Block IIR takes 506702 cycles
[Library Test] == Bi-quad Real Block IIR end ==

[Library Test] == Least Mean Square (LMS) Filter for Real Data test  ==
[Backend] CMSIS-DSP module
[Library Test] Least Mean Square (LMS) Filter for Real Data test takes 184792 cycles
[Library Test] == Least Mean Square (LMS) Filter for Real Data test end ==
```

NatureDSP 的输出如下：

```text
*** Booting Zephyr OS build v3.7.0-2815-g9018e424d7a1 ***

Proprietary library example!

[Library Test] == Vector Sum test  ==
[Backend] NatureDSP library
[Library Test] Vector Sum takes 3829 cycles
[Library Test] == Vector Sum test end with 1 ==

[Library Test] == Vector power sum test  ==
[Backend] NatureDSP library
[Library Test] Vector power sum takes 2432 cycles
[Library Test] == Vector power sum test end with 1 ==

[Library Test] == Vector power sum test  ==
[Backend] NatureDSP library
[Library Test] Vector power sum takes 2594 cycles
[Library Test] == Vector power sum test end ==

[Library Test] == Fast Fourier Transform on Real Data test  ==
[Backend] NatureDSP library
[Library Test] Fast Fourier Transform on Real Data takes 3338 cycles
[Library Test] == Fast Fourier Transform on Real Data test end ==

[Library Test] == Bi-quad Real Block IIR test  ==
[Backend] NatureDSP library
[Library Test] Bi-quad Real Block IIR takes 13501 cycles
[Library Test] == Bi-quad Real Block IIR end ==

[Library Test] == Least Mean Square (LMS) Filter for Real Data test  ==
[Backend] NatureDSP library
[Backend] NatureDSP library
[Library Test] Least Mean Square (LMS) Filter for Real Data test takes 7724 cycles
[Library Test] == Least Mean Square (LMS) Filter for Real Data test end ==
```

> 译注——源码入口：仓库相对参照：[src/main.c](../../../samples/boards/nxp/adsp/number_crunching/src/main.c)；[CMakeLists.txt](../../../samples/boards/nxp/adsp/number_crunching/CMakeLists.txt)；[src/math_ops.c](../../../samples/boards/nxp/adsp/number_crunching/src/math_ops.c)。本地版本可能与网页不同。

对应官方文档源码：[samples/boards/nxp/adsp/number_crunching/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nxp/adsp/number_crunching/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nxp/adsp/number_crunching/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P073_SmartDMA内存到内存传输.md) · [返回大纲](大纲.md) · [下一章](P075_DSP非对称多处理音频回环.md)
