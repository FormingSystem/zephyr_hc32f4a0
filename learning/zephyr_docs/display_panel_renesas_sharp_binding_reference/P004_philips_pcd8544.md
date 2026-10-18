---
id: learning.zephyr-docs.display-panel-renesas-sharp-binding-reference.page-4
title: philips_pcd8544
kind: reference
status: maintained
domains: [zephyr, devicetree, display]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/philips,pcd8544.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第4章\_philips_pcd8544

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/philips,pcd8544.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="philips-pcd8544-on-mipi-dbi-bus"></a>
<a id="dtbinding-philips-pcd8544"></a>
<a id="std-dtcompatible-philips-pcd8544"></a>

兼容字符串（Compatible String）：`philips,pcd8544`。厂商：[ Philips ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-philips)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=philips,pcd8544)。

驱动源码（Driver Source）：[drivers/display/display_pcd8544.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/display_pcd8544.c)。

<a id="description"></a>

Philips PCD8544 LCD显示控制器（Display Controller），支持84×48像素的单色LCD，曾用于Nokia 5110手机。

译注：原文电压公式的常数项为3.06 V，但所列范围下限为3.00 V；此处分别保留，不擅自改写。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 4.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `bias` | `int` | 设置LCD偏置系统（Bias System）的 `BS2:BS0` 位，范围0～7，用于控制LCD偏置电压。详情参阅数据手册。 |
| `vop` | `int` | 设置LCD工作电压（Operating Voltage，VOP），对应“Set VOP”命令中的 `VOP6:VOP0` 位，数值范围0～127。原式为 `VLCD = 3.06 + (vop * 0.06) [V]`；原文给出的室温可编程电压范围为3.00～10.68 V。；默认值：`63` |
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

## PCD8544电压公式与原始范围

```text
VLCD = 3.06 + (vop * 0.06) [V], giving a program range of
3.00 to 10.68 V at room temperature.
```

## SPI枚举原始对照 3

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

[上一章](P003_zephyr_panel-timing.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_qemu_ramfb.md)
