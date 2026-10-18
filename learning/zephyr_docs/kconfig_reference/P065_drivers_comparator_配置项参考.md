---
id: learning.zephyr-docs.kconfig-reference.page-65
title: "`drivers/comparator`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第65章\_`drivers/comparator`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/comparator` 的 30 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_COMPARATOR"></a>

## 65.1 `CONFIG_COMPARATOR`

**提示（Prompt）**：比较器驱动（Comparator Drivers）

**说明（Help）**

启用比较器（Comparator）驱动配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/comparator/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_COMPARATOR_ESP32_ANA_CMPR"></a>

## 65.2 `CONFIG_COMPARATOR_ESP32_ANA_CMPR`

**提示（Prompt）**：ESP32 模拟比较器驱动，ana_cmpr（Analog Comparator Driver）

**说明（Help）**

启用乐鑫（Espressif）模拟比较器（Analog Comparator，`ana_cmpr`）外设驱动，该外设存在于 ESP32-P4、ESP32-C5 和 ESP32-H2 片上系统（SoC）中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_ANA_CMPR_ENABLED && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.esp32_ana_cmpr:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.esp32_ana_cmpr#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)。

<a id="CONFIG_COMPARATOR_FAKE_COMP"></a>

## 65.3 `CONFIG_COMPARATOR_FAKE_COMP`

**提示（Prompt）**：模拟比较器驱动（Fake comparator driver）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_FAKE_COMP_ENABLED && CONFIG_ZTEST && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.fake_comp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.fake_comp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST)、[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)。

<a id="CONFIG_COMPARATOR_INFINEON_AUTANALOG_PTCOMP"></a>

## 65.4 `CONFIG_COMPARATOR_INFINEON_AUTANALOG_PTCOMP`

**提示（Prompt）**：英飞凌 AutAnalog PTComp 比较器驱动（Infineon Comparator Driver）

**说明（Help）**

启用英飞凌（Infineon）AutAnalog PTComp 比较器（Comparator）驱动。每个实例提供一个比较器输出，即 Comp0 或 Comp1，并可配置输入多路选择路由（Input Mux Routing）、功耗模式（Power Mode）和迟滞（Hysteresis）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_AUTANALOG_PTCOMP_COMP_ENABLED && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.infineon_autanalog_ptcomp:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.infineon_autanalog_ptcomp#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_MFD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD)。

<a id="CONFIG_COMPARATOR_INFINEON_AUTANALOG_PTCOMP_INIT_PRIORITY"></a>

## 65.5 `CONFIG_COMPARATOR_INFINEON_AUTANALOG_PTCOMP_INIT_PRIORITY`

**提示（Prompt）**：英飞凌 AutAnalog PTComp 比较器初始化优先级（Init Priority）

**说明（Help）**

PTComp 比较器（Comparator）驱动的初始化优先级。数值必须大于 PTComp 多功能设备（MFD）的初始化优先级，后者默认为 42，即比较器应更晚初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COMPARATOR_INFINEON_AUTANALOG_PTCOMP && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
43
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.infineon_autanalog_ptcomp:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.infineon_autanalog_ptcomp#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers） → 英飞凌 AutAnalog PTComp 比较器驱动（Infineon Comparator Driver）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR_INFINEON_AUTANALOG_PTCOMP`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR_INFINEON_AUTANALOG_PTCOMP)、[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)。

<a id="CONFIG_COMPARATOR_INFINEON_HPPASS_CSG"></a>

## 65.6 `CONFIG_COMPARATOR_INFINEON_HPPASS_CSG`

**提示（Prompt）**：英飞凌 HPPASS CSG 比较器驱动（Infineon Comparator Driver）

**说明（Help）**

启用英飞凌（Infineon）HPPASS CSG 模块的比较器（Comparator）驱动。每个实例为一个 CSG 切片（Slice）提供标准 Zephyr 比较器 API。CSG 多功能设备（MFD）父设备负责合并的比较器中断，并分发通过此驱动注册的各切片回调（Per-Slice Callback）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_HPPASS_CSG_COMP_ENABLED && CONFIG_MFD_INFINEON_HPPASS_CSG && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.infineon_hppass_csg:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.infineon_hppass_csg#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MFD_INFINEON_HPPASS_CSG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MFD_INFINEON_HPPASS_CSG)、[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)。

<a id="CONFIG_COMPARATOR_INFINEON_HPPASS_CSG_INIT_PRIORITY"></a>

## 65.7 `CONFIG_COMPARATOR_INFINEON_HPPASS_CSG_INIT_PRIORITY`

**提示（Prompt）**：英飞凌 HPPASS CSG 比较器初始化优先级（Init Priority）

**说明（Help）**

每个切片的比较器子驱动（Comparator Child Driver）的初始化优先级。数值必须大于 `CONFIG_MFD_INFINEON_HPPASS_CSG_INIT_PRIORITY`，即更晚初始化，以确保本驱动运行前，CSG 多功能设备（MFD）父设备已能接受回调注册（Callback Registration）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COMPARATOR_INFINEON_HPPASS_CSG && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.infineon_hppass_csg:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.infineon_hppass_csg#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers） → 英飞凌 HPPASS CSG 比较器驱动（Infineon Comparator Driver）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR_INFINEON_HPPASS_CSG`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR_INFINEON_HPPASS_CSG)、[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)。

<a id="CONFIG_COMPARATOR_INFINEON_LPCOMP"></a>

## 65.8 `CONFIG_COMPARATOR_INFINEON_LPCOMP`

**提示（Prompt）**：英飞凌低功耗比较器驱动（Infineon LPCOMP Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_LP_COMP_ENABLED && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_LPCOMP
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.infineon_lpcomp:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.infineon_lpcomp#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_USE_INFINEON_LPCOMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_LPCOMP)。

<a id="CONFIG_COMPARATOR_INIT_PRIORITY"></a>

## 65.9 `CONFIG_COMPARATOR_INIT_PRIORITY`

**提示（Prompt）**：比较器初始化优先级（COMPARATOR Init Priority）

**说明（Help）**

比较器（Comparator）设备驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/comparator/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_COMPARATOR_IT51XXX_VCMP"></a>

## 65.10 `CONFIG_COMPARATOR_IT51XXX_VCMP`

**提示（Prompt）**：ITE IT51xxx 电压比较器（Voltage Comparator）

**说明（Help）**

启用 ITE IT51xxx 电压比较器（Voltage Comparator）。IT51xxx 支持三个具有 10 位阈值的电压比较器通道，每个比较器的输入来自模数转换器（ADC）引脚。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADC_ITE_IT51XXX && DT_HAS_ITE_IT51XXX_VCMP_ENABLED && CONFIG_DYNAMIC_INTERRUPTS && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.it51xxx_vcmp:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.it51xxx_vcmp#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ADC_ITE_IT51XXX`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_ITE_IT51XXX)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)。

<a id="CONFIG_COMPARATOR_MCHP_AC_G1"></a>

## 65.11 `CONFIG_COMPARATOR_MCHP_AC_G1`

**提示（Prompt）**：Microchip AC G1 外设比较器驱动（Comparator Driver）

**说明（Help）**

启用 Microchip G1 模拟比较器（AC）外设的比较器驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_AC_G1_COMPARATOR_ENABLED && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_COMPARATOR_MCUX_ACMP"></a>

## 65.12 `CONFIG_COMPARATOR_MCUX_ACMP`

**提示（Prompt）**：恩智浦 MCUX ACMP 比较器驱动（NXP Comparator Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KINETIS_ACMP_ENABLED && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.mcux_acmp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.mcux_acmp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_COMPARATOR_MSPM0"></a>

## 65.13 `CONFIG_COMPARATOR_MSPM0`

**提示（Prompt）**：TI MSPM0 比较器驱动（Comparator Driver）

**说明（Help）**

启用德州仪器（Texas Instruments）MSPM0 系列比较器（Comparator）驱动，支持参考电压配置（Reference Voltage Configuration）和内部数模转换器（DAC）控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_MSPM0_COMPARATOR_ENABLED && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_SHARED_INTERRUPTS
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.mspm0_comp:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.mspm0_comp#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_SHARED_INTERRUPTS`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_SHARED_INTERRUPTS)。

<a id="CONFIG_COMPARATOR_MSPM0_WINDOW_MODE"></a>

## 65.14 `CONFIG_COMPARATOR_MSPM0_WINDOW_MODE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

窗口比较器模式（Window Comparator Mode），在 MSPM0G 系列上自动启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COMPARATOR_MSPM0 && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_MSPM0G
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.mspm0_comp:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.mspm0_comp#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers） → TI MSPM0 比较器驱动（Comparator Driver）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR_MSPM0`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR_MSPM0)、[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_SOC_SERIES_MSPM0G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM0G)。

<a id="CONFIG_COMPARATOR_NRF_COMP"></a>

## 65.15 `CONFIG_COMPARATOR_NRF_COMP`

**提示（Prompt）**：Nordic COMP 比较器驱动（Comparator Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_COMP_ENABLED && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_COMP
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.nrf_comp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.nrf_comp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_NRFX_COMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_COMP)。

<a id="CONFIG_COMPARATOR_NRF_LPCOMP"></a>

## 65.16 `CONFIG_COMPARATOR_NRF_LPCOMP`

**提示（Prompt）**：Nordic LPCOMP 比较器驱动（Comparator Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_LPCOMP_ENABLED && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_LPCOMP
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.nrf_lpcomp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.nrf_lpcomp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_NRFX_LPCOMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_LPCOMP)。

<a id="CONFIG_COMPARATOR_NXP_ACOMP"></a>

## 65.17 `CONFIG_COMPARATOR_NXP_ACOMP`

**提示（Prompt）**：恩智浦模拟比较器驱动（NXP Analog Comparator Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_ACOMP_ENABLED && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.nxp_acomp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.nxp_acomp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)。

<a id="CONFIG_COMPARATOR_NXP_CMP"></a>

## 65.18 `CONFIG_COMPARATOR_NXP_CMP`

**提示（Prompt）**：恩智浦比较器驱动（NXP Comparator Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_CMP_ENABLED && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.nxp_cmp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.nxp_cmp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_COMPARATOR_NXP_HSCMP"></a>

## 65.19 `CONFIG_COMPARATOR_NXP_HSCMP`

**提示（Prompt）**：恩智浦 HSCMP 比较器驱动（NXP Comparator Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_HSCMP_ENABLED && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_CLOCK_CONTROL
CONFIG_RESET
CONFIG_REGULATOR
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.nxp_hscmp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.nxp_hscmp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_REGULATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REGULATOR)。

<a id="CONFIG_COMPARATOR_NXP_LPACMP"></a>

## 65.20 `CONFIG_COMPARATOR_NXP_LPACMP`

**提示（Prompt）**：恩智浦 LPACMP 比较器驱动（NXP Comparator Driver）

**说明（Help）**

启用恩智浦（NXP）低功耗模拟比较器（Low-Power Analog Comparator，LPACMP）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPACMP_ENABLED && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.nxp_lpacmp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.nxp_lpacmp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_COMPARATOR_NXP_LPCMP"></a>

## 65.21 `CONFIG_COMPARATOR_NXP_LPCMP`

**提示（Prompt）**：恩智浦 LPCMP 比较器驱动（NXP Comparator Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPCMP_ENABLED && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.nxp_lpcmp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.nxp_lpcmp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_COMPARATOR_RENESAS_RA"></a>

## 65.22 `CONFIG_COMPARATOR_RENESAS_RA`

**提示（Prompt）**：瑞萨 RA ACMPHS（Renesas RA ACMPHS）

**说明（Help）**

启用瑞萨（Renesas）RA ACMPHS 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_ACMPHS_ENABLED && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_ACMPHS
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.renesas_ra:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.renesas_ra#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_USE_RA_FSP_ACMPHS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_ACMPHS)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_COMPARATOR_RENESAS_RA_LVD"></a>

## 65.23 `CONFIG_COMPARATOR_RENESAS_RA_LVD`

**提示（Prompt）**：瑞萨 RA 低电压检测（Renesas RA LVD）

**说明（Help）**

启用瑞萨（Renesas）RA 低电压检测（LVD）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_LVD_ENABLED && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_LVD
CONFIG_RUNTIME_NMI
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.renesas_ra:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.renesas_ra#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_USE_RA_FSP_LVD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_LVD)、[`CONFIG_RUNTIME_NMI`](P030_arch_arm_配置项参考_2.md#CONFIG_RUNTIME_NMI)。

<a id="CONFIG_COMPARATOR_RENESAS_RX_LVD"></a>

## 65.24 `CONFIG_COMPARATOR_RENESAS_RX_LVD`

**提示（Prompt）**：瑞萨 RX 低电压检测（Renesas RX LVD）

**说明（Help）**

为瑞萨（Renesas）RX 微控制器（MCU）启用具有低电压检测（Low Voltage Detection，LVD）功能的比较器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_LVD_ENABLED && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RX_RDP_LVD
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.renesas_rx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.renesas_rx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_USE_RX_RDP_LVD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RX_RDP_LVD)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_COMPARATOR_SHELL"></a>

## 65.25 `CONFIG_COMPARATOR_SHELL`

**提示（Prompt）**：比较器命令行（Comparator Shell）

**说明（Help）**

比较器（Comparator）设备驱动的命令行（Shell）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.shell:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.shell#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)。

<a id="CONFIG_COMPARATOR_SHELL_AWAIT_TRIGGER_DEFAULT_TIMEOUT"></a>

## 65.26 `CONFIG_COMPARATOR_SHELL_AWAIT_TRIGGER_DEFAULT_TIMEOUT`

**提示（Prompt）**：await_trigger 命令的默认超时，单位为秒（Default Timeout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COMPARATOR_SHELL && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.shell:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.shell#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers） → 比较器命令行（Comparator Shell）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR_SHELL`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR_SHELL)、[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)。

<a id="CONFIG_COMPARATOR_SHELL_AWAIT_TRIGGER_MAX_TIMEOUT"></a>

## 65.27 `CONFIG_COMPARATOR_SHELL_AWAIT_TRIGGER_MAX_TIMEOUT`

**提示（Prompt）**：await_trigger 命令的最大超时，单位为秒（Max Timeout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_COMPARATOR_SHELL && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
60
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.shell:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.shell#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers） → 比较器命令行（Comparator Shell）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR_SHELL`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR_SHELL)、[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)。

<a id="CONFIG_COMPARATOR_SILABS_ACMP"></a>

## 65.28 `CONFIG_COMPARATOR_SILABS_ACMP`

**提示（Prompt）**：Silicon Labs ACMP 比较器驱动（Comparator Driver）

**说明（Help）**

启用 Silicon Labs 器件中模拟比较器（Analog Comparator）硬件模块的驱动。该模块常用于监测电源（Power Supply）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_ACMP_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_SILABS_SISDK_ACMP
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.silabs_acmp:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.silabs_acmp#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_SILABS_SISDK_ACMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_ACMP)。

<a id="CONFIG_COMPARATOR_STM32_COMP"></a>

## 65.29 `CONFIG_COMPARATOR_STM32_COMP`

**提示（Prompt）**：ST STM32 比较器驱动（Comparator Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_COMP_ENABLED && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_EXTI_STM32
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.stm32_comp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.stm32_comp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_EXTI_STM32`](P005_drivers_interrupt_controller_配置项参考_1.md#CONFIG_EXTI_STM32)。

<a id="CONFIG_COMPARATOR_WCH_CH5XX"></a>

## 65.30 `CONFIG_COMPARATOR_WCH_CH5XX`

**提示（Prompt）**：沁恒 CH5xx 比较器驱动（WCH Comparator Driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_CH5XX_COMPARATOR_ENABLED && CONFIG_COMPARATOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/comparator/Kconfig.wch_ch5xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/comparator/Kconfig.wch_ch5xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 比较器驱动（Comparator Drivers）

**配置项引用（Symbol References）**：[`CONFIG_COMPARATOR`](P065_drivers_comparator_配置项参考.md#CONFIG_COMPARATOR)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<!-- kconfig-navigation -->

[上一章](P064_drivers_clock_monitor_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P066_drivers_console_配置项参考.md)
