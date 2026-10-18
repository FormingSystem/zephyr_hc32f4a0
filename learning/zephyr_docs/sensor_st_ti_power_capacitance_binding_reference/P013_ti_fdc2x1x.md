---
id: learning.zephyr-docs.sensor-st-ti-power-capacitance-binding-reference.page-13
title: ti_fdc2x1x
kind: reference
status: maintained
domains: [zephyr, devicetree, sensor]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/ti,fdc2x1x.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第13章\_ti_fdc2x1x

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/ti,fdc2x1x.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="ti-fdc2x1x-on-i2c-bus"></a>
<a id="dtbinding-ti-fdc2x1x"></a>
<a id="std-dtcompatible-ti-fdc2x1x"></a>

兼容字符串（Compatible String）：`ti,fdc2x1x`。厂商：[ Texas Instruments ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-ti)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=ti,fdc2x1x)。

驱动源码（Driver Source）：[drivers/sensor/ti/fdc2x1x/fdc2x1x.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/fdc2x1x/fdc2x1x.c)。

<a id="description"></a>

Texas Instruments FDC2X1X 电容传感器（Capacitive Sensor）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 13.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `sd-gpios` | `phandle-array` | 传感器接收的 SD 信号默认高电平有效；属性标志应准确描述实际送到驱动的信号。 |
| `intb-gpios` | `phandle-array` | 传感器输出的 INTB 信号默认低电平有效；属性标志应准确描述实际送到驱动的信号。 |
| `fdc2x14` | `boolean` | 设置此属性，表示传感器为 FDC2114 或 FDC2214，即四通道版本。 |
| `autoscan` | `boolean` | 设置自动扫描模式（Auto-Scan Mode）：`false` 在 `active-channel` 指定的单一通道连续转换，即单通道模式；`true` 按 `rr-sequence` 指定的顺序自动扫描转换，即多通道模式。 |
| `fref` | `int` | **必需**。所用时钟源的参考频率（Reference Frequency），单位 kHz。内部时钟在 20 °C 时约为 43360 kHz（43.36 MHz）；建议外部时钟源使用 40000 kHz（40 MHz）。 |
| `rr-sequence` | `int` | 自动扫描顺序（Auto-Scan Sequence）配置。FDC 依次对所选序列中的每个通道进行一次转换，再不断重复该序列。上电复位后默认转换通道 0 和 1；仅在 `autoscan=true` 的多通道模式下适用。0 = Ch0、Ch1；1 = Ch0、Ch1、Ch2；2 = Ch0、Ch1、Ch2、Ch3。后两项仅适用于 FDC2114、FDC2214。；默认值：`0`；合法值：`0, 1, 2` |
| `active-channel` | `int` | 选择连续转换（Continuous Conversion）的通道。上电复位后默认使用通道 0；仅在 `autoscan=false` 的单通道模式下适用。0、1、2、3 分别表示在对应编号通道连续转换；通道 2 和 3 仅适用于 FDC2114、FDC2214。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `deglitch` | `int` | **必需**。输入毛刺滤波器（Deglitch Filter）带宽。选择高于 LC 谐振回路振荡频率的最低一档：1 = 1 MHz；4 = 3.3 MHz；5 = 10 MHz；7 = 33 MHz。；合法值：`1, 4, 5, 7` |
| `sensor-activate-sel` | `string` | 传感器激活模式（Sensor Activation Mode）选择，上电复位后默认为 `low-power`。`full-current` 使用最大传感器驱动电流，以缩短激活时间；`low-power` 在激活期间使用 `idrive` 编程的电流，以尽量降低功耗。；默认值：`low-power`；合法值：`full-current, low-power` |
| `ref-clk-src` | `string` | 参考频率源（Reference Frequency Source）选择，上电复位后默认使用内部时钟。`internal` 使用内部振荡器；`external` 从 CLKIN 引脚输入参考频率。；默认值：`internal`；合法值：`internal, external` |
| `current-drive` | `string` | 传感器驱动电流（Sensor Drive Current）选择，上电复位后默认为 `normal`。原文规定 `autoscan=false` 时不支持高电流驱动，会退回普通模式。`normal` 以普通电流驱动所有通道，最大 1.5 mA；`high` 以大于 1.5 mA 的电流驱动通道 0。；默认值：`normal`；合法值：`normal, high` |
| `output-gain` | `int` | 输出增益（Output Gain）控制，仅适用于 FDC2112、FDC2114，上电复位后默认编码为 0。0：增益 1、有效分辨率 12 位、满量程 100%；1：增益 4、有效分辨率 14 位、满量程 25%；2：增益 8、有效分辨率 15 位、满量程 12.5%；3：增益 16、有效分辨率 16 位、满量程 6.25%。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `friendly-name` | `string` | 描述传感器的可读字符串，可帮助主机操作系统区分同型号的多个实例，例如笔记本电脑上盖与底座的加速度计。此属性定义于[HID Usage Tables规范](https://usb.org/sites/default/files/hut1_3_0.pdf)第22.5节“通用传感器属性用途”（Generic Sensor Property Usages）。 |
| `supply-gpios` | `phandle-array` | 控制设备供电的GPIO说明符（Specifier）。设备有专用供电开关时提供此属性，供电状态完全由设备驱动负责；与vin-supply的共享稳压器方式相区别 |
| `vin-supply` | `phandle` | 控制设备供电的稳压器引用，目标设备树节点必须使用稳压器兼容字符串。通过共享稳压器供电时应提供此属性，其供电状态取决于所有受电设备的请求状态。若同时提供supply-gpios，则必须先请求稳压器再将GPIO置为有效；释放稳压器前，必须先将GPIO置为无效 |

本页没有已弃用的节点专用属性。

## 13.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
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
| `rcount` | `int` | **必需**。通道 X 的参考计数转换间隔时间（Reference Count Conversion Interval Time）。；范围：`256 to 65535` |
| `offset` | `int` | 通道 X 的转换偏移（Conversion Offset），仅适用于 FDC2112、FDC2212；上电复位后默认为 0。；默认值：`0`；范围：`0 to 65535` |
| `settlecount` | `int` | **必需**。通道 X 的转换稳定时间（Conversion Settling）。FDC 在开始通道 X 的转换前等待此时间，让 LC 传感器稳定。；范围：`0 to 65535` |
| `fref-divider` | `int` | **必需**。通道 X 的参考分频器（Reference Divider），设置该通道参考信号的分频比，用于缩放最大转换频率。；范围：`1 to 1023` |
| `idrive` | `int` | **必需**。通道 X 的传感器驱动电流。此字段定义通道 X 传感器时钟稳定阶段及转换阶段使用的驱动电流（Drive Current）。；范围：`0 to 31` |
| `fin-sel` | `int` | **必需**。通道 X 的传感器频率选择（Sensor Frequency Select）。差分传感器（Differential Sensor）配置：1 表示除以 1，用于 0.01–8.75 MHz；2 表示除以 2，用于 5–10 MHz。单端传感器（Single-Ended Sensor）配置：2 表示除以 2，用于 0.01–10 MHz。；合法值：`1, 2` |
| `inductance` | `int` | **必需**。印制电路板（PCB）上该通道感测网络使用的电感值，通常为 18 µH。 |

## 参数编码原始对照 6

```text
0 = Ch0, Ch1
1 = Ch0, Ch1, Ch2 (FDC2114, FDC2214 only)
2 = Ch0, Ch1, Ch2, Ch3 (FDC2114, FDC2214 only)
```

## 参数编码原始对照 7

```text
0 = Perform continuous conversions on Channel 0
1 = Perform continuous conversions on Channel 1
2 = Perform continuous conversions on Channel 2 (FDC2114, FDC2214 only)
3 = Perform continuous conversions on Channel 3 (FDC2114, FDC2214 only)
```

## 参数编码原始对照 8

```text
1 = 1MHz
4 = 3.3MHz
5 = 10MHz
7 = 33MHz
```

## 参数编码原始对照 12

```text
0 = Gain = 1   | Effective Resolution 12 bits | 100% full scale
1 = Gain = 4   | Effective Resolution 14 bits | 25% full scale
2 = Gain = 8   | Effective Resolution 15 bits | 12.5% full scale
3 = Gain = 16  | Effective Resolution 16 bits | 6.25% full scale
```

## 参数编码原始对照 52

```text
1 = divide by 1. Choose for sensor frequencies between
0.01MHz and 8.75MHz
2 = divide by 2. Choose for sensor frequencies between 5MHz
and 10MHz

For single-ended sensor configuration:
2 = divide by 2. Choose for sensor frequencies between
```

译注：`current-drive` 原文明确写作 `autoscan=false` 时不支持高电流驱动，此处按原文保留该条件；未擅自改为相反条件。

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

---

[上一章](P012_ti_fdc1004.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_ti_hdc.md)
