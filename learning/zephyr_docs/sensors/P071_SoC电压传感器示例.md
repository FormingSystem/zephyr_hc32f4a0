---
id: learning.zephyr-docs.sensors.page-71
title: SoC电压传感器示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/soc_voltage/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="soc_voltage"></a>

# 第71章\_SoC电压传感器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/soc_voltage/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 71.1 概述（Overview）

本示例读取片上系统（System-on-Chip，SoC）可能提供的一个或多个电压传感器，并显示结果。

对于STM32目标，如果[`st,stm32-vref`节点](../sensor_st_ti_power_capacitance_binding_reference/P003_st_stm32-vref.md#std-dtcompatible-st-stm32-vref)处于启用状态，并设置`CONFIG_ADC_STM32_VREFINT_CALIBRATE=y`，这里报告的电压应与任一STM32 ADC的`adc_ref_internal()`返回值一致：测得的电源轨（Rail）电压缓存在整个SoC范围内共享。

需要使用`adc_raw_to_millivolts_dt()`时，优先采用ADC API；本传感器示例适合显式读取VREF+／VBAT等电压通道。

<a id="building-and-running"></a>

## 71.2 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行；Windows使用UCRT64 Bash，Linux使用原生Bash，主机工具、模块与目标工具链先按官方入门说明准备。读取真实传感器还需要对应目标板、设备树节点和接线；下面的命令与日志来自官方文档，本次没有执行硬件实验。

启用支持`SENSOR_CHAN_VOLTAGE`的传感器节点，并创建名为`volt-sensor0`的设备树别名（Alias）指向该节点。尾部`0`是传感器编号；示例最多支持16个传感器。

```sh
west build -b nucleo_g071rb samples/sensor/soc_voltage
```

> 译注——读取次数：当前实现仅收集实际存在的`volt-sensor0`至`volt-sensor15`别名，对每个设备读取一次并退出。它不会自动发现所有电压节点，也没有周期采样循环。原命令仅构建固件，未包含烧录步骤。

<a id="sample-output"></a>

### 71.2.1 示例输出（Sample Output）

```text
Sensor voltage: 2.99 V
```

> 译注——日志格式：当前实现还在`Sensor voltage[...]`方括号中打印设备名，以区分多个传感器；上方保留原页日志。

<a id="see-also"></a>

## 71.3 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/soc_voltage/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/soc_voltage/src/main.c)、[samples/sensor/soc_voltage/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/soc_voltage/prj.conf)、[samples/sensor/soc_voltage/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/soc_voltage/tests.yaml)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/soc_voltage/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/soc_voltage/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/soc_voltage/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/soc_voltage/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P070_NXP_MCUX低功耗模拟比较器示例.md) · [返回大纲](大纲.md) · [下一章](P072_INA219双向电流与功率监测示例.md)
