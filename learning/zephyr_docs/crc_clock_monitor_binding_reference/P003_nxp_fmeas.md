---
id: learning.zephyr-docs.crc-clock-monitor-binding-reference.page-3
title: nxp_fmeas
kind: reference
status: maintained
domains: [zephyr, devicetree, crc, clock]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock-monitor/nxp,fmeas.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第3章\_nxp_fmeas

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock-monitor/nxp,fmeas.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-fmeas"></a>
<a id="dtbinding-nxp-fmeas"></a>
<a id="std-dtcompatible-nxp-fmeas"></a>

兼容字符串（Compatible String）：`nxp,fmeas`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,fmeas)。

驱动源码（Driver Source）：[drivers/clock_monitor/clock_monitor_nxp_fmeas.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_monitor/clock_monitor_nxp_fmeas.c)。

<a id="description"></a>

NXP BASIC频率测量模块（Frequency Measurement，FREQME／fmeas）。这是通过MCUX SDK的fsl_fmeas硬件抽象层（Hardware Abstraction Layer，HAL）驱动的单寄存器FREQMECTRL变体，适用于RT6xx／RT5xx／RW6xx。它相对于参考时钟测量目标时钟，并以Hz返回结果；参考和目标输入通过Zephyr多路复用子系统（Mux Subsystem）经INPUTMUX外设路由。

硬件没有中断线，也没有MIN／MAX阈值寄存器，因此仅支持Zephyr clock_monitor的单次测量模式MEASURE（One-shot），WINDOW模式返回 `-ENOTSUP`。测量窗口由硬件／HAL固定为 `2^20` 个参考时钟周期，因此MEASURE请求中的window_ns仅作建议。

可选时钟源（Clock Source）通过reference-sources和target-sources两个容器子节点（Container Child Node）声明。每个容器为每个可选源包含一个子节点，把INPUTMUX路由与可选频率提供者（Frequency Provider）配对。标记default-source的子节点为上电选择；`clock_monitor_set_source()` 使用INPUTMUX连接标识（Connection Cookie，参见mux-states）在运行期间切换已声明的源。

频率可以通过clock-frequency提供固定Hz值，或通过clocks调用 `clock_control_get_rate()` 查询。两者同时存在时clock-frequency优先。参考源必须解析为非零频率，驱动据此把原始计数转换成Hz；目标源可省略两者，因为此实现仅测量，不预测频率。

驱动不会使能所选源时钟。应用必须在 `configure()/start()` 前确保参考和目标时钟已经运行；未开启的源只会测得零个边沿并报告CLOCK_LOST。reference-sources子节点使用 `NXP_FMEAS_*_REF_*` 连接标识，target-sources子节点使用 `NXP_FMEAS_*_TAR_*` 或共享的 `NXP_FMEAS_*` 标识，参见 `<zephyr/dt-bindings/clock-monitor/nxp-fmeas.h>`。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 3.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `resets` | `phandle-array` | **必需**。FREQME外设复位线。驱动在初始化时切换一次，以使模块退出复位；缺少此步骤时，FREQMECTRL寄存器不工作，写入被丢弃、读取返回0，每次测量也都报告0 |
| `reset-names` | `string-array` | 每个复位（Reset）的名称 |

本页没有已弃用的节点专用属性。

## 3.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `clocks` | `phandle-array` | **必需**。FREQME外设门控时钟（Peripheral Gate Clock，ipg），由驱动调用clock_control_on()使能 |
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

<a id="grandchild-node-properties"></a>

## 孙节点属性

以下属性属于reference-sources和target-sources容器内部的源节点，即孙节点（Grandchild Node），不属于顶层控制器。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `mux-states` | `phandle-array` | **必需**。此源的INPUTMUX路由（Route），以单个mux-states条目 `<&inputmux channel connection>` 指定。&inputmux为INPUTMUX多路复用控制器；channel选择FMEASURE_CH_SEL槽，0为参考输入FMEASURE_CH_SEL[0]，1为目标输入FMEASURE_CH_SEL[1]；connection为zephyr/dt-bindings/clock-monitor/nxp-fmeas.h中的NXP_FMEAS_*连接标识，同时也作为运行期间clock_monitor_set_source()对此源的选择值 |
| `clocks` | `phandle-array` | 通过clock_control_get_rate()查询的频率提供者（Frequency Provider）；存在clock-frequency时被忽略 |
| `clock-frequency` | `int` | 固定频率提供者，单位Hz，直接使用且不查询clock_control，优先于clocks。用于clock_control驱动无法报告速率的源，例如外部晶体（External Crystal） |
| `default-source` | `boolean` | 把此源标记为其容器的上电选择（Power-on Selection）；每个容器必须恰好有一个子节点设置本属性 |
| `mux-controls` | `phandle-array` | MUX控制器说明符（MUX Controller Specifier）列表，每个条目为指向控制器的节点引用，后接#mux-control-cells个寻址单元 |
| `mux-control-names` | `string-array` | mux-controls条目的可选名称 |
| `mux-state-names` | `string-array` | mux-states条目的可选名称 |

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

[上一章](P002_nxp_cmu-fm.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_nxp_freqme.md)
