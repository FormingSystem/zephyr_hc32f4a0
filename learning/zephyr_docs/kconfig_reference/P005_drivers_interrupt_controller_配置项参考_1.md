---
id: learning.zephyr-docs.kconfig-reference.page-5
title: "`drivers/interrupt_controller`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第5章\_`drivers/interrupt_controller`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `drivers/interrupt_controller` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_1ST_LEVEL_INTERRUPT_BITS"></a>

## 5.1 `CONFIG_1ST_LEVEL_INTERRUPT_BITS`

**提示（Prompt）**：第一级中断位总数（First-level Interrupt Bits）

**说明（Help）**

32 位中断掩码（Interrupt Mask）中用于第一级中断的位数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_2ND_LEVEL_INTERRUPTS"></a>

## 5.2 `CONFIG_2ND_LEVEL_INTERRUPTS`

**提示（Prompt）**：第二级中断支持（Second-level Interrupt Support）

**说明（Help）**

第二级中断（Second-level Interrupt）用于增加系统可寻址的中断数量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTI_LEVEL_INTERRUPTS
```

**被选择（Selected by）**

```text
CONFIG_INFINEON_INTC_SYSINTC
CONFIG_PLIC
CONFIG_RISCV_AIA
CONFIG_THEJAS32_INTC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)、[`CONFIG_INFINEON_INTC_SYSINTC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_INFINEON_INTC_SYSINTC)、[`CONFIG_PLIC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC)、[`CONFIG_RISCV_AIA`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RISCV_AIA)、[`CONFIG_THEJAS32_INTC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_THEJAS32_INTC)。

<a id="CONFIG_2ND_LEVEL_INTERRUPT_BITS"></a>

## 5.3 `CONFIG_2ND_LEVEL_INTERRUPT_BITS`

**提示（Prompt）**：第二级中断位总数（Second-level Interrupt Bits）

**说明（Help）**

32 位中断掩码（Interrupt Mask）中用于第二级中断的位数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[0, 31]
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_2ND_LVL_INTR_00_OFFSET"></a>

## 5.4 `CONFIG_2ND_LVL_INTR_00_OFFSET`

**提示（Prompt）**：第二级聚合器 0 的第一级 IRQ 线（IRQ Line）

**说明（Help）**

这是第 `$(cur-level-num)` 级中断聚合器（Interrupt Aggregator）`$(aggregator)` 对应的第 `$(prev-level-num)` 级中断号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_2ND_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel.aggregator_template:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel.aggregator_template#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_2ND_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_2ND_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_2ND_LVL_INTR_01_OFFSET"></a>

## 5.5 `CONFIG_2ND_LVL_INTR_01_OFFSET`

**提示（Prompt）**：第二级聚合器 1 的第一级 IRQ 线（IRQ Line）

**说明（Help）**

这是第 `$(cur-level-num)` 级中断聚合器（Interrupt Aggregator）`$(aggregator)` 对应的第 `$(prev-level-num)` 级中断号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_2ND_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel.aggregator_template:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel.aggregator_template#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_2ND_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_2ND_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_2ND_LVL_INTR_02_OFFSET"></a>

## 5.6 `CONFIG_2ND_LVL_INTR_02_OFFSET`

**提示（Prompt）**：第二级聚合器 2 的第一级 IRQ 线（IRQ Line）

**说明（Help）**

这是第 `$(cur-level-num)` 级中断聚合器（Interrupt Aggregator）`$(aggregator)` 对应的第 `$(prev-level-num)` 级中断号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_2ND_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel.aggregator_template:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel.aggregator_template#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_2ND_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_2ND_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_2ND_LVL_INTR_03_OFFSET"></a>

## 5.7 `CONFIG_2ND_LVL_INTR_03_OFFSET`

**提示（Prompt）**：第二级聚合器 3 的第一级 IRQ 线（IRQ Line）

**说明（Help）**

这是第 `$(cur-level-num)` 级中断聚合器（Interrupt Aggregator）`$(aggregator)` 对应的第 `$(prev-level-num)` 级中断号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_2ND_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel.aggregator_template:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel.aggregator_template#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_2ND_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_2ND_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_2ND_LVL_INTR_04_OFFSET"></a>

## 5.8 `CONFIG_2ND_LVL_INTR_04_OFFSET`

**提示（Prompt）**：第二级聚合器 4 的第一级 IRQ 线（IRQ Line）

**说明（Help）**

这是第 `$(cur-level-num)` 级中断聚合器（Interrupt Aggregator）`$(aggregator)` 对应的第 `$(prev-level-num)` 级中断号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_2ND_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel.aggregator_template:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel.aggregator_template#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_2ND_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_2ND_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_2ND_LVL_INTR_05_OFFSET"></a>

## 5.9 `CONFIG_2ND_LVL_INTR_05_OFFSET`

**提示（Prompt）**：第二级聚合器 5 的第一级 IRQ 线（IRQ Line）

**说明（Help）**

这是第 `$(cur-level-num)` 级中断聚合器（Interrupt Aggregator）`$(aggregator)` 对应的第 `$(prev-level-num)` 级中断号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_2ND_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel.aggregator_template:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel.aggregator_template#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_2ND_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_2ND_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_2ND_LVL_INTR_06_OFFSET"></a>

## 5.10 `CONFIG_2ND_LVL_INTR_06_OFFSET`

**提示（Prompt）**：第二级聚合器 6 的第一级 IRQ 线（IRQ Line）

**说明（Help）**

这是第 `$(cur-level-num)` 级中断聚合器（Interrupt Aggregator）`$(aggregator)` 对应的第 `$(prev-level-num)` 级中断号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_2ND_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel.aggregator_template:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel.aggregator_template#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_2ND_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_2ND_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_2ND_LVL_INTR_07_OFFSET"></a>

## 5.11 `CONFIG_2ND_LVL_INTR_07_OFFSET`

**提示（Prompt）**：第二级聚合器 7 的第一级 IRQ 线（IRQ Line）

**说明（Help）**

这是第 `$(cur-level-num)` 级中断聚合器（Interrupt Aggregator）`$(aggregator)` 对应的第 `$(prev-level-num)` 级中断号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_2ND_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel.aggregator_template:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel.aggregator_template#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_2ND_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_2ND_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_2ND_LVL_ISR_TBL_OFFSET"></a>

## 5.12 `CONFIG_2ND_LVL_ISR_TBL_OFFSET`

**提示（Prompt）**：第二级中断在 `_sw_isr_table` 中的偏移量（Offset）

**说明（Help）**

这是第二级中断的中断服务例程（Interrupt Service Routine，ISR）存储区在生成的 ISR 处理程序表 `_sw_isr_table` 中的起始偏移量。该区域通常分配在第一级中断的 ISR 之后。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_2ND_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support） → 第二级中断支持（Second-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_2ND_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_2ND_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_3RD_LEVEL_INTERRUPTS"></a>

## 5.13 `CONFIG_3RD_LEVEL_INTERRUPTS`

**提示（Prompt）**：第三级中断支持（Third-level Interrupt Support）

**说明（Help）**

第三级中断（Third-level Interrupt）用于增加系统可寻址的中断数量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_2ND_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_2ND_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_2ND_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_3RD_LEVEL_INTERRUPT_BITS"></a>

## 5.14 `CONFIG_3RD_LEVEL_INTERRUPT_BITS`

**提示（Prompt）**：第三级中断位总数（Third-level Interrupt Bits）

**说明（Help）**

32 位中断掩码（Interrupt Mask）中用于第三级中断的位数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[0, 30]
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_3RD_LVL_INTR_00_OFFSET"></a>

## 5.15 `CONFIG_3RD_LVL_INTR_00_OFFSET`

**提示（Prompt）**：第三级聚合器 0 的第二级 IRQ 线（IRQ Line）

**说明（Help）**

这是第 `$(cur-level-num)` 级中断聚合器（Interrupt Aggregator）`$(aggregator)` 对应的第 `$(prev-level-num)` 级中断号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_3RD_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel.aggregator_template:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel.aggregator_template#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_3RD_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_3RD_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_3RD_LVL_INTR_01_OFFSET"></a>

## 5.16 `CONFIG_3RD_LVL_INTR_01_OFFSET`

**提示（Prompt）**：第三级聚合器 1 的第二级 IRQ 线（IRQ Line）

**说明（Help）**

这是第 `$(cur-level-num)` 级中断聚合器（Interrupt Aggregator）`$(aggregator)` 对应的第 `$(prev-level-num)` 级中断号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_3RD_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel.aggregator_template:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel.aggregator_template#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_3RD_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_3RD_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_3RD_LVL_INTR_02_OFFSET"></a>

## 5.17 `CONFIG_3RD_LVL_INTR_02_OFFSET`

**提示（Prompt）**：第三级聚合器 2 的第二级 IRQ 线（IRQ Line）

**说明（Help）**

这是第 `$(cur-level-num)` 级中断聚合器（Interrupt Aggregator）`$(aggregator)` 对应的第 `$(prev-level-num)` 级中断号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_3RD_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel.aggregator_template:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel.aggregator_template#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_3RD_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_3RD_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_3RD_LVL_INTR_03_OFFSET"></a>

## 5.18 `CONFIG_3RD_LVL_INTR_03_OFFSET`

**提示（Prompt）**：第三级聚合器 3 的第二级 IRQ 线（IRQ Line）

**说明（Help）**

这是第 `$(cur-level-num)` 级中断聚合器（Interrupt Aggregator）`$(aggregator)` 对应的第 `$(prev-level-num)` 级中断号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_3RD_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel.aggregator_template:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel.aggregator_template#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_3RD_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_3RD_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_3RD_LVL_INTR_04_OFFSET"></a>

## 5.19 `CONFIG_3RD_LVL_INTR_04_OFFSET`

**提示（Prompt）**：第三级聚合器 4 的第二级 IRQ 线（IRQ Line）

**说明（Help）**

这是第 `$(cur-level-num)` 级中断聚合器（Interrupt Aggregator）`$(aggregator)` 对应的第 `$(prev-level-num)` 级中断号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_3RD_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel.aggregator_template:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel.aggregator_template#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_3RD_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_3RD_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_3RD_LVL_INTR_05_OFFSET"></a>

## 5.20 `CONFIG_3RD_LVL_INTR_05_OFFSET`

**提示（Prompt）**：第三级聚合器 5 的第二级 IRQ 线（IRQ Line）

**说明（Help）**

这是第 `$(cur-level-num)` 级中断聚合器（Interrupt Aggregator）`$(aggregator)` 对应的第 `$(prev-level-num)` 级中断号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_3RD_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel.aggregator_template:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel.aggregator_template#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_3RD_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_3RD_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_3RD_LVL_INTR_06_OFFSET"></a>

## 5.21 `CONFIG_3RD_LVL_INTR_06_OFFSET`

**提示（Prompt）**：第三级聚合器 6 的第二级 IRQ 线（IRQ Line）

**说明（Help）**

这是第 `$(cur-level-num)` 级中断聚合器（Interrupt Aggregator）`$(aggregator)` 对应的第 `$(prev-level-num)` 级中断号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_3RD_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel.aggregator_template:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel.aggregator_template#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_3RD_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_3RD_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_3RD_LVL_INTR_07_OFFSET"></a>

## 5.22 `CONFIG_3RD_LVL_INTR_07_OFFSET`

**提示（Prompt）**：第三级聚合器 7 的第二级 IRQ 线（IRQ Line）

**说明（Help）**

这是第 `$(cur-level-num)` 级中断聚合器（Interrupt Aggregator）`$(aggregator)` 对应的第 `$(prev-level-num)` 级中断号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_3RD_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel.aggregator_template:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel.aggregator_template#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_3RD_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_3RD_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_3RD_LVL_ISR_TBL_OFFSET"></a>

## 5.23 `CONFIG_3RD_LVL_ISR_TBL_OFFSET`

**提示（Prompt）**：第三级中断在 `_sw_isr_table` 中的偏移量（Offset）

**说明（Help）**

这是第三级中断的中断服务例程（Interrupt Service Routine，ISR）存储区在生成的 ISR 处理程序表 `_sw_isr_table` 中的起始偏移量。该区域通常分配在第二级中断的 ISR 之后。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_3RD_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support） → 第三级中断支持（Third-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_3RD_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_3RD_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_ARCV2_INTERRUPT_UNIT"></a>

## 5.24 `CONFIG_ARCV2_INTERRUPT_UNIT`

**提示（Prompt）**：ARCv2 中断单元（Interrupt Unit）

**说明（Help）**

ARCv2 中断单元（Interrupt Unit）分配了 16 个异常（Exception），对应向量 0～15；另有 240 个中断（Interrupt），对应向量 16～255。在基于 ARCv2 的处理器中，中断单元属于可选部件。构建处理器时，可以将其配置为包含中断单元。ARCv2 中断单元具有很高的可编程性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC)。

<a id="CONFIG_AURIX_IR"></a>

## 5.25 `CONFIG_AURIX_IR`

**提示（Prompt）**：Infineon AURIX 中断路由器（Interrupt Router）

**说明（Help）**

启用 Infineon AURIX 中断路由器（Interrupt Router）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_AURIX_IR_ENABLED
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_TC3X
CONFIG_SOC_SERIES_TC4X
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.infineon_aurix:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.infineon_aurix#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_TC3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TC3X)、[`CONFIG_SOC_SERIES_TC4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TC4X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_TC3X`、`CONFIG_SOC_SERIES_TC4X`。

<a id="CONFIG_BCM2835_ARMCTRL_IC"></a>

## 5.26 `CONFIG_BCM2835_ARMCTRL_IC`

**提示（Prompt）**：BCM2835 ARMC 外设中断控制器（Peripheral Interrupt Controller）

**说明（Help）**

BCM2835 ARMC 外设中断控制器（Peripheral Interrupt Controller）驱动，对应 BCM283x 系列的“GPU IRQ”一侧。在 BCM2710（Pi Zero 2 W）上，它级联在 BCM2836 ARM 本地中断控制器（ARM-local INTC）下；在 BCM2835（Pi 1 / Pi Zero W）上，它是直接连接到 ARM 内核 IRQ 线的根控制器（Root Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BRCM_BCM2835_ARMCTRL_IC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.brcm:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.brcm#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_BCM2836_L1_INTC"></a>

## 5.27 `CONFIG_BCM2836_L1_INTC`

**提示（Prompt）**：BCM2836 ARM 本地中断控制器（ARM-local Interrupt Controller）

**说明（Help）**

BCM2836 ARM 本地中断控制器（ARM-local Interrupt Controller）驱动；BCM2710 / Pi Zero 2 W 也具有该控制器。它将每个内核的 ARM 通用定时器（Generic Timer）IRQ、每核四个邮箱（Mailbox）IRQ、每核 PMU IRQ 以及级联的 GPU IRQ，路由到 ARM CPU IRQ 线的父控制器（Parent Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BRCM_BCM2836_L1_INTC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.brcm:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.brcm#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_CAVS_ICTL"></a>

## 5.28 `CONFIG_CAVS_ICTL`

**提示（Prompt）**：CAVS 中断逻辑（Interrupt Logic）

**说明（Help）**

共有 4 个这样的中断逻辑单元（Interrupt Logic），每个最多支持 32 个中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_CAVS_INTC_ENABLED && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.cavs:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.cavs#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_CAVS_ICTL_0_OFFSET"></a>

## 5.29 `CONFIG_CAVS_ICTL_0_OFFSET`

**提示（Prompt）**：CAVS_0 映射到的父级中断号（Parent Interrupt Number）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAVS_ICTL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.cavs:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.cavs#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → CAVS 中断逻辑（Interrupt Logic）

**配置项引用（Symbol References）**：[`CONFIG_CAVS_ICTL`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CAVS_ICTL)。

<a id="CONFIG_CAVS_ICTL_1_OFFSET"></a>

## 5.30 `CONFIG_CAVS_ICTL_1_OFFSET`

**提示（Prompt）**：CAVS_1 映射到的父级中断号（Parent Interrupt Number）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAVS_ICTL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.cavs:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.cavs#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → CAVS 中断逻辑（Interrupt Logic）

**配置项引用（Symbol References）**：[`CONFIG_CAVS_ICTL`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CAVS_ICTL)。

<a id="CONFIG_CAVS_ICTL_2_OFFSET"></a>

## 5.31 `CONFIG_CAVS_ICTL_2_OFFSET`

**提示（Prompt）**：CAVS_2 映射到的父级中断号（Parent Interrupt Number）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAVS_ICTL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.cavs:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.cavs#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → CAVS 中断逻辑（Interrupt Logic）

**配置项引用（Symbol References）**：[`CONFIG_CAVS_ICTL`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CAVS_ICTL)。

<a id="CONFIG_CAVS_ICTL_3_OFFSET"></a>

## 5.32 `CONFIG_CAVS_ICTL_3_OFFSET`

**提示（Prompt）**：CAVS_3 映射到的父级中断号（Parent Interrupt Number）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAVS_ICTL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.cavs:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.cavs#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → CAVS 中断逻辑（Interrupt Logic）

**配置项引用（Symbol References）**：[`CONFIG_CAVS_ICTL`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CAVS_ICTL)。

<a id="CONFIG_CAVS_ICTL_INIT_PRIORITY"></a>

## 5.33 `CONFIG_CAVS_ICTL_INIT_PRIORITY`

**提示（Prompt）**：CAVS ICTL 初始化优先级（Initialization Priority）

**说明（Help）**

CAVS 中断逻辑（Interrupt Logic）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAVS_ICTL
```

**默认值（Defaults）**

```text
45
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.cavs:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.cavs#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → CAVS 中断逻辑（Interrupt Logic）

**配置项引用（Symbol References）**：[`CONFIG_CAVS_ICTL`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CAVS_ICTL)。

<a id="CONFIG_CAVS_ISR_TBL_OFFSET"></a>

## 5.34 `CONFIG_CAVS_ISR_TBL_OFFSET`

**提示（Prompt）**：软件 ISR 表（SW ISR Table）中的偏移量

**说明（Help）**

该值表示软件中断服务例程表（SW_ISR_TABLE）中的偏移量，CAVS 中断控制器的 ISR 从该位置开始分配。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CAVS_ICTL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.cavs:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.cavs#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → CAVS 中断逻辑（Interrupt Logic）

**配置项引用（Symbol References）**：[`CONFIG_CAVS_ICTL`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CAVS_ICTL)。

<a id="CONFIG_CLIC"></a>

## 5.35 `CONFIG_CLIC`

**提示（Prompt）**：RISC-V 内核本地中断控制器（Core Local Interrupt Controller，CLIC）

**说明（Help）**

内核本地中断控制器（Core Local Interrupt Controller，CLIC）为 RISC-V 系统提供低延迟、向量化且可抢占的中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUCLEI_ECLIC_ENABLED || DT_HAS_RISCV_CLIC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RISCV_SOC_HAS_CUSTOM_IRQ_HANDLING
```

**被选择（Selected by）**

```text
CONFIG_NUCLEI_ECLIC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.clic:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.clic#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_SOC_HAS_CUSTOM_IRQ_HANDLING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_SOC_HAS_CUSTOM_IRQ_HANDLING)、[`CONFIG_NUCLEI_ECLIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_NUCLEI_ECLIC)。

<a id="CONFIG_CLIC_PARAMETER_INTCTLBITS"></a>

## 5.36 `CONFIG_CLIC_PARAMETER_INTCTLBITS`

**提示（Prompt）**：`clicintctl` 寄存器中的可修改位数（Modifiable Bits）

**说明（Help）**

该选项指定 `clicintctl` 寄存器中可修改的位数（Modifiable Bits）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLIC
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[0, 8]
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.clic:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.clic#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CLIC)。

<a id="CONFIG_CLIC_PARAMETER_MNLBITS"></a>

## 5.37 `CONFIG_CLIC_PARAMETER_MNLBITS`

**提示（Prompt）**：`CLICINTCTLBITS` 中用于编码中断级别（Interrupt Level）的位数

**说明（Help）**

该选项指定 `CLICINTCTLBITS` 中分配用于编码机器模式（Machine Mode）中断级别（Interrupt Level）的位数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLIC
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, CONFIG_CLIC_PARAMETER_INTCTLBITS]
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.clic:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.clic#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CLIC)、[`CONFIG_CLIC_PARAMETER_INTCTLBITS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CLIC_PARAMETER_INTCTLBITS)。

<a id="CONFIG_CLIC_SMCLICCONFIG_EXT"></a>

## 5.38 `CONFIG_CLIC_SMCLICCONFIG_EXT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 SMCLICCONFIG 扩展（Extension），允许配置中断级别位数等 CLIC 参数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLIC
```

**被选择（Selected by）**

```text
CONFIG_SOC_AE350_INTERRUPT_TYPE_CLIC
CONFIG_NUCLEI_ECLIC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.clic:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.clic#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CLIC)、[`CONFIG_SOC_AE350_INTERRUPT_TYPE_CLIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AE350_INTERRUPT_TYPE_CLIC)、[`CONFIG_NUCLEI_ECLIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_NUCLEI_ECLIC)。

<a id="CONFIG_CLIC_SMCLICSHV_EXT"></a>

## 5.39 `CONFIG_CLIC_SMCLICSHV_EXT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

选择性硬件向量化扩展（Selective Hardware Vectoring Extension）使用户能够灵活选择每个中断的行为。CLIC 驱动需要实现 `riscv_clic_irq_vector_set()` 函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLIC
```

**被选择（Selected by）**

```text
CONFIG_SOC_AE350_INTERRUPT_TYPE_CLIC
CONFIG_NUCLEI_ECLIC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.clic:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.clic#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CLIC)、[`CONFIG_SOC_AE350_INTERRUPT_TYPE_CLIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AE350_INTERRUPT_TYPE_CLIC)、[`CONFIG_NUCLEI_ECLIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_NUCLEI_ECLIC)。

<a id="CONFIG_DW_ICTL"></a>

## 5.40 `CONFIG_DW_ICTL`

**提示（Prompt）**：DesignWare 中断控制器（Interrupt Controller）

**说明（Help）**

DesignWare 中断控制器（Interrupt Controller）可用作第二级中断控制器，将多个中断源合并到一根线上，再将其路由至第一级中断控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_DESIGNWARE_INTC_ENABLED && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.dw:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.dw#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_DW_ICTL_ACE"></a>

## 5.41 `CONFIG_DW_ICTL_ACE`

**提示（Prompt）**：用于 ACE 的 DesignWare 中断控制器（Interrupt Controller）

**说明（Help）**

ACE 使用的 DesignWare 中断控制器（Interrupt Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ACE_INTC_ENABLED && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_INTEL_ADSP_ACE
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.dw:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.dw#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)、[`CONFIG_SOC_SERIES_INTEL_ADSP_ACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_INTEL_ADSP_ACE)。

<a id="CONFIG_DW_ICTL_INIT_PRIORITY"></a>

## 5.42 `CONFIG_DW_ICTL_INIT_PRIORITY`

**提示（Prompt）**：DW 中断控制器的初始化优先级（Initialization Priority）

**说明（Help）**

DesignWare 中断控制器（Interrupt Controller）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DW_ICTL
```

**默认值（Defaults）**

```text
48
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.dw:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.dw#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → DesignWare 中断控制器（Interrupt Controller）

**配置项引用（Symbol References）**：[`CONFIG_DW_ICTL`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_DW_ICTL)。

<a id="CONFIG_DW_ICTL_NAME"></a>

## 5.43 `CONFIG_DW_ICTL_NAME`

**提示（Prompt）**：DesignWare 中断控制器名称（Name）

**说明（Help）**

为 DesignWare 中断控制器（Interrupt Controller）实例指定名称。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_DW_ICTL
```

**默认值（Defaults）**

```text
"DW_ICTL"
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.dw:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.dw#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → DesignWare 中断控制器（Interrupt Controller）

**配置项引用（Symbol References）**：[`CONFIG_DW_ICTL`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_DW_ICTL)。

<a id="CONFIG_DW_ISR_TBL_OFFSET"></a>

## 5.44 `CONFIG_DW_ISR_TBL_OFFSET`

**提示（Prompt）**：软件 ISR 表（SW ISR Table）中的偏移量

**说明（Help）**

该值表示软件中断服务例程表（SW_ISR_TABLE）中的偏移量，DesignWare 中断控制器的 ISR 从该位置开始分配。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DW_ICTL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.dw:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.dw#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → DesignWare 中断控制器（Interrupt Controller）

**配置项引用（Symbol References）**：[`CONFIG_DW_ICTL`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_DW_ICTL)。

<a id="CONFIG_EXTI_STM32"></a>

## 5.45 `CONFIG_EXTI_STM32`

**提示（Prompt）**：STM32 外部中断／事件控制器（External Interrupt/Event Controller，EXTI）驱动

**说明（Help）**

启用 STM32 外部中断／事件控制器（EXTI）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_EXTI_ENABLED && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_COMPARATOR_STM32_COMP
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.stm32:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.stm32#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_COMPARATOR_STM32_COMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COMPARATOR_STM32_COMP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_GD32_EXTI"></a>

## 5.46 `CONFIG_GD32_EXTI`

**提示（Prompt）**：GD32 扩展中断与事件控制器（Extended Interrupts and Events Controller，EXTI）

**说明（Help）**

启用 GigaDevice GD32 扩展中断与事件控制器（Extended Interrupts and Events Controller，EXTI）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_EXTI_ENABLED
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_GPIO_GD32
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.gd32_exti:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.gd32_exti#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO_GD32)。

<a id="CONFIG_GIC_SAFE_CONFIG"></a>

## 5.47 `CONFIG_GIC_SAFE_CONFIG`

**提示（Prompt）**：GIC 分发器安全配置（Distributor Safe Configuration）

**说明（Help）**

多个操作系统（Operating System，OS）可能共享同一个 GIC 分发器（Distributor）。如果另一个 OS 已启用分发器，再次执行完整的分发器初始化可能覆盖其使能状态、目标和优先级。启用此选项后，如果 GIC 分发器已经处于活动状态，Zephyr 将跳过其初始化。`arm_gic_irq_enable()` 仍会更新各 IRQ 的亲和性（Affinity）。此选项适用于 GICv1、GICv2 和 GICv3。

限制（GICv1/GICv2）：`arm_gic_irq_enable()` 中各 IRQ 的亲和性更新是对共享 `GICD_ITARGETSRn` 寄存器的读—改—写（Read-modify-write）操作，没有在各 OS 之间进行串行化。两个独立的 Zephyr 实例若同时启用同一个共享外设中断（Shared Peripheral Interrupt，SPI），可能发生竞争并丢失一次更新；多个 OS 并发启用同一个共享 SPI 的情况不在此选项的处理范围内。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GIC && CONFIG_CPU_CORTEX
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.gic:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.gic#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GIC)、[`CONFIG_CPU_CORTEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_GIC`。

<a id="CONFIG_GIC_SINGLE_SECURITY_STATE"></a>

## 5.48 `CONFIG_GIC_SINGLE_SECURITY_STATE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

某些 ARM Cortex 系列处理器仅支持单一安全状态（Single Security State）。其他处理器必须从 EL3 设置此状态，才能在单一安全模式下运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GIC_V3 && CONFIG_CPU_CORTEX
```

**被选择（Selected by）**

```text
CONFIG_SOC_R8A779F0_R52
CONFIG_SOC_R8A779G0_R52
CONFIG_SOC_R8A78000_R52
CONFIG_SOC_SERIES_RZN2H
CONFIG_SOC_SERIES_RZN2L
CONFIG_SOC_SERIES_RZT2H
CONFIG_SOC_SERIES_RZT2L
CONFIG_SOC_SERIES_RZT2M
CONFIG_SOC_AMD_VERSALNET_RPU
CONFIG_SOC_AMD_VERSAL2_RPU
CONFIG_SOC_FVP_AEMV8R_AARCH64
CONFIG_SOC_FVP_AEMV8R_AARCH32
CONFIG_SOC_AN536
CONFIG_SOC_S32K566_R52
CONFIG_SOC_SERIES_S32ZE
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.gic:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.gic#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GIC_V3`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_GIC_V3)、[`CONFIG_CPU_CORTEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX)、[`CONFIG_SOC_R8A779F0_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A779F0_R52)、[`CONFIG_SOC_R8A779G0_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A779G0_R52)、[`CONFIG_SOC_R8A78000_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A78000_R52)、[`CONFIG_SOC_SERIES_RZN2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2H)、[`CONFIG_SOC_SERIES_RZN2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2L)、[`CONFIG_SOC_SERIES_RZT2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2H)、[`CONFIG_SOC_SERIES_RZT2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2L)、[`CONFIG_SOC_SERIES_RZT2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2M)、[`CONFIG_SOC_AMD_VERSALNET_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET_RPU)、[`CONFIG_SOC_AMD_VERSAL2_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2_RPU)、[`CONFIG_SOC_FVP_AEMV8R_AARCH64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FVP_AEMV8R_AARCH64)、[`CONFIG_SOC_FVP_AEMV8R_AARCH32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FVP_AEMV8R_AARCH32)、[`CONFIG_SOC_AN536`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN536)、[`CONFIG_SOC_S32K566_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K566_R52)、[`CONFIG_SOC_SERIES_S32ZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32ZE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_R8A779G0_R52`、`CONFIG_SOC_FVP_AEMV8R_AARCH64`、`CONFIG_SOC_FVP_AEMV8R_AARCH32`、`CONFIG_SOC_AN536`、`CONFIG_SOC_S32K566_R52`、`CONFIG_SOC_SERIES_S32ZE`。

<a id="CONFIG_GIC_V1"></a>

## 5.49 `CONFIG_GIC_V1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARM 通用中断控制器（Generic Interrupt Controller，GIC）v1，例如 PL390，可配合 ARM Cortex 系列处理器工作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX
```

**默认值（Defaults）**

```text
DT_HAS_ARM_GIC_V1_ENABLED
```

**主动选择（Selects）**

```text
CONFIG_GIC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.gic:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.gic#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX)、[`CONFIG_GIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_GIC`。

<a id="CONFIG_GIC_V2"></a>

## 5.50 `CONFIG_GIC_V2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARM 通用中断控制器（Generic Interrupt Controller，GIC）v2，例如 GIC-400，可配合 ARM Cortex 系列处理器工作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX
```

**默认值（Defaults）**

```text
DT_HAS_ARM_GIC_V2_ENABLED
```

**主动选择（Selects）**

```text
CONFIG_GIC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.gic:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.gic#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX)、[`CONFIG_GIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_GIC`。

<a id="CONFIG_GIC_V3"></a>

## 5.51 `CONFIG_GIC_V3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ARM 通用中断控制器（Generic Interrupt Controller，GIC）v3，例如 GIC-500 和 GIC-600，可配合 ARM Cortex 系列处理器工作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX
```

**默认值（Defaults）**

```text
DT_HAS_ARM_GIC_V3_ENABLED
```

**主动选择（Selects）**

```text
CONFIG_GIC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.gic:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.gic#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX)、[`CONFIG_GIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_GIC`。

<a id="CONFIG_GIC_V3_ITS"></a>

## 5.52 `CONFIG_GIC_V3_ITS`

**提示（Prompt）**：GIC v3 中断转换服务（Interrupt Translation Service，ITS）

**说明（Help）**

支持可选的中断转换服务（Interrupt Translation Service，ITS），例如用于转换来自 PCIe MSI 消息的硬件中断。请注意，ITS 从系统堆（System Heap）分配其表；下方的最小大小配置项 `HEAP_MEM_POOL_ADD_SIZE_GIC_V3_ITS` 已将这部分需求计入。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GIC_V3 && CONFIG_CPU_CORTEX
```

**主动选择（Selects）**

```text
CONFIG_ARMV8_A_NS
CONFIG_DYNAMIC_INTERRUPTS
CONFIG_KERNEL_MEM_POOL
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.gic:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.gic#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GIC_V3`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_GIC_V3)、[`CONFIG_CPU_CORTEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX)、[`CONFIG_ARMV8_A_NS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARMV8_A_NS)、[`CONFIG_DYNAMIC_INTERRUPTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_KERNEL_MEM_POOL`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_MEM_POOL)。

<a id="CONFIG_GIC_V3_ITS_DMA_NONCOHERENT"></a>

## 5.53 `CONFIG_GIC_V3_ITS_DMA_NONCOHERENT`

**提示（Prompt）**：GIC ITS 不具备 DMA 一致性（DMA Noncoherent）

**说明（Help）**

某些平台上的 GIC ITS 连接到不具备一致性的下游互连（Non-coherent Downstream Interconnect），因此需要使用不可缓存（Non-cacheable）且不可共享（Non-shareable）的访问属性来访问外部存储器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GIC_V3_ITS && CONFIG_CPU_CORTEX
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.gic:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.gic#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GIC_V3_ITS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_GIC_V3_ITS)、[`CONFIG_CPU_CORTEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX)。

<a id="CONFIG_GIC_V3_RDIST_DMA_NONCOHERENT"></a>

## 5.54 `CONFIG_GIC_V3_RDIST_DMA_NONCOHERENT`

**提示（Prompt）**：GIC 重分发器（Redistributor）不具备 DMA 一致性

**说明（Help）**

某些平台上的 GIC 重分发器（Redistributor）连接到不具备一致性的下游互连（Non-coherent Downstream Interconnect），因此需要使用不可缓存（Non-cacheable）且不可共享（Non-shareable）的访问属性来访问外部存储器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GIC_V3 && CONFIG_CPU_CORTEX
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.gic:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.gic#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GIC_V3`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_GIC_V3)、[`CONFIG_CPU_CORTEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX)。

<a id="CONFIG_GIC_V3_RDIST_MATCHING_AFF0_ONLY"></a>

## 5.55 `CONFIG_GIC_V3_RDIST_MATCHING_AFF0_ONLY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

某些平台仅使用 `aff0` 来匹配 `mpdir` 与 `GICR.aff`。启用此选项后，仅比较 `aff0` 来查找目标重分发器（Redistributor）。

译注：`mpdir` 按原文保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GIC_V3 && CONFIG_CPU_CORTEX
```

**默认值（Defaults）**

```text
y if CONFIG_CPU_CORTEX_R52
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.gic:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.gic#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GIC_V3`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_GIC_V3)、[`CONFIG_CPU_CORTEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX)、[`CONFIG_CPU_CORTEX_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_R52)。

<a id="CONFIG_GPIO_INTC_STM32"></a>

## 5.56 `CONFIG_GPIO_INTC_STM32`

**提示（Prompt）**：STM32 GPIO 中断／事件控制器（Interrupt/Event Controller，EXTI）驱动

**说明（Help）**

启用 STM32 GPIO 中断控制器（Interrupt Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EXTI_STM32 && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.stm32:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.stm32#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → STM32 外部中断／事件控制器（External Interrupt/Event Controller，EXTI）驱动

**配置项引用（Symbol References）**：[`CONFIG_EXTI_STM32`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_EXTI_STM32)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_GPIO_INTC_STM32WB0"></a>

## 5.57 `CONFIG_GPIO_INTC_STM32WB0`

**提示（Prompt）**：STM32WB0 系列 GPIO 中断控制器（Interrupt Controller）驱动

**说明（Help）**

启用 STM32WB0 系列 GPIO 中断控制器（Interrupt Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32WB0_GPIO_INTC_ENABLED && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.stm32:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.stm32#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_HAS_ITE_INTC"></a>

## 5.58 `CONFIG_HAS_ITE_INTC`

原库同名定义共 2 条；本项为数据库第 7274 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 `ITE_IT51XXX_INTC` 时，选择此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ITE_IT51XXX_INTC
CONFIG_ITE_IT8XXX2_INTC
CONFIG_ITE_IT8XXX2_INTC_V2
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.it51xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.it51xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ITE_IT51XXX_INTC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_ITE_IT51XXX_INTC)、[`CONFIG_ITE_IT8XXX2_INTC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_ITE_IT8XXX2_INTC)、[`CONFIG_ITE_IT8XXX2_INTC_V2`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_ITE_IT8XXX2_INTC_V2)。

<a id="CONFIG_HAS_ITE_INTC--record-7275"></a>

## 5.59 `CONFIG_HAS_ITE_INTC`

原库同名定义共 2 条；本项为数据库第 7275 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 `ITE_IT8XXX2_INTC` 或 `ITE_IT8XXX2_INTC_V2` 时，选择此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ITE_IT51XXX_INTC
CONFIG_ITE_IT8XXX2_INTC
CONFIG_ITE_IT8XXX2_INTC_V2
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.it8xxx2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.it8xxx2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ITE_IT51XXX_INTC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_ITE_IT51XXX_INTC)、[`CONFIG_ITE_IT8XXX2_INTC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_ITE_IT8XXX2_INTC)、[`CONFIG_ITE_IT8XXX2_INTC_V2`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_ITE_IT8XXX2_INTC_V2)。

<a id="CONFIG_HAZARD3_INTC"></a>

## 5.60 `CONFIG_HAZARD3_INTC`

**提示（Prompt）**：Hazard3 中断控制器（Interrupt Controller）

**说明（Help）**

RP2350 系列片上系统（SoC）中 Hazard3 中断控制器（Interrupt Controller）的 IRQ 实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_HAZARD3_HAZARD3_INTC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PICOSDK_USE_CLAIM
CONFIG_RISCV_SOC_HAS_CUSTOM_IRQ_HANDLING
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_PICOSDK_USE_CLAIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_CLAIM)、[`CONFIG_RISCV_SOC_HAS_CUSTOM_IRQ_HANDLING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_SOC_HAS_CUSTOM_IRQ_HANDLING)。

<a id="CONFIG_INFINEON_INTC_SYSINTC"></a>

## 5.61 `CONFIG_INFINEON_INTC_SYSINTC`

**提示（Prompt）**：Infineon CAT1 CPUSS 系统中断多路复用器（System Interrupt Multiplexer）

**说明（Help）**

使用 Zephyr 多级中断框架（Multi-level Interrupt Framework）的 Infineon CAT1 CPUSS 中断多路复用器（Interrupt Multiplexer）驱动。系统中断属于第二级，NvicMux 线是第一级聚合器（Aggregator）。`_sw_isr_table` 在构建时生成并存储于 ROM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_SYSINTC_ENABLED && CONFIG_SOC_FAMILY_INFINEON_CAT1
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MULTI_LEVEL_INTERRUPTS
CONFIG_2ND_LEVEL_INTERRUPTS
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.infineon:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.infineon#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_INFINEON_CAT1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_CAT1)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)、[`CONFIG_2ND_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_2ND_LEVEL_INTERRUPTS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INFINEON_CAT1`。

<a id="CONFIG_INTC_AMD_ACP"></a>

## 5.62 `CONFIG_INTC_AMD_ACP`

**提示（Prompt）**：AMD ACP 中断控制器（Interrupt Controller）驱动

**说明（Help）**

启用 AMD 音频协处理器（Audio Co-Processor，ACP）中断控制器支持。该驱动管理 ACP 7.0 音频子系统的中断处理，为 AMD 音频 DSP 支持最多 9 个中断源，包括 DMA、SoundWire 以及其他音频相关外设中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMD_ACP_INTC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.acp:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.acp#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_INTC_AMD_ACP_INIT_PRIORITY"></a>

## 5.63 `CONFIG_INTC_AMD_ACP_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Initialization Priority）

**说明（Help）**

ACP 中断控制器（Interrupt Controller）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INTC_AMD_ACP
```

**默认值（Defaults）**

```text
40
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.acp:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.acp#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → AMD ACP 中断控制器（Interrupt Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_INTC_AMD_ACP`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_INTC_AMD_ACP)。

<a id="CONFIG_INTC_AMD_ACP_ISR_TBL_OFFSET"></a>

## 5.64 `CONFIG_INTC_AMD_ACP_ISR_TBL_OFFSET`

**提示（Prompt）**：软件 ISR 表（SW ISR Table）中的偏移量

**说明（Help）**

该值表示软件中断服务例程表（SW_ISR_TABLE）中的偏移量，ACP 中断控制器的 ISR 从该位置开始分配。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INTC_AMD_ACP
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.acp:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.acp#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → AMD ACP 中断控制器（Interrupt Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_INTC_AMD_ACP`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_INTC_AMD_ACP)。

<a id="CONFIG_INTC_ESP32"></a>

## 5.65 `CONFIG_INTC_ESP32`

**提示（Prompt）**：Espressif SoC 的中断分配器（Interrupt Allocator）

**说明（Help）**

为基于 Xtensa 架构的 Espressif 片上系统（SoC）启用自定义中断分配器（Interrupt Allocator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y if !CONFIG_SOC_ESP32C5_LPCORE && !CONFIG_SOC_ESP32C6_LPCORE && !CONFIG_SOC_ESP32P4_LPCORE
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.esp32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.esp32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SOC_ESP32C5_LPCORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32C5_LPCORE)、[`CONFIG_SOC_ESP32C6_LPCORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32C6_LPCORE)、[`CONFIG_SOC_ESP32P4_LPCORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32P4_LPCORE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_INTC_ESP32_DECISIONS_LOG"></a>

## 5.66 `CONFIG_INTC_ESP32_DECISIONS_LOG`

**提示（Prompt）**：Espressif 中断分配器日志（Interrupt Allocator Logging）

**说明（Help）**

启用此选项可显示中断分配器（Interrupt Allocator）所作决策的信息。这不会影响中断分配器的使用，但可能有助于调试。启用后，消息将打印到串行控制台（Serial Console）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INTC_ESP32
```

**主动选择（Selects）**

```text
CONFIG_LOG
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.esp32:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.esp32#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → Espressif SoC 的中断分配器（Interrupt Allocator）

**配置项引用（Symbol References）**：[`CONFIG_INTC_ESP32`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_INTC_ESP32)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)。

<a id="CONFIG_INTC_INIT_PRIORITY"></a>

## 5.67 `CONFIG_INTC_INIT_PRIORITY`

**提示（Prompt）**：中断控制器初始化优先级（Initialization Priority）

**说明（Help）**

中断控制器（Interrupt Controller）设备的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEFAULT
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_KERNEL_INIT_PRIORITY_DEFAULT`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEFAULT)。

<a id="CONFIG_INTC_MCHP_AIC_G1"></a>

## 5.68 `CONFIG_INTC_MCHP_AIC_G1`

**提示（Prompt）**：Microchip AIC G1 中断控制器（Interrupt Controller）驱动

**说明（Help）**

此选项启用 AIC（高级中断控制器，Advanced Interrupt Controller）外设 g1 分组的中断控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_AIC_G1_INTC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_INTC_MCHP_EIC_G1"></a>

## 5.69 `CONFIG_INTC_MCHP_EIC_G1`

**提示（Prompt）**：Microchip 器件外部中断控制器（External Interrupt Controller，EIC）驱动

**说明（Help）**

启用 Microchip EIC G1 外设的外部中断控制器（EIC）驱动。GPIO 中断支持需要此驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_EIC_G1_INTC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.mchp:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.mchp#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_INTC_MTK_ADSP"></a>

## 5.70 `CONFIG_INTC_MTK_ADSP`

**提示（Prompt）**：MediaTek 音频 DSP 中断控制器（Interrupt Controller）

**说明（Help）**

一种非常简单的级联中断控制器（Cascaded Interrupt Controller），由两个位域寄存器（状态和使能）以及一个定义有效中断的掩码值组成。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MEDIATEK_ADSP_INTC_ENABLED
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.mtk_adsp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.mtk_adsp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_INTEL_VTD_ICTL"></a>

## 5.71 `CONFIG_INTEL_VTD_ICTL`

**提示（Prompt）**：Intel VT-D 中断重映射控制器（Interrupt Remapping Controller）

**说明（Help）**

此类中断重映射（Interrupt Remapping）硬件由 Intel VT-D 技术提供。目前它仅用于 MSI/MSI-X 多向量支持（Multi-vector Support）。如果 PCIe 设备需要多向量支持，就必须启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_VT_D_ENABLED && !CONFIG_BOARD_QEMU_X86_64 && CONFIG_ACPI && CONFIG_X86 && CONFIG_64BIT && CONFIG_PCIE_MSI_MULTI_VECTOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CACHE_MANAGEMENT
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.intel_vtd:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.intel_vtd#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_QEMU_X86_64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_QEMU_X86_64)、[`CONFIG_ACPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ACPI)、[`CONFIG_X86`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86)、[`CONFIG_64BIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_64BIT)、[`CONFIG_PCIE_MSI_MULTI_VECTOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE_MSI_MULTI_VECTOR)、[`CONFIG_CACHE_MANAGEMENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_MANAGEMENT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_QEMU_X86_64`。

<a id="CONFIG_INTEL_VTD_ICTL_INIT_PRIORITY"></a>

## 5.72 `CONFIG_INTEL_VTD_ICTL_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Initialization Priority）

**说明（Help）**

应尽早初始化此设备，先于任何可能依赖它来获得 MSI/MSI-X 多向量支持（Multi-vector Support）的其他设备。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INTEL_VTD_ICTL
```

**默认值（Defaults）**

```text
40
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.intel_vtd:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.intel_vtd#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → Intel VT-D 中断重映射控制器（Interrupt Remapping Controller）

**配置项引用（Symbol References）**：[`CONFIG_INTEL_VTD_ICTL`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_INTEL_VTD_ICTL)。

<a id="CONFIG_INTEL_VTD_ICTL_NO_SRC_ID_CHECK"></a>

## 5.73 `CONFIG_INTEL_VTD_ICTL_NO_SRC_ID_CHECK`

**提示（Prompt）**：从不检查源标识（Source ID）

**说明（Help）**

禁用中断重映射表项（Interrupt Remapping Table Entry，IRTE）中的源标识（Source ID）检查。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INTEL_VTD_ICTL
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.intel_vtd:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.intel_vtd#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → Intel VT-D 中断重映射控制器（Interrupt Remapping Controller）

**配置项引用（Symbol References）**：[`CONFIG_INTEL_VTD_ICTL`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_INTEL_VTD_ICTL)。

<a id="CONFIG_INTEL_VTD_ICTL_XAPIC_PASSTHROUGH"></a>

## 5.74 `CONFIG_INTEL_VTD_ICTL_XAPIC_PASSTHROUGH`

**提示（Prompt）**：XAPIC 模式直通（Pass-through）

**说明（Help）**

如果启用 XAPIC 模式，将避免重映射所有中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_X2APIC && CONFIG_INTEL_VTD_ICTL
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.intel_vtd:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.intel_vtd#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → Intel VT-D 中断重映射控制器（Interrupt Remapping Controller）

**配置项引用（Symbol References）**：[`CONFIG_X2APIC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_X2APIC)、[`CONFIG_INTEL_VTD_ICTL`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_INTEL_VTD_ICTL)。

<a id="CONFIG_IOAPIC"></a>

## 5.75 `CONFIG_IOAPIC`

**提示（Prompt）**：I/O 高级可编程中断控制器（IO-APIC）

**说明（Help）**

此选项表示目标具有 I/O 高级可编程中断控制器（IO-APIC）设备。该能力使依赖 IO-APIC 的代码能够被纳入。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_IOAPIC_ENABLED && CONFIG_LOAPIC
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_INTEL_ISH
CONFIG_HPET_TIMER
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.loapic:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.loapic#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 本地高级可编程中断控制器（Local APIC，LOAPIC）

**配置项引用（Symbol References）**：[`CONFIG_LOAPIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_LOAPIC)、[`CONFIG_SOC_FAMILY_INTEL_ISH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ISH)、[`CONFIG_HPET_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HPET_TIMER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ISH`。

<a id="CONFIG_IOAPIC_MASK_RTE"></a>

## 5.76 `CONFIG_IOAPIC_MASK_RTE`

**提示（Prompt）**：启动时屏蔽重定向表项（RTE）

**说明（Help）**

如果 IOAPIC 重定向表项（Redirection Table Entry，RTE）可能处于未定义状态，则在启动时屏蔽所有 RTE。若能保证 OS 启动时所有 RTE 均已被屏蔽，或前一个启动阶段已经完成需要保留的 IOAPIC 配置，则不需要此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IOAPIC && CONFIG_LOAPIC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.loapic:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.loapic#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 本地高级可编程中断控制器（Local APIC，LOAPIC） → I/O 高级可编程中断控制器（IO-APIC）

**配置项引用（Symbol References）**：[`CONFIG_IOAPIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_IOAPIC)、[`CONFIG_LOAPIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_LOAPIC)。

<a id="CONFIG_ITE_IT51XXX_INTC"></a>

## 5.77 `CONFIG_ITE_IT51XXX_INTC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项主要用于汇集来自多个模块的中断。可配置电平触发（Level-triggered）和边沿触发（Edge-triggered）模式，也可配置触发模式的中断极性（Interrupt Polarity）。每个中断源都可以单独使能或屏蔽。

译注：原文的 `dege-triggered` 按边沿触发理解。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_INTC_ENABLED
```

**默认值（Defaults）**

```text
DT_HAS_ITE_IT51XXX_INTC_ENABLED
```

**主动选择（Selects）**

```text
CONFIG_HAS_ITE_INTC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.it51xxx:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.it51xxx#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_ITE_INTC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_HAS_ITE_INTC)。

<a id="CONFIG_ITE_IT51XXX_INTC_VECTOR_LOADING_CTRL_SUPPORTED"></a>

## 5.78 `CONFIG_ITE_IT51XXX_INTC_VECTOR_LOADING_CTRL_SUPPORTED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

某些 IT51xxx SoC 要求固件在访问中断向量（Interrupt Vector）之前，先配置中断向量加载控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ITE_IT51XXX_INTC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.it51xxx:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.it51xxx#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ITE_IT51XXX_INTC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_ITE_IT51XXX_INTC)。

<a id="CONFIG_ITE_IT51XXX_WUC"></a>

## 5.79 `CONFIG_ITE_IT51XXX_WUC`

**提示（Prompt）**：ITE it51xxx 唤醒控制器（Wakeup Controller，WUC）接口

**说明（Help）**

此选项启用 IT51XXX 系列的唤醒控制器（Wakeup Controller）接口。KSCAN、UART、eSPI、GPIO 等的中断支持需要此接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_WUC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.it51xxx:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.it51xxx#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_ITE_IT51XXX_WUC_EITHER_EDGE_HW"></a>

## 5.80 `CONFIG_ITE_IT51XXX_WUC_EITHER_EDGE_HW`

**提示（Prompt）**：IT51XXX WUC 的硬件双边沿触发（Either-edge Triggering）支持

**说明（Help）**

如果硬件支持双边沿触发（Either-edge Triggering），选择此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.it51xxx:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.it51xxx#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_ITE_IT8XXX2_INTC"></a>

## 5.81 `CONFIG_ITE_IT8XXX2_INTC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

配置共享中断驱动（Shared Interrupt Driver）的每个共享实例允许的最大客户端数。为节省 RAM，请将该值设置为实际可用的最小值。此软件中断默认由设备树（Devicetree）启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_INTC_ENABLED
```

**默认值（Defaults）**

```text
DT_HAS_ITE_IT8XXX2_INTC_ENABLED
```

**主动选择（Selects）**

```text
CONFIG_HAS_ITE_INTC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.it8xxx2:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.it8xxx2#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_ITE_INTC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_HAS_ITE_INTC)。

<a id="CONFIG_ITE_IT8XXX2_INTC_V2"></a>

## 5.82 `CONFIG_ITE_IT8XXX2_INTC_V2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项启用 IT82XX2 系列的中断控制器（Interrupt Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_INTC_V2_ENABLED
```

**默认值（Defaults）**

```text
DT_HAS_ITE_IT8XXX2_INTC_V2_ENABLED
```

**主动选择（Selects）**

```text
CONFIG_HAS_ITE_INTC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.it8xxx2:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.it8xxx2#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_ITE_INTC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_HAS_ITE_INTC)。

<a id="CONFIG_ITE_IT8XXX2_WUC"></a>

## 5.83 `CONFIG_ITE_IT8XXX2_WUC`

**提示（Prompt）**：ITE it8xxx2 唤醒控制器（Wakeup Controller，WUC）接口

**说明（Help）**

此选项启用 IT8XXX2 系列的唤醒控制器（Wakeup Controller）接口。KSCAN、UART、eSPI、GPIO 等的中断支持需要此接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_WUC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.it8xxx2:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.it8xxx2#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_LEGACY_CLIC"></a>

## 5.84 `CONFIG_LEGACY_CLIC`

**提示（Prompt）**：使用旧版 CLIC 规范（Legacy CLIC Specification）

**说明（Help）**

启用旧版内核本地中断控制器（Legacy CLIC）；该版本不支持 `smclicshv` 扩展，通过 `mtvec` 的模式位设置硬件向量化（Hardware Vectoring）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_HAS_CLIC && CONFIG_CLIC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.clic:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.clic#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_HAS_CLIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_HAS_CLIC)、[`CONFIG_CLIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CLIC)。

<a id="CONFIG_LEGACY_CLIC_MEMORYMAP_ACCESS"></a>

## 5.85 `CONFIG_LEGACY_CLIC_MEMORYMAP_ACCESS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用旧版内核本地中断控制器（Legacy CLIC），允许通过内存映射访问（Memory-mapped Access）而非间接 CSR 访问来访问 CLIC 寄存器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLIC
```

**被选择（Selected by）**

```text
CONFIG_SOC_AE350_INTERRUPT_TYPE_CLIC
CONFIG_NUCLEI_ECLIC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.clic:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.clic#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CLIC)、[`CONFIG_SOC_AE350_INTERRUPT_TYPE_CLIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AE350_INTERRUPT_TYPE_CLIC)、[`CONFIG_NUCLEI_ECLIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_NUCLEI_ECLIC)。

<a id="CONFIG_LEON_IRQMP"></a>

## 5.86 `CONFIG_LEON_IRQMP`

**提示（Prompt）**：GRLIB IRQMP 中断控制器（Interrupt Controller）

**说明（Help）**

GRLIB IRQMP 和 IRQAMP

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GAISLER_IRQMP_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_LOAPIC"></a>

## 5.87 `CONFIG_LOAPIC`

**提示（Prompt）**：本地高级可编程中断控制器（Local APIC，LOAPIC）

**说明（Help）**

此选项选择本地 APIC（Local APIC）作为中断控制器（Interrupt Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_INTEL_ISH
CONFIG_HPET_TIMER
CONFIG_APIC_TIMER
CONFIG_APIC_TSC_DEADLINE_TIMER
CONFIG_APIC_TIMER_TSC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.loapic:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.loapic#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_X86`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86)、[`CONFIG_SOC_FAMILY_INTEL_ISH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INTEL_ISH)、[`CONFIG_HPET_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HPET_TIMER)、[`CONFIG_APIC_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_APIC_TIMER)、[`CONFIG_APIC_TSC_DEADLINE_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_APIC_TSC_DEADLINE_TIMER)、[`CONFIG_APIC_TIMER_TSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_APIC_TIMER_TSC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_INTEL_ISH`。

<a id="CONFIG_LOAPIC_SPURIOUS_VECTOR"></a>

## 5.88 `CONFIG_LOAPIC_SPURIOUS_VECTOR`

**提示（Prompt）**：处理 LOAPIC 伪中断（Spurious Interrupt）

**说明（Help）**

当处理器将任务优先级提高到大于或等于当前使处理器 INTR 信号有效的中断级别时，可能出现一种特殊情况。如果在发出 INTA 周期时，原本应交付的中断已被软件编程屏蔽，本地 APIC（Local APIC）将交付一个伪中断向量（Spurious-interrupt Vector）。交付此向量不会影响 ISR，因此该向量的处理程序应直接返回，而不发送中断结束（End of Interrupt，EOI）。内容来自 x86 手册第 3 卷第 10.9 节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOAPIC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.loapic:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.loapic#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 本地高级可编程中断控制器（Local APIC，LOAPIC）

**配置项引用（Symbol References）**：[`CONFIG_LOAPIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_LOAPIC)。

<a id="CONFIG_LOAPIC_SPURIOUS_VECTOR_ID"></a>

## 5.89 `CONFIG_LOAPIC_SPURIOUS_VECTOR_ID`

**提示（Prompt）**：LOAPIC 伪中断向量 ID（Spurious Vector ID）

**说明（Help）**

用于 LOAPIC 伪中断（Spurious Interrupt）的中断描述符表（Interrupt Descriptor Table，IDT）向量。请注意，某些架构（P6、Pentium）忽略低 4 位并将其固定为 `0xF`。若保留该值为 `-1`，将使用 IDT 中的最后一个表项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOAPIC_SPURIOUS_VECTOR && CONFIG_LOAPIC
```

**默认值（Defaults）**

```text
-1
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.loapic:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.loapic#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 本地高级可编程中断控制器（Local APIC，LOAPIC） → 处理 LOAPIC 伪中断（Spurious Interrupt）

**配置项引用（Symbol References）**：[`CONFIG_LOAPIC_SPURIOUS_VECTOR`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_LOAPIC_SPURIOUS_VECTOR)、[`CONFIG_LOAPIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_LOAPIC)。

<a id="CONFIG_MAX32_RV32_INTC"></a>

## 5.90 `CONFIG_MAX32_RV32_INTC`

**提示（Prompt）**：MAX32 RV32 内核中断控制器（Interrupt Controller）驱动

**说明（Help）**

启用 MAX32 RV32 内核的中断控制器（Interrupt Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_RV32_INTC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.max32_rv32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.max32_rv32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_MAX_IRQ_PER_AGGREGATOR"></a>

## 5.91 `CONFIG_MAX_IRQ_PER_AGGREGATOR`

**提示（Prompt）**：每个中断聚合器（Interrupt Aggregator）的最大 IRQ 数

**说明（Help）**

系统中任一中断聚合器（Interrupt Aggregator）的最大中断输入数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_MCHP_ECIA_XEC"></a>

## 5.92 `CONFIG_MCHP_ECIA_XEC`

**提示（Prompt）**：MCHP MEC 系列 MCU 的外部 EC 中断聚合器（External EC Interrupt Aggregator，ECIA）驱动

**说明（Help）**

为 Microchip MEC 系列微控制器（MCU）启用 XEC ECIA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_ECIA_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.xec:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.xec#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_MULTI_LEVEL_INTERRUPTS"></a>

## 5.93 `CONFIG_MULTI_LEVEL_INTERRUPTS`

**提示（Prompt）**：多级中断支持（Multi-level Interrupt Support）

**说明（Help）**

多级中断（Multiple Levels of Interrupts）通常用于增加系统可寻址的中断数量。例如，使用两级时，第二级中断聚合器（Interrupt Aggregator）会将路由给它的所有中断合并成第一级中断控制器上的一根 IRQ 线。使用三级时，第三级聚合器会将其输入中断合并成第二级的一根 IRQ 线。中断级数通常由硬件决定。这里的“聚合器（Aggregator）”指“中断控制器（Interrupt Controller）”。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GEN_SW_ISR_TABLE
```

**被选择（Selected by）**

```text
CONFIG_INFINEON_INTC_SYSINTC
CONFIG_PLIC
CONFIG_RISCV_AIA
CONFIG_THEJAS32_INTC
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GEN_SW_ISR_TABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GEN_SW_ISR_TABLE)、[`CONFIG_INFINEON_INTC_SYSINTC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_INFINEON_INTC_SYSINTC)、[`CONFIG_PLIC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC)、[`CONFIG_RISCV_AIA`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RISCV_AIA)、[`CONFIG_THEJAS32_INTC`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_THEJAS32_INTC)。

<a id="CONFIG_NPCX_MIWU"></a>

## 5.94 `CONFIG_NPCX_MIWU`

**提示（Prompt）**：Nuvoton NPCX 嵌入式控制器（Embedded Controller，EC）的 MIWU 驱动

**说明（Help）**

此选项启用 NPCX 系列处理器的多输入唤醒单元（Multi-Input Wake-Up Unit，MIWU）驱动。GPIO、RTC、LPC/eSPI 中断支持需要此驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_MIWU_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.npcx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.npcx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

<a id="CONFIG_NPCX_MIWU_BOTH_EDGE_TRIG_WORKAROUND"></a>

## 5.95 `CONFIG_NPCX_MIWU_BOTH_EDGE_TRIG_WORKAROUND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

规避 npcx9m7fb SoC 勘误中的“MIWU 任意边沿触发条件（MIWU Any Edge Trigger Condition）”问题。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y if CONFIG_SOC_NPCX9M7FB
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.npcx:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.npcx#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NPCX9M7FB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NPCX9M7FB)。

<a id="CONFIG_NRFX_CLIC"></a>

## 5.96 `CONFIG_NRFX_CLIC`

**提示（Prompt）**：VPR 内核本地中断控制器（Core Local Interrupt Controller，CLIC）

**说明（Help）**

Nordic VPR 内核的中断控制器（Interrupt Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_CLIC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GEN_IRQ_VECTOR_TABLE
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.clic:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.clic#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GEN_IRQ_VECTOR_TABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GEN_IRQ_VECTOR_TABLE)。

<a id="CONFIG_NUCLEI_ECLIC"></a>

## 5.97 `CONFIG_NUCLEI_ECLIC`

**提示（Prompt）**：增强型内核本地中断控制器（Enhanced Core Local Interrupt Controller，ECLIC）

**说明（Help）**

Nuclei SoC 内核的中断控制器（Interrupt Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUCLEI_ECLIC_ENABLED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLIC
CONFIG_CLIC_SMCLICSHV_EXT if CONFIG_RISCV_VECTORED_MODE
CONFIG_CLIC_SMCLICCONFIG_EXT
CONFIG_LEGACY_CLIC_MEMORYMAP_ACCESS
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.clic:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.clic#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CLIC)、[`CONFIG_CLIC_SMCLICSHV_EXT`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CLIC_SMCLICSHV_EXT)、[`CONFIG_RISCV_VECTORED_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_VECTORED_MODE)、[`CONFIG_CLIC_SMCLICCONFIG_EXT`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_CLIC_SMCLICCONFIG_EXT)、[`CONFIG_LEGACY_CLIC_MEMORYMAP_ACCESS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_LEGACY_CLIC_MEMORYMAP_ACCESS)。

<a id="CONFIG_NUM_2ND_LEVEL_AGGREGATORS"></a>

## 5.98 `CONFIG_NUM_2ND_LEVEL_AGGREGATORS`

**提示（Prompt）**：第二级中断聚合器（Interrupt Aggregator）总数

**说明（Help）**

要支持的第二级中断聚合器（Interrupt Aggregator）数量。每个聚合器最多可以管理 `MAX_IRQ_PER_AGGREGATOR` 个第二级中断。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_2ND_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support） → 第二级中断支持（Second-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_2ND_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_2ND_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_NUM_3RD_LEVEL_AGGREGATORS"></a>

## 5.99 `CONFIG_NUM_3RD_LEVEL_AGGREGATORS`

**提示（Prompt）**：第三级中断聚合器（Interrupt Aggregator）总数

**说明（Help）**

要支持的第三级中断聚合器（Interrupt Aggregator）数量。每个聚合器最多可以管理 `MAX_IRQ_PER_AGGREGATOR` 个第三级中断。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_3RD_LEVEL_INTERRUPTS && CONFIG_MULTI_LEVEL_INTERRUPTS
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.multilevel:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.multilevel#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers） → 多级中断支持（Multi-level Interrupt Support） → 第三级中断支持（Third-level Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_3RD_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_3RD_LEVEL_INTERRUPTS)、[`CONFIG_MULTI_LEVEL_INTERRUPTS`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_MULTI_LEVEL_INTERRUPTS)。

<a id="CONFIG_NXP_GINT"></a>

## 5.100 `CONFIG_NXP_GINT`

**提示（Prompt）**：NXP MCU 的分组 GPIO 输入中断（Grouped GPIO Input Interrupt，GINT）控制器

**说明（Help）**

启用 NXP 微控制器（MCU）的 GINT 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_GINT_ENABLED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RESET
```

**定义位置（Location）**：[`drivers/interrupt_controller/Kconfig.nxp_gint:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/interrupt_controller/Kconfig.nxp_gint#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 中断控制器驱动（Interrupt Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)。

<!-- kconfig-navigation -->

[上一章](P004_Kconfig.zephyr_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P006_drivers_interrupt_controller_配置项参考_2.md)
