---
id: learning.zephyr-docs.board-samples.page-23
title: CoreSight_STM基准测试
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nordic/coresight_stm/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="coresight_stm_sample"></a>

# 第23章\_CoreSight STM 基准测试（Coresight STM benchmark）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nordic/coresight_stm/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nordic/coresight_stm/README.rst/..)

<a id="overview"></a>

## 23.1 概述（Overview）

本示例介绍如何在 nRF54H20 平台上启用 STM 日志。

> 译注——术语：这里 STM 是 Arm 系统跟踪宏单元（System Trace Macrocell），与 STM32 厂商前缀无关。ETR 为嵌入式跟踪路由器（Embedded Trace Router），STPv2 为 MIPI 系统跟踪协议第 2 版（System Trace Protocol v2）；PPR 为外设处理器（Peripheral Processor），FLPR 为快速轻量处理器（Fast Lightweight Processor）。

示例还会打印不同日志消息的耗时，因此可以比较不同日志记录方式的性能。

`tests.yaml` 中包含三种示例配置。

> 译注——原文范围：本次 tests.yaml 实际还有 C++、RTT 与 TPIU 字典等变体。正文只介绍以下三种，不能把这里的数量当作当前全部测试配置数量。

- sample.boards.nrf.coresight_stm.local_uart

  这种配置不使用 STM，而是在本地控制台打印日志。

- sample.boards.nrf.coresight_stm

  这种配置使用 STM。应用核、无线核、PPR 核和 FLPR 核将日志发送到 ETR 缓冲区。代理（Proxy，位于应用核）从 ETR 缓冲区取出日志，解码 STPv2 数据，并通过 UART 打印可读日志。

- sample.boards.nrf.coresight_stm.dict

  这种配置以字典模式（Dictionary mode）记录 STM 日志。应用核、无线核、PPR 核和 FLPR 核将日志发送到 ETR 缓冲区。代理（位于应用核）通过 UART 将 ETR 中的数据转发给主机；需要主机工具解码这些日志。

<a id="requirements"></a>

## 23.2 前提条件（Requirements）

本应用使用 nRF54H20 DK 开发板进行演示。

sample.boards.nrf.coresight_stm.dict 需要 `nrfutil trace` 等主机工具来解码跟踪数据。

<a id="building-and-running"></a>

## 23.3 构建与运行（Building and running）

> 译注——执行前提：除本页另有说明的目录外，west 命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先准备[入门指南](../getting_started/大纲.md)所需的主机工具、west 工作区、模块与目标工具链；应用、配置及 overlay 为官方源码，构建目录由工具生成。构建成功后再按目标板文档烧录，失败时返回构建输出或板文档检查；下方日志是官方预期示例，本次未执行硬件步骤。

构建示例时，通过 `-T` 选项选择 `tests.yaml` 中的配置。示例如下：

> 译注——执行目录：下方命令末尾的点号表示当前应用目录，因此应先进入 Zephyr 源码下的 samples/boards/nordic/coresight_stm；其他以 samples/... 为应用参数的章节通常从源码根执行。-T 选择 tests.yaml 的测试场景；本次文件标记 sysbuild: true，并指定所需配置片段和远端核。不要漏掉该场景参数而假定四个核会自动得到相同配置。

nRF54H20 DK

> ```text
> west build -p -b nrf54h20dk/nrf54h20/cpuapp -T sample.boards.nrf.coresight_stm .
> ```

<a id="sample-output"></a>

### 23.3.1 输出示例（Sample Output）

> 译注——基准结果边界：Timing 为耗时，arguments 为参数个数，tracepoint 为跟踪点，us 为微秒。日志中的 0.0us 是此测量和打印精度下的结果，不是保证零开销；旧版 Zephyr 标识、各核标签与全部数值按原文保留。

```text
*** Using Zephyr OS v3.6.99-5bb7bb0af17c ***
(...)
[00:00:00.227,264] <inf> app/app: test with one argument 100
[00:00:00.227,265] <inf> app/app: test with one argument 100
(...)
[00:00:00.585,558] <inf> rad/app: test with one argument 100
[00:00:00.585,569] <inf> rad/app: test with one argument 100
(...)
[00:00:00.624,408] <inf> ppr/app: test with one argument 100
[00:00:00.624,433] <inf> ppr/app: test with one argument 100
(...)
[00:00:00.625,249] <inf> flpr/app: test with one argument 100
[00:00:00.625,251] <inf> flpr/app: test with one argument 100
(...)
rad: Timing for log message with 0 arguments: 5.10us
rad: Timing for log message with 1 argument: 6.10us
rad: Timing for log message with 2 arguments: 6.0us
rad: Timing for log message with 3 arguments: 6.40us
rad: Timing for log_message with string: 7.10us
rad: Timing for tracepoint: 0.5us
rad: Timing for tracepoint_d32: 0.5us
flpr: Timing for log message with 0 arguments: 1.20us
flpr: Timing for log message with 1 argument: 1.20us
flpr: Timing for log message with 2 arguments: 1.20us
flpr: Timing for log message with 3 arguments: 1.30us
flpr: Timing for log_message with string: 3.0us
flpr: Timing for tracepoint: 0.0us
flpr: Timing for tracepoint_d32: 0.0us
app: Timing for log message with 0 arguments: 1.80us
app: Timing for log message with 1 argument: 2.0us
app: Timing for log message with 2 arguments: 2.0us
app: Timing for log message with 3 arguments: 2.10us
app: Timing for log_message with string: 4.40us
app: Timing for tracepoint: 0.10us
app: Timing for tracepoint_d32: 0.10us
ppr: Timing for log message with 0 arguments: 25.20us
ppr: Timing for log message with 1 argument: 26.20us
ppr: Timing for log message with 2 arguments: 26.90us
ppr: Timing for log message with 3 arguments: 27.40us
ppr: Timing for log_message with string: 64.80us
ppr: Timing for tracepoint: 0.30us
ppr: Timing for tracepoint_d32: 0.25us
```

关于在 nRF54H20 上使用 ARM CoreSight STM 记录日志，请参阅[使用 ARM CoreSight STM 进行多域日志记录（Multi-domain logging using ARM Coresight STM）](../observability/P012_CoreSight系统跟踪日志.md#logging-cs-stm)。

<a id="see-also"></a>

## 23.4 另请参阅（See also）

[日志 API（Logging API）](../log_core_reference/P002_日志公共接口.md)

> 译注——实现入口：[samples/boards/nordic/coresight_stm/src/main.c](../../../samples/boards/nordic/coresight_stm/src/main.c)与[samples/boards/nordic/coresight_stm/prj.conf](../../../samples/boards/nordic/coresight_stm/prj.conf)。仓库源码仅作参照，版本可能与本次官方页面不同；本地链接按文档位置相对解析。 配置依据见[本次上游 tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/coresight_stm/tests.yaml)。

对应官方文档源码：[samples/boards/nordic/coresight_stm/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/coresight_stm/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nordic/coresight_stm/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P022_nRF5x时钟偏差.md) · [返回大纲](大纲.md) · [下一章](P024_CoreSight_STM远程Shell.md)
