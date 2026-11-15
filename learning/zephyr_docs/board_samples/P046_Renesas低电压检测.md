---
id: learning.zephyr-docs.board-samples.page-46
title: Renesas低电压检测
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/renesas/lvd/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="renesas_lvd"></a>

# 第46章\_使用比较器的 Renesas 低电压检测示例（Renesas Low-voltage Detection Sample using Comparator）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/renesas/lvd/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/renesas/lvd/README.rst/..)

<a id="overview"></a>

## 46.1 概述（Overview）

本示例展示如何通过比较器（Comparator）使用 Renesas 低电压检测（Low-voltage Detection，LVD）功能监测电压。

> 译注——检测目标：本次 RX LVD 绑定可选择 Vcc 或受支持的 CMPA 模拟输入，并非所有通道都支持外部 CMPA。使用外部引脚时，需要对应 pinctrl 与模拟输入设置；应用本身不提供测试电压，接线与电压范围以所用板和芯片要求为准。

<a id="hardware-setup"></a>

## 46.2 硬件设置（Hardware Setup）

- 确保被监测的目标引脚已接入电源。

<a id="building-and-running"></a>

## 46.3 构建与运行（Building and Running）

> 译注——执行前提：west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工具、工作区、模块和目标工具链；应用与 overlay 为官方源码，构建目录由工具生成。构建成功后按具体板文档处理下载与启动，不能把通用 west flash 视为所有板都采用同一种连接方式。失败时先检查构建输出、目标板配置和实际硬件；本次没有运行这些命令或进行实板测量。

在受支持的 Renesas RX 开发板上构建并烧录示例：

```text
west build -b rsk_rx130@512kb samples/boards/renesas/lvd
west flash
```

比较器的触发配置为上升沿（Rising edge）。当被监测引脚的电压跨过开发板设备树定义的阈值 Vref 时，产生中断并点亮 LED。

> 译注——LED 状态：回调将 LED 置为有效状态，示例没有在电压恢复后自动熄灭它，因此点亮表示曾经触发，不是完整的实时电压显示。ABOVE／BELOW 分别表示高于／低于阈值；错误返回需要和正常比较结果区分。

> 译注——阈值单位与触发：绑定中的 voltage-level 使用百分之一伏，384 表示 3.84 V，而不是 384 mV；源码虽然把宏命名为 VREF_MV，打印时实际除以 100。此例设置 COMPARATOR_TRIGGER_RISING_EDGE，不能仅凭“低电压检测”的名称将它改述为所有下降越限都会中断。

> 译注——源码入口：[main.c](../../../samples/boards/renesas/lvd/src/main.c)；[prj.conf](../../../samples/boards/renesas/lvd/prj.conf)；[comparator_renesas_rx_lvd.c](../../../drivers/comparator/comparator_renesas_rx_lvd.c)；[renesas,rx-lvd.yaml](../../../dts/bindings/comparator/renesas,rx-lvd.yaml)。本地参照实现使用相对路径，版本可能与本次网页不同。

对应官方文档源码：[samples/boards/renesas/lvd/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/renesas/lvd/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/renesas/lvd/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P045_Renesas事件链接控制器.md) · [返回大纲](大纲.md) · [下一章](P047_Renesas示例目录.md)
