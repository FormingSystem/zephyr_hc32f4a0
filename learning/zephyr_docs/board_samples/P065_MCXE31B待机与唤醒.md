---
id: learning.zephyr-docs.board-samples.page-65
title: MCXE31B待机与唤醒
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nxp/frdm_mcxe31b/system_off/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="frdm-mcxe31b-system-off"></a>

# 第65章\_系统关闭：MCXE31B 待机（System Off: MCXE31B standby）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nxp/frdm_mcxe31b/system_off/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nxp/frdm_mcxe31b/system_off/README.rst/..)

<a id="overview"></a>

## 65.1 概述（Overview）

本示例展示如何在 NXP FRDM-MCXE31B 开发板上使用 [`sys_poweroff()`](../power/P063_系统关机接口.md#gaf4552a8ea40b4adb94f85b0a1ff06e39)。

与提供可恢复挂起状态的 SoC 不同，MCXE31B 唯一的低功耗模式是待机（Standby），且采用唤醒后复位（Reset-on-wake）的方式：运行电源域关闭，唤醒事件触发功能复位（Functional reset）。因此，应用将待机建模为系统关闭，而不是 Zephyr PM 挂起状态。

示例将 RTC 闹钟设为唤醒源，关闭 SoC，随后由 RTC 闹钟唤醒并重新启动开发板。下一次启动时，示例报告从待机唤醒，并从待机保持的 noinit 内存读取循环计数。该过程重复 `CONFIG_APP_TEST_CYCLES` 次，默认十次。

> 译注——保持与初始化：noinit 表示启动时不由 C 运行时清零，不等于普通 SRAM 自动具备掉电保持能力。源码把计数放入 stdby_ram 专用段，更新后刷新数据缓存；从待机唤醒保留计数，其他启动先置零。RTC 即实时时钟（Real-Time Clock）。

<a id="requirements"></a>

## 65.2 前提条件（Requirements）

FRDM-MCXE31B 开发板，并连接串口控制台。

<a id="building-and-running"></a>

## 65.3 构建与运行（Building and Running）

> 译注——执行前提：west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行；先按[入门指南](../getting_started/大纲.md)准备工具链、模块及对应板。构建产物由工具生成，下载与启动按具体板文档核对。本次未执行构建、烧录或硬件测量。

```text
west build -b frdm_mcxe31b samples/boards/nxp/frdm_mcxe31b/system_off
west flash
```

<a id="sample-output"></a>

### 65.3.1 输出示例（Sample Output）

```text
Cold boot
Powering off in 3 s...
Powering off in 2 s...
Powering off in 1 s...
Wake-up alarm set for 5 seconds (cycle 1/10)
Powering off

*** Booting Zephyr OS ***
Woke from standby
Retained standby cycle count: 1/10
Powering off in 3 s...
Powering off in 2 s...
Powering off in 1 s...
Wake-up alarm set for 5 seconds (cycle 2/10)
Powering off
...

*** Booting Zephyr OS ***
Woke from standby
Retained standby cycle count: 10/10
Completed 10 standby cycles
```

开发板关闭后，RTC 闹钟在五秒后将其唤醒，启动横幅再次出现；这是复位，不是从暂停位置恢复。待机保持的 noinit 计数器使示例在完成配置的待机循环次数后停止。

> 译注——时间与回调：每轮在设置闹钟前先留出三秒恢复窗口，再设置五秒唤醒。闹钟回调仅满足计数器 API 参数要求，待机唤醒实际通过复位重新执行 main()，不会从这个回调继续运行。Completed 日志才表示计数达到目标。

<a id="see-also"></a>

## 65.4 另请参阅（See also）

[系统关闭（System power off）](../power/P063_系统关机接口.md)

[计数器（Counter）](../timer_reference/P022_计数器公共接口.md)

> 译注——源码入口：仓库相对参照：[src/main.c](../../../samples/boards/nxp/frdm_mcxe31b/system_off/src/main.c)；[prj.conf](../../../samples/boards/nxp/frdm_mcxe31b/system_off/prj.conf)。本地版本可能与网页不同。

对应官方文档源码：[samples/boards/nxp/frdm_mcxe31b/system_off/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nxp/frdm_mcxe31b/system_off/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nxp/frdm_mcxe31b/system_off/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P064_Intel示例目录.md) · [返回大纲](大纲.md) · [下一章](P066_RW612低功耗Flash擦写检查.md)
