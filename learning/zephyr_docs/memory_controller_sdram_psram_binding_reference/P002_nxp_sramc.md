---
id: learning.zephyr-docs.memory-controller-sdram-psram-binding-reference.page-2
title: nxp_sramc
kind: reference
status: maintained
domains: [zephyr, devicetree, memory]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/memory-controllers/nxp,sramc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第2章\_nxp_sramc

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/memory-controllers/nxp,sramc.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-sramc"></a>
<a id="dtbinding-nxp-sramc"></a>
<a id="std-dtcompatible-nxp-sramc"></a>

兼容字符串（Compatible String）：`nxp,sramc`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,sramc)。

驱动源码（Driver Source）：[drivers/memc/memc_nxp_sramc.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/memc_nxp_sramc.c)。

<a id="description"></a>

NXP AHB SRAM控制器（SRAMC），用于外部异步并行SRAM或类SRAM FPGA接口。

SRAMCR0／SRAMCR1配置寄存器实际位于 `BLK_CTRL_WAKEUPMIX` 模块中。此节点通过 `nxp,blk-ctrl` 节点引用访问该模块，不使用自身的 `reg` 再次映射同一组寄存器；该模块已由 `nxp,imx-blkctrl-wakeup` 节点描述。

每个连接外部SRAM的片选（Chip Select，最多4个，每个最大128KB）用一个 `mmio-sram` 子节点描述，其 `reg` 为片选内存窗口，例如i.MX RT118x的CS0位于 `0x43880000`。下方保留完整原例。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 2.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `nxp,blk-ctrl` | `phandle` | **必需**。指向包含SRAMCR0和SRAMCR1配置寄存器的 `BLK_CTRL_WAKEUPMIX` 模块节点的引用。驱动从被引用节点取得控制器基地址（Base Address）。 |
| `turnaround-time` | `int` | 周转时间（Turnaround Time，TA），实际值为 `(TA+1) * granularity`。；默认值：`1`；范围：`0 to 15` |
| `address-hold-time` | `int` | 地址保持时间（Address Hold Time，AH），实际值为 `(AH+1) * granularity`。；默认值：`1`；范围：`0 to 15` |
| `address-setup-time` | `int` | 地址建立时间（Address Setup Time，AS），实际值为 `AS * granularity`。；默认值：`4`；范围：`0 to 15` |
| `ce-hold-time` | `int` | 片选使能保持时间（Chip-Enable Hold Time，CEH），实际值为 `CEH * granularity`。；默认值：`1`；范围：`0 to 15` |
| `ce-setup-time` | `int` | 片选使能建立时间（Chip-Enable Setup Time，CES），实际值为 `CES * granularity`。；默认值：`1`；范围：`0 to 15` |
| `adv-polarity` | `string` | ADV#信号极性（Signal Polarity）。；默认值：`active-low`；合法值：`active-low, active-high` |
| `address-mode` | `string` | SRAM地址模式（Address Mode）。；默认值：`admux`；合法值：`admux, non-admux` |
| `port-size` | `string` | **必需**。外部SRAM数据端口宽度（Data-Port Width），取决于开发板和器件，必须显式设置。若8位设备采用更宽的默认值，会以错误总线宽度驱动，因此不提供默认值。；合法值：`8-bit, 16-bit` |
| `bus-timeout-enable` | `boolean` | 启用AHB总线超时（Bus Timeout，BTOEN）。 |
| `bus-timeout-counter` | `int` | AHB总线超时等待周期（BTO），超时为 `BTO * 1024 hclk`。；默认值：`0`；范围：`0 to 255` |
| `prescaler` | `string` | 用于设置时序粒度（Timing Granularity）的预分频器（Prescaler）。；默认值：`prescaler-4`；合法值：`prescaler-1, prescaler-2, prescaler-3, prescaler-4` |
| `read-enable-high-time` | `int` | 读使能（OE#）高电平时间REH，实际值为 `(REH+1) * granularity`。；默认值：`9`；范围：`0 to 15` |
| `read-enable-low-time` | `int` | 读使能（OE#）低电平时间REL，实际值为 `(REL+1) * granularity`。；默认值：`16`；范围：`0 to 63` |
| `write-enable-high-time` | `int` | 写使能（WE#）高电平时间WEH，实际值为 `(WEH+1) * granularity`。；默认值：`10`；范围：`0 to 15` |
| `write-enable-low-time` | `int` | 写使能（WE#）低电平时间WEL，实际值为 `(WEL+1) * granularity`。；默认值：`31`；范围：`0 to 63` |
| `pinctrl-0` | `phandles` | 第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-names` | `string-array` | 所提供状态的名称，名称数量必须与状态数量一致 |

本页没有已弃用的节点专用属性。

## 2.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`1` |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节；固定值：`1` |
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

## AHB SRAM控制器与外部存储器原例

```dts
  sramc: sramc {
      compatible = "nxp,sramc";
      nxp,blk-ctrl = <&blkctrl_wakeup>;
      pinctrl-0 = <&pinmux_sramc>;
      pinctrl-names = "default";
      port-size = "16-bit";
      address-mode = "admux";
      #address-cells = <1>;
      #size-cells = <1>;
      status = "okay";

      ext_sram: sram@43880000 {
          compatible = "mmio-sram";
          reg = <0x43880000 DT_SIZE_K(128)>;
      };
  };
```

## 2.3\_寄存器块命名原例

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

[上一章](P001_nxp_imx-snvs-gpr.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_nxp_xspi-psram.md)
