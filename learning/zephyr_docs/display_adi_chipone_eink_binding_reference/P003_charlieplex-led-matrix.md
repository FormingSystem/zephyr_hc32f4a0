---
id: learning.zephyr-docs.display-adi-chipone-eink-binding-reference.page-3
title: charlieplex-led-matrix
kind: reference
status: maintained
domains: [zephyr, devicetree, display]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/charlieplex-led-matrix.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第3章\_charlieplex-led-matrix

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/charlieplex-led-matrix.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="charlieplex-led-matrix"></a>
<a id="dtbinding-charlieplex-led-matrix"></a>
<a id="std-dtcompatible-charlieplex-led-matrix"></a>

兼容字符串（Compatible String）：`charlieplex-led-matrix`。厂商：[ 无厂商前缀 ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-no-vendor)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=charlieplex-led-matrix)。

驱动源码（Driver Source）：[drivers/display/display_charlieplex_led_matrix.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/display_charlieplex_led_matrix.c)。

<a id="description"></a>

采用查理复用（Charlieplexing）GPIO驱动的单色／灰度LED矩阵（Monochrome/Grayscale LED Matrix）。

N根GPIO线最多可驱动 `N*(N-1)` 个LED。点亮某像素时，将一根线驱动为高电平、另一根为低电平，其余线保持高阻态（High Impedance），即输入／断开。定时器（计数器设备）的中断服务程序（Interrupt Service Routine，ISR）逐个扫描像素，扫描速度足够快时，视觉暂留（Persistence of Vision）使整个矩阵看起来同时点亮。灰度通过逐像素调节其在全部扫描周期中被驱动的比例产生。

帧缓冲区（Frame Buffer）按行优先（Row-Major）排列，像素索引为 `y * width + x`；`pixel-pairs` 属性把每个帧缓冲像素映射到能点亮它的那一对GPIO线。

<a id="examples"></a>

官方设备树配置原例：

```dts
/* 2x2 matrix on 3 charlieplexed lines */
/ {
    matrix: charlieplex-led-matrix {
        compatible = "charlieplex-led-matrix";
        gpios = <&gpioa 0 0>, <&gpioa 1 0>, <&gpioa 2 0>;
        counter = <&timer0>;
        refresh-frequency = <100>;
        width = <2>;
        height = <2>;
        grayscale-bits = <1>;
        /* (high << 8) | low, framebuffer order */
        /* pixel-pairs[0] = 0x0001 -> (0,0) lit by gpios[0] high, gpios[1] low */
        pixel-pairs = <0x0001 0x0100 0x0002 0x0200>;
    };
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 3.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `gpios` | `phandle-array` | **必需**。供 `pixel-pairs` 索引的查理复用GPIO线组。GPIO控制器必须支持将引脚配置为断开／高阻态（Disconnected/High-Impedance），这是标准Zephyr GPIO控制器的默认能力。每根线的极性标志，例如 `GPIO_ACTIVE_LOW`，会被忽略：驱动直接使用物理电平，一次扫描中同一根线可能根据所点亮的像素分别输出高、低电平，因此此处极性没有意义。应使用标志0，即 `GPIO_ACTIVE_HIGH`；误带极性标志也不会造成影响。 |
| `counter` | `phandle` | **必需**。用作扫描时基（Scan Time Source）的定时器实例（Timer Instance）。 |
| `refresh-frequency` | `int` | **必需**。整个矩阵的目标刷新率（Refresh Rate），单位为Hz，例如100。 |
| `pixel-pairs` | `array` | **必需**。每个像素对应一项，按帧缓冲区的行优先顺序排列，长度必须等于 `width * height`。每项以 `(high_index << 8) | low_index` 编码能点亮该像素的GPIO线对；两个索引都是 `gpios` 列表中的位置。将 `gpios[high_index]` 置高、`gpios[low_index]` 置低即可点亮像素。 |
| `grayscale-bits` | `int` | **必需**。每像素亮度位数（Brightness Bits）。1表示单色亮灭；更高值可获得 `2^bits` 级亮度，但会消耗刷新余量（Refresh Headroom）。；合法值：`1, 2, 3, 4` |
| `height` | `int` | **必需**。控制器所驱动面板的高度（Height），单位为像素。 |
| `width` | `int` | **必需**。控制器所驱动面板的宽度（Width），单位为像素。 |

本页没有已弃用的节点专用属性。

## 3.2\_基础属性

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

---

[上一章](P002_adi_adv7535.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_chipone_co5300-mipi-dsi.md)
