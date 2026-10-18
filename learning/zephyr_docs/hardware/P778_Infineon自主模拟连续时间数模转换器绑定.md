---
id: learning.zephyr-docs.hardware.dacrest-7
title: Infineon自主模拟连续时间数模转换器绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/dac/infineon,autanalog-ctdac.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第778章\_Infineon自主模拟连续时间数模转换器绑定

<a id="dtbinding-infineon-autanalog-ctdac"></a>

原文：[infineon,autanalog-ctdac](https://docs.zephyrproject.org/latest/build/dts/api/bindings/dac/infineon,autanalog-ctdac.html)。读取日期：2026-10-13，`latest`。

`infineon,autanalog-ctdac` 是设备树绑定（Devicetree Binding），描述Infineon PSOC Edge自主模拟（Autonomous Analog，AutAnalog）子系统中的连续时间数模转换器（Continuous Time Digital-to-Analog Converter，CTDAC）配置。下文DAC指数模转换器（Digital-to-Analog Converter）。

驱动为 [`drivers/dac/dac_infineon_autanalog_ctdac.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/dac_infineon_autanalog_ctdac.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,autanalog-ctdac)。

## 778.1\_直接写值与自主波形通道

CTDAC是AutAnalog内的12位连续时间分段数模转换器（Segmented DAC），支持直接输出、带缓冲且仅用于内部连接的输出，以及带缓冲并用于内部和外部连接的输出，可选择参考电压源并启用采样保持（Sample-and-Hold）。初始化CTDAC前，必须先设置其所属的[AutAnalog子系统](P720_Infineon自主模拟子系统绑定.md)。

固件（Firmware，FW）通道15通过标准Zephyr DAC应用程序接口（Application Programming Interface，API）直接写值，是简单DAC输出的默认通道。波形通道0至14通过自主控制器（Autonomous Controller，AC）状态机（State Machine）输出波形，编号直接对应硬件通道0至14；查找表（Look-Up Table，LUT）的地址区间由子节点配置，波形数据在运行时加载。

后文CTB指连续时间模块（Continuous Time Block），OA指运算放大器（Operational Amplifier），PRB指可编程参考模块（Programmable Reference Block），PTCOMP指可编程阈值比较器（Programmable Threshold Comparator），SAR ADC指逐次逼近寄存器型模数转换器（Successive Approximation Register Analog-to-Digital Converter）。Vdda、Vssa、Vref分别为模拟供电、模拟地和参考电压标识。

## 778.2\_控制器节点专用属性

本节属性作用于控制器节点。`int` 为整数，`array` 为数值数组，`string` 为字符串，`boolean` 为布尔属性，`phandle` 为节点引用（Phandle），`phandles` 为引用列表，`phandle-array` 为引用与说明单元数组，`string-array` 为字符串数组。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `#io-channel-cells` | `int` | **必需**。输入输出通道说明符（I/O Channel Specifier）中的单元数量（Cell Count）；固定值：`1` |
| `clk-dst` | `int` | **必需**。此CTDAC实例的外设时钟目标编号（Peripheral Clock Destination ID） |
| `vref-source` | `int` | 选择DAC参考电压源（Reference Voltage Source）；使用 `dt-bindings/dac/infineon-autanalog-ctdac.h` 中的 `IFX_AUTANALOG_CTDAC_VREF_*` 常量，完整对应关系见后文；默认值：`0x100`；合法值：`0x100, 0, 1, 2, 3, 4, 6, 7` |
| `topology` | `int` | 选择DAC输出拓扑（Output Topology）；使用同一头文件中的 `IFX_AUTANALOG_CTDAC_TOPO_*` 常量，完整对应关系见后文；默认值：`4`；合法值：`0, 1, 2, 3, 4` |
| `ref-buf-pwr` | `int` | 参考电压缓冲器的功耗模式（Power Mode），使用同一头文件中的 `IFX_AUTANALOG_CTDAC_REF_BUF_PWR_*` 常量。电流与增益带宽（Gain Bandwidth，GBW）见后表；选择Vdda参考路径时，必须设为OFF（0），因为该路径不使用参考缓冲器；默认值：`0`；合法值：`0, 1, 2, 4, 6, 7, 8, 10` |
| `out-buf-pwr` | `int` | 输出电压缓冲器的功耗模式，使用同一头文件中的 `IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_*` 常量，电流及驱动能力见后表。**采用内部或外部缓冲拓扑时必须设为非OFF值**；默认值：`0`；合法值：`0, 1, 2, 4, 6, 8, 10` |
| `lp-mode` | `boolean` | 请求自主模拟子系统低功耗（Low Power，LP）运行。设置后，父级AutAnalog多功能设备（Multi-Function Device，MFD）的基本模式状态转换表（State Transition Table，STT）使AC各状态进入LP运行。其他任一AutAnalog子外设（SAR ADC、CTB、PTCOMP、PRB）设置 `lp-mode` 也会激活LP模式；高级模式（`ac-states`）应改用各状态自己的 `ac-lp-mode` |
| `lp-div-dac` | `int` | DAC低功耗时钟分频（Clock Divider）配置，有效范围0至1023；硬件实际除数为 `lp-div-dac + 1`；默认值：`0` |
| `bottom-sel` | `boolean` | R-2R电阻梯形网络（R-2R Resistor Ladder）底端连接选择；设置后底端接参考电压Vref，而不是模拟地Vssa |
| `disabled-mode` | `boolean` | DAC禁用时的输出行为：设置后仍驱动Vssa或Vref，取决于 `bottom-sel`；否则输出呈三态（Tri-State） |
| `deglitch` | `boolean` | 启用去毛刺（De-Glitch）功能，通过输出路径上的开关在编码转换期间消隐毛刺 |
| `deglitch-time` | `int` | 去毛刺时间，单位为DAC时钟周期；范围0至255，实际周期数为 `deglitch-time + 1`。仅启用 `deglitch` 时使用；默认值：`0` |
| `sign` | `boolean` | 设置后，将DAC输入数据解释为12位有符号二进制补码（Signed Two’s Complement）；否则为无符号值（Unsigned Value） |
| `sample-time` | `int` | 采样时间（Sample Time）的DAC时钟周期配置，范围0至255；硬件实际采样周期数为 `sample-time + 1`；默认值：`0` |
| `step-val` | `array` | 波形地址递增的步长（Step Value），数组必须恰有3项：`step-val[0]`、`step-val[1]`、`step-val[2]`；每个波形通道通过其 `step-sel` 选择一项；默认值：`[0, 0, 0]` |
| `limit-cfg-0` | `array` | 限值槽0的范围检测（Range Detection）配置，格式为三个单元 `<condition low-threshold high-threshold>`。条件使用同一头文件中的 `IFX_AUTANALOG_CTDAC_LIMIT_*` 常量，比较边界见后表；波形通道通过 `stat-sel = <1>` 引用此槽 |
| `limit-cfg-1` | `array` | 限值槽1的范围检测配置，格式同 `limit-cfg-0`；通过 `stat-sel = <2>` 引用 |
| `limit-cfg-2` | `array` | 限值槽2的范围检测配置，格式同 `limit-cfg-0`；通过 `stat-sel = <3>` 引用 |

## 778.3\_控制器资源

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。CTDAC在AutAnalog子系统内的基址偏移（Base Address Offset） |
| `clocks` | `phandle-array` | **必需**。提供CTDAC外设时钟的 `infineon,peri-div` 分频器节点引用；分频器位于PERI0的组2（CLK_HF9）。每个实例需要独立分频通道：DAC0对应 `PCLK_PASS_CLOCK_DAC0`（peri0、组2、索引0）；DAC1对应 `PCLK_PASS_CLOCK_DAC1`（peri0、组2、索引1） |

通道说明单元名称（Specifier Cell Name）为 `output`，即输出；`io-channel` 说明符包含一个单元。

## 778.4\_通道子节点属性

这些属性用于DAC的通道子节点，其中 `reg` 是通道编号，与控制器节点的寄存器地址含义不同。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `start-addr` | `int` | DAC查找表（Look-Up Table，LUT）起始地址，范围0至511；**波形通道（reg为0至14）必须提供** |
| `end-addr` | `int` | DAC查找表结束地址，范围0至511，必须大于或等于 `start-addr`；**波形通道（reg为0至14）必须提供** |
| `op-mode` | `int` | 本通道波形工作模式（Waveform Operating Mode）；使用同一头文件中的 `IFX_AUTANALOG_CTDAC_OP_*` 常量，完整模式表见后文；默认值：`3`；合法值：`0, 1, 2, 3, 4, 5, 6, 7` |
| `sample-and-hold` | `boolean` | 为本通道启用采样保持（Sample-and-Hold） |
| `step-sel` | `int` | 地址递增步长选择；使用同一头文件中的 `IFX_AUTANALOG_CTDAC_STEP_SEL_*` 常量。DISABLED（0）使用默认步长1；常量后缀0／1／2分别编码1／2／3，使用 `stepVal[0]`／`stepVal[1]`／`stepVal[2]`；默认值：`0`；合法值：`0, 1, 2, 3` |
| `stat-sel` | `int` | 范围检测／状态选择（Status Selector）；使用同一头文件中的 `IFX_AUTANALOG_CTDAC_STAT_SEL_*` 常量。DISABLED（0）不验证范围；常量后缀0／1／2分别编码1／2／3，使用 `chLimitCfg[0]`／`chLimitCfg[1]`／`chLimitCfg[2]`；默认值：`0`；合法值：`0, 1, 2, 3` |
| `reg` | `array` | **必需**。通道标识（Channel Identifier） |
| `zephyr,resolution` | `int` | 此通道使用的DAC分辨率（Resolution） |
| `zephyr,buffered` | `boolean` | 为此通道启用输出缓冲器（Output Buffer） |
| `zephyr,internal` | `boolean` | 为此通道启用内部输出路径（Internal Output Path） |
| `zephyr,vref-mv` | `int` | 指定此通道所选参考源的电压，单位为毫伏（Millivolt，mV），使应用在需要计算时能够获取该值 |

## 778.5\_参考源与输出拓扑常量

下列常量均来自 `dt-bindings/dac/infineon-autanalog-ctdac.h`，电压为伏（Volt，V）。

| 常量 | 编码 | 含义 |
| --- | --- | --- |
| `IFX_AUTANALOG_CTDAC_VREF_VDDA` | `0x100` | Vdda供电，典型1.8 V |
| `IFX_AUTANALOG_CTDAC_VREF_VBGR` | `0` | 带隙参考（Bandgap Reference），典型0.9 V |
| `IFX_AUTANALOG_CTDAC_VREF_CTB0_OA0` | `1` | CTB0运放0输出 |
| `IFX_AUTANALOG_CTDAC_VREF_CTB0_OA1` | `2` | CTB0运放1输出 |
| `IFX_AUTANALOG_CTDAC_VREF_CTB1_OA0` | `3` | CTB1运放0输出 |
| `IFX_AUTANALOG_CTDAC_VREF_CTB1_OA1` | `4` | CTB1运放1输出 |
| `IFX_AUTANALOG_CTDAC_VREF_PRB_OUT0` | `6` | PRB Vref0 |
| `IFX_AUTANALOG_CTDAC_VREF_PRB_OUT1` | `7` | PRB Vref1 |

| 常量 | 编码 | 含义 |
| --- | --- | --- |
| `IFX_AUTANALOG_CTDAC_TOPO_DIRECT` | `0` | 直接输出（Direct Output） |
| `IFX_AUTANALOG_CTDAC_TOPO_DIRECT_TRACK_CAP` | `1` | 直接输出，带跟踪电容（Track Capacitor） |
| `IFX_AUTANALOG_CTDAC_TOPO_DIRECT_TRACK_HOLD` | `2` | 直接输出，带跟踪和保持电容（Hold Capacitor） |
| `IFX_AUTANALOG_CTDAC_TOPO_BUFFERED_INTERNAL` | `3` | 带缓冲，仅内部连接 |
| `IFX_AUTANALOG_CTDAC_TOPO_BUFFERED_EXTERNAL` | `4` | 带缓冲，内部和外部连接 |

**译注：缓冲器说明中的 `vdda`、`buffered-internal`、`buffered-external` 是模式名称，本页对应属性类型为整数。**分别使用上表VDDA（0x100）、BUFFERED_INTERNAL（3）、BUFFERED_EXTERNAL（4）或相应常量，不将这些模式名称作为字符串填入属性。

## 778.6\_参考缓冲器与输出缓冲器档位

电流单位为微安（Microampere，µA）和毫安（Milliampere，mA）；GBW为增益带宽，单位为千赫兹（Kilohertz，kHz）或兆赫兹（Megahertz，MHz）。“电荷泵开启”仅标在原文明确说明的档位；未标者不额外推断电荷泵状态。

| 常量 | 编码 | 含义 |
| --- | --- | --- |
| `IFX_AUTANALOG_CTDAC_REF_BUF_PWR_OFF` | `0` | 缓冲器关闭 |
| `IFX_AUTANALOG_CTDAC_REF_BUF_PWR_ULTRA_LOW` | `1` | 15 µA，30 kHz GBW |
| `IFX_AUTANALOG_CTDAC_REF_BUF_PWR_ULTRA_LOW_RAIL` | `2` | 电荷泵（Charge Pump）开启，35 µA，30 kHz GBW |
| `IFX_AUTANALOG_CTDAC_REF_BUF_PWR_LOW_RAIL` | `4` | 电荷泵开启，150 µA，350 kHz GBW |
| `IFX_AUTANALOG_CTDAC_REF_BUF_PWR_MEDIUM_RAIL` | `6` | 电荷泵开启，200 µA，700 kHz GBW |
| `IFX_AUTANALOG_CTDAC_REF_BUF_PWR_HIGH` | `7` | 400 µA，1.75 MHz GBW；Vref ≤ 0.9 V |
| `IFX_AUTANALOG_CTDAC_REF_BUF_PWR_HIGH_RAIL` | `8` | 电荷泵开启，600 µA，1.75 MHz GBW |
| `IFX_AUTANALOG_CTDAC_REF_BUF_PWR_ULTRA_HIGH_RAIL` | `10` | 电荷泵开启，800 µA，2.8 MHz GBW |

| 常量 | 编码 | 含义 |
| --- | --- | --- |
| `IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_OFF` | `0` | 缓冲器关闭 |
| `IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_ULTRA_LOW` | `1` | 15 µA，驱动10 µA |
| `IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_ULTRA_LOW_RAIL` | `2` | 电荷泵开启，35 µA，驱动10 µA |
| `IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_LOW_RAIL` | `4` | 电荷泵开启，150 µA，驱动100 µA |
| `IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_MEDIUM_RAIL` | `6` | 电荷泵开启，200 µA，驱动1 mA |
| `IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_HIGH_RAIL` | `8` | 电荷泵开启，600 µA，驱动1 mA |
| `IFX_AUTANALOG_CTDAC_OUT_BUF_PWR_ULTRA_HIGH_RAIL` | `10` | 电荷泵开启，800 µA，驱动10 mA |

## 778.7\_范围检测与波形模式常量

下表Value表示检测值，low／high分别为低／高阈值；不等号严格按原文保留，注意ABOVE与OUTSIDE对等于high的处理不同。

| 常量 | 编码 | 含义 |
| --- | --- | --- |
| `IFX_AUTANALOG_CTDAC_LIMIT_BELOW` | `0` | `Value < low`，低于下限 |
| `IFX_AUTANALOG_CTDAC_LIMIT_INSIDE` | `1` | `low <= Value < high`，位于范围内 |
| `IFX_AUTANALOG_CTDAC_LIMIT_ABOVE` | `2` | `Value > high`，高于上限 |
| `IFX_AUTANALOG_CTDAC_LIMIT_OUTSIDE` | `3` | `Value < low OR Value >= high`，位于范围外 |

| 常量 | 编码 | 含义 |
| --- | --- | --- |
| `IFX_AUTANALOG_CTDAC_OP_OS_ONE_QUAD` | `0` | 单次（One-Shot），一个象限（Quadrant） |
| `IFX_AUTANALOG_CTDAC_OP_OS_TWO_QUAD` | `1` | 单次，两个象限 |
| `IFX_AUTANALOG_CTDAC_OP_OS_FOUR_QUAD` | `2` | 单次，四个象限 |
| `IFX_AUTANALOG_CTDAC_OP_CONT_ONE_QUAD` | `3` | 连续（Continuous），一个象限 |
| `IFX_AUTANALOG_CTDAC_OP_CONT_TWO_QUAD` | `4` | 连续，两个象限 |
| `IFX_AUTANALOG_CTDAC_OP_CONT_FOUR_QUAD` | `5` | 连续，四个象限 |
| `IFX_AUTANALOG_CTDAC_OP_ADDR` | `6` | 外部地址模式（External Address Mode） |
| `IFX_AUTANALOG_CTDAC_OP_DATA` | `7` | 外部数据模式（External Data Mode） |

| 常量 | 编码 | 含义 |
| --- | --- | --- |
| `IFX_AUTANALOG_CTDAC_STEP_SEL_DISABLED` | `0` | 步长为1，默认行为 |
| `IFX_AUTANALOG_CTDAC_STEP_SEL_0` | `1` | 使用 `stepVal[0]` |
| `IFX_AUTANALOG_CTDAC_STEP_SEL_1` | `2` | 使用 `stepVal[1]` |
| `IFX_AUTANALOG_CTDAC_STEP_SEL_2` | `3` | 使用 `stepVal[2]` |

| 常量 | 编码 | 含义 |
| --- | --- | --- |
| `IFX_AUTANALOG_CTDAC_STAT_SEL_DISABLED` | `0` | 不验证范围 |
| `IFX_AUTANALOG_CTDAC_STAT_SEL_0` | `1` | 使用 `chLimitCfg[0]` |
| `IFX_AUTANALOG_CTDAC_STAT_SEL_1` | `2` | 使用 `chLimitCfg[1]` |
| `IFX_AUTANALOG_CTDAC_STAT_SEL_2` | `3` | 使用 `chLimitCfg[2]` |

没有已弃用的控制器专用属性。以下为控制器继承的基础属性，不保证全部适用于本绑定；必需性以本页标记为准。

## 778.8\_状态、兼容字符串与寄存器

本页 `int` 为整数，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`boolean` 为布尔属性，`compound` 为复合类型。**节点引用（Phandle）**用来指向其他节点；`phandle-array` 表示节点引用及其说明单元，`phandles` 表示节点引用列表。

`status` 的类型为 `string`，描述节点所代表硬件或其他资源的运行状态。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将它视为不存在。合法值为 `okay`、`disabled`、`reserved`、`fail`、`fail-sss`。详见《设备树规范》（Devicetree Specification）v0.4 第 2.3.4 节。

`compatible` 的类型为 `string-array`，是**必需属性**。它用字符串列表定义节点代表的硬件或其他资源类型；设备驱动检查特定兼容字符串，以寻找应由自己管理的节点。推荐格式为 `vendor,device`，其中 `vendor` 是厂商简称，`device` 通常取自数据手册。多个值应按从最具体到最通用排列，使某一通用家族的具体设备能匹配当前可用的最具体驱动。详见规范 v0.4 第 2.3.1 节。


`reg-names` 的类型为 `string-array`，为 `reg` 中各寄存器块提供可选名称。以下保留官方示例；`#address-cells` 和 `#size-cells` 分别声明地址与长度使用的 32 位单元数。

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

`uart@1000` 节点有两个寄存器块：名称 `foo` 对应基址 `0x1000`、大小 `0x2000`；名称 `bar` 对应基址 `0x3000`、大小 `0x4000`。这里 uart 是**通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）**节点名称，示例只是演示寄存器块命名。

## 778.9\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 778.10\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 778.11\_DMA、输入输出与邮箱通道

**直接存储器访问（Direct Memory Access，DMA）**属性描述设备的 DMA 能力、通道和地址映射；输入输出（Input/Output，I/O）及邮箱（Mailbox）属性描述关联通道。IPM 是**处理器间消息（Inter-Processor Messaging）**接口。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `dma-coherent` | `boolean` | 表示设备支持一致性 DMA 操作，见规范 v0.4 第 2.3.10 节 |
| `dmas` | `phandle-array` | 与设备相关的 DMA 通道说明符 |
| `dma-names` | `string-array` | `dmas` 中各 DMA 通道说明符的可选名称 |
| `dma-ranges` | `compound` | 定义总线物理地址空间与其父总线物理地址空间之间的映射或转换，见规范 v0.4 第 2.3.9 节 |
| `io-channels` | `phandle-array` | 与设备相关的 I/O 通道说明符 |
| `io-channel-names` | `string-array` | `io-channels` 中各通道说明符的可选名称 |
| `mboxes` | `phandle-array` | 与设备相关的邮箱/IPM 通道说明符 |
| `mbox-names` | `string-array` | `mboxes` 中各邮箱说明符的可选名称 |

## 778.12\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 778.13\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：MicrochipG2数模转换器绑定](P777_MicrochipG2数模转换器绑定.md) · [下一章：Infineon斜坡发生器数模转换器绑定](P779_Infineon斜坡发生器数模转换器绑定.md) · [返回大纲](大纲.md)
