---
id: learning.zephyr-docs.sensors.page-70
title: NXP_MCUX低功耗模拟比较器示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/mcux_lpcmp/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="mcux_lpcmp"></a>

# 第70章\_NXP\_MCUX低功耗模拟比较器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/mcux_lpcmp/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 70.1 概述（Overview）

本示例演示NXP MCUX低功耗模拟比较器（Low-power Analog Comparator，LPCMP）驱动的用法。

> 原文提示（Note）：本示例使用已经弃用（Deprecated）的`mcux_lpcmp`传感器驱动。新应用应改用[比较器API（Comparator API）](../hardware/P087_比较器.md#comparator-api)及[`CONFIG_COMPARATOR_NXP_LPCMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COMPARATOR_NXP_LPCMP)。该驱动和本示例计划在Zephyr 4.6中移除。

应用通过`CONFIG_LPCMP_NEGATIVE_PORT`设置LPCMP反相输入端口，使输入电压来自内部DAC。原文将DAC参考电压设置描述为“0”，具体芯片对应哪一路电压源须查参考手册（Reference manual）。DAC输出电压等于`(VREF/256)*(data+1)`，其中`data`通过属性`SENSOR_ATTR_MCUX_LPCMP_DAC_OUTPUT_VOLTAGE`设置。

同相输入（Positive input）端口由`CONFIG_LPCMP_POSITIVE_PORT`设置。根据参考手册和开发板原理图确认实际端口后，可连接外部电压，改变输入并观察LPCMP输出变化。输出值通过控制台报告。

> 译注——“0”的含义：当前源码将DAC参考源选择属性设为0，并非把参考电压设成0 V。DAC数据为`0xFF >> 1`，即127，代入原公式得到`VREF/2`；实际电压仍取决于所选参考源。

<a id="building-and-running"></a>

## 70.2 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行；Windows使用UCRT64 Bash，Linux使用原生Bash，主机工具、模块与目标工具链先按官方入门说明准备。读取真实传感器还需要对应目标板、设备树节点和接线；下面的命令与日志来自官方文档，本次没有执行硬件实验。

<a id="building-and-running-for-nxp-frdm-mcxn947"></a>

### 70.2.1 FRDM-MCXN947（Building and Running for NXP FRDM-MCXN947）

为[FRDM-MCXN947](https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxn947/doc/index.html#frdm_mcxn947)开发板构建应用，改变J2-17处的电压来调节LPCMP同相输入。

```sh
west build -b frdm_mcxn947//cpu0 samples/sensor/mcux_lpcmp
west flash
```

<a id="building-and-running-for-nxp-frdm-mcxn236"></a>

### 70.2.2 FRDM-MCXN236（Building and Running for NXP FRDM-MCXN236）

为[FRDM-MCXN236](https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxn236/doc/index.html#frdm_mcxn236)开发板构建应用，改变J2-8处的电压来调节LPCMP同相输入。

```sh
west build -b frdm_mcxn236 samples/sensor/mcux_lpcmp
west flash
```

<a id="building-and-running-for-nxp-frdm-mcxa156"></a>

### 70.2.3 FRDM-MCXA156（Building and Running for NXP FRDM-MCXA156）

为[FRDM-MCXA156](https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxa156/doc/index.html#frdm_mcxa156)开发板构建应用，改变J2-9处的电压来调节LPCMP同相输入。

```sh
west build -b frdm_mcxa156 samples/sensor/mcux_lpcmp
west flash
```

<a id="building-and-running-for-nxp-frdm-mcxa153"></a>

### 70.2.4 FRDM-MCXA153（Building and Running for NXP FRDM-MCXA153）

为[FRDM-MCXA153](https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxa153/doc/index.html#frdm_mcxa153)开发板构建应用，改变J2-9处的电压来调节LPCMP同相输入。

```sh
west build -b frdm_mcxa153 samples/sensor/mcux_lpcmp
west flash
```

<a id="building-and-running-for-nxp-frdm-mcxa346"></a>

### 70.2.5 FRDM-MCXA346（Building and Running for NXP FRDM-MCXA346）

为[FRDM-MCXA346](https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxaxx6/doc/frdm_mcxa346.html#frdm_mcxa346)开发板构建应用，改变J2-17处的电压来调节LPCMP同相输入。

```sh
west build -b frdm_mcxa346 samples/sensor/mcux_lpcmp
west flash
```

<a id="building-and-running-for-nxp-frdm-mcxa266"></a>

### 70.2.6 FRDM-MCXA266（Building and Running for NXP FRDM-MCXA266）

为[FRDM-MCXA266](https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxaxx6/doc/frdm_mcxa266.html#frdm_mcxa266)开发板构建应用，改变J2-17处的电压来调节LPCMP同相输入。

```sh
west build -b frdm_mcxa266 samples/sensor/mcux_lpcmp
west flash
```

<a id="building-and-running-for-nxp-frdm-mcxa366"></a>

### 70.2.7 FRDM-MCXA366（Building and Running for NXP FRDM-MCXA366）

为[FRDM-MCXA366](https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxaxx6/doc/frdm_mcxa366.html#frdm_mcxa366)开发板构建应用，改变J2-17处的电压来调节LPCMP同相输入。

```sh
west build -b frdm_mcxa366 samples/sensor/mcux_lpcmp
west flash
```

> 译注——示例配置与分支：当前`prj.conf`启用旧传感器驱动及触发功能，并关闭新比较器驱动以避免同时选择。启用触发时注册比较结果的上升沿和下降沿回调；未启用触发时，主程序读取一次比较结果后返回，并非持续轮询。本页保留旧示例供跟踪，新增应用应遵循上方原文的迁移提示。

<a id="see-also"></a>

## 70.3 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/mcux_lpcmp/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/mcux_lpcmp/src/main.c)、[samples/sensor/mcux_lpcmp/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/mcux_lpcmp/prj.conf)、[samples/sensor/mcux_lpcmp/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/mcux_lpcmp/tests.yaml)、[samples/sensor/mcux_lpcmp/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/mcux_lpcmp/Kconfig)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/mcux_lpcmp/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/mcux_lpcmp/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/mcux_lpcmp/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/mcux_lpcmp/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P069_NXP_MCUX模拟比较器示例.md) · [返回大纲](大纲.md) · [下一章](P071_SoC电压传感器示例.md)
