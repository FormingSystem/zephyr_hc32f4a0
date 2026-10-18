---
id: learning.zephyr-docs.hardware.compifx-1
title: Infineon斜坡发生器比较器绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/comparator/infineon,hppass-csg-comp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第736章\_Infineon斜坡发生器比较器绑定

<a id="dtbinding-infineon-hppass-csg-comp"></a>

原文：[infineon,hppass-csg-comp](https://docs.zephyrproject.org/latest/build/dts/api/bindings/comparator/infineon,hppass-csg-comp.html)。读取日期：2026-10-13，`latest`。

`infineon,hppass-csg-comp` 是Infineon Technologies的设备树绑定（Devicetree Binding），描述高性能可编程模拟子系统（High Performance Programmable Analog Sub-System，HPPASS）内的比较器斜坡发生器（Comparator Slope Generator，CSG）比较器。一个实例代表一个CSG切片（Slice）内的比较器，必须是兼容字符串为 `infineon,hppass-csg` 的多功能设备（Multi-Function Device，MFD）的子节点，参见[CSG父设备](P726_Infineon斜坡发生器绑定.md)。负输入可选择同一切片中配对的数模转换器（Digital-to-Analog Converter，DAC）输出，或两个外部模拟输入AIN_NA／AIN_NB。`negative-input = "dac"` 时，配对DAC也必须配置并启用；选择 `ain-na` 或 `ain-nb` 时，比较器以独立纯模拟比较器运行，不使用配对DAC。CSG父MFD管理合并的比较器中断（Combined Comparator Interrupt）并分发回调（Callback）。

驱动为 [`drivers/comparator/comparator_infineon_hppass_csg.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/comparator_infineon_hppass_csg.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,hppass-csg-comp)。

## 736.1\_节点专用属性

`int` 为整数，`string` 为字符串，`boolean` 为布尔属性；本文出现的 `reg` 使用数值数组（`array`）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `positive-input` | `string` | **必需**。比较器正输入源，对应 `CMP_CFG.CMP_POS_SEL`：`ain-pa` 为外部模拟输入AIN_PA；`ain-pb` 为外部模拟输入AIN_PB；合法值：`ain-pa, ain-pb` |
| `negative-input` | `string` | **必需**。比较器负输入源，对应 `CMP_CFG.CMP_NEG_SEL`：`dac` 为同切片配对DAC输出，原文称其为默认工作模式；`ain-na`／`ain-nb` 分别为外部模拟输入AIN_NA／AIN_NB，用于独立比较器。此属性仍为必需，原页未声明可省略时的绑定默认值；合法值：`dac, ain-na, ain-nb` |
| `invert-output` | `boolean` | 在边沿检测（Edge Detection）、消隐（Blanking）和状态可见性处理之前，将比较器数字输出反相，对应 `CMP_CFG.CMP_POLARITY` |
| `blank-mode` | `string` | 比较器输出消隐模式，对应 `CMP_CFG.CMP_BLANK_MODE`。选定外部触发有效时，消隐将输出门控为无效，防止瞬态条件引起误触发。`disabled` 不消隐；`gate-on-one` 在选定触发为高电平时强制输出无效；`gate-on-zero` 在触发为低电平时强制输出无效；默认值：`disabled`；合法值：`disabled, gate-on-one, gate-on-zero` |
| `blank-trigger-sel` | `string` | 启用 `blank-mode` 时，选择门控比较器输出的HPPASS触发输入，对应 `CMP_CFG.CMP_BLANK_TR_SEL`。`tr0` 至 `tr7` 对应父 `infineon,hppass-analog` 节点配置的8个触发输入；默认值：`disabled`；合法值：`disabled, tr0, tr1, tr2, tr3, tr4, tr5, tr6, tr7` |

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。CSG块内、本切片CMP_CFG对应的寄存器区域；切片索引在编译期通过“偏移量除以CSG切片步长（Slice Stride）”得到 |

触发输入的父设备配置见[HPPASS模拟子系统绑定](P724_Infineon高性能可编程模拟子系统绑定.md)。

没有已弃用的节点专用属性。以下保留继承的基础属性，不保证全部适用于本绑定；`compatible` 为必需属性。

## 736.2\_状态、兼容字符串与寄存器

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

## 736.3\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 736.4\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者信息，通常应遵守下述 dt-schema 时钟绑定约定 |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 736.5\_DMA、输入输出与邮箱通道

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

## 736.6\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 736.7\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：Infineon可编程阈值比较器通道绑定](P735_Infineon可编程阈值比较器通道绑定.md) · [下一章：Infineon低功耗比较器绑定](P737_Infineon低功耗比较器绑定.md) · [返回大纲](大纲.md)
