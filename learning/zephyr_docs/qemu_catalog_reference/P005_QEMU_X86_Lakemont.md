---
id: learning.zephyr-docs.qemu-catalog-reference.page-5
title: QEMU_X86_Lakemont
kind: reference
status: maintained
domains: [zephyr, boards, qemu]
source_url: https://docs.zephyrproject.org/latest/boards/qemu/x86_lakemont/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_QEMU\_X86\_Lakemont

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/qemu/x86_lakemont/doc/index.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="qemu_x86_lakemont"></a>

## 5.1\_开发板概况与概述

名称：`qemu_x86_lakemont`。厂商：[Intel Corporation](https://docs.zephyrproject.org/latest/boards/index.html#vendor=intel)。状态：未积极维护（Not Actively Maintained）。架构（Architecture）：[x86](https://docs.zephyrproject.org/latest/boards/index.html#arch=x86)；片上系统（SoC）：[lakemont](https://docs.zephyrproject.org/latest/boards/index.html#soc=lakemont)。

<a id="board-github-link"></a>

[浏览开发板源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/boards/qemu/x86_lakemont)。

<a id="overview"></a>

X86 Lakemont QEMU 开发板配置用于仿真 Quark 系列 SoC 中的 Intel Lakemont（Minute IA）CPU。

基于 Lakemont 的硬件目标既没有基本输入输出系统（BIOS），也没有高级配置与电源接口（ACPI）；QEMU 则提供兼容个人计算机（PC-compatible）的虚拟机器。因此，本配置提供高精度事件定时器（HPET）、高级可编程中断控制器（APIC）和 NS16550 UART。

<a id="hardware"></a>

## 5.2\_硬件

<a id="supported-features"></a>

<a id="qemu_x86_lakemont-hw-features"></a>

`qemu_x86_lakemont` 的硬件特性（Supported Features）及图例如下。片上（on-chip）表示集成在 SoC 内，板上（on-board）表示位于开发板。启用／禁用数字保留相应实例数量，链接指向开发板或 SoC 设备树源码（DTS）中该状态的第一个实例；兼容字符串（Compatible String，如 `vnd,foo`）链接指向绑定文档。

CPU 为中央处理器，UART 为通用异步收发器；RAM 为随机存取存储器，Flash 为闪存；KiB、MiB 为二进制千字节和兆字节。

原页未列出具体构建目标或硬件特性表行。

<a id="programming-and-debugging"></a>

## 5.3\_编程与调试

原页列出 `qemu_x86_lakemont` 支持的运行器（Runner）及关联 west 命令：

| 运行器 | `west flash` | `west debug` |
| --- | --- | --- |

原页表体为空，未列出运行器或默认值。

应用可按仿真开发板的通常方式构建和运行，详见[构建应用](../application/P001_应用开发.md#build-an-application)和[运行应用](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)。

<a id="flashing"></a>

虽然该开发板是仿真的，不能实际“烧写”（Flash），但可用此配置运行基本 Zephyr 应用及内核测试。

以[基础同步示例（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)为例，下面的命令从 Zephyr 仓库根目录执行，原代码注释也表示这一位置。

```shell
# From the root of the zephyr repository
west build -b qemu_x86_lakemont samples/synchronization
west build -t run
```

按 `CTRL+A`，再按 `x` 退出 QEMU。

<a id="debugging"></a>

详细概述参见[应用调试](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

> 译注：命令、日志和版本号按官方示例保留，本次翻译未构建或运行固件。

---

[上一章](P004_QEMU_X86_64位.md) · [本册大纲](大纲.md) · [全站进度](../PROGRESS.md) · [下一章](P006_QEMU_Xtensa.md)
