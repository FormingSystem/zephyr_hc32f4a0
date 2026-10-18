---
id: learning.zephyr-docs.hardware.comprest-2
title: Microchip模拟比较器通道绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/comparator/microchip,ac-g1-comparator.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第756章\_Microchip模拟比较器通道绑定

<a id="dtbinding-microchip-ac-g1-comparator"></a>

原文：[microchip,ac-g1-comparator](https://docs.zephyrproject.org/latest/build/dts/api/bindings/comparator/microchip,ac-g1-comparator.html)。读取日期：2026-10-13，`latest`。

`microchip,ac-g1-comparator` 是设备树绑定（Devicetree Binding），描述Microchip G1模拟比较器（Analog Comparator，AC）驱动绑定，支持AC G1外设。g1组支持名称为AC、标识U2501、版本1.0.0的模块，以及名称为AC、标识U2245、版本1.1.1的模块。

驱动为 [`drivers/comparator/comparator_mchp_ac_g1.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/comparator_mchp_ac_g1.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=microchip,ac-g1-comparator)。

## 756.1\_原始节点示例

以下设备树源码（Devicetree Source，DTS）配置比较器通道0，初始状态为禁用；`win0-1` 为原始中断名称。

```dts
ac: ac@42004c00 {
  compatible = "microchip,ac-g1-comparator";
  reg = <0x42004c00 0x24>;
  interrupts = <27 0>;
  interrupt-names = "win0-1";
  comparator-channel = <0>;
  status = "disabled";
};
```

## 756.2\_节点专用属性

`int` 为整数，`string` 为字符串，`boolean` 为布尔属性，`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明单元数组，`string-array` 为字符串数组。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `comparator-channel` | `int` | **必需**。比较器通道索引（Comparator Channel Index），为0或1；合法值：`0, 1` |
| `single-shot-mode` | `boolean` | 启用单次比较模式（Single-Shot Mode）。比较器执行一次比较后自行禁用；使用迟滞等连续模式（Continuous Mode）功能时，必须禁用本属性 |
| `positive-mux-input` | `string` | 正输入多路复用器（Positive Input Multiplexer，MUXPOS）源选择：`pin0`／`pin1`／`pin2`／`pin3` 分别为输入输出（Input/Output，I/O）引脚0／1／2／3，编码0x0／0x1／0x2／0x3；`vscale` 为模拟电源VDDANA的分压输出（Scaler），编码0x4；合法值：`pin0, pin1, pin2, pin3, vscale` |
| `negative-mux-input` | `string` | 负输入多路复用器（Negative Input Multiplexer，MUXNEG）源选择：`pin0` 至 `pin3` 为I/O引脚0至3，编码0x0至0x3；`gnd` 为地（Ground），编码0x4；`vscale` 为VDDANA分压输出，编码0x5；`bandgap` 为内部带隙电压（Internal Bandgap Voltage），编码0x6；`dac` 为数模转换器（Digital-to-Analog Converter，DAC）输出，编码0x7；合法值：`pin0, pin1, pin2, pin3, gnd, vscale, bandgap, dac` |
| `vddana-scale-value` | `int` | 分压公式为 `VSCALE = (VDDANA * (value + 1)) / 64`。仅当正输入或负输入配置为 `vscale` 时使用，有效范围0至63；VSCALE为分压输出，VDDANA为模拟电源电压；默认值：`0` |
| `output-mode` | `string` | 比较器输出路由模式（Output Routing Mode）：`off` 不将输出路由到COMPn I/O引脚，编码0x0；`async` 路由异步输出（Asynchronous Output），编码0x1；`sync` 路由经过滤波的同步输出（Synchronous Filtered Output），编码0x2；默认值：`off`；合法值：`off, async, sync` |
| `run-standby` | `boolean` | 内核睡眠时，在待机模式（Standby Mode）下保持比较器运行 |
| `hysteresis-enable` | `boolean` | 启用比较器输出迟滞（Hysteresis）；仅当单次比较模式禁用、即处于连续模式时有效 |
| `hysteresis-level` | `string` | 启用迟滞时使用的电压等级：`hyst50` 为50 mV（0x0），`hyst100` 为100 mV（0x1），`hyst150` 为150 mV（0x2）。只有启用迟滞且禁用单次比较模式时才生效；默认值：`hyst50`；合法值：`hyst50, hyst100, hyst150` |
| `filter-length` | `string` | 输出滤波／去抖（Output Filtering/Debounce）模式：`off` 不滤波（0x0）；`maj3` 为3位多数滤波（Majority Filter），3取2（0x1）；`maj5` 为5位多数滤波，5取3（0x2）；默认值：`off`；合法值：`off, maj3, maj5` |
| `swap-inputs` | `boolean` | 交换比较器输入并将输出反相。为假时MUXPOS接正端、MUXNEG接负端；为真时MUXNEG接正端、MUXPOS接负端，输出反相。可用于失调抵消（Offset Cancellation），**必须在使能比较器前配置** |
| `event-input-enable` | `boolean` | 启用比较器事件输入路径（Event Input Path） |
| `event-output-enable` | `boolean` | 启用比较器事件输出路径（Event Output Path） |
| `pinctrl-0` | `phandles` | 第一个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定 |
| `pinctrl-1` | `phandles` | 第二个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-2` | `phandles` | 第三个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-3` | `phandles` | 第四个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-4` | `phandles` | 第五个引脚控制（Pin Control）状态的配置引用；具体内容由选用的引脚控制器驱动实现决定，参见 `pinctrl-0` |
| `pinctrl-names` | `string-array` | 已提供的引脚状态名称；名称数量必须与状态数量一致 |

## 756.3\_寄存器资源

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。AC外设基址（Base Address）和大小（Size） |

没有已弃用的节点专用属性。以下保留继承的基础属性，不保证全部适用于本绑定；必需性以本页标记为准。

## 756.4\_状态、兼容字符串与寄存器

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

## 756.5\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 756.6\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者信息，通常应遵守下述 dt-schema 时钟绑定约定 |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 756.7\_DMA、输入输出与邮箱通道

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

## 756.8\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 756.9\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：ITE电压比较器绑定](P755_ITE电压比较器绑定.md) · [下一章：SiliconLabs模拟比较器绑定](P757_SiliconLabs模拟比较器绑定.md) · [返回大纲](大纲.md)
