---
id: learning.zephyr-docs.sensor-ti-vishay-wurth-sensing-binding-reference.page-12
title: vishay_vcnl36825t
kind: reference
status: maintained
domains: [zephyr, devicetree, sensor]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/vishay,vcnl36825t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第12章\_vishay_vcnl36825t

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/vishay,vcnl36825t.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="vishay-vcnl36825t-on-i2c-bus"></a>
<a id="dtbinding-vishay-vcnl36825t"></a>
<a id="std-dtcompatible-vishay-vcnl36825t"></a>

兼容字符串（Compatible String）：`vishay,vcnl36825t`。厂商：[ Vishay Intertechnology, Inc ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-vishay)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=vishay,vcnl36825t)。

驱动源码（Driver Source）：[drivers/sensor/vishay/vcnl36825t/vcnl36825t.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/vishay/vcnl36825t/vcnl36825t.c)。

<a id="description"></a>

VCNL36825T 接近与环境光传感器（Proximity and Ambient Light Sensor），参见 [VCNL36825T 数据手册](https://www.vishay.com/docs/84274/vcnl36825t.pdf)。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 12.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `operation-mode` | `string` | 工作模式（Mode of Operation）：`auto` 连续采样；`force` 在每次获取（fetch）命令时采样。默认值为传感器复位值；`force` 仅在低功耗模式未启用时可用。；默认值：`auto`；合法值：`auto, force` |
| `measurement-period` | `int` | 测量周期（Measurement Period），单位 ms，值越大，功耗越低。原文限定：10–80 ms 仅用于非低功耗模式，80–320 ms 仅用于低功耗模式；同时又说明默认 40 ms 在普通与低功耗模式下均受支持。此处保留这两处说明。；默认值：`40`；合法值：`10, 20, 40, 80, 160, 320` |
| `proximity-it` | `string` | 接近感测积分时间（Proximity Integration Time），单位 T，默认值为传感器复位值。；默认值：`1`；合法值：`1, 2, 4, 8` |
| `proximity-itb` | `int` | 接近感测积分时间单位 T 的时长，单位 µs，默认值为传感器复位值。；默认值：`25`；合法值：`25, 50` |
| `multi-pulse` | `int` | 每次测量的脉冲数（Pulse Count）。值越大，精度和功耗越高；默认值为传感器复位值。；默认值：`1`；合法值：`1, 2, 4, 8` |
| `laser-current` | `int` | 测量期间激光器使用的电流（Laser Current），默认为允许的最小值。；默认值：`10`；合法值：`10, 12, 14, 16, 18, 20` |
| `low-power` | `boolean` | 启用低功耗模式（Low-Power Mode），允许将测量周期增加到 320 ms。 |
| `high-gain` | `boolean` | 启用高增益模式（High-Gain Mode）。 |
| `sunlight-cancellation` | `boolean` | 启用阳光消除（Sunlight Cancellation）功能。 |
| `high-dynamic-output` | `boolean` | 启用 16 位高动态输出模式（High Dynamic Output Mode），不能与阈值中断（Threshold Interrupt）同时使用。 |
| `int-gpios` | `phandle-array` | INT 信号连接，传感器输出时低电平有效。 |
| `int-mode` | `string` | 中断行为（Interrupt Behavior）：`normal` 在超过上阈值或低于下阈值且达到接近计数条件时通知；`first high` 首次超过上阈值时通知，随后低于下阈值且达到计数条件时再次通知，若从未超过上阈值则不触发；`logic high / low` 在超过上阈值且达到计数条件时有效，低于下阈值时解除。默认 `normal`，因为最容易配置。；默认值：`normal`；合法值：`normal, first high, logic high / low` |
| `int-proximity-count` | `int` | 发出中断所需的连续高于／低于阈值的测量次数，默认值为传感器复位值。；默认值：`1`；合法值：`1, 2, 3, 4` |
| `int-smart-persistence` | `boolean` | 启用智能持续判定（Smart Persistence），以缩短发出中断前的总响应时间。 |
| `friendly-name` | `string` | 描述传感器的可读字符串，可帮助主机操作系统区分同型号的多个实例，例如笔记本电脑上盖与底座的加速度计。此属性定义于[HID Usage Tables规范](https://usb.org/sites/default/files/hut1_3_0.pdf)第22.5节“通用传感器属性用途”（Generic Sensor Property Usages）。 |
| `supply-gpios` | `phandle-array` | 控制设备供电的GPIO说明符（Specifier）。设备有专用供电开关时提供此属性，供电状态完全由设备驱动负责；与vin-supply的共享稳压器方式相区别 |
| `vin-supply` | `phandle` | 控制设备供电的稳压器引用，目标设备树节点必须使用稳压器兼容字符串。通过共享稳压器供电时应提供此属性，其供电状态取决于所有受电设备的请求状态。若同时提供supply-gpios，则必须先请求稳压器再将GPIO置为有效；释放稳压器前，必须先将GPIO置为无效 |

本页没有已弃用的节点专用属性。

## 12.2\_基础属性

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

译注：测量周期说明中的低功耗范围为80–320 ms，但同一段又称40 ms默认值同时适用于普通和低功耗模式，原文存在差异，未擅自统一。

来源链接状态（2026-10-16）：原文提供的VCNL36825T外部数据手册链接经重试仍返回HTTP 404；原始地址保留，Zephyr官方绑定正文已完整翻译。

## 12.3\_寄存器块命名原例

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

[上一章](P011_ti_tmp451.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P013_vishay_vcnl4040.md)
