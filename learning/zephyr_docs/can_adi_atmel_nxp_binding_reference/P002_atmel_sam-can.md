---
id: learning.zephyr-docs.can-adi-atmel-nxp-binding-reference.page-2
title: atmel_sam-can
kind: reference
status: maintained
domains: [zephyr, devicetree, can]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/can/atmel,sam-can.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第2章\_atmel_sam-can

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/can/atmel,sam-can.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="atmel-sam-can"></a>
<a id="dtbinding-atmel-sam-can"></a>
<a id="std-dtcompatible-atmel-sam-can"></a>

兼容字符串（Compatible String）：`atmel,sam-can`。厂商：[ Atmel ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-atmel)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=atmel,sam-can)。

驱动源码（Driver Source）：[drivers/can/can_sam.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/can/can_sam.c)。

<a id="description"></a>

针对Atmel SAM适配的Bosch M_CAN灵活数据速率CAN（CAN with Flexible Data Rate，CAN FD）控制器。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 2.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `divider` | `int` | CAN内核时钟分频器，SAMx7x SoC必须提供。建议CAN时钟为20、40或80 MHz；为此PMC PCK5须选择480 MHz的UPLLCK作源时钟，分别除以24、12或6。PCK5使系统总线与处理器时钟改变时不影响通信位速率。；合法值：`6, 12, 24` |
| `bosch,mram-cfg` | `array` | **必需**。Bosch M_CAN消息RAM（Message RAM）配置，单元按顺序为`offset`、`std-filter-elements`、`ext-filter-elements`、`rx-fifo0-elements`、`rx-fifo1-elements`、`rx-buffer-elements`、`tx-event-fifo-elements`、`tx-buffer-elements`。`offset`指定后续元素在消息RAM中的起始地址偏移；非共享RAM通常设`0x0`。其余单元指定每种过滤器／FIFO／缓冲区分配的元素数量。<br>IP支持范围：11位过滤器0至128元素／0至128字；29位过滤器0至64元素／0至128字；接收FIFO0、接收FIFO1、接收缓冲区各为0至64元素／0至1152字；发送事件FIFO为0至32元素／0至64字；发送缓冲区为0至32元素／0至576字。下方保留原始排列与容量表。；长度范围：`8 to 8` |
| `bosch,timestamp-counter-prescaler` | `int` | 内部时间戳计数器（Timestamp Counter）时间单位，以CAN位时间的倍数表示，有效范围1至16。默认预分频值1，即一个CAN位时间。；默认值：`1`；范围：`1 to 16` |
| `bitrate-data` | `int` | 数据阶段（Data Phase）初始位速率，单位为bit/s；未设置时使用`CONFIG_CAN_DEFAULT_BITRATE_DATA`。 |
| `sample-point-data` | `int` | 数据阶段初始采样点，以千分比表示，例如875代表87.5%。未设置或为0时，位速率大于800 kbit/s默认75.0%，大于500 kbit/s默认80.0%，其余默认87.5%。 |
| `bitrate` | `int` | 初始位速率（Bitrate），单位为bit/s。未设置时使用`CONFIG_CAN_DEFAULT_BITRATE`。 |
| `sample-point` | `int` | 初始采样点（Sample Point），单位为千分比，例如875代表87.5%。未设置或设为0时，位速率大于800 kbit/s默认75.0%，大于500 kbit/s默认80.0%，其余默认87.5%。 |
| `phys` | `phandle` | 可主动控制的CAN收发器（Transceiver），下方保留完整设备树原例。 |
| `pinctrl-0` | `phandles` | 第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-names` | `string-array` | 所提供状态的名称，名称数量必须与状态数量一致 |

本页没有已弃用的节点专用属性。

## 2.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。需要2或3个寄存器块，按SoC选择：MCAN配置寄存器块；SAMx7x的DMA基址寄存器块；SAMA7G5的消息RAM块；SAMA7G5的MCAN SRAM选择寄存器块。 |
| `reg-names` | `string-array` | **必需**。寄存器块名称：`m_can`、`dma_base`、`message_ram`、`sram_sel`。 |
| `interrupts` | `array` | **必需**。设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | **必需**。设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `clocks` | `phandle-array` | **必需**。设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
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

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `min-bitrate` | `int` | CAN收发器支持的最低位速率，单位为bit/s。 |
| `max-bitrate` | `int` | **必需**。CAN收发器支持的最高位速率，单位为bit/s。 |

## 消息RAM数组与容量原表

数组单元顺序：

```text
<offset std-filter-elements ext-filter-elements rx-fifo0-elements rx-fifo1-elements
rx-buffer-elements tx-event-fifo-elements tx-buffer-elements>
```

容量原表；中文含义与单位见属性表：

```text
11-bit Filter    0-128 elements / 0-128 words
29-bit Filter     0-64 elements / 0-128 words
Rx FIFO 0                   0-64 elements / 0-1152 words
Rx FIFO 1                   0-64 elements / 0-1152 words
Rx Buffers          0-64 elements / 0-1152 words
Tx Event FIFO     0-32 elements / 0-64 words
Tx Buffers          0-32 elements / 0-576 words
```

## CAN收发器配置原例

```dts
  transceiver0: can-phy0 {
    compatible = "nxp,tja1040", "can-transceiver-gpio";
    standby-gpios = <gpioa 0 GPIO_ACTIVE_HIGH>;
    max-bitrate = <1000000>;
    #phy-cells = <0>;
  };

  &can0 {
    status = "okay";

    phys = <&transceiver0>;
  };
```

译注：原文 `standby-gpios` 的 `gpioa` 前未写 `&`；这里保留原例，实际配置须按设备树节点引用语法核对。

---

[上一章](P001_adi_max32-can.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_atmel_sam0-can.md)
