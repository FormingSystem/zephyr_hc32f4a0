---
id: learning.zephyr-docs.stm32-ti-silabs-timer-binding-reference.page-8
title: st_stm32-timers
kind: reference
status: maintained
domains: [zephyr, devicetree, interrupts, timer]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/timer/st,stm32-timers.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第8章\_st_stm32-timers

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/timer/st,stm32-timers.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="st-stm32-timers"></a>
<a id="dtbinding-st-stm32-timers"></a>
<a id="std-dtcompatible-st-stm32-timers"></a>

兼容字符串（Compatible String）：`st,stm32-timers`。厂商：[ STMicroelectronics ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-st)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=st,stm32-timers)。

<a id="description"></a>

STM32定时器（Timer）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 8.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `resets` | `phandle-array` | **必需**。复位（Reset）信息 |
| `st,prescaler` | `int` | **必需**。定时器输入时钟预分频器（Clock Prescaler）。STM32通用定时器（General Purpose Timer）的取值范围为0至0xFFFF，计数频率为 `CLK/(prescaler+1)` |
| `st,countermode` | `int` | 设置计数器模式（Counter Mode），使用 `dt-bindings/timer/stm32-timer.h` 中定义的常量。完整模式说明见下文。若未提供此属性，则使用复位状态 `STM32_TIM_COUNTERMODE_UP`；默认值：`0` |
| `st,deadtime` | `int` | 设置关联定时器的死区时间（Dead Time），在参考信号上升沿与OCx、OCxN两路信号上升沿之间加入延迟。桥式电路（Bridge Circuit）通常需要此功能来避免直通电流（Shoot-through Current）。仅部分定时器实例支持；应查阅产品参考手册（Reference Manual）确认可用性，尤其是STM32L0／STM32L1等系列没有支持该功能的实例；默认值：`0`；范围：`0 to 255` |
| `st,mastermode` | `string` | 选择定时器实例的主模式（Master Mode），即触发输出TRGO的信号源。只对具备主功能（Master Function）的实例有效，否则忽略此属性；完整取值说明见下文，细节参见设备参考手册；默认值：`RESET`；合法值：`RESET, ENABLE, UPDATE, CC1IF, OC1REF, OC2REF, OC3REF, OC4REF` |
| `st,slavemode` | `string` | 选择定时器实例的从模式（Slave Mode）行为，只对具备从功能（Slave Function）的实例有效，否则忽略此属性。仅与采用 `four-channel-capture-support` 模式的 `CONFIG_PWM_CAPTURE` 兼容；完整取值说明见下文，细节参见设备参考手册；默认值：`disabled`；合法值：`disabled, reset, gated, trigger, combined_resettrigger, combined_gatedreset` |
| `st,trigger-selection` | `string` | 选择从模式运行的触发输入（Trigger Input，TRGI）源。只对具备从功能的实例有效，否则忽略此属性。并非所有系列都支持ITR4至ITR15选项；细节参见设备参考手册；默认值：`ITR0`；合法值：`ITR0, ITR1, ITR2, ITR3, ITR4, ITR5, ITR6, ITR7, ITR8, ITR9, ITR10, ITR11, ITR12, ITR13, ITR14, ITR15, TI1F_ED, TI1FP1, TI1FP2, ETRF` |
| `reset-names` | `string-array` | 每个复位的名称 |

本页没有已弃用的节点专用属性。

## 8.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `clocks` | `phandle-array` | **必需**。设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
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

## 计数器模式

输出比较（Output Compare）中断标志的置位时机随模式不同：

| 常量 | 行为 |
| --- | --- |
| `STM32_TIM_COUNTERMODE_UP` | 向上计数（Upcounter） |
| `STM32_TIM_COUNTERMODE_DOWN` | 向下计数（Downcounter） |
| `STM32_TIM_COUNTERMODE_CENTER_DOWN` | 交替向上、向下计数；仅在向下计数时置位输出通道的输出比较中断标志 |
| `STM32_TIM_COUNTERMODE_CENTER_UP` | 交替向上、向下计数；仅在向上计数时置位输出通道的输出比较中断标志 |
| `STM32_TIM_COUNTERMODE_CENTER_UP_DOWN` | 交替向上、向下计数；向上或向下计数时都置位输出通道的输出比较中断标志 |

## 主模式触发输出

| 选项 | TRGO来源 |
| --- | --- |
| `RESET` | `TIMx_EGR` 寄存器中的 `UG` 位 |
| `ENABLE` | 计数器使能信号（Counter Enable Signal）`CNT_EN` |
| `UPDATE` | 更新事件（Update Event） |
| `CC1IF` | `CC1IF` 置位事件 |
| `OC1REF` | `OC1REF` 信号 |
| `OC2REF` | `OC2REF` 信号 |
| `OC3REF` | `OC3REF` 信号 |
| `OC4REF` | `OC4REF` 信号 |

## 从模式触发行为

TRGI来源由 `st,trigger-selection` 指定。

| 选项 | 行为 |
| --- | --- |
| `disabled` | 禁用从模式 |
| `reset` | TRGI上升沿重新初始化计数器，并触发寄存器更新 |
| `gated` | TRGI为高电平时使能计数器时钟；触发信号一旦变低，计数器停止但不复位。启动与停止都受控制 |
| `trigger` | TRGI上升沿启动计数器但不复位；仅控制启动 |
| `combined_resettrigger` | TRGI上升沿重新初始化计数器、触发寄存器更新并启动计数器；并非所有系列均支持 |
| `combined_gatedreset` | TRGI为高电平时使能计数器时钟；触发信号一旦变低，计数器停止并复位。启动与停止都受控制；并非所有系列均支持 |

## 8.3\_寄存器块命名原例

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

[上一章](P007_st_stm32-lptim.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P009_st_stm32u5-lptim.md)
