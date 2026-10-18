---
id: learning.zephyr-docs.kconfig-reference.page-7
title: "`drivers/timer`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第7章\_`drivers/timer`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `drivers/timer` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_AMBIQ_STIMER_TIMER"></a>

## 7.1 `CONFIG_AMBIQ_STIMER_TIMER`

**提示（Prompt）**：Ambiq STIMER 系统时钟驱动（System Clock Driver）

**说明（Help）**

Ambiq Apollo STIMER 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_STIMER_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_AMBIQ_HAL
CONFIG_TICKLESS_CAPABLE
CONFIG_AMBIQ_HAL_USE_STIMER
```

**定义位置（Location）**：[`drivers/timer/Kconfig.ambiq:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.ambiq#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_AMBIQ_HAL_USE_STIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_STIMER)。

<a id="CONFIG_AMD_TMRCTR"></a>

## 7.2 `CONFIG_AMD_TMRCTR`

**提示（Prompt）**：AMD AXI 定时器（Timer）

**说明（Help）**

此模块为 AMD AXI Timer IP 实现内核设备驱动（Kernel Device Driver）。驱动使用一个定时器通道作为时钟事件源（Clock Event Source），另一个通道作为时钟源（Clock Source），支持周期性（Periodic）和无滴答（Tickless）内核运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMD_XPS_TIMER_1_00_A_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
```

**定义位置（Location）**：[`drivers/timer/Kconfig.amd_tmrctr:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.amd_tmrctr#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)。

<a id="CONFIG_APIC_TIMER"></a>

## 7.3 `CONFIG_APIC_TIMER`

**提示（Prompt）**：本地 APIC 定时器（Local APIC Timer）

**说明（Help）**

将 x86 本地 APIC 的周期模式（Periodic Mode）用作系统时间源（System Time Source）。注意：除较旧或特殊硬件，以及未完整模拟 APIC 的 QEMU 等环境外，这通常不是合适的选择。现代硬件使用 `CONFIG_APIC_TSC_DEADLINE_TIMER` 会更好。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_LOAPIC
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
CONFIG_SYSTEM_CLOCK_LOCK_FREE_COUNT
```

**定义位置（Location）**：[`drivers/timer/Kconfig.x86:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.x86#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → 默认系统定时器（Default System Timer）

**配置项引用（Symbol References）**：[`CONFIG_LOAPIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_LOAPIC)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)、[`CONFIG_SYSTEM_CLOCK_LOCK_FREE_COUNT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_CLOCK_LOCK_FREE_COUNT)。

<a id="CONFIG_APIC_TIMER_IRQ"></a>

## 7.4 `CONFIG_APIC_TIMER_IRQ`

**提示（Prompt）**：本地 APIC 定时器 IRQ（Local APIC Timer IRQ）

**说明（Help）**

此选项指定本地 APIC 定时器（Local APIC Timer）使用的 IRQ。注意：必须将其设置为紧接最后一个 IO-APIC IRQ 之后的索引，因为定时器是 APIC 本地向量表（Local Vector Table）的第一个表项。这种容易出错的设置本意并不是供用户配置的，而且几乎肯定应通过其他机制来管理。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_APIC_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
24
```

**定义位置（Location）**：[`drivers/timer/Kconfig.x86:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.x86#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_APIC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_APIC_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_APIC_TIMER_IRQ_PRIORITY"></a>

## 7.5 `CONFIG_APIC_TIMER_IRQ_PRIORITY`

**提示（Prompt）**：本地 APIC 定时器中断优先级（Interrupt Priority）

**说明（Help）**

此选项指定本地 APIC 定时器（Local APIC Timer）使用的中断优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_APIC_TIMER || CONFIG_APIC_TSC_DEADLINE_TIMER || CONFIG_APIC_TIMER_TSC) && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/timer/Kconfig.x86:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.x86#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_APIC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_APIC_TIMER)、[`CONFIG_APIC_TSC_DEADLINE_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_APIC_TSC_DEADLINE_TIMER)、[`CONFIG_APIC_TIMER_TSC`](P007_drivers_timer_配置项参考_1.md#CONFIG_APIC_TIMER_TSC)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_APIC_TIMER_TSC"></a>

## 7.6 `CONFIG_APIC_TIMER_TSC`

**提示（Prompt）**：使用 TSC 时间源（Time Source）的本地 APIC 定时器

**说明（Help）**

如果 CPU 支持恒定时间戳计数器（Invariant TSC），但不支持 TSC 截止时间（TSC Deadline）功能，此选项将使用 TSC 作为时间源（Time Source），并以单次模式（One-shot Mode）的本地 APIC 作为超时事件源（Timeout Event Source）。必须知道 TSC 频率与本地 APIC 定时器频率的比值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SMP && <choice>
```

**主动选择（Selects）**

```text
CONFIG_LOAPIC
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
```

**定义位置（Location）**：[`drivers/timer/Kconfig.x86:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.x86#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → 默认系统定时器（Default System Timer）

**配置项引用（Symbol References）**：[`CONFIG_SMP`](P002_kernel_配置项参考_2.md#CONFIG_SMP)、[`CONFIG_LOAPIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_LOAPIC)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)。

<a id="CONFIG_APIC_TIMER_TSC_M"></a>

## 7.7 `CONFIG_APIC_TIMER_TSC_M`

**提示（Prompt）**：TSC 到本地 APIC 定时器频率的除数（Divisor，M）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_APIC_TIMER_TSC && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/timer/Kconfig.x86:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.x86#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_APIC_TIMER_TSC`](P007_drivers_timer_配置项参考_1.md#CONFIG_APIC_TIMER_TSC)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_APIC_TIMER_TSC_N"></a>

## 7.8 `CONFIG_APIC_TIMER_TSC_N`

**提示（Prompt）**：TSC 到本地 APIC 定时器频率的乘数（Multiplier，N）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_APIC_TIMER_TSC && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/timer/Kconfig.x86:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.x86#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_APIC_TIMER_TSC`](P007_drivers_timer_配置项参考_1.md#CONFIG_APIC_TIMER_TSC)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_APIC_TSC_DEADLINE_TIMER"></a>

## 7.9 `CONFIG_APIC_TSC_DEADLINE_TIMER`

**提示（Prompt）**：使用 TSC 截止时间模式（TSC Deadline Mode）的本地 APIC 定时器

**说明（Help）**

基于本地 APIC TSC 截止时间（TSC Deadline）功能的极简定时器驱动。使用带比较器的自由运行 64 位计数器（Free-running 64-bit Counter），几乎消除了处理中的所有边界情况；接近指令周期的分辨率，可在需要时提供实际上不受限的精度，此时限制来自 CPU 执行计时逻辑所花费的时间。它支持对称多处理（SMP）安全运行，且速度很快；对于任何支持恒定 TSC（Invariant TSC）和 TSC 截止时间功能的 x86 设备，都应优先选择此驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_LOAPIC
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
```

**定义位置（Location）**：[`drivers/timer/Kconfig.x86:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.x86#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → 默认系统定时器（Default System Timer）

**配置项引用（Symbol References）**：[`CONFIG_LOAPIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_LOAPIC)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)。

<a id="CONFIG_ARCV2_TIMER"></a>

## 7.10 `CONFIG_ARCV2_TIMER`

**提示（Prompt）**：ARC 定时器（Timer）

**说明（Help）**

此模块为 ARCv2 处理器定时器 0 实现内核设备驱动（Kernel Device Driver），并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARC && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.arcv2:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.arcv2#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARC)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_ARCV2_TIMER_IRQ_PRIORITY"></a>

## 7.11 `CONFIG_ARCV2_TIMER_IRQ_PRIORITY`

**提示（Prompt）**：ARC 定时器中断优先级（Interrupt Priority）

**说明（Help）**

此选项指定 ARC 定时器使用的 IRQ 优先级（Priority）。数值越小，优先级越高。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCV2_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/timer/Kconfig.arcv2:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.arcv2#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → ARC 定时器（Timer）

**配置项引用（Symbol References）**：[`CONFIG_ARCV2_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_ARCV2_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_ARM_ARCH_TIMER"></a>

## 7.12 `CONFIG_ARM_ARCH_TIMER`

**提示（Prompt）**：ARM 架构定义的定时器（Architected Timer）

**说明（Help）**

此模块为 ARM 架构定义的定时器（Architected Timer）实现内核设备驱动。该定时器为每个 CPU 提供连接到 GIC 的定时器，通过私有外设中断（Private Peripheral Interrupt，PPI）交付各处理器的中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_GIC || CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER) && CONFIG_SYS_CLOCK_EXISTS
```

**主动选择（Selects）**

```text
CONFIG_ARCH_HAS_CUSTOM_BUSY_WAIT
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
```

**被选择（Selected by）**

```text
CONFIG_SOC_SUN8I_H3
CONFIG_SOC_R8A77951_A57
CONFIG_SOC_R8A77961
CONFIG_SOC_R8A779F0_R52
CONFIG_SOC_R8A779F0_A55
CONFIG_SOC_R8A779G0_R52
CONFIG_SOC_R8A779G0_A76
CONFIG_SOC_R8A78000_R52
CONFIG_SOC_R8A78000_A720
CONFIG_SOC_SUN50I_H618
CONFIG_SOC_BCM2712
CONFIG_SOC_BCM58402_A72
CONFIG_SOC_BCM2711
CONFIG_SOC_SERIES_AM62LX_A53
CONFIG_SOC_SERIES_AM62X_A53
CONFIG_SOC_MIMX8MM6_A53
CONFIG_SOC_MIMX8ML8_A53
CONFIG_SOC_MIMX8MN6_A53
CONFIG_SOC_MIMX9111
CONFIG_SOC_MIMX9131
CONFIG_SOC_MIMX9352_A55
CONFIG_SOC_MIMX94398_A55
CONFIG_SOC_MIMX9596_A55
CONFIG_SOC_MIMX9529_A55
CONFIG_SOC_BCM2710
CONFIG_SOC_XILINX_ZYNQMP_APU
CONFIG_SOC_VERSAL_APU
CONFIG_SOC_FAMILY_ENSEMBLE_APSS
CONFIG_SOC_SERIES_RZA3M
CONFIG_SOC_SERIES_RZA3UL
CONFIG_SOC_SERIES_RZN2H
CONFIG_SOC_SERIES_RZN2L
CONFIG_SOC_SERIES_RZT2H
CONFIG_SOC_SERIES_RZT2L
CONFIG_SOC_SERIES_RZT2M
CONFIG_SOC_R9A09G057H44GBG_CR8
CONFIG_SOC_RK3399
CONFIG_SOC_RK3568
CONFIG_SOC_RK3588
CONFIG_SOC_RK3588S
CONFIG_SOC_RV1106
CONFIG_SOC_AMD_VERSALNET_RPU
CONFIG_SOC_AMD_VERSALNET_APU
CONFIG_SOC_AMD_VERSAL2_RPU
CONFIG_SOC_AMD_VERSAL2_APU
CONFIG_SOC_LS1046A
CONFIG_SOC_SERIES_STM32MP13X
CONFIG_SOC_AN536
CONFIG_SOC_XENVM
CONFIG_SOC_QNXHV_VM
CONFIG_SOC_S32K566_R52
CONFIG_SOC_SERIES_S32ZE
CONFIG_SOC_MT8188_A55
```

**定义位置（Location）**：[`drivers/timer/Kconfig.arm_arch:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.arm_arch#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GIC)、[`CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_CUSTOM_INTERRUPT_CONTROLLER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_ARCH_HAS_CUSTOM_BUSY_WAIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_CUSTOM_BUSY_WAIT)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)、[`CONFIG_SOC_SUN8I_H3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SUN8I_H3)、[`CONFIG_SOC_R8A77951_A57`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A77951_A57)、[`CONFIG_SOC_R8A77961`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A77961)、[`CONFIG_SOC_R8A779F0_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A779F0_R52)、[`CONFIG_SOC_R8A779F0_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A779F0_A55)、[`CONFIG_SOC_R8A779G0_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A779G0_R52)、[`CONFIG_SOC_R8A779G0_A76`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A779G0_A76)、[`CONFIG_SOC_R8A78000_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A78000_R52)、[`CONFIG_SOC_R8A78000_A720`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R8A78000_A720)、[`CONFIG_SOC_SUN50I_H618`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SUN50I_H618)、[`CONFIG_SOC_BCM2712`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM2712)、[`CONFIG_SOC_BCM58402_A72`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM58402_A72)、[`CONFIG_SOC_BCM2711`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM2711)、[`CONFIG_SOC_SERIES_AM62LX_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62LX_A53)、[`CONFIG_SOC_SERIES_AM62X_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AM62X_A53)、[`CONFIG_SOC_MIMX8MM6_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MM6_A53)、[`CONFIG_SOC_MIMX8ML8_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8ML8_A53)、[`CONFIG_SOC_MIMX8MN6_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX8MN6_A53)、[`CONFIG_SOC_MIMX9111`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9111)、[`CONFIG_SOC_MIMX9131`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9131)、[`CONFIG_SOC_MIMX9352_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9352_A55)、[`CONFIG_SOC_MIMX94398_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX94398_A55)、[`CONFIG_SOC_MIMX9596_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9596_A55)、[`CONFIG_SOC_MIMX9529_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MIMX9529_A55)、[`CONFIG_SOC_BCM2710`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_BCM2710)、[`CONFIG_SOC_XILINX_ZYNQMP_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XILINX_ZYNQMP_APU)、[`CONFIG_SOC_VERSAL_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VERSAL_APU)、[`CONFIG_SOC_FAMILY_ENSEMBLE_APSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ENSEMBLE_APSS)、[`CONFIG_SOC_SERIES_RZA3M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZA3M)、[`CONFIG_SOC_SERIES_RZA3UL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZA3UL)、[`CONFIG_SOC_SERIES_RZN2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2H)、[`CONFIG_SOC_SERIES_RZN2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2L)、[`CONFIG_SOC_SERIES_RZT2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2H)、[`CONFIG_SOC_SERIES_RZT2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2L)、[`CONFIG_SOC_SERIES_RZT2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2M)、[`CONFIG_SOC_R9A09G057H44GBG_CR8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_R9A09G057H44GBG_CR8)、[`CONFIG_SOC_RK3399`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RK3399)、[`CONFIG_SOC_RK3568`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RK3568)、[`CONFIG_SOC_RK3588`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RK3588)、[`CONFIG_SOC_RK3588S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RK3588S)、[`CONFIG_SOC_RV1106`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RV1106)、[`CONFIG_SOC_AMD_VERSALNET_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET_RPU)、[`CONFIG_SOC_AMD_VERSALNET_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSALNET_APU)、[`CONFIG_SOC_AMD_VERSAL2_RPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2_RPU)、[`CONFIG_SOC_AMD_VERSAL2_APU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AMD_VERSAL2_APU)、[`CONFIG_SOC_LS1046A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LS1046A)、[`CONFIG_SOC_SERIES_STM32MP13X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32MP13X)、[`CONFIG_SOC_AN536`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AN536)、[`CONFIG_SOC_XENVM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_XENVM)、[`CONFIG_SOC_QNXHV_VM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QNXHV_VM)、[`CONFIG_SOC_S32K566_R52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_S32K566_R52)、[`CONFIG_SOC_SERIES_S32ZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32ZE)、[`CONFIG_SOC_MT8188_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8188_A55)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_GIC`、`CONFIG_SOC_SUN8I_H3`、`CONFIG_SOC_R8A779G0_R52`、`CONFIG_SOC_R8A779G0_A76`、`CONFIG_SOC_SUN50I_H618`、`CONFIG_SOC_BCM2712`、`CONFIG_SOC_BCM2711`、`CONFIG_SOC_BCM2710`、`CONFIG_SOC_FAMILY_ENSEMBLE_APSS`、`CONFIG_SOC_RK3399`、`CONFIG_SOC_RK3568`、`CONFIG_SOC_RK3588`、`CONFIG_SOC_RK3588S`、`CONFIG_SOC_RV1106`、`CONFIG_SOC_SERIES_STM32MP13X`、`CONFIG_SOC_AN536`、`CONFIG_SOC_XENVM`、`CONFIG_SOC_QNXHV_VM`、`CONFIG_SOC_S32K566_R52`、`CONFIG_SOC_SERIES_S32ZE`。

<a id="CONFIG_ARM_ARCH_TIMER_ERRATUM_740657"></a>

## 7.13 `CONFIG_ARM_ARCH_TIMER_ERRATUM_740657`

**提示（Prompt）**：ARM 架构定时器受 ARM 勘误（Erratum）740657 影响

**说明（Help）**

此选项表示目标硬件中的 ARM 架构定义的定时器（Architected Timer）实现受 ARM 勘误（Erratum）740657 影响，参见 ARM Cortex-A9 处理器《软件开发者勘误通知（Software Developers Errata Notice）》，ARM 文档 ID032315。该问题会在每次实际定时器中断时产生额外的伪中断指示（Spurious Interrupt Indication）。此选项启用定时器驱动内针对该勘误的规避措施（Workaround）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_ARCH_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_XC7ZXXX
CONFIG_SOC_SERIES_XC7ZXXXS
CONFIG_SOC_SERIES_CYCLONEV
```

**定义位置（Location）**：[`drivers/timer/Kconfig.arm_arch:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.arm_arch#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → ARM 架构定义的定时器（Architected Timer）

**配置项引用（Symbol References）**：[`CONFIG_ARM_ARCH_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_ARM_ARCH_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_SOC_SERIES_XC7ZXXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XC7ZXXX)、[`CONFIG_SOC_SERIES_XC7ZXXXS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_XC7ZXXXS)、[`CONFIG_SOC_SERIES_CYCLONEV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYCLONEV)。

<a id="CONFIG_AURIX_STM"></a>

## 7.14 `CONFIG_AURIX_STM`

**提示（Prompt）**：AURIX 系统定时器模块（System Timer Module，STM）支持

**说明（Help）**

此选项为 TC3X 和 TC4X 器件上的 Infineon AURIX 系统定时器模块（System Timer Module）启用系统定时器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_TC3X || CONFIG_SOC_SERIES_TC4X) && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT
CONFIG_SYSTEM_CLOCK_LOCK_FREE_COUNT
```

**定义位置（Location）**：[`drivers/timer/Kconfig.infineon_aurix_stm:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.infineon_aurix_stm#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_TC3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TC3X)、[`CONFIG_SOC_SERIES_TC4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TC4X)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)、[`CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT)、[`CONFIG_SYSTEM_CLOCK_LOCK_FREE_COUNT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_CLOCK_LOCK_FREE_COUNT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_TC3X`、`CONFIG_SOC_SERIES_TC4X`。

<a id="CONFIG_CAVS_TIMER"></a>

## 7.15 `CONFIG_CAVS_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`INTEL_ADSP_TIMER` 的临时别名（Temporary Alias）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SYS_CLOCK_EXISTS
```

**被选择（Selected by）**

```text
CONFIG_INTEL_ADSP_TIMER
```

**定义位置（Location）**：[`drivers/timer/Kconfig.cavs:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.cavs#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_INTEL_ADSP_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_INTEL_ADSP_TIMER)。

<a id="CONFIG_CC13XX_CC26XX_RTC_TIMER"></a>

## 7.16 `CONFIG_CC13XX_CC26XX_RTC_TIMER`

**提示（Prompt）**：TI SimpleLink CC13xx/CC26xx RTC 系统时钟定时器（System Clock Timer）

**说明（Help）**

此模块为 TI SimpleLink CC13XX_CC26XX 系列实时计数器（Real Time Counter）实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC13XX_CC26XX_RTC_TIMER_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
```

**定义位置（Location）**：[`drivers/timer/Kconfig.cc13xx_cc26xx_rtc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.cc13xx_cc26xx_rtc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)。

<a id="CONFIG_CC23X0_RTC_TIMER"></a>

## 7.17 `CONFIG_CC23X0_RTC_TIMER`

**提示（Prompt）**：RTC 定时器（Timer）

**说明（Help）**

此模块为 TI SimpleLink CC23X0 器件提供以 RTC 实现的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.cc23x0:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.cc23x0#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → TI SimpleLink CC23X 默认系统定时器（Default System Timer）

**配置项引用（Symbol References）**：[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_CC23X0_SYSTIM_TIMER"></a>

## 7.18 `CONFIG_CC23X0_SYSTIM_TIMER`

**提示（Prompt）**：SYSTIM 定时器（Timer）

**说明（Help）**

此模块为 TI SimpleLink CC23X0 器件提供以 SYSTIM 实现的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.cc23x0:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.cc23x0#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → TI SimpleLink CC23X 默认系统定时器（Default System Timer）

**配置项引用（Symbol References）**：[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_CH32V00X_SYSTICK"></a>

## 7.19 `CONFIG_CH32V00X_SYSTICK`

**提示（Prompt）**：CH32V QingKe 内核 SysTick 定时器（Timer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_QINGKE_V2A || CONFIG_SOC_SERIES_QINGKE_V2C || CONFIG_SOC_SERIES_QINGKE_V3A || CONFIG_SOC_SERIES_QINGKE_V3C || CONFIG_SOC_SERIES_QINGKE_V4B || CONFIG_SOC_SERIES_QINGKE_V4C || CONFIG_SOC_SERIES_QINGKE_V4F || CONFIG_SOC_SERIES_CH32H41X) && DT_HAS_WCH_SYSTICK_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_CH32V
```

**定义位置（Location）**：[`drivers/timer/Kconfig.wch_ch32v00x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.wch_ch32v00x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_QINGKE_V2A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_QINGKE_V2A)、[`CONFIG_SOC_SERIES_QINGKE_V2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_QINGKE_V2C)、[`CONFIG_SOC_SERIES_QINGKE_V3A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_QINGKE_V3A)、[`CONFIG_SOC_SERIES_QINGKE_V3C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_QINGKE_V3C)、[`CONFIG_SOC_SERIES_QINGKE_V4B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_QINGKE_V4B)、[`CONFIG_SOC_SERIES_QINGKE_V4C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_QINGKE_V4C)、[`CONFIG_SOC_SERIES_QINGKE_V4F`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_QINGKE_V4F)、[`CONFIG_SOC_SERIES_CH32H41X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CH32H41X)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_SOC_FAMILY_CH32V`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_CH32V)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_QINGKE_V2A`、`CONFIG_SOC_SERIES_QINGKE_V2C`、`CONFIG_SOC_SERIES_QINGKE_V3A`、`CONFIG_SOC_SERIES_QINGKE_V3C`、`CONFIG_SOC_SERIES_QINGKE_V4B`、`CONFIG_SOC_SERIES_QINGKE_V4C`、`CONFIG_SOC_SERIES_QINGKE_V4F`、`CONFIG_SOC_SERIES_CH32H41X`、`CONFIG_SOC_FAMILY_CH32V`。

<a id="CONFIG_CMSDK_APB_TIMER"></a>

## 7.20 `CONFIG_CMSDK_APB_TIMER`

**提示（Prompt）**：将 CMSDK APB 定时器（Timer）用作系统时钟

**说明（Help）**

启用将 CMSDK APB 定时器（Timer）作为系统时钟（System Clock）的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.cmsdk_apb_timer:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.cmsdk_apb_timer#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_CMSDK_APB_TIMER_MIN_DELAY_CYCLES"></a>

## 7.21 `CONFIG_CMSDK_APB_TIMER_MIN_DELAY_CYCLES`

**提示（Prompt）**：最小延迟周期数（Minimum Delay Cycles）

**说明（Help）**

设置的值将覆盖默认的最小延迟周期数（Minimum Delay Cycles）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSDK_APB_TIMER_MIN_DELAY_OVERRIDE && CONFIG_CMSDK_APB_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/timer/Kconfig.cmsdk_apb_timer:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.cmsdk_apb_timer#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → 将 CMSDK APB 定时器（Timer）用作系统时钟 → 覆盖最小延迟周期数（Minimum Delay Cycles）

**配置项引用（Symbol References）**：[`CONFIG_CMSDK_APB_TIMER_MIN_DELAY_OVERRIDE`](P007_drivers_timer_配置项参考_1.md#CONFIG_CMSDK_APB_TIMER_MIN_DELAY_OVERRIDE)、[`CONFIG_CMSDK_APB_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_CMSDK_APB_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_CMSDK_APB_TIMER_MIN_DELAY_OVERRIDE"></a>

## 7.22 `CONFIG_CMSDK_APB_TIMER_MIN_DELAY_OVERRIDE`

**提示（Prompt）**：覆盖最小延迟周期数（Minimum Delay Cycles）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CMSDK_APB_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**定义位置（Location）**：[`drivers/timer/Kconfig.cmsdk_apb_timer:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.cmsdk_apb_timer#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → 将 CMSDK APB 定时器（Timer）用作系统时钟

**配置项引用（Symbol References）**：[`CONFIG_CMSDK_APB_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_CMSDK_APB_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_CORTEX_M_SYSTICK"></a>

## 7.23 `CONFIG_CORTEX_M_SYSTICK`

**提示（Prompt）**：Cortex-M SYSTICK 定时器（Timer）

**说明（Help）**

此模块为 Cortex-M 处理器的 SYSTICK 定时器实现内核设备驱动（Kernel Device Driver），并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M_HAS_SYSTICK && (DT_HAS_ARM_ARMV6M_SYSTICK_ENABLED || DT_HAS_ARM_ARMV7M_SYSTICK_ENABLED || DT_HAS_ARM_ARMV8M_SYSTICK_ENABLED || DT_HAS_ARM_ARMV8_1M_SYSTICK_ENABLED) && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT
CONFIG_SYSTEM_TIMER_HAS_LPM_COMPANION_SUPPORT
CONFIG_CORTEX_M_SYSTICK_INSTALL_ISR
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_M46X
CONFIG_SOC_SERIES_NPCM4
```

**定义位置（Location）**：[`drivers/timer/Kconfig.cortex_m_systick:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.cortex_m_systick#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M_HAS_SYSTICK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M_HAS_SYSTICK)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT)、[`CONFIG_SYSTEM_TIMER_HAS_LPM_COMPANION_SUPPORT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_HAS_LPM_COMPANION_SUPPORT)、[`CONFIG_CORTEX_M_SYSTICK_INSTALL_ISR`](P007_drivers_timer_配置项参考_1.md#CONFIG_CORTEX_M_SYSTICK_INSTALL_ISR)、[`CONFIG_SOC_SERIES_M46X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_M46X)、[`CONFIG_SOC_SERIES_NPCM4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NPCM4)。

<a id="CONFIG_CORTEX_M_SYSTICK_64BIT_CYCLE_COUNTER"></a>

## 7.24 `CONFIG_CORTEX_M_SYSTICK_64BIT_CYCLE_COUNTER`

**提示（Prompt）**：支持 `sys_clock_cycle_get_64()` 的 Cortex-M SYSTICK 定时器

**说明（Help）**

通用定时器核心（Generic Timer Core）会基于自身的通告基准（Announce Baseline），扩展此驱动的 32 位软件周期计数（Software Cycle Count），因此无论是否设置此选项，`sys_clock_cycle_get_64()` 都可用。此选项额外告知系统的其余部分：有一个可供使用的 64 位周期计数器（Cycle Counter）；在 32 位计数器很快回绕时，这样做很有价值。当硬件时钟快到使 `sys_clock_cycle_get_32()` 大约在一分钟内或更短时间内回绕时，此选项默认设为 `y`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CORTEX_M_SYSTICK && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y if CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC > 60000000
```

**主动选择（Selects）**

```text
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
```

**定义位置（Location）**：[`drivers/timer/Kconfig.cortex_m_systick:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.cortex_m_systick#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CORTEX_M_SYSTICK`](P007_drivers_timer_配置项参考_1.md#CONFIG_CORTEX_M_SYSTICK)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)。

<a id="CONFIG_CORTEX_M_SYSTICK_INSTALL_ISR"></a>

## 7.25 `CONFIG_CORTEX_M_SYSTICK_INSTALL_ISR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

基于 SysTick 的驱动应选择此选项，以便安装 `sys_clock_isr()` 函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M_HAS_SYSTICK && CONFIG_SYS_CLOCK_EXISTS
```

**被选择（Selected by）**

```text
CONFIG_CORTEX_M_SYSTICK
```

**定义位置（Location）**：[`drivers/timer/Kconfig.cortex_m_systick:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.cortex_m_systick#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M_HAS_SYSTICK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M_HAS_SYSTICK)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_CORTEX_M_SYSTICK`](P007_drivers_timer_配置项参考_1.md#CONFIG_CORTEX_M_SYSTICK)。

<a id="CONFIG_CORTEX_M_SYSTICK_INTERRUPT_PRIORITY"></a>

## 7.26 `CONFIG_CORTEX_M_SYSTICK_INTERRUPT_PRIORITY`

**提示（Prompt）**：Cortex-M SYSTICK 定时器中断优先级（Interrupt Priority）

**说明（Help）**

此选项指定 Cortex-M SysTick 定时器使用的中断优先级（Interrupt Priority），表示方式与传给 `IRQ_CONNECT()` 的其他优先级相同：`0` 是最紧急的内核级别，内核保留级偏移量 `_IRQ_PRIO_OFFSET` 会在内部应用。有效值从 `0` 到目标内核可用的最低 IRQ 优先级 `IRQ_PRIO_LOWEST`。默认值 `0` 保留历史行为，即让 SysTick 在最高的可屏蔽／内核 IRQ 优先级运行。

警告：SysTick 驱动的计时（Timekeeping）代码只允许相邻两次更新之间最多发生一次计数器回绕（Counter Wrap）。除非通过 systick 节点上的 `zephyr,min-timeout-cycles` 覆盖，否则最小超时采用固定 10 µs 的预算 `SYSTICK_MIN_DELAY_US`，按实际时钟频率换算成周期数，且下限为两个周期。如果 SysTick 中断被延后超过一个回绕周期，就会静默丢失整整 `last_load` 对应的运行时间（Uptime），不会产生任何诊断。增大优先级数值，即降低 SysTick 的优先级，可以减少对更高优先级中断的延迟影响，但也会使 SysTick 的最坏延后时间等于系统中所有更高优先级中断的总嵌套运行时间。因此，只有该最坏延后时间仍短于回绕周期时，这样做才安全。

重要：实际使用中，任何非默认值都必须配合 systick 节点上更大的 `zephyr,min-timeout-cycles`，使最小超时以及由此决定的回绕周期能够覆盖最坏延后时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CORTEX_M_SYSTICK && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/timer/Kconfig.cortex_m_systick:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.cortex_m_systick#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CORTEX_M_SYSTICK`](P007_drivers_timer_配置项参考_1.md#CONFIG_CORTEX_M_SYSTICK)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_COUNTER"></a>

## 7.27 `CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_COUNTER`

**提示（Prompt）**：SysTick 低功耗模式定时器（LPM Timer）：计数器（Counter）［已弃用］

**说明（Help）**

已弃用（Deprecated）。请改用 `CONFIG_SYSTEM_TIMER_LPM_COMPANION_COUNTER`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CORTEX_M_SYSTICK && CONFIG_SYS_CLOCK_EXISTS
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/timer/Kconfig.cortex_m_systick:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.cortex_m_systick#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CORTEX_M_SYSTICK`](P007_drivers_timer_配置项参考_1.md#CONFIG_CORTEX_M_SYSTICK)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_HOOKS"></a>

## 7.28 `CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_HOOKS`

**提示（Prompt）**：SysTick 低功耗模式定时器（LPM Timer）：钩子（Hooks）［已弃用］

**说明（Help）**

已弃用（Deprecated）。请改用 `CONFIG_SYSTEM_TIMER_LPM_COMPANION_HOOKS`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CORTEX_M_SYSTICK && CONFIG_SYS_CLOCK_EXISTS
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/timer/Kconfig.cortex_m_systick:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.cortex_m_systick#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CORTEX_M_SYSTICK`](P007_drivers_timer_配置项参考_1.md#CONFIG_CORTEX_M_SYSTICK)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_NONE"></a>

## 7.29 `CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_NONE`

**提示（Prompt）**：SysTick 低功耗模式定时器（LPM Timer）：无（None）［已弃用］

**说明（Help）**

已弃用（Deprecated）。请改用 `CONFIG_SYSTEM_TIMER_LPM_COMPANION_NONE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CORTEX_M_SYSTICK && CONFIG_SYS_CLOCK_EXISTS
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/timer/Kconfig.cortex_m_systick:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.cortex_m_systick#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CORTEX_M_SYSTICK`](P007_drivers_timer_配置项参考_1.md#CONFIG_CORTEX_M_SYSTICK)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_CORTEX_M_SYSTICK_RESET_BY_LPM"></a>

## 7.30 `CONFIG_CORTEX_M_SYSTICK_RESET_BY_LPM`

**提示（Prompt）**：SysTick 被低功耗模式（LPM）复位［已弃用］

**说明（Help）**

已弃用（Deprecated）。请改用 `CONFIG_SYSTEM_TIMER_RESET_BY_LPM`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CORTEX_M_SYSTICK && CONFIG_SYS_CLOCK_EXISTS
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
CONFIG_SYSTEM_TIMER_RESET_BY_LPM
```

**定义位置（Location）**：[`drivers/timer/Kconfig.cortex_m_systick:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.cortex_m_systick#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CORTEX_M_SYSTICK`](P007_drivers_timer_配置项参考_1.md#CONFIG_CORTEX_M_SYSTICK)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)、[`CONFIG_SYSTEM_TIMER_RESET_BY_LPM`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_RESET_BY_LPM)。

<a id="CONFIG_ESP32_SYS_TIMER"></a>

## 7.31 `CONFIG_ESP32_SYS_TIMER`

**提示（Prompt）**：ESP32 系统定时器（Sys-timer）支持（ESP32Cx 系列）

**说明（Help）**

此选项为 Espressif ESP32Cx 启用系统定时器驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C3 || (CONFIG_SOC_SERIES_ESP32C5 && !CONFIG_SOC_ESP32C5_LPCORE) || CONFIG_SOC_SERIES_ESP32C61 || (CONFIG_SOC_SERIES_ESP32C6 && !CONFIG_SOC_ESP32C6_LPCORE) || CONFIG_SOC_SERIES_ESP32H2 || (CONFIG_SOC_SERIES_ESP32P4 && !CONFIG_SOC_ESP32P4_LPCORE)) && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT if CONFIG_MCUBOOT
```

**定义位置（Location）**：[`drivers/timer/Kconfig.esp32:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.esp32#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_ESP32C5_LPCORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32C5_LPCORE)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_ESP32C6_LPCORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32C6_LPCORE)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_ESP32P4_LPCORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32P4_LPCORE)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)、[`CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT)、[`CONFIG_MCUBOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUBOOT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_SERIES_ESP32P4`。

<a id="CONFIG_GECKO_BURTC_TIMER"></a>

## 7.32 `CONFIG_GECKO_BURTC_TIMER`

**提示（Prompt）**：SiLabs Gecko BURTC 系统时钟驱动（System Clock Driver）

**说明（Help）**

启用后，将使用 BURTC 代替 Cortex-M SysTick 来提供 `hw_cycles` 和内核滴答（Kernel Tick）。系统若要在 EM2 和 EM3 休眠状态下保持时间跟踪并唤醒，就需要此选项。

注意：使用 BURTC 代替 SysTick 会显著影响内核计时精度。

1. 无法使用通常具有 0.1 ms 粒度的无滴答调度（Tickless Scheduling）。内核滴答时长应至少为 6 个 BURTC 时钟周期，即在 32768 Hz（LFXO、LFRCO）下约为 183 µs，在 1000 Hz（ULFRCO）下约为 6 ms。
2. 总体上，内核实时调度（Real-time Scheduling）的准确性会降低：定时器、可延迟工作（Delayable Work）、`k_sleep` 等所有基于超时的机制，在线程唤醒时的精确程度都低于使用 SysTick 定时器时。
3. `hw_cycles` 粒度将等于 1 个 BURTC 时钟周期，即在 32768 Hz 下约为 31 µs，在 1000 Hz 下约为 1 ms。这会降低所有依赖周期 API（Cycles API）的代码的计时精度，例如使用 `k_cycle_get_32()` 及类似函数的代码。

如不确定，选择 `N`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_SILABS_S2 && DT_HAS_SILABS_GECKO_BURTC_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_BURTC
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME
```

**定义位置（Location）**：[`drivers/timer/Kconfig.gecko:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.gecko#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_SILABS_SISDK_BURTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_BURTC)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="CONFIG_HEXAGON_TIMER"></a>

## 7.33 `CONFIG_HEXAGON_TIMER`

**提示（Prompt）**：Hexagon 虚拟机（VM）定时器驱动

**说明（Help）**

此选项启用 Hexagon 虚拟机（VM）定时器驱动，为系统时钟和计时服务提供支持。该驱动采用无滴答（Tickless）方式：通过 H2 `vmtimerop` 接口设置绝对截止时间（Absolute Deadline），并通过通用系统定时器核心（Generic System-timer Core）进行滴答计数统计。其计数器速率在启动时向虚拟机监控器（Hypervisor）查询。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HEXAGON && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME
```

**定义位置（Location）**：[`drivers/timer/Kconfig.hexagon:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.hexagon#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HEXAGON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HEXAGON)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)、[`CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME)。

<a id="CONFIG_HEXAGON_TIMER_IRQ"></a>

## 7.34 `CONFIG_HEXAGON_TIMER_IRQ`

**提示（Prompt）**：定时器中断号（Interrupt Number）

**说明（Help）**

Hexagon 系统定时器的中断号。在 H2 下，定时器向客户机（Guest）投递虚拟中断 12，即 `H2K_TIME_GUESTINT`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HEXAGON_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
12
```

**定义位置（Location）**：[`drivers/timer/Kconfig.hexagon:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.hexagon#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → Hexagon 虚拟机（VM）定时器驱动

**配置项引用（Symbol References）**：[`CONFIG_HEXAGON_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_HEXAGON_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_HEXAGON_TIMER_PRIORITY"></a>

## 7.35 `CONFIG_HEXAGON_TIMER_PRIORITY`

**提示（Prompt）**：定时器中断优先级（Interrupt Priority）

**说明（Help）**

Hexagon 系统定时器的中断优先级（Interrupt Priority）。数值越小，优先级越高。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HEXAGON_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/timer/Kconfig.hexagon:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.hexagon#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → Hexagon 虚拟机（VM）定时器驱动

**配置项引用（Symbol References）**：[`CONFIG_HEXAGON_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_HEXAGON_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_HPET_TIMER"></a>

## 7.36 `CONFIG_HPET_TIMER`

**提示（Prompt）**：高精度事件定时器（HPET）

**说明（Help）**

此选项选择高精度事件定时器（High Precision Event Timer，HPET）作为系统定时器（System Timer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_HPET_ENABLED && <choice>
```

**主动选择（Selects）**

```text
CONFIG_IOAPIC
CONFIG_LOAPIC
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
```

**弱选择（Implies）**

```text
CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME
```

**定义位置（Location）**：[`drivers/timer/Kconfig.x86:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.x86#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → 默认系统定时器（Default System Timer）

**配置项引用（Symbol References）**：[`CONFIG_IOAPIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_IOAPIC)、[`CONFIG_LOAPIC`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_LOAPIC)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)、[`CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME)。

<a id="CONFIG_INFINEON_LP_TIMER_HAL"></a>

## 7.37 `CONFIG_INFINEON_LP_TIMER_HAL`

**提示（Prompt）**：Infineon 低功耗定时器（Low Power Timer）驱动

**说明（Help）**

此模块为低功耗定时器（LowPower Timer）实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。此实现基于 Infineon 旧版硬件抽象层（Legacy HAL）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_LP_TIMER_ENABLED && CONFIG_USE_INFINEON_LEGACY_HAL && CONFIG_PM && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_LPTIMER
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.infineon_lp:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.infineon_lp#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_USE_INFINEON_LEGACY_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_LEGACY_HAL)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_USE_INFINEON_LPTIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_LPTIMER)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_INFINEON_LP_TIMER_PDL"></a>

## 7.38 `CONFIG_INFINEON_LP_TIMER_PDL`

**提示（Prompt）**：Infineon 低功耗定时器（Low Power Timer）驱动

**说明（Help）**

此模块基于 PDL 为低功耗定时器（LowPower Timer）实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_LP_TIMER_ENABLED && !CONFIG_USE_INFINEON_LEGACY_HAL && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_LPTIMER
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.infineon_lp:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.infineon_lp#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_USE_INFINEON_LEGACY_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_LEGACY_HAL)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_USE_INFINEON_LPTIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_LPTIMER)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_INTEL_ADSP_TIMER"></a>

## 7.39 `CONFIG_INTEL_ADSP_TIMER`

**提示（Prompt）**：Intel 音频 DSP 定时器（Timer）

**说明（Help）**

DSP 墙钟定时器（Wall Clock Timer）由外部振荡器直接驱动，位于 CPU 内核之外。其速度不及内核内部时钟，但可为所有 CPU 内核提供公共且同步的计数器，这对对称多处理（SMP）很有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ADSP_TIMER_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CAVS_TIMER
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
CONFIG_SYSTEM_CLOCK_LOCK_FREE_COUNT
```

**定义位置（Location）**：[`drivers/timer/Kconfig.cavs:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.cavs#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_CAVS_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_CAVS_TIMER)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)、[`CONFIG_SYSTEM_CLOCK_LOCK_FREE_COUNT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_CLOCK_LOCK_FREE_COUNT)。

<a id="CONFIG_ITE_IT51XXX_TIMER"></a>

## 7.40 `CONFIG_ITE_IT51XXX_TIMER`

**提示（Prompt）**：ITE it51xxx 定时器驱动（Timer Driver）

**说明（Help）**

此模块为 ITE IT51XXX 硬件定时器模型（HW Timer Model）实现内核设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT51XXX_TIMER_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.it51xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.it51xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_ITE_IT51XXX_TIMER_COUNTUP_IN_COMBINATION_MODE"></a>

## 7.41 `CONFIG_ITE_IT51XXX_TIMER_COUNTUP_IN_COMBINATION_MODE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用组合模式（Combination Mode）时，为外部定时器启用向上计数模式（Count-up Mode）。应根据硬件设计选择此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ITE_IT51XXX_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_IT51526AW || CONFIG_SOC_IT51526BW
```

**定义位置（Location）**：[`drivers/timer/Kconfig.it51xxx:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.it51xxx#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → ITE it51xxx 定时器驱动（Timer Driver）

**配置项引用（Symbol References）**：[`CONFIG_ITE_IT51XXX_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_ITE_IT51XXX_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_SOC_IT51526AW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT51526AW)、[`CONFIG_SOC_IT51526BW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT51526BW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_IT51526AW`、`CONFIG_SOC_IT51526BW`。

<a id="CONFIG_ITE_IT8XXX2_TIMER"></a>

## 7.42 `CONFIG_ITE_IT8XXX2_TIMER`

**提示（Prompt）**：ITE it8xxx2 定时器驱动（Timer Driver）

**说明（Help）**

此模块为 ITE it8xxx2 硬件定时器模型（HW Timer Model）实现内核设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_TIMER_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.ite_it8xxx2:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.ite_it8xxx2#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_LEON_GPTIMER"></a>

## 7.43 `CONFIG_LEON_GPTIMER`

**提示（Prompt）**：LEON 定时器（Timer）

**说明（Help）**

此模块为 LEON 系统中常见的 GRLIB GPTIMER 实现内核设备驱动（Kernel Device Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GAISLER_GPTIMER_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DYNAMIC_INTERRUPTS
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.leon_gptimer:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.leon_gptimer#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_DYNAMIC_INTERRUPTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_LITEX_TIMER"></a>

## 7.44 `CONFIG_LITEX_TIMER`

**提示（Prompt）**：LiteX 定时器（Timer）

**说明（Help）**

此模块为 LiteX 定时器（Timer）实现内核设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LITEX_TIMER0_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
```

**定义位置（Location）**：[`drivers/timer/Kconfig.litex:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.litex#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)。

<a id="CONFIG_MAX32_RV32_SYS_TIMER"></a>

## 7.45 `CONFIG_MAX32_RV32_SYS_TIMER`

**提示（Prompt）**：ADI MAX32 RV32 系统定时器驱动（System Timer Driver）

**说明（Help）**

此模块实现内核设备驱动，将 MAX32 定时器外设用作 RV32 内核的系统时钟（System Clock），并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_RV32_SYS_TIMER_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.max32_rv32_sys_timer:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.max32_rv32_sys_timer#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_MAX32_WUT_TIMER"></a>

## 7.46 `CONFIG_MAX32_WUT_TIMER`

**提示（Prompt）**：MAX32 唤醒定时器（Wake-Up Timer）系统时钟驱动

**说明（Help）**

此模块为 MAX32 唤醒定时器（Wake-Up Timer）实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_WUT_TIMER_ENABLED && CONFIG_SOC_FAMILY_MAX32 && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.max32_wut:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.max32_wut#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32`。

<a id="CONFIG_MCHP_PIT_G1_TIMER"></a>

## 7.47 `CONFIG_MCHP_PIT_G1_TIMER`

**提示（Prompt）**：Microchip 周期间隔定时器（Periodic Interval Timer，PIT）

**说明（Help）**

此模块为 Microchip SAMA5D2 系列 PIT 定时器实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_PIT_G1_TIMER_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/timer/Kconfig.mchp_sam:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.mchp_sam#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_MCHP_SAM_PIT64B_TIMER"></a>

## 7.48 `CONFIG_MCHP_SAM_PIT64B_TIMER`

**提示（Prompt）**：Microchip SAM 64 位周期间隔定时器（Periodic Interval Timer，PIT64B）

**说明（Help）**

此模块为 Microchip SAMA7G5 系列 PIT64B 定时器实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_SAM_PIT64B_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.mchp_sam:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.mchp_sam#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_MCHP_XEC_RTOS_TIMER"></a>

## 7.49 `CONFIG_MCHP_XEC_RTOS_TIMER`

**提示（Prompt）**：Microchip XEC 系列实时操作系统（RTOS）定时器

**说明（Help）**

此模块为 Microchip XEC 系列 RTOS 定时器实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_RTOS_TIMER_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT
```

**定义位置（Location）**：[`drivers/timer/Kconfig.mchp_xec_rtos:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.mchp_xec_rtos#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT)。

<a id="CONFIG_MCUX_GPT_TIMER"></a>

## 7.50 `CONFIG_MCUX_GPT_TIMER`

**提示（Prompt）**：MCUX GPT 事件定时器（Event Timer）

**说明（Help）**

此模块为 NXP GPT 定时器实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。它使用系统中定义的第一个 GPT 外设，该外设随后便不能再用于 GPT 计数器驱动（Counter Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM && DT_HAS_NXP_GPT_HW_TIMER_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.mcux_gpt:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.mcux_gpt#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_MCUX_LPTMR_TIMER"></a>

## 7.51 `CONFIG_MCUX_LPTMR_TIMER`

**提示（Prompt）**：MCUX LPTMR 定时器（Timer）

**说明（Help）**

此模块为 NXP MCUX 低功耗定时器（Low Power Timer，LPTMR）实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。要使用的实例由 `chosen` 节点的 `zephyr,system-timer` 属性选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.mcux_lptmr:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.mcux_lptmr#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_MCUX_OS_TIMER"></a>

## 7.52 `CONFIG_MCUX_OS_TIMER`

**提示（Prompt）**：MCUX OS 事件定时器（Event Timer）

**说明（Help）**

此模块为 NXP OS 事件定时器（Event Timer）实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_OS_TIMER_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
CONFIG_RESET
CONFIG_SYSTEM_TIMER_HAS_LPM_COMPANION_SUPPORT
```

**定义位置（Location）**：[`drivers/timer/Kconfig.mcux_os:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.mcux_os#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_SYSTEM_TIMER_HAS_LPM_COMPANION_SUPPORT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_HAS_LPM_COMPANION_SUPPORT)。

<a id="CONFIG_MCUX_OS_TIMER_MIN_DELAY"></a>

## 7.53 `CONFIG_MCUX_OS_TIMER_MIN_DELAY`

**提示（Prompt）**：OS 定时器匹配值的最小延迟周期数（Minimum Delay Cycles）

**说明（Help）**

定时器硬件需要最短设置时间（Minimum Setup Time），才能可靠地触发中断。如果设置的匹配值（Match Value）太接近当前定时器计数，硬件可能来不及处理。较小的值可改善计时精度，但可能降低可靠性；较大的值可提供更多安全裕量，但会略微降低计时准确性。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUX_OS_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/timer/Kconfig.mcux_os:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.mcux_os#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → MCUX OS 事件定时器（Event Timer）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_OS_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_MCUX_OS_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_MCUX_OS_TIMER_PM_POWERED_OFF"></a>

## 7.54 `CONFIG_MCUX_OS_TIMER_PM_POWERED_OFF`

**提示（Prompt）**：重新初始化 OS 定时器（Reinitialize the OS Timer）

**说明（Help）**

OS 定时器在某些低功耗模式（Low Power Mode）下会被关闭。选择此选项后，OS 定时器会采取措施保存状态，并在唤醒时重新初始化。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUX_OS_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**定义位置（Location）**：[`drivers/timer/Kconfig.mcux_os:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.mcux_os#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → MCUX OS 事件定时器（Event Timer）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_OS_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_MCUX_OS_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_MCUX_RTC_JDP_TIMER"></a>

## 7.55 `CONFIG_MCUX_RTC_JDP_TIMER`

**提示（Prompt）**：MCUX RTC JDP 系统定时器（System Timer）

**说明（Help）**

此模块为 NXP RTC（JDP 代）实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。由于 RTC 在所有低功耗状态下都保持运行，因此无需伴随定时器（Companion Timer），即可用作系统滴答源（System Tick Source）。要使用的实例由 `chosen` 节点的 `zephyr,system-timer` 属性选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT
CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME
```

**定义位置（Location）**：[`drivers/timer/Kconfig.mcux_rtc_jdp:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.mcux_rtc_jdp#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT)、[`CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME)。

<a id="CONFIG_MCUX_STM_TIMER"></a>

## 7.56 `CONFIG_MCUX_STM_TIMER`

**提示（Prompt）**：MCUX STM 系统定时器（System Timer）

**说明（Help）**

将 NXP 系统定时器模块（System Timer Module，STM）外设用作 Zephyr 的系统定时器。此驱动直接使用 MCUXpresso SDK 的 STM 驱动 `fsl_stm`，支持有滴答（Tickful）和无滴答（Tickless）内核运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME
CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT
```

**定义位置（Location）**：[`drivers/timer/Kconfig.mcux_stm:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.mcux_stm#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME)、[`CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT)。

<a id="CONFIG_MCUX_SYSCTR_TIMER"></a>

## 7.57 `CONFIG_MCUX_SYSCTR_TIMER`

**提示（Prompt）**：MCUX 系统计数器（System Counter，SYS_CTR）定时器

**说明（Help）**

NXP 系统计数器（System Counter，SYS_CTR）的系统时钟驱动：SYS_CTR 是一个以 24 MHz 运行的 56 位自由运行计数器（Free-running Counter），具有两个比较帧（Compare Frame）。仅使用比较帧 0 作为系统定时器；通过 `chosen` 节点的 `zephyr,system-timer` 属性选择实例。注意，SYS_CTR 是多个内核共享的时基（Time Base），此驱动在初始化时会复位整个模块，包括计数器和两个比较帧。因此，驱动必须独占该实例：如果另一个内核或某个启动阶段已经在使用同一个 SYS_CTR，请勿启用此驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT
```

**定义位置（Location）**：[`drivers/timer/Kconfig.mcux_sysctr:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.mcux_sysctr#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)、[`CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT)。

<a id="CONFIG_MCUX_SYSCTR_TIMER_MIN_DELAY"></a>

## 7.58 `CONFIG_MCUX_SYSCTR_TIMER_MIN_DELAY`

**提示（Prompt）**：定时器匹配值的最小延迟周期数（Minimum Delay Cycles）

**说明（Help）**

定时器硬件需要最短设置时间（Minimum Setup Time），才能可靠地触发中断。如果设置的匹配值（Match Value）太接近当前定时器计数，硬件可能来不及处理。较小的值可改善计时精度，但可能降低可靠性；较大的值可提供更多安全裕量，但会略微降低计时准确性。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUX_SYSCTR_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/timer/Kconfig.mcux_sysctr:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.mcux_sysctr#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → MCUX 系统计数器（System Counter，SYS_CTR）定时器

**配置项引用（Symbol References）**：[`CONFIG_MCUX_SYSCTR_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_MCUX_SYSCTR_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_MIPS_CP0_TIMER"></a>

## 7.59 `CONFIG_MIPS_CP0_TIMER`

**提示（Prompt）**：MIPS CP0 定时器（Timer）

**说明（Help）**

此模块为 MIPS CP0 定时器（Timer）实现内核设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MIPS && CONFIG_SYS_CLOCK_EXISTS
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.mips_cp0:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.mips_cp0#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MIPS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPS)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_MTK_ADSP_TIMER"></a>

## 7.60 `CONFIG_MTK_ADSP_TIMER`

**提示（Prompt）**：MediaTek 音频 DSP 定时器（Timer）

**说明（Help）**

MediaTek MT81xx 音频 DSP 具有用于系统时间的 13 MHz 墙钟定时器（Wall Clock Timer），其速率独立于 CPU 速度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MEDIATEK_OSTIMER64_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
CONFIG_SYSTEM_CLOCK_LOCK_FREE_COUNT
```

**定义位置（Location）**：[`drivers/timer/Kconfig.mtk_adsp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.mtk_adsp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)、[`CONFIG_SYSTEM_CLOCK_LOCK_FREE_COUNT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_CLOCK_LOCK_FREE_COUNT)。

<a id="CONFIG_NATIVE_SIM_TIMER"></a>

## 7.61 `CONFIG_NATIVE_SIM_TIMER`

**提示（Prompt）**：（POSIX）native_sim 定时器驱动（Timer Driver）

**说明（Help）**

此模块为 native_sim 硬件定时器模型（HW Timer Model）实现内核设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BOARD_NATIVE_SIM && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT
```

**定义位置（Location）**：[`drivers/timer/Kconfig.native_sim:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.native_sim#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_NATIVE_SIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NATIVE_SIM)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)、[`CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_NATIVE_SIM`。

<a id="CONFIG_NPCX_ITIM_TIMER"></a>

## 7.62 `CONFIG_NPCX_ITIM_TIMER`

**提示（Prompt）**：Nuvoton NPCX 系列内部 64/32 位定时器（Timer）

**说明（Help）**

此模块为 Nuvoton NPCX 系列内部 64/32 位定时器实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NPCX_ITIM_TIMER_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
```

**定义位置（Location）**：[`drivers/timer/Kconfig.npcx_itim:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.npcx_itim#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)。

<a id="CONFIG_NRF_GRTC_ALWAYS_ON"></a>

## 7.63 `CONFIG_NRF_GRTC_ALWAYS_ON`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

即使 CPU 处于休眠模式（Sleep Mode），也始终保持 SYSCOUNTER 活动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_GRTC_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_grtc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_grtc#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → nRF GRTC 定时器（Timer）

**配置项引用（Symbol References）**：[`CONFIG_NRF_GRTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_NRF_GRTC_START_SYSCOUNTER"></a>

## 7.64 `CONFIG_NRF_GRTC_START_SYSCOUNTER`

**提示（Prompt）**：驱动初始化（Driver Init）时启动 SYSCOUNTER

**说明（Help）**

初始化 GRTC 时启动 SYSCOUNTER。系统中应当只有一个处理器负责此操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_GRTC_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**主动选择（Selects）**

```text
CONFIG_NRF_GRTC_TIMER_CLOCK_MANAGEMENT
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_grtc:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_grtc#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → nRF GRTC 定时器（Timer）

**配置项引用（Symbol References）**：[`CONFIG_NRF_GRTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_NRF_GRTC_TIMER_CLOCK_MANAGEMENT`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER_CLOCK_MANAGEMENT)。

<a id="CONFIG_NRF_GRTC_SYSCOUNTER_SLEEP_MINIMUM_LATENCY"></a>

## 7.65 `CONFIG_NRF_GRTC_SYSCOUNTER_SLEEP_MINIMUM_LATENCY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

该值以微秒（µs）为单位，确保唤醒事件（Wakeup Event）不会过早触发。换言之，让 SYSCOUNTER 进入休眠状态的时间若短于 `NRF_GRTC_SYSCOUNTER_SLEEP_MINIMUM_LATENCY`，便没有意义。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POWEROFF && CONFIG_NRF_GRTC_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_grtc:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_grtc#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → nRF GRTC 定时器（Timer）

**配置项引用（Symbol References）**：[`CONFIG_POWEROFF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POWEROFF)、[`CONFIG_NRF_GRTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_NRF_GRTC_TIMER"></a>

## 7.66 `CONFIG_NRF_GRTC_TIMER`

**提示（Prompt）**：nRF GRTC 定时器（Timer）

**说明（Help）**

此模块为 nRF 全局实时计数器（Global Real Time Counter）`NRF_GRTC` 实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_GRTC_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
CONFIG_NRFX_GRTC
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_grtc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_grtc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)、[`CONFIG_NRFX_GRTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GRTC)。

<a id="CONFIG_NRF_GRTC_TIMER_APP_DEFINED_INIT"></a>

## 7.67 `CONFIG_NRF_GRTC_TIMER_APP_DEFINED_INIT`

**提示（Prompt）**：由应用程序定义 GRTC 初始化（Initialization）

**说明（Help）**

由应用程序定义 GRTC 驱动的初始化过程和时机，而不交由 `SYS_INIT` 决定。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_GRTC_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_grtc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_grtc#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → nRF GRTC 定时器（Timer）

**配置项引用（Symbol References）**：[`CONFIG_NRF_GRTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_NRF_GRTC_TIMER_AUTO_KEEP_ALIVE"></a>

## 7.68 `CONFIG_NRF_GRTC_TIMER_AUTO_KEEP_ALIVE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此功能防止 SYSCOUNTER 在任何内核处于活动状态（Active State）时休眠。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_GRTC_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y if CONFIG_NRF_GRTC_START_SYSCOUNTER
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_grtc:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_grtc#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → nRF GRTC 定时器（Timer）

**配置项引用（Symbol References）**：[`CONFIG_NRF_GRTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_NRF_GRTC_START_SYSCOUNTER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_START_SYSCOUNTER)。

<a id="CONFIG_NRF_GRTC_TIMER_CLEAR_AT_UNINIT"></a>

## 7.69 `CONFIG_NRF_GRTC_TIMER_CLEAR_AT_UNINIT`

**提示（Prompt）**：反初始化（Uninitialize）时自动清除 GRTC

**说明（Help）**

启用后，在驱动反初始化（Uninitialize）时，例如调用 `sys_clock_disable()` 时，将自动清除 GRTC 定时器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_GRTC_START_SYSCOUNTER && CONFIG_NRF_GRTC_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y if !CONFIG_MCUBOOT
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_grtc:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_grtc#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → nRF GRTC 定时器（Timer）

**配置项引用（Symbol References）**：[`CONFIG_NRF_GRTC_START_SYSCOUNTER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_START_SYSCOUNTER)、[`CONFIG_NRF_GRTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_MCUBOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUBOOT)。

<a id="CONFIG_NRF_GRTC_TIMER_CLOCK_MANAGEMENT"></a>

## 7.70 `CONFIG_NRF_GRTC_TIMER_CLOCK_MANAGEMENT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

编译额外的驱动代码，以启用 GRTC 管理功能（Management Functionality）。通常只有负责启动 SYSCOUNTER 的处理器需要它，但系统中的多个处理器也可以共享此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_GRTC_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**被选择（Selected by）**

```text
CONFIG_NRF_GRTC_START_SYSCOUNTER
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_grtc:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_grtc#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → nRF GRTC 定时器（Timer）

**配置项引用（Symbol References）**：[`CONFIG_NRF_GRTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_NRF_GRTC_START_SYSCOUNTER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_START_SYSCOUNTER)。

<a id="CONFIG_NRF_GRTC_TIMER_SOURCE"></a>

## 7.71 `CONFIG_NRF_GRTC_TIMER_SOURCE`

**提示（Prompt）**：nRF GRTC 时钟源（Clock Source）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_GRTC_START_SYSCOUNTER && CONFIG_NRF_GRTC_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
CONFIG_NRF_GRTC_TIMER_SOURCE_LFLPRC if CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC || n
CONFIG_NRF_GRTC_TIMER_SOURCE_LFXO
CONFIG_NRF_GRTC_TIMER_SOURCE_SYSTEM_LFCLK
```

**可选项（Choices）**

```text
CONFIG_NRF_GRTC_TIMER_SOURCE_LFXO
CONFIG_NRF_GRTC_TIMER_SOURCE_SYSTEM_LFCLK
CONFIG_NRF_GRTC_TIMER_SOURCE_LFLPRC
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_grtc:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_grtc#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → nRF GRTC 定时器（Timer）

**配置项引用（Symbol References）**：[`CONFIG_NRF_GRTC_START_SYSCOUNTER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_START_SYSCOUNTER)、[`CONFIG_NRF_GRTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_NRF_GRTC_TIMER_SOURCE_LFLPRC`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER_SOURCE_LFLPRC)、[`CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC)、[`CONFIG_NRF_GRTC_TIMER_SOURCE_LFXO`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER_SOURCE_LFXO)、[`CONFIG_NRF_GRTC_TIMER_SOURCE_SYSTEM_LFCLK`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER_SOURCE_SYSTEM_LFCLK)。

<a id="CONFIG_NRF_GRTC_TIMER_SOURCE_LFLPRC"></a>

## 7.72 `CONFIG_NRF_GRTC_TIMER_SOURCE_LFLPRC`

**提示（Prompt）**：使用低频低功耗 RC（Low Frequency Low Power RC）作为时钟源

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_GRTC_TIMER_SOURCE>
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_grtc:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_grtc#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → nRF GRTC 定时器（Timer） → nRF GRTC 时钟源（Clock Source）

**配置项引用（Symbol References）**：[`CONFIG_NRF_GRTC_TIMER_SOURCE`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER_SOURCE)。

<a id="CONFIG_NRF_GRTC_TIMER_SOURCE_LFXO"></a>

## 7.73 `CONFIG_NRF_GRTC_TIMER_SOURCE_LFXO`

**提示（Prompt）**：使用低频晶体振荡器（Low Frequency XO）作为时钟源

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_grtc:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_grtc#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → nRF GRTC 定时器（Timer） → nRF GRTC 时钟源（Clock Source）

<a id="CONFIG_NRF_GRTC_TIMER_SOURCE_SYSTEM_LFCLK"></a>

## 7.74 `CONFIG_NRF_GRTC_TIMER_SOURCE_SYSTEM_LFCLK`

**提示（Prompt）**：使用系统低频时钟（System Low Frequency Clock）作为时钟源

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NRF_GRTC_TIMER_SOURCE>
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_grtc:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_grtc#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → nRF GRTC 定时器（Timer） → nRF GRTC 时钟源（Clock Source）

**配置项引用（Symbol References）**：[`CONFIG_NRF_GRTC_TIMER_SOURCE`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER_SOURCE)。

<a id="CONFIG_NRF_GRTC_TIMER_STOP_AT_UNINIT"></a>

## 7.75 `CONFIG_NRF_GRTC_TIMER_STOP_AT_UNINIT`

**提示（Prompt）**：反初始化（Uninitialize）时自动停止 GRTC

**说明（Help）**

启用后，在驱动反初始化（Uninitialize）时，例如调用 `sys_clock_disable()` 时，将自动停止 GRTC 定时器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_GRTC_START_SYSCOUNTER && CONFIG_NRF_GRTC_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y if !CONFIG_MCUBOOT
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_grtc:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_grtc#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → nRF GRTC 定时器（Timer）

**配置项引用（Symbol References）**：[`CONFIG_NRF_GRTC_START_SYSCOUNTER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_START_SYSCOUNTER)、[`CONFIG_NRF_GRTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_MCUBOOT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUBOOT)。

<a id="CONFIG_NRF_RTC_TIMER"></a>

## 7.76 `CONFIG_NRF_RTC_TIMER`

**提示（Prompt）**：nRF 实时计数器（Real Time Counter，NRF_RTC1）定时器

**说明（Help）**

此模块为 nRF 实时计数器（Real Time Counter）`NRF_RTC1` 实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL && CONFIG_SOC_COMPATIBLE_NRF && !n && !DT_HAS_NORDIC_NRF_GRTC_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y if CONFIG_SYS_CLOCK_EXISTS
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT
CONFIG_NRFX_GPPI if CONFIG_SOC_NRF52832
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_rtc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_rtc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL)、[`CONFIG_SOC_COMPATIBLE_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)、[`CONFIG_SOC_NRF52832`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF52832)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF`、`CONFIG_SOC_NRF52832`。

<a id="CONFIG_NRF_RTC_TIMER_LOCK_ZERO_LATENCY_IRQS"></a>

## 7.77 `CONFIG_NRF_RTC_TIMER_LOCK_ZERO_LATENCY_IRQS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用通过 `__disable_irq()` 禁用零延迟中断（Zero Latency IRQ，ZLI）的功能，防止更高优先级的上下文（包括 ZLI）抢占处理程序并调用 `nrf_rtc_timer` API，从而破坏 `nrf_rtc_timer` 的内部状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZERO_LATENCY_IRQS && CONFIG_NRF_RTC_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y if !CONFIG_BT_LL_SW_SPLIT
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_rtc:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_rtc#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → nRF 实时计数器（Real Time Counter，NRF_RTC1）定时器

**配置项引用（Symbol References）**：[`CONFIG_ZERO_LATENCY_IRQS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZERO_LATENCY_IRQS)、[`CONFIG_NRF_RTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_RTC_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_BT_LL_SW_SPLIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LL_SW_SPLIT)。

<a id="CONFIG_NRF_RTC_TIMER_TRIGGER_OVERFLOW"></a>

## 7.78 `CONFIG_NRF_RTC_TIMER_TRIGGER_OVERFLOW`

**提示（Prompt）**：触发溢出（Trigger Overflow）

**说明（Help）**

启用后，可以通过一个函数触发 RTC 溢出（Overflow），从而实际将时间向未来推进。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_RTC_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_rtc:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_rtc#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → nRF 实时计数器（Real Time Counter，NRF_RTC1）定时器

**配置项引用（Symbol References）**：[`CONFIG_NRF_RTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_RTC_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_NRF_RTC_TIMER_USER_CHAN_COUNT"></a>

## 7.79 `CONFIG_NRF_RTC_TIMER_USER_CHAN_COUNT`

**提示（Prompt）**：可使用的附加通道（Additional Channels）

**说明（Help）**

使用 `nrf_rtc_timer.h` API。驱动不负责管理通道分配（Channel Allocation）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NRF_RTC_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
2 if CONFIG_NRF_802154_RADIO_DRIVER && CONFIG_SOC_COMPATIBLE_NRF5340_CPUNET
3 if CONFIG_NRF_802154_RADIO_DRIVER
0
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_rtc:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_rtc#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → nRF 实时计数器（Real Time Counter，NRF_RTC1）定时器

**配置项引用（Symbol References）**：[`CONFIG_NRF_RTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_RTC_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_NRF_802154_RADIO_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_SOC_COMPATIBLE_NRF5340_CPUNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_COMPATIBLE_NRF5340_CPUNET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_COMPATIBLE_NRF5340_CPUNET`。

<a id="CONFIG_OPENRISC_TICK_TIMER"></a>

## 7.80 `CONFIG_OPENRISC_TICK_TIMER`

**提示（Prompt）**：OpenRISC 滴答定时器（Tick Timer）

**说明（Help）**

此模块为 OpenRISC 滴答定时器（Tick Timer）实现内核设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENRISC && CONFIG_SYS_CLOCK_EXISTS
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.openrisc_tick:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.openrisc_tick#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_OPENRISC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENRISC)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_RCAR_CMT_TIMER"></a>

## 7.81 `CONFIG_RCAR_CMT_TIMER`

**提示（Prompt）**：Renesas RCar CMT 定时器（Timer）

**说明（Help）**

此模块为 Renesas RCAR 平台实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。如果未选中，将不使用任何定时器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RCAR_CMT_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/timer/Kconfig.rcar_cmt:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.rcar_cmt#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_REALTEK_RTS5912_RTMR"></a>

## 7.82 `CONFIG_REALTEK_RTS5912_RTMR`

**提示（Prompt）**：Realtek RTS5912 实时操作系统（RTOS）定时器

**说明（Help）**

此模块为 Realtek RTS5912 系列 RTOS 定时器实现内核设备驱动（Kernel Device Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RTS5912 && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y if DT_HAS_REALTEK_RTS5912_RTMR_ENABLED
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT
```

**定义位置（Location）**：[`drivers/timer/Kconfig.realtek_rts5912_rtmr:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.realtek_rts5912_rtmr#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RTS5912`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RTS5912)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT)。

<a id="CONFIG_RENESAS_RA_ULPT_TIMER"></a>

## 7.83 `CONFIG_RENESAS_RA_ULPT_TIMER`

**提示（Prompt）**：Renesas RA 系列 ULPT 定时器（Timer）

**说明（Help）**

此模块为 Renesas RA 系列 ULPT 定时器实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_ULPT_TIMER_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y if CONFIG_PM
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.renesas_ra_ulpt:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.renesas_ra_ulpt#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_RENESAS_RX_TIMER_CMT"></a>

## 7.84 `CONFIG_RENESAS_RX_TIMER_CMT`

**提示（Prompt）**：Renesas RX CMT 定时器（Timer）

**说明（Help）**

此模块为 Renesas RX 平台实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。如果未选中，将不使用任何定时器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_TIMER_CMT_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.renesas_rx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.renesas_rx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_RISCV_MACHINE_TIMER"></a>

## 7.85 `CONFIG_RISCV_MACHINE_TIMER`

**提示（Prompt）**：RISC-V 机器定时器（Machine Timer）

**说明（Help）**

此模块为通用 RISC-V 机器定时器（Machine Timer）驱动实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_M_MODE && (DT_HAS_RISCV_MACHINE_TIMER_ENABLED || DT_HAS_NUCLEI_SYSTIMER_ENABLED) && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_CPU_XUANTIE_E907
```

**定义位置（Location）**：[`drivers/timer/Kconfig.riscv_machine:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.riscv_machine#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_M_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_M_MODE)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)、[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_CPU_XUANTIE_E907`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_XUANTIE_E907)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CPU_XUANTIE_E907`。

<a id="CONFIG_RISCV_MACHINE_TIMER_SYSTEM_CLOCK_DIVIDER"></a>

## 7.86 `CONFIG_RISCV_MACHINE_TIMER_SYSTEM_CLOCK_DIVIDER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

指定供给机器定时器（Machine Timer）的系统时钟分频比（Division Ratio）。将系统时钟除以 `2^N` 后得到的时钟提供给定时器，其中 `N` 为本参数的值。`N=2` 时除以 4，`N=5` 时除以 32。默认 `N=0`，表示将系统时钟直接用作机器定时器时钟，这是 RISC-V 机器时钟的常规配置。此参数通常取决于硬件配置。分频比应定义在设备树（Devicetree）中，推荐在 Kconfig 中使用 `dt_node_int_prop_int` 等函数引用它，不建议在 `.conf` 文件中调整。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_MACHINE_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/timer/Kconfig.riscv_machine:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.riscv_machine#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → RISC-V 机器定时器（Machine Timer）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_MACHINE_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_RISCV_MACHINE_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_RISCV_SUPERVISOR_TIMER"></a>

## 7.87 `CONFIG_RISCV_SUPERVISOR_TIMER`

**提示（Prompt）**：RISC-V 监管者定时器（Supervisor Timer）

**说明（Help）**

此模块为 RISC-V 监管者模式（Supervisor Mode）定时器实现内核设备驱动。它使用 SBI 定时器扩展（Timer Extension）设置定时器截止时间，并通过 `time` 控制与状态寄存器（CSR）读取时间，提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV_S_MODE && (DT_HAS_RISCV_MACHINE_TIMER_ENABLED || DT_HAS_NUCLEI_SYSTIMER_ENABLED) && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER
```

**定义位置（Location）**：[`drivers/timer/Kconfig.riscv_supervisor:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.riscv_supervisor#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RISCV_S_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_S_MODE)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)。

<a id="CONFIG_RV32M1_LPTMR_TIMER"></a>

## 7.88 `CONFIG_RV32M1_LPTMR_TIMER`

**提示（Prompt）**：RV32M1 LPTMR 系统定时器驱动（System Timer Driver）

**说明（Help）**

此模块实现内核设备驱动，将 LPTMR 外设用作系统时钟（System Clock），并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_OPENISA_RV32M1_LPTMR_ENABLED && CONFIG_RV32M1_INTMUX && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/timer/Kconfig.rv32m1_lptmr:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.rv32m1_lptmr#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RV32M1_INTMUX`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_RV32M1_INTMUX)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_RZA2M_OSTM_TIMER"></a>

## 7.89 `CONFIG_RZA2M_OSTM_TIMER`

**提示（Prompt）**：Renesas RZ/A2M OS 定时器（Timer）

**说明（Help）**

此模块为 Renesas RZ/A2M 平台实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZA2M_OSTM_TIMER_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME
CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.renesas_rza2m:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.renesas_rza2m#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME)、[`CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_RZ_OS_TIMER"></a>

## 7.90 `CONFIG_RZ_OS_TIMER`

**提示（Prompt）**：Renesas RZ OS 定时器（Timer）

**说明（Help）**

此模块为 Renesas RZ 平台实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_GTM_OS_TIMER_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME
CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT
CONFIG_TICKLESS_CAPABLE
CONFIG_USE_RZ_FSP_GTM
```

**定义位置（Location）**：[`drivers/timer/Kconfig.renesas_rz:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.renesas_rz#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME)、[`CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_USE_RZ_FSP_GTM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_GTM)。

<a id="CONFIG_SAM0_RTC_TIMER"></a>

## 7.91 `CONFIG_SAM0_RTC_TIMER`

**提示（Prompt）**：Atmel SAM0 系列 RTC 定时器（Timer）

**说明（Help）**

此模块为 Atmel SAM0 系列实时计数器（Real Time Counter）实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM0_RTC_ENABLED && n && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.sam0_rtc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.sam0_rtc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_SILABS_SLEEPTIMER_TIMER"></a>

## 7.92 `CONFIG_SILABS_SLEEPTIMER_TIMER`

**提示（Prompt）**：Silabs 休眠定时器（Sleeptimer）系统时钟驱动

**说明（Help）**

此模块为休眠定时器（Sleeptimer）实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_SILABS_GECKO_SLEEPTIMER
CONFIG_SILABS_SISDK_SLEEPTIMER
CONFIG_TICKLESS_CAPABLE
CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME
```

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_SILABS_SIWX91X
```

**定义位置（Location）**：[`drivers/timer/Kconfig.silabs:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.silabs#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SILABS_GECKO_SLEEPTIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_GECKO_SLEEPTIMER)、[`CONFIG_SILABS_SISDK_SLEEPTIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_SLEEPTIMER)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME)、[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_SIWX91X`。

<a id="CONFIG_SMARTBOND_TIMER"></a>

## 7.93 `CONFIG_SMARTBOND_TIMER`

**提示（Prompt）**：Renesas SmartBond™ 定时器（Timer）

**说明（Help）**

此模块为 TIMER2 定时器实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RENESAS_SMARTBOND && CONFIG_CLOCK_CONTROL && !n && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.smartbond:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.smartbond#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_SMARTBOND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_SMARTBOND)、[`CONFIG_CLOCK_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_SMARTBOND`。

<a id="CONFIG_STM32WB0_RADIO_TIMER"></a>

## 7.94 `CONFIG_STM32WB0_RADIO_TIMER`

**提示（Prompt）**：STM32 WB0x 射频定时器（Radio Timer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_STM32WB0X && !((CONFIG_SOC_STM32WB06XX || CONFIG_SOC_STM32WB07XX) && CONFIG_PM) && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y if CONFIG_PM || CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_RADIO_TIMER
CONFIG_HAS_STM32LIB
CONFIG_TICKLESS_CAPABLE
CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT
```

**定义位置（Location）**：[`drivers/timer/Kconfig.stm32wb0_radio_timer:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.stm32wb0_radio_timer#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32WB0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WB0X)、[`CONFIG_SOC_STM32WB06XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32WB06XX)、[`CONFIG_SOC_STM32WB07XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32WB07XX)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT)、[`CONFIG_USE_STM32_HAL_RADIO_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_RADIO_TIMER)、[`CONFIG_HAS_STM32LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32LIB)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32WB0X`、`CONFIG_SOC_STM32WB06XX`、`CONFIG_SOC_STM32WB07XX`、`CONFIG_HAS_STM32LIB`。

<a id="CONFIG_STM32_LPTIM_CLOCK_LSE"></a>

## 7.95 `CONFIG_STM32_LPTIM_CLOCK_LSE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 LSE 作为 LPTIM 时钟源（Clock Source）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STM32_LPTIM_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
0 = 2
```

**定义位置（Location）**：[`drivers/timer/Kconfig.stm32_lptim:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.stm32_lptim#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → STM32 低功耗定时器（Low Power Timer）［实验性］

**配置项引用（Symbol References）**：[`CONFIG_STM32_LPTIM_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_STM32_LPTIM_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_STM32_LPTIM_CLOCK_LSI"></a>

## 7.96 `CONFIG_STM32_LPTIM_CLOCK_LSI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 LSI 作为 LPTIM 时钟源（Clock Source）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STM32_LPTIM_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
0 = 3
```

**定义位置（Location）**：[`drivers/timer/Kconfig.stm32_lptim:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.stm32_lptim#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → STM32 低功耗定时器（Low Power Timer）［实验性］

**配置项引用（Symbol References）**：[`CONFIG_STM32_LPTIM_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_STM32_LPTIM_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_STM32_LPTIM_STDBY_TIMER"></a>

## 7.97 `CONFIG_STM32_LPTIM_STDBY_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

进入待机模式（Standby Mode）时使用附加定时器。某些芯片，例如 STM32WBAX 系列，使用 LPTIM 作为系统定时器，但 LPTIM 在待机模式下没有时钟。这些芯片通常还有另一个不会停止的定时器，例如 RTC，但其频率较低，因此不能用作主系统定时器。STM32U5 的 STOP3 模式也采用相同方式。系统进入待机状态（Standby State）时，使用待机定时器处理超时，即唤醒。所选待机定时器节点必须支持通过计数器 API（Counter API）设置告警（Alarm）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COUNTER && CONFIG_TICKLESS_KERNEL && CONFIG_STM32_LPTIM_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/timer/Kconfig.stm32_lptim:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.stm32_lptim#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → STM32 低功耗定时器（Low Power Timer）［实验性］

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_STM32_LPTIM_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_STM32_LPTIM_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_STM32_LPTIM_TICK_FREQ_RATIO_OVERRIDE"></a>

## 7.98 `CONFIG_STM32_LPTIM_TICK_FREQ_RATIO_OVERRIDE`

**提示（Prompt）**：覆盖滴答与频率比值检查（Tick-to-frequency Ratio Check）

**说明（Help）**

对于 LPTIM 配置，根据 LPTIM 输入时钟建议采用特定的滴答频率（Tick Frequency）：

- LSI（32 kHz）：4000 滴答／秒。
- LSE（32768 Hz）：4096 滴答／秒。

为防止配置错误，驱动中实现了专门的检查。此选项允许覆盖该检查。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STM32_LPTIM_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y if CONFIG_ZTEST
```

**定义位置（Location）**：[`drivers/timer/Kconfig.stm32_lptim:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.stm32_lptim#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → STM32 低功耗定时器（Low Power Timer）［实验性］

**配置项引用（Symbol References）**：[`CONFIG_STM32_LPTIM_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_STM32_LPTIM_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST)。

<a id="CONFIG_STM32_LPTIM_TIMEBASE"></a>

## 7.99 `CONFIG_STM32_LPTIM_TIMEBASE`

**提示（Prompt）**：LPTIM 自动重装载值（AutoReload Value）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_STM32_LPTIM_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
0xFFFF if CONFIG_STM32_LPTIM_CLOCK_LSE
0xF9FF if CONFIG_STM32_LPTIM_CLOCK_LSI
```

**定义位置（Location）**：[`drivers/timer/Kconfig.stm32_lptim:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.stm32_lptim#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → STM32 低功耗定时器（Low Power Timer）［实验性］

**配置项引用（Symbol References）**：[`CONFIG_STM32_LPTIM_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_STM32_LPTIM_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_STM32_LPTIM_CLOCK_LSE`](P007_drivers_timer_配置项参考_1.md#CONFIG_STM32_LPTIM_CLOCK_LSE)、[`CONFIG_STM32_LPTIM_CLOCK_LSI`](P007_drivers_timer_配置项参考_1.md#CONFIG_STM32_LPTIM_CLOCK_LSI)。

<a id="CONFIG_STM32_LPTIM_TIMER"></a>

## 7.100 `CONFIG_STM32_LPTIM_TIMER`

**提示（Prompt）**：STM32 低功耗定时器（Low Power Timer）［实验性］

**说明（Help）**

此模块为低功耗定时器（LowPower Timer）实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RESET
CONFIG_TICKLESS_CAPABLE
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/timer/Kconfig.stm32_lptim:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.stm32_lptim#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<!-- kconfig-navigation -->

[上一章](P006_drivers_interrupt_controller_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P008_drivers_timer_配置项参考_2.md)
