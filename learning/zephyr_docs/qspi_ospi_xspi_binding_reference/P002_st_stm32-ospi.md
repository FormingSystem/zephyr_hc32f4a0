---
id: learning.zephyr-docs.qspi-ospi-xspi-binding-reference.page-2
title: st_stm32-ospi
kind: reference
status: maintained
domains: [zephyr, devicetree, qspi, ospi, xspi]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/ospi/st,stm32-ospi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第2章\_st_stm32-ospi

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/ospi/st,stm32-ospi.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="st-stm32-ospi"></a>
<a id="dtbinding-st-stm32-ospi"></a>
<a id="std-dtcompatible-st-stm32-ospi"></a>

兼容字符串（Compatible String）：`st,stm32-ospi`。厂商：[ STMicroelectronics ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-st)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=st,stm32-ospi)。

<a id="description"></a>

STM32 OSPI控制器。

在开发板描述中启用STM32 octospi节点通常需要下方原例所示的引脚及DMA配置。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 2.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | **必需**。第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-names` | `string-array` | **必需**。所提供状态的名称，名称数量必须与状态数量一致 |
| `dlyb-bypass` | `boolean` | 启用延迟模块（Delay Block，DLYB）旁路。 |
| `ssht-enable` | `boolean` | 启用半周期采样移位（Sample Shifting）；建议在单传输速率（Single Transfer Rate，STR）模式启用，在双传输速率（Double Transfer Rate，DTR）模式禁用。 |
| `io-low-port` | `string` | 指定OCTOSPI I/O管理器用于IO[3:0]的端口。未提供时使用`IOPORT_<n>_LOW`，其中n是OSPI实例编号。可能需要启用管理器时钟，请查参考手册；可在设备树中启用该时钟。；合法值：`IOPORT_NONE, IOPORT_1_LOW, IOPORT_1_HIGH, IOPORT_2_LOW, IOPORT_2_HIGH` |
| `io-high-port` | `string` | 指定OCTOSPI I/O管理器用于IO[7:4]的端口。未提供时使用`IOPORT_<n>_HIGH`，其中n是OSPI实例编号。单线、双线、四线SPI可设为`IOPORT_NONE`。可能需要启用管理器时钟，请查参考手册；可在设备树中启用。；合法值：`IOPORT_NONE, IOPORT_1_LOW, IOPORT_1_HIGH, IOPORT_2_LOW, IOPORT_2_HIGH` |
| `clk-port` | `int` | 指定OCTOSPI I/O管理器用于clk引脚的端口。未提供时使用OSPI实例编号n。可能需要启用管理器时钟，请查参考手册；可在设备树中启用。；合法值：`1, 2` |
| `dqs-port` | `int` | 指定OCTOSPI I/O管理器用于数据选通（Data Strobe，DQS）引脚的端口。未提供时使用OSPI实例编号n；0表示不使用该信号。可能需要启用管理器时钟，请查参考手册；可在设备树中启用。；合法值：`0, 1, 2` |
| `ncs-port` | `int` | 指定OCTOSPI I/O管理器用于ncs引脚的端口。未提供时使用OSPI实例编号n。可能需要启用管理器时钟，请查参考手册；可在设备树中启用。；合法值：`1, 2` |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |

本页没有已弃用的节点专用属性。

## 2.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `interrupts` | `array` | **必需**。设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `clock-names` | `string-array` | **必需**。`clocks` 中各时钟提供者的名称；通用说明称其为可选名称，是否必须填写以本层的必需标记为准 |
| `dmas` | `phandle-array` | 可选的DMA通道说明符，执行DMA事务时必需。下方保留OSPI发送／接收的原例。各单元依次表示：`&dma1`为DMA控制器节点引用；5为通道号，范围0至最大通道数减1，STM32U5x为0至15；41为请求槽编号，可由DMA复用器（DMAMUX）给出；`0x10000`为通道配置，仅源／目的数据大小和优先级参与。<br>支持DMAMUX的系列应引用DMA节点，同时在DTS中启用DMAMUX节点。通道配置仅使用优先级及外设／存储器数据宽度位，两者宽度必须相同，0是有效配置值。该DMA外设不使用FIFO。原文重复列出的两个例子均保留。 |
| `dma-names` | `string-array` | DMA通道名称；使用DMA时应为`"tx_rx"`，下方保留原始配置。 |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节 |
| `dma-coherent` | `boolean` | 表示设备支持一致性 DMA 操作，见规范 v0.4 第 2.3.10 节 |
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

## STM32 OSPI节点原例

```dts
    &octospi {
        pinctrl-0 = <&octospi_clk_pe9 &octospi_ncs_pe10 &octospi_dqs_pe11
                     &octospi_io0_pe12 &octospi_io1_pe13
                     &octospi_io2_pe14 &octospi_io3_pe15
                     &octospi_io4_pe16 &octospi_io5_pe17
                     &octospi_io6_pe18 &octospi_io7_pe19>;

        dmas = <&dma1 5 41 0x10000>;
        dma-names = "tx_rx";

        status = "okay";
    };
```

## DMA或闪存选择原例 17

```dts
   dmas = <&dma1 5 41 0x10000>;
```

```dts
   dmas = <&dma1 5 41 0x10000>;
```

## DMA或闪存选择原例 18

```dts
   dma-names = "tx_rx";
```

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

[上一章](P001_renesas_ra-ospi-b.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_adi_max32-spixf.md)
