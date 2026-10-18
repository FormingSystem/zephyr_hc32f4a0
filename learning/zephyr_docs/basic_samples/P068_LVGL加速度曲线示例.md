---
id: learning.zephyr-docs.basic_samples.page-68
title: LVGL加速度曲线示例
kind: reference
status: maintained
domains: [zephyr, basic_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/modules/lvgl/accelerometer_chart/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lvgl-accelerometer-chart"></a>

# 第68章\_LVGL加速度曲线示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/modules/lvgl/accelerometer_chart/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 68.1 概述（Overview）

本示例演示如何结合LVGL与[传感器（Sensors）](../sensors/P001_传感器驱动概览.md#sensor)接口，在实时更新的折线图（Line chart）中显示加速度数据。

示例创建包含三条数据序列（Series）的折线图，分别对应加速度计三个轴。LVGL定时器默认每20ms从传感器获取最新加速度数据并更新图表。更新周期可配置，见下文[构建与运行](#lvgl-accelerometer-chart-building-and-running)。

<a id="requirements"></a>

## 68.2 要求（Requirements）

- 一块带显示器的开发板。
- 一个提供加速度数据（[`SENSOR_CHAN_ACCEL_XYZ`](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9)）、可通过设备树（Devicetree）别名`&accel0`访问的传感器。

> 注意：`native_sim*`开发板变体提供设备树覆盖文件（Devicetree overlay），声明模拟的BMI160加速度计，因此可以在本机运行此示例。

<a id="building-and-running"></a>
<a id="lvgl-accelerometer-chart-building-and-running"></a>

## 68.3 构建与运行（Building and Running）

Kconfig选项`CONFIG_SAMPLE_CHART_POINTS_PER_SERIES`与`CONFIG_SAMPLE_ACCEL_SAMPLING_RATE`分别配置每条序列最多显示的点数与加速度计采样率（Sampling rate）。默认采样率为50Hz，每条序列最多50个点。

可按以下方式构建演示；注意，此命令将采样率设为自定义的20Hz：

```sh
west build -b native_sim samples/modules/lvgl/accelerometer_chart -- -DCONFIG_SAMPLE_ACCEL_SAMPLING_RATE=20
west build -t run
```

> 译注——更新频率：默认50Hz对应20ms周期，命令中的20Hz对应50ms。当前实现用`1000 / CONFIG_SAMPLE_ACCEL_SAMPLING_RATE`计算LVGL定时器周期，再调用`sensor_sample_fetch()`与`sensor_channel_get()`获取三个轴的数据；该选项控制应用获取与更新数据的节奏，不表示代码同时设置了传感器硬件输出数据率（Output data rate，ODR）。

<a id="see-also"></a>

## 68.4 另请参阅（See also）

[显示接口（Display）](../hardware/P214_显示公共接口.md)、[传感器接口（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/modules/lvgl/accelerometer_chart/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/lvgl/accelerometer_chart/Kconfig)、[samples/modules/lvgl/accelerometer_chart/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/lvgl/accelerometer_chart/src/main.c)。这些链接对应本次核对的官方main来源，内容会随分支变化，所保存快照的摘要见[来源记录](../SOURCES.md)。下方本仓库源码仅用于版本对照。

对应官方文档源码：[samples/modules/lvgl/accelerometer_chart/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/lvgl/accelerometer_chart/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/modules/lvgl/accelerometer_chart/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/modules/lvgl/accelerometer_chart/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P067_LVGL示例目录.md) · [返回大纲](大纲.md) · [下一章](P069_LVGL演示合集.md)
