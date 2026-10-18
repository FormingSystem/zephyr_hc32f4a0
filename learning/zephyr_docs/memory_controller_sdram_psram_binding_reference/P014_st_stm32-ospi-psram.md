---
id: learning.zephyr-docs.memory-controller-sdram-psram-binding-reference.page-14
title: st_stm32-ospi-psram
kind: reference
status: maintained
domains: [zephyr, devicetree, memory]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/memory-controllers/st,stm32-ospi-psram.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第14章\_st_stm32-ospi-psram

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/memory-controllers/st,stm32-ospi-psram.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="st-stm32-ospi-psram"></a>
<a id="dtbinding-st-stm32-ospi-psram"></a>
<a id="std-dtcompatible-st-stm32-ospi-psram"></a>

兼容字符串（Compatible String）：`st,stm32-ospi-psram`。厂商：[ STMicroelectronics ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-st)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=st,stm32-ospi-psram)。

驱动源码（Driver Source）：[drivers/memc/memc_stm32_ospi_psram.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/memc_stm32_ospi_psram.c)。

<a id="description"></a>

STM32八线串行外设接口（Octal SPI，OSPI）PSRAM控制器。

通过OSPI外设提供微控制器与外部PSRAM的通信接口。PSRAM可配置为内存映射（Memory-Mapped），像内部设备一样读写。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 14.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `size` | `int` | **必需**。存储容量（Memory Size），单位位（Bit）。 |
| `max-frequency` | `int` | **必需**。设备OSPI接口的最大时钟频率（Maximum Clock Frequency），单位Hz。 |
| `fixed-latency` | `boolean` | 读取延迟（Read Latency）：设置时固定，未设置时可变。 |
| `drive-strength` | `int` | 驱动强度（Drive Strength）编码：0为全强度，1为一半，2为四分之一，3为八分之一。；默认值：`0`；合法值：`0, 1, 2, 3` |
| `read-latency` | `int` | 读取延迟编码（Read Latency Code）：0为LCx2 3／最高66MHz；1为LCx2 4／104MHz；2为LCx2 5／133MHz；3为LCx2 6／133MHz；4为LCx2 7／133MHz；5为LCx2 8／133MHz。；默认值：`5`；合法值：`0, 1, 2, 3, 4, 5` |
| `write-latency` | `int` | 写入延迟编码（Write Latency Code）：0为LC 3／最高66MHz；1为LC 4／104MHz；2为LC 5／133MHz；3为LC 6／133MHz；4为LC 7／133MHz；5为LC 8／133MHz。；默认值：`2`；合法值：`0, 1, 2, 3, 4, 5` |
| `adaptive-refresh-rate` | `int` | 0：快速刷新（Fast Refresh）；1：温度允许时启用慢速刷新（Slow Refresh）。；默认值：`0`；合法值：`0, 1` |
| `pasr` | `int` | 部分阵列自刷新（Partial Array Self-Refresh，PASR）覆盖范围：0为完整阵列；1为底部1/2；2为底部1/4；3为底部1/8；4为无；5为顶部1/2；6为顶部1/4；7为顶部1/8。；默认值：`0`；合法值：`0, 1, 2, 3, 4, 5, 6, 7` |
| `rbx` | `boolean` | 未启用时，读取保持在页（行）边界内；启用时，允许读取跨越页（行）边界。 |
| `burst-length` | `int` | 突发长度（Burst Length）：0为16字节／字回绕（Wrap）；1为32字节／字回绕；2为64字节／字回绕；3为1K字回绕。；默认值：`1`；合法值：`0, 1, 2, 3` |
| `burst-type-hybrid-wrap` | `boolean` | 未启用时，设备持续在 `burst-length` 指定的突发地址空间内回绕。启用时，设备先完成一次初始回绕长度的突发，再递增突发至最大列地址（1K），随后在整个列地址空间内回绕。 |
| `st,csbound` | `int` | 将事务限制在对齐地址边界内，对齐大小原文为`2^(csbound)`位（Bits）。`csbound`为0表示禁用。默认值为参考手册建议的最小值；建议根据PSRAM线性突发命令的突发回绕长度设置。；默认值：`3`；范围：`0 to 31` |
| `st,refresh` | `int` | **必需**。刷新率（Refresh Rate），以存储器时钟周期数表示。片选保持低电平的时间不得超过此值，因此该值实际限定事务（Transaction）的最大长度，应按存储器数据手册配置。0表示禁用此功能。 |

本页没有已弃用的节点专用属性。

## 14.2\_基础属性

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

## PSRAM编码原表 5

```text
- 0: LCx2 3 / Fmax 66 MHz
- 1: LCx2 4 / Fmax 104 MHz
- 2: LCx2 5 / Fmax 133 MHz
- 3: LCx2 6 / Fmax 133 MHz
- 4: LCx2 7 / Fmax 133 MHz
- 5: LCx2 8 / Fmax 133 MHz
```

## PSRAM编码原表 6

```text
- 0: LC 3 / Fmax 66 MHz
- 1: LC 4 / Fmax 104 MHz
- 2: LC 5 / Fmax 133 MHz
- 3: LC 6 / Fmax 133 MHz
- 4: LC 7 / Fmax 133 MHz
- 5: LC 8 / Fmax 133 MHz
```

## PSRAM编码原表 7

```text
- 0: Fast Refresh
- 1: Enables Slow Refresh when temperature allows
```

## PSRAM编码原表 8

```text
- 0: Full array
- 1: Bottom 1/2 array
- 2: Bottom 1/4 array
- 3: Bottom 1/8 array
- 4: None
- 5: Top 1/2 array
- 6: Top 1/4 array
- 7: Top 1/8 array
```

## PSRAM编码原表 10

```text
0: 16 Byte/Word Wrap
1: 32 Byte/Word Wrap
2: 64 Byte/Word Wrap
3: 1K Word Wrap
```

## 14.3\_寄存器块命名原例

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

[上一章](P013_st_stm32-fmc.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P015_st_stm32-xspi-psram.md)
