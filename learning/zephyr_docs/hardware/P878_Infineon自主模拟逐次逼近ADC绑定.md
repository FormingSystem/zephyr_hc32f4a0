---
id: learning.zephyr-docs.hardware.adcifx-1
title: Infineon自主模拟逐次逼近ADC绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/adc/infineon,autanalog-sar-adc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第878章\_Infineon自主模拟逐次逼近ADC绑定

<a id="dtbinding-infineon-autanalog-sar-adc"></a>

原文：[infineon,autanalog-sar-adc](https://docs.zephyrproject.org/latest/build/dts/api/bindings/adc/infineon,autanalog-sar-adc.html)。读取日期：2026-10-13，`latest`。

`infineon,autanalog-sar-adc` 是Infineon Technologies模数转换器（Analog-to-Digital Converter，ADC）的设备树绑定（Devicetree Binding）。此节点用于PSOC Edge 84自主模拟（Autonomous Analog，AutAnalog）子系统的逐次逼近寄存器（Successive Approximation Register，SAR）ADC。其分辨率为12位，高性能模式下采样率最高5 Msps（每秒百万次采样）。输入可直接选择最多8个通用输入输出（General-Purpose Input/Output，GPIO）模拟通道，或经内部多路复用器（Multiplexer，MUX）选择最多16个内部通道。

MUX可采样连续时间模块（Continuous Time Block，CTB）的运算放大器（Operational Amplifier）输出、数模转换器（Digital-to-Analog Converter，DAC）输出、温度传感器及其他内部模拟信号。使用 `<dt-bindings/adc/infineon-autanalog-sar.h>` 中的 `IFX_AUTANALOG_SAR_PIN_MUX_*` 常量选择MUX通道。

初始化ADC之前必须先配置[AutAnalog子系统](P720_Infineon自主模拟子系统绑定.md)，子系统的共享中断处理所有AutAnalog外设事件。先入先出队列（First In, First Out，FIFO）采用独立中断，见[FIFO配置](P879_Infineon自主模拟SAR队列绑定.md)；有限冲激响应（Finite Impulse Response，FIR）滤波器见[FIR配置](P880_Infineon自主模拟SAR有限冲激响应滤波器绑定.md)。低功耗相关其他外设还包括可编程阈值比较器（Programmable Threshold Comparator，PTCOMP）与可编程参考模块（Programmable Reference Block，PRB）。

驱动为 [`drivers/adc/adc_infineon_autanalog_sar.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/adc_infineon_autanalog_sar.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,autanalog-sar-adc)。

以下严格区分各层节点，必需性、固定值及合法取值仅适用于所在层。`int` 为整数，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`string` 为字符串，`string-array` 为字符串数组，`boolean` 为布尔属性，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用及说明单元数组。Kconfig是Zephyr的配置系统。

基础属性可用于多种节点，不保证全部适用于当前硬件。电源域（Power Domain）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox）及处理器间消息（Inter-Processor Messaging，IPM）的通用属性也按原页保留。

## 878.1\_控制器节点属性

本层 `reg` 是寄存器地址属性；`CLK_HF` 是原页使用的时钟标识（Clock Identifier），低功耗模式会将它替换为LPOSC。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `#io-channel-cells` | `int` | **必需**。输入输出通道说明符（I/O Channel Specifier）的单元数量（Cell Count）；固定值：`1` |
| `vref-mv` | `int` | 内部参考电压（Internal Reference Voltage），单位为毫伏（Millivolt，mV）；默认值：`1800` |
| `offset-cal` | `boolean` | 启用失调自校准（Offset Self-Calibration）；禁用时使用出厂失调校准值 |
| `linear-cal` | `boolean` | 启用线性度自校准（Linearity Self-Calibration）；禁用时使用出厂线性度校准值 |
| `vref-source` | `int` | 选择ADC参考电压源（Voltage Reference Source），使用表后的 `IFX_AUTANALOG_SAR_VREF_*` 常量；默认值：`0`；合法值：`0, 1, 2, 3, 4, 5` |
| `pos-buf-pwr` | `int` | 多路复用器（Multiplexer，MUX）正输入缓冲器的功耗模式（Power Mode），使用表后的 `IFX_AUTANALOG_SAR_BUF_PWR_*` 常量；默认值：`0`；合法值：`0, 1, 2, 4, 6, 8, 10` |
| `neg-buf-pwr` | `int` | MUX负输入缓冲器的功耗模式；使用与 `pos-buf-pwr` 相同的 `IFX_AUTANALOG_SAR_BUF_PWR_*` 常量及取值；默认值：`0`；合法值：`0, 1, 2, 4, 6, 8, 10` |
| `acc-mode` | `int` | ADC累加／平均模式（Accumulator / Averaging Mode），使用表后的 `IFX_AUTANALOG_SAR_ACC_*` 常量；默认值：`0`；合法值：`0, 1` |
| `shift-mode` | `boolean` | 硬件执行平均时的结果分辨率（Resolution）：false为默认值，将结果移回12位；true将结果移到16位 |
| `fifo-chan-id` | `boolean` | 为存入先入先出队列（First In, First Out，FIFO）的数据启用通道编号标识 |
| `lp-mode` | `boolean` | 启用低功耗（Low Power，LP）模式。ADC由4.096 MHz低功耗振荡器（Low Power Oscillator，LPOSC）提供时钟，替代 `CLK_HF`；**只允许使用MUX通道，通道编号至少为8，最大吞吐率200 ksps（每秒千次采样）**。LP模式在活动（Active）及深度睡眠（Deep Sleep）电源模式下均可使用。设置此属性时，父AutAnalog多功能设备（Multi-Function Device，MFD）的基本模式状态转换表（State Transition Table，STT）会自动为自主控制器（Autonomous Controller，AC）各状态启用LP运行。其他任意AutAnalog子外设DAC、CTB、PTCOMP或PRB设置 `lp-mode` 时也会启用LP。**高级模式 `ac-states` 应改用各状态的 `ac-lp-mode` 属性** |
| `lp-diff-en` | `boolean` | 启用LP通道的差分模式（Differential Mode），LP采样器测量MUX正、负输入之差。**LP模式下精确测量芯片裸片温度（Die Temperature）需要此设置，且仅在同时设置 `lp-mode` 时有效** |
| `reg` | `array` | **必需**。AutAnalog SAR ADC寄存器基地址（Register Base Address）；参见[重要属性](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props) |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`1` |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`0` |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的名称；通用说明称其为可选名称，是否必须填写以本层的必需标记为准 |
| `dma-coherent` | `boolean` | 表示设备支持一致性 DMA 操作，见规范 v0.4 第 2.3.10 节 |
| `dmas` | `phandle-array` | 与设备相关的 DMA 通道说明符 |
| `dma-names` | `string-array` | `dmas` 中各 DMA 通道说明符的可选名称 |
| `dma-ranges` | `compound` | 定义总线物理地址空间与其父总线物理地址空间之间的映射或转换，见规范 v0.4 第 2.3.9 节 |
| `io-channels` | `phandle-array` | 与设备相关的 I/O 通道说明符 |
| `io-channel-names` | `string-array` | `io-channels` 中各通道说明符的可选名称 |
| `mboxes` | `phandle-array` | 与设备相关的邮箱/IPM 通道说明符 |
| `mbox-names` | `string-array` | `mboxes` 中各邮箱说明符的可选名称 |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁（Hardware Spinlock）标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |
| `zephyr,deferred-init` | `boolean` | 延迟初始化（Deferred Initialization）：启动时不自动初始化设备，应由应用使用 `device_init()` 手动初始化 |
| `wakeup-source` | `boolean` | 标记设备可用作唤醒源（Wakeup Source）。设置该属性后，设备中会设置专门标志，通知系统此设备有唤醒能力。唤醒功能默认禁用，即中断不会唤醒系统；必要时可在运行期间启用 |
| `zephyr,pm-device-runtime-auto` | `boolean` | 初始化函数执行后，自动为设备配置运行时电源管理（Runtime Power Management） |
| `zephyr,disabling-power-states` | `phandles` | 会关闭该设备电源的电源状态（Power State）列表 |

本层 `reg-names` 的原始示例如下。设备树源码（Devicetree Source，DTS）中的 `uart` 是通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）节点名称，仅用于说明寄存器命名。

```dts
  / {
       soc {
           #address-cells = <1>;
           #size-cells = <1>;

           uart@1000 {
               reg = <0x1000 0x2000>, <0x3000 0x4000>;
               reg-names = "foo", "bar";
           };
       };
  };
```

其中 `uart@1000` 有两个寄存器块：`foo` 和 `bar` 是示例寄存器块名称；`foo` 的基址为 `0x1000`、大小为 `0x2000`；`bar` 的基址为 `0x3000`、大小为 `0x4000`。

## 878.2\_通道子节点属性

本层 `reg` 是通道标识（Channel Identifier），并非控制器寄存器地址；增益、参考源和采集时间是原页要求的必需配置。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `mux-buf-bypass` | `boolean` | 绕过MUX通道的高阻抗（High Impedance，Hi-Z）缓冲器 |
| `fifo-sel` | `int` | 选择接收输出结果的FIFO缓冲区，使用表后的 `IFX_AUTANALOG_SAR_FIFO_*` 常量；默认值：`0`；合法值：`0, 1, 2, 3, 4, 5, 6, 7, 8` |
| `reg` | `array` | **必需**。通道标识（Channel Identifier）；参见[重要属性](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props) |
| `zephyr,gain` | `string` | **必需**。增益（Gain）选择，各常量对应的倍率见通道表后的完整对照；合法值：`ADC_GAIN_1_6, ADC_GAIN_1_5, ADC_GAIN_1_4, ADC_GAIN_2_7, ADC_GAIN_1_3, ADC_GAIN_2_5, ADC_GAIN_1_2, ADC_GAIN_2_3, ADC_GAIN_4_5, ADC_GAIN_1, ADC_GAIN_2, ADC_GAIN_3, ADC_GAIN_4, ADC_GAIN_6, ADC_GAIN_8, ADC_GAIN_12, ADC_GAIN_16, ADC_GAIN_24, ADC_GAIN_32, ADC_GAIN_64, ADC_GAIN_128` |
| `zephyr,reference` | `string` | **必需**。参考电压源（Reference Source）选择，各常量对应的源见通道表后的完整对照；合法值：`ADC_REF_VDD_1, ADC_REF_VDD_1_2, ADC_REF_VDD_1_3, ADC_REF_VDD_1_4, ADC_REF_INTERNAL, ADC_REF_EXTERNAL0, ADC_REF_EXTERNAL1` |
| `zephyr,vref-mv` | `int` | 此通道选择的参考源电压，单位为毫伏（Millivolt，mV），便于应用在需要计算时取得该值。内部参考（Internal Reference）的电压通常可由专用ADC应用程序接口（Application Programming Interface，API）获取，因此通常无须设置本属性；其他参考源使用此属性可能有帮助 |
| `zephyr,acquisition-time` | `int` | **必需**。采集时间（Acquisition Time）。使用 `ADC_ACQ_TIME` 宏组合属性值，或传入 `ADC_ACQ_TIME_DEFAULT` 采用硬件默认设置，例如硬件不允许配置采集时间的情况 |
| `zephyr,differential` | `boolean` | 设置后选择差分输入模式（Differential Input Mode）；否则使用单端模式（Single-Ended Mode），但若设置 `zephyr,input-negative`，则会隐式选择差分模式 |
| `zephyr,input-positive` | `int` | ADC正输入（Positive Input），**仅供选择 `ADC_CONFIGURABLE_INPUTS` Kconfig选项的驱动使用** |
| `zephyr,input-negative` | `int` | ADC负输入（Negative Input），**仅供选择 `ADC_CONFIGURABLE_INPUTS` Kconfig选项的驱动使用**；指定此属性即隐式选择该通道的差分输入模式 |
| `zephyr,resolution` | `int` | 此通道使用的ADC分辨率（Resolution） |
| `zephyr,oversampling` | `int` | 此通道的过采样（Oversampling）设置。指定后，每个采样值由 `2^N` 次转换结果平均得到，N为属性提供的值 |
| `zephyr,current-source-pin` | `uint8-array` | 电流源（Current Source）的输出引脚选择，实际解释由驱动决定。**仅供选择 `ADC_CONFIGURABLE_EXCITATION_CURRENT_SOURCE_PIN` Kconfig选项的驱动使用** |
| `zephyr,vbias-pins` | `int` | 偏置电压（Bias Voltage）的输出引脚选择，实际解释由驱动决定。**仅供选择 `ADC_CONFIGURABLE_VBIAS_PIN` Kconfig选项的驱动使用** |

增益常量（Gain Constant）与倍率逐项对应如下；列出这些通用合法常量并不意味着每种硬件都支持所有档位。

| 增益常量 | 倍率 |
| --- | --- |
| `ADC_GAIN_1_6` | `1/6` |
| `ADC_GAIN_1_5` | `1/5` |
| `ADC_GAIN_1_4` | `1/4` |
| `ADC_GAIN_2_7` | `2/7` |
| `ADC_GAIN_1_3` | `1/3` |
| `ADC_GAIN_2_5` | `2/5` |
| `ADC_GAIN_1_2` | `1/2` |
| `ADC_GAIN_2_3` | `2/3` |
| `ADC_GAIN_4_5` | `4/5` |
| `ADC_GAIN_1` | `1` |
| `ADC_GAIN_2` | `2` |
| `ADC_GAIN_3` | `3` |
| `ADC_GAIN_4` | `4` |
| `ADC_GAIN_6` | `6` |
| `ADC_GAIN_8` | `8` |
| `ADC_GAIN_12` | `12` |
| `ADC_GAIN_16` | `16` |
| `ADC_GAIN_24` | `24` |
| `ADC_GAIN_32` | `32` |
| `ADC_GAIN_64` | `64` |
| `ADC_GAIN_128` | `128` |

参考源常量（Reference Constant）与来源如下。VDD表示供电电压（Supply Voltage）。

| 常量 | 参考源 |
| --- | --- |
| `ADC_REF_VDD_1` | VDD |
| `ADC_REF_VDD_1_2` | VDD/2 |
| `ADC_REF_VDD_1_3` | VDD/3 |
| `ADC_REF_VDD_1_4` | VDD/4 |
| `ADC_REF_INTERNAL` | 内部参考（Internal Reference） |
| `ADC_REF_EXTERNAL0` | 外部参考输入0（External Reference Input 0） |
| `ADC_REF_EXTERNAL1` | 外部参考输入1（External Reference Input 1） |

下列厂商常量均来自 `<dt-bindings/adc/infineon-autanalog-sar.h>`。

参考源编码：

| 常量 | 编码与含义 |
| --- | --- |
| `IFX_AUTANALOG_SAR_VREF_VDDA` | `0`：Vdda供电（默认） |
| `IFX_AUTANALOG_SAR_VREF_EXT` | `1`：外部参考 |
| `IFX_AUTANALOG_SAR_VREF_VBGR` | `2`：带隙参考（Bandgap Reference） |
| `IFX_AUTANALOG_SAR_VREF_VDDA_BY_2` | `3`：Vdda/2 |
| `IFX_AUTANALOG_SAR_VREF_PRB_OUT0` | `4`：PRB Vref0 |
| `IFX_AUTANALOG_SAR_VREF_PRB_OUT1` | `5`：PRB Vref1 |

正、负MUX输入缓冲器使用同一组功耗编码。电荷泵（Charge Pump）的启停也属于该模式。

| 常量 | 编码与含义 |
| --- | --- |
| `IFX_AUTANALOG_SAR_BUF_PWR_OFF` | `0`：关闭（默认） |
| `IFX_AUTANALOG_SAR_BUF_PWR_ULTRA_LOW` | `1`：超低功耗，电荷泵关闭 |
| `IFX_AUTANALOG_SAR_BUF_PWR_ULTRA_LOW_RAIL` | `2`：超低功耗，电荷泵开启 |
| `IFX_AUTANALOG_SAR_BUF_PWR_LOW_RAIL` | `4`：低功耗，电荷泵开启 |
| `IFX_AUTANALOG_SAR_BUF_PWR_MEDIUM_RAIL` | `6`：中等功耗，电荷泵开启，推荐值 |
| `IFX_AUTANALOG_SAR_BUF_PWR_HIGH_RAIL` | `8`：高功耗，电荷泵开启 |
| `IFX_AUTANALOG_SAR_BUF_PWR_ULTRA_HIGH_RAIL` | `10`：超高功耗，电荷泵开启 |

累加／平均编码：

| 常量 | 编码与含义 |
| --- | --- |
| `IFX_AUTANALOG_SAR_ACC_DISABLED` | `0`：禁用平均（默认） |
| `IFX_AUTANALOG_SAR_ACC_ACCUNDUMP` | `1`：累加后输出（Accumulate and Dump） |

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

输入输出通道说明符的单元名称（Specifier Cell Name）为 `input`。

本页没有已弃用的顶层专用属性。

---

[上一章：Infineon模数转换器绑定](P877_Infineon模数转换器绑定.md) · [下一章：Infineon自主模拟SAR队列绑定](P879_Infineon自主模拟SAR队列绑定.md) · [返回大纲](大纲.md)
