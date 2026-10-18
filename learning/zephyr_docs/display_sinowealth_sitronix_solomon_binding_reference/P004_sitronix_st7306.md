---
id: learning.zephyr-docs.display-sinowealth-sitronix-solomon-binding-reference.page-4
title: sitronix_st7306
kind: reference
status: maintained
domains: [zephyr, devicetree, display]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/sitronix,st7306.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第4章\_sitronix_st7306

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/sitronix,st7306.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="sitronix-st7306-on-mipi-dbi-bus"></a>
<a id="dtbinding-sitronix-st7306"></a>
<a id="std-dtcompatible-sitronix-st7306"></a>

兼容字符串（Compatible String）：`sitronix,st7306`。厂商：[ Sitronix ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-sitronix)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=sitronix,st7306)。

<a id="description"></a>

Sitronix ST7306多模式720×480显示控制器（Multi-Mode Display Controller）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 4.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `color-mode` | `string` | 显示器类型（Display Type）：`MONO` 为单色，每像素1位；`RBW` 为红、黑、白及关闭状态，每像素2位。暂不支持其他颜色模式。非单色显示器必须提供调色板（Palette）。；合法值：`MONO, RBW` |
| `mono-color` | `int` | 多色显示器在 `MONO` 模式下使用的颜色（Color）。红黑白显示器默认为黑色。；默认值：`3` |
| `start-line` | `int` | **必需**。显示RAM中待显示的起始行（Start Line），即第一个栅极输出。 |
| `start-column` | `int` | **必需**。显示RAM中待显示的起始列（Start Column），必须为12的倍数。 |
| `nvm-load` | `uint8-array` | **必需**。非易失性存储器加载设置（Non-Volatile Memory Load Settings），2字节。 |
| `gate-voltages` | `uint8-array` | **必需**。栅极电压（Gate Voltages），共2字节，各电压使用5位。 |
| `vsh` | `uint8-array` | **必需**。不同模式下的高正电压（High Positive Voltage），4字节。LCD的高、低电压会影响对比度。 |
| `vsl` | `uint8-array` | **必需**。不同模式下的低正电压（Low Positive Voltage），4字节。LCD的高、低电压会影响对比度。 |
| `vshn` | `uint8-array` | **必需**。不同模式下的高负电压（High Negative Voltage），4字节。LCD的高、低电压会影响对比度。 |
| `vsln` | `uint8-array` | **必需**。不同模式下的低负电压（Low Negative Voltage），4字节。LCD的高、低电压会影响对比度。 |
| `osc-settings` | `int` | **必需**。振荡器设置（Oscillator Settings），1字节：位7用于启用／禁用；位5与位2:1选择最高帧率，`000` 为51 Hz、`111` 为32 Hz；位6、位4:3和位0为0。原始位字段对照见后文。 |
| `framerate` | `int` | **必需**。帧率设置（Framerate Settings），1字节。位4控制高功率模式帧率：最高帧率编码为 `000` 时，0为25.5 Hz、1为51 Hz；否则0为16 Hz、1为32 Hz。位2:0控制低功率模式帧率：0、1、2、3、4、5分别对应0.25、0.5、1、2、4、8 Hz。原始位字段对照见后文。 |
| `multiplex-ratio` | `int` | **必需**。显示器使用的栅极线数参数（Gate Line Count）。原文将其描述为“栅极线数乘4”，同时给出的典型设置是 `y-size / 4`；两种表述在此保留。 |
| `source-voltage` | `int` | **必需**。源极电压选择（Source Voltage Selection），使用位1:0。`00` 选择 `VSHPA1/ VSLPA1/ VSHNA1/ VSLNA1`；`01` 选择第2组同名电压；`10` 选择第3组；`11` 选择第4组。完整原始标识符对照见后文。 |
| `remap-value` | `int` | **必需**。重映射存储器数据访问（Memory Data Access Remap）以翻转显示：位7翻转页地址顺序，位6翻转列地址顺序，位5交换页／列顺序，位3翻转数据输出顺序，位2翻转栅极扫描顺序。 |
| `panel-settings` | `int` | **必需**。设置面板和栅极布局（Panel/Gate Layout）。位7和位4为0；位6:5选择列点反转：`00` 为列反转，`01` 为1点反转，`10` 为2点反转。位3:2选择栅极扫描模式：`00` 为间隔2行，`01` 为间隔1行，`10` 为帧间隔。位1:0选择面板布局：`00` 为2行交错，`01` 为1行交错，`10` 为不交错。原文认为本驱动的列点反转很可能应设为1点反转（1-Dot Inversion）。 |
| `hpm-gate-waveform` | `uint8-array` | 高功率模式驱动LCD的波形（High-Power Waveform），共10字节：首字节为 `0xA5`（禁用）或 `0xE5`（启用）；第二字节为 `0xF6`；余下8字节中，位7和位3为0，位6:4为 `GPCHPUx`，位2:0为 `GPCHPUx+1`，详情参见数据手册。默认采用控制器默认值。；默认值：`[0xe5, 0xf6, 0x5, 0x46, 0x77, 0x77, 0x77, 0x77, 0x76, 0x45]` |
| `lpm-gate-waveform` | `uint8-array` | 低功率模式驱动LCD的波形（Low-Power Waveform），共8字节。每字节的位7和位3为0，位6:4为 `GPCLPUx`，位2:0为 `GPCLPUx+1`，详情参见数据手册。默认采用控制器默认值。；默认值：`[0x5, 0x46, 0x77, 0x77, 0x77, 0x77, 0x76, 0x45]` |
| `inversion-on` | `boolean` | 开启显示颜色反转（Display Color Inverting）。 |
| `low-power-mode` | `boolean` | 使用低功率模式（Low-Power Mode）代替高功率模式（High-Power Mode）。 |
| `duplex` | `int` | SPI双工模式（Duplex Mode），可为全双工或半双工。默认全双工，数值为0，这是最常见的模式。选择半双工可将SPI控制器的SDO用作双向数据线，通常用于只连接一根数据线的场景。应使用宏而非直接填写枚举数值：0对应 `SPI_FULL_DUPLEX`，2048对应 `SPI_HALF_DUPLEX`；参见 `dt-bindings/spi/spi.h`，原始对照保留在后文。；默认值：`0` |
| `mipi-cpol` | `boolean` | SPI时钟极性（Clock Polarity），指示时钟空闲状态；设置时空闲为逻辑高电平，否则为低电平 |
| `mipi-cpha` | `boolean` | SPI时钟相位（Clock Phase），决定采样边沿；设置时在第二个边沿采样，否则在第一个边沿采样 |
| `mipi-hold-cs` | `boolean` | 某些场景需由控制器通过软件管理SPI片选（Chip Select，CS），以连续执行多次SPI事务而不释放片选。典型情况为变长数据包：第一笔事务读取长度，第二笔读取该长度的字节数据 |
| `mipi-max-frequency` | `int` | 设备MIPI接口的最高时钟频率（Maximum Clock Frequency），单位为Hz。 |
| `mipi-mode` | `string` | 使用的MIPI DBI模式（Mode）。这些定义应与 `dt-bindings/mipi_dbi/mipi_dbi.h` 一致。；合法值：`MIPI_DBI_MODE_SPI_3WIRE, MIPI_DBI_MODE_SPI_4WIRE, MIPI_DBI_MODE_6800_BUS_16_BIT, MIPI_DBI_MODE_6800_BUS_9_BIT, MIPI_DBI_MODE_6800_BUS_8_BIT, MIPI_DBI_MODE_8080_BUS_16_BIT, MIPI_DBI_MODE_8080_BUS_9_BIT, MIPI_DBI_MODE_8080_BUS_8_BIT` |
| `color-coding` | `string` | MIPI DBI类型A或类型B，即6800／8080接口的颜色编码（Color Coding）。这些定义应与 `dt-bindings/mipi_dbi/mipi_dbi.h` 一致。；合法值：`MIPI_DBI_MODE_RGB332, MIPI_DBI_MODE_RGB444, MIPI_DBI_MODE_RGB565, MIPI_DBI_MODE_RGB666_1, MIPI_DBI_MODE_RGB666_2, MIPI_DBI_MODE_RGB888_1, MIPI_DBI_MODE_RGB888_2` |
| `te-mode` | `string` | MIPI DBI撕裂使能信号模式（Tearing Enable Signal Mode），默认禁用。；默认值：`MIPI_DBI_TE_NO_EDGE`；合法值：`MIPI_DBI_TE_NO_EDGE, MIPI_DBI_TE_RISING_EDGE, MIPI_DBI_TE_FALLING_EDGE` |
| `te-delay` | `int` | 检测到撕裂使能同步信号（Tearing Enable Synchronization Signal）后，发送显示数据前等待的延时，单位为微秒。多数控制器不需要延时，因此默认为0。；默认值：`0` |
| `supply-gpios` | `phandle-array` | 控制设备供电的GPIO说明符（Specifier）。设备有专用供电开关时提供此属性，供电状态完全由设备驱动负责；与vin-supply的共享稳压器方式相区别 |
| `vin-supply` | `phandle` | 控制设备供电的稳压器引用，目标设备树节点必须使用稳压器兼容字符串。通过共享稳压器供电时应提供此属性，其供电状态取决于所有受电设备的请求状态。若同时提供supply-gpios，则必须先请求稳压器再将GPIO置为有效；释放稳压器前，必须先将GPIO置为无效 |
| `height` | `int` | **必需**。控制器所驱动面板的高度（Height），单位为像素。 |
| `width` | `int` | **必需**。控制器所驱动面板的宽度（Width），单位为像素。 |

本页没有已弃用的节点专用属性。

## 4.2\_基础属性

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

## ST730x原始位字段与波形 11

```text
- [7]: enabled or disabled
- [5][2-1]: Max framerate: 000 = 51Hz, 111 = 32Hz
- [6][4-3][0]: 0
```

## ST730x原始位字段与波形 12

```text
- [4]: High power mode framerate, max framerate is 000, 0=25.5Hz, 1=51Hz, else 0=16Hz, 1=32Hz.
- [2-0]: Low power mode framerate, 0:0.25Hz, 1:0.5Hz, 2:1Hz, 3:2hz, 4:4Hz, 5:8Hz.
```

## ST730x原始位字段与波形 14

```text
- 00: VSHPA1/ VSLPA1/ VSHNA1/ VSLNA1
- 01: VSHPA2/ VSLPA2/ VSHNA2/ VSLNA2
- 10: VSHPA3/ VSLPA3/ VSHNA3/ VSLNA3
- 11: VSHPA4/ VSLPA4/ VSHNA4/ VSLNA4
```

## ST730x原始位字段与波形 15

```text
- [7]: Page address order flip
- [6]: Column address order flip
- [5]: Page/Column order flip
- [3]: Data output order flip
- [2]: Gate scan order flip
```

## ST730x原始位字段与波形 16

```text
- [7][4]: 0
- [6-5]: Column dot inversion: 00: Column inversion, 01: 1-Dot inversion, 10: 2-Dot inversion
- [3-2]: Gate scan mode: 00: 2 line interval, 01: 1 line interval, 10: frame interval
- [1-0]: Panel layout: 00: 2 line interlace, 01: 1 line interlace, 10: no interlacing
```

## ST730x原始位字段与波形 17

```text
- 1 byte: 0xA5 (disable) or 0xE5 (enable), tells if waveform is enabled or disabled
- 1 byte: 0xF6
- 8 bytes: [7][3]: 0, [6-4]: GPCHPUx, [2-0]: GPCHPUx+1. Please See datasheet.
```

## ST730x原始位字段与波形 18

```text
- 8 bytes: [7][3]: 0, [6-4]: GPCLPUx, [2-0]: GPCLPUx+1. Please See datasheet.
```

## SPI枚举原始对照 21

```text
  0    SPI_FULL_DUPLEX
  2048 SPI_HALF_DUPLEX
```

## 4.3\_寄存器块命名原例

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

[上一章](P003_sitronix_st7305.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_sitronix_st75256.md)
