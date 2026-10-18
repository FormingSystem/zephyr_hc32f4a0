---
id: learning.zephyr-docs.sensor-nxp-qdec-optical-binding-reference.page-6
title: nxp_mcux-eqdc
kind: reference
status: maintained
domains: [zephyr, devicetree, sensor]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/nxp,mcux-eqdc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第6章\_nxp_mcux-eqdc

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/sensor/nxp,mcux-eqdc.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-mcux-eqdc"></a>
<a id="dtbinding-nxp-mcux-eqdc"></a>
<a id="std-dtcompatible-nxp-mcux-eqdc"></a>

兼容字符串（Compatible String）：`nxp,mcux-eqdc`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,mcux-eqdc)。

驱动源码（Driver Source）：[drivers/sensor/nxp/eqdc_mcux/eqdc_mcux.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/eqdc_mcux/eqdc_mcux.c)。

<a id="description"></a>

NXP MCUX 增强型正交解码器（Enhanced Quadrature Decoder，EQDC）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 6.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `counts-per-revolution` | `int` | **必需**。完整旋转一圈（360 度）的编码器计数，用于将位置转换为角度。内部根据当前解码模式的计数倍数缩放，因此有效模数（Modulus）为 `counts-per-revolution * multiplier - 1`。默认正交 X4 模式的倍数为 4；单相模式（Single-phase Mode）的倍数为 1。 |
| `input-filter-count` | `int` | 输入滤波采样计数（Input Filter Sample Count）：输入滤波器接受信号跳变前，必须连续一致的采样次数。0x0 表示 3 次，0x7 表示 10 次。`FILT_CNT` 的值影响输入延迟（Input Latency）。；默认值：`0`；合法值：`0, 1, 2, 3, 4, 5, 6, 7` |
| `input-filter-period` | `int` | 输入滤波采样周期（Input Filter Sample Period），以 IPBus 时钟周期表示，决定对解码器输入信号重复采样的速率。设为 0x0（默认）时旁路输入滤波器。`FILT_PER` 的值影响输入延迟。；默认值：`0`；范围：`0 to 255` |
| `prescaler` | `int` | 预分频器（Prescaler）对外设时钟分频，该时钟用于 `LASTEDGE`、`POSDPER` 计数器、看门狗定时器和输入滤波器。分频系数为 `2^PRSC`：`prescaler = 0` 除以 1，`prescaler = 1` 除以 2，依此类推，`prescaler = 15` 除以 32768。；默认值：`0`；范围：`0 to 15` |
| `reverse-direction` | `boolean` | 选择计数方向与位置计数器初始值。`false` 正常计数，`true` 反向计数（Reverse Direction）。 |
| `single-phase-mode` | `boolean` | 旁路正交解码器，改用单相解码模式（Single-phase Decode Mode）。PHASEA 输入的跳变产生计数，PHASEB 与反向设置共同控制方向。每个脉冲只计一个边沿，没有 X4 正交倍频，因此 `counts-per-revolution` 是每圈原始脉冲数。不设置时默认采用标准正交 X4 解码。 |
| `revolution-count-mode` | `int` | 0：使用 INDEX 脉冲使圈数计数器（Revolution Counter）递增／递减。1：改用模数计数上溢或下溢事件（Roll-over / Roll-under），代替 INDEX 脉冲。；默认值：`1`；合法值：`0, 1` |
| `mux-states` | `phandle-array` | EQDC PHASEA／PHASEB 输入的 INPUTMUX 路由。每项格式为 `<&inputmuxN index connection>`：`&inputmuxN` 是提供路由的 INPUTMUX 控制器，`index` 是目标索引，`connection` 是 NXP 硬件抽象层（HAL）头文件 `fsl_inputmux_connections.h` 中的 `inputmux_connection_t` 值。<br><br>后文 MCXA153 原例通过 INPUTMUX0 将 TRIG_IN10 路由到 EQDC PHASEA，将 TRIG_IN5 路由到 EQDC PHASEB。 |
| `friendly-name` | `string` | 描述传感器的可读字符串，可帮助主机操作系统区分同型号的多个实例，例如笔记本电脑上盖与底座的加速度计。此属性定义于[HID Usage Tables规范](https://usb.org/sites/default/files/hut1_3_0.pdf)第22.5节“通用传感器属性用途”（Generic Sensor Property Usages）。 |
| `pinctrl-0` | `phandles` | 第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-names` | `string-array` | 所提供状态的名称，名称数量必须与状态数量一致 |
| `mux-controls` | `phandle-array` | 复用控制器说明符（MUX Controller Specifier）列表；每项先引用MUX控制器，再附上`#mux-control-cells`个寻址单元。 |
| `mux-control-names` | `string-array` | `mux-controls`中各条目的可选名称。 |
| `mux-state-names` | `string-array` | `mux-states`中各条目的可选名称。 |

本页没有已弃用的节点专用属性。

## 6.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `interrupts` | `array` | **必需**。设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
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

## EQDC INPUTMUX路由原例

说明符格式：

```dts
<&inputmuxN index connection>
```

MCXA153路由示例：

```dts
  mux-states = <&inputmux0 0 0x37000022>, /* TrigIn10ToQdc0Phasea */
               <&inputmux0 0 0x36c0001d>; /* TrigIn5ToQdc0Phaseb */
```

## 6.3\_寄存器块命名原例

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

[上一章](P005_nxp_lpadc-temp40.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_nxp_mcux-qdc.md)
