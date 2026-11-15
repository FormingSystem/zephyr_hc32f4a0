---
id: learning.zephyr-docs.hardware.pwmsamp-1
title: PWM输入捕获示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/pwm/capture/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="capture"></a>

# 第169章\_PWM输入捕获示例

原文：[PWM Capture](https://docs.zephyrproject.org/latest/samples/drivers/pwm/capture/README.html)。读取日期：2026-10-13，`latest`。

## 169.1\_概述（Overview）

本示例使用 **脉冲宽度调制（Pulse Width Modulation，PWM）**的捕获 **应用程序编程接口（Application Programming Interface，API）**，测量外部 PWM 信号的周期（Period）和脉冲宽度（Pulse Width）。

## 169.2\_要求（Requirements）

硬件必须具有与 PWM 捕获模块兼容的定时器 **硬件知识产权核（Intellectual Property Core，IP Core）**支持。

## 169.3\_构建与运行（Building and Running）

译注：在已配置 Zephyr 开发环境的终端中，从 Zephyr 源码根目录执行以下官方命令。示例源码由官方仓库提供；第一条命令生成构建产物，第二条调用该目标的 `run` 构建目标。

```bash
west build -b lp_mspm0g3507 samples/drivers/pwm/capture
west build -t run
```

## 169.4\_示例输出（Sample Output）

以下为原文日志。TIMCLK 表示定时器时钟（Timer Clock），占空比（Duty Cycle）是脉冲宽度占周期的比例；`<repeats endlessly>` 表示持续重复。

```text
PWM capture lp_mspm0g3507/mspm0g350

timclk 80000000 Hz
{period:1000  pulse width: 499} in TIMCLK cycle
{period: 80000.000000 Hz duty: 49.900002}

<repeats endlessly>
```

译注：原日志最后一行把以 `Hz` 为单位的数值标为 `period`，此处保留原样。根据上一行的 80 MHz 定时器时钟和 1000 个时钟周期，80,000 Hz 对应的是频率；499/1000 对应 49.9% 的占空比。

## 169.5\_相关资料

[PWM接口](P255_PWM公共接口.md) · [官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/pwm/capture)

[上一章：PWM示例目录](P168_PWM示例目录.md) · [下一章：PWM事件示例](P170_PWM事件示例.md) · [返回大纲](大纲.md)
