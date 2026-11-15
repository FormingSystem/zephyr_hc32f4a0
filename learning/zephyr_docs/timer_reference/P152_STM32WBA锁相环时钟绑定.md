---
id: learning.zephyr-docs.timer_reference.stmpllus-152
title: STM32WBA锁相环时钟绑定
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/st,stm32wba-pll-clock.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第152章\_STM32WBA锁相环时钟绑定

<a id="dtbinding-st-stm32wba-pll-clock"></a>

原文：[st,stm32wba-pll-clock](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/st,stm32wba-pll-clock.html)。读取日期：2026-10-13，`latest`。

`st,stm32wba-pll-clock`是 STMicroelectronics 的设备树绑定（Devicetree Binding），描述STM32WBA的PLL1节点。PLL 指锁相环（Phase-Locked Loop），VCO 指压控振荡器（Voltage-Controlled Oscillator）。

采用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=st,stm32wba-pll-clock)。

## 152.1\_输入源与频率计算

PLL通过输入预分频器（Prescaler）、VCO倍频系数（Multiplier）和输出分频系数（Divider）生成输出时钟。输入节点`clk_hse`表示高速外部时钟（High-speed External Clock，HSE），`clk_hsi`表示高速内部时钟（High-speed Internal Clock，HSI）。下式`f`表示频率（Frequency），MHz为兆赫（Megahertz）。

此绑定用于描述`PLL1`，输入可选`clk_hse`或`clk_hsi`。

PLL输入频率的允许范围为**4至16 MHz**，通过`PLLM`分频系数将输入调整到该范围。每个PLL最多有3路输出；P、Q、R输出各使用自己的分频系数，频率按下述官方原式计算。`with`表示附带的VCO频率关系，`to`和箭头标示输出用途。

公式中的`PLL_P`、`PLL_Q`、`PLL_R`是3个输出时钟标识，分别除以`PLLP`、`PLLQ`、`PLLR`；`PLLN`为VCO倍频系数，`PLLM`为输入分频系数。属性说明中的`DIVP`、`DIVQ`、`DIVR`分别表示P、Q、R输出分频系数。

```text
  f(PLL_P) = f(VCO clock) / PLLP
  f(PLL_Q) = f(VCO clock) / PLLQ
  f(PLL_R) = f(VCO clock) / PLLR

    with f(VCO clock) = f(PLL clock input) × (PLLN / PLLM)
```

VCOx频率范围为**128至544 MHz**。为了降低功耗（Power Consumption），原文建议将VCO配置为最低频率。

PLL输出频率不得超过**100 MHz**。

## 152.2\_节点专用属性

属性类型：`int`为整数，`boolean`为布尔属性，`string`为字符串，`string-array`为字符串数组，`array`为数值数组，`compound`为复合类型；`phandle`为节点引用（Phandle），`phandles`为节点引用列表，`phandle-array`为节点引用与说明符单元数组。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `#clock-cells` | `int` | **必需**。时钟说明符（Clock Specifier）所需的单元数量；固定值：`0` |
| `div-m` | `int` | **必需**。PLLx输入时钟预分频系数；范围：`1 to 8` |
| `mul-n` | `int` | **必需**。PLLx的VCO倍频系数；范围：`4 to 512` |
| `div-p` | `int` | **必需**。PLLx的`DIVP`分频系数；范围：`1 to 128` |
| `div-q` | `int` | PLLx的`DIVQ`分频系数；范围：`1 to 128` |
| `div-r` | `int` | **必需**。PLLx的`DIVR`分频系数；范围：`1 to 128` |

本页没有已弃用的节点专用属性。

## 152.3\_基础属性

以下31项属性继承自基础绑定（Base Binding），**并非全部一定适用于本兼容字符串**。表中涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）和硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `clocks` | `phandle-array` | **必需**。设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg` | `array` | 给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md) |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的名称；通用说明称其为可选名称，是否必须填写以本层的必需标记为准 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节 |
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

## 152.4\_寄存器块命名原例

以下为`reg-names`的原设备树源码（Devicetree Source，DTS）示例；`uart`为通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）节点。

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

`uart@1000`包含两个寄存器块（Register Block）：`foo`基址`0x1000`、大小`0x2000`；`bar`基址`0x3000`、大小`0x4000`。


---

[上一章：STM32WB锁相环时钟绑定](P151_STM32WB锁相环时钟绑定.md) · [下一章：STM32H5锁相环时钟绑定](P153_STM32H5锁相环时钟绑定.md) · [返回大纲](大纲.md)
