---
id: learning.zephyr-docs.display-panel-renesas-sharp-binding-reference.page-11
title: renesas_ra-glcdc
kind: reference
status: maintained
domains: [zephyr, devicetree, display]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/renesas,ra-glcdc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第11章\_renesas_ra-glcdc

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/renesas,ra-glcdc.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="renesas-ra-glcdc"></a>
<a id="dtbinding-renesas-ra-glcdc"></a>
<a id="std-dtcompatible-renesas-ra-glcdc"></a>

兼容字符串（Compatible String）：`renesas,ra-glcdc`。厂商：[ Renesas Electronics ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-renesas)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=renesas,ra-glcdc)。

驱动源码（Driver Source）：[drivers/display/display_renesas_ra.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/display_renesas_ra.c)。

<a id="description"></a>

Renesas图形LCD控制器（Graphic LCD Controller，GLCDC）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 11.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | 为并行像素输出（Parallel Pixel Output）提供引脚配置（Pin Configuration）。与DSI主机组合时使用专用MIPI D-PHY引脚，因此不需要此引脚配置。 |
| `backlight-gpios` | `phandle-array` | 使 `BLn` 引脚有效可控制面板背光（Backlight）。器件将该信号视为高电平有效（Active-High）；原文称器件为传感器（Sensor）。 |
| `output-pin-hsync` | `string` | 选择并行LCD的水平同步（HSYNC）引脚。使用DSI显示器时不要选择。；合法值：`TCON_PIN_NONE, TCON_PIN_0, TCON_PIN_1, TCON_PIN_2, TCON_PIN_3` |
| `output-pin-vsync` | `string` | 选择并行LCD的垂直同步（VSYNC）引脚。使用DSI显示器时不要选择。；合法值：`TCON_PIN_NONE, TCON_PIN_0, TCON_PIN_1, TCON_PIN_2, TCON_PIN_3` |
| `output-pin-de` | `string` | 选择并行LCD的数据使能（DE）引脚。使用DSI显示器时不要选择。；合法值：`TCON_PIN_NONE, TCON_PIN_0, TCON_PIN_1, TCON_PIN_2, TCON_PIN_3` |
| `output-clock-divisor` | `int` | 选择GLCDC向面板输出的时钟分频比（Clock Frequency Division Ratio）。；合法值：`1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 16, 24, 32` |
| `output-endian` | `string` | 选择输出数据位序（Output Data Bit Order），默认小端（Little Endian）。；合法值：`LITTLE, BIG` |
| `output-color-oder` | `string` | 选择像素中的输出颜色顺序（Output Color Order），默认为RGB。；合法值：`RGB, GBR` |
| `output-data-signal-polarity` | `string` | 选择输出数据使能信号极性（Data Enable Signal Polarity），默认高电平有效。；合法值：`LOACTIVE, HIACTIVE` |
| `output-signal-sync-edge` | `string` | 选择输出信号同步边沿（Synchronization Edge），默认下降沿。；合法值：`FALLING, RISING` |
| `input-pixel-format` | `int` | **必需**。图形LCD控制器的初始输入像素格式（Initial Input Pixel Format）。 |
| `output-pixel-format` | `int` | **必需**。图形LCD控制器的初始输出像素格式（Initial Output Pixel Format）。 |
| `def-back-color-alpha` | `int` | 默认显示背景色的Alpha分量（Background Color Alpha）。 |
| `def-back-color-red` | `int` | 默认显示背景色的红色分量（Background Color Red）。 |
| `def-back-color-green` | `int` | 默认显示背景色的绿色分量（Background Color Green）。 |
| `def-back-color-blue` | `int` | 默认显示背景色的蓝色分量（Background Color Blue）。 |
| `ext-ram` | `phandle` | 存放帧缓冲区（Frame Buffer）的次级RAM（Secondary RAM）。未定义时，使用 `zephyr,sram` chosen节点指定的存储器。 |
| `height` | `int` | **必需**。控制器所驱动面板的高度（Height），单位为像素。 |
| `width` | `int` | **必需**。控制器所驱动面板的宽度（Width），单位为像素。 |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-names` | `string-array` | 所提供状态的名称，名称数量必须与状态数量一致 |

本页没有已弃用的节点专用属性。

## 11.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `clocks` | `phandle-array` | **必需**。设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
| `interrupts` | `array` | **必需**。设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | **必需**。各中断的名称（Interrupt Name）。 |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
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

[上一章](P010_raydium_rm692c9.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P012_renesas_rz-lcdc.md)
