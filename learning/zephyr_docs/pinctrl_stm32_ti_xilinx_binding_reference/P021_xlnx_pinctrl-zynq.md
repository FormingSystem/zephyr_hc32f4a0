---
id: learning.zephyr-docs.pinctrl-stm32-ti-xilinx-binding-reference.page-21
title: xlnx_pinctrl-zynq
kind: reference
status: maintained
domains: [zephyr, devicetree, pinctrl]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/xlnx,pinctrl-zynq.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第21章\_xlnx_pinctrl-zynq

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/xlnx,pinctrl-zynq.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="xlnx-pinctrl-zynq"></a>
<a id="dtbinding-xlnx-pinctrl-zynq"></a>
<a id="std-dtcompatible-xlnx-pinctrl-zynq"></a>

兼容字符串（Compatible String）：`xlnx,pinctrl-zynq`。厂商：[ Xilinx ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-xlnx)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=xlnx,pinctrl-zynq)。

驱动源码（Driver Source）：[drivers/pinctrl/pinctrl_xlnx_zynq.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pinctrl/pinctrl_xlnx_zynq.c)。

<a id="description"></a>

Xilinx Zynq-7000 SoC系列引脚控制节点（Pinctrl Node），按组定义引脚复用（Pin Multiplexing）和配置。Pinctrl节点中的每组定义一个外设的引脚复用与配置，每个子组定义该外设具有相同配置属性的引脚。可通过命名引脚组选择，例如 `groups = "uart1_10_grp"`；也可通过引脚名称选择，例如 `pins = "MIO49"`；还可组合两种方式。其余属性设置所选引脚的配置值。

后文保留UART1的原例：`mux` 为组 `uart1_10_grp` 选择 `uart1` 功能；`conf` 设置慢速边沿和LVCMOS18；`conf-rx` 将MIO49设为高阻态（High Impedance）；`conf-tx` 为MIO48禁用偏置。更多复用和配置选项见《Xilinx Zynq-7000 SoC技术参考手册》（Technical Reference Manual，UG585）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 21.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `syscon` | `phandle` | **必需**。指向系统级控制寄存器（System Level Control Registers，SLCR）的节点引用（Phandle）。 |

本页没有已弃用的节点专用属性。

## 21.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。系统级控制寄存器（System Level Control Registers，SLCR）空间的基址（Base Address）与大小。 |
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

<a id="grandchild-node-properties"></a>

## 孙节点属性（Grandchild Properties）

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `groups` | `string-array` | 指定此配置节点选择的引脚组（Pin Groups）列表。全部有效组名按原文逐项保留在后文的“Zynq有效引脚组原始列表”中。引脚组与 `pins` 指定的引脚名称合并，形成完整的所选引脚列表。 |
| `pins` | `string-array` | 指定此配置节点选择的引脚名称（Pin Names），有效范围为 `MIO0` 至 `MIO53`。这些名称与 `groups` 中的引脚组合并，形成完整的所选引脚列表。 |
| `function` | `string` | 为指定引脚组选择复用功能（Alternative Function），设置SLCR中的 `MIO_PIN_xx` 寄存器的 `L3_SEL`、`L2_SEL`、`L1_SEL` 和 `L0_SEL` 字段。；合法值：`ethernet0, ethernet1, mdio0, mdio1, qspi0, qspi1, qspi_fbclk, qspi_cs1, spi0, spi0_ss, spi1, spi1_ss, sdio0, sdio0_pc, sdio0_cd, sdio0_wp, sdio1, sdio1_pc, sdio1_cd, sdio1_wp, smc0_nor, smc0_nor_cs1, smc0_nor_addr25, smc0_nand, can0, can1, uart0, uart1, i2c0, i2c1, ttc0, ttc1, swdt0, gpio0, usb0, usb1` |
| `bias-disable` | `boolean` | 禁用I/O缓冲引脚的所有偏置（Bias），清除SLCR的 `MIO_PIN_xx` 寄存器中的 `PULLUP` 与 `TRI_ENABLE` 字段。 |
| `bias-high-impedance` | `boolean` | 为I/O缓冲引脚启用三态（Tri-state），设置SLCR的 `MIO_PIN_xx` 寄存器中的 `TRI_ENABLE` 字段。 |
| `bias-pull-up` | `boolean` | 为I/O缓冲引脚启用上拉（Pull-up），设置SLCR的 `MIO_PIN_xx` 寄存器中的 `PULLUP` 字段。 |
| `low-power-enable` | `boolean` | 仅作为输出使用时，禁用高速收发器逻辑（High-speed Transceiver Logic，HSTL）输入缓冲以节省功耗。适用于 `power-source`（`IO_Type`）为HSTL的情况；设置SLCR的 `MIO_PIN_xx` 寄存器中的 `DisableRcvr` 字段。 |
| `low-power-disable` | `boolean` | 启用HSTL输入缓冲（Input Buffer），适用于供电／I/O类型选择 `power-source`（`IO_Type`）为HSTL的情况；清除SLCR的 `MIO_PIN_xx` 寄存器中的 `DisableRcvr` 字段。 |
| `power-source` | `int` | I/O缓冲类型（I/O Buffer Type），设置SLCR的 `MIO_PIN_xx` 寄存器中的 `IO_Type` 字段。`IO_STANDARD_*` 宏定义于 `pinctrl-zynq.h`：1或 `IO_STANDARD_LVCMOS18`；2或 `IO_STANDARD_LVCMOS25`；3或 `IO_STANDARD_LVCMOS33`；4或 `IO_STANDARD_HSTL`。；合法值：`1, 2, 3, 4` |
| `slew-rate` | `int` | I/O缓冲的边沿速率（Edge Rate），适用于 `power-source`（`IO_type`）为LVCMOS18、LVCMOS25或LVCMOS33时。设置SLCR的 `MIO_PIN_xx` 寄存器中的 `Speed` 字段。`IO_SPEED_*` 宏定义于 `pinctrl-zynq.h`：0或 `IO_SPEED_SLOW` 表示慢速，1或 `IO_SPEED_FAST` 表示快速。；合法值：`0, 1` |

## Zynq UART1复用与电气配置原例

```dts
#include <zephyr/dt-bindings/pinctrl/pinctrl-zynq.h>

&pinctrl0 {
  pinctrl_uart1_default: uart1-default {
    mux {
      groups = "uart1_10_grp";
      function = "uart1";
    };

    conf {
      groups = "uart1_10_grp";
      slew-rate = <IO_SPEED_SLOW>;
      power-source = <IO_STANDARD_LVCMOS18>;
    };

    conf-rx {
      pins = "MIO49";
      bias-high-impedance;
    };

    conf-tx {
      pins = "MIO48";
      bias-disable;
    };
  };
};
```

## Zynq有效引脚组原始列表

```text
"ethernet0_0_grp", "ethernet1_0_grp", "mdio0_0_grp," "mdio1_0_grp",
"qspi0_0_grp", "qspi1_0_grp", "qspi_fbclk," "qspi_cs1_grp", "spi0_0_grp", "spi0_1_grp",
"spi0_2_grp," "spi0_0_ss0", "spi0_0_ss1", "spi0_0_ss2", "spi0_1_ss0," "spi0_1_ss1",
"spi0_1_ss2", "spi0_2_ss0", "spi0_2_ss1," "spi0_2_ss2", "spi1_0_grp", "spi1_1_grp",
"spi1_2_grp," "spi1_3_grp", "spi1_0_ss0", "spi1_0_ss1", "spi1_0_ss2," "spi1_1_ss0",
"spi1_1_ss1", "spi1_1_ss2", "spi1_2_ss0," "spi1_2_ss1", "spi1_2_ss2", "spi1_3_ss0",
"spi1_3_ss1," "spi1_3_ss2", "sdio0_0_grp", "sdio0_1_grp", "sdio0_2_grp," "sdio1_0_grp",
"sdio1_1_grp", "sdio1_2_grp", "sdio1_3_grp," "sdio0_emio_wp", "sdio0_emio_cd",
"sdio1_emio_wp," "sdio1_emio_cd", "smc0_nor", "smc0_nor_cs1_grp," "smc0_nor_addr25_grp",
"smc0_nand", "can0_0_grp", "can0_1_grp," "can0_2_grp", "can0_3_grp", "can0_4_grp",
"can0_5_grp," "can0_6_grp", "can0_7_grp", "can0_8_grp", "can0_9_grp," "can0_10_grp",
"can1_0_grp", "can1_1_grp", "can1_2_grp," "can1_3_grp", "can1_4_grp", "can1_5_grp",
"can1_6_grp," "can1_7_grp", "can1_8_grp", "can1_9_grp", "can1_10_grp," "can1_11_grp",
"uart0_0_grp", "uart0_1_grp", "uart0_2_grp," "uart0_3_grp", "uart0_4_grp", "uart0_5_grp",
"uart0_6_grp," "uart0_7_grp", "uart0_8_grp", "uart0_9_grp", "uart0_10_grp," "uart1_0_grp",
"uart1_1_grp", "uart1_2_grp", "uart1_3_grp," "uart1_4_grp", "uart1_5_grp", "uart1_6_grp",
"uart1_7_grp," "uart1_8_grp", "uart1_9_grp", "uart1_10_grp", "uart1_11_grp," "i2c0_0_grp",
"i2c0_1_grp", "i2c0_2_grp", "i2c0_3_grp," "i2c0_4_grp", "i2c0_5_grp", "i2c0_6_grp",
"i2c0_7_grp," "i2c0_8_grp", "i2c0_9_grp", "i2c0_10_grp", "i2c1_0_grp," "i2c1_1_grp",
"i2c1_2_grp", "i2c1_3_grp", "i2c1_4_grp," "i2c1_5_grp", "i2c1_6_grp", "i2c1_7_grp",
"i2c1_8_grp," "i2c1_9_grp", "i2c1_10_grp", "ttc0_0_grp", "ttc0_1_grp," "ttc0_2_grp",
"ttc1_0_grp", "ttc1_1_grp", "ttc1_2_grp," "swdt0_0_grp", "swdt0_1_grp", "swdt0_2_grp",
"swdt0_3_grp," "swdt0_4_grp", "gpio0_0_grp", "gpio0_1_grp", "gpio0_2_grp," "gpio0_3_grp",
"gpio0_4_grp", "gpio0_5_grp", "gpio0_6_grp," "gpio0_7_grp", "gpio0_8_grp", "gpio0_9_grp",
"gpio0_10_grp," "gpio0_11_grp", "gpio0_12_grp", "gpio0_13_grp", "gpio0_14_grp,"
"gpio0_15_grp", "gpio0_16_grp", "gpio0_17_grp", "gpio0_18_grp," "gpio0_19_grp",
"gpio0_20_grp", "gpio0_21_grp", "gpio0_22_grp," "gpio0_23_grp", "gpio0_24_grp",
"gpio0_25_grp", "gpio0_26_grp," "gpio0_27_grp", "gpio0_28_grp", "gpio0_29_grp",
"gpio0_30_grp," "gpio0_31_grp", "gpio0_32_grp", "gpio0_33_grp", "gpio0_34_grp,"
"gpio0_35_grp", "gpio0_36_grp", "gpio0_37_grp", "gpio0_38_grp," "gpio0_39_grp",
"gpio0_40_grp", "gpio0_41_grp", "gpio0_42_grp," "gpio0_43_grp", "gpio0_44_grp",
"gpio0_45_grp", "gpio0_46_grp," "gpio0_47_grp", "gpio0_48_grp", "gpio0_49_grp",
"gpio0_50_grp," "gpio0_51_grp", "gpio0_52_grp", "gpio0_53_grp", "usb0_0_grp," "usb1_0_grp"
```

译注：原文部分组名的逗号位于引号之内，以上列表逐字保留；使用时应核对有效组名。原文 `power-souce` 对应本页属性 `power-source`。

## 21.3\_寄存器块命名原例

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

[上一章](P020_wch_h41x-afio.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P022_xlnx_pinctrl-zynqmp.md)
