---
id: learning.zephyr-docs.hardware.regprbparent-0
title: Infineon可编程参考模块绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/mfd/infineon,autanalog-prb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第659章\_Infineon可编程参考模块绑定

<a id="dtbinding-infineon-autanalog-prb"></a>

原文：[infineon,autanalog-prb](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mfd/infineon,autanalog-prb.html)。读取日期：2026-10-13，`latest`。

`infineon,autanalog-prb` 是Infineon Technologies的设备树绑定（Devicetree Binding），描述AutAnalog可编程参考模块（Programmable Reference Block，PRB）多功能设备（Multi-Function Device，MFD）。

PRB通过16位置电阻抽头分压器（Resistive Tap Divider），从VBGR（0.9 V）或VDDA（最高1.8 V）生成两个可编程参考电压 `Vref0`、`Vref1`。每路参考输出都表示为兼容字符串为 `infineon,autanalog-prb-vref` 的稳压器子节点；详见[参考电压子节点绑定](P650_Infineon自主模拟参考电压绑定.md)。VBGR和VDDA为原文的源电压标识。

PRB位于AutAnalog子系统内，由自主控制器（Autonomous Controller，AC）的状态转换表（State Transition Table，STT）协调。MFD驱动将两个Vref子节点合并到一个外设驱动库（Peripheral Driver Library，PDL）配置结构 `cy_stc_autanalog_prb_t` 中，并管理STT内共享的PRB解锁操作。

驱动为 [`drivers/mfd/mfd_infineon_autanalog_prb.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/mfd_infineon_autanalog_prb.c)。使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,autanalog-prb)。

## 659.1\_原始设备树示例

以下示例使用[设备树配置头文件](../power/P115_Infineon可编程参考设备树头文件.md)中的宏常量。`IFX_AUTANALOG_PRB_SRC_VDDA` 选择VDDA源电压；`IFX_AUTANALOG_PRB_TAP_7`、`IFX_AUTANALOG_PRB_TAP_6` 分别选择抽头7和抽头6。

```dts
/*
 * Use constants from <dt-bindings/regulator/infineon-autanalog-prb.h>.
 */
prb0: prb@0 {
    compatible = "infineon,autanalog-prb";
    status = "okay";

    vref0: vref@0 {
        compatible = "infineon,autanalog-prb-vref";
        reg = <0>;
        source = <IFX_AUTANALOG_PRB_SRC_VDDA>;
        tap = <IFX_AUTANALOG_PRB_TAP_7>;
    };

    vref1: vref@1 {
        compatible = "infineon,autanalog-prb-vref";
        reg = <1>;
        source = <IFX_AUTANALOG_PRB_SRC_VDDA>;
        tap = <IFX_AUTANALOG_PRB_TAP_6>;
    };
};
```

## 659.2\_低功耗请求

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `lp-mode` | `boolean` | 为AutAnalog子系统请求低功耗（Low Power，LP）运行；原页未标为必需 |

`boolean` 表示布尔属性。设置 `lp-mode` 后，父AutAnalog MFD在基本模式（Basic Mode）下的STT会使AC各状态进入LP运行。如果其他任一AutAnalog子外设设置了 `lp-mode`，也会启用LP模式；这些外设包括逐次逼近型模数转换器（Successive Approximation Register Analog-to-Digital Converter，SAR ADC）、数模转换器（Digital-to-Analog Converter，DAC）、连续时间模块（Continuous Time Block，CTB）和可编程阈值比较器（Programmable Threshold Comparator，PTCOMP）。

在高级模式（Advanced Mode，即 `ac-states`）下，应改用各状态独立的 `ac-lp-mode` 属性。

译注：CTB与PTCOMP的名称分别对应官方[CTB绑定](P722_Infineon连续时间模块绑定.md)和[PTCOMP绑定](P723_Infineon可编程阈值比较器绑定.md)；PDL名称见厂商[外设驱动库参考](https://infineon.github.io/mtb-pdl-cat1/pdl_api_reference_manual/html/modules.html)。

## 659.3\_地址与基础属性约束

`reg`（类型 `array`，数值数组）为**必需**，给出设备地址与大小；`#address-cells`（类型 `int`，整数）固定为 `1`，`#size-cells`（类型 `int`）固定为 `0`。`compatible` 也是**必需属性**。

没有已弃用的节点专用属性。以下完整保留继承的基础属性，不保证全部适用于本绑定。

## 659.4\_状态、兼容字符串与寄存器

本页 `int` 为整数，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`boolean` 为布尔属性，`compound` 为复合类型。**节点引用（Phandle）**用来指向其他节点；`phandle-array` 表示节点引用及其说明单元，`phandles` 表示节点引用列表。

`status` 的类型为 `string`，描述节点所代表硬件或其他资源的运行状态。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将它视为不存在。合法值为 `okay`、`disabled`、`reserved`、`fail`、`fail-sss`。详见《设备树规范》（Devicetree Specification）v0.4 第 2.3.4 节。

`compatible` 的类型为 `string-array`，是**必需属性**。它用字符串列表定义节点代表的硬件或其他资源类型；设备驱动检查特定兼容字符串，以寻找应由自己管理的节点。推荐格式为 `vendor,device`，其中 `vendor` 是厂商简称，`device` 通常取自数据手册。多个值应按从最具体到最通用排列，使某一通用家族的具体设备能匹配当前可用的最具体驱动。详见规范 v0.4 第 2.3.1 节。

`reg` 的类型为 `array`，给出寻址设备所需的信息，其含义取决于设备及 `compatible`。通常是一组“地址、长度”对，每对称为**寄存器块（Register Block）**，数值惯常写成十六进制。详见规范 v0.4 第 2.3.6 节。

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

## 659.5\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 659.6\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者信息，通常应遵守下述 dt-schema 时钟绑定约定 |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 659.7\_DMA、输入输出与邮箱通道

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

## 659.8\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 659.9\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：MSPM0参考电压绑定](P658_MSPM0参考电压绑定.md) · [下一章：nPM10xx稳压器绑定](P660_nPM10xx稳压器绑定.md) · [返回大纲](大纲.md)
