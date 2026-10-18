---
id: learning.zephyr-docs.mtd-microchip-nordic-nxp-binding-reference.page-12
title: nordic_qspi-nor
kind: reference
status: maintained
domains: [zephyr, devicetree, flash]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/mtd/nordic,qspi-nor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第12章\_nordic_qspi-nor

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mtd/nordic,qspi-nor.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nordic-qspi-nor-on-qspi-bus"></a>
<a id="dtbinding-nordic-qspi-nor"></a>
<a id="std-dtcompatible-nordic-qspi-nor"></a>

兼容字符串（Compatible String）：`nordic,qspi-nor`。厂商：[ Nordic Semiconductor ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nordic)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nordic,qspi-nor)。

驱动源码（Driver Source）：[drivers/flash/nrf_qspi_nor.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/nrf_qspi_nor.c)。

<a id="description"></a>

支持JEDEC通用闪存接口（Common Flash Interface，CFI）的QSPI NOR闪存。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 12.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `jedec-id` | `uint8-array` | **必需**。JEDEC标识，依次为制造商标识（Manufacturer ID）、存储器类型（Memory Type）及存储密度（Memory Density）。 |
| `size` | `int` | 容量，单位位（bit）。此属性与 `size-in-bytes` 二选一，不可同时设置。 |
| `size-in-bytes` | `int` | 容量，单位字节（Byte）。此属性与 `size` 二选一，不可同时设置。 |
| `quad-enable-requirements` | `string` | JESD216 BFP第15个双字（DW15）中的四线使能要求（Quad Enable Requirements）值。<br>设备通过指令识别1-1-4及1-4-4模式时使用`NONE`。若四线使能位QE位于第一个状态寄存器字节的第6位，并可通过`RDSR`读一个字节、再以`WRSR`写一个字节来配置，则使用`S1B6`。其他字段含义见规范。；默认值：`S1B6`；合法值：`NONE, S2B1v1, S1B6, S2B7, S2B1v4, S2B1v5, S2B1v6` |
| `readoc` | `string` | 指定读取使用的数据线数量与操作码（Opcode）。未提供时选择 `fastread`。；合法值：`fastread, read2o, read2io, read4o, read4io` |
| `writeoc` | `string` | 指定写入使用的数据线数量与操作码（Opcode）。未提供时选择 `pp`。；合法值：`pp, pp2o, pp4o, pp4io` |
| `address-size-32` | `boolean` | 设置时使用32位寻址（32-bit Addressing）；未设置时使用24位寻址。 |
| `ppsize-512` | `boolean` | 设置时，写操作码作用于512字节页（Page）；未设置时作用于256字节页。 |
| `sck-delay` | `int` | 原文描述为CSn在能够再次变低之前必须保持有效的时钟周期数量，但指定单位为纳秒（ns）；原文的信号状态与单位措辞保留，见译注。；默认值：`0` |
| `rx-delay` | `int` | 从SPI时钟上升沿到采样串行输入数据之间的时钟周期数（Clock Cycles）。 |
| `cpha` | `boolean` | 设置时表示相位以有效半相位开始（CPHA=1）。此驱动要求设置该属性时同时设置 `cpol`。 |
| `cpol` | `boolean` | 设置时表示时钟前导边沿为下降沿（CPOL=1）。此驱动要求设置该属性时同时设置 `cpha`。 |
| `sck-frequency` | `int` | **必需**。设备支持的最大时钟速率（Maximum Clock Speed），单位为Hz。 |
| `requires-ulbpr` | `boolean` | 表示器件需要解锁块保护寄存器命令（Unlock Block Protection Register，ULBPR，0x98）。Microchip SST26VF系列等闪存的块保护寄存器（Block Protection Register，BPR）初始化为写保护；用此属性声明必须先解锁BPR，才能执行写入。 |
| `has-dpd` | `boolean` | 表示设备支持`0xB9`深度掉电（Deep Power-Down，DPD）命令，可将功耗降低至普通待机水平以下。使用此属性也意味着支持`0xAB`退出深度掉电（Release from Deep Power Down，RDPD）命令。某些芯片中该命令用于读取电子签名（Read Electronic Signature）；参见`t-enter-dpd`。 |
| `dpd-wakeup-sequence` | `array` | 为不使用RDPD命令的设备规定唤醒时间。某些设备，特别是Macronix MX25R，通过定时翻转CSn退出深度掉电。按顺序提供三段纳秒时间：①`tDPDD`，退出深度掉电延迟；②`tCDRP`，退出前CSn翻转时间；③`tRDP`，退出恢复时间。未提供本属性时，使用RDPD命令唤醒芯片。 |
| `t-enter-dpd` | `int` | 完成DPD命令的时间：发出DPD后，在芯片进入深度掉电之前，CSn必须持续保持无效的纳秒数。未提供时，驱动不强制延迟。 |
| `t-exit-dpd` | `int` | 完成RDPD命令的时间：发出RDPD后，在芯片退出深度掉电并可接收更多命令之前，CSn必须持续保持无效的纳秒数。未提供时，驱动不强制延迟。 |
| `t-reset-recovery` | `int` | 闪存复位后的最短恢复时间，单位为纳秒。GPIO复位、软件复位后执行此延迟；指定`supply-gpios`时，芯片上电后也执行。 |
| `has-lock` | `int` | 启动时应清除的状态寄存器位掩码（Status Register Bit Mask）。某些厂商的器件上电时设置块保护位，阻止所有擦除和编程操作，因此启动时必须清除这些位。但其他器件的状态寄存器可能包含不应清除的非易失位（Non-volatile Bits）。设置此属性时，其值明确标识初始化器件时应清除哪些位。 |
| `mxicy,mx25r-power-mode` | `string` | 选择超低功耗模式（Ultra Low Power Mode）或高性能模式（High Performance Mode），即L/H切换。高性能模式的写入和擦除更快，但功耗高于超低功耗模式。仅支持Macronix MX25R超低功耗系列。；合法值：`low-power, high-performance` |
| `use-4b-addr-opcodes` | `boolean` | 表示器件支持专用的4字节地址操作码（4-byte Address Opcodes）。器件通过专用操作码进行4字节寻址，而非切换到4字节地址模式。某些器件为读、写、擦除提供这种操作码；用此属性声明支持该方式。 |
| `use-flag-status-register` | `boolean` | 表示器件支持标志状态寄存器（Flag Status Register）。Micron及可能的其他器件用它提供更详细的编程或擦除状态。某些情况下，如果编程操作后不读取该寄存器，编程操作将不能正常工作。 |
| `use-fast-read` | `boolean` | 表示器件支持快速读取（Fast Read）。大多数SPI NOR器件提供快速读取命令，允许以高于标准读取命令的时钟速率输出数据。此属性声明支持地址阶段后带8个空周期（Dummy Cycles）的快速读取命令。 |
| `sfdp-bfp` | `uint8-array` | 包含JESD216串行闪存可发现参数（Serial Flash Discoverable Parameters，SFDP）的基本闪存参数（Basic Flash Parameters，BFP）表中的32位字，按小端字节序（Little-endian Byte Order）存放。在不希望运行时读取SFDP数据的情况下，用于提供特定闪存的配置。 |
| `sfdp-ff05` | `uint8-array` | 包含JESD216 SFDP xSPI Profile 1.0表的32位字，按小端字节序存放。 |
| `sfdp-ff84` | `uint8-array` | 包含JESD216 SFDP四字节地址指令参数表（4-byte Address Instruction Parameter Table）的32位字，按小端字节序存放。 |
| `enter-4byte-addr` | `int` | JESD216 BFP DW16中的进入四字节寻址（Enter 4-Byte Addressing）值。<br>配置为通过`sfdp-bfp`取得SFDP数据（`CONFIG_SPI_NOR_SFDP_DEVICETREE`），或运行时读取SFDP（`CONFIG_SPI_NOR_SFDP_RUNTIME`）时，本属性忽略。<br>在`CONFIG_SPI_NOR_SFDP_MINIMAL`配置下，本属性为DW16的31:24位构成的8位值，用来标示设备进入四字节寻址模式的方法。提供非零值时，驱动认为访问完整地址范围需要四字节寻址，并在初始化设备时自动切换到此模式。 |
| `page-size` | `int` | JESD216 BFP DW11规定的每页字节数。<br>仅在`CONFIG_SPI_NOR_SFDP_MINIMAL`配置下使用。通过`sfdp-bfp`提供SFDP（`CONFIG_SPI_NOR_SFDP_DEVICETREE`），或运行时从设备读取SFDP（`CONFIG_SPI_NOR_SFDP_RUNTIME`）时忽略。未指定时默认256字节。 |

本页没有已弃用的节点专用属性。

## 12.2\_基础属性

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

译注：`sck-delay` 原文同时使用“时钟周期数量”和“纳秒”，并写CSn有效后才能再次变低；译文保留该措辞，没有自行换算或改写信号极性。配置时应核对驱动与器件时序。

## 12.3\_寄存器块命名原例

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

[上一章](P011_nordic_owned-partitions.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P013_nordic_tz-nonsecure.md)
