---
id: learning.zephyr-docs.sensors.page-86
title: VEAA_X_3比例压力控制阀示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/veaa_x_3/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="veea_x_3"></a>

# 第86章\_VEAA\_X\_3比例压力控制阀示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/veaa_x_3/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 86.1 概述（Overview）

本传感器示例演示如何使用VEAA-X-3比例压力控制阀（Proportional pressure control valve）。

<a id="building-and-running"></a>

## 86.2 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行；Windows使用UCRT64 Bash，Linux使用原生Bash，先按官方入门说明准备主机工具、模块与目标工具链。原生模拟目标还须满足相应主机环境要求；硬件分支需要目标板、设备树节点和接线。下方命令及日志来自官方文档，本次没有运行模拟器或硬件实验。

示例连续设置阀的设定值（Setpoint），再读取实际压力（Actual pressure）。达到所支持的最大压力后，设定值恢复为阀所支持的最小压力，并继续循环。

```sh
west build -b <board to use> samples/sensor/veaa_x_3
west flash
```

> 译注——目标与控制流程：`<board to use>`是板名占位符。当前官方测试使用`nucleo_h563zi`，随附覆盖文件为阀定义ADC反馈、DAC控制和压力范围类型。主程序先读取设备支持的范围，再按`CONFIG_SAMPLE_LOOP_INCREMENT`增加设定值；设置后等待`CONFIG_SAMPLE_LOOP_INTERVAL`毫秒，使DAC及ADC稳定再读取反馈。默认分别为1 kPa和200 ms。此示例会实际改变控制输出，不能当作只读传感器查询。

<a id="sample-output"></a>

### 86.2.1 示例输出（Sample Output）

```text
Testing test_veaa_x_3
Valve range: 1 to 200 kPa
Setpoint:    1 kPa, actual:   1 kPa
Setpoint:    2 kPa, actual:   2 kPa
Setpoint:    3 kPa, actual:   3 kPa
...
Setpoint:  199 kPa, actual: 199 kPa
Setpoint:  200 kPa, actual: 200 kPa
Setpoint:    1 kPa, actual:   1 kPa
<repeats endlessly>
```

`<repeats endlessly>`表示上述升压及回到最低值的循环持续进行。

> 译注——范围属性与命令行分支：专用属性`SENSOR_ATTR_VEAA_X_3_RANGE`把最小值放在`val1`、最大值放在`val2`，两者单位都是kPa；这里的`val2`不是通用测量值的小数部分。启用`CONFIG_SAMPLE_USE_SHELL`时，自动循环被禁用，改由设备控制台的`sensor`命令测试，不会自动出现上方连续日志。

<a id="see-also"></a>

## 86.3 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/veaa_x_3/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/veaa_x_3/src/main.c)、[samples/sensor/veaa_x_3/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/veaa_x_3/prj.conf)、[samples/sensor/veaa_x_3/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/veaa_x_3/tests.yaml)、[samples/sensor/veaa_x_3/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/veaa_x_3/Kconfig)、[samples/sensor/veaa_x_3/boards/nucleo_h563zi.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/veaa_x_3/boards/nucleo_h563zi.overlay)、[include/zephyr/drivers/sensor/veaa_x_3.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/sensor/veaa_x_3.h)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/veaa_x_3/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/veaa_x_3/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/veaa_x_3/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/veaa_x_3/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P085_TDK_APEX计步与事件检测示例.md) · [返回大纲](大纲.md) · [下一章](P087_官方传感器示例总览.md)
