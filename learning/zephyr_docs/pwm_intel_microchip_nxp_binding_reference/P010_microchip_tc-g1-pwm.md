---
id: learning.zephyr-docs.pwm-intel-microchip-nxp-binding-reference.page-10
title: microchip_tc-g1-pwm
kind: reference
status: maintained
domains: [zephyr, devicetree, pwm]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pwm/microchip,tc-g1-pwm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第10章\_microchip_tc-g1-pwm

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pwm/microchip,tc-g1-pwm.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="microchip-tc-g1-pwm"></a>
<a id="dtbinding-microchip-tc-g1-pwm"></a>
<a id="std-dtcompatible-microchip-tc-g1-pwm"></a>

兼容字符串（Compatible String）：`microchip,tc-g1-pwm`。厂商：[ Microchip Technology ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-microchip)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=microchip,tc-g1-pwm)。

驱动源码（Driver Source）：[drivers/pwm/pwm_mchp_tc_g1.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/pwm_mchp_tc_g1.c)。

<a id="description"></a>

Microchip PWM TC g1驱动，负责为PWM用途配置和管理Microchip微控制器中的定时器／计数器（Timer/Counter，TC）外设，支持`tc-u2249 (3.0.0)`。

下方保留DTS使用原例。`pwm_led0`代表由PWM驱动的设备，例如LED；`pwms`引用控制器`tc0`，周期为20 ms，极性0表示正常。原文解释称其指定“通道2”，但示例写的是1；此处保留差异。参数顺序为`<&controller channel period polarity>`，与`pwm-cells`定义一致，使设备采用指定配置由Microchip PWM TC驱动控制。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 10.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `#pwm-cells` | `int` | **必需**。PWM说明符（PWM Specifier）中预期的单元数量。；固定值：`3` |
| `channels` | `int` | **必需**。控制器支持的PWM通道（Channel）数量。 |
| `prescaler` | `int` | 定时器预分频值（Timer Prescaler）；用于对输入时钟分频，取得所需定时器频率。；合法值：`1, 2, 4, 8, 16, 64, 256, 1024` |
| `max-bit-width` | `int` | **必需**。PWM计数器支持的最大位宽（Maximum Bit Width），表示其分辨率。设备树应填写该硬件实例支持的最大值；只有核对相关系列数据手册、确保兼容后才应覆盖。；合法值：`8, 16, 32` |
| `pinctrl-0` | `phandles` | 第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-names` | `string-array` | 所提供状态的名称，名称数量必须与状态数量一致 |

本页没有已弃用的节点专用属性。

## 10.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。定时器／计数器外设寄存器组的基地址与大小（Base Address and Size）。 |
| `interrupts` | `array` | **必需**。定时器／计数器外设使用的中断线路，指定中断号与优先级（Interrupt Number and Priority）。 |
| `clocks` | `phandle-array` | **必需**。定时器／计数器外设的时钟源及其配置，确保外设取得所需时钟信号。适用时钟名包括`mclk`、`gclk`及可选的`client_mclk`。后者是可与当前实例配对的另一实例（Client）的时钟子系统，只适用于能与另一实例配对以提高最大位宽的外设；这里通过两个实例配对可得到32位最大位宽。是否支持配对应查各自数据手册，并非所有实例都具备此能力。 |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
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

## TC官方配置示例

```dts
   pwm_led0: pwm_led_0 {
       status = "okay";
       pwms = <&tc0 1 PWM_MSEC(20) 0>;
   };
```

## 10.3\_寄存器块命名原例

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

## 10.4\_说明符单元名称

PWM说明符单元（PWM Specifier Cells）按原文顺序为：`channel`, `period`, `polarity`。

名称对照：`channel` 为通道；`period` 为周期；`polarity` 为极性。

---

[上一章](P009_microchip_pwm-g1.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_microchip_tcc-g1-pwm.md)
