---
id: learning.zephyr-docs.board-samples.page-43
title: ADI电源模式
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/adi/power_mgmt/power_modes/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="adi-pm"></a>

# 第43章\_ADI 电源模式（ADI Power Modes）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/adi/power_mgmt/power_modes/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/adi/power_mgmt/power_modes/README.rst/..)

<a id="overview"></a>

## 43.1 概述（Overview）

ADI PM 示例运行指定 SoC 的各种电源模式，用于演示与功耗测量。

`prj.conf` 展示启用电源管理所需的 Kconfig 配置；设备树覆盖文件（Devicetree overlay）展示如何按存储体（Memory bank）配置 RAM 保持（RAM retention）。

> 译注——保持范围：RAM 保持用于指定低功耗模式下保留所选 SRAM 存储体内容，不能代替断电后的非易失存储。本次 max32657 overlay 在 sram0 上设置 adi,ram-bank-retained，实际范围以对应 SoC 的存储体定义为准。

<a id="requirements"></a>

## 43.2 前提条件（Requirements）

开发板应支持电源管理，并具有可用作系统定时器伴随设备（System timer companion）的计数器设备。

<a id="building-and-running"></a>

## 43.3 构建与运行（Building and Running）

> 译注——执行前提：west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工具、工作区、模块和目标工具链；应用与 overlay 为官方源码，构建目录由工具生成。构建成功后按具体板文档处理下载与启动，不能把通用 west flash 视为所有板都采用同一种连接方式。失败时先检查构建输出、目标板配置和实际硬件；本次没有运行这些命令或进行实板测量。

按以下方式构建并烧录 ADI 电源模式示例：

```text
west build -b max32657evkit/max32657 samples/boards/adi/power_mgmt/power_modes
west flash
```

烧录后，应用通过每次休眠至少达到相应模式要求的最小驻留时间（Minimum residency time），反复遍历设备树定义的全部电源模式。

> 译注——源码中的休眠时间：示例实际使用 min_residency_us + exit_latency_us + 100 微秒，先以忙等方式闪烁 LED，再调用 k_usleep() 让电源策略有机会选择状态；它没有逐项调用强制状态 API。实际状态还受就绪设备、约束与策略影响，LED 闪烁和请求的休眠时长不足以证明功耗指标。

提示：

- 测试电源模式或为设备启用 PM 时，建议启用 [`CONFIG_BOOT_DELAY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOOT_DELAY)，避免调试器无法接入。

> 译注——配置类型与当前示例：CONFIG_BOOT_DELAY 是以毫秒为单位的整数启动延迟，不是赋值 y/n 的布尔开关。本次 prj.conf 实际配置的是 CONFIG_MAX32_STANDBY_DELAY=1000，用于开机后一段时间内阻止进入待机；它与通用启动延迟不是同一个配置。原文建议保留，使用时按目的选择。

> 译注——源码入口：[main.c](../../../samples/boards/adi/power_mgmt/power_modes/src/main.c)；[prj.conf](../../../samples/boards/adi/power_mgmt/power_modes/prj.conf)。本地参照实现使用相对路径，版本可能与本次网页不同。

对应官方文档源码：[samples/boards/adi/power_mgmt/power_modes/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/adi/power_mgmt/power_modes/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/adi/power_mgmt/power_modes/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P042_ADI_MAX32的GPIO唤醒.md) · [返回大纲](大纲.md) · [下一章](P044_ADI示例目录.md)
