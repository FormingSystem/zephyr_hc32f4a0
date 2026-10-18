---
id: learning.zephyr-docs.board-samples.page-22
title: nRF5x时钟偏差
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nordic/clock_skew/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nrf_clock_skew"></a>

# 第22章\_nRF5x 时钟偏差（nRF5x Clock Skew）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nordic/clock_skew/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nordic/clock_skew/README.rst/..)

<a id="overview"></a>

## 22.1 概述（Overview）

本示例使用时间源关联（Time source correlation）API，测量 HFCLK（CPU 使用的高频时钟）与 LFCLK（系统时间使用的低频时钟）之间的时钟偏差（Clock skew）。它还演示如何利用该偏差，将 LFCLK 时钟域测得的时长修正为 HFCLK 时钟域中的时长。

> 译注——关联与校准：HFCLK 是高频时钟（High-Frequency Clock），LFCLK 是低频时钟（Low-Frequency Clock）；示例比较 timer0 与系统 tick，并在软件中换算时间。它没有调整晶体频率，也没有把 HFCLK 宣称为外部标准时间。

可以选择 Kconfig 选项 `CONFIG_APP_ENABLE_HFXO`，将高频时钟配置为使用晶体振荡器，而不是默认的 RC 振荡器。（蓝牙等需要精确高频时钟的功能通常会自动启用这个时钟源。）启用高频晶体振荡器（High-Frequency Crystal Oscillator，HFXO）后，相对误差会显著降低。

<a id="requirements"></a>

## 22.2 前提条件（Requirements）

本应用可使用任意 nRF51 DK 或 nRF52 DK 开发板进行演示。

<a id="building-flashing-and-running"></a>

## 22.3 构建、烧录与运行（Building, Flashing and Running）

> 译注——执行前提：除本页另有说明的目录外，west 命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先准备[入门指南](../getting_started/大纲.md)所需的主机工具、west 工作区、模块与目标工具链；应用、配置及 overlay 为官方源码，构建目录由工具生成。构建成功后再按目标板文档烧录，失败时返回构建输出或板文档检查；下方日志是官方预期示例，本次未执行硬件步骤。

```text
west build -b nrf52dk/nrf52832 samples/boards/nordic/clock_skew
west flash
```

运行结果：

> 译注——日志阅读：Latest 为最近采样，Base 为基准采样，Span 为经过时长，Err 为误差；HF/LF 分别对应高／低频时间，RHF 为按估计偏差重建的高频参考时间，Skew 为偏差比例，ppb 为十亿分之一（Parts per billion）。原始日志是示例结果，误差数值随板、时钟源与测量条件变化。

<a id="sample-output"></a>

### 22.3.1 输出示例（Sample Output）

```text
*** Booting Zephyr OS build v2.5.0-rc3-94-g06a4b650467b  ***
Power-up clocks: LFCLK[ON]: Running LFXO ; HFCLK[OFF]: Running HFINT
Start TIMER_0: 0
Timer-running clocks: LFCLK[ON]: Running LFXO ; HFCLK[OFF]: Running HFINT
Checking TIMER_0 at 16000000 Hz against ticks at 32768 Hz
Timer wraps every 268 s

Ty  Latest           Base             Span             Err
HF  00:00:00.015666
LF  00:00:00.404937
Started sync: 0

Ty  Latest           Base             Span             Err
HF  00:00:09.978436  00:00:00.015666  00:00:09.962769
LF  00:00:10.414520  00:00:00.404937  00:00:10.009582  00:00:00.046813
RHF 00:00:09.978435                                   -00:00:00.000000
Skew 0.995323 ; err 4676818 ppb

Ty  Latest           Base             Span             Err
HF  00:00:19.959136  00:00:00.015666  00:00:19.943469
LF  00:00:20.441589  00:00:00.404937  00:00:20.036651  00:00:00.093182
RHF 00:00:19.959117                                   -00:00:00.000018
Skew 0.995349 ; err 4650592 ppb

Ty  Latest           Base             Span             Err
HF  00:00:29.937181  00:00:00.015666  00:00:29.921514
LF  00:00:30.468627  00:00:00.404937  00:00:30.063690  00:00:00.142176
RHF 00:00:29.937175                                   -00:00:00.000005
Skew 0.995271 ; err 4729151 ppb

Ty  Latest           Base             Span             Err
HF  00:00:39.917347  00:00:00.015666  00:00:39.901680
LF  00:00:40.495666  00:00:00.404937  00:00:40.090728  00:00:00.189048
RHF 00:00:39.917339                                   -00:00:00.000008
Skew 0.995284 ; err 4715502 ppb

Ty  Latest           Base             Span             Err
HF  00:00:49.899493  00:00:00.015666  00:00:49.883826
LF  00:00:50.522674  00:00:00.404937  00:00:50.117736  00:00:00.233910
RHF 00:00:49.899486                                   -00:00:00.000007
Skew 0.995333 ; err 4667222 ppb

Ty  Latest           Base             Span             Err
HF  00:00:59.878166  00:00:00.015666  00:00:59.862499
LF  00:01:00.549713  00:00:00.404937  00:01:00.144775  00:00:00.282276
RHF 00:00:59.878154                                   -00:00:00.000011
Skew 0.995307 ; err 4693269 ppb
...
Ty  Latest           Base             Span             Err
HF  00:02:59.654855  00:00:00.015666  00:02:59.639188
LF  00:03:00.873901  00:00:00.404937  00:03:00.468963  00:00:00.829775
RHF 00:02:59.654857                                    00:00:00.000001
Skew 0.995402 ; err 4597902 ppb
...
Ty  Latest           Base             Span             Err
HF  00:04:59.410593  00:00:00.015666  00:04:59.394926
LF  00:05:01.198181  00:00:00.404937  00:05:00.793243  00:00:01.398317
RHF 00:04:59.410594                                    00:00:00.000001
Skew 0.995351 ; err 4648745 ppb
...
Ty  Latest           Base             Span             Err
HF  00:09:58.829511  00:00:00.015666  00:09:58.813845
LF  00:10:02.008911  00:00:00.404937  00:10:01.603973  00:00:02.790128
RHF 00:09:58.829509                                   -00:00:00.000002
Skew 0.995362 ; err 4637837 ppb
...
Ty  Latest           Base             Span             Err
HF  00:29:56.607589  00:00:00.015666  00:29:56.591923
LF  00:30:05.250732  00:00:00.404937  00:30:04.845794  00:00:08.253871
RHF 00:29:56.607585                                   -00:00:00.000004
Skew 0.995427 ; err 4573166 ppb
...
Ty  Latest           Base             Span             Err
HF  00:59:43.781443  00:00:00.015666  00:59:43.765776
LF  01:00:00.085113  00:00:00.404937  00:59:59.680175  00:00:15.914399
RHF 00:59:43.781535                                    00:00:00.000092
Skew 0.995579 ; err 4421055 ppb
...
Ty  Latest           Base             Span             Err
HF  01:59:37.666395  00:00:00.015666  01:59:37.650728
LF  02:00:09.810913  00:00:00.404937  02:00:09.405975  00:00:31.755247
RHF 01:59:37.666057                                   -00:00:00.000338
Skew 0.995595 ; err 4404723 ppb
...
Ty  Latest           Base             Span             Err
HF  05:58:33.905236  00:00:00.015666  05:58:33.889570
LF  06:00:08.604980  00:00:00.404937  06:00:08.200042  00:01:34.310472
RHF 05:58:33.904338                                   -00:00:00.000898
..
Skew 0.995635 ; err 4364550 ppb
Ty  Latest           Base             Span             Err
HF  11:56:59.503922  00:00:00.015666  11:56:59.488255
LF  12:00:06.793182  00:00:00.404937  12:00:06.388244  00:03:06.899989
RHF 11:56:59.503948                                    00:00:00.000025
Skew 0.995674 ; err 4325747 ppb
```

> 译注——实现入口：[samples/boards/nordic/clock_skew/src/main.c](../../../samples/boards/nordic/clock_skew/src/main.c)与[samples/boards/nordic/clock_skew/prj.conf](../../../samples/boards/nordic/clock_skew/prj.conf)。仓库源码仅作参照，版本可能与本次官方页面不同；本地链接按文档位置相对解析。

对应官方文档源码：[samples/boards/nordic/clock_skew/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/clock_skew/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nordic/clock_skew/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P021_电池电压测量.md) · [返回大纲](大纲.md) · [下一章](P023_CoreSight_STM基准测试.md)
