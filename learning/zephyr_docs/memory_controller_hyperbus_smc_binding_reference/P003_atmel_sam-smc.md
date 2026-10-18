---
id: learning.zephyr-docs.memory-controller-hyperbus-smc-binding-reference.page-3
title: atmel_sam-smc
kind: reference
status: maintained
domains: [zephyr, devicetree, memory]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/memory-controllers/atmel,sam-smc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第3章\_atmel_sam-smc

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/memory-controllers/atmel,sam-smc.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="atmel-sam-smc"></a>
<a id="dtbinding-atmel-sam-smc"></a>
<a id="std-dtcompatible-atmel-sam-smc"></a>

兼容字符串（Compatible String）：`atmel,sam-smc`。厂商：[ Atmel Corporation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-atmel)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=atmel,sam-smc)。

驱动源码（Driver Source）：[drivers/memc/memc_sam_smc.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/memc_sam_smc.c)。

<a id="description"></a>

Atmel静态存储器控制器（Static Memory Controller，SMC）。

SMC可连接静态内存映射的外部设备，例如静态RAM（SRAM）、伪静态RAM（PSRAM）、可编程只读存储器（PROM）、可擦除PROM（EPROM）、电可擦PROM（EEPROM）、液晶模块（LCD Module）、NOR Flash与NAND Flash。SMC使用主时钟（Master Clock，MCK），由电源管理控制器（Power Management Controller，PMC）控制。

SMC控制器最多有4个子节点，用于定义所连接的外部存储器；`reg` 设置为设备的片选编号（Chip Select）。第一份设备树原例来自 `sam4_xplained` 开发板，采用控制器默认8位接口配置 `is66wv51216dbll-55` 低功耗静态RAM，NWE与NRD分别连接WE与OE输入。假定MCK为120MHz（CPU全速），每周期约8.33ns。按存储器规格，完整周期为55ns，因此 `atmel,smc-cycle-timing` 至少需要7周期，即约58.33ns。

完整周期由建立（Setup）、脉冲（Pulse）和保持（Hold）三部分组成：建立阶段寻址，脉冲阶段读写，保持阶段释放存储器。该器件至少需要5ns建立时间（1周期）、45ns CPU读写时间（6周期），无需保持时间。SMC没有独立保持参数，需要保持时间时，应在 `atmel,smc-cycle-timing` 中增加周期：无保持时 `7 = 1 + 6 + 0`；保持3周期时 `10 = 1 + 6 + 3`。

第二份原例配置连接到SAME70 SMC的16位 `CY62157EV30LL-45BVXI` SRAM。原例注释说明SAME70的MCK为300MHz，每周期约3.33ns，满足45ns访问时间至少需要14周期。最后，还必须在设备树中定义新的存储器设备，才能使内存可用；下方保留512KB SRAM区域原例。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 3.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | 第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-names` | `string-array` | 所提供状态的名称，名称数量必须与状态数量一致 |

本页没有已弃用的节点专用属性。

## 3.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `clocks` | `phandle-array` | **必需**。设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
| `#address-cells` | `int` | **必需**。子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`1` |
| `#size-cells` | `int` | **必需**。子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`0` |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts` | `array` | 设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的名称；通用说明称其为可选名称，是否必须填写以本层的必需标记为准 |
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

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `int` | **必需**。设备的SMC片选编号（Chip Select Number），有效范围0～3。 |
| `atmel,smc-write-mode` | `string` | **必需**。选择写操作使用片选信号（`ncs`）还是专用写使能引脚（`nwe`）。在该信号的脉冲与保持阶段，将数据置于总线上；NCS_WR或NWE建立时间之后，内部数据缓冲区切换到输出模式。；合法值：`ncs, nwe` |
| `atmel,smc-read-mode` | `string` | **必需**。选择读操作使用片选信号（`ncs`）还是专用输出使能引脚（`nrd`）。在该信号的脉冲与保持阶段，从总线读取数据。；合法值：`ncs, nrd` |
| `atmel,smc-setup-timing` | `array` | **必需**。用于建立内存区域访问，即设置地址。建立时间（Setup Timing）数组依次对应NWE、NCS_WR、NRD、NCS_RD信号，各值以MCK周期计。连续读写时，SMC允许值0，表示无延迟。各值采用6位编码，最高位增加128周期偏移；每项有效值为 `128 x setup[5] + setup[4:0]`。 |
| `atmel,smc-pulse-timing` | `array` | **必需**。用于实际读写内存区域的脉冲阶段（Pulse Phase）。数组依次对应NWE、NCS_WR、NRD、NCS_RD，各值以MCK周期计，禁止为0。各值采用7位编码，最高位增加256周期偏移；每项有效值为 `256 x pulse[6] + pulse[5:0]`。 |
| `atmel,smc-cycle-timing` | `array` | **必需**。SMC总写入时长和总读取时长的周期配置，描述完整读写时序：`cycle = setup + pulse + hold`。值必须大于或等于建立时间与脉冲时间之和。采用9位编码，最高两位对应256倍偏移；每项有效值为 `256 x cycle[8:7] + cycle[6:0]`。 |
| `atmel,smc-data-bus-width` | `int` | 所连接设备使用的外部数据总线宽度（External Data Bus Width）。；合法值：`8, 16` |
| `atmel,smc-byte-access-type` | `string` | 选择所连接设备处理字节访问周期（Byte-Access Cycles）的方式。；合法值：`byte-select, byte-write` |
| `atmel,smc-page-mode` | `boolean` | 当所连接设备支持时，启用页模式（Page Mode）。 |
| `atmel,smc-page-size` | `int` | 启用页模式时使用的页大小（Page Size），单位字节。；合法值：`4, 8, 16, 32` |

## SMC八位、十六位与存储器区域原例

```dts
&smc {
  status = "okay";
  pinctrl-0 = <&smc_default>;
  pinctrl-names = "default";

  is66wv51216dbll@0 {
    reg = <0>;

    atmel,smc-data-bus-width = <8>;
    atmel,smc-write-mode = "nwe";
    atmel,smc-read-mode = "nrd";
    atmel,smc-setup-timing = <1 1 1 1>;
    atmel,smc-pulse-timing = <6 6 6 6>;
    atmel,smc-cycle-timing = <7 7>;
  };
};
```

```dts
&smc {
  status = "okay";
  pinctrl-0 = <&smc_default>;
  pinctrl-names = "default";

  ext_sram_bus: ext-sram@0 {
    reg = <0>;

    atmel,smc-data-bus-width = <16>;
    atmel,smc-write-mode = "nwe";
    atmel,smc-read-mode = "nrd";
    atmel,smc-setup-timing = <1 1 1 1>;
    /*
     * MCK is 300 MHz on SAME70, so one cycle is approximately 3.33 ns.
     * 14 cycles is the minimum value that meets the 45 ns access time.
     */
    atmel,smc-pulse-timing = <14 14 14 14>;
    atmel,smc-cycle-timing = <15 15>;
    status = "okay";
  };
};
```

```dts
sram1: sram@60000000 {
    compatible = "zephyr,memory-region", "mmio-sram";
    device_type = "memory";
    reg = <0x60000000 DT_SIZE_K(512)>;
    zephyr,memory-region = "SRAM1";
};
```

## SMC建立、脉冲及保持时间原式

```text
  No Hold Time:
  cycle-timing (7) = setup (1) + pulse (6) + hold (0)

  With 3 Hold Times:
  cycle-timing (10) = setup (1) + pulse (6) + hold (3)
```

## SMC时序编码原式 41

```text
128 x setup[5] + setup[4:0]
```

## SMC时序编码原式 42

```text
256 x pulse[6] + pulse[5:0]
```

## SMC时序编码原式 43

```text
256 x cycle[8:7] + cycle[6:0]
```

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

[上一章](P002_adi_max32-hpb.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_bflb_bl61x-psram.md)
