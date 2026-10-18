---
id: learning.zephyr-docs.hardware.mfdifx-0
title: Infineon自主模拟子系统绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/mfd/infineon,autanalog.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第720章\_Infineon自主模拟子系统绑定

<a id="dtbinding-infineon-autanalog"></a>

原文：[infineon,autanalog](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mfd/infineon,autanalog.html)。读取日期：2026-10-13，`latest`。

`infineon,autanalog` 是Infineon Technologies的设备树绑定（Devicetree Binding），属于多功能设备（Multi-Function Device，MFD）目录，描述自主模拟（Autonomous Analog，AutAnalog）共享模拟外设子系统，包含SAR ADC、DAC、可编程稳压器、CTB运算放大器和PTCOMP，均由自主控制器（Autonomous Controller，AC）协调。MFD设备管理AC状态机（State Machine）、共享中断分发（Shared Interrupt Dispatch）和子系统初始化；ADC、DAC、比较器等各外设作为子节点。

本页SAR ADC指逐次逼近寄存器型模数转换器（Successive Approximation Register Analog-to-Digital Converter），DAC指数模转换器（Digital-to-Analog Converter），CTB指连续时间模块（Continuous Time Block），PTCOMP指可编程阈值比较器（Programmable Threshold Comparator），PRB指可编程参考模块（Programmable Reference Block）。通用输入输出（General-Purpose Input/Output，GPIO）与运算放大器（Operational Amplifier，Opamp）相关字段保留原属性名。

驱动为 [`drivers/mfd/mfd_infineon_autanalog.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/mfd_infineon_autanalog.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,autanalog)。

## 720.1\_基本模式与高级模式

基本模式（Basic Mode）省略 `ac-states`。驱动自动生成3状态SAR单次转换（Single-Shot）AC序列；SAR ADC子节点启用时，在编译期填入SAR字段，用户无需配置AC。

高级模式（Advanced Mode）提供 `ac-states`，用有序节点引用列表配置STT。各节点的兼容字符串必须为 `infineon,autanalog-ac-state`，每节点定义一个状态，并完整控制SAR、CTB、PTCOMP和DAC的子外设字段。参见[AC状态条目](P721_Infineon自主模拟控制器状态绑定.md)。

## 720.2\_原始设备树示例

以下完整保留官方设备树源码（Devicetree Source，DTS）示例。

译注：下列配置宏的作用与[官方配置头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/mfd/infineon-autanalog.h)对照说明。STOP表示停止动作，SAR_EOS表示SAR扫描结束；原例混用 `IFX_*` 宏和 `CY_*` 枚举标识，代码保持原样。

| 配置标识 | 含义 |
| --- | --- |
| `IFX_AUTANALOG_AC_COND_BLOCK_READY` | 子系统初始化并就绪条件（Block Ready） |
| `IFX_AUTANALOG_AC_COND_FALSE` | 恒假条件（False） |
| `CY_AUTANALOG_STT_AC_CONDITION_TRUE` | 原例使用的恒真条件（True）标识 |
| `CY_AUTANALOG_STT_AC_CONDITION_SAR_EOS` | 原例使用的SAR扫描结束条件标识 |
| `IFX_AUTANALOG_AC_ACTION_WAIT_FOR` | 等待条件为真（Wait For） |
| `IFX_AUTANALOG_AC_ACTION_STOP` | 停止AC（Stop） |
| `IFX_AUTANALOG_AC_ACTION_BRANCH_IF_TRUE` | 条件为真时分支（Branch If True） |

示例使用 `dt-bindings/mfd/infineon-autanalog.h` 常量，演示4状态序列：状态0等待模块就绪（BLOCK_READY）、使能SAR并转入状态1；状态1停止并等待重新配置请求；状态2等待SAR扫描结束（End of Scan，EOS）、触发SAR并转入状态3；状态3返回状态1。

```dts
/* Example of custom 4-state sequence using SAR.
 * Use constants from <dt-bindings/mfd/infineon-autanalog.h>.
 */

/ {
    /*
    * AC State Transition Table:
    * State 0: Wait for BLOCK_READY, enable SAR, branch to 1
    * State 1: STOP and wait for any reconfiguration request
    * State 2: Wait for SAR_EOS, trigger SAR, branch to 3
    * State 3: Loop back to state 1
    */
    ac_state0: ac-state-0 {
        compatible = "infineon,autanalog-ac-state";
        ac-unlock = <1>;
        ac-condition = <IFX_AUTANALOG_AC_COND_BLOCK_READY>;
        ac-action = <IFX_AUTANALOG_AC_ACTION_WAIT_FOR>;
        branch-state = <1>;
        sar-unlock = <1>;
        sar-enable = <1>;
    };

    ac_state1: ac-state-1 {
        compatible = "infineon,autanalog-ac-state";
        ac-condition = <IFX_AUTANALOG_AC_COND_FALSE>;
        ac-action = <IFX_AUTANALOG_AC_ACTION_STOP>;
        sar-unlock = <1>;
        sar-enable = <1>;
    };

    ac_state2: ac-state-2 {
        compatible = "infineon,autanalog-ac-state";
        ac-condition = <CY_AUTANALOG_STT_AC_CONDITION_SAR_EOS>;
        ac-action = <IFX_AUTANALOG_AC_ACTION_WAIT_FOR>;
        branch-state = <3>;
        sar-unlock = <1>;
        sar-enable = <1>;
        sar-trigger = <1>;
    };

    ac_state3: ac-state-3 {
        compatible = "infineon,autanalog-ac-state";
        ac-condition = <CY_AUTANALOG_STT_AC_CONDITION_TRUE>;
        ac-action = <IFX_AUTANALOG_AC_ACTION_BRANCH_IF_TRUE>;
        branch-state = <1>;   /* loop back to stop state */
        sar-unlock = <1>;
        sar-enable = <1>;
    };
};

&autanalog {
    ac-states = <&ac_state0 &ac_state1 &ac_state2 &ac_state3>;
};
```

译注：`ac-states` 的文字说明建议将状态节点放在AutAnalog节点下，但原例放在根节点下，随后通过引用关联。这里保留两者，不把示例位置改写为另一种层级。

## 720.3\_节点专用属性

本页 `int` 为整数，`boolean` 为布尔属性，`array` 为数值数组，`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明单元数组。标为0或1的 `int` 属性仍应使用数值单元，不等同于无值的布尔属性。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `ac-states` | `phandles` | 高级模式的有序AC状态节点引用列表，驱动据此构建完整STT；各被引用节点必须具有兼容字符串 `infineon,autanalog-ac-state`。这些状态节点应定义为AutAnalog节点的子节点，与所配置外设放在一起。省略时使用内建3状态SAR单次转换序列，并按SAR ADC子节点状态自动填入SAR字段 |

## 720.4\_专用寄存器与中断资源

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `interrupts` | `array` | **必需**。AutAnalog主子系统中断（SAR、DAC、CTB、PTCOMP、AC）始终必需。`autanalog_fifo` 中断只在使用SAR ADC的先进先出缓冲区（First-In, First-Out，FIFO）时需要；SAR ADC没有配置FIFO子节点时可以省略该中断 |

没有已弃用的节点专用属性。以下完整保留继承的基础属性，不保证全部适用于本绑定；`compatible` 为必需属性。

## 720.5\_状态、兼容字符串与寄存器

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

## 720.6\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | **必需**。设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 720.7\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者信息，通常应遵守下述 dt-schema 时钟绑定约定 |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 固定值：`1`。子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 固定值：`1`。子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 720.8\_DMA、输入输出与邮箱通道

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

## 720.9\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 720.10\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：MAXQ10xx多功能设备绑定](P719_MAXQ10xx多功能设备绑定.md) · [下一章：Infineon自主模拟控制器状态绑定](P721_Infineon自主模拟控制器状态绑定.md) · [返回大纲](大纲.md)
