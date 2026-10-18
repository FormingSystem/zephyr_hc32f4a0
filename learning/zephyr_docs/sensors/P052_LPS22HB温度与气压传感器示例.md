---
id: learning.zephyr-docs.sensors.page-52
title: LPS22HB温度与气压传感器示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/lps22hb/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lps22hb"></a>

# 第52章\_LPS22HB温度与气压传感器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/lps22hb/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 52.1 概述（Overview）

本示例周期性读取LPS22HB微机电系统（Micro-Electro-Mechanical Systems，MEMS）压力传感器（Pressure sensor）的压力值，并在控制台显示。

<a id="requirements"></a>

## 52.2 要求（Requirements）

示例通过I2C接口控制LPS22HB。

<a id="references"></a>

## 52.3 参考资料（References）

LPS22HB：[ST官方产品资料](https://www.st.com/en/mems-and-sensors/lps22hb.html)。

<a id="building-and-running"></a>

## 52.4 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行，终端及工具链按官方入门说明准备。读取真实传感器还需要对应目标板、设备树节点和接线；下面的命令与日志来自官方文档，本次没有执行硬件实验。

项目向控制台输出传感器数据，需要LPS22HB；`disco_l475_iot1`开发板具有该传感器。

```sh
west build -b disco_l475_iot1 samples/sensor/lps22hb
```

<a id="sample-output"></a>

### 52.4.1 示例输出（Sample Output）

```text
Observation:1
Pressure:98.7 kPa
Temperature:22.5 C
Observation:2
Pressure:98.7 kPa
Temperature:22.5 C
Observation:3
Pressure:98.7 kPa
Temperature:22.5 C

<repeats endlessly every 2 seconds>
```

以上输出每2秒不断重复（`<repeats endlessly every 2 seconds>`）。

> 译注——实际读取通道：虽然概述只写压力，当前实现与原日志都同时读取压力和环境温度（Ambient temperature）。每次完整读取成功后增加观测编号（Observation），按一位小数显示压力kPa和温度°C，然后主循环休眠2秒。

<a id="see-also"></a>

## 52.5 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/lps22hb/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lps22hb/src/main.c)、[samples/sensor/lps22hb/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lps22hb/prj.conf)、[samples/sensor/lps22hb/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lps22hb/tests.yaml)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/lps22hb/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lps22hb/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/lps22hb/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/lps22hb/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P051_CCS811室内空气质量传感器示例.md) · [返回大纲](大纲.md) · [下一章](P053_LPS22HH温度与气压传感器示例.md)
