---
id: learning.zephyr-docs.kconfig-reference.page-249
title: "`modules/segger`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第249章\_`modules/segger`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/segger` 的 25 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HAS_SEGGER_RTT"></a>

## 249.1 `CONFIG_HAS_SEGGER_RTT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示平台支持 SEGGER J-Link 实时传输（Real Time Transfer，RTT）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_KB106X
CONFIG_SOC_FT9001
CONFIG_SOC_FAMILY_LPC
CONFIG_SOC_FAMILY_MICROCHIP_MEC
CONFIG_SOC_FAMILY_ATMEL_SAM0
CONFIG_SOC_SERIES_RP2040
CONFIG_SOC_SERIES_RP2350
CONFIG_SOC_FAMILY_RENESAS_RA
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC
CONFIG_SOC_FAMILY_MCXA
CONFIG_SOC_FAMILY_MCXC
CONFIG_SOC_FAMILY_MCXN
CONFIG_SOC_FAMILY_MCXW
CONFIG_SOC_FAMILY_SILABS_S0
CONFIG_SOC_FAMILY_SILABS_S1
CONFIG_SOC_FAMILY_SILABS_S2
CONFIG_SOC_FAMILY_SILABS_S3
CONFIG_SOC_FAMILY_SILABS_SIM3
CONFIG_SOC_FAMILY_SILABS_SIWX91X
CONFIG_SOC_FAMILY_NXP_IMXRT
CONFIG_SOC_FAMILY_KINETIS
CONFIG_SOC_SERIES_NRF51
CONFIG_SOC_SERIES_NRF52
CONFIG_SOC_SERIES_NRF53
CONFIG_SOC_NRF54H20_CPUAPP_COMMON
CONFIG_SOC_NRF54H20_CPURAD_COMMON
CONFIG_SOC_SERIES_NRF54L
CONFIG_SOC_SERIES_NRF71
CONFIG_SOC_SERIES_NRF91
CONFIG_SOC_NRF9230_ENGB_CPUAPP
CONFIG_SOC_NRF9230_ENGB_CPURAD
CONFIG_SOC_FAMILY_NXP_IMX
CONFIG_SOC_FAMILY_INFINEON_EDGE
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL
CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG
CONFIG_SOC_SERIES_CYW20829
CONFIG_SOC_FAMILY_GD_GD32
CONFIG_SOC_SERIES_CC13X2_CC26X2
CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7
CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X
CONFIG_SOC_SERIES_DA1469X
CONFIG_SOC_FAMILY_RENESAS_RZ
CONFIG_SOC_FAMILY_ATMEL_SAM
CONFIG_SOC_FAMILY_INFINEON_XMC
CONFIG_SOC_FAMILY_REALTEK_BEE
CONFIG_SOC_FAMILY_MAX32
CONFIG_SOC_FAMILY_STM32
CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1
CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3
CONFIG_SOC_SERIES_RW6XX
CONFIG_SOC_SERIES_S32K1
CONFIG_SOC_SERIES_S32K3
```

**定义位置（Location）**：[`modules/segger/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_KB106X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KB106X)、[`CONFIG_SOC_FT9001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FT9001)、[`CONFIG_SOC_FAMILY_LPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_LPC)、[`CONFIG_SOC_FAMILY_MICROCHIP_MEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_MEC)、[`CONFIG_SOC_FAMILY_ATMEL_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM0)、[`CONFIG_SOC_SERIES_RP2040`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2040)、[`CONFIG_SOC_SERIES_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2350)、[`CONFIG_SOC_FAMILY_RENESAS_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RA)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC)、[`CONFIG_SOC_FAMILY_MCXA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXA)、[`CONFIG_SOC_FAMILY_MCXC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXC)、[`CONFIG_SOC_FAMILY_MCXN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXN)、[`CONFIG_SOC_FAMILY_MCXW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MCXW)、[`CONFIG_SOC_FAMILY_SILABS_S0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S0)、[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_FAMILY_SILABS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3)、[`CONFIG_SOC_FAMILY_SILABS_SIM3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIM3)、[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_SOC_FAMILY_NXP_IMXRT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMXRT)、[`CONFIG_SOC_FAMILY_KINETIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KINETIS)、[`CONFIG_SOC_SERIES_NRF51`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF51)、[`CONFIG_SOC_SERIES_NRF52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_SOC_SERIES_NRF53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPUAPP_COMMON)、[`CONFIG_SOC_NRF54H20_CPURAD_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20_CPURAD_COMMON)、[`CONFIG_SOC_SERIES_NRF54L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_SOC_SERIES_NRF71`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF71)、[`CONFIG_SOC_SERIES_NRF91`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF91)、[`CONFIG_SOC_NRF9230_ENGB_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPUAPP)、[`CONFIG_SOC_NRF9230_ENGB_CPURAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9230_ENGB_CPURAD)、[`CONFIG_SOC_FAMILY_NXP_IMX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NXP_IMX)、[`CONFIG_SOC_FAMILY_INFINEON_EDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_EDGE)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL)、[`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG)、[`CONFIG_SOC_SERIES_CYW20829`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYW20829)、[`CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_GD_GD32)、[`CONFIG_SOC_SERIES_CC13X2_CC26X2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC13X2_CC26X2)、[`CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC13X2X7_CC26X2X7)、[`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X)、[`CONFIG_SOC_SERIES_DA1469X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_DA1469X)、[`CONFIG_SOC_FAMILY_RENESAS_RZ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RZ)、[`CONFIG_SOC_FAMILY_ATMEL_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ATMEL_SAM)、[`CONFIG_SOC_FAMILY_INFINEON_XMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_INFINEON_XMC)、[`CONFIG_SOC_FAMILY_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_BEE)、[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M1)、[`CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_DESIGNSTART_FPGA_CORTEX_M3)、[`CONFIG_SOC_SERIES_RW6XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RW6XX)、[`CONFIG_SOC_SERIES_S32K1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K1)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_KB106X`、`CONFIG_SOC_FAMILY_LPC`、`CONFIG_SOC_FAMILY_MICROCHIP_MEC`、`CONFIG_SOC_FAMILY_ATMEL_SAM0`、`CONFIG_SOC_SERIES_RP2350`、`CONFIG_SOC_FAMILY_RENESAS_RA`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_SG_GC`、`CONFIG_SOC_FAMILY_MCXA`、`CONFIG_SOC_FAMILY_MCXC`、`CONFIG_SOC_FAMILY_MCXN`、`CONFIG_SOC_FAMILY_MCXW`、`CONFIG_SOC_FAMILY_SILABS_S0`、`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_FAMILY_SILABS_S2`、`CONFIG_SOC_FAMILY_SILABS_S3`、`CONFIG_SOC_FAMILY_SILABS_SIM3`、`CONFIG_SOC_FAMILY_SILABS_SIWX91X`、`CONFIG_SOC_FAMILY_NXP_IMXRT`、`CONFIG_SOC_FAMILY_KINETIS`、`CONFIG_SOC_NRF54H20_CPUAPP_COMMON`、`CONFIG_SOC_NRF54H20_CPURAD_COMMON`、`CONFIG_SOC_NRF9230_ENGB_CPUAPP`、`CONFIG_SOC_NRF9230_ENGB_CPURAD`、`CONFIG_SOC_FAMILY_NXP_IMX`、`CONFIG_SOC_FAMILY_INFINEON_EDGE`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_PL`、`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CX_SG`、`CONFIG_SOC_SERIES_CYW20829`、`CONFIG_SOC_FAMILY_GD_GD32`、`CONFIG_SOC_FAMILY_MICROCHIP_SAM_D5X_E5X`、`CONFIG_SOC_FAMILY_RENESAS_RZ`、`CONFIG_SOC_FAMILY_ATMEL_SAM`、`CONFIG_SOC_FAMILY_INFINEON_XMC`、`CONFIG_SOC_FAMILY_REALTEK_BEE`、`CONFIG_SOC_FAMILY_MAX32`、`CONFIG_SOC_FAMILY_STM32`、`CONFIG_SOC_SERIES_RW6XX`、`CONFIG_SOC_SERIES_S32K1`、`CONFIG_SOC_SERIES_S32K3`。

<a id="CONFIG_SEGGER_RTT_BUFFER_SIZE_DOWN"></a>

## 249.2 `CONFIG_SEGGER_RTT_BUFFER_SIZE_DOWN`

**提示（Prompt）**：目标端接收主机终端输入的缓冲区大小（terminal input buffer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SEGGER_RTT
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`modules/segger/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。

**配置项引用（Symbol References）**：[`CONFIG_USE_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_USE_SEGGER_RTT)。

<a id="CONFIG_SEGGER_RTT_BUFFER_SIZE_UP"></a>

## 249.3 `CONFIG_SEGGER_RTT_BUFFER_SIZE_UP`

**提示（Prompt）**：目标端向主机发送终端输出的缓冲区大小（terminal output buffer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SEGGER_RTT
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`modules/segger/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。

**配置项引用（Symbol References）**：[`CONFIG_USE_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_USE_SEGGER_RTT)。

<a id="CONFIG_SEGGER_RTT_CB_ALIGNMENT"></a>

## 249.4 `CONFIG_SEGGER_RTT_CB_ALIGNMENT`

**提示（Prompt）**：RTT 控制块对齐（control block alignment）

**说明（Help）**

指定 RTT 控制块（control block）在内存中的对齐方式。默认选择 16 字节对齐，是因为当 16 字节的 `acID` 字段跨越 32 字节边界时，PyOCD 无法发现该控制块。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SEGGER_RTT
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`modules/segger/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。

**配置项引用（Symbol References）**：[`CONFIG_USE_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_USE_SEGGER_RTT)。

<a id="CONFIG_SEGGER_RTT_CUSTOM_LOCKING"></a>

## 249.5 `CONFIG_SEGGER_RTT_CUSTOM_LOCKING`

**提示（Prompt）**：自定义加锁（Custom locking）

**说明（Help）**

启用使用 Zephyr API 的自定义加锁（custom locking）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SEGGER_RTT
```

**被选择（Selected by）**

```text
CONFIG_DEBUG_NRF_ETR_BACKEND_RTT
CONFIG_UART_RTT
CONFIG_LOG_BACKEND_RTT
CONFIG_SHELL_BACKEND_RTT
CONFIG_SEGGER_SYSTEMVIEW
```

**定义位置（Location）**：[`modules/segger/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。

**配置项引用（Symbol References）**：[`CONFIG_USE_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_USE_SEGGER_RTT)、[`CONFIG_DEBUG_NRF_ETR_BACKEND_RTT`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_BACKEND_RTT)、[`CONFIG_UART_RTT`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_RTT)、[`CONFIG_LOG_BACKEND_RTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_BACKEND_RTT)、[`CONFIG_SHELL_BACKEND_RTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_RTT)、[`CONFIG_SEGGER_SYSTEMVIEW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SEGGER_SYSTEMVIEW)。

<a id="CONFIG_SEGGER_RTT_INIT_MODE"></a>

## 249.6 `CONFIG_SEGGER_RTT_INIT_MODE`

**提示（Prompt）**：RTT 初始化模式（Initialization mode）

**说明（Help）**

如果另一个程序（例如引导加载程序，bootloader）已初始化控制块（Control Block），RTT 初始化函数可以避免再次初始化它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SEGGER_RTT
```

**默认值（Defaults）**

```text
CONFIG_SEGGER_RTT_INIT_MODE_STRONG_CHECK if CONFIG_SEGGER_RTT_SECTION_CUSTOM
CONFIG_SEGGER_RTT_INIT_MODE_STRONG_CHECK
```

**可选项（Choices）**

```text
CONFIG_SEGGER_RTT_INIT_MODE_ALWAYS
CONFIG_SEGGER_RTT_INIT_MODE_STRONG_CHECK
CONFIG_SEGGER_RTT_INIT_MODE_WEAK_CHECK
CONFIG_SEGGER_RTT_INIT_MODE_ALWAYS
CONFIG_SEGGER_RTT_INIT_MODE_STRONG_CHECK
CONFIG_SEGGER_RTT_INIT_MODE_WEAK_CHECK
```

**定义位置（Location）**：[`modules/segger/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。

**配置项引用（Symbol References）**：[`CONFIG_USE_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_USE_SEGGER_RTT)、[`CONFIG_SEGGER_RTT_INIT_MODE_STRONG_CHECK`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_INIT_MODE_STRONG_CHECK)、[`CONFIG_SEGGER_RTT_SECTION_CUSTOM`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_SECTION_CUSTOM)、[`CONFIG_SEGGER_RTT_INIT_MODE_ALWAYS`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_INIT_MODE_ALWAYS)、[`CONFIG_SEGGER_RTT_INIT_MODE_WEAK_CHECK`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_INIT_MODE_WEAK_CHECK)。

<a id="CONFIG_SEGGER_RTT_INIT_MODE_ALWAYS"></a>

## 249.7 `CONFIG_SEGGER_RTT_INIT_MODE_ALWAYS`

**提示（Prompt）**：无条件执行 RTT 初始化（Initialization without conditions）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SEGGER_RTT_INIT_MODE>
```

**定义位置（Location）**：[`modules/segger/Kconfig:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。 → RTT 初始化模式（Initialization mode）

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_RTT_INIT_MODE`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_INIT_MODE)。

<a id="CONFIG_SEGGER_RTT_INIT_MODE_STRONG_CHECK"></a>

## 249.8 `CONFIG_SEGGER_RTT_INIT_MODE_STRONG_CHECK`

**提示（Prompt）**：控制块标识完整检查失败时执行 RTT 初始化（full check on Control Block ID）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SEGGER_RTT_INIT_MODE>
```

**定义位置（Location）**：[`modules/segger/Kconfig:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。 → RTT 初始化模式（Initialization mode）

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_RTT_INIT_MODE`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_INIT_MODE)。

<a id="CONFIG_SEGGER_RTT_INIT_MODE_WEAK_CHECK"></a>

## 249.9 `CONFIG_SEGGER_RTT_INIT_MODE_WEAK_CHECK`

**提示（Prompt）**：控制块标识部分检查失败时执行 RTT 初始化（partial check on Control Block ID）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SEGGER_RTT_INIT_MODE>
```

**定义位置（Location）**：[`modules/segger/Kconfig:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。 → RTT 初始化模式（Initialization mode）

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_RTT_INIT_MODE`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_INIT_MODE)。

<a id="CONFIG_SEGGER_RTT_MAX_NUM_DOWN_BUFFERS"></a>

## 249.10 `CONFIG_SEGGER_RTT_MAX_NUM_DOWN_BUFFERS`

**提示（Prompt）**：下行缓冲区的最大数量（Maximum number of down-buffers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SEGGER_RTT
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`modules/segger/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。

**配置项引用（Symbol References）**：[`CONFIG_USE_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_USE_SEGGER_RTT)。

<a id="CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS"></a>

## 249.11 `CONFIG_SEGGER_RTT_MAX_NUM_UP_BUFFERS`

**提示（Prompt）**：上行缓冲区的最大数量（Maximum number of up-buffers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SEGGER_RTT
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`modules/segger/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。

**配置项引用（Symbol References）**：[`CONFIG_USE_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_USE_SEGGER_RTT)。

<a id="CONFIG_SEGGER_RTT_MEMCPY_USE_BYTELOOP"></a>

## 249.12 `CONFIG_SEGGER_RTT_MEMCPY_USE_BYTELOOP`

**提示（Prompt）**：使用简单的逐字节循环（byte-loop）替代标准 memcpy

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SEGGER_RTT
```

**定义位置（Location）**：[`modules/segger/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。

**配置项引用（Symbol References）**：[`CONFIG_USE_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_USE_SEGGER_RTT)。

<a id="CONFIG_SEGGER_RTT_MODE"></a>

## 249.13 `CONFIG_SEGGER_RTT_MODE`

**提示（Prompt）**：预初始化终端通道的模式，缓冲区 0（pre-initialized terminal channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SEGGER_RTT
```

**默认值（Defaults）**

```text
CONFIG_SEGGER_RTT_MODE_NO_BLOCK_SKIP
```

**可选项（Choices）**

```text
CONFIG_SEGGER_RTT_MODE_NO_BLOCK_SKIP
CONFIG_SEGGER_RTT_MODE_NO_BLOCK_TRIM
CONFIG_SEGGER_RTT_MODE_BLOCK_IF_FIFO_FULL
CONFIG_SEGGER_RTT_MODE_NO_BLOCK_SKIP
CONFIG_SEGGER_RTT_MODE_NO_BLOCK_TRIM
CONFIG_SEGGER_RTT_MODE_BLOCK_IF_FIFO_FULL
```

**定义位置（Location）**：[`modules/segger/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。

**配置项引用（Symbol References）**：[`CONFIG_USE_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_USE_SEGGER_RTT)、[`CONFIG_SEGGER_RTT_MODE_NO_BLOCK_SKIP`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_MODE_NO_BLOCK_SKIP)、[`CONFIG_SEGGER_RTT_MODE_NO_BLOCK_TRIM`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_MODE_NO_BLOCK_TRIM)、[`CONFIG_SEGGER_RTT_MODE_BLOCK_IF_FIFO_FULL`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_MODE_BLOCK_IF_FIFO_FULL)。

<a id="CONFIG_SEGGER_RTT_MODE_BLOCK_IF_FIFO_FULL"></a>

## 249.14 `CONFIG_SEGGER_RTT_MODE_BLOCK_IF_FIFO_FULL`

**提示（Prompt）**：阻塞（Block）：等待缓冲区出现可用空间。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SEGGER_RTT_MODE>
```

**定义位置（Location）**：[`modules/segger/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。 → 预初始化终端通道的模式，缓冲区 0（pre-initialized terminal channel）

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_RTT_MODE`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_MODE)。

<a id="CONFIG_SEGGER_RTT_MODE_NO_BLOCK_SKIP"></a>

## 249.15 `CONFIG_SEGGER_RTT_MODE_NO_BLOCK_SKIP`

**提示（Prompt）**：跳过（Skip）：不阻塞，不输出任何内容。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SEGGER_RTT_MODE>
```

**定义位置（Location）**：[`modules/segger/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。 → 预初始化终端通道的模式，缓冲区 0（pre-initialized terminal channel）

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_RTT_MODE`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_MODE)。

<a id="CONFIG_SEGGER_RTT_MODE_NO_BLOCK_TRIM"></a>

## 249.16 `CONFIG_SEGGER_RTT_MODE_NO_BLOCK_TRIM`

**提示（Prompt）**：截断（Trim）：不阻塞，尽量输出缓冲区能够容纳的内容。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SEGGER_RTT_MODE>
```

**定义位置（Location）**：[`modules/segger/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。 → 预初始化终端通道的模式，缓冲区 0（pre-initialized terminal channel）

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_RTT_MODE`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_MODE)。

<a id="CONFIG_SEGGER_RTT_PRINTF_BUFFER_SIZE"></a>

## 249.17 `CONFIG_SEGGER_RTT_PRINTF_BUFFER_SIZE`

**提示（Prompt）**：RTT printf 通过 RTT 批量发送字符所用的缓冲区大小（bulk-send buffer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SEGGER_RTT
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`modules/segger/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。

**配置项引用（Symbol References）**：[`CONFIG_USE_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_USE_SEGGER_RTT)。

<a id="CONFIG_SEGGER_RTT_SECTION"></a>

## 249.18 `CONFIG_SEGGER_RTT_SECTION`

**提示（Prompt）**：选择 RTT 数据的链接器节（data linker section）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_SEGGER_RTT
```

**默认值（Defaults）**

```text
CONFIG_SEGGER_RTT_SECTION_CUSTOM
```

**可选项（Choices）**

```text
CONFIG_SEGGER_RTT_SECTION_NONE
CONFIG_SEGGER_RTT_SECTION_DTCM
CONFIG_SEGGER_RTT_SECTION_CCM
CONFIG_SEGGER_RTT_SECTION_CUSTOM
CONFIG_SEGGER_RTT_SECTION_CUSTOM_DTS_REGION
CONFIG_SEGGER_RTT_SECTION_NONE
CONFIG_SEGGER_RTT_SECTION_DTCM
CONFIG_SEGGER_RTT_SECTION_CCM
CONFIG_SEGGER_RTT_SECTION_CUSTOM
CONFIG_SEGGER_RTT_SECTION_CUSTOM_DTS_REGION
```

**定义位置（Location）**：[`modules/segger/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。

**配置项引用（Symbol References）**：[`CONFIG_USE_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_USE_SEGGER_RTT)、[`CONFIG_SEGGER_RTT_SECTION_CUSTOM`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_SECTION_CUSTOM)、[`CONFIG_SEGGER_RTT_SECTION_NONE`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_SECTION_NONE)、[`CONFIG_SEGGER_RTT_SECTION_DTCM`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_SECTION_DTCM)、[`CONFIG_SEGGER_RTT_SECTION_CCM`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_SECTION_CCM)、[`CONFIG_SEGGER_RTT_SECTION_CUSTOM_DTS_REGION`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_SECTION_CUSTOM_DTS_REGION)。

<a id="CONFIG_SEGGER_RTT_SECTION_CCM"></a>

## 249.19 `CONFIG_SEGGER_RTT_SECTION_CCM`

**提示（Prompt）**：将 RTT 数据放入 CCM 链接器节（linker section）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SEGGER_RTT_SECTION>
```

**定义位置（Location）**：[`modules/segger/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。 → 选择 RTT 数据的链接器节（data linker section）

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_RTT_SECTION`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_SECTION)。

<a id="CONFIG_SEGGER_RTT_SECTION_CUSTOM"></a>

## 249.20 `CONFIG_SEGGER_RTT_SECTION_CUSTOM`

**提示（Prompt）**：将 RTT 数据放入 RAM 起始处的自定义链接器节（custom linker section）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M && <choice CONFIG_SEGGER_RTT_SECTION>
```

**定义位置（Location）**：[`modules/segger/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。 → 选择 RTT 数据的链接器节（data linker section）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_SEGGER_RTT_SECTION`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_SECTION)。

<a id="CONFIG_SEGGER_RTT_SECTION_CUSTOM_DTS_REGION"></a>

## 249.21 `CONFIG_SEGGER_RTT_SECTION_CUSTOM_DTS_REGION`

**提示（Prompt）**：将 RTT 数据放入由 DTS 内存区域定义的自定义链接器节（custom linker section）

**说明（Help）**

DTS 内存节（memory section）需要具有 `rtt_custom_section` 别名（alias）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CPU_CORTEX_M && <choice CONFIG_SEGGER_RTT_SECTION>
```

**定义位置（Location）**：[`modules/segger/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。 → 选择 RTT 数据的链接器节（data linker section）

**配置项引用（Symbol References）**：[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)、[`CONFIG_SEGGER_RTT_SECTION`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_SECTION)。

<a id="CONFIG_SEGGER_RTT_SECTION_CUSTOM_NAME"></a>

## 249.22 `CONFIG_SEGGER_RTT_SECTION_CUSTOM_NAME`

**提示（Prompt）**：RTT 数据自定义链接器节名称（custom linker section name）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
(CONFIG_SEGGER_RTT_SECTION_CUSTOM || CONFIG_SEGGER_RTT_SECTION_CUSTOM_DTS_REGION) && CONFIG_USE_SEGGER_RTT
```

**默认值（Defaults）**

```text
".rtt_buff_data"
```

**定义位置（Location）**：[`modules/segger/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_RTT_SECTION_CUSTOM`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_SECTION_CUSTOM)、[`CONFIG_SEGGER_RTT_SECTION_CUSTOM_DTS_REGION`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_SECTION_CUSTOM_DTS_REGION)、[`CONFIG_USE_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_USE_SEGGER_RTT)。

<a id="CONFIG_SEGGER_RTT_SECTION_DTCM"></a>

## 249.23 `CONFIG_SEGGER_RTT_SECTION_DTCM`

**提示（Prompt）**：将 RTT 数据放入 DTCM 链接器节（linker section）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SEGGER_RTT_SECTION>
```

**定义位置（Location）**：[`modules/segger/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。 → 选择 RTT 数据的链接器节（data linker section）

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_RTT_SECTION`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_SECTION)。

<a id="CONFIG_SEGGER_RTT_SECTION_NONE"></a>

## 249.24 `CONFIG_SEGGER_RTT_SECTION_NONE`

**提示（Prompt）**：将 RTT 数据放入默认链接器节（default linker section）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SEGGER_RTT_SECTION>
```

**定义位置（Location）**：[`modules/segger/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录） → SEGGER RTT 库（RTT libraries）。 → 选择 RTT 数据的链接器节（data linker section）

**配置项引用（Symbol References）**：[`CONFIG_SEGGER_RTT_SECTION`](P249_modules_segger_配置项参考.md#CONFIG_SEGGER_RTT_SECTION)。

<a id="CONFIG_USE_SEGGER_RTT"></a>

## 249.25 `CONFIG_USE_SEGGER_RTT`

**提示（Prompt）**：SEGGER RTT 库（RTT libraries）。

**说明（Help）**

为支持 SEGGER J-Link RTT 的平台启用相应库。选择此选项后，各种子系统可以使用实时传输（RTT）。注意，启用此选项后，RTT 缓冲区会消耗更多 RAM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_SEGGER_RTT
```

**主动选择（Selects）**

```text
CONFIG_STM32_ENABLE_DEBUG_SLEEP_STOP if CONFIG_SOC_FAMILY_STM32
```

**被选择（Selected by）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT
CONFIG_DEBUG_NRF_ETR_BACKEND_RTT
CONFIG_SEGGER_SYSTEMVIEW
```

**定义位置（Location）**：[`modules/segger/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/segger/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → segger（模块路径 `modules/debug/segger`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_HAS_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_HAS_SEGGER_RTT)、[`CONFIG_STM32_ENABLE_DEBUG_SLEEP_STOP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32_ENABLE_DEBUG_SLEEP_STOP)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT)、[`CONFIG_DEBUG_NRF_ETR_BACKEND_RTT`](P075_drivers_debug_配置项参考.md#CONFIG_DEBUG_NRF_ETR_BACKEND_RTT)、[`CONFIG_SEGGER_SYSTEMVIEW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SEGGER_SYSTEMVIEW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<!-- kconfig-navigation -->

[上一章](P248_modules_openthread_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P250_modules_tflite-micro_配置项参考.md)
