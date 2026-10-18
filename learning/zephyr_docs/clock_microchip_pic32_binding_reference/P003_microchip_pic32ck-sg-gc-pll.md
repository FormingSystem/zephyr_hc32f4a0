---
id: learning.zephyr-docs.clock-microchip-pic32-binding-reference.page-3
title: microchip_pic32ck-sg-gc-pll
kind: reference
status: maintained
domains: [zephyr, devicetree, clock]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/microchip/pic32ck_sg_gc/microchip,pic32ck-sg-gc-pll.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第3章\_microchip_pic32ck-sg-gc-pll

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/microchip/pic32ck_sg_gc/microchip,pic32ck-sg-gc-pll.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="microchip-pic32ck-sg-gc-pll"></a>
<a id="dtbinding-microchip-pic32ck-sg-gc-pll"></a>
<a id="std-dtcompatible-microchip-pic32ck-sg-gc-pll"></a>

兼容字符串（Compatible String）：`microchip,pic32ck-sg-gc-pll`。厂商：[ Microchip Technology Inc. ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-microchip)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=microchip,pic32ck-sg-gc-pll)。

<a id="description"></a>

PIC32CK_SG_GC锁相环（Phase Locked Loop，PLL）时钟。由4～48MHz参考输入时钟产生12.7～200MHz输出；供小数分频模块（Fractional Divider Module）使用时，频率可达1.6GHz。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 3.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

## 3.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg` | `array` | 给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
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
| `subsystem` | `int` | **必需**。时钟子系统（Clock Subsystem）。 |
| `pll-enable` | `int` | 振荡器使能控制（Oscillator Enable）：0禁用，1启用。；默认值：`0`；合法值：`0, 1` |
| `pll-on-demand-en` | `int` | 按需振荡器控制（On-demand Oscillator Control）：0表示振荡器始终开启；1表示仅在外设请求将其作为时钟源时运行，没有请求则停止。重要：若初始化时同时将此项和时钟使能设为1，而时钟初始化序列中没有外设请求该时钟，可能无限等待时钟开启。如有需要，宜通过API开启时钟，避免在启动时同时启用两者。；默认值：`0`；合法值：`0, 1` |
| `pll-bandwidth-sel` | `string` | 选择PLL0闭环滤波带宽（Closed-loop Filter Bandwidth）。根据参考分频后的频率FPFD选择；正确的滤波带宽对PLL0压控振荡器（Voltage Controlled Oscillator，VCO）工作于最佳范围非常重要。；默认值：`bwsel-0`；合法值：`bwsel-0, bwsel-1, bwsel-2, bwsel-3, bwsel-4, bwsel-5, bwsel-6, bwsel-7` |
| `pll-src` | `string` | 参考时钟源选择（Reference Clock Source Selection），为PLL选择参考源时钟。；默认值：`dfll48m`；合法值：`gclk0, gclk1, gclk2, gclk3, gclk4, gclk5, gclk6, gclk7, gclk8, gclk9, gclk10, gclk11, xosc, dfll48m` |
| `pll-feedback-divider-factor` | `int` | PLL反馈分频值（Feedback Divider）。此字段决定PLL0的VCO输出频率与PLL0参考输入频率之比。写入FBDIV（feedback-divider-factor）位会导致失锁（Lock Lost）；必须满足 `21 ≤ FBDIV ≤ 1023`。VCO振荡频率为 `FVCO = FCKR * (FBDIV / REFDIV)`，必须在800～1600MHz之间。源时钟fCKR、REFDIV（ref-division-factor）和FBDIV的选择均须满足此条件。；默认值：`0` |
| `pll-ref-division-factor` | `int` | PLL参考分频值（Reference Divider），决定PLL0输入参考频率的分频系数。写入REFDIV位会导致失锁；必须满足 `1 ≤ REFDIV ≤ 63`。参考分频后的频率为 `FPFD = FCKR / REFDIV`，FPFD必须始终在4～48MHz之间。；默认值：`0` |
| `pll-freq-division-factor-int` | `int` | PLL频率分频系数整数部分（Integer Part），决定PLL0的VCO输出频率与PLL0参考输入频率之比。；默认值：`0` |
| `pll-freq-division-factor-rem` | `int` | PLL频率分频系数余数部分（Remainder Part），决定PLL0的VCO输出频率与PLL0参考输入频率之比。；默认值：`0` |

<a id="grandchild-node-properties"></a>

## 孙节点属性（Grandchild Properties）

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `subsystem` | `int` | **必需**。时钟子系统（Clock Subsystem）。 |
| `pll-output-en` | `int` | PLL输出使能控制（Output Enable Control）：0禁用输出，1启用输出。；默认值：`0`；合法值：`0, 1` |
| `pll-output-division-factor` | `int` | PLL输出分频系数（Output Division Factor）。此字段决定PLL0 FVCO输出的分频比，用来生成FCLK_PLL0和CLK_PLL0_CLKOUTn。POSTDIV必须满足 `1 ≤ POSTDIV ≤ 63`。；默认值：`0` |

## 3.3\_寄存器块命名原例

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

---

[上一章](P002_microchip_pic32ck-sg-gc-mclkperiph.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_microchip_pic32ck-sg-gc-rtc.md)
