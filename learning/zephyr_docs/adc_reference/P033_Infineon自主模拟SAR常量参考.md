---
id: learning.zephyr-docs.adc_reference.adcheadermcu-33
title: Infineon自主模拟SAR常量参考
kind: reference
status: maintained
domains: [zephyr, adc_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-sar_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第33章\_Infineon自主模拟SAR常量参考

原文：[infineon-autanalog-sar_8h](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-sar_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/dt-bindings/adc/infineon-autanalog-sar.h` 定义Infineon自主模拟（Autonomous Analog，AutAnalog）逐次逼近寄存器模数转换器（Successive Approximation Register Analog-to-Digital Converter，SAR ADC）的设备树（Devicetree）绑定常量。

这些常量与外设驱动库（Peripheral Driver Library，PDL）的枚举（Enumeration）值一致，用于配置SAR ADC通道的设备树属性。原页按9组列出87个宏（Macro）；下文保留对应PDL类型或字段名和全部数值。设备树配置见[AutAnalog SAR绑定](../hardware/P878_Infineon自主模拟逐次逼近ADC绑定.md)，完整可见源码见[下一章](P034_Infineon自主模拟SAR常量源码.md)。

## 33.1\_参考电压源

参考电压（Reference Voltage，Vref）可选供电、外部参考、带隙参考（Band-Gap Reference）或可编程参考模块（Programmable Reference Block，PRB）。

原文对应类型或字段：`cy_en_autanalog_sar_vref_t`。

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `IFX_AUTANALOG_SAR_VREF_VDDA` | `0` | Vdda供电 |
| `IFX_AUTANALOG_SAR_VREF_EXT` | `1` | 外部参考（External Reference） |
| `IFX_AUTANALOG_SAR_VREF_VBGR` | `2` | 带隙参考 |
| `IFX_AUTANALOG_SAR_VREF_VDDA_BY_2` | `3` | Vdda / 2 |
| `IFX_AUTANALOG_SAR_VREF_PRB_OUT0` | `4` | PRB Vref0 |
| `IFX_AUTANALOG_SAR_VREF_PRB_OUT1` | `5` | PRB Vref1 |

## 33.2\_累加与平均模式

累加器（Accumulator）与平均（Averaging）模式包括禁用平均，以及累加后输出（Accumulate and Dump）平均。

原文对应类型或字段：`cy_en_autanalog_sar_acc_mode_t`。

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `IFX_AUTANALOG_SAR_ACC_DISABLED` | `0` | 禁用平均 |
| `IFX_AUTANALOG_SAR_ACC_ACCUNDUMP` | `1` | 累加后输出平均 |

## 33.3\_多路复用输入分配

多路复用器（Multiplexer，MUX）输入可以来自连续时间模块（Continuous Time Block，CTB）、运算放大器（Operational Amplifier，OpAmp）、数模转换器（Digital-to-Analog Converter，DAC）、温度传感器或通用输入输出（General-Purpose Input/Output，GPIO）。

原文对应类型或字段：`cy_en_autanalog_sar_pin_mux_t`。

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `IFX_AUTANALOG_SAR_PIN_MUX_CTB0_PIN1` | `0` | CTB0的GPIO引脚1 |
| `IFX_AUTANALOG_SAR_PIN_MUX_CTB0_PIN4` | `1` | CTB0的GPIO引脚4 |
| `IFX_AUTANALOG_SAR_PIN_MUX_CTB0_PIN6` | `2` | CTB0的GPIO引脚6 |
| `IFX_AUTANALOG_SAR_PIN_MUX_CTB0_PIN7` | `3` | CTB0的GPIO引脚7 |
| `IFX_AUTANALOG_SAR_PIN_MUX_CTB1_PIN1` | `4` | CTB1的GPIO引脚1 |
| `IFX_AUTANALOG_SAR_PIN_MUX_CTB1_PIN4` | `5` | CTB1的GPIO引脚4 |
| `IFX_AUTANALOG_SAR_PIN_MUX_CTB1_PIN6` | `6` | CTB1的GPIO引脚6 |
| `IFX_AUTANALOG_SAR_PIN_MUX_CTB1_PIN7` | `7` | CTB1的GPIO引脚7 |
| `IFX_AUTANALOG_SAR_PIN_MUX_CTB0_OA0_OUT` | `8` | CTB0的运算放大器0输出 |
| `IFX_AUTANALOG_SAR_PIN_MUX_CTB0_OA1_OUT` | `9` | CTB0的运算放大器1输出 |
| `IFX_AUTANALOG_SAR_PIN_MUX_CTB1_OA0_OUT` | `10` | CTB1的运算放大器0输出 |
| `IFX_AUTANALOG_SAR_PIN_MUX_CTB1_OA1_OUT` | `11` | CTB1的运算放大器1输出 |
| `IFX_AUTANALOG_SAR_PIN_MUX_DAC0` | `12` | DAC0输出 |
| `IFX_AUTANALOG_SAR_PIN_MUX_DAC1` | `13` | DAC1输出 |
| `IFX_AUTANALOG_SAR_PIN_MUX_TEMP_SENSOR` | `14` | 温度传感器（Temperature Sensor） |
| `IFX_AUTANALOG_SAR_PIN_MUX_GPIO0` | `15` | GPIO 0 |
| `IFX_AUTANALOG_SAR_PIN_MUX_GPIO1` | `16` | GPIO 1 |
| `IFX_AUTANALOG_SAR_PIN_MUX_GPIO2` | `17` | GPIO 2 |
| `IFX_AUTANALOG_SAR_PIN_MUX_GPIO3` | `18` | GPIO 3 |
| `IFX_AUTANALOG_SAR_PIN_MUX_GPIO4` | `19` | GPIO 4 |
| `IFX_AUTANALOG_SAR_PIN_MUX_GPIO5` | `20` | GPIO 5 |
| `IFX_AUTANALOG_SAR_PIN_MUX_GPIO6` | `21` | GPIO 6 |
| `IFX_AUTANALOG_SAR_PIN_MUX_GPIO7` | `22` | GPIO 7 |
| `IFX_AUTANALOG_SAR_PIN_MUX_VSSA` | `25` | ADC接地（Ground） |

## 33.4\_高速序列器多路复用模式

高速序列器（High-Speed Sequencer，HS Sequencer）的muxMode字段选择单端（Single-Ended）或伪差分（Pseudo-Differential）模式。

原文对应类型或字段：`cy_stc_autanalog_sar_seq_tab_hs_t::muxMode`。

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `IFX_AUTANALOG_SAR_MUX_DISABLED` | `0` | 禁用MUX通道 |
| `IFX_AUTANALOG_SAR_MUX0_SINGLE_ENDED` | `1` | MUX通道0单端 |
| `IFX_AUTANALOG_SAR_MUX1_SINGLE_ENDED` | `2` | MUX通道1单端 |
| `IFX_AUTANALOG_SAR_MUX0_MUX1_SINGLE_ENDED` | `3` | MUX通道0、1单端 |
| `IFX_AUTANALOG_SAR_MUX0_PSEUDO_DIFF` | `4` | MUX通道伪差分 |

## 33.5\_缓冲器功耗模式

缓冲器（Buffer）功耗模式同时区分电荷泵（Charge Pump）启用状态；中等功耗且启用电荷泵是原文推荐项。

原文对应类型或字段：`cy_en_autanalog_sar_buf_pwr_t`。

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `IFX_AUTANALOG_SAR_BUF_PWR_OFF` | `0` | 关闭缓冲器 |
| `IFX_AUTANALOG_SAR_BUF_PWR_ULTRA_LOW` | `1` | 超低功耗，关闭电荷泵 |
| `IFX_AUTANALOG_SAR_BUF_PWR_ULTRA_LOW_RAIL` | `2` | 超低功耗，开启电荷泵 |
| `IFX_AUTANALOG_SAR_BUF_PWR_LOW_RAIL` | `4` | 低功耗，开启电荷泵 |
| `IFX_AUTANALOG_SAR_BUF_PWR_MEDIUM_RAIL` | `6` | 中等功耗，开启电荷泵；**推荐** |
| `IFX_AUTANALOG_SAR_BUF_PWR_HIGH_RAIL` | `8` | 高功耗，开启电荷泵 |
| `IFX_AUTANALOG_SAR_BUF_PWR_ULTRA_HIGH_RAIL` | `10` | 超高功耗，开启电荷泵 |

## 33.6\_有限冲激响应滤波器输入

有限冲激响应（Finite Impulse Response，FIR）滤波器输入可禁用，也可以从GPIO和MUX通道选择。

原文对应类型或字段：`cy_en_autanalog_sar_fir_channel_t`。

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `IFX_AUTANALOG_SAR_FIR_CH_DISABLED` | `0` | 禁用FIR滤波器输入 |
| `IFX_AUTANALOG_SAR_FIR_CH_GPIO0` | `1` | GPIO通道0 |
| `IFX_AUTANALOG_SAR_FIR_CH_GPIO1` | `2` | GPIO通道1 |
| `IFX_AUTANALOG_SAR_FIR_CH_GPIO2` | `3` | GPIO通道2 |
| `IFX_AUTANALOG_SAR_FIR_CH_GPIO3` | `4` | GPIO通道3 |
| `IFX_AUTANALOG_SAR_FIR_CH_GPIO4` | `5` | GPIO通道4 |
| `IFX_AUTANALOG_SAR_FIR_CH_GPIO5` | `6` | GPIO通道5 |
| `IFX_AUTANALOG_SAR_FIR_CH_GPIO6` | `7` | GPIO通道6 |
| `IFX_AUTANALOG_SAR_FIR_CH_GPIO7` | `8` | GPIO通道7 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX0` | `9` | MUX通道0 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX1` | `10` | MUX通道1 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX2` | `11` | MUX通道2 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX3` | `12` | MUX通道3 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX4` | `13` | MUX通道4 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX5` | `14` | MUX通道5 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX6` | `15` | MUX通道6 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX7` | `16` | MUX通道7 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX8` | `17` | MUX通道8 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX9` | `18` | MUX通道9 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX10` | `19` | MUX通道10 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX11` | `20` | MUX通道11 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX12` | `21` | MUX通道12 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX13` | `22` | MUX通道13 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX14` | `23` | MUX通道14 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX15` | `24` | MUX通道15 |

## 33.7\_先入先出队列选择

先入先出队列（First In, First Out，FIFO）可以禁用，或选择0至7号队列。

原文对应类型或字段：`cy_en_autanalog_fifo_sel_t`。

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `IFX_AUTANALOG_SAR_FIFO_DISABLED` | `0` | 禁用FIFO |
| `IFX_AUTANALOG_SAR_FIFO_0` | `1` | FIFO 0 |
| `IFX_AUTANALOG_SAR_FIFO_1` | `2` | FIFO 1 |
| `IFX_AUTANALOG_SAR_FIFO_2` | `3` | FIFO 2 |
| `IFX_AUTANALOG_SAR_FIFO_3` | `4` | FIFO 3 |
| `IFX_AUTANALOG_SAR_FIFO_4` | `5` | FIFO 4 |
| `IFX_AUTANALOG_SAR_FIFO_5` | `6` | FIFO 5 |
| `IFX_AUTANALOG_SAR_FIFO_6` | `7` | FIFO 6 |
| `IFX_AUTANALOG_SAR_FIFO_7` | `8` | FIFO 7 |

## 33.8\_限值状态选择

限值状态（Limit Status）可以禁用，或选择0至3号配置。

原文对应类型或字段：`cy_en_autanalog_sar_limit_t`。

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `IFX_AUTANALOG_SAR_LIMIT_DISABLED` | `0` | 禁用限值状态 |
| `IFX_AUTANALOG_SAR_LIMIT_STC0` | `1` | 限值状态配置0 |
| `IFX_AUTANALOG_SAR_LIMIT_STC1` | `2` | 限值状态配置1 |
| `IFX_AUTANALOG_SAR_LIMIT_STC2` | `3` | 限值状态配置2 |
| `IFX_AUTANALOG_SAR_LIMIT_STC3` | `4` | 限值状态配置3 |

## 33.9\_先入先出队列分割

FIFO分割（FIFO Split）把总容量分成1、2、4或8个缓冲区；下面的容量单位是字（Word），不自行换算为字节。

原文对应类型或字段：`cy_en_autanalog_fifo_split_t`。

| 宏 | 原始值或表达式 | 中文说明 |
| --- | --- | --- |
| `IFX_AUTANALOG_SAR_FIFO_SPLIT1` | `0` | 单个512字缓冲区 |
| `IFX_AUTANALOG_SAR_FIFO_SPLIT2` | `1` | 两个256字缓冲区 |
| `IFX_AUTANALOG_SAR_FIFO_SPLIT4` | `2` | 四个128字缓冲区 |
| `IFX_AUTANALOG_SAR_FIFO_SPLIT8` | `3` | 八个64字缓冲区 |


---

[上一章：WisBlockADC设备树常量源码](P032_WisBlockADC设备树常量源码.md) · [下一章：Infineon自主模拟SAR常量源码](P034_Infineon自主模拟SAR常量源码.md) · [返回大纲](大纲.md)
