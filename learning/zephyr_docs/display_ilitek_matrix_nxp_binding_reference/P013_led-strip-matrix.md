---
id: learning.zephyr-docs.display-ilitek-matrix-nxp-binding-reference.page-13
title: led-strip-matrix
kind: reference
status: maintained
domains: [zephyr, devicetree, display]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/led-strip-matrix.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第13章\_led-strip-matrix

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/led-strip-matrix.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="led-strip-matrix"></a>
<a id="dtbinding-led-strip-matrix"></a>
<a id="std-dtcompatible-led-strip-matrix"></a>

兼容字符串（Compatible String）：`led-strip-matrix`。厂商：[ 无厂商前缀 ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-no-vendor)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=led-strip-matrix)。

驱动源码（Driver Source）：[drivers/display/display_led_strip_matrix.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/display_led_strip_matrix.c)。

<a id="description"></a>

通用LED灯带矩阵（LED Strip Matrix），即将LED灯带排列成网格。

译注：底部起始模块布局原图的英文标题仍写“from the right”；原图保留，属性正文按原文“bottom to top”翻译。像素格式说明中的 `PANEL_PIXEL_FORMAT_RRGB_8888` 拼写也按原文保留。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 13.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `circulative` | `boolean` | 使用循环布局（Circulative Layout）：到达右边缘后，返回下一行左边缘继续。未设置时采用蛇形布局（Serpentine Layout），到达右边缘后折返向左。两种完整像素编号字符图见后文。 |
| `start-from-right` | `boolean` | 指定第一个LED位于右侧（Start from the Right）。后文保留从右侧开始的蛇形与循环布局编号图。 |
| `start-from-bottom` | `boolean` | 指定第一个LED位于底部（Start from the Bottom）。后文保留从底部开始的循环与蛇形布局编号图。 |
| `width` | `int` | **必需**。矩阵总宽度（Overall Width）。由多个模块组成时，为这些模块的宽度之和。 |
| `height` | `int` | **必需**。矩阵总高度（Overall Height）。由多个模块组成时，为这些模块的高度之和。 |
| `horizontal-modules` | `int` | 由多个模块组成时，指定水平方向模块数（Horizontal Modules），该数必须能整除宽度。未设置时控制单个矩阵。原例用两个蛇形布局模块组成8×4显示区域，完整编号图见后文。；默认值：`1` |
| `vertical-modules` | `int` | 由多个模块组成时，指定垂直方向模块数（Vertical Modules），该数必须能整除高度。未设置时控制单个矩阵。原例用两个蛇形布局模块组成4×8显示区域，完整编号图见后文。；默认值：`1` |
| `modules-circulative` | `boolean` | 指定构成矩阵的模块按循环顺序（Circulative Module Layout）排列。后文保留循环和蛇形模块编号图。 |
| `modules-start-from-right` | `boolean` | 指定模块从右向左排列（Right-to-Left Module Order）。后文保留从右侧开始的蛇形和循环模块编号图。 |
| `modules-start-from-bottom` | `boolean` | 指定模块从下向上排列（Bottom-to-Top Module Order）。后文保留对应的蛇形和循环模块编号图。 |
| `led-strips` | `phandles` | **必需**。指定构成矩阵的LED灯带（LED Strip）。若指定多条灯带，会将它们展平并依次连接；例如 `strip0` 和 `strip1` 各含128个LED时，`strip1` 的第一个LED视为第129个LED。随后依布局规则将这些LED逐个映射到坐标。LED总数必须等于 `width * height`。 |
| `chain-lengths` | `array` | 指定每条灯带的LED数量。所有灯带节点均含 `chain-length` 时可省略。各值必须为每模块LED数量 `[(width / horizontal-modules) * (height / vertical-modules)]` 的整数倍。 |
| `pixel-format` | `int` | 初始像素格式（Initial Pixel Format），列表见 `dt-bindings/display/panel.h`。原文说明仅接受 `PANEL_PIXEL_FORMAT_RGB_888` 和 `PANEL_PIXEL_FORMAT_RRGB_8888`；未设置时默认为 `PANEL_PIXEL_FORMAT_RGB_888`。；默认值：`1` |

本页没有已弃用的节点专用属性。

## 13.2\_基础属性

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

## LED矩阵布局原图 1

```text
* circulative layout
  [ 0][ 1][ 2][ 3]
  [ 4][ 5][ 6][ 7]
  [ 8][ 9][10][11]
  [12][13][14][15]
```

```text
* serpentine layout
  [ 0][ 1][ 2][ 3]
  [ 7][ 6][ 5][ 4]
  [ 8][ 9][10][11]
  [15][14][13][12]
```

## LED矩阵布局原图 2

```text
* Start from the right with a serpentine layout
  [ 3][ 2][ 1][ 0]
  [ 4][ 5][ 6][ 7]
  [11][10][ 9][ 8]
  [12][13][14][15]
```

```text
* Start from the right with a circulative layout
  [ 3][ 2][ 1][ 0]
  [ 7][ 6][ 5][ 4]
  [11][10][ 9][ 8]
  [15][14][13][12]
```

## LED矩阵布局原图 3

```text
* Start from the bottom with a circulative layout
  [12][13][14][15]
  [ 8][ 9][10][11]
  [ 4][ 5][ 6][ 7]
  [ 0][ 1][ 2][ 3]
```

```text
* Start from the bottom with a serpentine layout
  [15][14][13][12]
  [ 8][ 9][10][11]
  [ 7][ 6][ 5][ 4]
  [ 0][ 1][ 2][ 3]
```

## LED矩阵布局原图 6

```text
* 8x4 display with 2 serpentine layout modules
  [ 0][ 1][ 2][ 3]  [16][17][18][19]
  [ 7][ 6][ 5][ 4]  [23][22][21][20]
  [ 8][ 9][10][11]  [24][25][26][27]
  [15][14][13][12]  [31][30][29][28]
```

## LED矩阵布局原图 7

```text
* 4x8 display with 2 serpentine layout modules
  [ 0][ 1][ 2][ 3]
  [ 7][ 6][ 5][ 4]
  [ 8][ 9][10][11]
  [15][14][13][12]

  [16][17][18][19]
  [23][22][21][20]
  [24][25][26][27]
  [31][30][29][28]
```

## LED矩阵布局原图 8

```text
* circulative module layout
  [M0][M1][M2]
  [M3][M4][M5]
  [M6][M7][M8]
```

```text
* serpentine module layout
  [M0][M1][M2]
  [M5][M4][M3]
  [M6][M7][M8]
```

## LED矩阵布局原图 9

```text
* Start from the right with a module serpentine layout
  [M2][M1][M0]
  [M3][M4][M5]
  [M8][M7][M6]
```

```text
* Start from the right with a module circulative layout
  [M2][M1][M0]
  [M5][M4][M3]
  [M8][M7][M6]
```

## LED矩阵布局原图 10

```text
* Start from the right with a module serpentine layout
  [M6][M7][M8]
  [M5][M4][M3]
  [M0][M1][M2]
```

```text
* Start from the right with a module circulative layout
  [M6][M7][M8]
  [M3][M4][M5]
  [M0][M1][M2]
```

## 13.3\_寄存器块命名原例

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

[上一章](P012_jdi_lpm013m126.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_levetop_lt7680.md)
