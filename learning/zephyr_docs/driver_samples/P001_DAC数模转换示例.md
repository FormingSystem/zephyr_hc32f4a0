---
id: learning.zephyr-docs.driver_samples.page-1
title: DAC数模转换示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/dac/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="dac"></a>

# 第1章\_DAC数模转换示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/dac/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 1.1\_概览（Overview）

本例演示如何使用数模转换器（Digital-to-Analog Converter，DAC）的[驱动API](../hardware/P010_DAC数模转换.md#dac-api)。

<a id="building-and-running"></a>

## 1.2\_构建与运行前提（Building and Running）

DAC输出由开发板的设备树（Devicetree）及引脚复用（Pinmux）文件定义。开发板的 [/zephyr,user](../devicetree/P016_用户设备树节点.md#dt-zephyr-user) 节点必须设置 `dac`、`dac-channel-id` 和 `dac-resolution` 属性。示例覆盖文件见 [samples/drivers/dac/boards](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/dac/boards)。

<a id="id1"></a>

### 1.2.1\_构建与运行命令（Building and Running）

满足上述条件后，构建并烧录：

```bash
west build -b <board-name> samples/drivers/dac
west flash
```

> 译注——操作前提：从读者Zephyr源码根运行west，替换 `<board-name>` 为实际受支持板目标；主机工具、模块和目标工具链应已准备。构建成功不等于DAC输出已验证，烧录后还需在板定义的输出引脚观察信号。缺少设备树属性时先修正板配置，不要直接套用其他板的引脚。

<a id="sample-output"></a>

### 1.2.2\_示例输出（Sample output）

在板定义的DAC输出引脚，应看到幅度为DAC参考电压、周期约4秒的锯齿波（Sawtooth Signal）。控制台输出：

```text
Generating sawtooth signal at DAC channel 1.
```

**注意：**若不支持DAC，输出会是错误消息。

> 译注——周期与分辨率：所读[示例实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/dac/src/main.c)按分辨率生成递增数值，并把每步休眠限制为至少1毫秒。12位时4096步约为4秒；更高分辨率及调度开销会改变实际周期，不能把“约4秒”当作所有DAC的精确指标。日志仅表示开始生成，模拟电压仍需在实际引脚测量。

<a id="see-also"></a>

## 1.3\_相关接口（See also）

[DAC接口参考](../hardware/P822_数模转换器接口.md)。


对应官方文档源码：[samples/drivers/dac/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/dac/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/dac/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/dac/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[返回大纲](大纲.md) · [下一章](P002_GPIO按钮中断示例.md)
