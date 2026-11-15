---
id: learning.zephyr-docs.board-samples.page-85
title: MEC15xx板级电源管理测试
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/microchip/mec15xxevb_assy6853/power_management/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="mec15xx-sample-board-test-application"></a>

<a id="mec15xxevb-sample"></a>

# 第85章\_MEC15xx 示例板测试应用（MEC15xx sample board test application）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/microchip/mec15xxevb_assy6853/power_management/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 85.1 概述（Overview）

本示例展示基于 MEC15xx 的开发板的电源管理功能，应用可以进入浅睡眠（Light sleep）和深度睡眠（Deep sleep）。

> 译注——测试组合：main.c 依次运行单线程无日志、单线程有日志、多线程无日志、多线程有日志四组，各传入五次循环。浅睡眠和深度睡眠分别通过 PM_STATE_SUSPEND_TO_IDLE 与 PM_STATE_SUSPEND_TO_RAM 事件观察，不等于每块板的任意休眠模式都有相同行为。

<a id="building-and-running"></a>

## 85.2 构建与运行（Building and Running）

> 译注——执行前提：主机 west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行；先按[入门指南](../getting_started/大纲.md)准备工具、模块、工具链和具体板。调试器、双镜像及外部下载工具的目录要求分别按本页说明处理。本次未构建、烧录或执行硬件实验。

可通过 west 在开发板上构建并执行示例。除了使用 GPIO014 指示进入／退出之外，无需其他引脚配置。

> 译注——测量引脚：正文只提 GPIO014，但本次 power_mgmt.c 还使用 GPIO012、GPIO013 指示两种睡眠，注释列出了该 EVB 的跳线和探测位置。GPIO014 是应用触发标记；要接测量仪器，应按具体板布局检查源码所列引脚，不能把这些编号跨板照搬。原文没有给出具体 west 构建命令。

<a id="sample-output"></a>

### 85.2.1 输出示例（Sample output）

```text
Wake from Light Sleep
Wake from Deep Sleep
ResumeBBBAA
Wake from Light Sleep
Suspend...
Wake from Deep Sleep
ResumeBBBAA
```

注意（Note）：上面显示的数值可能不同。

> 译注——日志与延迟：Resume／Suspend 分别表示恢复／挂起，A／B 输出来自测试线程。源码比较进入／退出次数，并把异常记为警告；延迟阈值宏实际为 500 ms，旁边“低于300 ms”的注释较旧。串口输出会影响观察，日志出现不等同于功耗或延迟已达标。

> 译注——源码入口：[src/main.c](../../../samples/boards/microchip/mec15xxevb_assy6853/power_management/src/main.c)；[src/power_mgmt.c](../../../samples/boards/microchip/mec15xxevb_assy6853/power_management/src/power_mgmt.c)。仓库参照使用相对路径，版本可能与本次上游快照不同。

对应官方文档源码：[samples/boards/microchip/mec15xxevb_assy6853/power_management/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/microchip/mec15xxevb_assy6853/power_management/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/microchip/mec15xxevb_assy6853/power_management/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P084_Google示例目录.md) · [返回大纲](大纲.md) · [下一章](P086_MEC15xx参考板示例目录.md)
