---
id: learning.zephyr-docs.watchdog-binding-reference.page-2
title: adi_max42500-watchdog
kind: reference
status: maintained
domains: [zephyr, devicetree, watchdog]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/watchdog/adi,max42500-watchdog.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第2章\_adi_max42500-watchdog

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/watchdog/adi,max42500-watchdog.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="adi-max42500-watchdog-on-i2c-bus"></a>
<a id="dtbinding-adi-max42500-watchdog"></a>
<a id="std-dtcompatible-adi-max42500-watchdog"></a>

兼容字符串（Compatible String）：`adi,max42500-watchdog`。厂商：[ Analog Devices, Inc. ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-adi)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=adi,max42500-watchdog)。

驱动源码（Driver Source）：[drivers/watchdog/wdt_adi_max42500.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/wdt_adi_max42500.c)。

<a id="description"></a>

用于配置并使用MAX42500电压监测器／看门狗（Voltage Monitor/Watchdog）的驱动；本绑定位于集成电路间总线（Inter-Integrated Circuit，I²C）上。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

以下顶层属性（Top-level Properties）用于MAX42500看门狗节点本身。

## 2.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `wdiv` | `int` | 看门狗时钟分频器（Watchdog Clock Divider，WDIV）的值，用于调整窗口值及相关计算。未设置时使用从一次性可编程存储器（One-Time Programmable Memory，OTP）加载到设备中的默认值 |
| `enable-vmpd` | `boolean` | 启用电压监测器掉电（Voltage-monitor Power-down），在EN0为低电平时降低集成电路（IC）功耗 |
| `mode` | `string` | 选择简单窗口看门狗（Simple Windowed Watchdog）或质询／响应（Challenge/Response）模式；值 `default` 保留从OTP加载的模式；合法值：`default, sww, challenge_response` |
| `supply-gpios` | `phandle-array` | 控制设备电源的通用输入输出（General-Purpose Input/Output，GPIO）说明符。设备有专用电源开关时应提供此属性，供电状态完全由设备驱动负责；与 `vin-supply` 相对照 |
| `vin-supply` | `phandle` | 引用控制设备电源的稳压器（Regulator），被引用的设备树节点必须具有稳压器兼容字符串。设备由共享稳压器供电时应提供此属性；供电状态取决于由该稳压器供电的全部设备的请求状态。与 `supply-gpios` 相对照：两者都提供时，必须先请求稳压器，再将供电GPIO置为有效状态；释放稳压器前必须先将供电GPIO置为无效状态 |

本页没有已弃用的节点专用属性。

## 2.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `#address-cells` | `int` | **必需**。子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`1` |
| `#size-cells` | `int` | **必需**。子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`0` |
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

## 电压输入子节点属性

以下属性放在子节点（Child Node）中。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `int` | **必需**。需要配置的电压输入通道（Voltage Input Channel）。通道1至5为单端（Single-ended），通道6和7为差分（Differential） |
| `nominal-voltage` | `int` | 通道1至5设置标称电压（Nominal Voltage）；通道6和7是差分通道，只使用欠压／过压（Under Voltage/Over Voltage，UV/OV）设置 |
| `uv-limit` | `int` | **必需**。欠压阈值（Under-voltage Limit）。通道1至5使用以标称电压为基准的百分比；通道6和7使用绝对电压（Absolute Voltage） |
| `ov-limit` | `int` | **必需**。过压阈值（Over-voltage Limit）。通道1至5使用以标称电压为基准的百分比；通道6和7使用绝对电压 |
| `uvov-trigger-reset` | `boolean` | 表示该通道出现欠压／过压情形时，应触发复位条件（RESET Condition） |

## 2.3\_寄存器块命名原例

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

[上一章](P001_adi_max32-watchdog.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_ambiq_watchdog.md)
