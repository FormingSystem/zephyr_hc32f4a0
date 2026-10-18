---
id: learning.zephyr-docs.board-samples.page-29
title: nRF系统事件
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nordic/nrf_sys_event/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nrf-sys-event"></a>

# 第29章\_nRF 系统事件（nRF System Events）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nordic/nrf_sys_event/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nordic/nrf_sys_event/README.rst/..)

<a id="overview"></a>

## 29.1 概述（Overview）

本示例展示如何使用 `nrf_sys_event` API，在 Nordic Semiconductor SoC 上请求和释放全局恒定延迟模式（Global constant latency mode）。

> 译注——引用计数：两次 request 需要配对两次 release；第一次释放后模式仍启用，是因为还有未释放请求。启用强制恒定延迟配置时，硬件最终状态还受该配置约束，不能仅凭示例打印 disabled 就推断所有全局请求都已撤销。

示例执行以下步骤：

1. 请求全局恒定延迟模式。

2. 再次请求全局恒定延迟模式（引用计数增加）。

3. 释放全局恒定延迟模式——由于仍有未释放的请求，该模式保持启用。

4. 再次释放全局恒定延迟模式——此时该模式被禁用。

如果启用 [`CONFIG_NRF_SYS_EVENT_IRQ_LATENCY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_SYS_EVENT_IRQ_LATENCY)，示例还会在以下三种模式下测量访问 RRAMC（Resistive RAM Controller，电阻式 RAM 控制器）的中断延迟：

默认 RRAMC 模式（Default RRAMC mode）

RRAMC 进入低功耗状态，唤醒时间约为 15 µs。

由 PPI 唤醒 RRAMC（RRAMC woken by PPI）

使用 nrf_sys_event API，安排 PPI 在预期中断之前唤醒 RRAMC。

RRAMC 待机模式（RRAMC Standby mode）

使用 nrf_sys_event API，将 RRAMC 配置为唤醒时间为 0 µs。

> 译注——零微秒的含义：这里说的是 RRAMC 的唤醒时间，不是整个系统中断延迟为零。源码以 k_cycle_get_32() 测量等待闹钟的周期数，并进行十次平均；execution took 后的数值不能未经周期频率换算就当作微秒。

<a id="requirements"></a>

## 29.2 前提条件（Requirements）

本示例支持以下 Nordic Semiconductor 开发板目标：

- nrf52dk/nrf52810

- nrf52dk/nrf52832

- nrf52833dk/nrf52820

- nrf52833dk/nrf52833

- nrf52840dk/nrf52811

- nrf52840dk/nrf52840

- nrf5340dk/nrf5340/cpuapp

- nrf5340dk/nrf5340/cpunet

- nrf54h20dk/nrf54h20/cpuapp

- nrf54h20dk/nrf54h20/cpurad

- nrf54l15dk/nrf54l15/cpuapp

- nrf7120dk/nrf7120/cpuapp

<a id="building-and-running"></a>

## 29.3 构建与运行（Building and Running）

> 译注——执行前提：除本页另有说明的目录外，west 命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先准备[入门指南](../getting_started/大纲.md)所需的主机工具、west 工作区、模块与目标工具链；应用、配置及 overlay 为官方源码，构建目录由工具生成。构建成功后再按目标板文档烧录，失败时返回构建输出或板文档检查；下方日志是官方预期示例，本次未执行硬件步骤。

```text
west build -b nrf52840dk/nrf52840 samples/boards/nordic/nrf_sys_event
west flash
```

要测试从启动时就强制启用恒定延迟模式（[`CONFIG_SOC_NRF_FORCE_CONSTLAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF_FORCE_CONSTLAT)）：

```text
west build -b nrf52840dk/nrf52840 samples/boards/nordic/nrf_sys_event -- -DCONFIG_SOC_NRF_FORCE_CONSTLAT=y
west flash
```

要启用 RRAMC 的 IRQ 延迟测量（仅限 nrf54l15dk）：

> 译注——平台范围差异：原页把这一分支写为仅限 nrf54l15dk；本次 tests.yaml 的 RRAMC 场景还列出 nrf54lm20dk 的两个目标。保留原文，其他目标是否适用应以所用源码测试配置和设备树为准；不要把前面的全局恒定延迟支持列表直接套到 RRAMC 测量分支。

```text
west build -b nrf54l15dk/nrf54l15/cpuapp samples/boards/nordic/nrf_sys_event -- -DCONFIG_NRF_SYS_EVENT_IRQ_LATENCY=y
west flash
```

<a id="sample-output"></a>

## 29.4 输出示例（Sample Output）

```text
request global constant latency mode
constant latency mode enabled
request global constant latency mode again
release global constant latency mode
constant latency mode will remain enabled
release global constant latency mode again
constant latency mode will be disabled
constant latency mode disabled
```

> 译注——实现入口：[samples/boards/nordic/nrf_sys_event/src/main.c](../../../samples/boards/nordic/nrf_sys_event/src/main.c)与[samples/boards/nordic/nrf_sys_event/prj.conf](../../../samples/boards/nordic/nrf_sys_event/prj.conf)。仓库源码仅作参照，版本可能与本次官方页面不同；本地链接按文档位置相对解析。 配置依据见[本次上游 tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/nrf_sys_event/tests.yaml)。

对应官方文档源码：[samples/boards/nordic/nrf_sys_event/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/nrf_sys_event/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nordic/nrf_sys_event/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P028_Nordic_LED矩阵.md) · [返回大纲](大纲.md) · [下一章](P030_nrfx外设驱动示例.md)
