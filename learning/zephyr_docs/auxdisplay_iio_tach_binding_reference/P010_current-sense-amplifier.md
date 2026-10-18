---
id: learning.zephyr-docs.auxdisplay-iio-tach-binding-reference.page-10
title: current-sense-amplifier
kind: reference
status: maintained
domains: [zephyr, devicetree, display, sensor]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/iio/afe/current-sense-amplifier.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第10章\_current-sense-amplifier

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/iio/afe/current-sense-amplifier.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="current-sense-amplifier"></a>
<a id="dtbinding-current-sense-amplifier"></a>
<a id="std-dtcompatible-current-sense-amplifier"></a>

兼容字符串（Compatible String）：`current-sense-amplifier`。厂商：[ 未指定厂商 ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-no-vendor)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=current-sense-amplifier)。

驱动源码（Driver Source）：[drivers/sensor/current_amp/current_amp.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/current_amp/current_amp.c)。

<a id="description"></a>

当I/O通道测量电流检测放大器（Current Sense Amplifier）的输出电压时，通常关注的是流经检测电阻的电流，而非电阻两端电压。本绑定描述这种电流检测电路。

本绑定基于Linux的[电流检测放大器设备树说明](https://www.kernel.org/doc/Documentation/devicetree/bindings/iio/afe/current-sense-amplifier.yaml)。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 10.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `sense-resistor-milli-ohms` | `int` | **必需**。分流电阻（Shunt Resistor）的阻值，单位为毫欧（mΩ）。 |
| `sense-gain-mult` | `int` | 放大器增益乘数（Gain Multiplier），默认为1，最大65535。；默认值：`1` |
| `sense-gain-div` | `int` | 放大器增益除数（Gain Divider），默认为1，最大65535。；默认值：`1` |
| `zero-current-voltage-mv` | `int` | 零电流电压（Zero-current Voltage），单位为mV，默认0，范围-32768至32767。部分电流检测放大器不依赖检测电阻，而是直接输出与电流成比例的电压，例如霍尔效应电流传感器（Hall-effect Current Sensor），通常以非零偏置电压对应零电流。此类传感器使用本绑定时，`sense-resistor-milli-ohms`应设为1。；默认值：`0` |
| `power-gpios` | `phandle-array` | 控制电流放大器电源。提供本属性时，必须将对应GPIO置为有效电平，才能使能放大器。 |
| `enable-calibration` | `boolean` | 启用电流检测放大器校准（Calibration），用于在测量前校准ADC。 |
| `zephyr,noise-threshold` | `int` | 低于此阈值的原始ADC读数视为噪声，并上报为0 µA。默认0表示禁用阈值。；默认值：`0` |
| `gain-extended-range` | `string` | 主测量达到极限时使用的替代增益（Alternate Gain）。下方完整保留20个ADC增益常量与倍率对照，其中冒号后的`x`表示相乘的倍率，覆盖1/6、1/5、1/4、1/3、2/5、1/2、2/3、4/5及1、2、3、4、6、8、12、16、24、32、64、128倍。；合法值：`ADC_GAIN_1_6, ADC_GAIN_1_5, ADC_GAIN_1_4, ADC_GAIN_1_3, ADC_GAIN_2_5, ADC_GAIN_1_2, ADC_GAIN_2_3, ADC_GAIN_4_5, ADC_GAIN_1, ADC_GAIN_2, ADC_GAIN_3, ADC_GAIN_4, ADC_GAIN_6, ADC_GAIN_8, ADC_GAIN_12, ADC_GAIN_16, ADC_GAIN_24, ADC_GAIN_32, ADC_GAIN_64, ADC_GAIN_128` |
| `friendly-name` | `string` | 描述传感器的可读字符串，可帮助主机操作系统区分同型号的多个实例，例如笔记本电脑上盖与底座的加速度计。此属性定义于[HID Usage Tables规范](https://usb.org/sites/default/files/hut1_3_0.pdf)第22.5节“通用传感器属性用途”（Generic Sensor Property Usages）。 |

本页没有已弃用的节点专用属性。

## 10.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `io-channels` | `phandle-array` | **必需**。采用此分压器配置可用的通道。 |
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

## ADC替代增益原表

```text
- ADC_GAIN_1_6: x 1/6
- ADC_GAIN_1_5: x 1/5
- ADC_GAIN_1_4: x 1/4
- ADC_GAIN_1_3: x 1/3
- ADC_GAIN_2_5: x 2/5
- ADC_GAIN_1_2: x 1/2
- ADC_GAIN_2_3: x 2/3
- ADC_GAIN_4_5: x 4/5
- ADC_GAIN_1:   x 1
- ADC_GAIN_2:   x 2
- ADC_GAIN_3:   x 3
- ADC_GAIN_4:   x 4
- ADC_GAIN_6:   x 6
- ADC_GAIN_8:   x 8
- ADC_GAIN_12:  x 12
- ADC_GAIN_16:  x 16
- ADC_GAIN_24:  x 24
- ADC_GAIN_32:  x 32
- ADC_GAIN_64:  x 64
- ADC_GAIN_128: x 128
```

译注：本页 `io-channels` 说明沿用“此分压器配置”的措辞，按原文保留。

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

---

[上一章](P009_titanmec_tm1637.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_current-sense-shunt.md)
