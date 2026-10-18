---
id: learning.zephyr-docs.hardware.mfdifx-3
title: Infineon可编程阈值比较器绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/mfd/infineon,autanalog-ptcomp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第723章\_Infineon可编程阈值比较器绑定

<a id="dtbinding-infineon-autanalog-ptcomp"></a>

原文：[infineon,autanalog-ptcomp](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mfd/infineon,autanalog-ptcomp.html)。读取日期：2026-10-13，`latest`。

`infineon,autanalog-ptcomp` 是Infineon Technologies的设备树绑定（Devicetree Binding），属于多功能设备（Multi-Function Device，MFD）目录，描述AutAnalog可编程阈值比较器（Programmable Threshold Comparator，PTComp／PTCOMP）。该模块有一对比较器Comp0、Comp1，将一个输入的电压与另一输入的参考值比较；每个比较器输出均表示为兼容字符串为 `infineon,autanalog-ptcomp-comp` 的子节点。PTComp位于AutAnalog子系统内，由自主控制器（Autonomous Controller，AC）的状态转换表（State Transition Table，STT）协调。本驱动将两个比较器子节点汇总到同一个外设驱动库（Peripheral Driver Library，PDL）配置结构 `cy_stc_autanalog_ptcomp_t`，并管理STT内共享的PTComp解锁操作。

本页SAR ADC指逐次逼近寄存器型模数转换器（Successive Approximation Register Analog-to-Digital Converter），DAC指数模转换器（Digital-to-Analog Converter），CTB指连续时间模块（Continuous Time Block），PTCOMP指可编程阈值比较器（Programmable Threshold Comparator），PRB指可编程参考模块（Programmable Reference Block）。通用输入输出（General-Purpose Input/Output，GPIO）与运算放大器（Operational Amplifier，Opamp）相关字段保留原属性名。

驱动为 [`drivers/mfd/mfd_infineon_autanalog_ptcomp.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/mfd_infineon_autanalog_ptcomp.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,autanalog-ptcomp)。

## 723.1\_原始设备树示例

以下完整保留官方设备树源码（Devicetree Source，DTS）示例。

译注：示例中的配置宏按[官方PTCOMP头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/comparator/infineon-autanalog-ptcomp.h)说明如下；输入多路复用器（Input Multiplexer，MUX）用于选择输入源。

| 配置宏 | 含义 |
| --- | --- |
| `IFX_AUTANALOG_PTCOMP_PWR_NORMAL` | 正常功耗模式（Normal Power Mode） |
| `IFX_AUTANALOG_PTCOMP_INT_EDGE_RISING` | 上升沿检测（Rising Edge Detection） |
| `IFX_AUTANALOG_PTCOMP_MUX_GPIO2` | 选择GPIO2 |
| `IFX_AUTANALOG_PTCOMP_MUX_GPIO4` | 选择GPIO4 |
| `IFX_AUTANALOG_PTCOMP_MUX_PRB_OUT0` | 选择PRB输出0 |
| `IFX_AUTANALOG_PTCOMP_MUX_DAC0` | 选择DAC0输出 |

常量来自 `dt-bindings/comparator/infineon-autanalog-ptcomp.h`。第一例是基础功能配置；第二例是高级模式，每个 `dyn-cfg-*` 子节点表示一个动态配置槽（Dynamic Configuration Slot）。

```dts
/*
 * Use constants from <dt-bindings/comparator/infineon-autanalog-ptcomp.h>.
 */
ptcomp0: ptcomp@0 {
    compatible = "infineon,autanalog-ptcomp";
    status = "okay";

    comp0: comp@0 {
        compatible = "infineon,autanalog-ptcomp-comp";
        reg = <0>;
        power-mode = <IFX_AUTANALOG_PTCOMP_PWR_NORMAL>;
        interrupt-mode = <IFX_AUTANALOG_PTCOMP_INT_EDGE_RISING>;
        positive-mux = <IFX_AUTANALOG_PTCOMP_MUX_GPIO2>;
        negative-mux = <IFX_AUTANALOG_PTCOMP_MUX_PRB_OUT0>;
    };

    comp1: comp@1 {
        compatible = "infineon,autanalog-ptcomp-comp";
        reg = <1>;
        power-mode = <IFX_AUTANALOG_PTCOMP_PWR_NORMAL>;
        positive-mux = <IFX_AUTANALOG_PTCOMP_MUX_GPIO4>;
        negative-mux = <IFX_AUTANALOG_PTCOMP_MUX_PRB_OUT0>;
    };
};
```

```dts
/*
 * Advanced mode: 2 dynamic mux config slots per comparator.
 * Each child node is one slot with named properties.
 */
ptcomp0: ptcomp@0 {
    compatible = "infineon,autanalog-ptcomp";
    status = "okay";

    comp0: comp@0 {
        compatible = "infineon,autanalog-ptcomp-comp";
        reg = <0>;
        power-mode = <IFX_AUTANALOG_PTCOMP_PWR_NORMAL>;
        interrupt-mode = <IFX_AUTANALOG_PTCOMP_INT_EDGE_RISING>;
        positive-mux = <IFX_AUTANALOG_PTCOMP_MUX_GPIO2>;
        negative-mux = <IFX_AUTANALOG_PTCOMP_MUX_PRB_OUT0>;

        dyn-cfg-0 {
            positive-mux = <IFX_AUTANALOG_PTCOMP_MUX_GPIO2>;
            negative-mux = <IFX_AUTANALOG_PTCOMP_MUX_PRB_OUT0>;
        };

        dyn-cfg-1 {
            positive-mux = <IFX_AUTANALOG_PTCOMP_MUX_GPIO2>;
            negative-mux = <IFX_AUTANALOG_PTCOMP_MUX_DAC0>;
        };
    };

    comp1: comp@1 {
        compatible = "infineon,autanalog-ptcomp-comp";
        reg = <1>;
        power-mode = <IFX_AUTANALOG_PTCOMP_PWR_NORMAL>;
        positive-mux = <IFX_AUTANALOG_PTCOMP_MUX_GPIO4>;
        negative-mux = <IFX_AUTANALOG_PTCOMP_MUX_PRB_OUT0>;

        dyn-cfg-0 {
            positive-mux = <IFX_AUTANALOG_PTCOMP_MUX_GPIO4>;
            negative-mux = <IFX_AUTANALOG_PTCOMP_MUX_PRB_OUT0>;
        };

        dyn-cfg-1 {
            positive-mux = <IFX_AUTANALOG_PTCOMP_MUX_GPIO4>;
            negative-mux = <IFX_AUTANALOG_PTCOMP_MUX_DAC0>;
        };
    };
};
```

译注：原例PTCOMP父节点未给出本绑定声明为必需的 `reg` 属性；代码保持原样，实际应用需结合芯片设备树提供该属性。

## 723.2\_节点专用属性

本页 `int` 为整数，`boolean` 为布尔属性，`array` 为数值数组，`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明单元数组。标为0或1的 `int` 属性仍应使用数值单元，不等同于无值的布尔属性。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `lp-mode` | `boolean` | 为AutAnalog子系统请求低功耗（Low Power，LP）运行；设置后，父AutAnalog MFD基本模式STT中的AC状态进入低功耗运行。其他任一AutAnalog子外设（SAR ADC、DAC、CTB、PRB）设置 `lp-mode` 时也会激活低功耗模式。高级模式提供 `ac-states` 时，应改用逐状态的 `ac-lp-mode` 属性 |

没有已弃用的节点专用属性。以下完整保留继承的基础属性，不保证全部适用于本绑定；`compatible` 为必需属性。

## 723.3\_状态、兼容字符串与寄存器

本页 `int` 为整数，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`boolean` 为布尔属性，`compound` 为复合类型。**节点引用（Phandle）**用来指向其他节点；`phandle-array` 表示节点引用及其说明单元，`phandles` 表示节点引用列表。

`status` 的类型为 `string`，描述节点所代表硬件或其他资源的运行状态。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将它视为不存在。合法值为 `okay`、`disabled`、`reserved`、`fail`、`fail-sss`。详见《设备树规范》（Devicetree Specification）v0.4 第 2.3.4 节。

`compatible` 的类型为 `string-array`，是**必需属性**。它用字符串列表定义节点代表的硬件或其他资源类型；设备驱动检查特定兼容字符串，以寻找应由自己管理的节点。推荐格式为 `vendor,device`，其中 `vendor` 是厂商简称，`device` 通常取自数据手册。多个值应按从最具体到最通用排列，使某一通用家族的具体设备能匹配当前可用的最具体驱动。详见规范 v0.4 第 2.3.1 节。

`reg` 的类型为 `array`，是**必需属性**，给出寻址设备所需的信息，其含义取决于设备及 `compatible`。通常是一组“地址、长度”对，每对称为**寄存器块（Register Block）**，数值惯常写成十六进制。详见规范 v0.4 第 2.3.6 节。

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

## 723.4\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 723.5\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者信息，通常应遵守下述 dt-schema 时钟绑定约定 |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 固定值：`1`。子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 固定值：`0`。子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 723.6\_DMA、输入输出与邮箱通道

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

## 723.7\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 723.8\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：Infineon连续时间模块绑定](P722_Infineon连续时间模块绑定.md) · [下一章：Infineon高性能可编程模拟子系统绑定](P724_Infineon高性能可编程模拟子系统绑定.md) · [返回大纲](大纲.md)
