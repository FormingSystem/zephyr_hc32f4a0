---
id: learning.zephyr-docs.intel-microchip-dma-binding-reference.page-13
title: microchip_dmac-g1-dma
kind: reference
status: maintained
domains: [zephyr, devicetree, dma]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/dma/microchip,dmac-g1-dma.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第13章\_microchip_dmac-g1-dma

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/dma/microchip,dmac-g1-dma.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="microchip-dmac-g1-dma"></a>
<a id="dtbinding-microchip-dmac-g1-dma"></a>
<a id="std-dtcompatible-microchip-dmac-g1-dma"></a>

兼容字符串（Compatible String）：`microchip,dmac-g1-dma`。厂商：[ Microchip Technology Inc. ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-microchip)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=microchip,dmac-g1-dma)。

驱动源码（Driver Source）：[drivers/dma/dma_mchp_dmac_g1.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/dma_mchp_dmac_g1.c)。

<a id="description"></a>

Microchip G1 DMA控制器及驱动。G1组DMA驱动支持的硬件外设为：模块名称DMAC、标识U2503、版本1.0.1。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 13.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `dma-channels` | `int` | **必需**。DMA控制器中可用的DMA通道数量 |
| `dma-alignment` | `int` | DMA传输所需的存储器对齐（Memory Alignment），128位对齐应设为16；默认值：`16` |
| `#dma-cells` | `int` | **必需**。DMA说明符（DMA Specifier）使用的单元数量；固定值：`2` |
| `dma-channel-mask` | `int` | 可用DMA通道的位掩码（Bitmask），按通道升序排列：最低有效位（Least Significant Bit，LSB）对应第一个通道。表示未被固件（Firmware）预留、可供内核（Kernel）使用的通道 |
| `dma-requests` | `int` | 控制器支持的DMA请求信号数量（Number of DMA Request Signals） |
| `dma-buf-addr-alignment` | `int` | 控制器使用的DMA缓冲区（DMA Buffer）的存储器地址对齐要求（Memory Address Alignment Requirement） |
| `dma-buf-size-alignment` | `int` | 控制器使用的DMA缓冲区的存储器大小对齐要求（Memory Size Alignment Requirement） |
| `dma-copy-alignment` | `int` | 控制器能够复制的最小数据块（Minimal Chunk of Data） |

本页没有已弃用的节点专用属性。

## 13.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。DMA控制器存储器映射寄存器（Memory-mapped Registers）的基地址和大小 |
| `interrupts` | `array` | **必需**。与DMA控制器关联的中断编号列表（Interrupt Number List） |
| `clocks` | `phandle-array` | **必需**。DMA控制器使用的时钟源引用（Clock Source Reference） |
| `clock-names` | `string-array` | **必需**。clocks属性引用的时钟源名称 |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
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

## 13.3\_寄存器块命名原例

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

<a id="specifier-cell-names"></a>

## 13.4\_说明符单元名称

DMA说明符单元（DMA Specifier Cells）按原文顺序为：`channel`, `trigsrc`。

名称对照：`channel` 为通道；`trigsrc` 为触发源。

---

[上一章](P012_intel_sedi-dma.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_microchip_dmac-g2-dma.md)
