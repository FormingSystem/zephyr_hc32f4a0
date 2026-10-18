---
id: learning.zephyr-docs.pinctrl-infineon-nordic-nxp-binding-reference.page-2
title: infineon_xmc4xxx-pinctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, pinctrl]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/infineon,xmc4xxx-pinctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第2章\_infineon_xmc4xxx-pinctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/infineon,xmc4xxx-pinctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="infineon-xmc4xxx-pinctrl"></a>
<a id="dtbinding-infineon-xmc4xxx-pinctrl"></a>
<a id="std-dtcompatible-infineon-xmc4xxx-pinctrl"></a>

兼容字符串（Compatible String）：`infineon,xmc4xxx-pinctrl`。厂商：[ Infineon Technologies ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-infineon)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,xmc4xxx-pinctrl)。

驱动源码（Driver Source）：[drivers/pinctrl/pinctrl_xmc4xxx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pinctrl/pinctrl_xmc4xxx.c)。

<a id="description"></a>

Infineon XMC4XXX引脚控制器（Pin Controller）。

这是将外设输出连接到指定端口／引脚（即复用功能，Alternate Function）并配置引脚属性的单例节点。设备树外设节点引用Pinctrl设置；下方UART原例通过USIC1通道1的 `pinctrl-0` 引用 `uart_tx_p0_1_u1c1` 与 `uart_rx_p0_0_u1c1`，并以 `input-src = "DX0D"` 指定输入源。

`pinctrl-0` 的节点引用（Phandle）保存两针配置。预定义节点的命名包含外设类型、引脚方向、端口／引脚编号及USIC，帮助选择正确配置。预定义节点只设置输出引脚的复用功能；驱动强度等配置应在开发板设置中补充。允许的配置见下方属性表及从 `pincfg-node.yaml` 继承的属性允许列表（Property Allowlist）。

可向 `&pinctrl` 添加节点创建新配置。原例包含 `zephyr/dt-bindings/pinctrl/xmc4xxx-pinctrl.h`，用 `XMC4XXX_PINMUX_SET(0, 1, 2)` 设置复用并启用推挽。辅助宏 `XMC4XXX_PINMUX_SET(PORT, PIN, ALTERNATE_FUNCTION)` 为指定端口／引脚设置复用功能；最后一个参数为0表示不选择复用功能。

Pinctrl驱动仅设置输出引脚复用；输入多路复用（Input Mux）由外设驱动处理，例如USIC节点的 `input-src`。输入复用没有预定义节点，用户必须正确设置，参阅外设YAML（例如 `infineon,xmc4xxx-uart.yaml`）和XMC4XXX文档。原始代码保留在下方。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 2.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

## 2.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `#address-cells` | `int` | **必需**。子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`1` |
| `#size-cells` | `int` | **必需**。子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`1` |
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
| `pinmux` | `int` | **必需**。编码端口／引脚与复用功能，原文指向辅助宏 `XMC4XX_PINMUX_SET()`。仅为输出引脚设置复用，选择GPIO单元的ALT1～ALT4输出线；输入复用由外设单独处理，外设负责选择输入引脚，例如 `infineon,xmc4xxx-uart.yaml` 的 `input-src`。 |
| `drive-strength` | `string` | **必需**。输出引脚驱动强度（Drive Strength），选项与 `XMC_GPIO_OUTPUT_STRENGTH` 一致，见 `xmc4_gpio.h`。仅在引脚采用 `drive-push-pull` 模式时有效。；合法值：`strong-sharp-edge, strong-medium-edge, strong-soft-edge, strong-slow-edge, medium, medium-unknown1-edge, medium-unknown2-edge, weak` |
| `invert-input` | `boolean` | 反转输入（Invert Input）。 |
| `hwctrl` | `string` | **必需**。预先把引脚的硬件控制权（Hardware Control）分配给指定外设。；合法值：`disabled, periph1, periph2` |
| `bias-pull-up` | `boolean` | 启用上拉电阻（Pull-Up Resistor）。 |
| `bias-pull-down` | `boolean` | 启用下拉电阻（Pull-Down Resistor）。 |
| `drive-push-pull` | `boolean` | 主动驱动高、低电平（Push-Pull）。 |
| `drive-open-drain` | `boolean` | 开漏驱动（Open Drain），实现硬件与（Hardware AND）。 |
| `output-low` | `boolean` | 将引脚设置为低电平输出模式（Output Low）。 |
| `output-high` | `boolean` | 将引脚设置为高电平输出模式（Output High）。 |

## XMC4XXX输出复用与外设输入选择原例

```dts
&usic1ch1 {
    compatible = "infineon,xmc4xxx-uart";
    pinctrl-0 = <&uart_tx_p0_1_u1c1 &uart_rx_p0_0_u1c1>;
    pinctrl-names = "default";
    input-src = "DX0D";
    ...
};
```

```dts
#include <zephyr/dt-bindings/pinctrl/xmc4xxx-pinctrl.h>
&pinctrl {
    my_node_config: my_node_config {
    pinmux = <XMC4XXX_PINMUX_SET(0, 1, 2)>;
    drive-push-pull;
      ... other supported pin configurations ..
};
```

译注：原文属性说明使用 `XMC4XX_PINMUX_SET()`，概述和原例使用 `XMC4XXX_PINMUX_SET()`；原例新配置片段还缺少完整的大括号闭合。此处保留原始内容。

## 2.3\_寄存器块命名原例

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

[上一章](P001_infineon_pinctrl.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_ite_it8xxx2-pinctrl-func.md)
