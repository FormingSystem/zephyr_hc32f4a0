---
id: learning.zephyr-docs.board-samples.page-24
title: CoreSight_STM远程Shell
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nordic/coresight_stm_shell/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="coresight_stm_shell"></a>

# 第24章\_带远程 Shell 的 CoreSight STM（Coresight STM with remote shell）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nordic/coresight_stm_shell/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nordic/coresight_stm_shell/README.rst/..)

<a id="overview"></a>

## 24.1 概述（Overview）

本示例将使用 ARM CoreSight STM 进行多域日志记录（Multi-domain logging using ARM Coresight STM，在应用核上通过 CoreSight STM 记录日志）与 [Shell](../interaction/P001_Shell命令行.md#shell-api)、[远程 Shell（Remote Shell）](../interaction/P001_Shell命令行.md#shell-remote)结合起来，演示在多个处理器核上使用远程 Shell，以及 STM 日志的运行时过滤（Runtime filtering）。 相关链接：[使用 ARM CoreSight STM 进行多域日志记录（Multi-domain logging using ARM Coresight STM）](../observability/P012_CoreSight系统跟踪日志.md#logging-cs-stm)。

可以使用 Shell 调整所有处理器核上日志模块的运行时过滤设置。

例如，`log enable dbg app` 会为 `cpuapp` 核的 `app` 日志模块启用最高到调试级别的消息；`remote_shell radio log enable dbg app` 会在 `cpurad` 核上执行同样的操作。

自定义的 `ping` 命令在每个严重级别（从错误到调试）分别打印一条消息；更改日志过滤配置后运行该命令，可确认启用了哪些级别。

> 译注——命令运行位置：这些 log、remote_shell 和 ping 命令输入板上的 Zephyr Shell，不是在电脑 Bash 里执行。这里 ping 是打印日志及 pong 的自定义命令，不是 ICMP 网络探测；编译时已去除的日志不能仅通过运行时过滤重新恢复。

本示例仅支持 `nrf54h20dk/nrf54h20/cpuapp`。

<a id="requirements"></a>

## 24.2 前提条件（Requirements）

- nRF54H20 DK

<a id="building-and-running"></a>

## 24.3 构建与运行（Building and running）

> 译注——执行前提：除本页另有说明的目录外，west 命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先准备[入门指南](../getting_started/大纲.md)所需的主机工具、west 工作区、模块与目标工具链；应用、配置及 overlay 为官方源码，构建目录由工具生成。构建成功后再按目标板文档烧录，失败时返回构建输出或板文档检查；下方日志是官方预期示例，本次未执行硬件步骤。

```text
west build -b nrf54h20dk/nrf54h20/cpuapp samples/boards/nordic/coresight_stm_shell \
  -T sample.boards.nrf.coresight_stm_shell
```

`nordic-log-stm` 配置片段（Snippet）在所有处理器核上启用 STM 日志前端（Frontend）与 CoreSight 覆盖文件（Overlay）。

> 译注——多核构建依据：本次 tests.yaml 通过 sysbuild: true 和 required_snippets 指定多核系统构建与 nordic-log-stm；命令的 -T 参数用于选取这一场景。cpuapp 与 cpurad 的日志模块同名不代表同一个运行实例，远程命令中的 radio 指目标端。

<a id="see-also"></a>

## 24.4 另请参阅（See also）

[日志 API（Logging API）](../log_core_reference/P002_日志公共接口.md)

> 译注——实现入口：[samples/boards/nordic/coresight_stm_shell/src/main.c](../../../samples/boards/nordic/coresight_stm_shell/src/main.c)与[samples/boards/nordic/coresight_stm_shell/prj.conf](../../../samples/boards/nordic/coresight_stm_shell/prj.conf)。仓库源码仅作参照，版本可能与本次官方页面不同；本地链接按文档位置相对解析。 配置依据见[本次上游 tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/coresight_stm_shell/tests.yaml)。

对应官方文档源码：[samples/boards/nordic/coresight_stm_shell/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/coresight_stm_shell/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nordic/coresight_stm_shell/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P023_CoreSight_STM基准测试.md) · [返回大纲](大纲.md) · [下一章](P025_动态引脚控制.md)
