---
id: learning.zephyr-docs.sensors.page-68
title: NPCX模数转换比较器示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/adc_cmp_npcx/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="adc_cmp_npcx"></a>

# 第68章\_NPCX模数转换比较器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/adc_cmp_npcx/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 68.1 概述（Overview）

本示例演示NPCX模数转换比较器（ADC Comparator）驱动的用法，支持[NPCX9M6F EVB开发板](https://docs.zephyrproject.org/latest/boards/nuvoton/npcx9m6f_evb/doc/index.html#npcx9m6f_evb)。

应用实现带迟滞（Hysteresis）的电压比较器，上限设为1 V，下限设为250 mV，初始配置为检测上限。

<a id="building-and-running"></a>

## 68.2 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行；Windows使用UCRT64 Bash，Linux使用原生Bash，主机工具、模块与目标工具链先按官方入门说明准备。读取真实传感器还需要对应目标板、设备树节点和接线；下面的命令与日志来自官方文档，本次没有执行硬件实验。

为NPCX9M6F EVB构建应用，并向ADC通道8提供输入电压。电压越过上限或下限时，控制台会打印检测消息。

```sh
west build -b npcx9m6f_evb samples/sensor/adc_cmp_npcx
west flash
```

> 译注——通道与消息含义：官方覆盖文件的`io-channels = <&adc0 8>`对应上述通道8。当前主程序首次设置1000 mV上阈值；回调关闭告警后改为检测250 mV下阈值，再重新使能告警，之后交替切换。当前日志字符串在切换到下阈值时打印`Lower threshold detected`，切换到上阈值时打印`Upper threshold detected`；字符串与刚触发的阈值方向相反，判断触发条件应对照状态切换，不能仅凭该行名称。

<a id="see-also"></a>

## 68.3 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/adc_cmp_npcx/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/adc_cmp_npcx/src/main.c)、[samples/sensor/adc_cmp_npcx/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/adc_cmp_npcx/prj.conf)、[samples/sensor/adc_cmp_npcx/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/adc_cmp_npcx/tests.yaml)、[samples/sensor/adc_cmp_npcx/boards/npcx9m6f_evb.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/adc_cmp_npcx/boards/npcx9m6f_evb.overlay)、[include/zephyr/drivers/sensor/adc_cmp_npcx.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/sensor/adc_cmp_npcx.h)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/adc_cmp_npcx/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/adc_cmp_npcx/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/adc_cmp_npcx/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/adc_cmp_npcx/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P067_S3KM1110毫米波传感器示例.md) · [返回大纲](大纲.md) · [下一章](P069_NXP_MCUX模拟比较器示例.md)
