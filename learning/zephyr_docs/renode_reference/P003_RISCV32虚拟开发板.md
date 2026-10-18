---
id: learning.zephyr-docs.renode-reference.page-3
title: RISCV32虚拟开发板
kind: reference
status: maintained
domains: [zephyr, boards, simulation]
source_url: https://docs.zephyrproject.org/latest/boards/renode/riscv32_virtual/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_RISC-V 32位虚拟开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/renode/riscv32_virtual/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="riscv32_virtual"></a>


开发板名称：`riscv32_virtual`。厂商分类：[Antmicro的开源模拟与虚拟开发框架](https://docs.zephyrproject.org/latest/boards/index.html#vendor=renode)。维护状态：未积极维护（Not Actively Maintained）。架构（Architecture）：[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)；片上系统（SoC）：[riscv_virtual_renode](https://docs.zephyrproject.org/latest/boards/index.html#soc=riscv_virtual_renode)。

<a id="board-github-link"></a>

[浏览开发板源码](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renode/riscv32_virtual)。

<a id="overview"></a>

## 3.1\_概述

RISCV32 Virtual 是用 Renode 构建的虚拟平台（Virtual Platform），提供 QEMU 之外的另一种选择。原文指出，相比 QEMU，此平台可以方便地通过修改 `riscv32_virtual.repl` 脚本并相应调整设备树（Devicetree）文件来配置外设，从而在上游持续集成（Continuous Integration，CI）中测试某些仅存在于专有开发板／SoC中的硬件配置。

<a id="programming-and-debugging"></a>

## 3.2\_编程与调试

原文在此声明该开发板支持下表列出的运行器（Runner）与对应 west 命令。官方生成表只有 `flash`、`debug` 列标题，表体为空，没有提供具体运行器条目。

| 运行器 | `west flash` | `west debug` |
| --- | --- | --- |

<a id="building"></a>

## 3.3\_构建

此开发板配置的应用可以按通常方式构建，见[构建应用](../application/P001_应用开发.md#build-an-application)：

```shell
west build -b riscv32_virtual
```

<a id="flashing"></a>

## 3.4\_烧录与模拟运行

此开发板由软件仿真，不能实际“烧录”（Flashing），但可以用该配置在 Renode 仿真环境中运行基础 Zephyr 应用与内核测试。例如，运行[基础同步示例（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)：

```shell
# From the root of the zephyr repository
west build -b riscv32_virtual samples/synchronization
west build -t run
```

代码注释表示从 Zephyr 仓库根目录执行。命令会构建包含同步示例应用的镜像（Image），用 Renode 启动，并显示下列控制台输出（Console Output）：

```text
*** Booting Zephyr OS build zephyr-v3.5.0-1511-g56f73bde0fb0 ***
thread_a: Hello World from cpu 0 on riscv32_virtual!
thread_b: Hello World from cpu 0 on riscv32_virtual!
thread_a: Hello World from cpu 0 on riscv32_virtual!
thread_b: Hello World from cpu 0 on riscv32_virtual!
```

输出是官方给出的示例，版本字符串与内容原样保留。按 `CTRL+C` 退出 Renode。

<a id="debugging"></a>

## 3.5\_调试

详细说明见[应用调试](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

---

[上一章](P002_Cortex_R8虚拟开发板.md) · [本册大纲](大纲.md) · [全站进度](../PROGRESS.md)
