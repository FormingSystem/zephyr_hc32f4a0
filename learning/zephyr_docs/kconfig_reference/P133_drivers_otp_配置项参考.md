---
id: learning.zephyr-docs.kconfig-reference.page-133
title: "`drivers/otp`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第133章\_`drivers/otp`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/otp` 的 19 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_OTP"></a>

## 133.1 `CONFIG_OTP`

**提示（Prompt）**：一次性可编程（One Time Programmable，OTP）驱动【实验性】

**说明（Help）**

启用硬件 OTP 支持。OTP 技术可从熔丝（Fuse）到 Flash 选项字节（Option Bytes），只要保持一次性可编程特性即可。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_BL60X
CONFIG_SOC_SERIES_BL616CL
CONFIG_SOC_SERIES_BL61X
CONFIG_SOC_SERIES_BL70X
CONFIG_SOC_SERIES_BL70XL
CONFIG_SOC_SERIES_BL808
```

**被弱选择（Implied by）**

```text
CONFIG_NXP_PMC_TMPSNS
```

**定义位置（Location）**：[`drivers/otp/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_SOC_SERIES_BL60X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL60X)、[`CONFIG_SOC_SERIES_BL616CL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL616CL)、[`CONFIG_SOC_SERIES_BL61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL61X)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_SOC_SERIES_BL808`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL808)、[`CONFIG_NXP_PMC_TMPSNS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_PMC_TMPSNS)。

<a id="CONFIG_OTP_ADI_AXI_SYSID"></a>

## 133.2 `CONFIG_OTP_ADI_AXI_SYSID`

**提示（Prompt）**：Analog Devices AXI System ID ROM（只读 OTP）

**说明（Help）**

启用 Analog Devices AXI System ID 核的只读 OTP 驱动。该核公开 FPGA 构建信息 ROM，包含开发板、产品和 Git 数据，通过标准 OTP API 呈现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_AXI_SYSID_ENABLED && CONFIG_OTP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/otp/Kconfig.adi_axi_sysid:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig.adi_axi_sysid#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)。

<a id="CONFIG_OTP_BFLB"></a>

## 133.3 `CONFIG_OTP_BFLB`

**提示（Prompt）**：Bouffalolab 电子熔丝（EFUSE）驱动

**说明（Help）**

通过 OTP API 访问 Bouffalolab 平台的电子熔丝（E-Fuse）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_EFUSE_ENABLED && CONFIG_OTP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/otp/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)。

<a id="CONFIG_OTP_EMULATOR"></a>

## 133.4 `CONFIG_OTP_EMULATOR`

**提示（Prompt）**：OTP 存储器仿真驱动（Emulation Driver）

**说明（Help）**

启用可用于测试的 OTP 仿真器驱动。每个实例使用一个静态 RAM 缓冲区，其大小在 OTP 设备的设备树节点中定义。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_OTP_EMUL_ENABLED && CONFIG_OTP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/otp/Kconfig.emu:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig.emu#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)。

<a id="CONFIG_OTP_INIT_PRIORITY"></a>

## 133.5 `CONFIG_OTP_INIT_PRIORITY`

**提示（Prompt）**：OTP 初始化优先级

**说明（Help）**

OTP 设备驱动的初始化优先级。除非驱动实现有自己的初始化优先级，否则使用此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OTP
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/otp/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_OTP_MCUX_OCOTP"></a>

## 133.6 `CONFIG_OTP_MCUX_OCOTP`

**提示（Prompt）**：MCUX OCOTP 驱动

**说明（Help）**

启用 MCUX OCOTP 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_OCOTP_ENABLED && CONFIG_OTP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL if n
```

**定义位置（Location）**：[`drivers/otp/Kconfig.mcux_ocotp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig.mcux_ocotp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)。

<a id="CONFIG_OTP_NPM10XX"></a>

## 133.7 `CONFIG_OTP_NPM10XX`

**提示（Prompt）**：Nordic nPM10xx UICR（用户 OTP，User OTP）驱动

**说明（Help）**

启用 Nordic nPM10xx UICR OTP 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NPM10XX_UICR_ENABLED && CONFIG_OTP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/otp/Kconfig.npm10xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig.npm10xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_OTP_NPM10XX_DRY_RUN"></a>

## 133.8 `CONFIG_OTP_NPM10XX_DRY_RUN`

**提示（Prompt）**：nPM10xx UICR 模拟执行编程（Dry-run Programming）

**说明（Help）**

不实际烧写 UICR 位。编程序列执行到 `TASKS.PROG` 触发动作之前，不包含该触发，改为记录原计划写入的位地址。由于 UICR 编程不可逆，此功能有助于安全测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OTP_PROGRAM && CONFIG_OTP_NPM10XX && CONFIG_OTP
```

**定义位置（Location）**：[`drivers/otp/Kconfig.npm10xx:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig.npm10xx#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】 → Nordic nPM10xx UICR（用户 OTP，User OTP）驱动

**配置项引用（Symbol References）**：[`CONFIG_OTP_PROGRAM`](P133_drivers_otp_配置项参考.md#CONFIG_OTP_PROGRAM)、[`CONFIG_OTP_NPM10XX`](P133_drivers_otp_配置项参考.md#CONFIG_OTP_NPM10XX)、[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)。

<a id="CONFIG_OTP_NPM10XX_INIT_PRIORITY"></a>

## 133.9 `CONFIG_OTP_NPM10XX_INIT_PRIORITY`

**提示（Prompt）**：nPM10xx UICR 驱动初始化优先级

**说明（Help）**

nPM10xx UICR 驱动的初始化优先级，必须大于 I²C 初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OTP_NPM10XX && CONFIG_OTP
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`drivers/otp/Kconfig.npm10xx:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig.npm10xx#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】 → Nordic nPM10xx UICR（用户 OTP，User OTP）驱动

**配置项引用（Symbol References）**：[`CONFIG_OTP_NPM10XX`](P133_drivers_otp_配置项参考.md#CONFIG_OTP_NPM10XX)、[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)。

<a id="CONFIG_OTP_NXP_OTPC"></a>

## 133.10 `CONFIG_OTP_NXP_OTPC`

**提示（Prompt）**：NXP OTPC 电子熔丝（eFuse）驱动

**说明（Help）**

启用 NXP OTPC eFuse 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_OTPC_ENABLED && CONFIG_OTP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/otp/Kconfig.nxp_otpc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig.nxp_otpc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)。

<a id="CONFIG_OTP_NXP_RT7XX_OCOTP"></a>

## 133.11 `CONFIG_OTP_NXP_RT7XX_OCOTP`

**提示（Prompt）**：NXP RT7xx OCOTP 驱动

**说明（Help）**

启用 NXP RT7xx OCOTP 控制器的 OTP 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_RT7XX_OCOTP_ENABLED && CONFIG_OTP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/otp/Kconfig.nxp_rt7xx_ocotp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig.nxp_rt7xx_ocotp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)。

<a id="CONFIG_OTP_PROGRAM"></a>

## 133.12 `CONFIG_OTP_PROGRAM`

**提示（Prompt）**：支持通过 Zephyr API 编程 OTP

**说明（Help）**

允许编程 OTP 可能对平台造成不可逆的损坏。请极其谨慎使用，并自行承担风险。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OTP
```

**定义位置（Location）**：[`drivers/otp/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)。

<a id="CONFIG_OTP_RTS5817"></a>

## 133.13 `CONFIG_OTP_RTS5817`

**提示（Prompt）**：RTS5817 OCOTP 驱动

**说明（Help）**

启用 RTS5817 OCOTP 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5817_OCOTP_ENABLED && CONFIG_RESET_RTS5817 && CONFIG_CLOCK_CONTROL_RTS5817 && CONFIG_SYSCON && CONFIG_OTP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/otp/Kconfig.rts5817:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig.rts5817#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_RESET_RTS5817`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET_RTS5817)、[`CONFIG_CLOCK_CONTROL_RTS5817`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_RTS5817)、[`CONFIG_SYSCON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSCON)、[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)。

<a id="CONFIG_OTP_SHELL"></a>

## 133.14 `CONFIG_OTP_SHELL`

**提示（Prompt）**：OTP 命令行（Shell）

**说明（Help）**

启用包含一次性可编程（OTP）相关命令的 Shell。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_OTP
```

**定义位置（Location）**：[`drivers/otp/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)。

<a id="CONFIG_OTP_SHELL_BUFFER_SIZE"></a>

## 133.15 `CONFIG_OTP_SHELL_BUFFER_SIZE`

**提示（Prompt）**：OTP Shell 编程缓冲区大小（Program Buffer Size）

**说明（Help）**

OTP Shell 中 OTP 编程命令使用的缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OTP_SHELL && CONFIG_OTP
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/otp/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】 → OTP 命令行（Shell）

**配置项引用（Symbol References）**：[`CONFIG_OTP_SHELL`](P133_drivers_otp_配置项参考.md#CONFIG_OTP_SHELL)、[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)。

<a id="CONFIG_OTP_SIFLI_EFUSE"></a>

## 133.16 `CONFIG_OTP_SIFLI_EFUSE`

**提示（Prompt）**：SiFli SF32LB 系列 eFuse OTP 驱动

**说明（Help）**

启用 SiFli SF32LB 系列 eFuse OTP 驱动。此驱动提供 eFuse OTP 存储器只读访问，并使用缓存机制：初始化时将全部 eFuse 内容加载到内存，提高读取性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_EFUSE_ENABLED && CONFIG_OTP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/otp/Kconfig.sifli:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig.sifli#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)。

<a id="CONFIG_OTP_STM32_BSEC"></a>

## 133.17 `CONFIG_OTP_STM32_BSEC`

**提示（Prompt）**：STM32 BSEC 驱动

**说明（Help）**

为内置 BSEC 外设的 STM32 SoC 启用 OTP 熔丝访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_BSEC_ENABLED && CONFIG_OTP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_BSEC
```

**定义位置（Location）**：[`drivers/otp/Kconfig.stm32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig.stm32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)、[`CONFIG_USE_STM32_HAL_BSEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_BSEC)。

<a id="CONFIG_OTP_STM32_NVM"></a>

## 133.18 `CONFIG_OTP_STM32_NVM`

**提示（Prompt）**：STM32 嵌入式非易失性存储器（NVM）OTP 驱动

**说明（Help）**

启用 STM32 SoC 内嵌非易失性存储器中 OTP 区域的驱动。注意，编程操作（`CONFIG_OTP_PROGRAM`）由各 STM32 系列的 Flash 驱动实现，而非此驱动。此驱动仅充当适配层（Shim），将 `otp_program()` 转发到适当的后端驱动。部分系列可能未实现编程操作，此时 `otp_program()` 返回 `-ENOTSUP`。应检查对应 Flash 驱动，确认是否实现该操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_NVM_OTP_ENABLED && CONFIG_OTP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/otp/Kconfig.stm32:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig.stm32#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)。

<a id="CONFIG_OTP_STM32_NVM_PROGRAMMING_SUPPORT"></a>

## 133.19 `CONFIG_OTP_STM32_NVM_PROGRAMMING_SUPPORT`

**提示（Prompt）**：NVM OTP 编程（Programming）

**说明（Help）**

启用对 STM32 NVM OTP 区域的编程。此选项尚不适用于 STM32WBA 系列。注意，OTP 编程逻辑在各系列专用的 Flash 驱动中实现；此驱动仅将 `otp_program()` 实现为适配层，调用 Flash 驱动的实现。目前并非所有 Flash 驱动都支持 OTP 编程。底层 Flash 驱动不支持此操作时，调用 `otp_program()` 将返回 `-ENOTSUP`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OTP_PROGRAM && CONFIG_SOC_FLASH_STM32 && !CONFIG_SOC_SERIES_STM32WBAX && CONFIG_OTP_STM32_NVM && CONFIG_OTP
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/otp/Kconfig.stm32:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/otp/Kconfig.stm32#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 一次性可编程（One Time Programmable，OTP）驱动【实验性】 → STM32 嵌入式非易失性存储器（NVM）OTP 驱动

**配置项引用（Symbol References）**：[`CONFIG_OTP_PROGRAM`](P133_drivers_otp_配置项参考.md#CONFIG_OTP_PROGRAM)、[`CONFIG_SOC_FLASH_STM32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_STM32)、[`CONFIG_SOC_SERIES_STM32WBAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WBAX)、[`CONFIG_OTP_STM32_NVM`](P133_drivers_otp_配置项参考.md#CONFIG_OTP_STM32_NVM)、[`CONFIG_OTP`](P133_drivers_otp_配置项参考.md#CONFIG_OTP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32WBAX`。

<!-- kconfig-navigation -->

[上一章](P132_drivers_opamp_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P134_drivers_pcie_配置项参考.md)
