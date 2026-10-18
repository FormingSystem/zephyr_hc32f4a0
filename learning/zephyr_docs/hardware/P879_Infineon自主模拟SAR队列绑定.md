---
id: learning.zephyr-docs.hardware.adcifx-2
title: Infineon自主模拟SAR队列绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/adc/infineon,autanalog-sar-fifo.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第879章\_Infineon自主模拟SAR队列绑定

<a id="dtbinding-infineon-autanalog-sar-fifo"></a>

原文：[infineon,autanalog-sar-fifo](https://docs.zephyrproject.org/latest/build/dts/api/bindings/adc/infineon,autanalog-sar-fifo.html)。读取日期：2026-10-13，`latest`。

`infineon,autanalog-sar-fifo` 是Infineon Technologies模数转换器（Analog-to-Digital Converter，ADC）的设备树绑定（Devicetree Binding）。本页配置自主模拟（Autonomous Analog，AutAnalog）子系统逐次逼近寄存器（Successive Approximation Register，SAR）ADC的先入先出队列（First In, First Out，FIFO）。AutAnalog共享FIFO最多可分为8个独立缓冲区。通用输入输出（General-Purpose Input/Output，GPIO）通道、多路复用器（Multiplexer，MUX）通道和有限冲激响应（Finite Impulse Response，FIR）滤波器输出，分别通过对应通道或FIR节点的 `fifo-sel` 路由到某个缓冲区。

**[父SAR ADC节点](P878_Infineon自主模拟逐次逼近ADC绑定.md)下必须放置一个名为 `fifo` 的节点。**FIFO具有名为 `autanalog_fifo` 的专用中断线，与AutAnalog主中断分开。

属性类型中，`int` 为整数，`array` 为数值数组，`boolean` 为布尔属性。

原页没有继承的基础属性。

## 879.1\_FIFO节点属性与分区

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `fifo-levels` | `array` | **必需**。FIFO缓冲区水位阈值（Level Threshold）数组；数组长度决定分区方式，见表后对照。缓冲区中的字（Word）数量达到阈值时产生FIFO水位中断（Watermark Interrupt）；非零阈值会自动启用对应缓冲区的水位中断，0不产生水位中断。有效阈值范围取决于分区后的缓冲区大小 |

`fifo-levels` 数组长度决定共享FIFO内存的分区。`SPLIT1`、`SPLIT2`、`SPLIT4`、`SPLIT8` 是原文的分区模式名称（Split Mode），数字表示缓冲区数量。大小以字（Word）为单位，原页没有规定每字的字节数。

| 数组条目数 | 分区方式与每区大小 |
| --- | --- |
| 1 | `SPLIT1`：1个512字缓冲区 |
| 2 | `SPLIT2`：2个256字缓冲区 |
| 4 | `SPLIT4`：4个128字缓冲区 |
| 8 | `SPLIT8`：8个64字缓冲区 |

本页没有已弃用的顶层专用属性。

---

[上一章：Infineon自主模拟逐次逼近ADC绑定](P878_Infineon自主模拟逐次逼近ADC绑定.md) · [下一章：Infineon自主模拟SAR有限冲激响应滤波器绑定](P880_Infineon自主模拟SAR有限冲激响应滤波器绑定.md) · [返回大纲](大纲.md)
