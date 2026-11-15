---
id: learning.zephyr-docs.hardware.dacrest-8
title: Infineon斜坡发生器数模转换器绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/dac/infineon,hppass-csg-dac.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第779章\_Infineon斜坡发生器数模转换器绑定

<a id="dtbinding-infineon-hppass-csg-dac"></a>

原文：[infineon,hppass-csg-dac](https://docs.zephyrproject.org/latest/build/dts/api/bindings/dac/infineon,hppass-csg-dac.html)。读取日期：2026-10-13，`latest`。

`infineon,hppass-csg-dac` 是设备树绑定（Devicetree Binding），描述Infineon高性能可编程模拟子系统（High Performance Programmable Analog Sub-System，HPPASS）比较器斜坡发生器（Comparator Slope Generator，CSG）的数模转换器（Digital-to-Analog Converter，DAC）配置。

驱动为 [`drivers/dac/dac_infineon_hppass_csg.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dac/dac_infineon_hppass_csg.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,hppass-csg-dac)。

## 779.1\_配对关系与驱动范围

此节点表示单个切片（Slice）内的10位、30百万次采样每秒（Million Samples per Second，Msps）DAC，必须是[CSG多功能设备（Multi-Function Device，MFD）](P726_Infineon斜坡发生器绑定.md)的子节点，父节点兼容字符串为 `infineon,hppass-csg`。

DAC没有外部输出引脚，输出在内部接到配对比较器（Comparator）的负输入，也可通过 `CSG_CTRL.VDAC_OUT_SEL` 选择路由到逐次逼近寄存器型模数转换器（Successive Approximation Register Analog-to-Digital Converter，SAR ADC）进行观测。**它不能独立使用，必须同时配置并启用相同切片索引的[比较器子节点](P736_Infineon斜坡发生器比较器绑定.md)。**

分辨率固定为10位；标准Zephyr DAC应用程序接口（Application Programming Interface，API）仅支持直接写入模式（Direct-Write Mode），尚不支持缓冲（Buffered）、斜坡（Slope）、查找表（Look-Up Table，LUT）等高级模式。

## 779.2\_控制器节点专用属性

本节属性作用于控制器节点。`int` 为整数，`array` 为数值数组，`string` 为字符串，`boolean` 为布尔属性，`phandle` 为节点引用（Phandle），`phandles` 为引用列表，`phandle-array` 为引用与说明单元数组，`string-array` 为字符串数组。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `deglitch` | `int` | DAC输出去毛刺（De-Glitch）宽度，单位为HPPASS时钟周期，对应 `DAC_CFG.DAC_DEGLITCH`（0至7）；模拟输出送到配对比较器负输入前，滤除持续时间小于该宽度的毛刺；默认值：`0`；范围：`0 to 7` |
| `initial-value` | `int` | 驱动初始化时、HPPASS自主控制器（Autonomous Controller，AC）进入锁定状态前，写入 `SLICE[s].DAC_VAL` 的可选10位初始值（Initial Value），范围0至1023。省略时保持硬件复位值0，输出约0 V；适用于应用尚未来得及调用 `dac_write_value()`、配对比较器就需要稳定的电源中点（Mid-Rail）或其他参考的情况；范围：`0 to 1023` |
| `#io-channel-cells` | `int` | **必需**。输入输出通道说明符（I/O Channel Specifier）中的单元数量（Cell Count）；固定值：`1` |

## 779.3\_控制器资源

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。覆盖CSG内此切片的 `DAC_CFG`、`DAC_VAL_A`、`DAC_VAL_B` 和 `DAC_VAL` 的寄存器区域；编译时用偏移除以CSG切片步距（Slice Stride）得出切片索引 |
| `interrupts` | `array` | 此切片的DAC中断线（Interrupt Line）；仅在高级模式下产生DAC中断：硬件启动触发（Hardware Start Trigger）、SLOPE／LUT完成，或BUFFERED／HYSTERETIC缓冲区空。此处保留硬件描述，不表示当前DAC API已支持这些高级模式 |

通道说明单元名称（Specifier Cell Name）为 `output`，即输出；`io-channel` 说明符包含一个单元。

## 779.4\_通道子节点属性

这些属性用于DAC的通道子节点，其中 `reg` 是通道编号，与控制器节点的寄存器地址含义不同。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。通道标识（Channel Identifier） |
| `zephyr,resolution` | `int` | 此通道使用的DAC分辨率（Resolution） |
| `zephyr,buffered` | `boolean` | 为此通道启用输出缓冲器（Output Buffer） |
| `zephyr,internal` | `boolean` | 为此通道启用内部输出路径（Internal Output Path） |
| `zephyr,vref-mv` | `int` | 指定此通道所选参考源的电压，单位为毫伏（Millivolt，mV），使应用在需要计算时能够获取该值 |

没有已弃用的控制器专用属性。以下为控制器继承的基础属性，不保证全部适用于本绑定；必需性以本页标记为准。

## 779.5\_状态、兼容字符串与寄存器

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

## 779.6\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 779.7\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者信息，通常应遵守下述 dt-schema 时钟绑定约定 |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 779.8\_DMA、输入输出与邮箱通道

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

## 779.9\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 779.10\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：Infineon自主模拟连续时间数模转换器绑定](P778_Infineon自主模拟连续时间数模转换器绑定.md) · [下一章：AD5529R数模转换器绑定](P780_AD5529R数模转换器绑定.md) · [返回大纲](大纲.md)
