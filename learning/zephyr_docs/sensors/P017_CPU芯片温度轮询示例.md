---
id: learning.zephyr-docs.sensors.page-17
title: CPU芯片温度轮询示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/die_temp_polling/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="die_temp_polling"></a>

# 第17章\_CPU芯片温度轮询示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/die_temp_polling/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 17.1 概述（Overview）

本示例周期性读取CPU芯片温度传感器（CPU die temperature sensor），并显示结果。

<a id="building-and-running"></a>

## 17.2 构建与运行（Building and Running）

> 译注——命令位置：以下主机构建命令从读者自己的Zephyr源码根目录执行，使用已完成官方入门配置的UCRT64 Bash或Linux Bash终端。设备树片段属于覆盖文件内容，不是Shell命令。构建成功只说明固件生成，烧录和传感器输出需要实际目标硬件及接线。出现设备未就绪或读取错误时，先核对别名、节点启用状态、驱动配置及总线连接。

启用支持`SENSOR_CHAN_DIE_TEMP`通道的传感器节点，并创建名为`die-temp0`的别名指向它。末尾的`0`为传感器编号。原文说明本示例最多支持15个传感器。

```sh
west build -b rpi_pico samples/sensor/die_temp_polling
```

> 译注——上限差异：当前`main.c`使用`LISTIFY(16, DIE_TEMPERATURE_SENSOR, ())`，枚举`die-temp0`至`die-temp15`共16个编号，与原文“15个”不一致。本文保留原说法并列出实现差异。循环每轮休眠300毫秒；这里测量的是芯片内部温度，不应直接当作环境温度。

<a id="sample-output"></a>

### 17.2.1 示例输出（Sample Output）

```text
CPU Die temperature[dietemp]: 22.6 °C
CPU Die temperature[dietemp]: 22.8 °C
CPU Die temperature[dietemp]: 23.1 °C
```

<a id="see-also"></a>

## 17.3 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/die_temp_polling/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/die_temp_polling/src/main.c)、[samples/sensor/die_temp_polling/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/die_temp_polling/prj.conf)、[samples/sensor/die_temp_polling/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/die_temp_polling/tests.yaml)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/die_temp_polling/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/die_temp_polling/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/die_temp_polling/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/die_temp_polling/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P016_温湿度传感器轮询示例.md) · [返回大纲](大纲.md) · [下一章](P018_距离传感器轮询示例.md)
