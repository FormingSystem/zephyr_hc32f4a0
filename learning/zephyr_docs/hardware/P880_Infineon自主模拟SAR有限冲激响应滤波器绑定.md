---
id: learning.zephyr-docs.hardware.adcifx-3
title: Infineon自主模拟SAR有限冲激响应滤波器绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/adc/infineon,autanalog-sar-fir.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第880章\_Infineon自主模拟SAR有限冲激响应滤波器绑定

<a id="dtbinding-infineon-autanalog-sar-fir"></a>

原文：[infineon,autanalog-sar-fir](https://docs.zephyrproject.org/latest/build/dts/api/bindings/adc/infineon,autanalog-sar-fir.html)。读取日期：2026-10-13，`latest`。

`infineon,autanalog-sar-fir` 是Infineon Technologies模数转换器（Analog-to-Digital Converter，ADC）的设备树绑定（Devicetree Binding）。本页配置自主模拟（Autonomous Analog，AutAnalog）子系统逐次逼近寄存器（Successive Approximation Register，SAR）ADC的有限冲激响应（Finite Impulse Response，FIR）滤波器，用于转换结果的后处理（Post-Processing）。最多提供2个滤波器，每个64抽头（Tap）；每个滤波器可以独立配置输入通道、系数集和输出选项。

**[父SAR ADC节点](P878_Infineon自主模拟逐次逼近ADC绑定.md)下的滤波器节点必须命名为 `fir-0` 和／或 `fir-1`**，分别对应硬件索引0和1。GPIO表示通用输入输出（General-Purpose Input/Output），MUX表示多路复用器（Multiplexer），FIFO表示先入先出队列（First In, First Out）。

属性类型中，`int` 为整数，`array` 为数值数组，`boolean` 为布尔属性。

原页没有继承的基础属性。

## 880.1\_FIR节点属性与编码

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `channel-source` | `int` | 选择FIR滤波器输入的ADC通道。省略时默认为DISABLED，**必须通过伪通道（Pseudo-Channel）的 `zephyr,input-positive` 属性，或运行期间通过厂商专用应用程序接口（Application Programming Interface，API）配置通道源**。使用表后的 `IFX_AUTANALOG_SAR_FIR_CH_*` 常量；默认值：`0` |
| `coefficients` | `array` | Q1.15定点格式（Fixed-Point Format）的FIR滤波系数数组，元素数量决定抽头数（Tap Count），范围1至64。使用二进制补码（Two’s Complement），小数点固定在最高有效位（Most Significant Bit，MSB）右侧。有效范围从-32768（原文约为-1.0）到32767（约为+1.0），分辨率1/32768；原始编码示例见表后 |
| `shift-sel` | `int` | FIR输出缩放（Output Scaling），将滤波结果向右移指定的位数，有效范围0至16；默认值：`0` |
| `wait-tap-init` | `boolean` | 设置时，在输出第一个有效数据前等待与抽头数量相等的更新次数；未设置时，每次更新后产生一次触发（Trigger） |
| `fir-limit` | `int` | FIR输出的范围检测（Range Detection）配置，使用表后的 `IFX_AUTANALOG_SAR_LIMIT_*` 常量；默认值：`0`；合法值：`0, 1, 2, 3, 4` |
| `fifo-sel` | `int` | 选择接收输出结果的FIFO缓冲区，使用表后的 `IFX_AUTANALOG_SAR_FIFO_*` 常量；默认值：`0`；合法值：`0, 1, 2, 3, 4, 5, 6, 7, 8` |

下列厂商常量均来自 `<dt-bindings/adc/infineon-autanalog-sar.h>`。

滤波输入源编码：

| 常量 | 编码与含义 |
| --- | --- |
| `IFX_AUTANALOG_SAR_FIR_CH_DISABLED` | `0`：禁用（默认） |
| `IFX_AUTANALOG_SAR_FIR_CH_GPIO0` | `1`：GPIO通道0 |
| `IFX_AUTANALOG_SAR_FIR_CH_GPIO1` | `2`：GPIO通道1 |
| `IFX_AUTANALOG_SAR_FIR_CH_GPIO2` | `3`：GPIO通道2 |
| `IFX_AUTANALOG_SAR_FIR_CH_GPIO3` | `4`：GPIO通道3 |
| `IFX_AUTANALOG_SAR_FIR_CH_GPIO4` | `5`：GPIO通道4 |
| `IFX_AUTANALOG_SAR_FIR_CH_GPIO5` | `6`：GPIO通道5 |
| `IFX_AUTANALOG_SAR_FIR_CH_GPIO6` | `7`：GPIO通道6 |
| `IFX_AUTANALOG_SAR_FIR_CH_GPIO7` | `8`：GPIO通道7 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX0` | `9`：MUX通道0 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX1` | `10`：MUX通道1 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX2` | `11`：MUX通道2 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX3` | `12`：MUX通道3 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX4` | `13`：MUX通道4 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX5` | `14`：MUX通道5 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX6` | `15`：MUX通道6 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX7` | `16`：MUX通道7 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX8` | `17`：MUX通道8 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX9` | `18`：MUX通道9 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX10` | `19`：MUX通道10 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX11` | `20`：MUX通道11 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX12` | `21`：MUX通道12 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX13` | `22`：MUX通道13 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX14` | `23`：MUX通道14 |
| `IFX_AUTANALOG_SAR_FIR_CH_MUX15` | `24`：MUX通道15 |

范围检测编码：

| 常量 | 编码与含义 |
| --- | --- |
| `IFX_AUTANALOG_SAR_LIMIT_DISABLED` | `0`：禁用（默认） |
| `IFX_AUTANALOG_SAR_LIMIT_STC0` | `1`：限值配置0 |
| `IFX_AUTANALOG_SAR_LIMIT_STC1` | `2`：限值配置1 |
| `IFX_AUTANALOG_SAR_LIMIT_STC2` | `3`：限值配置2 |
| `IFX_AUTANALOG_SAR_LIMIT_STC3` | `4`：限值配置3 |

FIFO路由编码如下。

| 常量 | 编码与含义 |
| --- | --- |
| `IFX_AUTANALOG_SAR_FIFO_DISABLED` | `0`：禁用（默认） |
| `IFX_AUTANALOG_SAR_FIFO_0` | `1`：FIFO缓冲区0 |
| `IFX_AUTANALOG_SAR_FIFO_1` | `2`：FIFO缓冲区1 |
| `IFX_AUTANALOG_SAR_FIFO_2` | `3`：FIFO缓冲区2 |
| `IFX_AUTANALOG_SAR_FIFO_3` | `4`：FIFO缓冲区3 |
| `IFX_AUTANALOG_SAR_FIFO_4` | `5`：FIFO缓冲区4 |
| `IFX_AUTANALOG_SAR_FIFO_5` | `6`：FIFO缓冲区5 |
| `IFX_AUTANALOG_SAR_FIFO_6` | `7`：FIFO缓冲区6 |
| `IFX_AUTANALOG_SAR_FIFO_7` | `8`：FIFO缓冲区7 |

Q1.15系数的原始编码示例。负数-8192经过符号扩展（Sign Extension）放入32位设备树单元，编码为 `0xFFFFE000`：

```text
  0.25  = 0x2000 (8192)
  -0.25 = 0xFFFFE000 (-8192, sign-extended to 32-bit cell)
  0.5   = 0x4000 (16384)
```

本页没有已弃用的顶层专用属性。

---

[上一章：Infineon自主模拟SAR队列绑定](P879_Infineon自主模拟SAR队列绑定.md) · [下一章：Infineon高性能模拟子系统SAR绑定](P881_Infineon高性能模拟子系统SAR绑定.md) · [返回大纲](大纲.md)
