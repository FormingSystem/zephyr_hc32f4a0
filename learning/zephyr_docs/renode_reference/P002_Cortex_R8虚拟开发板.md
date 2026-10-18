---
id: learning.zephyr-docs.renode-reference.page-2
title: Cortex_R8虚拟开发板
kind: reference
status: maintained
domains: [zephyr, boards, simulation]
source_url: https://docs.zephyrproject.org/latest/boards/renode/cortex_r8_virtual/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_Cortex-R8虚拟开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/renode/cortex_r8_virtual/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="cortex_r8_virtual"></a>


开发板名称：`cortex_r8_virtual`。厂商分类：[Antmicro的开源模拟与虚拟开发框架](https://docs.zephyrproject.org/latest/boards/index.html#vendor=renode)。维护状态：未积极维护（Not Actively Maintained）。架构（Architecture）：[arm](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm)；片上系统（SoC）：[cortex_r8_virtual](https://docs.zephyrproject.org/latest/boards/index.html#soc=cortex_r8_virtual)。

<a id="board-github-link"></a>

[浏览开发板源码](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renode/cortex_r8_virtual)。

<a id="overview"></a>

## 2.1\_概述

Cortex-R8 Virtual 是可由 Renode 仿真的虚拟平台（Virtual Platform）。编辑 [boards/renode/cortex_r8_virtual/support/cortex_r8_virtual.repl](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renode/cortex_r8_virtual/support/cortex_r8_virtual.repl) 文件，可按需求调整平台布局（Platform Layout）。

如何为宿主系统获取 Renode，见 [Renode 文档](https://renode.readthedocs.io/en/latest/)。

<a id="programming-and-debugging"></a>

## 2.2\_编程与调试

原文在此声明该开发板支持下表列出的运行器（Runner）与对应 west 命令。官方生成表只有 `flash`、`debug` 列标题，表体为空，没有提供具体运行器条目。

| 运行器 | `west flash` | `west debug` |
| --- | --- | --- |

<a id="building"></a>

## 2.3\_构建

此目标的应用可按标准构建流程生成，见[构建应用](../application/P001_应用开发.md#build-an-application)：

```shell
west build -b cortex_r8_virtual
```

<a id="flashing"></a>

## 2.4\_烧录与模拟运行

软件运行于模拟环境，不需要传统意义上的“烧录”（Flashing）。使用此开发板配置和 `run` 命令，可以直接在 Renode 中运行 Zephyr 应用与内核测试。例如，运行[基础同步示例（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)：

```shell
# From the root of the zephyr repository
west build -b cortex_r8_virtual samples/synchronization
west build -t run
```

代码注释表示从 Zephyr 仓库根目录执行。命令会构建包含同步示例应用的镜像（Image），用 Renode 启动，并显示下列控制台输出（Console Output）：

```text
*** Booting Zephyr OS build v3.6.0-5689-g2a5c606abfa7 ***
thread_a: Hello World from cpu 0 on cortex_r8_virtual!
thread_b: Hello World from cpu 0 on cortex_r8_virtual!
thread_a: Hello World from cpu 0 on cortex_r8_virtual!
thread_b: Hello World from cpu 0 on cortex_r8_virtual!
```

输出是官方给出的示例，版本字符串与内容原样保留。按 `CTRL+C` 退出 Renode。

<a id="debugging"></a>

## 2.5\_调试

详细说明见[应用调试](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

Renode 可以作为 GDB 调试服务器（GDB Server），更多信息见 [Renode 的 GDB 调试文档](https://renode.readthedocs.io/en/latest/debugging/gdb.html)。

---

[上一章](P001_Renode目录.md) · [本册大纲](大纲.md) · [全站进度](../PROGRESS.md) · [下一章](P003_RISCV32虚拟开发板.md)
