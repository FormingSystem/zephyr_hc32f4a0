---
id: learning.zephyr-docs.hardware.pwmsamp-2
title: PWM事件示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/pwm/event/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="event"></a>

# 第170章\_PWM事件示例

原文：[PWM Event](https://docs.zephyrproject.org/latest/samples/drivers/pwm/event/README.html)。读取日期：2026-10-13，`latest`。

## 170.1\_概述（Overview）

本示例使用 **脉冲宽度调制（Pulse Width Modulation，PWM）**的事件 **应用程序编程接口（Application Programming Interface，API）**，获取 PWM 信号上的事件。

示例展示如何通过事件精确控制 PWM 信号的若干个周期。例如，**红外（Infrared，IR）**遥控器的发送部分需要精确的脉冲时序（Pulse Timing），可以使用这种机制。

## 170.2\_要求（Requirements）

平台的 PWM 驱动必须支持事件 API。

## 170.3\_构建与运行（Building and Running）

译注：在已配置 Zephyr 开发环境的终端中，从 Zephyr 源码根目录执行下列官方命令。示例源码由官方仓库提供；第一条命令生成构建产物，第二条调用该目标的 `run` 构建目标。

```bash
west build -b sam4s_xplained samples/drivers/pwm/event
west build -t run
```

## 170.4\_示例输出（Sample Output）

使用示波器（Oscilloscope）或逻辑分析仪（Logic Analyzer）捕获信号时，在启动瞬态（Startup Transient）结束后，应观察到如下重复序列：

```text
 ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐                   ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐
─┘ └─┘ └─┘ └─┘ └─┘ └───────────────────┘ └─┘ └─┘ └─┘ └─┘ └─────
```

译注：这里保留原文的字符波形图；它是文本代码块，不是单独的图片文件。

## 170.5\_相关资料

[PWM接口](P255_PWM公共接口.md) · [官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/pwm/event)

[上一章：PWM输入捕获示例](P169_PWM输入捕获示例.md) · [下一章：显示驱动示例](P171_显示驱动示例.md) · [返回大纲](大纲.md)
