---
id: learning.zephyr-docs.memory-controller-sdram-psram-binding-reference.page-11
title: st_stm32-fmc-nor-psram
kind: reference
status: maintained
domains: [zephyr, devicetree, memory]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/memory-controllers/st,stm32-fmc-nor-psram.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第11章\_st_stm32-fmc-nor-psram

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/memory-controllers/st,stm32-fmc-nor-psram.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="st-stm32-fmc-nor-psram"></a>
<a id="dtbinding-st-stm32-fmc-nor-psram"></a>
<a id="std-dtcompatible-st-stm32-fmc-nor-psram"></a>

兼容字符串（Compatible String）：`st,stm32-fmc-nor-psram`。厂商：[ STMicroelectronics ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-st)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=st,stm32-fmc-nor-psram)。

驱动源码（Driver Source）：[drivers/memc/memc_stm32_nor_psram.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/memc_stm32_nor_psram.c)。

<a id="description"></a>

STM32灵活存储器控制器（Flexible Memory Controller，FMC）的NOR Flash／PSRAM／SRAM控制器。

FMC生成适当的信号时序，可驱动：8、16、32位异步SRAM及ROM；PSRAM（Cellular RAM，CRAM）的异步模式和同步访问突发模式，CRAM 1.5可配置跨页边界时分割突发访问，支持地址／数据复用或非复用；NOR Flash的异步及同步突发模式，同样支持复用或非复用。

每个存储组（Bank）使用独立片选信号NE，其余地址、数据和控制信号共享。通过可编程时序支持广泛器件，细节见参考手册。

FMC NOR／PSRAM控制器定义在FMC节点下，各存储组定义为该控制器的子节点。下方保留设备树启用原例，使用 `dt-bindings/memory-controller/stm32-fmc-nor-psram.h` 中定义的常量。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 11.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

## 11.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `#address-cells` | `int` | **必需**。子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`1` |
| `#size-cells` | `int` | **必需**。子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`0` |
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
| `reg` | `int` | **必需**。SRAM／NOR存储组（Bank）编号，用于选择设备连接的存储组，应为 `STM32_FMC_NORSRAM_BANKx` 的某个值。 |
| `st,control` | `array` | **必需**。SRAM／NOR Flash控制寄存器（FMC_BCRx），包含各存储组用于SRAM、PSRAM和NOR Flash的控制信息。字段依次为：MUXEN，地址／数据复用使能；MTYP，存储器类型；MWID，存储器数据总线宽度；BURSTEN，突发使能；WAITPOL，等待信号极性；WAITCFG，等待时序配置；WREN，写使能；WAITEN，等待使能；EXTMOD，扩展模式使能，设置后必须提供 `st,timing-ext`；ASYNCWAIT，异步传输期间的等待信号；CBURSTRW，写突发使能；CCLKEN，连续时钟使能；WFDIS，写FIFO禁用；CPSIZE，Cellular RAM 1.5页大小。 |
| `st,timing` | `array` | **必需**。SRAM／NOR Flash读取时序寄存器（FMC_BTRx）。若控制寄存器FMC_BCRx的EXTMOD置位，读写访问时序分开配置：此属性配置读访问，`st,timing-ext` 配置写访问。字段依次为：ADDSET，地址建立阶段，0～15个HCLK周期，不用于同步NOR Flash；ADDHLD，地址保持阶段，1～15个HCLK周期，不用于同步NOR Flash；DATAST，数据建立阶段，1～255个HCLK周期，用于SRAM、ROM及异步复用NOR Flash；BUSTURN，总线周转阶段，0～15个HCLK周期，仅用于复用NOR Flash；CLKDIV，FMC_CLK时钟分频比，输出CLK周期以HCLK周期数表示，范围2～16，不用于异步NOR Flash、SRAM或ROM访问；DATLAT，同步存储器数据延迟，表示取得首个数据前向存储器发出的存储器时钟周期数，CRAM必须为0，异步NOR／SRAM／ROM访问不关心该值，同步突发NOR Flash可取2～17；ACCMOD，访问模式（Access Mode），定义见 `dt-bindings/memory-controller/stm32-fmc-nor-psram.h`。 |
| `st,timing-ext` | `array` | SRAM／NOR Flash写入时序寄存器（FMC_BWTRx）。字段依次为：ADDSET，地址建立阶段，复位值15（0xF）；ADDHLD，地址保持阶段，复位值15（0xF）；DATAST，数据阶段，复位值255（0xFF）；BUSTURN，总线周转阶段，复位值15（0xF）；ACCMOD，访问模式，复位值0（0x0）。各字段详见 `st,timing`。仅当FMC_BCRx控制寄存器的EXTMOD置位时应用此属性；缺省时使用复位值。；默认值：`[0xf, 0xf, 0xff, 0xf, 0x0]` |
| `st,data-hold-cycles` | `int` | 读访问的数据保持阶段（Data-Hold Phase，DATAHLD）时长，以HCLK周期计。仅支持FMC_BTRx具有DATAHLD位的FMC控制器版本。；合法值：`0, 1, 2, 3` |
| `st,data-hold-cycles-ext` | `int` | 写访问的数据保持阶段（Data-Hold Phase，DATAHLD）时长，以HCLK周期计。仅支持FMC_BWTRx具有DATAHLD位的FMC控制器版本。；合法值：`0, 1, 2, 3` |

## STM32 FMC与存储器区域原例

```dts
&fmc {
  status = "okay";
  pinctrl-0 = <&fmc_nwe_pd5 &fmc_noe_pd4 ...>;
  pinctrl-names = "default";

  sram {
    status = "okay";
    compatible = "st,stm32-fmc-nor-psram";

    #address-cells = <1>;
    #size-cells = <0>;

    sram2@2 {
      reg = <0x2>;
      st,control = <STM32_FMC_DATA_ADDRESS_MUX_DISABLE
                    STM32_FMC_MEMORY_TYPE_SRAM
                    STM32_FMC_NORSRAM_MEM_BUS_WIDTH_16
                    STM32_FMC_BURST_ACCESS_MODE_DISABLE
                    STM32_FMC_WAIT_SIGNAL_POLARITY_LOW
                    STM32_FMC_WAIT_TIMING_BEFORE_WS
                    STM32_FMC_WRITE_OPERATION_ENABLE
                    STM32_FMC_WAIT_SIGNAL_DISABLE
                    STM32_FMC_EXTENDED_MODE_DISABLE
                    STM32_FMC_ASYNCHRONOUS_WAIT_DISABLE
                    STM32_FMC_WRITE_BURST_DISABLE
                    STM32_FMC_CONTINUOUS_CLOCK_SYNC_ONLY
                    STM32_FMC_WRITE_FIFO_DISABLE
                    STM32_FMC_PAGE_SIZE_NONE>;
      st,timing = <4 2 3 0 16 17 STM32_FMC_ACCESS_MODE_A>;
    };
  };
};
```

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

[上一章](P010_st_stm32-bbram.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P012_st_stm32-fmc-sdram.md)
