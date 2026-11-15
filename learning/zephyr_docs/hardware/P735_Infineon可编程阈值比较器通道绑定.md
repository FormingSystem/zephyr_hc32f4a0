---
id: learning.zephyr-docs.hardware.compifx-0
title: Infineon可编程阈值比较器通道绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/comparator/infineon,autanalog-ptcomp-comp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第735章\_Infineon可编程阈值比较器通道绑定

<a id="dtbinding-infineon-autanalog-ptcomp-comp"></a>

原文：[infineon,autanalog-ptcomp-comp](https://docs.zephyrproject.org/latest/build/dts/api/bindings/comparator/infineon,autanalog-ptcomp-comp.html)。读取日期：2026-10-13，`latest`。

`infineon,autanalog-ptcomp-comp` 是Infineon Technologies的设备树绑定（Devicetree Binding），描述自主模拟（Autonomous Analog，AutAnalog）可编程阈值比较器（Programmable Threshold Comparator，PTComp／PTCOMP）通道。每个节点表示PTComp块内的Comp0、Comp1两个比较器之一，将同相（Non-Inverting）输入电压与反相（Inverting）输入电压比较，产生数字输出。通过 `positive-mux`、`negative-mux` 配置输入路由，数值对应 `cy_en_autanalog_ptcomp_comp_mux_t` 枚举。父节点必须具有兼容字符串 `infineon,autanalog-ptcomp`，参见[PTCOMP父设备](P723_Infineon可编程阈值比较器绑定.md)。

驱动为 [`drivers/comparator/comparator_infineon_autanalog_ptcomp.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/comparator_infineon_autanalog_ptcomp.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,autanalog-ptcomp-comp)。

## 735.1\_输入路由与原始示例

CTB指连续时间模块（Continuous Time Block），OA指运算放大器（Operational Amplifier）；DAC指数模转换器（Digital-to-Analog Converter），PRB指可编程参考模块（Programmable Reference Block），VREF指参考电压（Voltage Reference）。SAR指逐次逼近寄存器（Successive Approximation Register），PTC沿用原文对阈值比较相关引脚的标识；GPIO为通用输入输出（General-Purpose Input/Output）。

| 选择值 | 输入来源 |
| --- | --- |
| 0 | CTB0引脚1 |
| 1 | CTB0引脚4 |
| 2 | CTB0引脚6 |
| 3 | CTB0引脚7 |
| 4 | CTB1引脚1 |
| 5 | CTB1引脚4 |
| 6 | CTB1引脚6 |
| 7 | CTB1引脚7 |
| 8 | CTB0的OA0输出 |
| 9 | CTB0的OA1输出 |
| 10 | CTB1的OA0输出 |
| 11 | CTB1的OA1输出 |
| 12 | DAC0（VREF0） |
| 13 | DAC1（VREF1） |
| 14 | PRB OUT0（VREF2） |
| 15 | PRB OUT1（VREF3） |
| 16至23 | SAR/PTC GPIO引脚0至7，依次对应 |

以下设备树源码（Devicetree Source，DTS）使用 `dt-bindings/comparator/infineon-autanalog-ptcomp.h` 中的常量。`IFX_AUTANALOG_PTCOMP_PWR_NORMAL` 为正常功耗模式，`IFX_AUTANALOG_PTCOMP_INT_EDGE_RISING` 为上升沿中断；`IFX_AUTANALOG_PTCOMP_MUX_GPIO2`、`IFX_AUTANALOG_PTCOMP_MUX_PRB_OUT0`、`IFX_AUTANALOG_PTCOMP_MUX_DAC0` 分别选择GPIO2、PRB OUT0和DAC0。第一例为基础配置，第二例为高级模式（Advanced Mode），在Comp0下定义两个动态多路复用配置槽（Dynamic Mux Configuration Slot）。

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
};
```

```dts
/*
 * Advanced mode: 2 dynamic mux config slots on comp@0.
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
};
```

译注：原例PTCOMP父节点没有写出父绑定要求的 `reg`；这里保留原例，实际配置需结合芯片设备树补全。

## 735.2\_节点专用属性

`int` 为整数，`string` 为字符串，`boolean` 为布尔属性；本文出现的 `reg` 使用数值数组（`array`）。

本页 `IFX_AUTANALOG_PTCOMP_*` 常量均来自 `dt-bindings/comparator/infineon-autanalog-ptcomp.h`。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `power-mode` | `int` | **必需**。比较器功耗模式（Power Mode）；使用 `IFX_AUTANALOG_PTCOMP_PWR_*` 常量，完整枚举与电流／时间参数见后文；合法值：`0, 1, 2, 3` |
| `hysteresis` | `boolean` | 启用比较器30毫伏（Millivolt，mV）的输入迟滞（Input Hysteresis） |
| `interrupt-mode` | `int` | 比较器中断的边沿检测模式（Edge Detection Mode）；使用 `IFX_AUTANALOG_PTCOMP_INT_*` 常量，完整枚举见后文；默认值：`0` |
| `positive-mux` | `int` | **必需**。同相（正）输入多路复用器（Non-Inverting Input Multiplexer）选择；使用 `IFX_AUTANALOG_PTCOMP_MUX_*` 常量，顶层说明给出的范围为0至23 |
| `negative-mux` | `int` | **必需**。反相（负）输入多路复用器（Inverting Input Multiplexer）选择；使用 `IFX_AUTANALOG_PTCOMP_MUX_*` 常量，顶层说明给出的范围为0至23 |
| `pp-input-source` | `int` | 后处理（Post-Processing）输入源，使用 `IFX_AUTANALOG_PTCOMP_PP_SRC_*` 常量，映射见后文；默认值：`0`；合法值：`0, 1, 2` |
| `pp-input-type` | `int` | 后处理的边沿／电平检测类型（Edge/Level Sensing Type），使用 `IFX_AUTANALOG_PTCOMP_PP_TYPE_*` 常量，映射见后文；默认值：`0`；合法值：`0, 1, 2, 3` |
| `pp-count-mode` | `int` | 后处理计数器模式（Counter Mode），使用 `IFX_AUTANALOG_PTCOMP_PP_MODE_*` 常量，映射见后文；默认值：`0`；合法值：`0, 1, 2` |
| `pp-data-function` | `int` | 通过查找表（Look-Up Table，LUT）的布尔函数（Boolean Function）组合两个比较器输出；使用 `IFX_AUTANALOG_PTCOMP_PP_FUNC_*` 常量，范围0至13；默认值：`0` |
| `pp-window-size` | `int` | WINDOW模式的后处理窗口大小（Window Size）；使用 `IFX_AUTANALOG_PTCOMP_PP_WIN_*` 常量，映射见后文；默认值：`0`；合法值：`0, 1, 2, 3, 4, 5, 6` |
| `pp-period` | `int` | FRAME模式的后处理帧周期（Frame Period），以时钟周期数表示；默认值：`0` |
| `pp-limit-condition` | `int` | 后处理计数器的限值条件（Limit Condition）；使用 `IFX_AUTANALOG_PTCOMP_PP_COND_*` 常量，映射见后文；默认值：`0`；合法值：`0, 1, 2, 3` |
| `pp-threshold-low` | `int` | 后处理计数器范围检测的低阈值（Low Threshold）；默认值：`0` |
| `pp-threshold-high` | `int` | 后处理计数器范围检测的高阈值（High Threshold）；默认值：`0` |

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。PTComp块内的比较器索引，为0或1 |

## 735.3\_功耗、中断与后处理常量

功耗项保留原文给出的电流与时间组合；原页未进一步说明时间参数的测量条件。各常量、编码与含义如下。

| 常量 | 编码 | 含义 |
| --- | --- | --- |
| `IFX_AUTANALOG_PTCOMP_PWR_OFF` | 0 | 关闭 |
| `IFX_AUTANALOG_PTCOMP_PWR_ULP` | 1 | 超低功耗（Ultra-Low Power），小于300纳安（nA），7微秒（µs） |
| `IFX_AUTANALOG_PTCOMP_PWR_LP` | 2 | 低功耗（Low Power），小于10微安（µA），1微秒 |
| `IFX_AUTANALOG_PTCOMP_PWR_NORMAL` | 3 | 正常（Normal），小于150微安，0.1微秒 |
| `IFX_AUTANALOG_PTCOMP_INT_DISABLED` | 0 | 禁用 |
| `IFX_AUTANALOG_PTCOMP_INT_EDGE_RISING` | 1 | 上升沿（Rising Edge） |
| `IFX_AUTANALOG_PTCOMP_INT_EDGE_FALLING` | 2 | 下降沿（Falling Edge） |
| `IFX_AUTANALOG_PTCOMP_INT_EDGE_BOTH` | 3 | 双边沿（Both Edges） |
| `IFX_AUTANALOG_PTCOMP_PP_SRC_DISABLED` | 0 | 禁用 |
| `IFX_AUTANALOG_PTCOMP_PP_SRC_COMP0` | 1 | 比较器Comp0 |
| `IFX_AUTANALOG_PTCOMP_PP_SRC_COMP1` | 2 | 比较器Comp1 |
| `IFX_AUTANALOG_PTCOMP_PP_TYPE_LEVEL` | 0 | 电平检测 |
| `IFX_AUTANALOG_PTCOMP_PP_TYPE_EDGE_RISING` | 1 | 上升沿检测 |
| `IFX_AUTANALOG_PTCOMP_PP_TYPE_EDGE_FALLING` | 2 | 下降沿检测 |
| `IFX_AUTANALOG_PTCOMP_PP_TYPE_EDGE_BOTH` | 3 | 双边沿检测 |
| `IFX_AUTANALOG_PTCOMP_PP_MODE_DIRECT` | 0 | 计数事件，并在满足条件时复位 |
| `IFX_AUTANALOG_PTCOMP_PP_MODE_FRAME` | 1 | 在一个帧周期内计数事件 |
| `IFX_AUTANALOG_PTCOMP_PP_MODE_WINDOW` | 2 | 滑动窗口计数器（Sliding Window Counter） |
| `IFX_AUTANALOG_PTCOMP_PP_WIN_2` | 0 | 窗口大小2 |
| `IFX_AUTANALOG_PTCOMP_PP_WIN_4` | 1 | 窗口大小4 |
| `IFX_AUTANALOG_PTCOMP_PP_WIN_8` | 2 | 窗口大小8 |
| `IFX_AUTANALOG_PTCOMP_PP_WIN_16` | 3 | 窗口大小16 |
| `IFX_AUTANALOG_PTCOMP_PP_WIN_32` | 4 | 窗口大小32 |
| `IFX_AUTANALOG_PTCOMP_PP_WIN_64` | 5 | 窗口大小64 |
| `IFX_AUTANALOG_PTCOMP_PP_WIN_128` | 6 | 窗口大小128 |
| `IFX_AUTANALOG_PTCOMP_PP_COND_BELOW` | 0 | 低于低阈值 |
| `IFX_AUTANALOG_PTCOMP_PP_COND_INSIDE` | 1 | 位于低阈值与高阈值之间 |
| `IFX_AUTANALOG_PTCOMP_PP_COND_ABOVE` | 2 | 高于高阈值 |
| `IFX_AUTANALOG_PTCOMP_PP_COND_OUTSIDE` | 3 | 低于低阈值或高于高阈值 |

## 735.4\_动态配置子节点

以下属性应用于动态配置槽子节点。顶层的正、负输入选择均为必需；子节点中的对应属性有独立默认值0，原页没有将它们标为必需。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `positive-mux` | `int` | 同相（正）输入多路复用器（Non-Inverting Input Multiplexer）选择；使用 `IFX_AUTANALOG_PTCOMP_MUX_*` 常量；默认值：`0` |
| `negative-mux` | `int` | 反相（负）输入多路复用器（Inverting Input Multiplexer）选择；使用 `IFX_AUTANALOG_PTCOMP_MUX_*` 常量；默认值：`0` |

没有已弃用的节点专用属性。以下保留继承的基础属性，不保证全部适用于本绑定；`compatible` 为必需属性。

## 735.5\_状态、兼容字符串与寄存器

本页 `int` 为整数，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`boolean` 为布尔属性，`compound` 为复合类型。**节点引用（Phandle）**用来指向其他节点；`phandle-array` 表示节点引用及其说明单元，`phandles` 表示节点引用列表。

`status` 的类型为 `string`，描述节点所代表硬件或其他资源的运行状态。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将它视为不存在。合法值为 `okay`、`disabled`、`reserved`、`fail`、`fail-sss`。详见《设备树规范》（Devicetree Specification）v0.4 第 2.3.4 节。

`compatible` 的类型为 `string-array`，是**必需属性**。它用字符串列表定义节点代表的硬件或其他资源类型；设备驱动检查特定兼容字符串，以寻找应由自己管理的节点。推荐格式为 `vendor,device`，其中 `vendor` 是厂商简称，`device` 通常取自数据手册。多个值应按从最具体到最通用排列，使某一通用家族的具体设备能匹配当前可用的最具体驱动。详见规范 v0.4 第 2.3.1 节。


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

## 735.6\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 735.7\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者信息，通常应遵守下述 dt-schema 时钟绑定约定 |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 735.8\_DMA、输入输出与邮箱通道

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

## 735.9\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 735.10\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：STM32G4运算放大器绑定](P734_STM32G4运算放大器绑定.md) · [下一章：Infineon斜坡发生器比较器绑定](P736_Infineon斜坡发生器比较器绑定.md) · [返回大纲](大纲.md)
