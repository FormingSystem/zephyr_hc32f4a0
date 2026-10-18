---
id: learning.zephyr-docs.pinctrl-nxp-pico-binding-reference.page-18
title: nxp_rt-iocon-pinctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, pinctrl]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/nxp,rt-iocon-pinctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第18章\_nxp_rt-iocon-pinctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/nxp,rt-iocon-pinctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-rt-iocon-pinctrl"></a>
<a id="dtbinding-nxp-rt-iocon-pinctrl"></a>
<a id="std-dtcompatible-nxp-rt-iocon-pinctrl"></a>

兼容字符串（Compatible String）：`nxp,rt-iocon-pinctrl`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,rt-iocon-pinctrl)。

<a id="description"></a>

RT600／RT500引脚控制器（Pin Controller）。SoC设备树中标识为 `pinctrl`，按引脚组定义配置。每个组描述某外设，每个编号子组包含该外设共享配置的引脚；`pinmux` 选择应用这些属性的引脚。下方FLEXCOMM0原例选择PIO0_1、PIO0_2对应复用功能，压摆率和驱动强度均设为 `normal`。

仅提供必需属性时，原文所称ICON_PIO寄存器配置为：IOCON_FUNC取复用选择，IOCON_PUPDENA=0，IOCON_PUPDSEL=0，IOCON_IBENA=0，IOCON_SLEWRATE取压摆率，IOCON_FULLDRIVE取驱动强度，IOCON_AMENA=0，IOCON_ODENA=0，IOCON_IIENA=0。

继承属性的影响：`drive-open-drain` 设置IOCON_ODENA=1；`bias-pull-up` 设置IOCON_PUPDENA=1、IOCON_PUPSEL=1；`bias-pull-down` 设置IOCON_PUPDENA=1、IOCON_PUPSEL=0；`input-enable` 设置IOCON_IBENA=1。原始代码与寄存器字段保留在下方。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 18.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

## 18.2\_基础属性

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
| `pinmux` | `array` | **必需**。此组的引脚复用选择。选项列表见NXP HAL中SoC级Pinctrl头文件。 |
| `slew-rate` | `string` | **必需**。引脚输出压摆率（Slew Rate），设置IOCON的SLEWRATE字段：0 SLEWRATE_0为正常模式、标准输出压摆率；1 SLEWRATE_1为慢速模式、较慢压摆率。；合法值：`normal, slow` |
| `drive-strength` | `string` | **必需**。引脚输出驱动强度（Drive Strength），设置IOCON的FULLDRIVE字段：0 FULLDRIVE_0为正常输出驱动；1 FULLDRIVE_1为全驱动，强度为正常模式的两倍。；合法值：`normal, high` |
| `nxp,drive-current` | `int` | 发送器电流驱动阻抗选择（Transmitter Drive Impedance），设置IOPCTL的ODRIVE字段（位12～13）：0为100Ω（默认），1为66Ω，2为50Ω，3为33Ω。仅部分I/O端口支持。；默认值：`0` |
| `nxp,invert` | `boolean` | 反转引脚输入逻辑电平（Invert Input Logic Level）。 |
| `nxp,analog-mode` | `boolean` | 把引脚设为模拟模式（Analog Mode），设置AMENA=1。 |
| `bias-pull-up` | `boolean` | 启用上拉电阻（Pull-Up Resistor）。 |
| `bias-pull-down` | `boolean` | 启用下拉电阻（Pull-Down Resistor）。 |
| `drive-open-drain` | `boolean` | 开漏驱动（Open Drain），实现硬件与（Hardware AND）。 |
| `input-enable` | `boolean` | 启用引脚输入，例如启用输入缓冲器（Input Buffer）；不影响输出。 |

## FLEXCOMM引脚组原例

```dts
pinmux_flexcomm0_usart: pinmux_flexcomm0_usart {
  group0 {
    pinmux = <FC0_TXD_SCL_MISO_WS_PIO0_1>,
            <FC0_RXD_SDA_MOSI_DATA_PIO0_2>;
    slew-rate = "normal";
    drive-strength = "normal";
  };
};
```

## 引脚寄存器原始字段对照

```text
IOCON_FUNC=<pin mux selection>,
IOCON_PUPDENA = 0,
IOCON_PUPDSEL = 0,
IOCON_IBENA = 0,
IOCON_SLEWRATE = <slew-rate selection>,
IOCON_FULLDRIVE = <drive-strength selection>,
IOCON_AMENA = 0,
IOCON_ODENA = 0,
IOCON_IIENA = 0,
```

```text
drive-open-drain: IOCON_ODENA=1
bias-pull-up: IOCON_PUPDENA=1, IOCON_PUPSEL=1
bias-pull-down: IOCON_PUPDENA=1, IOCON_PUPSEL=0
input-enable: IOCON_IBENA=1
```

译注：原文默认表使用IOCON_PUPDSEL，属性映射使用IOCON_PUPSEL，保持原样。

## 18.3\_寄存器块命名原例

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

[上一章](P017_nxp_port-pinmux.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P019_nxp_s32k3-siul2-pinctrl.md)
