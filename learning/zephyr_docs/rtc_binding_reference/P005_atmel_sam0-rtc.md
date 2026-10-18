---
id: learning.zephyr-docs.rtc-binding-reference.page-5
title: 使能比较／闹钟0事件
kind: reference
status: maintained
domains: [zephyr, devicetree, rtc]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/rtc/atmel,sam0-rtc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第5章\_atmel_sam0-rtc

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/rtc/atmel,sam0-rtc.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="atmel-sam0-rtc"></a>
<a id="dtbinding-atmel-sam0-rtc"></a>
<a id="std-dtcompatible-atmel-sam0-rtc"></a>

兼容字符串（Compatible String）：`atmel,sam0-rtc`。厂商：[ Atmel Corporation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-atmel)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=atmel,sam0-rtc)。

驱动源码（Driver Source）：[drivers/rtc/rtc_sam0.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/rtc_sam0.c)。

<a id="description"></a>

Atmel SAM0实时时钟（Real-Time Clock，RTC）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 5.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `atmel,assigned-clocks` | `phandle-array` | **必需**。分配的时钟（Assigned Clock）信息 |
| `atmel,assigned-clock-names` | `string-array` | **必需**。每个分配时钟的名称 |
| `systimer` | `boolean` | 选择RTC外设作为系统定时器（System Timer），取代Arm SysTick。启用后，RTC进入系统定时器独占模式（Exclusive Mode），正常RTC功能不可用；启用原例见下文 |
| `cal-constant` | `int` | **必需**。定义用于计算校准（Calibration）的常数。更多信息参见各SoC系列数据手册（Datasheet）的RTC频率校正（Frequency Correction）章节；公式和配置原例见下文 |
| `counter-mode` | `string` | 配置RTC计数器运行模式（Counter Operating Mode）：模式0将寄存器配置为32位计数器，模式1类似但仅为16位计数器，模式2配置为时钟／日历（Clock/Calendar）；原例见下文；合法值：`count-32, count-16, clock` |
| `prescaler` | `int` | 原文描述为：以指定频率使能CLKOUT；禁用时CLKOUT引脚为低电平，默认值0表示禁用CLKOUT信号。译注：此段来自名为 `prescaler` 的属性，原文称默认0，但下方合法值不含0；原文与配置示例均保留；合法值：`1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024` |
| `event-control-msk` | `int` | 通过位掩码（Bitmask）使能外设事件源（Event Source），默认所有通道均禁用；完整事件表和配置原例见下文；默认值：`0` |
| `alarms-count` | `int` | RTC设备支持的闹钟（Alarm）数量，默认值0表示RTC没有闹钟；默认值：`0` |
| `pinctrl-0` | `phandles` | 第一个状态（State）的引脚配置（Pin Configuration），具体内容由所选引脚控制器驱动（Pin Controller Driver）实现决定 |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置（Pin Configuration）；参见 `pinctrl-0` |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置（Pin Configuration）；参见 `pinctrl-0` |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置（Pin Configuration）；参见 `pinctrl-0` |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置（Pin Configuration）；参见 `pinctrl-0` |
| `pinctrl-names` | `string-array` | 所提供状态的名称；名称数量必须与状态数量匹配 |

本页没有已弃用的节点专用属性。

## 5.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `clocks` | `phandle-array` | **必需**。设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
| `clock-names` | `string-array` | **必需**。`clocks` 中各时钟提供者的名称；通用说明称其为可选名称，是否必须填写以本层的必需标记为准 |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
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

## 启用系统定时器独占模式

```dts
  &rtc {
    status = "okay";
    systimer;
  };
```

## 校准常数

原式中的Correction指频率校正量，ppm为百万分率（Parts Per Million）：

```text
  Correction in ppm = (FREQCORR.VALUE * 1e6 ppm) / (8192 * 128)
```

```dts
  &rtc {
    cal-constant = <8192 * 128>;
  };
```

## 计数器运行模式

```dts
  &rtc {
    status = "okay";
    counter-mode = "clock";
    prescaler = <1024>;
  };
```

## prescaler属性原例

```dts
  &rtc {
    status = "okay";
    counter-mode = "clock";
    prescaler = <1024>;
  };
```

## 使能比较／闹钟0事件

| 位号 | 事件源（Event Source） |
| --- | --- |
| 0 | 周期间隔0事件输出（Periodic Interval 0 Event Output） |
| 1 | 周期间隔1事件输出（Periodic Interval 1 Event Output） |
| 2 | 周期间隔2事件输出（Periodic Interval 2 Event Output） |
| 3 | 周期间隔3事件输出（Periodic Interval 3 Event Output） |
| 4 | 周期间隔4事件输出（Periodic Interval 4 Event Output） |
| 5 | 周期间隔5事件输出（Periodic Interval 5 Event Output） |
| 6 | 周期间隔6事件输出（Periodic Interval 6 Event Output） |
| 7 | 周期间隔7事件输出（Periodic Interval 7 Event Output） |
| 8 | 比较／闹钟0事件输出（Compare/Alarm 0 Event Output） |
| 9 | 比较／闹钟1事件输出（Compare/Alarm 1 Event Output） |
| 14 | 篡改事件输出（Tamper Event Output） |
| 15 | 溢出事件输出（Overflow Event Output） |
| 16 | 篡改事件输入（Tamper Event Input） |

原文给出的使能比较／闹钟0事件输出配置如下。译注：原例数值为 `<100>`，与上表位8的位掩码含义不一致；按原样保留。

```dts
  &rtc {
    event-control-msk = <100>;
  };
```

## 5.3\_寄存器块命名原例

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

[上一章](P004_atmel_sam-rtc.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P006_epson_rx8130ce-rtc.md)
