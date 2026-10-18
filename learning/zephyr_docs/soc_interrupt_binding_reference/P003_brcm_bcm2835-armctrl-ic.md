---
id: learning.zephyr-docs.soc-interrupt-binding-reference.page-3
title: brcm_bcm2835-armctrl-ic
kind: reference
status: maintained
domains: [zephyr, devicetree, interrupts, timer]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/interrupt-controller/brcm,bcm2835-armctrl-ic.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第3章\_brcm_bcm2835-armctrl-ic

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/interrupt-controller/brcm,bcm2835-armctrl-ic.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="brcm-bcm2835-armctrl-ic"></a>
<a id="dtbinding-brcm-bcm2835-armctrl-ic"></a>
<a id="std-dtcompatible-brcm-bcm2835-armctrl-ic"></a>

兼容字符串（Compatible String）：`brcm,bcm2835-armctrl-ic`。厂商：[ Broadcom ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-brcm)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=brcm,bcm2835-armctrl-ic)。

驱动源码（Driver Source）：[drivers/interrupt_controller/intc_bcm2835_armctrl.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/intc_bcm2835_armctrl.c)。

<a id="description"></a>

BCM2835 ARMC外设中断控制器，对应BCM283x系列（Pi 1、Pi 2、Pi 3及Pi Zero系列）的“GPU IRQ”一侧。它可作为子控制器挂接到BCM2836 ARM本地中断控制器，将64个GPU中断（PEND1与PEND2寄存器组）以及八个ARMC基本中断汇聚到父控制器的GPU级联中断线（Cascade Line）。

Zephyr把这些中断映射到偏移32的平坦编号空间（Flat IRQ Space）；第一级ARM本地控制器占用0至31，其中仅0至9被使用。ARMC编号映射如下：

| 平坦IRQ编号 | 寄存器组 | 对应位 |
| --- | --- | --- |
| 32至39 | 基本组（Basic Bank） | `IRQ_BASIC_PENDING` 的位0至7 |
| 64至95 | GPU PEND1 | `PEND1` 的位0至31 |
| 96至127 | GPU PEND2 | `PEND2` 的位0至31 |

符号常量见 `<zephyr/dt-bindings/interrupt-controller/bcm2835-armctrl.h>`。把上述编号解码到第0寄存器组快捷位（Bank-0 Shortcut Bits）以及PEND1／PEND2寄存器的逻辑，见仓库相对路径 `soc/brcm/bcm2710/soc_irq.c` 与 `drivers/interrupt_controller/intc_bcm2835_armctrl.c`。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 3.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `interrupt-controller` | `boolean` | **必需**。表示本节点是中断控制器（Interrupt Controller） |
| `#interrupt-cells` | `int` | **必需**。单元0为偏移32的ARMC平坦IRQ编号：32至39对应基本组，64至95对应PEND1，96至127对应PEND2。单元1为触发类型标志 `IRQ_TYPE_LEVEL`／`IRQ_TYPE_EDGE`。单元2为优先级（Priority），此控制器不使用它，但为与父 `brcm,bcm2836-l1-intc` 绑定保持一致，固定保留第三个单元；理由见父控制器文档；固定值：`3` |

本页没有已弃用的节点专用属性。

## 3.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `interrupts` | `array` | 父BCM2836 ARM本地中断控制器上的单个GPU级联IRQ。仅在级联配置（BCM2836／Pi 2及后续）中提供。BCM2835（Pi 1／Zero／Zero W）上的ARMC是根中断控制器，直接连接ARM核心IRQ线，没有父中断，因此省略本属性 |
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

## 3.3\_寄存器块命名原例

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

## 3.4\_说明符单元名称

中断说明符单元（Interrupt Specifier Cells）按原文顺序为：`irq`, `flags`, `priority`。

名称对照：`irq` 为中断请求编号；`flags` 为标志；`priority` 为优先级。

---

[上一章](P002_amd_acp-intc.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_brcm_bcm2836-l1-intc.md)
