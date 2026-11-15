---
id: learning.zephyr-docs.sensors.page-53
title: LPS22HH温度与气压传感器示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/lps22hh/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lps22hh"></a>

# 第53章\_LPS22HH温度与气压传感器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/lps22hh/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 53.1 概述（Overview）

本示例周期性读取LPS22HH微机电系统（Micro-Electro-Mechanical Systems，MEMS）压力传感器（Pressure sensor）的压力值，并在控制台显示。

<a id="requirements"></a>

## 53.2 要求（Requirements）

示例通过I2C接口控制LPS22HH。

<a id="references"></a>

## 53.3 参考资料（References）

LPS22HH：[ST官方产品资料](https://www.st.com/en/mems-and-sensors/lps22hh.html)。

<a id="building-and-running"></a>

## 53.4 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行，终端及工具链按官方入门说明准备。读取真实传感器还需要对应目标板、设备树节点和接线；下面的命令与日志来自官方文档，本次没有执行硬件实验。

项目向控制台输出传感器数据，需要LPS22HH；X-NUCLEO-IKS01A3扩展板（Shield）具有该传感器。

```sh
west build -b nrf52dk/nrf52832 --shield x_nucleo_iks01a3 samples/sensor/lps22hh
```

<a id="sample-output"></a>

### 53.4.1 示例输出（Sample Output）

```text
Configured for triggered collection at 1 Hz
Observation: 1
Pressure: 97.474 kPa
Temperature: 22.19 C
Observation: 2
Pressure: 97.466 kPa
Temperature: 22.21 C
Observation: 3
Pressure: 97.473 kPa
Temperature: 22.21 C
Observation: 4
Pressure: 97.455 kPa
Temperature: 22.21 C

<repeats endlessly every second>
```

以上输出每秒不断重复（`<repeats endlessly every second>`）。

> 译注——触发与轮询：这段输出对应1 Hz数据就绪触发（Data-ready trigger）。当前实现启用`CONFIG_LPS22HH_TRIGGER`时设置该频率并在回调中读取；未启用时则采用轮询，每次读取后休眠2秒。两种模式都读取压力和温度，分别以三位和两位小数输出，不能把原日志中的1秒间隔直接用于轮询分支。

<a id="see-also"></a>

## 53.5 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/lps22hh/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lps22hh/src/main.c)、[samples/sensor/lps22hh/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lps22hh/prj.conf)、[samples/sensor/lps22hh/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lps22hh/tests.yaml)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/lps22hh/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lps22hh/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/lps22hh/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/lps22hh/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P052_LPS22HB温度与气压传感器示例.md) · [返回大纲](大纲.md) · [下一章](P054_MAX6675热电偶数字转换示例.md)
