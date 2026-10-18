---
id: learning.zephyr-docs.mtd-atmel-bouffalo-binding-reference.page-23
title: is66wv-mspi
kind: reference
status: maintained
domains: [zephyr, devicetree, flash]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/mtd/is66wv-mspi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第23章\_is66wv-mspi

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mtd/is66wv-mspi.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="is66wv-on-mspi-bus"></a>
<a id="dtbinding-is66wv-mspi"></a>
<a id="std-dtcompatible-is66wv"></a>

兼容字符串（Compatible String）：`is66wv`。厂商：[ Generic or vendor-independent ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-no-vendor)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=is66wv)。

驱动源码（Driver Source）：[drivers/memc/memc_mspi_is66wv.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/memc_mspi_is66wv.c)。

<a id="description"></a>

MSPI总线上的ISSI IS66/67WV串行伪静态随机存取存储器（Serial PSRAM）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 23.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `mspi-max-frequency` | `int` | **必需**。为设备配置的最大时钟频率，单位为Hz；在设备树中通常表示初始化后的目标工作频率。 |
| `mspi-io-mode` | `string` | MSPI I/O模式设置，在设备树中通常表示初始化后的目标I/O模式。；合法值：`MSPI_IO_MODE_SINGLE, MSPI_IO_MODE_DUAL, MSPI_IO_MODE_DUAL_1_1_2, MSPI_IO_MODE_DUAL_1_2_2, MSPI_IO_MODE_QUAD, MSPI_IO_MODE_QUAD_1_1_4, MSPI_IO_MODE_QUAD_1_4_4, MSPI_IO_MODE_OCTAL, MSPI_IO_MODE_OCTAL_1_1_8, MSPI_IO_MODE_OCTAL_1_8_8, MSPI_IO_MODE_HEX, MSPI_IO_MODE_HEX_8_8_16, MSPI_IO_MODE_HEX_8_16_16` |
| `mspi-data-rate` | `string` | MSPI数据速率（Data Rate）设置，在设备树中通常表示初始化后的目标数据速率。；合法值：`MSPI_DATA_RATE_SINGLE, MSPI_DATA_RATE_S_S_D, MSPI_DATA_RATE_S_D_D, MSPI_DATA_RATE_DUAL` |
| `mspi-hardware-ce-num` | `int` | MSPI硬件CE编号。控制器可通过分配专用CE编号，在同一MSPI实例上原生支持多个外设。 |
| `mspi-cpp-mode` | `string` | MSPI时钟极性／相位设置：`MSPI_CPP_MODE_0`为CPOL=0、CPHA=0；`MSPI_CPP_MODE_1`为CPOL=0、CPHA=1；`MSPI_CPP_MODE_2`为CPOL=1、CPHA=0；`MSPI_CPP_MODE_3`为CPOL=1、CPHA=1。；合法值：`MSPI_CPP_MODE_0, MSPI_CPP_MODE_1, MSPI_CPP_MODE_2, MSPI_CPP_MODE_3` |
| `mspi-endian` | `string` | MSPI传输选择最高有效位优先（MSB First）或最低有效位优先（LSB First）。；合法值：`MSPI_LITTLE_ENDIAN, MSPI_BIG_ENDIAN` |
| `mspi-ce-polarity` | `string` | MSPI CE极性（Polarity），通常为低电平有效。；合法值：`MSPI_CE_ACTIVE_LOW, MSPI_CE_ACTIVE_HIGH` |
| `mspi-dqs-enable` | `boolean` | 对支持DQS的设备启用DQS模式。驱动会与`dqs-support`核对，若硬件支持则配置MSPI。 |
| `mspi-hold-ce` | `boolean` | 某些情况需要控制器通过软件管理MSPI芯片使能，使多个MSPI事务之间不释放CE。典型场景为变长数据包：第一次事务读取长度，第二次读取该长度的数据字节。 |
| `rx-dummy` | `int` | 接收（RX）方向地址阶段与数据阶段之间的数据或时钟周期数；0表示禁用RX空周期阶段（Dummy Phase）。 |
| `tx-dummy` | `int` | 发送（TX）方向地址阶段与数据阶段之间的数据或时钟周期数；0表示禁用TX空周期阶段。 |
| `read-command` | `int` | 接收方向要发送的读命令（Read Command）。 |
| `write-command` | `int` | 接收方向要发送的写命令（Write Command）。译注：原文此处明确写作RX，与“写命令”的通常方向不一致，此处保留该差异。 |
| `command-length` | `string` | 读命令与写命令的长度，单位为字节。；合法值：`INSTR_DISABLED, INSTR_1_BYTE, INSTR_2_BYTE` |
| `address-length` | `string` | 地址阶段发送的地址长度，单位为字节。；合法值：`ADDR_DISABLED, ADDR_1_BYTE, ADDR_2_BYTE, ADDR_3_BYTE, ADDR_4_BYTE` |
| `memmap-config` | `array` | 配置存储器映射（Memory Mapping）功能的参数数组。`enable`表示是否启用；`address_offset`为相对平台专用映射区域起点的字节偏移；`size`为要启用或禁用区域的字节大小；`permission`指定读写（RW）或只读（RO）权限。<br>支持此功能的控制器可将设备存储器映射到SoC系统地址空间，使其作为外部RAM并执行代码。下方保留默认关闭、偏移与大小及权限均为0的原始配置。 |
| `scramble-config` | `array` | 配置扰码（Scrambling）功能的参数数组。`enable`表示是否启用；`address_offset`是到起始地址的字节偏移，可相对平台映射区域起点或物理设备地址；`size`是要启用或禁用区域的字节大小。<br>支持硬件扰码的控制器可用此功能为外部设备保存的数据或代码增加保护。下方保留默认关闭、偏移与大小均为0的原始配置。 |
| `ce-break-config` | `array` | 配置自动CE中断（Auto CE Break）功能的参数数组。`mem_boundary`为单次传输不能跨越的设备存储边界，单位为字节；`time_to_break`为单次传输不应超过的最大时间，单位为微秒。<br>通常用于存在存储边界或要求周期性内部刷新的设备，例如伪静态RAM（Pseudo-static RAM，PSRAM）。下方保留两个字段均为0的原始默认配置。 |
| `supply-gpios` | `phandle-array` | 控制设备供电的GPIO说明符（Specifier）。设备有专用供电开关时提供此属性，供电状态完全由设备驱动负责；与vin-supply的共享稳压器方式相区别 |
| `vin-supply` | `phandle` | 控制设备供电的稳压器引用，目标设备树节点必须使用稳压器兼容字符串。通过共享稳压器供电时应提供此属性，其供电状态取决于所有受电设备的请求状态。若同时提供supply-gpios，则必须先请求稳压器再将GPIO置为有效；释放稳压器前，必须先将GPIO置为无效 |
| `jedec-id` | `uint8-array` | JEDEC标识，依次为制造商标识（Manufacturer ID）、存储器类型（Memory Type）及存储密度（Memory Density）。 |
| `size` | `int` | 闪存容量，单位为位（Bits）。 |
| `sfdp-bfp` | `uint8-array` | 包含JESD216串行闪存可发现参数（Serial Flash Discoverable Parameters，SFDP）的基本闪存参数（Basic Flash Parameters，BFP）表中的32位字，按小端字节序（Little-endian Byte Order）存放。在不希望运行时读取SFDP数据的情况下，用于提供特定闪存的配置。 |
| `sfdp-ff05` | `uint8-array` | 包含JESD216 SFDP xSPI Profile 1.0表的32位字，按小端字节序存放。 |
| `sfdp-ff84` | `uint8-array` | 包含JESD216 SFDP四字节地址指令参数表（4-byte Address Instruction Parameter Table）的32位字，按小端字节序存放。 |
| `quad-enable-requirements` | `string` | JESD216 BFP第15个双字（DW15）中的四线使能要求（Quad Enable Requirements）值。<br>设备通过指令识别1-1-4及1-4-4模式时使用`NONE`。若四线使能位QE位于第一个状态寄存器字节的第6位，并可通过`RDSR`读一个字节、再以`WRSR`写一个字节来配置，则使用`S1B6`。其他字段含义见规范。；合法值：`NONE, S2B1v1, S1B6, S2B7, S2B1v4, S2B1v5, S2B1v6` |
| `enter-4byte-addr` | `int` | JESD216 BFP DW16中的进入四字节寻址（Enter 4-Byte Addressing）值。<br>配置为通过`sfdp-bfp`取得SFDP数据（`CONFIG_SPI_NOR_SFDP_DEVICETREE`），或运行时读取SFDP（`CONFIG_SPI_NOR_SFDP_RUNTIME`）时，本属性忽略。<br>在`CONFIG_SPI_NOR_SFDP_MINIMAL`配置下，本属性为DW16的31:24位构成的8位值，用来标示设备进入四字节寻址模式的方法。提供非零值时，驱动认为访问完整地址范围需要四字节寻址，并在初始化设备时自动切换到此模式。 |
| `page-size` | `int` | JESD216 BFP DW11规定的每页字节数。<br>仅在`CONFIG_SPI_NOR_SFDP_MINIMAL`配置下使用。通过`sfdp-bfp`提供SFDP（`CONFIG_SPI_NOR_SFDP_DEVICETREE`），或运行时从设备读取SFDP（`CONFIG_SPI_NOR_SFDP_RUNTIME`）时忽略。未指定时默认256字节。 |

本页没有已弃用的节点专用属性。

## 23.2\_基础属性

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

## 23.3\_寄存器块命名原例

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

[上一章](P022_is25xX0xx-mspi.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P024_jedec_nor-mspi.md)
