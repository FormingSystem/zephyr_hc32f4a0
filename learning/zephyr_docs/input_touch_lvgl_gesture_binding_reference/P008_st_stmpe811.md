---
id: learning.zephyr-docs.input-touch-lvgl-gesture-binding-reference.page-8
title: st_stmpe811
kind: reference
status: maintained
domains: [zephyr, devicetree, input]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/st,stmpe811.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第8章\_st_stmpe811

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/st,stmpe811.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="st-stmpe811-on-i2c-bus"></a>
<a id="dtbinding-st-stmpe811"></a>
<a id="std-dtcompatible-st-stmpe811"></a>

兼容字符串（Compatible String）：`st,stmpe811`。厂商：[ STMicroelectronics ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-st)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=st,stmpe811)。

驱动源码（Driver Source）：[drivers/input/input_stmpe811.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/input/input_stmpe811.c)。

<a id="description"></a>

STMPE811 I²C触摸屏控制器（Touchscreen Controller）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 8.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `int-gpios` | `phandle-array` | 中断GPIO（Interrupt GPIO），控制器用它通知触摸数据已就绪，低电平有效。 |
| `raw-x-min` | `int` | 用于缩放上报坐标的有符号原始X轴起点（Signed Raw X Start）。未设置屏幕尺寸时不起作用。 |
| `raw-y-min` | `int` | 用于缩放上报坐标的有符号原始Y轴起点（Signed Raw Y Start）。未设置屏幕尺寸时不起作用。 |
| `raw-x-max` | `int` | 用于缩放上报坐标的原始X轴终点（Raw X End）。未设置屏幕尺寸时不起作用。 |
| `raw-y-max` | `int` | 用于缩放上报坐标的原始Y轴终点（Raw Y End）。未设置屏幕尺寸时不起作用。 |
| `panel-driver-settling-time-us` | `int` | **必需**。面板驱动稳定时间（Panel Driver Settling Time），单位为微秒。对于大于6英寸的面板，建议在触摸屏端子连接10 nF电容以滤除噪声。一般1～5 nF电容需要约500 μs稳定时间，5～10 nF需要约1 ms；使用更大电容时应修改此值，否则可能造成测量不准确。；合法值：`10, 100, 500, 1000, 5000, 10000, 50000, 100000` |
| `touch-detect-delay-us` | `int` | **必需**。触摸检测延迟（Touch Detect Delay），单位为微秒，表示从启用X+线的上拉电阻到设备执行触摸检测之间的时间。不接电容或使用较小电容时可减小此值以降低检测延迟，但可能降低位置稳定性。；合法值：`10, 50, 100, 500, 1000, 5000, 10000, 50000` |
| `touch-average-control` | `int` | **必需**。平均控制（Average Control），即采样数量，可设为任一支持值。值越大，噪声滤除越充分，但触摸检测延迟也越大。要求低检测延迟的场景可选较小值，代价是噪声滤除能力降低。；合法值：`1, 2, 4, 8` |
| `tracking-index` | `int` | **必需**。跟踪指数（Tracking Index）规定当前与上一次触摸位置之间的最小距离；距离小于该值的结果会被丢弃。减小此值可提高触摸事件频率，同时增加系统负载。；合法值：`0, 4, 8, 16, 32, 64, 92, 127` |
| `supply-gpios` | `phandle-array` | 控制设备供电的GPIO说明符（Specifier）。设备有专用供电开关时提供此属性，供电状态完全由设备驱动负责；与vin-supply的共享稳压器方式相区别 |
| `vin-supply` | `phandle` | 控制设备供电的稳压器引用，目标设备树节点必须使用稳压器兼容字符串。通过共享稳压器供电时应提供此属性，其供电状态取决于所有受电设备的请求状态。若同时提供supply-gpios，则必须先请求稳压器再将GPIO置为有效；释放稳压器前，必须先将GPIO置为无效 |
| `screen-width` | `int` | 触摸屏水平分辨率（Horizontal Resolution），即上报最大x坐标加1。默认值可用于未反转轴；显示器x轴反转时必须提供正确值。；默认值：`0` |
| `screen-height` | `int` | 触摸屏垂直分辨率（Vertical Resolution），即上报最大y坐标加1。默认值可用于未反转轴；显示器y轴反转时必须提供正确值。；默认值：`0` |
| `inverted-x` | `boolean` | 反转X轴（Invert X Axis）。 |
| `inverted-y` | `boolean` | 反转Y轴（Invert Y Axis）。 |
| `swapped-x-y` | `boolean` | 交换X、Y轴（Swap X/Y Axes），交换操作在轴反转之后执行。 |
| `display` | `phandle` | 可选的显示控制器引用（Display Controller Handle），表示此触摸屏对应的显示器。提供后，输出宽高从所引用节点的 `width`／`height` 取得，忽略下方 `output-width`／`output-height`，避免重复定义面板分辨率；未提供时使用这两个输出尺寸属性。 |
| `output-width` | `int` | 触摸屏所绑定显示器的水平分辨率（Display Horizontal Resolution）。两对尺寸表示不同坐标空间：`screen-width`／`screen-height` 描述触摸控制器上报范围，`output-width`／`output-height` 描述坐标应落到的显示面板范围。同时提供两个输出尺寸时，将前者缩放到后者；省略时不缩放，原样上报控制器坐标。设置 `display` 后，输出尺寸改由引用节点提供，本属性被忽略。缩放在反转与交换之后进行，使 `swapped-x-y` 可用于宽高不同的旋转面板：交换后的轴带有彼此的原始范围，仅交换而不缩放会与显示范围不匹配。 |
| `output-height` | `int` | 触摸屏所绑定显示器的垂直分辨率（Display Vertical Resolution），参见 `output-width`。 |

本页没有已弃用的节点专用属性。

## 8.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。设备在I²C总线上的地址（Device Address） |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
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

[上一章](P007_st_stm32-tsc.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P009_tbs_crsf.md)
