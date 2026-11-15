---
id: learning.zephyr-docs.board-samples.page-45
title: Renesas事件链接控制器
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/renesas/elc/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="renesas-elc"></a>

# 第45章\_Renesas ELC 示例（Renesas ELC Sample）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/renesas/elc/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/renesas/elc/README.rst/..)

<a id="overview"></a>

## 45.1 概述（Overview）

本示例展示在基于 Zephyr 的系统中，将 Renesas 事件链接控制器（Event Link Controller，ELC）与脉宽调制（Pulse Width Modulation，PWM）功能集成。

示例从设备树初始化 PWM 发生器、PWM 捕获设备与 ELC 设备。随后配置 PWM 发生器，通过捕获验证信号；再使用 ELC 停止发生器，并通过捕获超时验证停止操作；最后使用 ELC 重新启动发生器，确认控制流程符合预期。

> 译注——验证链：源码设置周期 1000000 ns、脉宽 500000 ns，即 1 kHz、50% 占空比。先确认能捕获，停止事件后才把 -EAGAIN 超时当作预期结果，最后再次启动并要求周期误差不超过 1%。一开始就捕获超时不能证明 ELC 停止成功。

<a id="hardware-setup"></a>

## 45.2 硬件设置（Hardware Setup）

- 开发板要求：

  - 至少一个 PWM 输出通道。

  - 至少一个 PWM 捕获通道。

  - 设备树中具有 Renesas ELC 节点。

- 接线：

  - 必须将 PWM 输出引脚连接到 PWM 捕获引脚，示例才能通过捕获来验证产生的信号。

> 译注——设备树与线路：应用使用 pwm-gen、pwm-cap、elc-link 三个别名。ek_ra8m1 overlay 将 ELC 软件事件 0／1 分别连接到发生器的 start／stop，并选择 PWM7 与 PWM9；这些不是跨所有 Renesas 板通用的通道或引脚号。需按所选板的 overlay 与引脚定义连接实际输出和捕获输入。

  - 查阅所用开发板文档或设备树，确认正确的引脚并保证连接无误。

<a id="building-and-running"></a>

## 45.3 构建与运行（Building and Running）

> 译注——执行前提：west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工具、工作区、模块和目标工具链；应用与 overlay 为官方源码，构建目录由工具生成。构建成功后按具体板文档处理下载与启动，不能把通用 west flash 视为所有板都采用同一种连接方式。失败时先检查构建输出、目标板配置和实际硬件；本次没有运行这些命令或进行实板测量。

为 [RA8M1 评估套件（RA8M1 Evaluation Kit）](https://docs.zephyrproject.org/latest/boards/renesas/ek_ra8m1/doc/index.html#ek_ra8m1)构建并烧录本示例：

```text
west build -b ek_ra8m1 samples/boards/renesas/elc
west flash
```

对于其他受支持的开发板，相应替换 `ek_ra8m1`。

<a id="sample-output"></a>

### 45.3.1 输出示例（Sample Output）

预期控制台输出：

> 译注——日志单位：generator 为发生器，capture 为捕获，period 为周期，pulse 为有效脉宽，ns 为纳秒。原始设备地址与捕获值保留，不要求其他板的设备名和数值完全一致；应核对配置、停止和重启三阶段均满足源码判据。

```text
*** Booting Zephyr OS build a187e16d5baa ***
PWM generator device: pwm7@40322700
PWM capture device: pwm9@40322900
ELC device: elc@40201000

PWM generator configured: period=1000000 ns, pulse=500000 ns
PWM captured: period=999991 ns

Generate ELC software event to stop PWM generator.
PWM generator stopped by the ELC link as expected.

Generate ELC software event to start PWM generator.
PWM captured: period=999991 ns
PWM generator started by the ELC link as expected.
```

> 译注——源码入口：[main.c](../../../samples/boards/renesas/elc/src/main.c)；[prj.conf](../../../samples/boards/renesas/elc/prj.conf)。本地参照实现使用相对路径，版本可能与本次网页不同。

对应官方文档源码：[samples/boards/renesas/elc/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/renesas/elc/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/renesas/elc/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P044_ADI示例目录.md) · [返回大纲](大纲.md) · [下一章](P046_Renesas低电压检测.md)
