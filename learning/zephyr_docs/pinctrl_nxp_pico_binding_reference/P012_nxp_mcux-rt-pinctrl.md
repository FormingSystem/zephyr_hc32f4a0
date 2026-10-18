---
id: learning.zephyr-docs.pinctrl-nxp-pico-binding-reference.page-12
title: nxp_mcux-rt-pinctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, pinctrl]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/nxp,mcux-rt-pinctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第12章\_nxp_mcux-rt-pinctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/nxp,mcux-rt-pinctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-mcux-rt-pinctrl"></a>
<a id="dtbinding-nxp-mcux-rt-pinctrl"></a>
<a id="std-dtcompatible-nxp-mcux-rt-pinctrl"></a>

兼容字符串（Compatible String）：`nxp,mcux-rt-pinctrl`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,mcux-rt-pinctrl)。

<a id="description"></a>

MCUX RT SoC设备树中，此节点使用 `pinctrl` 标签。可结合MCUXpresso配置工具与NXP硬件抽象层（HAL）中的 `rt_dts_gen.py` 自动生成节点。组内mux、mode、input、daisy、cfg字段选择待配置引脚，其余设备树属性设置配置值。

下方配置原例说明LPUART1：GPIO_AD_B0_12为TX，GPIO_AD_B0_13为RX，两针均配置为弱锁存（Weak Latch）、`r0-6` 驱动强度、慢压摆率和100MHz速度。

可查看SoC级IOMUXC DTS文件查找可用引脚复用选项。属性对IOMUXC SW_PAD_CTL寄存器的影响如下：`input-schmitt-enable` 设置HYS=1；`drive-open-drain` 设置ODE=1；`input-enable` 设置SW_MUX_CTL_PAD中的SION=1；`bias-pull-down` 设置PUE=1、PUS取下拉值；`bias-pull-up` 设置PUE=1、PUS取上拉值；`bias-disable` 设置PKE=0；`slew-rate`、`drive-strength`、`nxp,speed` 分别以枚举索引设置SRE、DSE、SPEED。仅提供必需属性时，HYS=0、ODE=0、SION=0、PUE=0、PUS=0、PKE=1，而SRE、DSE、SPEED分别取上述属性值。原始配置与字段对照均保留在下方。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 12.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

## 12.2\_基础属性

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
| `drive-strength` | `string` | **必需**。引脚输出驱动强度（Drive Strength），设置IOMUXC的DSE字段。以给定电压下的输出阻抗表达；可结合具体负载阻抗计算最大电流。编码000禁用输出驱动；001 R0_1在3.3V／1.8V下为157Ω／260Ω；010 R0_2为78Ω／130Ω；011 R0_3为53Ω／88Ω；100 R0_4为39Ω／65Ω；101 R0_5为32Ω／52Ω；110 R0_6为32Ω／43Ω；111 R0_7为26Ω／37Ω。原始对照保留在下方。；合法值：`disabled, r0, r0-2, r0-3, r0-4, r0-5, r0-6, r0-7` |
| `bias-pull-up-value` | `string` | 选择此引脚的上拉电阻，设置IOMUXC的PUS字段。默认47kΩ，因为这是多数SoC引脚的默认上拉值。00未使用、不修改引脚；01为47kΩ；10为100kΩ；11为22kΩ，原文名称为 `PUS_2_22K_Ohm_Pull_Up`。；默认值：`47k`；合法值：`unused, 47k, 100k, 22k` |
| `bias-pull-down-value` | `string` | 原文首句称选择上拉电阻，随后说明此项对应IOMUXC的PUS字段且当前只支持100kΩ下拉：00 `PUS_0_100K_Ohm_Pull_Down` 为100kΩ下拉。；默认值：`100k`；合法值：`100k` |
| `slew-rate` | `string` | **必需**。选择引脚压摆率（Slew Rate），对应IOMUXC的SRE字段：0 `SRE_0_Slow_Slew_Rate` 为慢，1 `SRE_1_Fast_Slew_Rate` 为快。；合法值：`slow, fast` |
| `nxp,speed` | `string` | 设置引脚速度（Pin Speed），对应IOMUXC的SPEED字段：00为低速50MHz，01为中速100MHz，10为中速150MHz，11为最高200MHz。；合法值：`50-mhz, 100-mhz, 150-mhz, 200-mhz` |
| `bias-disable` | `boolean` | 禁用引脚的所有偏置（Bias）。 |
| `bias-pull-up` | `boolean` | 启用上拉电阻（Pull-Up Resistor）。 |
| `bias-pull-down` | `boolean` | 启用下拉电阻（Pull-Down Resistor）。 |
| `drive-open-drain` | `boolean` | 开漏驱动（Open Drain），实现硬件与（Hardware AND）。 |
| `input-enable` | `boolean` | 启用引脚输入，例如启用输入缓冲器（Input Buffer）；不影响输出。 |
| `input-schmitt-enable` | `boolean` | 启用施密特触发模式（Schmitt-Trigger Mode）。 |

## NXP串口引脚组原例

```dts
group0 {
  pinmux = <&iomuxc_gpio_ad_b0_12_lpuart1_tx,
    &iomuxc_gpio_ad_b0_13_lpuart1_rx>;
  drive-strength = "r0-6";
  slew-rate = "slow";
  nxp,speed = "100-mhz";
};
```

## IOMUXC属性与字段原始对照

```text
input-schmitt-enable: HYS=1
drive-open-drain: ODE=1
input-enable: SION=1 (in SW_MUX_CTL_PAD register)
bias-pull-down: PUE=1, PUS=<bias-pull-down-value>
bias-pull-up: PUE=1, PUS=<bias-pull-up-value>
bias-disable: PKE=0
slew-rate: SRE=<enum_idx>
drive-strength: DSE=<enum_idx>
nxp,speed: SPEED=<enum_idx>
```

## 仅必需属性时的寄存器原始配置

```text
HYS=0,
ODE=0,
SION=0,
PUE=0,
PUS=0,
PKE=1,
SRE=<slew-rate>,
DSE=<drive-strength>,
SPEED=<nxp,speed>
```

## 驱动阻抗原始编码表

```text
000 DSE_0_output_driver_disabled_ — output driver disabled
001 DSE_1_R0_1 — 157 Ohm impedance @3.3V, 260 Ohm impedance @1.8V
010 DSE_2_R0_2 — 78 Ohm @3.3V, 130 Ohm @1.8V
011 DSE_3_R0_3 — 53 Ohm @3.3V, 88 Ohm @1.8V
100 DSE_4_R0_4 — 39 Ohm @3.3V, 65 Ohm @1.8V
101 DSE_5_R0_5 — 32 Ohm @3.3V, 52 Ohm @1.8V
110 DSE_6_R0_6 — 32 Ohm @3.3V, 43 Ohm @1.8V
111 DSE_7_R0_7 — 26 Ohm @3.3V, 37 Ohm @1.8V
```

## 12.3\_寄存器块命名原例

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

[上一章](P011_nxp_mci-io-mux.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P013_nxp_mcux-rt11xx-pinctrl.md)
