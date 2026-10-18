---
id: learning.zephyr-docs.pinctrl-adi-ambiq-arm-binding-reference.page-6
title: ambiq_apollo4-pinctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, pinctrl]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/ambiq,apollo4-pinctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第6章\_ambiq_apollo4-pinctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/ambiq,apollo4-pinctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="ambiq-apollo4-pinctrl"></a>
<a id="dtbinding-ambiq-apollo4-pinctrl"></a>
<a id="std-dtcompatible-ambiq-apollo4-pinctrl"></a>

兼容字符串（Compatible String）：`ambiq,apollo4-pinctrl`。厂商：[ Ambiq Micro, Inc. ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-ambiq)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=ambiq,apollo4-pinctrl)。

<a id="description"></a>

Ambiq Apollo4引脚控制器（Pin Controller）。

这是负责引脚功能选择和属性控制的单例节点（Singleton Node），例如把UART0 TX路由到引脚60并为它启用上拉电阻。SoC设备树中的节点标签为 `pinctrl`，可用下方 `&pinctrl` 原例修改。

所有设备引脚配置应放在 `pinctrl` 的子节点（Child Node）中。可在开发板目录的 `board-pinctrl.dtsi` 等文件中，或应用的设备树覆盖文件（Devicetree Overlay）中定义，并包含对应SoC变体的预定义组合头文件；下方原例使用 `zephyr/dt-bindings/pinctrl/ambiq-apollo4-pinctrl.h`。

`uart0_default` 子节点编码设备某个特定状态的引脚配置，此处为默认即活动状态（Default／Active State）。各子节点内按组（Group）组织配置；每个组在 `pinmux` 属性中指定引脚功能选择列表，也可设置所有组内引脚共享的属性。原例group1选择UART0TX_P60，group2选择UART0RX_P47并通过 `input-enable` 启用输入。全部原始代码和注释保留在下方。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 6.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

## 6.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
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

<a id="grandchild-node-properties"></a>

## 孙节点属性（Grandchild Properties）

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pinmux` | `array` | **必需**。共享相同组属性的引脚数组。每个元素是由引脚编号与其复用功能（Alternate Function）构造的整数。 |
| `drive-strength` | `string` | 引脚驱动强度相对于完整驱动强度的比例。默认值0.1，也是复位值（Reset Value）。；默认值：`0.1`；合法值：`0.1, 0.5, 0.75, 1.0` |
| `slew-rate` | `string` | 选择引脚压摆率（Slew Rate）。默认为慢速（Slow），也是复位值。；默认值：`slow`；合法值：`slow, fast` |
| `ambiq,pull-up-ohms` | `int` | 上拉电阻值（Pull-Up Resistance），默认1500Ω。；默认值：`1500`；合法值：`1500, 6000, 12000, 24000, 50000, 100000` |
| `ambiq,nce-src` | `int` | IOM nCE模块选择，选择SPI通道CE编号0～42。0～31依次对应IOM0～IOM7各自的NCE0～NCE3；32、33对应MSPI0的NCE0、NCE1；34、35对应MSPI1的NCE0、NCE1；36、37对应MSPI2的NCE0、NCE1；38为DC DPI DE模块，39为DISP CONT CSX模块，40为DC SPI CS_N模块，41为DC QSPI CS_N模块，42为DC模块RESX。完整原始枚举对照表保留在下方。若引脚不是CE，则忽略此描述项。默认值0，也是复位值。；默认值：`0` |
| `ambiq,nce-pol` | `int` | NCE极性选择（Polarity Select）：LOW = `0x0` 表示低电平有效（Active Low）；HIGH = `0x1` 表示高电平有效（Active High）。；默认值：`0` |
| `ambiq,sdif-cdwp` | `int` | 配置SD卡检测（Card Detection）与写保护（Write Protection）引脚：`0x0` 非SDIF引脚，`0x1` 为SDIFCD，`0x2` 为SDIFWP。；默认值：`0` |
| `bias-high-impedance` | `boolean` | 高阻抗模式（High Impedance），即三态或悬空（Third State／Floating）。 |
| `bias-pull-up` | `boolean` | 启用上拉电阻（Pull-Up Resistor）。 |
| `bias-pull-down` | `boolean` | 启用下拉电阻（Pull-Down Resistor）。 |
| `drive-push-pull` | `boolean` | 主动驱动高、低电平（Push-Pull）。 |
| `drive-open-drain` | `boolean` | 开漏驱动（Open Drain），实现硬件与（Hardware AND）。 |
| `input-enable` | `boolean` | 启用引脚输入，例如启用输入缓冲器（Input Buffer）；不影响输出。 |

## Ambiq UART引脚组配置原例

```dts
  &pinctrl {
          /* your modifications go here */
  };
```

```dts
  /* You can put this in places like a board-pinctrl.dtsi file in
   * your board directory, or a devicetree overlay in your application.
   */

  /* include pre-defined combinations for the SoC variant used by the board */
  #include <zephyr/dt-bindings/pinctrl/ambiq-apollo4-pinctrl.h>

  &pinctrl {
    uart0_default: uart0_default {
      group1 {
        pinmux = <UART0TX_P60>;
      };
      group2 {
        pinmux = <UART0RX_P47>;
        input-enable;
      };
    };
  };
```

## Apollo4 NCE模块原始对照

```text
  0,     IOM0CE0 : IOM 0 NCE 0 module
  1,     IOM0CE1 : IOM 0 NCE 1 module
  2,     IOM0CE2 : IOM 0 NCE 2 module
  3,     IOM0CE3 : IOM 0 NCE 3 module
  4,     IOM1CE0 : IOM 1 NCE 0 module
  5,     IOM1CE1 : IOM 1 NCE 1 module
  6,     IOM1CE2 : IOM 1 NCE 2 module
  7,     IOM1CE3 : IOM 1 NCE 3 module
  8,     IOM2CE0 : IOM 2 NCE 0 module
  9,     IOM2CE1 : IOM 2 NCE 1 module
  10,    IOM2CE2 : IOM 2 NCE 2 module
  11,    IOM2CE3 : IOM 2 NCE 3 module
  12,    IOM3CE0 : IOM 3 NCE 0 module
  13,    IOM3CE1 : IOM 3 NCE 1 module
  14,    IOM3CE2 : IOM 3 NCE 2 module
  15,    IOM3CE3 : IOM 3 NCE 3 module
  16,    IOM4CE0 : IOM 4 NCE 0 module
  17,    IOM4CE1 : IOM 4 NCE 1 module
  18,    IOM4CE2 : IOM 4 NCE 2 module
  19,    IOM4CE3 : IOM 4 NCE 3 module
  20,    IOM5CE0 : IOM 5 NCE 0 module
  21,    IOM5CE1 : IOM 5 NCE 1 module
  22,    IOM5CE2 : IOM 5 NCE 2 module
  23,    IOM5CE3 : IOM 5 NCE 3 module
  24,    IOM6CE0 : IOM 6 NCE 0 module
  25,    IOM6CE1 : IOM 6 NCE 1 module
  26,    IOM6CE2 : IOM 6 NCE 2 module
  27,    IOM6CE3 : IOM 6 NCE 3 module
  28,    IOM7CE0 : IOM 7 NCE 0 module
  29,    IOM7CE1 : IOM 7 NCE 1 module
  30,    IOM7CE2 : IOM 7 NCE 2 module
  31,    IOM7CE3 : IOM 7 NCE 3 module
  32,    MSPI0CEN0 : MSPI 0 NCE 0 module
  33,    MSPI0CEN1 : MSPI 0 NCE 1 module
  34,    MSPI1CEN0 : MSPI 1 NCE 0 module
  35,    MSPI1CEN1 : MSPI 1 NCE 1 module
  36,    MSPI2CEN0 : MSPI 2 NCE 0 module
  37,    MSPI2CEN1 : MSPI 2 NCE 1 module
  38,    DC_DPI_DE : DC DPI DE module
  39,    DISP_CONT_CSX : DISP CONT CSX module
  40,    DC_SPI_CS_N : DC SPI CS_N module
  41,    DC_QSPI_CS_N : DC QSPI CS_N module
  42,    DC_RESX : DC module RESX
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

[上一章](P005_ambiq_apollo3-pinctrl.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_ambiq_apollo5-pinctrl.md)
