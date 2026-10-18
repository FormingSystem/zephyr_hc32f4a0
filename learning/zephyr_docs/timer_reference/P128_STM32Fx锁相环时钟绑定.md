---
id: learning.zephyr-docs.timer_reference.stmrcc-128
title: STM32Fx锁相环时钟绑定
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/st,stm32fx-pll-clock.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第128章\_STM32Fx锁相环时钟绑定

<a id="dtbinding-st-stm32fx-pll-clock"></a>

原文：[st,stm32fx-pll-clock](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/st,stm32fx-pll-clock.html)。读取日期：2026-10-13，`latest`。

`st,stm32fx-pll-clock`是 STMicroelectronics 的设备树绑定（Devicetree Binding）。

采用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=st,stm32fx-pll-clock)。

本绑定描述 STM32F2、STM32F4、STM32F7 片上系统（System on Chip，SoC）的锁相环（Phase-Locked Loop，PLL），可用于这些芯片上的`PLL`、`PLLI2S`和`PLLSAI`；后两者保留硬件模块标识，分别涉及芯片间音频总线（Inter-IC Sound，I²S）和串行音频接口（Serial Audio Interface，SAI）。输入时钟取`clk_hse`高速外部（High-speed External，HSE）或`clk_hsi`高速内部（High-speed Internal，HSI）之一。

## 128.1\_输出频率与共享输入

PLL 最多提供3路输出，分别由输出标识`PLL_P`、`PLL_Q`、`PLL_R`表示。每路频率按下式计算；`f`表示频率（Frequency），VCO 指压控振荡器（Voltage-Controlled Oscillator），`PLLM`是输入分频系数，`PLLN`是倍频系数，`PLLP``PLLQ``PLLR`是对应输出分频系数：

```text
  f(PLL_P) = f(VCO clock) / PLLP
  f(PLL_Q) = f(VCO clock) / PLLQ
  f(PLL_R) = f(VCO clock) / PLLR

    with f(VCO clock) = f(PLL clock input) × (PLLN / PLLM)
```

最后一行表示 VCO 时钟频率等于 PLL 输入频率乘以`PLLN / PLLM`。部分 SoC 的 Q、R 输出还具有额外分频器。

**同一 SoC 上 PLL／PLLI2S／PLLSAI 共享 PLL 输入时钟，因此必须设置相同的输入源**。这与部分芯片的 M 分频系数是否独立是两件事，具体见属性说明。

## 128.2\_节点专用属性

属性类型：`int`为整数，`boolean`为布尔属性，`string`为字符串，`string-array`为字符串数组，`array`为数值数组，`compound`为复合类型；`phandle`为节点引用（Phandle），`phandles`为节点引用列表，`phandle-array`为节点引用与说明符单元数组。

CPU 指中央处理器（Central Processing Unit），DMA 指直接存储器访问（Direct Memory Access）；Hz 为赫兹（Hertz），MHz 为兆赫（Megahertz）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `#clock-cells` | `int` | **必需**。时钟说明符（Clock Specifier）所需的单元数量；固定值：`0` |
| `div-m` | `int` | **必需**。PLL输入时钟分频系数。在STM32F411、F412、F413、F423、F446上，M分频系数独立于其他PLL；其他SoC的PLL、PLLSAI、PLLI2S共享M，因此一起使用时**必须设为相同值**；范围：`2 to 63` |
| `mul-n` | `int` | **必需**。VCO倍频系数。**STM32F2x和STM32F401有单独的有效范围`[192 432]`**；不能仅套用下列一般范围；范围：`50 to 432` |
| `div-p` | `int` | PLL_P输出分频系数。主PLL：所有SoC可用。PLLI2S：仅STM32F446、STM32F74x及更高型号可用。PLLSAI：仅STM32F446、F469、F479及全部STM32F7x可用；合法值：`2, 4, 6, 8` |
| `div-q` | `int` | PLL_Q输出分频系数。主PLL：所有SoC可用。PLLI2S：仅STM32F412、F413、F423、F427、F429、F437、F439、F446、F469、F479及全部STM32F7x可用。PLLSAI：仅STM32F427、F429、F437、F439、F446、F469、F479及全部STM32F7x可用；范围：`2 to 15` |
| `post-div-q` | `int` | PLL_Q之后的分频系数（Post-divider）。PLLI2S和PLLSAI均仅在STM32F427、F429、F437、F439、F446、F469、F479及全部STM32F7x可用。**若使用`div-q`，且本属性适用于该SoC，则必须定义本属性**；范围：`1 to 32` |
| `div-r` | `int` | PLL_R输出分频系数。主PLL：仅STM32F410、F412、F413、F423、F446、F469、F479、F769、F779可用。PLLI2S：除STM32F410以外的所有SoC可用。PLLSAI：仅STM32F427、F429、F437、F439、F469、F479及STM32F74x及更高型号可用；范围：`2 to 7` |
| `post-div-r` | `int` | PLL_R之后的分频系数。主PLL及PLLI2S：均仅STM32F413、F423可用。PLLSAI：仅STM32F427、F429、F437、F439、F469、F479及STM32F74x及更高型号可用。**若使用`div-r`，且本属性适用于该SoC，则必须定义本属性**；合法值：`2, 4, 8, 16` |

本页没有已弃用的节点专用属性。

## 128.3\_基础属性

以下属性继承自基础绑定（Base Binding），**并非全部一定适用于本兼容字符串**。表中还涉及中断（Interrupt）、时钟（Clock）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）和硬件自旋锁（Hardware Spinlock）。

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

## 128.4\_寄存器块命名原例

以下为`reg-names`原设备树源码（Devicetree Source，DTS）示例；`uart`为通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）节点名称。

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

`uart@1000`包含两个寄存器块（Register Block）：`foo`的基址`0x1000`、大小`0x2000`；`bar`的基址`0x3000`、大小`0x4000`。


---

[上一章：STM32F4复位与时钟控制绑定](P127_STM32F4复位与时钟控制绑定.md) · [下一章：STM32高速外部时钟绑定](P129_STM32高速外部时钟绑定.md) · [返回大纲](大纲.md)
