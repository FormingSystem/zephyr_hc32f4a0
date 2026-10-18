---
id: learning.zephyr-docs.board-samples.page-83
title: USB电力传输分析器
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/google/twinkie_v2/pda/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="twinkie_v2_pda"></a>

# 第83章\_电力传输分析器（Power Delivery Analyzer）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/google/twinkie_v2/pda/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/google/twinkie_v2/pda/README.rst/..)

<a id="overview"></a>

## 83.1 概述（Overview）

本示例提供对 [Twinkie V2](https://docs.zephyrproject.org/latest/boards/google/twinkie_v2/doc/index.html#google_twinkie_v2) 的访问，以便尝试其支持的功能。

> 译注——功能范围：Power Delivery 指 USB 电力传输（USB Power Delivery，USB PD）。此示例通过 ADC、分压与电流检测放大器测量 VBUS，并控制 LED，没有在正文中提供完整 PD 协议报文分析或协商解码流程；main() 实际在 src/view.c。

<a id="building-and-running"></a>

## 83.2 构建与运行（Building and Running）

> 译注——执行前提：主机 west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行；先按[入门指南](../getting_started/大纲.md)准备工具、模块、工具链和具体板。调试器、双镜像及外部下载工具的目录要求分别按本页说明处理。本次未构建、烧录或执行硬件实验。

按以下方式构建并烧录 Twinkie：

> 译注——采样与错误：源码每轮休眠 500 微秒，但一次循环还包含 ADC 转换和 LED 操作，不能据此宣称精确 2 kHz 采样。view.c 未检查测量函数返回值，异常时颜色也可能基于旧值；本次没有连接电源或测量设备。

```text
west build -b google_twinkie_v2 samples/boards/google/twinkie_v2/pda
west flash
```

烧录后，LED 初始显示红色。把 Twinkie 串接到 USB-C 连接中后，LED 变蓝；如果设备正在充电，LED 则显示绿色。

> 译注——实际判断：本次 view.c 在 VBUS 电压严格大于 5000 mV 时，才继续按电流判断；电流严格大于 1000 mA 显示绿，否则蓝，电压不满足则红。因此低于阈值的实际充电可能不显示绿色，不能把颜色当作所有 USB-C／USB PD 设备通用的充电状态判定。

<a id="see-also"></a>

## 83.3 另请参阅（See also）

[模数转换器（Analog-to-Digital Converter，ADC）](../hardware/P463_ADC公共接口参考.md)

> 译注——源码入口：[src/view.c](../../../samples/boards/google/twinkie_v2/pda/src/view.c)；[src/meas.c](../../../samples/boards/google/twinkie_v2/pda/src/meas.c)；[src/meas.h](../../../samples/boards/google/twinkie_v2/pda/src/meas.h)。仓库参照使用相对路径，版本可能与本次上游快照不同。

对应官方文档源码：[samples/boards/google/twinkie_v2/pda/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/google/twinkie_v2/pda/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/google/twinkie_v2/pda/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P082_ARC安全服务.md) · [返回大纲](大纲.md) · [下一章](P084_Google示例目录.md)
