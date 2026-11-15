---
id: learning.zephyr-docs.sensors.page-30
title: JEDEC温度传感器示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/jc42/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="jc42"></a>

# 第30章\_JEDEC温度传感器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/jc42/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 30.1 概述（Overview）

本示例以0.5 Hz周期测量环境温度（Ambient temperature），将结果输出到控制台。

启用触发测量（Triggered measurement）时，示例围绕当前温度初始化并维持±2 °C窗口。温度移出窗口后发出告警（Alert），并将窗口中心移动到新的温度。

> 译注——窗口差异：原文描述为±2 °C，但当前实现的`TEMP_WINDOW_HALF_UCEL=500000`对应±0.5 °C，初始中心为25 °C；下方原日志中的24500—25500毫摄氏度也对应24.5—25.5 °C。这里保留原描述，并单独指出它与源码及日志的差异。

<a id="requirements"></a>

## 30.2 要求（Requirements）

需要兼容JEDEC JC 42.4的温度传感器。示例配置使用MCP9808。

MCP9808将−20 °C至+100 °C范围内的温度转换为数字值，最大误差为±0.5 °C。它兼容I2C；原文说明同一总线上最多支持16个设备。

> 译注——地址数量条件：依据[Microchip数据手册表3-2](https://ww1.microchip.com/downloads/en/DeviceDoc/MCP9808-0.5C-Maximum-Accuracy-Digital-Temperature-Sensor-Data-Sheet-DS20005095B.pdf)，常规地址前缀配合A2—A0提供8个地址；第二组地址码需联系厂商。因而“16个”不是仅调整同一常规型号的三个地址引脚就能实现的数量，应核对实际器件地址版本。

<a id="wiring"></a>

## 30.3 接线（Wiring）

MCP9808可作为独立元件使用，但使用已经装有它的转接板（Breakout board）更方便。原文使用的是[Adafruit MCP9808传感器转接板](https://www.adafruit.com/product/1782)。

<a id="building-and-running"></a>

## 30.4 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行，使用已完成官方入门配置的UCRT64 Bash或Linux Bash终端。构建成功只表示固件生成；烧录和读取真实温湿度还需要正确的目标板、传感器节点及接线。若设备未就绪或读取失败，先检查节点状态、驱动配置和总线连接。

提供设备树覆盖文件，描述传感器I2C总线及告警GPIO后，使用以下命令构建：

```sh
# From the root of the zephyr repository
west build -b particle_xenon samples/sensor/jc42
west flash
```

<a id="sample-output"></a>

### 30.4.1 示例输出（Sample Output）

注意，下方记录中触发回调（Trigger callback）和主线程（Main thread）的输出相互穿插。

```text
*** Booting Zephyr OS build zephyr-v2.1.0-537-gbbdeaa1ae5bb  ***
Alert on temp outside [24500, 25500] milli-Celsius
Trtrigger fired 1, temp 15.9375 C
iggAlert on temp outside [15437, 16437] milli-Celsius
er set got 0
0:00:00.017: 15.9375 C
0:00:02.020: 16 C
0:00:04.022: 16.125 C
0:00:06.024: 16.1875 C
trigger fired 2, temp 16.3125 C
Alert on temp outside [15812, 16812] milli-Celsius
0:00:08.027: 16.3125 C
0:00:10.029: 16.375 C
0:00:12.032: 16.5 C
0:00:14.034: 16.5625 C
0:00:16.037: 16.5625 C
0:00:18.039: 16.625 C
0:00:20.042: 16.6875 C
trigger fired 3, temp 16.8125 C
Alert on temp outside [16312, 17312] milli-Celsius
0:00:22.044: 16.8125 C
0:00:24.047: 16.875 C
```

> 译注——交错日志：`Trtrigger`、`iggAlert`等片段是原记录中并发输出交错的结果，本文没有重排成看似完整的单线程日志。当前示例通过`CONFIG_JC42_TRIGGER`控制阈值触发路径，`prj.conf`选择专用触发线程（Own thread）。

<a id="see-also"></a>

## 30.5 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/jc42/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/jc42/src/main.c)、[samples/sensor/jc42/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/jc42/prj.conf)、[samples/sensor/jc42/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/jc42/tests.yaml)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/jc42/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/jc42/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/jc42/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/jc42/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P029_HTS221温湿度传感器示例.md) · [返回大纲](大纲.md) · [下一章](P031_SHT3XD温湿度传感器示例.md)
