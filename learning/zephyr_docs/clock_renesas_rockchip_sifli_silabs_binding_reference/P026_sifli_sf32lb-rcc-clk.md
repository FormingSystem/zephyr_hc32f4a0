---
id: learning.zephyr-docs.clock-renesas-rockchip-sifli-silabs-binding-reference.page-26
title: sifli_sf32lb-rcc-clk
kind: reference
status: maintained
domains: [zephyr, devicetree, clock]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/sifli,sf32lb-rcc-clk.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第26章\_sifli_sf32lb-rcc-clk

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/sifli,sf32lb-rcc-clk.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="sifli-sf32lb-rcc-clk"></a>
<a id="dtbinding-sifli-sf32lb-rcc-clk"></a>
<a id="std-dtcompatible-sifli-sf32lb-rcc-clk"></a>

兼容字符串（Compatible String）：`sifli,sf32lb-rcc-clk`。厂商：[ SiFli Technologies ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-sifli)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=sifli,sf32lb-rcc-clk)。

驱动源码（Driver Source）：[drivers/clock_control/clock_control_sf32lb_rcc.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/clock_control_sf32lb_rcc.c)。

<a id="description"></a>

SiFli复位与时钟控制器（Reset and Clock Controller，RCC）是负责全部SoC外设复位与时钟控制的多功能外设。此绑定描述时钟控制器部分，作为RCC节点的子节点使用，因为Zephyr不允许多个设备引用同一个设备树节点，例如时钟设备和复位设备。

外设使用标准clocks属性指定时钟，原始USART1示例见下方；单元编码RCC寄存器偏移和控制位位置。预定义RCC时钟单元见原文路径 `include/zephyr/dts-bindings/clock/sf32lb{xxx}-clocks.h`，其中{xxx}对应SoC系列，例如sf32lb52x。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 26.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `#clock-cells` | `int` | **必需**。时钟说明符（Clock Specifier）中预期的条目数量。；固定值：`1` |
| `sifli,cfg` | `phandle` | **必需**。指向SiFli SF32LB系统配置（System Configuration，HPSYS_CFG）的节点引用（Phandle）。 |
| `sifli,pmuc` | `phandle` | **必需**。SiFli SF32LB电源管理单元控制器（PMUC）节点。 |
| `sifli,hdiv` | `int` | **必需**。HCLK分频器（Divider），范围0～255，原式为 `fHCLK = clk_hpsys / HDIV`。 |
| `sifli,pdiv1` | `int` | **必需**。PCLK1分频器（Divider），范围0～7，原式为 `fPCLK1 = fHCLK / 2^PDIV1`。 |
| `sifli,pdiv2` | `int` | **必需**。PCLK2分频器（Divider），范围0～7，原式为 `fPCLK2 = fHCLK / 2^PDIV2`。 |
| `sifli,sys-clk-src` | `string` | HPSYS系统时钟源（System Clock Source）。选择dll1时必须启用DLL1子节点；省略时使用复位默认值hrc48。；默认值：`hrc48`；合法值：`hrc48, hxt48, lpclk, dll1` |
| `sifli,peri-clk-src` | `string` | HPSYS外设时钟域（Peripheral Clock Domain）的源；省略时使用复位默认值hxt48。；默认值：`hxt48`；合法值：`hrc48, hxt48` |
| `sifli,mpi1-clk-src` | `string` | MPI1／QSPI时钟树的源。选择dll1或dll2时必须启用对应DLL子节点；省略时使用复位默认值peri。；默认值：`peri`；合法值：`peri, dll1, dll2` |
| `sifli,mpi2-clk-src` | `string` | MPI2／QSPI时钟树的源。选择dll1或dll2时必须启用对应DLL子节点；省略时使用复位默认值peri。；默认值：`peri`；合法值：`peri, dll1, dll2` |
| `sifli,usb-clk-src` | `string` | USB全速控制器（USB Full-speed Controller）时钟源。选择dll2时必须启用DLL2子节点；省略时使用复位默认值sysclk。；默认值：`sysclk`；合法值：`sysclk, dll2` |
| `sifli,usb-div` | `int` | 对所选USB时钟源应用的分频器（Divider），分频后必须为60MHz。例如clk_dll2为240MHz时，分频值必须为4，也是复位默认值。；默认值：`4` |

本页没有已弃用的节点专用属性。

## 26.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `clocks` | `phandle-array` | **必需**。设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
| `clock-names` | `string-array` | **必需**。`clocks` 中各时钟提供者的名称；通用说明称其为可选名称，是否必须填写以本层的必需标记为准 |
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

## SiFli USART1时钟原例

```dts
  usart1: serial@xxx {
      ...
      /* cell encodes RCC register offset and control bit position */
      clocks = <&rcc_clk SF32LB52X_CLOCK_USART1>;
      ...
  }
```

译注：原文头文件路径写作 `dts-bindings`，此处保留；原例末尾未写分号，也原样保留。

## 26.3\_寄存器块命名原例

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

## 说明符单元名称

clock cells：`id`。依次为时钟或外设标识。

---

[上一章](P025_sifli_sf32lb-hxt48.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P027_silabs_hfxo.md)
