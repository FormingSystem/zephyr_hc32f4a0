---
id: learning.zephyr-docs.board-samples.page-72
title: FLEXRAM魔术地址
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nxp/mimxrt1170_evk_cm7/magic_addr/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="flexram_magic_addr"></a>

# 第72章\_FLEXRAM 魔术地址（FLEXRAM magic address）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nxp/mimxrt1170_evk_cm7/magic_addr/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nxp/mimxrt1170_evk_cm7/magic_addr/README.rst/..)

<a id="overview"></a>

## 72.1 概述（Overview）

本示例展示如何使用 RT11XX FLEXRAM 的魔术地址（Magic Addr）功能。

Magic Addr 是 FlexRAM 的一项功能，可配置在访问任意 RAM／TCM 地址时触发中断。本示例展示如何通过 Zephyr 中 FlexRAM 的专用 API 使用该功能。

> 译注——地址范围：TCM 为紧耦合存储器（Tightly Coupled Memory），DTCM 为数据紧耦合存储器（Data TCM）。本例把 var 放入 __dtcm_bss_section，再将其地址设为监测目标；驱动会检查地址是否落在设备树描述的 DTCM 区域。因此“任意地址”不表示可以监测整个 MCU 地址空间。

<a id="building-and-running"></a>

## 72.2 构建与运行（Building and Running）

参见开发板文档。

> 译注——实际交互：官方这一节未给出构建命令。源码先注册回调并初始化控制台，每收到一个字符，就写入 var，等待一次 DTCM 地址事件，再读取并等待第二次事件；回调递增 cnt 并释放信号量。它演示访问触发中断，不是 RAM 容量或数据完整性测试。

> 译注——源码入口：仓库相对参照：[src/main.c](../../../samples/boards/nxp/mimxrt1170_evk_cm7/magic_addr/src/main.c)；[prj.conf](../../../samples/boards/nxp/mimxrt1170_evk_cm7/magic_addr/prj.conf)；[drivers/misc/nxp_flexram/nxp_flexram.c](../../../drivers/misc/nxp_flexram/nxp_flexram.c)。本地版本可能与网页不同。

对应官方文档源码：[samples/boards/nxp/mimxrt1170_evk_cm7/magic_addr/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nxp/mimxrt1170_evk_cm7/magic_addr/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nxp/mimxrt1170_evk_cm7/magic_addr/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P071_RT700系统关闭.md) · [返回大纲](大纲.md) · [下一章](P073_SmartDMA内存到内存传输.md)
