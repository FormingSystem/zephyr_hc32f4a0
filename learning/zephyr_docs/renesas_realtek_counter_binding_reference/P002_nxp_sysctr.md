---
id: learning.zephyr-docs.renesas-realtek-counter-binding-reference.page-2
title: nxp_sysctr
kind: reference
status: maintained
domains: [zephyr, devicetree, counter]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/counter/nxp,sysctr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第2章\_nxp_sysctr

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/counter/nxp,sysctr.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-sysctr"></a>
<a id="dtbinding-nxp-sysctr"></a>
<a id="std-dtcompatible-nxp-sysctr"></a>

兼容字符串（Compatible String）：`nxp,sysctr`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,sysctr)。

驱动源码（Driver Source）：[drivers/counter/counter_mcux_sysctr.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/counter/counter_mcux_sysctr.c)。

<a id="description"></a>

NXP系统计数器（System Counter，SYS_CTR）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 2.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `clock-source` | `int` | 选择活动时钟源（Active Clock Source），直接对应 `sysctr_clock_source_t`：0为 `kSYSCTR_BaseFrequency`，即正常运行的基准时钟（Base Clock）；1为 `kSYSCTR_AlternateFrequency`，即在硬件内部除以64的慢时钟，用于低功耗（Low Power）。未指定时默认为0。**仅在clock-source为0时支持闹钟功能**；默认值：`0`；合法值：`0, 1` |
| `clock-frequency` | `int` | 活动SYS_CTR计数器时钟的频率，单位Hz；系统定时器驱动据此导出 `CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC` |

本页没有已弃用的节点专用属性。

## 2.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。三个SYS_CTR编程模型（Programming Model）的寄存器块（Register Block）：SYS_CTR_CONTROL用于计数器控制、频率选择及计数值；SYS_CTR_READ以只读方式访问当前计数值；SYS_CTR_COMPARE用于比较帧控制（Compare Frame Control）、中断屏蔽（Interrupt Mask）与状态 |
| `reg-names` | `string-array` | **必需**。三个寄存器块的名称 |
| `interrupts` | `array` | **必需**。比较帧0与比较帧1共享的一条中断线（Interrupt Line） |
| `clocks` | `phandle-array` | **必需**。按顺序提供两个时钟条目：24 MHz XTAL基准时钟与32 kHz LPO慢时钟；使用 `IMX_CCM_SYSCTR_BASE_CLK` 和 `IMX_CCM_SYSCTR_SLOW_CLK` |
| `clock-names` | `string-array` | **必需**。24 MHz基准时钟名称必须为base，32 kHz备用慢时钟名称必须为slow |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
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

---

[上一章](P001_nxp_stm.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_nxp_tpm-timer.md)
