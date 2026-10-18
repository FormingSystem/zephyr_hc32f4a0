---
id: learning.zephyr-docs.pinctrl-adi-ambiq-arm-binding-reference.page-19
title: elan_em32-pinctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, pinctrl]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/elan,em32-pinctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第19章\_elan_em32-pinctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/elan,em32-pinctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="elan-em32-pinctrl"></a>
<a id="dtbinding-elan-em32-pinctrl"></a>
<a id="std-dtcompatible-elan-em32-pinctrl"></a>

兼容字符串（Compatible String）：`elan,em32-pinctrl`。厂商：[ Elan Microelectronic Corp. ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-elan)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=elan,em32-pinctrl)。

<a id="description"></a>

EM32引脚控制器（Pin Controller，EM32F967）。基于 `pincfg-node.yaml` 绑定。

注意：默认引脚配置是 `bias-disable` 与 `drive-push-pull`；当子节点未设置任何 `bias-*` 或 `drive-*` 属性时，应用这些默认配置。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 19.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

## 19.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
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

属性说明中的“重要属性”参见[设备树语法与结构](../devicetree/P003_语法与结构.md#dt-important-props)。

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pinmux` | `int` | **必需**。32位数值，编码端口、引脚、复用功能（Mux Function），以及可选的一次或两次IP_SHARE寄存器操作。位布局与 `include/zephyr/dt-bindings/pinctrl/em32f967-pinctrl.h` 及 `drivers/pinctrl/pinctrl_em32.c` 的解码一致：位[2:0]为3位复用功能；[6:3]为4位引脚编号0～15；位7为端口（0为PA，1为PB）；位8为 `io1_valid`（1表示有第一次IP_SHARE操作）；[13:9]为 `io1_shift`（IP_SHARE位位置0～31）；[15:14]为 `io1_width_m1`（字段宽度减1，0表示1位）；[19:16]为写入值 `io1_value`；位20为 `io2_valid`（1表示有第二次操作）；[25:21]、[27:26]、[31:28]依次为 `io2_shift`、`io2_width_m1`、`io2_value`。原始位布局表保留在下方。<br><br>复用字段只有3位，取值0～7；此SoC没有“Analog”或“GPIO=17”别名。0为 `EM32F967_GPIO` 普通GPIO；1为AF1（SPI1等）；2为AF2（UART等）；3为AF3（Timer、7816等）；4为AF4（I2C等）；5为AF5（I2C、WKUP等）；6为AF6（在PB4～PB7上保留）；7为AF7（PWM等）。选择 `EM32F967_GPIO` 时，引脚静态配置为普通GPIO，默认输入；在子节点加入 `output-low` 或 `output-high` 可驱动输出电平。<br><br>同一头文件提供两种辅助宏：`EM32F967_PINMUX(port, pin, mux)` 是向后兼容的三参数形式，只设置位[7:0]，IP_SHARE位[31:8]为0；驱动回退到内建 `em32_ioshare_table[]` 查表配置该引脚的IP_SHARE。`EM32F967_PINMUX_IO(port, pin, mux, ioshare)` 是四参数形式，`ioshare` 直接在说明符单元中嵌入一次或两次IP_SHARE读改写操作（Read-Modify-Write），无需查表。<br><br>构造 `ioshare` 时，`EM32F967_IO_NONE` 表示无操作；`EM32F967_IO_SET_BIT(pos)` 置位；`EM32F967_IO_CLR_BIT(pos)` 清位；`EM32F967_IO_SET_2BIT(pos, val)` 写2位字段；`EM32F967_IO_CLR_2BIT(pos)` 清2位字段；`EM32F967_IO1(shift, width, val)` 显式设置操作槽1；`EM32F967_IO2(shift, width, val)` 显式设置操作槽2，可与上述值按位或组合。 |
| `bias-pull-up-value` | `int` | 选择同一引脚同时设置 `bias-pull-up` 时连接哪一个内部上拉电阻；如果没有 `bias-pull-up` 则忽略此项，SoC的 `Z_PINCTRL_EM32_PINCFG_INIT()` 宏会将此值与该布尔属性相乘。1为弱上拉PU0（默认，等同传统 `bias-pull-up;`）；2为强上拉PU1。<br><br>原因是标准布尔属性 `bias-disable`、`bias-pull-up`、`bias-pull-down` 只能表达2位硬件上拉／下拉字段的四种状态中的三种。该属性在兼容现有设备树节点的同时补充PU1状态。IOPUPxCTRL中每针2位：`0b00` 为悬空（Floating），对应 `bias-disable` 或没有偏置属性；`0b01` 为PU0，对应 `bias-pull-up`，可附加 `bias-pull-up-value = <1>`；`0b10` 为PU1，需同时设置 `bias-pull-up` 和 `bias-pull-up-value = <2>`；`0b11` 为下拉PD，对应 `bias-pull-down`。<br><br>寄存器基地址为 `0x4003_0000`，PA偏移 `0x214`，PB偏移 `0x218`。PA0～6位于[13:0]，PA11～15位于[31:22]，PB位于[31:0]；每针字段[1:0]均为00悬空、01为PU0、10为PU1、11为PD（原表标为默认）。<br><br>PA0～6：在5V／3.3V／1.8V下，PU0分别为66kΩ／101kΩ／238kΩ，PU1为4.7kΩ／6.41kΩ／12.7kΩ，PD为15kΩ／21.8kΩ／49.6kΩ。PA11～15及PB：在3.3V／1.8V下，PU0为66kΩ／140kΩ，PU1为4.7kΩ／8.53kΩ，PD为15kΩ／25.2kΩ。原始字段和电阻值对照保留在下方。；默认值：`1`；合法值：`1, 2` |
| `drive-strength` | `int` | 引脚输出驱动强度（Drive Strength），采用1位硬件字段。使用数值，例如 `drive-strength = <1>;`。寄存器基地址 `0x4003_0000`，PA高驱动控制偏移 `0x21C`，PB偏移 `0x220`。0表示输出配置下的低驱动强度（默认），原文数据为4MHz时470µA（32mA）；1表示高驱动强度，原文数据为4MHz时490µA（65mA）、48MHz时5.8mA（68mA）。原文括号内外数值均保留，原始对照见下方。；默认值：`0`；合法值：`0, 1` |
| `bias-disable` | `boolean` | 禁用引脚的所有偏置（Bias）。 |
| `bias-pull-up` | `boolean` | 启用上拉电阻（Pull-Up Resistor）。 |
| `bias-pull-down` | `boolean` | 启用下拉电阻（Pull-Down Resistor）。 |
| `drive-push-pull` | `boolean` | 主动驱动高、低电平（Push-Pull）。 |
| `drive-open-drain` | `boolean` | 开漏驱动（Open Drain），实现硬件与（Hardware AND）。 |
| `output-low` | `boolean` | 将引脚设置为低电平输出模式（Output Low）。 |
| `output-high` | `boolean` | 将引脚设置为高电平输出模式（Output High）。 |

## EM32复用单元位布局与原始功能对照

```text
  bits [ 2:0]   mux function    (3 bits)
  bits [ 6:3]   pin number 0-15 (4 bits)
  bit  [ 7]     port: 0 = PA, 1 = PB
  bit  [ 8]     io1_valid       (1 = first IP_SHARE op present)
  bits [13:9]   io1_shift       (bit position 0-31 in IP_SHARE)
  bits [15:14]  io1_width_m1    (field width minus 1: 0 = 1 bit)
  bits [19:16]  io1_value       (value to write at io1_shift)
  bit  [20]     io2_valid       (1 = second IP_SHARE op present)
  bits [25:21]  io2_shift
  bits [27:26]  io2_width_m1
  bits [31:28]  io2_value
```

```text
  * 0 : EM32F967_GPIO  — plain GPIO function
  * 1 : EM32F967_AF1   — alternate function 1 (SPI1, …)
  * 2 : EM32F967_AF2   — alternate function 2 (UART, …)
  * 3 : EM32F967_AF3   — alternate function 3 (Timer, 7816, …)
  * 4 : EM32F967_AF4   — alternate function 4 (I2C, …)
  * 5 : EM32F967_AF5   — alternate function 5 (I2C, WKUP, …)
  * 6 : EM32F967_AF6   — alternate function 6 (reserved on PB4-PB7)
  * 7 : EM32F967_AF7   — alternate function 7 (PWM, …)
```

## EM32上下拉字段与电阻原表

```text
  0b00 floating <- bias-disable        (or no bias property)
  0b01 PU0       <- bias-pull-up        [+ bias-pull-up-value = <1>]
  0b10 PU1       <- bias-pull-up         + bias-pull-up-value = <2>
  0b11 PD        <- bias-pull-down

Base Address 0x4003_0000 Offset 0x214 for GPIO PORT A (PA)
Base Address 0x4003_0000 Offset 0x218 for GPIO PORT B (PB)

GPIO Port A: PA0~6(Bit 13~0) PU0/PU1/PD:[1:0]
  00: Floating
  01: PU0 (Pull Up 5V→66K,  3.3V→101K, 1.8V→238K)
  10: PU1 (Pull Up 5V→4.7K,  3.3V→6.41K, 1.8V→12.7K)
  11: PD (Pull Down 5V→15K,  3.3V→21.8K, 1.8V→49.6K) (Default)

GPIO Port A: PA11~15(Bit 31~22) PU0/PU1/PD:[1:0]
  00: Floating
  01: PU0 (Pull Up 3.3V→66K, 1.8V→140K)
  10: PU1 (Pull Up 3.3V→4.7K, 1.8V→8.53K)
  11: PD (Pull Down 3.3V→15K, 1.8V→25.2K) (Default)

GPIO Port B(PB)(Bit 31~0) PU0/PU1/PD:[1:0]
  00: Floating
  01: PU0 (Pull Up 3.3V→66K, 1.8V→140K)
  10: PU1 (Pull Up 3.3V→4.7K, 1.8V→8.53K)
  11: PD (Pull Down 3.3V→15K, 1.8V→25.2K) (Default)
```

## EM32驱动强度原始数据

```text
Base Address 0x4003_0000 Offset 0x21C (PA high-drive control)
Base Address 0x4003_0000 Offset 0x220 (PB high-drive control)

0 - low drive strength when pin is configured as output (default)
    4Mhz:  470uA(32mA)

1 - high drive strength when pin is configured as output
    4Mhz:  490uA(65mA),
    48Mhz: 5.8mA(68mA)
```

## 19.3\_寄存器块命名原例

以下设备树源码（Devicetree Source，DTS）演示 `reg-names` 命名；`uart` 指通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）。

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

`uart@1000` 节点有两个寄存器块（Register Block）：一个基址为 `0x1000`、大小为 `0x2000`、名称为 `foo`；另一个基址为 `0x3000`、大小为 `0x4000`、名称为 `bar`。

---

[上一章](P018_brcm_bcm2712-pinctrl.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P020_ene_kb106x-pinctrl.md)
