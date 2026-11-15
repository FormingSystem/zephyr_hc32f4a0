---
id: learning.zephyr-docs.sensors.page-69
title: NXP_MCUX模拟比较器示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/mcux_acmp/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="mcux_acmp"></a>

# 第69章\_NXP\_MCUX模拟比较器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/mcux_acmp/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 69.1 概述（Overview）

本示例演示NXP MCUX模拟比较器（Analog Comparator，ACMP）驱动的用法，支持[TWR-KE18F](https://docs.zephyrproject.org/latest/boards/nxp/twr_ke18f/doc/index.html#twr_ke18f)、[MIMXRT1170-EVK](https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1170_evk/doc/index.html#mimxrt1170_evk)、[FRDM-KE17Z](https://docs.zephyrproject.org/latest/boards/nxp/frdm_ke17z/doc/index.html#frdm_ke17z)、[FRDM-KE17Z512](https://docs.zephyrproject.org/latest/boards/nxp/frdm_ke17z512/doc/index.html#frdm_ke17z512)、[MIMXRT1180-EVK](https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1180_evk/doc/index.html#mimxrt1180_evk)及[MIMXRT700-EVK](https://docs.zephyrproject.org/latest/boards/nxp/mimxrt700_evk/doc/index.html#mimxrt700_evk)开发板。

比较器反相输入（Negative input）的电压由ACMP内部数模转换器（Digital-to-Analog Converter，DAC）提供。比较器输出值通过控制台报告。

<a id="building-and-running"></a>

## 69.2 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行；Windows使用UCRT64 Bash，Linux使用原生Bash，主机工具、模块与目标工具链先按官方入门说明准备。读取真实传感器还需要对应目标板、设备树节点和接线；下面的命令与日志来自官方文档，本次没有执行硬件实验。

<a id="building-and-running-for-twr-ke18f"></a>

### 69.2.1 TWR-KE18F（Building and Running for TWR-KE18F）

为TWR-KE18F构建应用，旋转板载电位器（Potentiometer）来调节ACMP输入电压。

```sh
west build -b twr_ke18f samples/sensor/mcux_acmp
west flash
```

<a id="building-and-running-for-mimxrt1170-evk"></a>

### 69.2.2 MIMXRT1170-EVK（Building and Running for MIMXRT1170-EVK）

为MIMXRT1170-EVK构建应用，改变J25-13处的输入电压来调节ACMP输入。

```sh
west build -b mimxrt1170_evk/mimxrt1176/cm7 samples/sensor/mcux_acmp
west flash
```

<a id="building-and-running-for-frdm-ke17z"></a>

### 69.2.3 FRDM-KE17Z（Building and Running for FRDM-KE17Z）

为FRDM-KE17Z构建应用，改变J2-3处的输入电压来调节ACMP输入。

```sh
west build -b frdm_ke17z samples/sensor/mcux_acmp
west flash
```

<a id="building-and-running-for-frdm-ke17z512"></a>

### 69.2.4 FRDM-KE17Z512（Building and Running for FRDM-KE17Z512）

为FRDM-KE17Z512构建应用，改变J2-3处的输入电压来调节ACMP输入。

```sh
west build -b frdm_ke17z512 samples/sensor/mcux_acmp
west flash
```

<a id="building-and-running-for-mimxrt1180-evk"></a>

### 69.2.5 MIMXRT1180-EVK（Building and Running for MIMXRT1180-EVK）

为MIMXRT1180-EVK构建应用，改变J45-13处的输入电压来调节ACMP输入。原文分别给出Cortex-M33和Cortex-M7目标：

```sh
west build -b mimxrt1180_evk/mimxrt1189/cm33 samples/sensor/mcux_acmp
west flash
```

```sh
west build -b mimxrt1180_evk/mimxrt1189/cm7 samples/sensor/mcux_acmp
west flash
```

<a id="building-and-running-for-mimxrt700-evk"></a>

### 69.2.6 MIMXRT700-EVK（Building and Running for MIMXRT700-EVK）

为MIMXRT700-EVK构建应用，改变J7-9处的输入电压来调节ACMP输入。

原文注（Note）：下列分别为`cm33_cpu0`与`cm33_cpu1`目标的命令；原页未在“Note”后提供其他说明。

```sh
west build -b mimxrt700_evk/mimxrt798s/cm33_cpu0 samples/sensor/mcux_acmp
west flash
```

```sh
west build -b mimxrt700_evk/mimxrt798s/cm33_cpu1 samples/sensor/mcux_acmp
west flash
```

> 译注——比较结果与参考源：当前主程序按开发板选择比较器、正负输入和DAC参考源，DAC数值设为128。各芯片参考源及输入路由不同，128不是跨平台固定的电压值。程序注册上升沿／下降沿触发器，并在初始化后读取一次比较结果；等待循环中的1 ms休眠不是ADC采样率。

<a id="see-also"></a>

## 69.3 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/mcux_acmp/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/mcux_acmp/src/main.c)、[samples/sensor/mcux_acmp/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/mcux_acmp/prj.conf)、[samples/sensor/mcux_acmp/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/mcux_acmp/tests.yaml)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/mcux_acmp/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/mcux_acmp/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/mcux_acmp/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/mcux_acmp/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P068_NPCX模数转换比较器示例.md) · [返回大纲](大纲.md) · [下一章](P070_NXP_MCUX低功耗模拟比较器示例.md)
