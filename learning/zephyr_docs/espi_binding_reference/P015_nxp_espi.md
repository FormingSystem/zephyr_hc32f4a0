---
id: learning.zephyr-docs.espi-binding-reference.page-15
title: nxp_espi
kind: reference
status: maintained
domains: [zephyr, devicetree, espi]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/espi/nxp,espi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第15章\_nxp_espi

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/espi/nxp,espi.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-espi"></a>
<a id="dtbinding-nxp-espi"></a>
<a id="std-dtcompatible-nxp-espi"></a>

兼容字符串（Compatible String）：`nxp,espi`。厂商：[ NXP ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,espi)。

驱动源码（Driver Source）：[drivers/espi/espi_nxp.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/espi_nxp.c)。

<a id="description"></a>

NXP MCX A系列eSPI目标控制器。

此外设最多有5个可配置I/O端口。每个端口由一个子节点描述，其`reg`属性指定硬件端口索引0至4。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 15.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | **必需**。第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-names` | `string-array` | **必需**。所提供状态的名称，名称数量必须与状态数量一致 |
| `ram-base-addr` | `int` | **必需**。eSPI硬件用于邮箱（Mailbox）及带外（Out-of-Band，OOB）DMA缓冲区的SRAM基址；必须自然对齐（Naturally Aligned），且eSPI总线主控引擎（Bus-master Engine）可访问。 |
| `map-base0-addr` | `int` | 通过`PnADDR`寄存器选择BASE0寻址的端口所用的基址高16位，与端口`io-addr`组合成完整的主机侧地址。；默认值：`0` |
| `map-base1-addr` | `int` | 通过`PnADDR`寄存器选择BASE1寻址的端口所用的基址高16位，与端口`io-addr`组合成完整的主机侧地址。；默认值：`0` |
| `max-oob-payload-size` | `int` | 经`ESPICAP.OOBMX`能力字段向主机公布的OOB通道最大有效负载，单位为字节。它是能力上限，主机只能协商小于或等于它的值。默认值与硬件／HAL的复位能力一致。；默认值：`64`；合法值：`64, 128, 256` |
| `max-flash-payload-size` | `int` | 经`ESPICAP.FLASHMX`能力字段向主机公布的闪存通道最大有效负载，单位为字节。它是能力上限，主机只能协商小于或等于它的值。默认值与硬件／HAL的复位能力一致。；默认值：`64`；合法值：`64, 128, 256, 512` |
| `max-peripheral-payload-size` | `int` | 经`ESPICAP.MEMMX`能力字段向主机公布的外设通道最大有效负载，单位为字节。它是能力上限，主机只能协商小于或等于它的值。默认值与硬件／HAL的复位能力一致。；默认值：`64`；合法值：`64, 128, 256` |
| `max-taf-read-req-size` | `int` | 经`ESPICAP.TRGT_REQ_SIZE_SUPP`能力字段向主机公布的目标最大读请求大小，单位为字节。它是能力上限，主机只能协商小于或等于它的值。默认值与硬件／HAL的复位能力一致。；默认值：`64`；合法值：`64, 128, 256, 512, 1024, 2048, 4096` |
| `taf-erase-size` | `int` | 经`ESPICAP.SAFERA`能力字段向主机公布的目标附加闪存最小擦除扇区大小，单位为KB。默认值与硬件／HAL的复位能力一致。；默认值：`2`；合法值：`2, 4, 8, 16` |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |

本页没有已弃用的节点专用属性。

## 15.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `interrupts` | `array` | **必需**。设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `clocks` | `phandle-array` | **必需**。设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
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

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `int` | **必需**。硬件端口索引（Hardware Port Index）。驱动按声明顺序将子节点映射到对应索引的端口，因此从0到已使用的最高索引必须全部覆盖，不能有缺口。该范围内不需要有效功能的索引使用`port-type = <0x0>`占位。 |
| `port-type` | `int` | **必需**。端口功能类型（Port Function Type）。硬件端口槽号等于子节点在排序后子节点列表中的位置，因此0到最高活动端口的索引都必须存在。<br>0x0＝未配置（Unconfigured）；0x1＝ACPI端点（Endpoint）；0x2＝ACPI索引／数据（Index-Data）；0x4＝总线主控存储器（Bus Master Memory）；0x5＝总线主控闪存（Bus Master Flash）；0x8＝共享邮箱（Mailbox Shared）；0x9＝单邮箱（Mailbox Single）；0xA＝分离邮箱（Mailbox Split）；0xB＝OOB分离邮箱（Mailbox OOB Split）；0xC＝OEM邮箱（Mailbox OEM）。；合法值：`0x0, 0x1, 0x2, 0x4, 0x5, 0x8, 0x9, 0xa, 0xb, 0xc` |
| `io-addr` | `int` | 此端口的主机侧I/O地址偏移量。；默认值：`0` |
| `ram-offset` | `int` | 此端口DMA缓冲区相对于`ram-base-addr`的字节偏移量。；默认值：`0` |
| `ram-size` | `int` | 此端口DMA所用RAM缓冲区的字节大小。；默认值：`4`；合法值：`4, 8, 16, 32, 64, 128, 256, 512` |
| `idx-offset` | `int` | ACPI索引／数据端口的索引寄存器偏移量。；默认值：`0` |

## 15.3\_寄存器块命名原例

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

[上一章](P014_nxp_espi-taf.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P016_realtek_rts5912-espi.md)
