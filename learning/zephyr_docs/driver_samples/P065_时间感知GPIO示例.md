---
id: learning.zephyr-docs.driver_samples.page-65
title: 时间感知GPIO示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/timeaware_gpio/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="timeaware-gpio"></a>

# 第65章\_时间感知GPIO示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/timeaware_gpio/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 65.1 概述（Overview）

本示例应用可以用于任何支持它的开发板，例如RPL。它把配置信息打印到控制台，并测试以下功能：

- 产生周期脉冲（可能需要示波器或回环连接）。
- 为输入脉冲记录时间戳（可能需要脉冲发生器或回环连接）。

> 译注——功能定位：时间感知通用输入输出（Time-aware General-Purpose Input/Output，TGPIO）把引脚事件与硬件时间联系起来。此处“支持的开发板”要求具备对应TGPIO设备和配置，不能仅因支持普通GPIO就认为适用。

<a id="building-and-running"></a>

## 65.2 构建与运行（Building and Running）

可以按以下方式构建本应用：

```sh
# From the root of the zephyr repository
west build -b intel_rpl_crb samples/drivers/timeaware_gpio
```

若为另一块受支持的开发板构建，将`intel_rpl_crb`替换为该板名称（前提是它确实受支持）。

> 译注——构建与执行：上面的原命令只构建固件；原文没有在此给出部署或运行命令。当前官方[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/timeaware_gpio/src/main.c)使用设备树节点标签`tgpio`、输入引脚0和输出引脚1。它读取当前时间及每秒周期数，把首次输出安排在约一秒后，以一秒对应的周期数设置周期输出，并每500毫秒读取时间戳与事件计数。物理引脚映射及回环接线须依据目标板资料，不能把逻辑编号直接当作连接器脚号。

<a id="sample-output"></a>

### 65.2.1 示例输出（Sample Output）

以下为原页面记录的输出，时间戳、事件计数及构建版本按原样保留：

```text
*** Booting Zephyr OS build zephyr-v3.4.0-4166-g52b34a310c67 ***
[TGPIO] Bind Success
[TGPIO] Time now: 00000001477ed72f
[TGPIO] Running rate: 19200000
[TGPIO] Periodic pulses start at: 0000000148a3cf2f
[TGPIO] timestamp: 0000000000000000, event count: 0000000000000000
[TGPIO] timestamp: 0000000148a3cf31, event count: 0000000000000001
[TGPIO] timestamp: 0000000149c8c731, event count: 0000000000000002
[TGPIO] timestamp: 000000014aedbf31, event count: 0000000000000003
[TGPIO] timestamp: 000000014c12b731, event count: 0000000000000004
[TGPIO] timestamp: 000000014d37af31, event count: 0000000000000005
[TGPIO] timestamp: 000000014e5ca731, event count: 0000000000000006
[TGPIO] timestamp: 000000014f819f31, event count: 0000000000000007
[TGPIO] timestamp: 0000000150a69731, event count: 0000000000000008
[TGPIO] timestamp: 0000000151cb8f31, event count: 0000000000000009
[TGPIO] timestamp: 0000000152f08731, event count: 000000000000000a
[TGPIO] timestamp: 0000000154157f31, event count: 000000000000000b
```

<a id="see-also"></a>

## 65.3 另请参阅（See also）

- [时间感知GPIO（Time-aware GPIO）](../timer_reference/P191_时间感知GPIO公共接口.md)。


对应官方文档源码：[samples/drivers/timeaware_gpio/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/timeaware_gpio/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/timeaware_gpio/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/timeaware_gpio/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P064_RISC_V_AIA多处理器中断示例.md) · [返回大纲](大纲.md) · [下一章](P066_虚拟化示例目录.md)
