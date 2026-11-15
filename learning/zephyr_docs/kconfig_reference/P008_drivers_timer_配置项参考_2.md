---
id: learning.zephyr-docs.kconfig-reference.page-8
title: "`drivers/timer`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第8章\_`drivers/timer`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `drivers/timer` 的 26 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SY1XX_SYS_TIMER"></a>

## 8.1 `CONFIG_SY1XX_SYS_TIMER`

**提示（Prompt）**：Sensry ganymed 系统定时器（System Timer）

**说明（Help）**

此模块为系统定时器实现内核设备驱动，并提供标准的系统时钟驱动（System Clock Driver）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/timer/Kconfig.sy1xx_sys_timer:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.sy1xx_sys_timer#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

<a id="CONFIG_SYSTEM_CLOCK_HW_CYCLES_PER_SEC_RUNTIME_UPDATE"></a>

## 8.2 `CONFIG_SYSTEM_CLOCK_HW_CYCLES_PER_SEC_RUNTIME_UPDATE`

**提示（Prompt）**：系统定时器频率（System Timer Frequency）可在运行时更新

**说明（Help）**

允许系统定时器频率（System Timer Frequency）在运行时改变。启用后，平台必须在应用系统定时器时钟变更之后调用 `z_sys_clock_hw_cycles_per_sec_update()`，以更新 `sys_clock_hw_cycles_per_sec()` 返回、并供时间转换辅助函数使用的运行时值。如果系统定时器驱动缓存了派生常量，或需要在时钟变化时重新编程硬件，则应覆盖 `z_sys_clock_hw_cycles_per_sec_update()`，以保持驱动状态一致。此选项不兼容各 CPU 独立的频率调节（Per-CPU Frequency Scaling），因为系统定时器频率以单个全局值进行跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_CPU_FREQ_PER_CPU_SCALING && CONFIG_SYS_CLOCK_EXISTS
```

**定义位置（Location）**：[`drivers/timer/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CPU_FREQ_PER_CPU_SCALING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_FREQ_PER_CPU_SCALING)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_SYSTEM_CLOCK_INIT_PRIORITY"></a>

## 8.3 `CONFIG_SYSTEM_CLOCK_INIT_PRIORITY`

**提示（Prompt）**：系统时钟驱动初始化优先级（Initialization Priority）

**说明（Help）**

此选项可用于设置系统时钟驱动（System Clock Driver）的特定初始化优先级。由于驱动初始化可能要求时钟已经运行，应保留默认值 `0`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/timer/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_SYSTEM_CLOCK_LOCK_FREE_COUNT"></a>

## 8.4 `CONFIG_SYSTEM_CLOCK_LOCK_FREE_COUNT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

实现无锁周期计数访问器（Lock-free Cycle Count Accessor）的驱动应选择此选项。对自旋锁持有时间（Spin Lock Hold Time）进行测量时需要此能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SYS_CLOCK_EXISTS
```

**被选择（Selected by）**

```text
CONFIG_INTEL_ADSP_TIMER
CONFIG_AURIX_STM
CONFIG_MTK_ADSP_TIMER
CONFIG_APIC_TIMER
```

**定义位置（Location）**：[`drivers/timer/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_INTEL_ADSP_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_INTEL_ADSP_TIMER)、[`CONFIG_AURIX_STM`](P007_drivers_timer_配置项参考_1.md#CONFIG_AURIX_STM)、[`CONFIG_MTK_ADSP_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_MTK_ADSP_TIMER)、[`CONFIG_APIC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_APIC_TIMER)。

<a id="CONFIG_SYSTEM_CLOCK_NO_WAIT"></a>

## 8.5 `CONFIG_SYSTEM_CLOCK_NO_WAIT`

**提示（Prompt）**：不等待（No Wait）

**说明（Help）**

启动系统时钟源（System Clock Source），但不等待时钟就绪。选择此选项后，执行依赖内核 API 的代码时，系统时钟可能尚未就绪；请求的超时将延长尚未完成的启动时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_xrtc:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_xrtc#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → 时钟启动策略（Clock Startup Policy）

<a id="CONFIG_SYSTEM_CLOCK_SLOPPY_IDLE"></a>

## 8.6 `CONFIG_SYSTEM_CLOCK_SLOPPY_IDLE`

**提示（Prompt）**：允许定时器在空闲期间使运行时间时钟偏移（Skew Uptime Clock）［实验性］

**说明（Help）**

启用后，当没有待处理超时（Pending Timeout）时，内核可以让系统运行时间计数（System Uptime Count）发生漂移，而不必持续唤醒 CPU 来维护计数。某些平台可利用这一点，减少为处理计数器回绕（Counter Wraparound）而产生的周期性中断开销。源码树中的开发板均未启用此选项，驱动对它的支持也尚未完成全面审查，因此标记为实验性（Experimental）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SYS_CLOCK_EXISTS
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/timer/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_SYSTEM_CLOCK_WAIT_FOR_AVAILABILITY"></a>

## 8.7 `CONFIG_SYSTEM_CLOCK_WAIT_FOR_AVAILABILITY`

**提示（Prompt）**：等待可用（Wait for Availability）

**说明（Help）**

系统时钟源（System Clock Source）初始化会等待时钟可用。某些系统最初使用启动较快、精度较低的时钟源运行，等目标时钟源就绪后再无缝切换。选择此选项后，系统时钟在系统时钟驱动初始化结束后便可用，但精度可能较低。如果时钟源没有中间状态，此选项等同于等待稳定（Wait for Stability）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_xrtc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_xrtc#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → 时钟启动策略（Clock Startup Policy）

<a id="CONFIG_SYSTEM_CLOCK_WAIT_FOR_STABILITY"></a>

## 8.8 `CONFIG_SYSTEM_CLOCK_WAIT_FOR_STABILITY`

**提示（Prompt）**：等待稳定（Wait for Stability）

**说明（Help）**

系统时钟源（System Clock Source）初始化会等待时钟稳定。选择此选项后，系统时钟在系统时钟驱动初始化结束后已可用且稳定。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/timer/Kconfig.nrf_xrtc:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.nrf_xrtc#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → 时钟启动策略（Clock Startup Policy）

<a id="CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT"></a>

## 8.9 `CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

实现 `sys_clock_disable()` API 支持的驱动应选择此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SYS_CLOCK_EXISTS
```

**被选择（Selected by）**

```text
CONFIG_CORTEX_M_SYSTICK
CONFIG_ESP32_SYS_TIMER
CONFIG_AURIX_STM
CONFIG_MCHP_XEC_RTOS_TIMER
CONFIG_NATIVE_SIM_TIMER
CONFIG_NRF_GRTC_TIMER
CONFIG_NRF_RTC_TIMER
CONFIG_REALTEK_RTS5912_RTMR
CONFIG_RZ_OS_TIMER
CONFIG_RZA2M_OSTM_TIMER
CONFIG_STM32WB0_RADIO_TIMER
```

**定义位置（Location）**：[`drivers/timer/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_CORTEX_M_SYSTICK`](P007_drivers_timer_配置项参考_1.md#CONFIG_CORTEX_M_SYSTICK)、[`CONFIG_ESP32_SYS_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_ESP32_SYS_TIMER)、[`CONFIG_AURIX_STM`](P007_drivers_timer_配置项参考_1.md#CONFIG_AURIX_STM)、[`CONFIG_MCHP_XEC_RTOS_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_MCHP_XEC_RTOS_TIMER)、[`CONFIG_NATIVE_SIM_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NATIVE_SIM_TIMER)、[`CONFIG_NRF_GRTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER)、[`CONFIG_NRF_RTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_RTC_TIMER)、[`CONFIG_REALTEK_RTS5912_RTMR`](P007_drivers_timer_配置项参考_1.md#CONFIG_REALTEK_RTS5912_RTMR)、[`CONFIG_RZ_OS_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_RZ_OS_TIMER)、[`CONFIG_RZA2M_OSTM_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_RZA2M_OSTM_TIMER)、[`CONFIG_STM32WB0_RADIO_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_STM32WB0_RADIO_TIMER)。

<a id="CONFIG_SYSTEM_TIMER_HAS_LPM_COMPANION_SUPPORT"></a>

## 8.10 `CONFIG_SYSTEM_TIMER_HAS_LPM_COMPANION_SUPPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

支持将低功耗计时（Low-power Timekeeping）委托给伴随定时器（Companion Timer）的系统定时器驱动应选择此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SYS_CLOCK_EXISTS
```

**被选择（Selected by）**

```text
CONFIG_CORTEX_M_SYSTICK
CONFIG_MCUX_OS_TIMER
```

**定义位置（Location）**：[`drivers/timer/Kconfig.system_timer_lpm:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.system_timer_lpm#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_CORTEX_M_SYSTICK`](P007_drivers_timer_配置项参考_1.md#CONFIG_CORTEX_M_SYSTICK)、[`CONFIG_MCUX_OS_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_MCUX_OS_TIMER)。

<a id="CONFIG_SYSTEM_TIMER_LPM_COMPANION"></a>

## 8.11 `CONFIG_SYSTEM_TIMER_LPM_COMPANION`

**提示（Prompt）**：系统定时器低功耗伴随定时器（Low-power Companion）

**说明（Help）**

在某些平台上，最适合用作活动系统定时器（Active System Timer）的定时器，在系统处于低功耗状态时无法继续计时。另一个独立定时器可能在这些状态下保持活动，但例如因分辨率较低，仍不适合用作主系统定时器（Primary System Timer）。通过此选项，主系统定时器可在低功耗状态转换期间将计时交给低功耗伴随定时器（Low-power Companion），并在唤醒时恢复已经过的时间。

注意：如果 SoC 可能进入低功耗模式，必须启用电源管理（Power Management，PM），因此未启用 PM 时不能选择任何低功耗模式（LPM）伴随定时器。还必须启用无滴答内核（Tickless Kernel），因为周期性中断会阻止系统进入低功耗模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
CONFIG_SYSTEM_TIMER_LPM_COMPANION_COUNTER if CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_COUNTER
CONFIG_SYSTEM_TIMER_LPM_COMPANION_HOOKS if CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_HOOKS
CONFIG_SYSTEM_TIMER_LPM_COMPANION_NONE if CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_NONE
CONFIG_SYSTEM_TIMER_LPM_COMPANION_COUNTER
```

**可选项（Choices）**

```text
CONFIG_SYSTEM_TIMER_LPM_COMPANION_NONE
CONFIG_SYSTEM_TIMER_LPM_COMPANION_COUNTER
CONFIG_SYSTEM_TIMER_LPM_COMPANION_HOOKS
```

**定义位置（Location）**：[`drivers/timer/Kconfig.system_timer_lpm:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.system_timer_lpm#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_SYSTEM_TIMER_LPM_COMPANION_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_LPM_COMPANION_COUNTER)、[`CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_COUNTER`](P007_drivers_timer_配置项参考_1.md#CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_COUNTER)、[`CONFIG_SYSTEM_TIMER_LPM_COMPANION_HOOKS`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_LPM_COMPANION_HOOKS)、[`CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_HOOKS`](P007_drivers_timer_配置项参考_1.md#CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_HOOKS)、[`CONFIG_SYSTEM_TIMER_LPM_COMPANION_NONE`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_LPM_COMPANION_NONE)、[`CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_NONE`](P007_drivers_timer_配置项参考_1.md#CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_NONE)。

<a id="CONFIG_SYSTEM_TIMER_LPM_COMPANION_COUNTER"></a>

## 8.12 `CONFIG_SYSTEM_TIMER_LPM_COMPANION_COUNTER`

**提示（Prompt）**：计数器 API（Counter API）定时器

**说明（Help）**

使用实现计数器 API（Counter API）的设备作为系统定时器的低功耗伴随定时器（Low-power Companion）。该设备通过设备树 `chosen` 属性 `/chosen/zephyr,system-timer-companion` 选择。旧版兼容属性 `/chosen/zephyr,cortex-m-idle-timer` 已弃用，但仍被接受。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(n || n) && CONFIG_COUNTER && CONFIG_SYSTEM_TIMER_HAS_LPM_COMPANION_SUPPORT && CONFIG_TICKLESS_KERNEL && CONFIG_PM && <choice CONFIG_SYSTEM_TIMER_LPM_COMPANION>
```

**定义位置（Location）**：[`drivers/timer/Kconfig.system_timer_lpm:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.system_timer_lpm#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → 系统定时器低功耗伴随定时器（Low-power Companion）

**配置项引用（Symbol References）**：[`CONFIG_COUNTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER)、[`CONFIG_SYSTEM_TIMER_HAS_LPM_COMPANION_SUPPORT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_HAS_LPM_COMPANION_SUPPORT)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SYSTEM_TIMER_LPM_COMPANION`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_LPM_COMPANION)。

<a id="CONFIG_SYSTEM_TIMER_LPM_COMPANION_HOOKS"></a>

## 8.13 `CONFIG_SYSTEM_TIMER_LPM_COMPANION_HOOKS`

**提示（Prompt）**：基于钩子的定时器（Hook-based Timer）

**说明（Help）**

使用平台钩子（Platform Hook）配置系统定时器的低功耗伴随定时器（Low-power Companion）。更多详情参见 `include/zephyr/drivers/timer/system_timer_lpm.h`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SYSTEM_TIMER_HAS_LPM_COMPANION_SUPPORT && CONFIG_TICKLESS_KERNEL && CONFIG_PM && <choice CONFIG_SYSTEM_TIMER_LPM_COMPANION>
```

**定义位置（Location）**：[`drivers/timer/Kconfig.system_timer_lpm:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.system_timer_lpm#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → 系统定时器低功耗伴随定时器（Low-power Companion）

**配置项引用（Symbol References）**：[`CONFIG_SYSTEM_TIMER_HAS_LPM_COMPANION_SUPPORT`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_HAS_LPM_COMPANION_SUPPORT)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_SYSTEM_TIMER_LPM_COMPANION`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_LPM_COMPANION)。

<a id="CONFIG_SYSTEM_TIMER_LPM_COMPANION_NONE"></a>

## 8.14 `CONFIG_SYSTEM_TIMER_LPM_COMPANION_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**

不使用附加设备作为系统定时器的低功耗伴随定时器（Low-power Companion）。选择此选项后，平台绝不能进入活动系统定时器无法继续计时的低功耗模式，否则系统行为将不可预测。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYSTEM_TIMER_LPM_COMPANION>
```

**定义位置（Location）**：[`drivers/timer/Kconfig.system_timer_lpm:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.system_timer_lpm#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → 系统定时器低功耗伴随定时器（Low-power Companion）

**配置项引用（Symbol References）**：[`CONFIG_SYSTEM_TIMER_LPM_COMPANION`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_LPM_COMPANION)。

<a id="CONFIG_SYSTEM_TIMER_RESET_BY_LPM"></a>

## 8.15 `CONFIG_SYSTEM_TIMER_RESET_BY_LPM`

**提示（Prompt）**：低功耗模式复位系统定时器（System Timer Reset by Low-power Mode）

**说明（Help）**

某些平台提供一种或多种低功耗模式（Low-power Mode），这些模式在运行过程中会使活动系统定时器（Active System Timer）处于复位状态。这需要驱动特别处理，尤其是在唤醒后重新启动定时器并重建已经过的时间。如果平台可能进入此类低功耗模式，且需要系统定时器低功耗伴随定时器（Low-power Companion）来保证可靠计时，请选择此选项。更多详情参见 `CONFIG_SYSTEM_TIMER_LPM_COMPANION`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SYSTEM_TIMER_LPM_COMPANION_NONE && CONFIG_SYS_CLOCK_EXISTS
```

**被选择（Selected by）**

```text
CONFIG_CORTEX_M_SYSTICK_RESET_BY_LPM
```

**定义位置（Location）**：[`drivers/timer/Kconfig.system_timer_lpm:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.system_timer_lpm#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYSTEM_TIMER_LPM_COMPANION_NONE`](P008_drivers_timer_配置项参考_2.md#CONFIG_SYSTEM_TIMER_LPM_COMPANION_NONE)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_CORTEX_M_SYSTICK_RESET_BY_LPM`](P007_drivers_timer_配置项参考_1.md#CONFIG_CORTEX_M_SYSTICK_RESET_BY_LPM)。

<a id="CONFIG_TICKLESS_CAPABLE"></a>

## 8.16 `CONFIG_TICKLESS_CAPABLE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

支持无滴答运行（Tickless Operation）的定时器驱动应选择此标志。也就是说，使用大于 1 的滴答数调用 `sys_clock_set_timeout()` 后，在指定的到期时间之前，不应调用 `sys_clock_announce()`；实际上，在此之前根本不应产生中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SYS_CLOCK_EXISTS
```

**被选择（Selected by）**

```text
CONFIG_AMBIQ_STIMER_TIMER
CONFIG_AMD_TMRCTR
CONFIG_ARCV2_TIMER
CONFIG_ARM_ARCH_TIMER
CONFIG_INTEL_ADSP_TIMER
CONFIG_CC13XX_CC26XX_RTC_TIMER
CONFIG_CC23X0_SYSTIM_TIMER
CONFIG_CC23X0_RTC_TIMER
CONFIG_CORTEX_M_SYSTICK
CONFIG_ESP32_SYS_TIMER
CONFIG_GECKO_BURTC_TIMER
CONFIG_HEXAGON_TIMER
CONFIG_AURIX_STM
CONFIG_INFINEON_LP_TIMER_HAL
CONFIG_INFINEON_LP_TIMER_PDL
CONFIG_ITE_IT51XXX_TIMER
CONFIG_ITE_IT8XXX2_TIMER
CONFIG_LEON_GPTIMER
CONFIG_MAX32_RV32_SYS_TIMER
CONFIG_MAX32_WUT_TIMER
CONFIG_MCHP_SAM_PIT64B_TIMER
CONFIG_MCHP_XEC_RTOS_TIMER
CONFIG_MCUX_GPT_TIMER
CONFIG_MCUX_OS_TIMER
CONFIG_MIPS_CP0_TIMER
CONFIG_MTK_ADSP_TIMER
CONFIG_NATIVE_SIM_TIMER
CONFIG_NPCX_ITIM_TIMER
CONFIG_NRF_GRTC_TIMER
CONFIG_NRF_RTC_TIMER
CONFIG_OPENRISC_TICK_TIMER
CONFIG_REALTEK_RTS5912_RTMR
CONFIG_RENESAS_RA_ULPT_TIMER
CONFIG_RENESAS_RX_TIMER_CMT
CONFIG_RZ_OS_TIMER
CONFIG_RZA2M_OSTM_TIMER
CONFIG_RISCV_MACHINE_TIMER
CONFIG_RISCV_SUPERVISOR_TIMER
CONFIG_SAM0_RTC_TIMER
CONFIG_SMARTBOND_TIMER
CONFIG_STM32WB0_RADIO_TIMER
CONFIG_HPET_TIMER
CONFIG_APIC_TSC_DEADLINE_TIMER
CONFIG_APIC_TIMER_TSC
CONFIG_XLNX_PSTTC_TIMER
CONFIG_XTENSA_TIMER
```

**定义位置（Location）**：[`drivers/timer/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_AMBIQ_STIMER_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_AMBIQ_STIMER_TIMER)、[`CONFIG_AMD_TMRCTR`](P007_drivers_timer_配置项参考_1.md#CONFIG_AMD_TMRCTR)、[`CONFIG_ARCV2_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_ARCV2_TIMER)、[`CONFIG_ARM_ARCH_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_ARM_ARCH_TIMER)、[`CONFIG_INTEL_ADSP_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_INTEL_ADSP_TIMER)、[`CONFIG_CC13XX_CC26XX_RTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_CC13XX_CC26XX_RTC_TIMER)、[`CONFIG_CC23X0_SYSTIM_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_CC23X0_SYSTIM_TIMER)、[`CONFIG_CC23X0_RTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_CC23X0_RTC_TIMER)、[`CONFIG_CORTEX_M_SYSTICK`](P007_drivers_timer_配置项参考_1.md#CONFIG_CORTEX_M_SYSTICK)、[`CONFIG_ESP32_SYS_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_ESP32_SYS_TIMER)、[`CONFIG_GECKO_BURTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_GECKO_BURTC_TIMER)、[`CONFIG_HEXAGON_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_HEXAGON_TIMER)、[`CONFIG_AURIX_STM`](P007_drivers_timer_配置项参考_1.md#CONFIG_AURIX_STM)、[`CONFIG_INFINEON_LP_TIMER_HAL`](P007_drivers_timer_配置项参考_1.md#CONFIG_INFINEON_LP_TIMER_HAL)、[`CONFIG_INFINEON_LP_TIMER_PDL`](P007_drivers_timer_配置项参考_1.md#CONFIG_INFINEON_LP_TIMER_PDL)、[`CONFIG_ITE_IT51XXX_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_ITE_IT51XXX_TIMER)、[`CONFIG_ITE_IT8XXX2_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_ITE_IT8XXX2_TIMER)、[`CONFIG_LEON_GPTIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_LEON_GPTIMER)、[`CONFIG_MAX32_RV32_SYS_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_MAX32_RV32_SYS_TIMER)、[`CONFIG_MAX32_WUT_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_MAX32_WUT_TIMER)、[`CONFIG_MCHP_SAM_PIT64B_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_MCHP_SAM_PIT64B_TIMER)、[`CONFIG_MCHP_XEC_RTOS_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_MCHP_XEC_RTOS_TIMER)、[`CONFIG_MCUX_GPT_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_MCUX_GPT_TIMER)、[`CONFIG_MCUX_OS_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_MCUX_OS_TIMER)、[`CONFIG_MIPS_CP0_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_MIPS_CP0_TIMER)、[`CONFIG_MTK_ADSP_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_MTK_ADSP_TIMER)、[`CONFIG_NATIVE_SIM_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NATIVE_SIM_TIMER)、[`CONFIG_NPCX_ITIM_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NPCX_ITIM_TIMER)、[`CONFIG_NRF_GRTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER)、[`CONFIG_NRF_RTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_RTC_TIMER)、[`CONFIG_OPENRISC_TICK_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_OPENRISC_TICK_TIMER)、[`CONFIG_REALTEK_RTS5912_RTMR`](P007_drivers_timer_配置项参考_1.md#CONFIG_REALTEK_RTS5912_RTMR)、[`CONFIG_RENESAS_RA_ULPT_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_RENESAS_RA_ULPT_TIMER)、[`CONFIG_RENESAS_RX_TIMER_CMT`](P007_drivers_timer_配置项参考_1.md#CONFIG_RENESAS_RX_TIMER_CMT)、[`CONFIG_RZ_OS_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_RZ_OS_TIMER)、[`CONFIG_RZA2M_OSTM_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_RZA2M_OSTM_TIMER)、[`CONFIG_RISCV_MACHINE_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_RISCV_MACHINE_TIMER)、[`CONFIG_RISCV_SUPERVISOR_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_RISCV_SUPERVISOR_TIMER)、[`CONFIG_SAM0_RTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_SAM0_RTC_TIMER)、[`CONFIG_SMARTBOND_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_SMARTBOND_TIMER)、[`CONFIG_STM32WB0_RADIO_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_STM32WB0_RADIO_TIMER)、[`CONFIG_HPET_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_HPET_TIMER)、[`CONFIG_APIC_TSC_DEADLINE_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_APIC_TSC_DEADLINE_TIMER)、[`CONFIG_APIC_TIMER_TSC`](P007_drivers_timer_配置项参考_1.md#CONFIG_APIC_TIMER_TSC)、[`CONFIG_XLNX_PSTTC_TIMER`](P008_drivers_timer_配置项参考_2.md#CONFIG_XLNX_PSTTC_TIMER)、[`CONFIG_XTENSA_TIMER`](P008_drivers_timer_配置项参考_2.md#CONFIG_XTENSA_TIMER)。

<a id="CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER"></a>

## 8.17 `CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用此选项时，可调用 `k_cycle_get_64()`，从 64 位周期计数器（Cycle Counter）获取数值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SYS_CLOCK_EXISTS
```

**被选择（Selected by）**

```text
CONFIG_AMD_TMRCTR
CONFIG_ARM_ARCH_TIMER
CONFIG_INTEL_ADSP_TIMER
CONFIG_CC13XX_CC26XX_RTC_TIMER
CONFIG_CORTEX_M_SYSTICK_64BIT_CYCLE_COUNTER
CONFIG_ESP32_SYS_TIMER
CONFIG_HEXAGON_TIMER
CONFIG_AURIX_STM
CONFIG_LITEX_TIMER
CONFIG_MCUX_OS_TIMER
CONFIG_MTK_ADSP_TIMER
CONFIG_NATIVE_SIM_TIMER
CONFIG_NPCX_ITIM_TIMER
CONFIG_NRF_GRTC_TIMER
CONFIG_RENESAS_RX_TIMER_CMT
CONFIG_RISCV_MACHINE_TIMER
CONFIG_RISCV_SUPERVISOR_TIMER
CONFIG_HPET_TIMER
CONFIG_APIC_TIMER
CONFIG_APIC_TSC_DEADLINE_TIMER
CONFIG_APIC_TIMER_TSC
CONFIG_XTENSA_TIMER
```

**定义位置（Location）**：[`drivers/timer/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_AMD_TMRCTR`](P007_drivers_timer_配置项参考_1.md#CONFIG_AMD_TMRCTR)、[`CONFIG_ARM_ARCH_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_ARM_ARCH_TIMER)、[`CONFIG_INTEL_ADSP_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_INTEL_ADSP_TIMER)、[`CONFIG_CC13XX_CC26XX_RTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_CC13XX_CC26XX_RTC_TIMER)、[`CONFIG_CORTEX_M_SYSTICK_64BIT_CYCLE_COUNTER`](P007_drivers_timer_配置项参考_1.md#CONFIG_CORTEX_M_SYSTICK_64BIT_CYCLE_COUNTER)、[`CONFIG_ESP32_SYS_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_ESP32_SYS_TIMER)、[`CONFIG_HEXAGON_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_HEXAGON_TIMER)、[`CONFIG_AURIX_STM`](P007_drivers_timer_配置项参考_1.md#CONFIG_AURIX_STM)、[`CONFIG_LITEX_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_LITEX_TIMER)、[`CONFIG_MCUX_OS_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_MCUX_OS_TIMER)、[`CONFIG_MTK_ADSP_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_MTK_ADSP_TIMER)、[`CONFIG_NATIVE_SIM_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NATIVE_SIM_TIMER)、[`CONFIG_NPCX_ITIM_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NPCX_ITIM_TIMER)、[`CONFIG_NRF_GRTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_NRF_GRTC_TIMER)、[`CONFIG_RENESAS_RX_TIMER_CMT`](P007_drivers_timer_配置项参考_1.md#CONFIG_RENESAS_RX_TIMER_CMT)、[`CONFIG_RISCV_MACHINE_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_RISCV_MACHINE_TIMER)、[`CONFIG_RISCV_SUPERVISOR_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_RISCV_SUPERVISOR_TIMER)、[`CONFIG_HPET_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_HPET_TIMER)、[`CONFIG_APIC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_APIC_TIMER)、[`CONFIG_APIC_TSC_DEADLINE_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_APIC_TSC_DEADLINE_TIMER)、[`CONFIG_APIC_TIMER_TSC`](P007_drivers_timer_配置项参考_1.md#CONFIG_APIC_TIMER_TSC)、[`CONFIG_XTENSA_TIMER`](P008_drivers_timer_配置项参考_2.md#CONFIG_XTENSA_TIMER)。

<a id="CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME"></a>

## 8.18 `CONFIG_TIMER_READS_ITS_FREQUENCY_AT_RUNTIME`

**提示（Prompt）**：定时器在运行时查询硬件以确定频率（Frequency）

**说明（Help）**

驱动会在需要时自动选择此选项。除非有充分理由，否则不要修改。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SYS_CLOCK_EXISTS
```

**被选择（Selected by）**

```text
CONFIG_SOC_NEORV32_READ_FREQUENCY_AT_RUNTIME
CONFIG_SOC_MT8188_A55
CONFIG_GECKO_BURTC_TIMER
CONFIG_HEXAGON_TIMER
CONFIG_RZ_OS_TIMER
CONFIG_RZA2M_OSTM_TIMER
```

**被弱选择（Implied by）**

```text
CONFIG_SOC_SERIES_DA1469X
CONFIG_HPET_TIMER
```

**定义位置（Location）**：[`drivers/timer/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_SOC_NEORV32_READ_FREQUENCY_AT_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NEORV32_READ_FREQUENCY_AT_RUNTIME)、[`CONFIG_SOC_MT8188_A55`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MT8188_A55)、[`CONFIG_GECKO_BURTC_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_GECKO_BURTC_TIMER)、[`CONFIG_HEXAGON_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_HEXAGON_TIMER)、[`CONFIG_RZ_OS_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_RZ_OS_TIMER)、[`CONFIG_RZA2M_OSTM_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_RZA2M_OSTM_TIMER)、[`CONFIG_SOC_SERIES_DA1469X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_DA1469X)、[`CONFIG_HPET_TIMER`](P007_drivers_timer_配置项参考_1.md#CONFIG_HPET_TIMER)。

<a id="CONFIG_TI_DM_TIMER"></a>

## 8.19 `CONFIG_TI_DM_TIMER`

**提示（Prompt）**：TI 双模式定时器（Dual-Mode Timer）

**说明（Help）**

此模块为 TI 双模式定时器（Dual-Mode Timer）实现内核设备驱动。该驱动提供系统滴答（System Tick）接口。

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
CONFIG_SYSCON
```

**定义位置（Location）**：[`drivers/timer/Kconfig.ti_dm_timer:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.ti_dm_timer#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_SYSCON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSCON)。

<a id="CONFIG_TI_RTI_TIMER"></a>

## 8.20 `CONFIG_TI_RTI_TIMER`

**提示（Prompt）**：TI RTI 定时器（Timer）

**说明（Help）**

此模块为 TI RTI 定时器实现内核设备驱动。该驱动提供系统滴答（System Tick）接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_AM26_RTITIMER_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/timer/Kconfig.ti_rti_timer:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.ti_rti_timer#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_XLNX_PSTTC_TIMER"></a>

## 8.21 `CONFIG_XLNX_PSTTC_TIMER`

**提示（Prompt）**：Xilinx PS 三重定时器计数器（Triple-Timer Counter）支持

**说明（Help）**

为 Zynq UltraScale+ MPSoC（ZynqMP）和 Versal 平台启用 AMD Xilinx PS 三重定时器计数器（Triple Timer Counter，TTC）驱动。此基于 TTC 的定时器驱动提供标准系统时钟驱动（System Clock Driver）接口。若禁用，TTC 将不被用作系统定时器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_TTCPS_ENABLED && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TICKLESS_CAPABLE
```

**定义位置（Location）**：[`drivers/timer/Kconfig.xlnx_psttc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.xlnx_psttc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)。

<a id="CONFIG_XTENSA_TIMER"></a>

## 8.22 `CONFIG_XTENSA_TIMER`

**提示（Prompt）**：Xtensa 定时器（Timer）支持

**说明（Help）**

启用基于 `CCOUNT` 和 `CCOMPARE` 特殊寄存器（Special Register）的 Xtensa 系统定时器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA && CONFIG_SYS_CLOCK_EXISTS
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

**定义位置（Location）**：[`drivers/timer/Kconfig.xtensa:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.xtensa#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_TICKLESS_CAPABLE`](P008_drivers_timer_配置项参考_2.md#CONFIG_TICKLESS_CAPABLE)、[`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER`](P008_drivers_timer_配置项参考_2.md#CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER)。

<a id="CONFIG_XTENSA_TIMER_ID"></a>

## 8.23 `CONFIG_XTENSA_TIMER_ID`

**提示（Prompt）**：系统定时器 `CCOMPAREn` 寄存器索引（Register Index）

**说明（Help）**

用于系统定时器的 `CCOMPARE` 寄存器及其关联中断的索引（Index）。Xtensa CPU 为每个定时器硬件固定了中断优先级（Interrupt Priority），其中有些可能不可屏蔽，因此无法供定时器子系统等需要同步的 OS 代码使用。通常可以保证定时器 0 存在且可用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/timer/Kconfig.xtensa:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.xtensa#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → Xtensa 定时器（Timer）支持

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_TIMER`](P008_drivers_timer_配置项参考_2.md#CONFIG_XTENSA_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)。

<a id="CONFIG_XTENSA_TIMER_LPM_TIMER"></a>

## 8.24 `CONFIG_XTENSA_TIMER_LPM_TIMER`

**提示（Prompt）**：Xtensa CCOUNT 低功耗模式（Low-power Mode）支持

**说明（Help）**

低功耗模式（Low-power Mode）下，CPU 时钟被门控（Gated）时，CCOUNT 会停止。可使用仍保持活动的伴随定时器（Companion Timer）补偿丢失的周期。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA_TIMER && CONFIG_SYS_CLOCK_EXISTS
```

**默认值（Defaults）**

```text
CONFIG_XTENSA_TIMER_LPM_TIMER_NONE
```

**可选项（Choices）**

```text
CONFIG_XTENSA_TIMER_LPM_TIMER_NONE
CONFIG_XTENSA_TIMER_LPM_TIMER_HOOK
```

**定义位置（Location）**：[`drivers/timer/Kconfig.xtensa:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.xtensa#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → Xtensa 定时器（Timer）支持

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_TIMER`](P008_drivers_timer_配置项参考_2.md#CONFIG_XTENSA_TIMER)、[`CONFIG_SYS_CLOCK_EXISTS`](P002_kernel_配置项参考_2.md#CONFIG_SYS_CLOCK_EXISTS)、[`CONFIG_XTENSA_TIMER_LPM_TIMER_NONE`](P008_drivers_timer_配置项参考_2.md#CONFIG_XTENSA_TIMER_LPM_TIMER_NONE)、[`CONFIG_XTENSA_TIMER_LPM_TIMER_HOOK`](P008_drivers_timer_配置项参考_2.md#CONFIG_XTENSA_TIMER_LPM_TIMER_HOOK)。

<a id="CONFIG_XTENSA_TIMER_LPM_TIMER_HOOK"></a>

## 8.25 `CONFIG_XTENSA_TIMER_LPM_TIMER_HOOK`

**提示（Prompt）**：基于钩子的补偿（Hook-based Compensation）

**说明（Help）**

平台提供一个钩子（Hook），返回低功耗模式下 CCOUNT 停止期间丢失的 CPU 周期数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM && CONFIG_TICKLESS_KERNEL && <choice CONFIG_XTENSA_TIMER_LPM_TIMER>
```

**定义位置（Location）**：[`drivers/timer/Kconfig.xtensa:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.xtensa#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → Xtensa 定时器（Timer）支持 → Xtensa CCOUNT 低功耗模式（Low-power Mode）支持

**配置项引用（Symbol References）**：[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_XTENSA_TIMER_LPM_TIMER`](P008_drivers_timer_配置项参考_2.md#CONFIG_XTENSA_TIMER_LPM_TIMER)。

<a id="CONFIG_XTENSA_TIMER_LPM_TIMER_NONE"></a>

## 8.26 `CONFIG_XTENSA_TIMER_LPM_TIMER_NONE`

**提示（Prompt）**：无补偿（No Compensation）

**说明（Help）**

不使用附加设备作为低功耗模式定时器（Low-power Mode Timer）。选择此选项后，SoC 绝不能进入会使 CCOUNT 停止的低功耗模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_XTENSA_TIMER_LPM_TIMER>
```

**定义位置（Location）**：[`drivers/timer/Kconfig.xtensa:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/timer/Kconfig.xtensa#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 定时器驱动（Timer Drivers） → Xtensa 定时器（Timer）支持 → Xtensa CCOUNT 低功耗模式（Low-power Mode）支持

**配置项引用（Symbol References）**：[`CONFIG_XTENSA_TIMER_LPM_TIMER`](P008_drivers_timer_配置项参考_2.md#CONFIG_XTENSA_TIMER_LPM_TIMER)。

<!-- kconfig-navigation -->

[上一章](P007_drivers_timer_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P009_module_cmsis-dsp_zephyr_配置项参考.md)
