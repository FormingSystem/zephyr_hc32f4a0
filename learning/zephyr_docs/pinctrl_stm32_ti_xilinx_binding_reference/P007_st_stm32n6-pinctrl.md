---
id: learning.zephyr-docs.pinctrl-stm32-ti-xilinx-binding-reference.page-7
title: st_stm32n6-pinctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, pinctrl]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/st,stm32n6-pinctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第7章\_st_stm32n6-pinctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/st,stm32n6-pinctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="st-stm32n6-pinctrl"></a>
<a id="dtbinding-st-stm32n6-pinctrl"></a>
<a id="std-dtcompatible-st-stm32n6-pinctrl"></a>

兼容字符串（Compatible String）：`st,stm32n6-pinctrl`。厂商：[ STMicroelectronics ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-st)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=st,stm32n6-pinctrl)。

<a id="description"></a>

带输入输出同步（I/O Synchronization）功能的STM32引脚控制器（Pin Controller）。它与兼容字符串为 `st,stm32-pinctrl` 的普通控制器相同，额外支持在信号输入或输出路径上添加可编程延迟（I/O Delay），并让GPIO数据与配置时钟边沿同步，即I/O重定时（I/O Retime）。该控制器见于STM32N6系列。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 7.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `remap-pa11` | `boolean` | 将PA11引脚重映射（Remap）为PA9引脚使用。仅限STM32G0和STM32C0片上系统（SoC）。 |
| `remap-pa12` | `boolean` | 将PA12引脚重映射（Remap）为PA10引脚使用。仅限STM32G0和STM32C0片上系统（SoC）。 |
| `remap-pa11-pa12` | `boolean` | 将PA11/PA12引脚重映射（Remap）为PA9/PA10引脚使用。仅限STM32F070x片上系统（SoC）。 |

本页没有已弃用的节点专用属性。

## 7.2\_基础属性

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

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `st,io-retime-edge` | `string` | 选择对输入／输出数据进行重定时（Retiming）的时钟边沿。存在此属性时启用I/O重定时，并选择在上升沿（Rising）、下降沿（Falling）或双边沿（Both）进行；省略此属性时禁用I/O重定时。；合法值：`rising, falling, both` |
| `st,io-delay-ps` | `int` | 应用于输入或输出路径的延迟（Delay），单位为皮秒（Picosecond，ps）。默认值与硬件默认值一致，使多数不使用I/O延迟功能的Pinctrl节点可以省略该属性。；默认值：`0`；合法值：`0, 300, 500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000, 3250` |
| `st,io-delay-path` | `string` | 应用I/O延迟的方向（Direction）。默认值与硬件默认值一致。；默认值：`output`；合法值：`output, input` |
| `pinmux` | `int` | **必需**。复用自[Linux STM32引脚绑定](https://github.com/torvalds/linux/blob/master/Documentation/devicetree/bindings/pinctrl/st,stm32-pinctrl.yaml)。一个整数同时表示GPIO引脚编号和复用设置，编码端口（Port）、端口内引脚（Line）与复用功能（Alternate Function）：<br><br>- `port`：GPIO端口索引，原文列为PA=0、PB=1、……、PK=11。<br>- `line`：端口内偏移，PA0=0、PA1=1、……、PA15=15。<br>- `function`：0至15分别表示复用功能0至15；16表示模拟（Analog）；17表示GPIO。<br><br>选择GPIO功能时，引脚静态配置为普通输入／输出GPIO，默认为输入。可在引脚配置中添加原文所写的 `ouptut-low` 或 `output-high` 属性，配置输出值。`include/zephyr/dt-bindings/pinctrl/stm32-pinctrl.h` 提供用于生成 `pinmux` 字段的宏以简化配置。后文保留三份原例：GPIO A9使用复用功能2、使用模拟功能，以及作为GPIO输出高电平。 |
| `slew-rate` | `string` | 引脚速度（Pin Speed），默认为低速 `low-speed`。少数引脚的硬件复位值可能不同，例如部分SoC上的PA11、PB3可能为超高速 `very-high-speed`；应仔细核对这些引脚的参考手册（Reference Manual）。；默认值：`low-speed`；合法值：`low-speed, medium-speed, high-speed, very-high-speed` |
| `bias-disable` | `boolean` | 禁用引脚的所有偏置（Bias）。 |
| `bias-pull-up` | `boolean` | 启用上拉电阻（Pull-Up Resistor）。 |
| `bias-pull-down` | `boolean` | 启用下拉电阻（Pull-Down Resistor）。 |
| `drive-push-pull` | `boolean` | 主动驱动高、低电平（Push-Pull）。 |
| `drive-open-drain` | `boolean` | 开漏驱动（Open Drain），实现硬件与（Hardware AND）。 |
| `output-low` | `boolean` | 将引脚设置为低电平输出模式（Output Low）。 |
| `output-high` | `boolean` | 将引脚设置为高电平输出模式（Output High）。 |

## STM32引脚复用与静态GPIO原例

```dts
... {
         pinmux = <STM32_PINMUX('A', 9, AF2)>;
};
```

```dts
... {
         pinmux = <STM32_PINMUX('A', 9, ANALOG)>;
};
```

```dts
... {
         pinmux = <STM32_PINMUX('A', 9, GPIO)>;
         output-high;
};
```

译注：原文端口索引列为PA=0至PK=11，并将 `output-low` 写作 `ouptut-low`；这里明确保留原文，实际使用应核对对应绑定头文件与属性名称。

## 7.3\_寄存器块命名原例

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

[上一章](P006_st_stm32h5-pinctrl.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P008_syna_sr100-pinctrl.md)
