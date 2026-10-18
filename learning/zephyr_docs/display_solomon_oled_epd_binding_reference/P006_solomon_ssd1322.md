---
id: learning.zephyr-docs.display-solomon-oled-epd-binding-reference.page-6
title: solomon_ssd1322
kind: reference
status: maintained
domains: [zephyr, devicetree, display]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/solomon,ssd1322.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第6章\_solomon_ssd1322

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/solomon,ssd1322.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="solomon-ssd1322-on-mipi-dbi-bus"></a>
<a id="dtbinding-solomon-ssd1322"></a>
<a id="std-dtcompatible-solomon-ssd1322"></a>

兼容字符串（Compatible String）：`solomon,ssd1322`。厂商：[ Solomon Systech ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-solomon)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=solomon,ssd1322)。

驱动源码（Driver Source）：[drivers/display/ssd1322.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/ssd1322.c)。

<a id="description"></a>

Solomon SSD1322单色OLED显示控制器（Display Controller），最高分辨率为480×128。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 6.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `column-offset` | `int` | **必需**。第一个可见列的编号（First Visible Column）。数值含义不直观，可尝试对齐驱动显示示例来确定。 |
| `oscillator-freq` | `int` | **必需**。前级时钟分频（Front Clock Divider）位于位3:0，振荡器频率（Oscillator Frequency）位于位7:4，可设为 `0x0`。出现异常扫描线时，可提高振荡器频率并调整相位长度，例如设为 `0x90`；这会增加功耗。SSD1322可从 `0x91` 开始尝试。 |
| `precharge-voltage` | `int` | **必需**。设置预充电电压（Precharge Voltage），从0（`0.2 x VCC`）到 `0x1F`（`0.6x VCC`）。原文建议先尝试最高值，再逐步降低。 |
| `vcomh-voltage` | `int` | **必需**。设置COM非选中电压（COM Deselect Voltage），从0（`0.72 x VCC`）到 `0x7`（`0.86 x VCC`）。原文建议先尝试最高值，再逐步降低。 |
| `mux-ratio` | `int` | **必需**。COM引脚复用比（Multiplex Ratio），范围15～127，通常为 `height - 1`。 |
| `phase-length` | `int` | **必需**。段输出充电与放电的相位长度（Phase Length）：位7:4为充电，位3:0为放电。SSD1322可从 `0xE2` 开始尝试。 |
| `row-offset` | `int` | 用作第一行的COM引脚，映射到 `start-line` 指定的行。默认对应寄存器复位值（Reset Value）。；默认值：`0` |
| `start-line` | `int` | 显示RAM的起始行地址（Starting Line Address），范围0～127。默认对应寄存器复位值。；默认值：`0` |
| `precharge-period` | `int` | 第二预充电阶段（Second Precharge Period），从0（0个DCLK）到 `0xF`（15个DCLK），复位值为8。；默认值：`8` |
| `remap-row-first` | `boolean` | 将扫描方向设为垂直优先（Vertical First），交换行与列。 |
| `remap-columns` | `boolean` | 反转列顺序，即水平翻转（Horizontal Flip）。 |
| `remap-rows` | `boolean` | 反转行顺序，即垂直翻转（Vertical Flip）。 |
| `remap-nibble` | `boolean` | 反转每组4个半字节（Nibble）的顺序。 |
| `remap-com-odd-even-split` | `boolean` | COM引脚奇偶拆分（Odd/Even Split）。 |
| `remap-com-dual` | `boolean` | 双COM模式（Dual COM Mode）。 |
| `grayscale-enhancement` | `boolean` | 在部分显示器上启用灰阶增强（Grayscale Enhancement）；部分行为未公开文档。 |
| `inversion-on` | `boolean` | 开启显示颜色反转（Display Color Inverting）。 |
| `segments-per-pixel` | `int` | 将多个相邻段输出（Segment）映射到一个像素。某些显示器，例如Newhaven Display `NHD-2.7-12864WDW3`，将两个相邻像素驱动输出连接到同一物理像素；设为2时，驱动会重复每个像素。默认禁用，因为只适用于特定显示型号。；默认值：`1`；合法值：`1, 2` |
| `grayscale-enhancement-lg` | `boolean` | 启用低数值灰阶增强（Low-Value Grayscale Enhancement）。 |
| `external-vsl` | `boolean` | 使用外部VSL（External VSL）。 |
| `grayscale-table` | `uint8-array` | 包含15个元素的数组（Array），定义各亮度等级的伽马设置（Gamma Settings）；每项8位，范围0～180个DCLK。 |
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

## SPI枚举原始对照 22

```text
  0    SPI_FULL_DUPLEX
  2048 SPI_HALF_DUPLEX
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

[上一章](P005_solomon_ssd1320-mipi-dbi.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_solomon_ssd1325-i2c.md)
