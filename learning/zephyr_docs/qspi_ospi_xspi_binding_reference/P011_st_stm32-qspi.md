---
id: learning.zephyr-docs.qspi-ospi-xspi-binding-reference.page-11
title: st_stm32-qspi
kind: reference
status: maintained
domains: [zephyr, devicetree, qspi, ospi, xspi]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/qspi/st,stm32-qspi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第11章\_st_stm32-qspi

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/qspi/st,stm32-qspi.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="st-stm32-qspi"></a>
<a id="dtbinding-st-stm32-qspi"></a>
<a id="std-dtcompatible-st-stm32-qspi"></a>

兼容字符串（Compatible String）：`st,stm32-qspi`。厂商：[ STMicroelectronics ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-st)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=st,stm32-qspi)。

<a id="description"></a>

STM32 QSPI控制器。

<a id="examples"></a>

官方设备树配置原例：

```dts
&quadspi {
  pinctrl-0 = <&quadspi_clk_pe10 &quadspi_ncs_pe11
               &quadspi_bk1_io0_pe12 &quadspi_bk1_io1_pe13
               &quadspi_bk1_io2_pe14 &quadspi_bk1_io3_pe15>;

  dmas = <&dma1 5 5 0x0000 0x03>;
  dma-names = "tx_rx";

  status = "okay";
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 11.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | **必需**。第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-names` | `string-array` | **必需**。所提供状态的名称，名称数量必须与状态数量一致 |
| `ssht-enable` | `boolean` | 启用半周期采样移位（Sample Shifting）；建议在单传输速率（Single Transfer Rate，STR）模式启用，在双传输速率（Double Transfer Rate，DTR）模式禁用。 |
| `dual-flash` | `boolean` | 启用QSPI双闪存模式（Dual Flash Mode），使用两个外部四线SPI闪存FLASH 1与FLASH 2，每周期发送／接收8位，DDR模式下为16位，使吞吐率和容量均翻倍。为真时，`flash-id`不再有作用。 |
| `flash-id` | `int` | 闪存ID，用于选择正确的QSPI GPIO组，pinctrl中定义为`quadspi_bk[1/2]`。仅在未设置`dual-flash`时有效。下方保留选择ID 2的原例。 |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |

本页没有已弃用的节点专用属性。

## 11.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `interrupts` | `array` | **必需**。设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `dmas` | `phandle-array` | 可选DMA通道说明符。使用DMA时，依次提供DMA控制器节点引用（即使有DMAMUX也不能引用DMAMUX）、通道号、请求槽号、通道配置及特性；特性字段是否需要取决于DMA类型。<br>DMAMUX存在且启用时，通道仍为DMA通道，不是DMAMUX通道；请求由DMAMUX给出，无需特性字段。下方分别保留STM32L496使用DMA2通道7、请求3，以及STM32WB55通过DMAMUX使用DMA2通道0、请求20的QUADSPI例子，两者均无特性字段。 |
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
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的名称；通用说明称其为可选名称，是否必须填写以本层的必需标记为准 |
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

## DMA或闪存选择原例 6

```dts
   flash-id = <2>;
```

## DMA或闪存选择原例 14

```dts
   dma-names = "tx_rx";
```

## DMA与DMAMUX原例

STM32L496：DMA2通道7，请求3。

```dts
   /* select DMA2 channel 7 request 3 for QUADSPI */
   dmas = <&dma2 7 3 (STM32_DMA_PERIPH_TX | STM32_DMA_PRIORITY_HIGH)>;
```

STM32WB55：DMA2通道0，请求20。

```dts
   /* select DMA2 channel 0, request 20 for QUADSPI */
   dmas = <&dma2 0 20 (STM32_DMA_PERIPH_TX | STM32_DMA_PRIORITY_HIGH)>;
```

## 11.3\_寄存器块命名原例

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

[上一章](P010_renesas_rz-xspi.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P012_nxp_s32-xspi-sfp-frad.md)
