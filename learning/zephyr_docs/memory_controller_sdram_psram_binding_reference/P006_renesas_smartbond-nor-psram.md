---
id: learning.zephyr-docs.memory-controller-sdram-psram-binding-reference.page-6
title: renesas_smartbond-nor-psram
kind: reference
status: maintained
domains: [zephyr, devicetree, memory]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/memory-controllers/renesas,smartbond-nor-psram.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第6章\_renesas_smartbond-nor-psram

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/memory-controllers/renesas,smartbond-nor-psram.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="renesas-smartbond-nor-psram"></a>
<a id="dtbinding-renesas-smartbond-nor-psram"></a>
<a id="std-dtcompatible-renesas-smartbond-nor-psram"></a>

兼容字符串（Compatible String）：`renesas,smartbond-nor-psram`。厂商：[ Renesas Electronics Corporation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-renesas)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=renesas,smartbond-nor-psram)。

驱动源码（Driver Source）：[drivers/memc/memc_smartbond_nor_psram.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/memc_smartbond_nor_psram.c)。

<a id="description"></a>

Renesas SmartBond™ NOR／PSRAM控制器（Controller）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 6.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `is-ram` | `boolean` | 存在此属性时，将存储器控制器配置为驱动PSRAM设备。 |
| `dev-size` | `int` | **必需**。存储器容量（Memory Size/Capacity），单位位（Bit）。 |
| `dev-type` | `int` | **必需**。设备类型（Device Type），是设备标识的一部分，用于核验所用存储器。 |
| `dev-density` | `int` | **必需**。设备密度（Device Density），是设备标识的一部分，用于核验所用存储器。位 `[7:0]` 应为密度值，位 `[15:8]` 应为应用于返回设备标识值的掩码（Mask），因为返回字节中的部分位可能无效。 |
| `dev-id` | `int` | **必需**。制造商标识（Manufacturer ID），是设备标识的一部分，用于核验所用存储器。 |
| `reset-delay-us` | `int` | **必需**。软件复位（SW Reset）之后，存储器能够接受下一条命令所需的时间，单位微秒。 |
| `read-cs-idle-min-ns` | `int` | **必需**。发送两条不同指令之间，片选（#CS）保持无效的最短时间，单位纳秒。 |
| `erase-cs-idle-min-ns` | `int` | 执行写使能、擦除、暂停擦除或恢复擦除指令后，片选（#CS）保持无效的最短时间，单位纳秒。存在 `is-ram` 属性时不使用此设置。 |
| `enter-qpi-cmd` | `int` | 存储器支持的进入四线外设接口模式（Quad Peripheral Interface，QPI）的命令，应以单线总线模式（Single Bus Mode）发送。 |
| `exit-qpi-cmd` | `int` | 存储器支持的退出QPI模式的命令，应以四线总线模式（Quad Bus Mode）发送。 |
| `enter-qpi-mode` | `boolean` | 存在此属性时，存储器进入QPI模式，通常所有字节均以四线总线模式发送。前提是 `read-cmd` 和 `write-cmd` 分别指定的读写命令与QPI模式匹配。 |
| `read-cmd` | `int` | 自动模式下单次／突发读取（Single/Burst Read）的命令。默认操作码（Opcode）使用所有存储器均支持的单线模式。；默认值：`0x3` |
| `write-cmd` | `int` | 自动模式下单次／突发写入（Single/Burst Write）的命令。默认操作码使用所有存储器均支持的单线模式。；默认值：`0x2` |
| `clock-mode` | `string` | 片选（#CS）空闲或无效时的时钟模式（Clock Mode）：Mode0在#CS无效时使#CLK为低；Mode3在#CS无效时使#CLK为高。默认Mode0，因为所有存储器都应支持。；默认值：`spi-mode0`；合法值：`spi-mode0, spi-mode3` |
| `addr-range` | `string` | 自动模式的地址长度（Address Size）。24位模式最多访问16MB；32位模式最多访问32MB，这是QSPICx支持的最大地址空间。默认24位模式，所有存储器均支持。；默认值：`addr-range-24bit`；合法值：`addr-range-24bit, addr-range-32bit` |
| `clock-div` | `int` | QSPIC2控制器的时钟分频器（Clock Divider）。此模块的时钟路径始终为DIV1，对应当前系统时钟。 |
| `tcem-max-us` | `int` | 设置非零值后，QSPIC2会考虑Tcem：当突发读写总时间超过该值时分割访问，代价是重新发送指令、地址及可能的空周期字节（Dummy Bytes）所需的额外周期。仅存在 `is-ram` 时有意义。此值表示突发读写期间#CS允许保持低电平的最长时间，单位微秒，用于满足支持自动刷新机制的器件要求。 |
| `dummy-bytes-count` | `string` | **必需**。自动模式下单次／突发读取需要发送的空周期字节（Dummy Bytes）数量。；合法值：`dummy-bytes-count0, dummy-bytes-count1, dummy-bytes-count2, dummy-bytes-count4` |
| `extra-byte-enable` | `boolean` | 存在此属性时，在空周期字节之后（若有）发送额外字节（Extra Byte）。当需要3个空周期字节时很有用；此时应将 `dummy-bytes-count` 设为2。 |
| `extra-byte` | `int` | 存在 `extra-byte-enable` 时要发送的额外字节（Extra Byte）。 |
| `rx-addr-mode` | `string` | 自动模式下单次／突发读取的地址阶段（Address Phase）所用SPI总线模式。默认单线模式，所有存储器均应支持。；默认值：`single-spi`；合法值：`single-spi, dual-spi, quad-spi` |
| `rx-inst-mode` | `string` | 自动模式下单次／突发读取的指令阶段（Instruction Phase）所用SPI总线模式。默认单线模式，所有存储器均应支持。；默认值：`single-spi`；合法值：`single-spi, dual-spi, quad-spi` |
| `rx-data-mode` | `string` | 自动模式下单次／突发读取的数据阶段（Data Phase）所用SPI总线模式。默认单线模式，所有存储器均应支持。；默认值：`single-spi`；合法值：`single-spi, dual-spi, quad-spi` |
| `rx-dummy-mode` | `string` | 自动模式下单次／突发读取的空周期字节阶段（Dummy Bytes Phase）所用SPI总线模式。所有存储器均应支持单线模式。；默认值：`single-spi`；合法值：`single-spi, dual-spi, quad-spi` |
| `rx-extra-mode` | `string` | 自动模式下单次／突发读取的额外字节阶段（Extra Byte Phase）所用SPI总线模式。默认单线模式，所有存储器均应支持。；合法值：`single-spi, dual-spi, quad-spi` |
| `tx-addr-mode` | `string` | 自动模式下单次／突发写入的地址阶段（Address Phase）所用SPI总线模式。默认单线模式，所有存储器均应支持。；默认值：`single-spi`；合法值：`single-spi, dual-spi, quad-spi` |
| `tx-inst-mode` | `string` | 自动模式下单次／突发写入的指令阶段（Instruction Phase）所用SPI总线模式。所有存储器均应支持单线模式。；默认值：`single-spi`；合法值：`single-spi, dual-spi, quad-spi` |
| `tx-data-mode` | `string` | 自动模式下单次／突发写入的数据阶段（Data Phase）所用SPI总线模式。默认单线模式，所有存储器均应支持。；默认值：`single-spi`；合法值：`single-spi, dual-spi, quad-spi` |

本页没有已弃用的节点专用属性。

## 6.2\_基础属性

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

[上一章](P005_renesas_ra-sdram.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_sifive_fu740-c000-ddr.md)
