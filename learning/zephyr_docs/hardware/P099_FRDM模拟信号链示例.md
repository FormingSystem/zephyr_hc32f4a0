---
id: learning.zephyr-docs.hardware.analogsamp-2
title: FRDM模拟信号链示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nxp/frdm_mcxa156/lpdac_opamp_lpadc/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="frdm_mcxa156_lpdac_opamp_lpadc"></a>

# 第99章\_FRDM模拟信号链示例

原文：[FRDM-MCXA156 lpdac opamp lpadc example](https://docs.zephyrproject.org/latest/samples/boards/nxp/frdm_mcxa156/lpdac_opamp_lpadc/README.html)。读取日期：2026-10-13，`latest`。

## 99.1\_DAC、运放与ADC组成的信号链

本示例在FRDM-MCXA156上连接 **低功耗数模转换器（Low-Power Digital-to-Analog Converter，LPDAC）**、**运算放大器（Operational Amplifier，OPAMP）**和 **低功耗模数转换器（Low-Power Analog-to-Digital Converter，LPADC）**，展示采样驱动按理想范围调整增益的过程。

LPDAC输出300 mV到OPAMP同相输入。OPAMP采用 **同相放大模式（Non-Inverting Amplifier Mode）**，反相端接地。LPADC通道0接OPAMP输出，通道1接DAC输出，也就是OPAMP同相输入。

设备树属性 `ideal-sample-range` 指定运放输出通道的理想采样范围；`nxp,opamps` 指定LPADC采样哪个OPAMP输出，以及哪个ADC通道与该输出相连。

## 99.2\_逐轮调整增益

OPAMP同相输入为300 mV，初始增益设为1。第一轮输出约300 mV，低于理想采样范围下限，ADC驱动于是通过 `opamp_set_gain()` 增加增益。

第二轮输出约900 mV，仍低于下限，继续增加增益。第三轮约1500 mV，已处于理想范围，之后不再调整。具体接口说明见[运算放大器增益接口](P091_运算放大器接口参考.md)。

> 译注：原页前面写 `ideal-sample-range`，后面的过程描述写成 `ideal-sampling-range`；对照示例 `app.overlay` 使用的是前者。同一原页在概览称“同相放大模式”，接线标题却写“OPAMP0 in differential mode”；示例配置的 `functional-mode` 为 `non_inverting`。这里保留并指出文字不一致，复现应核对所用版本的[官方覆盖文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/nxp/frdm_mcxa156/lpdac_opamp_lpadc/app.overlay)，不能混用两个模式说明。

## 99.3\_构建与硬件连接

原文目标板为[FRDM-MCXA156](https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxa156/doc/index.html#frdm_mcxa156)。准备Zephyr环境、对应工具链和烧录工具后，在Ubuntu Bash或已准备好的UCRT64 Bash中，从实验Zephyr源码根目录执行：

```shell
west build -b frdm_mcxa156 samples/boards/nxp/frdm_mcxa156/lpdac_opamp_lpadc
west flash
```

构建成功后再烧录。原文硬件连接为：OPAMP正输入J2-12连接DAC0输出J2-9，并连接LPADC0通道1输入J4-2；OPAMP负输入R60-3连接 **地（Ground，GND）**。这些引脚名称属于该板，不适用于其他板的直接接线。

原文给出的电压关系为：`Ngain > 1` 时，`Vout = Vinp * (Ngain + 1)`；`Ngain = 1` 时，`Vout = Vinp * Ngain`。Vout为输出电压，Vinp为同相输入电压，Ngain为原例使用的增益参数。该关系结合示例的模式与硬件配置使用，不替代其他运放连接方式的增益公式。

## 99.4\_观察原始采样与电压

终端打印OPAMP同相输入（DAC输出）与OPAMP输出的原始采样值及换算电压。原文输出如下：

```text
*** Booting Zephyr OS build v4.2.0-3573-gd796bf703856 ***
round 0: output=5796 (~291 mV), input=5949 (~299 mV)
round 1: output=17806 (~896 mV), input=5945 (~299 mV)
round 2: output=29506 (~1485 mV), input=5964 (~300 mV)
round 3: output=29508 (~1485 mV), input=5957 (~299 mV)
round 4: output=29529 (~1486 mV), input=5944 (~299 mV)
```

`round` 为轮次，`input` 为输入通道采样，`output` 为运放输出通道采样，括号内以毫伏表示换算值。输出在前三轮增加，随后约稳定在1485—1486 mV；原文提醒实际数值可能不同。

版本字符串4.2.0属于历史示例输出，不是本次页面版本声明。相关 **应用程序编程接口（Application Programming Interface，API）**见[ADC参考](P463_ADC公共接口参考.md)。本次未烧录、接线、输出DAC电压或执行自动增益测量。

[上一章：Renesas比较器示例](P098_Renesas比较器示例.md) · [下一章：系统与诊断外设入口](P100_系统与诊断外设入口.md) · [返回大纲](大纲.md)
