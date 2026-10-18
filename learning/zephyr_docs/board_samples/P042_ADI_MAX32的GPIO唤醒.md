---
id: learning.zephyr-docs.board-samples.page-42
title: ADI_MAX32的GPIO唤醒
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/adi/power_mgmt/gpio_wakeup/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="adi-gpio-wakeup"></a>

# 第42章\_ADI MAX32 的 GPIO 唤醒（ADI MAX32 GPIO Wakeup）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/adi/power_mgmt/gpio_wakeup/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/adi/power_mgmt/gpio_wakeup/README.rst/..)

<a id="overview"></a>

## 42.1 概述（Overview）

本示例展示如何在 MAX32 SoC 上使用 GPIO 将系统从低功耗状态唤醒。它将按钮配置为唤醒源（Wakeup source），然后依次进入每种受支持的电源管理（Power Management，PM）状态。长按按钮会使系统关闭。读者可以通过按下按钮，验证系统能否从各状态唤醒。

> 译注——按键与状态选择：本次源码对 sw0 使用带 GPIO_INT_WAKEUP 的有效沿中断，延后 200 ms 处理按键；长按判断阈值为 3000 ms。它锁住其他电源状态并等待按键信号量，唤醒后再转向下一项。这里的日志是待测试状态，实际功耗仍需要测量。

系统关闭后，设备只能通过复位按钮、重新上电或专用唤醒输入唤醒。专用唤醒输入见开发板设备树中的 `wk_pin`。如果该引脚没有连接按钮，需要手动将其短接到地，才能从关机状态唤醒系统。

> 译注——两种唤醒输入：sw0 是一般低功耗测试按钮，wk_pin 是 sys_poweroff() 前配置的专用唤醒引脚；它们不必是同一引脚。短接到地的步骤只针对原文指定的专用输入，先核对所用板原理图与设备树，不能把任意 GPIO 或电源引脚短接。

可以使用功耗分析工具（Power profiling tool），验证系统确实进入预期的低功耗状态，并在这些状态下消耗更低功率。

<a id="requirements"></a>

<a id="max32-pm-gpio-wakeup-sample-requirements"></a>

## 42.2 前提条件（Requirements）

开发板应支持电源管理，并具有可用作唤醒源的 GPIO。本示例的按钮由开发板设备树中的 `sw0` 别名定义，因此开发板必须定义该别名，并使它指向连接按钮的 GPIO 引脚。

<a id="building-and-running"></a>

## 42.3 构建与运行（Building and Running）

> 译注——执行前提：west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工具、工作区、模块和目标工具链；应用与 overlay 为官方源码，构建目录由工具生成。构建成功后按具体板文档处理下载与启动，不能把通用 west flash 视为所有板都采用同一种连接方式。失败时先检查构建输出、目标板配置和实际硬件；本次没有运行这些命令或进行实板测量。

按以下方式构建并烧录 gpio_wakeup，将 `max32655evkit` 替换为所用开发板：

```text
west build -b max32655evkit/max32655/m4 samples/boards/adi/power_mgmt/gpio_wakeup
west flash
```

<a id="pm-configurations"></a>

## 42.4 PM 配置（PM configurations）

默认启用 [`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_PM_POLICY_DEVICE_CONSTRAINTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_POLICY_DEVICE_CONSTRAINTS)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE) 和 [`CONFIG_PM_DEVICE_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME)。

本示例禁用延迟日志（Deferred logging），确保系统不会调度可能在低功耗状态下将其唤醒的延后处理工作。

> 译注——日志与延后工作不同：prj.conf 选择 CONFIG_LOG_MODE_IMMEDIATE，即立即模式日志，避免日志后台处理线程干扰观察；源码仍使用延后工作做按钮去抖。原文并不是说此应用完全不含延后工作，也不表示打开串口日志不会影响功耗。

> 译注——源码入口：[main.c](../../../samples/boards/adi/power_mgmt/gpio_wakeup/src/main.c)；[prj.conf](../../../samples/boards/adi/power_mgmt/gpio_wakeup/prj.conf)。本地参照实现使用相对路径，版本可能与本次网页不同。

对应官方文档源码：[samples/boards/adi/power_mgmt/gpio_wakeup/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/adi/power_mgmt/gpio_wakeup/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/adi/power_mgmt/gpio_wakeup/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P041_BBC示例目录.md) · [返回大纲](大纲.md) · [下一章](P043_ADI电源模式.md)
