---
id: learning.zephyr-docs.pinctrl-nxp-pico-binding-reference.page-14
title: nxp_mcux-rt266x-pinctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, pinctrl]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/nxp,mcux-rt266x-pinctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第14章\_nxp_mcux-rt266x-pinctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/nxp,mcux-rt266x-pinctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-mcux-rt266x-pinctrl"></a>
<a id="dtbinding-nxp-mcux-rt266x-pinctrl"></a>
<a id="std-dtcompatible-nxp-mcux-rt266x-pinctrl"></a>

兼容字符串（Compatible String）：`nxp,mcux-rt266x-pinctrl`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,mcux-rt266x-pinctrl)。

<a id="description"></a>

MCUX RT266x SoC设备树中，此节点使用 `pinctrl` 标签。

RT10xx／RT11xx／RT118x分别提供SW_MUX_CTL与SW_PAD_CTL寄存器，而RT266x的每个焊盘由单一的组合IOMUXC PIO寄存器控制。因此本绑定直接描述PIO焊盘字段，由RT2661、RT2662、RT2663及未来采用同一IOMUXC的RT266x器件共用。

组的mux、mode、input、daisy、cfg字段选择待配置引脚，其余设备树属性设置配置值。下方LPUART0原例选择PIO3_30和PIO3_31的TXD、RXD，驱动强度为 `50-ohm`、压摆率为 `fast`。

属性对IOMUXC PIO的影响：`drive-open-drain` 设置ODENA=1，但仅PIO0～PIO4有该字段，PIO5／6／7没有；`input-enable` 设置IBENA=1，启用输入缓冲器／接收器；`bias-pull-down` 设置PULLENA=0b01；`bias-pull-up` 设置0b10；`bias-disable` 设置0b00；`slew-rate` 以枚举索引设置SLEWRATE；`drive-strength` 以枚举索引设置DRIVE。

仅提供必需属性时，PULLENA=0b00（禁用上下拉），IBENA=0，ODENA=0，SLEWRATE=0b00（低），DRIVE=0b00（100Ω）。原始代码与字段对照保留在下方。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 14.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

## 14.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg` | `array` | 给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
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

<a id="grandchild-node-properties"></a>

## 孙节点属性（Grandchild Properties）

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pinmux` | `phandles` | **必需**。此组的引脚复用选择。可用选项列表见SoC级IOMUXC DTSI文件。 |
| `drive-strength` | `string` | 输出驱动阻抗（Output Driver Impedance），设置IOMUXC PIO的DRIVE字段。列表按寄存器编码依次为100Ω（0b00，默认复位状态）、66Ω（0b01）、50Ω（0b10）、33Ω（0b11），与SDK头文件的 `IOMUXC_PIO_DRIVE` 编码一致；阻抗越低，驱动越强。<br><br>使用字符串枚举而非整数，与本绑定的 `slew-rate` 和其他NXP引脚绑定一致。`DT_ENUM_IDX` 读取的是值在列表中的位置，而非数字本身；整数类型会暗示存在实际并未发生的算术运算。<br><br>此属性有意不设置绑定默认值。省略时DRIVE保持100Ω复位值，因此默认值本来就多余；而且绑定默认值会自动填入每个组，导致无法区分用户显式指定与绑定填充，从而破坏拒绝在无DRIVE字段的PIO0～PIO4上使用本属性的构建期检查。<br><br>只有PIO5、PIO6、PIO7具有DRIVE字段。对于PIO0（VBAT）、PIO1（WAKE）和PIO2／PIO3／PIO4（MAIN），原文说明此属性不起作用，也不会写入。；合法值：`100-ohm, 66-ohm, 50-ohm, 33-ohm` |
| `slew-rate` | `string` | 焊盘压摆率（Slew Rate），设置IOMUXC PIO的SLEWRATE字段。列表依次映射为low（0b00，默认）、medium（0b01）、fast（0b10）、high（0b11）。只有PIO5／6／7的SLEWRATE为2位；PIO0、PIO1、PIO2／3／4只有1位，因此任何高于 `low` 的选项都选择该焊盘唯一的快速设置。；默认值：`low`；合法值：`low, medium, fast, high` |
| `bias-disable` | `boolean` | 禁用引脚的所有偏置（Bias）。 |
| `bias-pull-up` | `boolean` | 启用上拉电阻（Pull-Up Resistor）。 |
| `bias-pull-down` | `boolean` | 启用下拉电阻（Pull-Down Resistor）。 |
| `drive-open-drain` | `boolean` | 开漏驱动（Open Drain），实现硬件与（Hardware AND）。 |
| `input-enable` | `boolean` | 启用引脚输入，例如启用输入缓冲器（Input Buffer）；不影响输出。 |

## NXP串口引脚组原例

```dts
group0 {
    pinmux = <&main__iomuxc_pio3_30_hsp_lpuart0_txd>,
        <&main__iomuxc_pio3_31_hsp_lpuart0_rxd>;
    drive-strength = "50-ohm";
    slew-rate = "fast";
};
```

## IOMUXC属性与字段原始对照

```text
drive-open-drain: ODENA=1 (PIO0..PIO4 only; PIO5/6/7 have no ODENA)
input-enable:     IBENA=1 (input buffer / receiver enable)
bias-pull-down:   PULLENA=0b01
bias-pull-up:     PULLENA=0b10
bias-disable:     PULLENA=0b00
slew-rate:        SLEWRATE=<enum index>
drive-strength:   DRIVE=<enum index>
```

译注：原例为PIO3配置 `drive-strength`，而属性说明指出只有PIO5/6/7有DRIVE字段，并提到针对PIO0～4的构建期检查；这里保留原例与限制，实际配置须核对适用焊盘。

## 14.3\_寄存器块命名原例

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

[上一章](P013_nxp_mcux-rt11xx-pinctrl.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P015_nxp_mcxe31x-siul2-pinctrl.md)
