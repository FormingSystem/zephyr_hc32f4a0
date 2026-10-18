---
id: learning.zephyr-docs.clock-nordic-nuvoton-nxp-binding-reference.page-9
title: nuvoton_npcx-pcc
kind: reference
status: maintained
domains: [zephyr, devicetree, clock]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/nuvoton,npcx-pcc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第9章\_nuvoton_npcx-pcc

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/nuvoton,npcx-pcc.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nuvoton-npcx-pcc"></a>
<a id="dtbinding-nuvoton-npcx-pcc"></a>
<a id="std-dtcompatible-nuvoton-npcx-pcc"></a>

兼容字符串（Compatible String）：`nuvoton,npcx-pcc`。厂商：[ Nuvoton Technology Corporation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nuvoton)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nuvoton,npcx-pcc)。

驱动源码（Driver Source）：[drivers/clock_control/clock_control_npcx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/clock_control_npcx.c)。

<a id="description"></a>

Nuvoton NPCX电源与时钟控制器（Power and Clock Controller，PCC）节点。除电源管理外，还配置振荡器倍频时钟（Oscillator Frequency Multiplier Clock，OFMCLK）。OFMCLK来自高频时钟发生器（High-Frequency Clock Generator，HFCG），为Cortex-M4内核和大多数NPCX硬件模块提供源时钟。下方保留在开发板DTS中配置OFMCLK及其派生时钟的原例。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 9.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `clock-frequency` | `int` | **必需**。HFCG输出时钟OFMCLK的默认频率，单位Hz。目前仅允许120000000（120MHz）、100000000（100MHz）、96000000（96MHz）、90000000（90MHz）、80000000（80MHz）、66000000（66MHz）、50000000（50MHz）、48000000（48MHz）。；合法值：`120000000, 100000000, 96000000, 90000000, 80000000, 66000000, 50000000, 48000000` |
| `core-prescaler` | `int` | **必需**。内核时钟预分频器（Core Clock Prescaler，FPRED），通过分频OFMCLK（MCLK）设置CORE_CLK，必须满足 `4MHz <= CORE_CLK <= 100MHz`。仅允许1～10：取1时CORE_CLK=OFMCLK；取2、3、4、5、6、7、8、9、10时分别为OFMCLK除以对应值。；合法值：`1, 2, 3, 4, 5, 6, 7, 8, 9, 10` |
| `apb1-prescaler` | `int` | **必需**。APB1预分频器（Prescaler），通过分频OFMCLK（MCLK）设置APB1_CLK。必须满足 `4MHz <= APB1_CLK <= 50MHz`，且APB1_CLK必须是CORE_CLK的整数分频（包括1分频）。仅允许1～10：取1时APB1_CLK=OFMCLK；取2、3、4、5、6、7、8、9、10时分别为OFMCLK除以对应值。；合法值：`1, 2, 3, 4, 5, 6, 7, 8, 9, 10` |
| `apb2-prescaler` | `int` | **必需**。APB2预分频器（Prescaler），通过分频OFMCLK（MCLK）设置APB2_CLK。必须满足 `8MHz <= APB2_CLK <= 50MHz`，且APB2_CLK必须是CORE_CLK的整数分频（包括1分频）。仅允许1～10：取1时APB2_CLK=OFMCLK；取2、3、4、5、6、7、8、9、10时分别为OFMCLK除以对应值。；合法值：`1, 2, 3, 4, 5, 6, 7, 8, 9, 10` |
| `apb3-prescaler` | `int` | **必需**。APB3预分频器（Prescaler），通过分频OFMCLK（MCLK）设置APB3_CLK。必须满足 `12.5MHz <= APB3_CLK <= 50MHz`，且APB3_CLK必须是CORE_CLK的整数分频（包括1分频）。仅允许1～10：取1时APB3_CLK=OFMCLK；取2、3、4、5、6、7、8、9、10时分别为OFMCLK除以对应值。；合法值：`1, 2, 3, 4, 5, 6, 7, 8, 9, 10` |
| `apb4-prescaler` | `int` | APB4预分频器（Prescaler），通过分频OFMCLK（MCLK）设置APB4_CLK。必须满足 `8MHz <= APB4_CLK <= 50MHz`，且APB4_CLK必须是CORE_CLK的整数分频（包括1分频）。仅允许1～10：取1时APB4_CLK=OFMCLK；取2、3、4、5、6、7、8、9、10时分别为OFMCLK除以对应值。；合法值：`1, 2, 3, 4, 5, 6, 7, 8, 9, 10` |
| `ram-pd-depth` | `int` | RAM块掉电控制寄存器（RAM Power-Down Control，RAM_PD）的有效位宽。RAM_PDn中的每一位设为1可关闭对应RAM块以降低功耗；有效位宽因NPCX系列而异。；合法值：`8, 12, 15` |
| `pwdwn-ctl-val` | `array` | **必需**。系统初始化时让模块掉电（Power-down，即关闭时钟），以降低功耗。 |
| `fast-clk-to-espi-sleep-support` | `boolean` | 芯片处于睡眠（Sleep）或深度睡眠（Deep Sleep）电源状态时，可保持eSPI_SIF模块的快速时钟FMCLK开启。仅在实现ENSLP_CTL寄存器ESPI_FMCLK_ENSLP字段的系列上设置，即NPCXn变体的SOC_SERIES_NPCX4及后续系列。 |
| `#clock-cells` | `int` | **必需**。时钟说明符（Clock Specifier）中预期的条目数量。 |

本页没有已弃用的节点专用属性。

## 9.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
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

## PCC时钟配置原例

```dts
&pcc {
    clock-frequency = <DT_FREQ_M(100)>; /* OFMCLK runs at 100MHz */
    core-prescaler = <5>; /* CORE_CLK runs at 20MHz */
    apb1-prescaler = <5>; /* APB1_CLK runs at 20MHz */
    apb2-prescaler = <5>; /* APB2_CLK runs at 20MHz */
    apb3-prescaler = <5>; /* APB3_CLK runs at 20MHz */
};
```

## 预分频器原始数值对照 2

```text
  1, CORE_CLK = OFMCLK
  2, CORE_CLK = OFMCLK / 2
  3, CORE_CLK = OFMCLK / 3
  4, CORE_CLK = OFMCLK / 4
  5, CORE_CLK = OFMCLK / 5
  6, CORE_CLK = OFMCLK / 6
  7, CORE_CLK = OFMCLK / 7
  8, CORE_CLK = OFMCLK / 8
  9, CORE_CLK = OFMCLK / 9
  10, CORE_CLK = OFMCLK / 10
```

## 预分频器原始数值对照 3

```text
  1, APB1_CLK = OFMCLK
  2, APB1_CLK = OFMCLK / 2
  3, APB1_CLK = OFMCLK / 3
  4, APB1_CLK = OFMCLK / 4
  5, APB1_CLK = OFMCLK / 5
  6, APB1_CLK = OFMCLK / 6
  7, APB1_CLK = OFMCLK / 7
  8, APB1_CLK = OFMCLK / 8
  9, APB1_CLK = OFMCLK / 9
  10, APB1_CLK = OFMCLK / 10
```

## 预分频器原始数值对照 4

```text
  1, APB2_CLK = OFMCLK
  2, APB2_CLK = OFMCLK / 2
  3, APB2_CLK = OFMCLK / 3
  4, APB2_CLK = OFMCLK / 4
  5, APB2_CLK = OFMCLK / 5
  6, APB2_CLK = OFMCLK / 6
  7, APB2_CLK = OFMCLK / 7
  8, APB2_CLK = OFMCLK / 8
  9, APB2_CLK = OFMCLK / 9
  10, APB2_CLK = OFMCLK / 10
```

## 预分频器原始数值对照 5

```text
  1, APB3_CLK = OFMCLK
  2, APB3_CLK = OFMCLK / 2
  3, APB3_CLK = OFMCLK / 3
  4, APB3_CLK = OFMCLK / 4
  5, APB3_CLK = OFMCLK / 5
  6, APB3_CLK = OFMCLK / 6
  7, APB3_CLK = OFMCLK / 7
  8, APB3_CLK = OFMCLK / 8
  9, APB3_CLK = OFMCLK / 9
  10, APB3_CLK = OFMCLK / 10
```

## 预分频器原始数值对照 6

```text
  1, APB4_CLK = OFMCLK
  2, APB4_CLK = OFMCLK / 2
  3, APB4_CLK = OFMCLK / 3
  4, APB4_CLK = OFMCLK / 4
  5, APB4_CLK = OFMCLK / 5
  6, APB4_CLK = OFMCLK / 6
  7, APB4_CLK = OFMCLK / 7
  8, APB4_CLK = OFMCLK / 8
  9, APB4_CLK = OFMCLK / 9
  10, APB4_CLK = OFMCLK / 10
```

## 9.3\_寄存器块命名原例

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

clock cells：`bus`, `ctl`, `bit`。依次为总线标识、控制项、位位置。

---

[上一章](P008_nuvoton_npcm-pcc.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_nuvoton_numaker-pcc.md)
