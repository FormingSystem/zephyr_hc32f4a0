---
id: learning.zephyr-docs.kconfig-reference.page-119
title: "`drivers/memc`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第119章\_`drivers/memc`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/memc` 的 35 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_FORCE_USING_OVRDVAL"></a>

## 119.1 `CONFIG_FLASH_MCUX_FLEXSPI_FORCE_USING_OVRDVAL`

**提示（Prompt）**：强制使用 FLEXSPI 目标时钟延迟线覆盖值（Target Clock Delay Line Override Value）

**说明（Help）**

启用此设置，强制为 `DLLCR` 寄存器的 `OVRDVAL` 字段使用指定原始值。与 DTS 中的 `data-valid-time` 字段相比，此选项提供更细的粒度；`data-valid-time` 的单位是纳秒，`OVRDVAL` 的单位则是原始延迟单元（Delay Cell）。通常，任意 `nxp,imx-flexspi-device` 设备的 `data-valid-time` 都会设置 `DLLCR` 寄存器中的 `OVRDVAL` 和 `OVRDEN` 字段，但仅当 `rx-clock-source` 配置为“#0 来自 DQS 焊盘的外部输入”（External Input from DQS Pad），且频率不超过 100 MHz 时才生效。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_MEMC
```

**定义位置（Location）**：[`drivers/memc/Kconfig.mcux:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.mcux#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)。

<a id="CONFIG_FLASH_MCUX_FLEXSPI_OVRDVAL"></a>

## 119.2 `CONFIG_FLASH_MCUX_FLEXSPI_OVRDVAL`

**提示（Prompt）**：FLEXSPI 目标时钟延迟线覆盖值（Target Clock Delay Line Override Value）

**说明（Help）**

要存入 `DDLCR->OVRDVAL` 字段的原始值（Raw Value）。译注：此处原文拼作 DDLCR，而相关强制覆盖选项的帮助使用 DLLCR；保留原始标识差异。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MCUX_FLEXSPI_FORCE_USING_OVRDVAL && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
27
```

**取值范围（Ranges）**

```text
[0, 63]
```

**定义位置（Location）**：[`drivers/memc/Kconfig.mcux:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.mcux#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】 → 强制使用 FLEXSPI 目标时钟延迟线覆盖值（Target Clock Delay Line Override Value）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MCUX_FLEXSPI_FORCE_USING_OVRDVAL`](P119_drivers_memc_配置项参考.md#CONFIG_FLASH_MCUX_FLEXSPI_FORCE_USING_OVRDVAL)、[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)。

<a id="CONFIG_MEMC"></a>

## 119.3 `CONFIG_MEMC`

**提示（Prompt）**：存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**说明（Help）**

添加存储器控制器（Memory Controller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_DISK_DRIVER_MEMC_RAM
CONFIG_DISPLAY_RENESAS_LCDC_BUFFER_PSRAM
CONFIG_FLASH_MCUX_FLEXSPI_NOR
CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G
CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH
CONFIG_FLASH_MCUX_FLEXSPI_NAND
CONFIG_FLASH_MCUX_XSPI
CONFIG_FLASH_NXP_S32_QSPI_NOR
CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH
CONFIG_FLASH_NXP_S32_XSPI_HYPERRAM
CONFIG_MIPI_DBI_STM32_FMC
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/rtk7eka6m3b00001bu/boards/ek_ra8d1.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtk7eka6m3b00001bu/boards/ek_ra8d1.defconfig)。

```text
y
```

来源：[`boards/shields/rtklcdpar1s00001be/boards/ek_ra8d2_r7ka8d2kflcac_cm85.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtklcdpar1s00001be/boards/ek_ra8d2_r7ka8d2kflcac_cm85.defconfig)。

```text
y
```

来源：[`boards/shields/rtklcdpar1s00001be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtklcdpar1s00001be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig)。

```text
y
```

来源：[`boards/shields/rtkmipilcdb00000be/boards/aik_ra8d1.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/boards/aik_ra8d1.defconfig)。

```text
y
```

来源：[`boards/shields/rtkmipilcdb00000be/boards/ek_ra8d1.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/boards/ek_ra8d1.defconfig)。

```text
y
```

来源：[`boards/shields/rtkmipilcdb00000be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/memc/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_DISK_DRIVER_MEMC_RAM`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_MEMC_RAM)、[`CONFIG_DISPLAY_RENESAS_LCDC_BUFFER_PSRAM`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_RENESAS_LCDC_BUFFER_PSRAM)、[`CONFIG_FLASH_MCUX_FLEXSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_NOR)、[`CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_MX25UM51345G)、[`CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_HYPERFLASH)、[`CONFIG_FLASH_MCUX_FLEXSPI_NAND`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_NAND)、[`CONFIG_FLASH_MCUX_XSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_XSPI)、[`CONFIG_FLASH_NXP_S32_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_NXP_S32_QSPI_NOR)、[`CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH)、[`CONFIG_FLASH_NXP_S32_XSPI_HYPERRAM`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_NXP_S32_XSPI_HYPERRAM)、[`CONFIG_MIPI_DBI_STM32_FMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI_STM32_FMC)。

<a id="CONFIG_MEMC_BFLB_BL61X"></a>

## 119.4 `CONFIG_MEMC_BFLB_BL61X`

**提示（Prompt）**：Bouffalolab BL61x 伪静态 RAM（PSRAM）控制器

**说明（Help）**

启用 Bouffalolab BL61x PSRAM 控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_BL61X_PSRAM_ENABLED && CONFIG_OTP_BFLB && CONFIG_CLOCK_CONTROL && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/memc/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_OTP_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OTP_BFLB)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)。

<a id="CONFIG_MEMC_BFLB_BL808_PSRAM_UHS"></a>

## 119.5 `CONFIG_MEMC_BFLB_BL808_PSRAM_UHS`

**提示（Prompt）**：Bouffalolab BL808 UHS PSRAM 控制器

**说明（Help）**

启用 Bouffalolab BL808 UHS PSRAM 控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_BL808_PSRAM_UHS_CONTROLLER_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/memc/Kconfig.bflb:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.bflb#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)。

<a id="CONFIG_MEMC_HIFIVE_UNMATCHED_DRAM"></a>

## 119.6 `CONFIG_MEMC_HIFIVE_UNMATCHED_DRAM`

**提示（Prompt）**：HiFive Unmatched DRAM 存储器控制器

**说明（Help）**

启用 HiFive Unmatched 存储器控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFIVE_FU740_C000_DDR_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/memc/Kconfig.sifive:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.sifive#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)。

<a id="CONFIG_MEMC_INIT_PRIORITY"></a>

## 119.7 `CONFIG_MEMC_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Initialization Priority）

**说明（Help）**

存储器控制器初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MEMC
```

**默认值（Defaults）**

```text
80 if CONFIG_MSPI
0
```

**定义位置（Location）**：[`drivers/memc/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_MSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI)。

<a id="CONFIG_MEMC_MAX32_HPB"></a>

## 119.8 `CONFIG_MEMC_MAX32_HPB`

**提示（Prompt）**：MAX32 HyperBus

**说明（Help）**

启用 ADI MAX32 HyperBus 控制器。如果希望依赖链接器（Linker）将符号放入此存储器，例如使用 `zephyr_code_relocate()` 或 `Z_GENERIC_SECTION()`，必须确保此驱动在 `KERNEL_INIT_PRIORITY_OBJECTS`（=30）之前初始化。此外，此驱动依赖时钟，因此还必须确保时钟先于此驱动启动，参见 `CLOCK_CONTROL_INIT_PRIORITY`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_HPB_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/memc/Kconfig.max32_hpb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.max32_hpb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_MEMC_MCUX_FLEXSPI_APS6404L"></a>

## 119.9 `CONFIG_MEMC_MCUX_FLEXSPI_APS6404L`

**提示（Prompt）**：MCUX FlexSPI AP Memory APS6404L pSRAM 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_FLEXSPI_APS6404L_ENABLED && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MEMC_MCUX_FLEXSPI
```

**定义位置（Location）**：[`drivers/memc/Kconfig.mcux:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.mcux#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_MEMC_MCUX_FLEXSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC_MCUX_FLEXSPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MEMC_MCUX_FLEXSPI`。

<a id="CONFIG_MEMC_MCUX_FLEXSPI_APS6408L"></a>

## 119.10 `CONFIG_MEMC_MCUX_FLEXSPI_APS6408L`

**提示（Prompt）**：MCUX FlexSPI AP Memory APS6408L pSRAM 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_FLEXSPI_APS6408L_ENABLED && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MEMC_MCUX_FLEXSPI
```

**定义位置（Location）**：[`drivers/memc/Kconfig.mcux:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.mcux#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_MEMC_MCUX_FLEXSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC_MCUX_FLEXSPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MEMC_MCUX_FLEXSPI`。

<a id="CONFIG_MEMC_MCUX_FLEXSPI_INIT_PRIORITY"></a>

## 119.11 `CONFIG_MEMC_MCUX_FLEXSPI_INIT_PRIORITY`

**提示（Prompt）**：MCUX FLEXSPI MEMC 驱动初始化优先级

**说明（Help）**

FlexSPI 存储器控制器（MEMC）驱动的初始化优先级。Flash 驱动必须先于 MEMC RAM 驱动初始化时，可将初始化优先级设置为：

```text
MEMC_MCUX_FLEXSPI_INIT_PRIORITY < FLASH_INIT_PRIORITY <
MEMC_INIT_PRIORITY
```

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
CONFIG_MEMC_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/memc/Kconfig.mcux:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.mcux#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_MEMC_INIT_PRIORITY`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_INIT_PRIORITY)。

<a id="CONFIG_MEMC_MCUX_FLEXSPI_INIT_XIP"></a>

## 119.12 `CONFIG_MEMC_MCUX_FLEXSPI_INIT_XIP`

**提示（Prompt）**：使用设备进行就地执行（XIP）时初始化 FLEXSPI

**说明（Help）**

即使 FLEXSPI 设备正用于就地执行（XIP），也对其初始化。启用此 Kconfig 后，用户必须确保所用引脚控制状态（Pinctrl State）不会重新配置与 XIP Flash 相连的引脚，而且 FLEXSPI 配置与从该 Flash 执行 XIP 所需的配置兼容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_MEMC
```

**定义位置（Location）**：[`drivers/memc/Kconfig.mcux:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.mcux#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)。

<a id="CONFIG_MEMC_MCUX_FLEXSPI_IS66WVQ8M4"></a>

## 119.13 `CONFIG_MEMC_MCUX_FLEXSPI_IS66WVQ8M4`

**提示（Prompt）**：MCUX FlexSPI ISSI IS66WVQ8M4 pSRAM 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_FLEXSPI_IS66WVQ8M4_ENABLED && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MEMC_MCUX_FLEXSPI
```

**定义位置（Location）**：[`drivers/memc/Kconfig.mcux:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.mcux#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_MEMC_MCUX_FLEXSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC_MCUX_FLEXSPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MEMC_MCUX_FLEXSPI`。

<a id="CONFIG_MEMC_MCUX_FLEXSPI_IS66WVS8M8"></a>

## 119.14 `CONFIG_MEMC_MCUX_FLEXSPI_IS66WVS8M8`

**提示（Prompt）**：MCUX FlexSPI ISSI IS66WVS8M8 pSRAM 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_FLEXSPI_IS66WVS8M8_ENABLED && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MEMC_MCUX_FLEXSPI
```

**定义位置（Location）**：[`drivers/memc/Kconfig.mcux:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.mcux#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_MEMC_MCUX_FLEXSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC_MCUX_FLEXSPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MEMC_MCUX_FLEXSPI`。

<a id="CONFIG_MEMC_MCUX_FLEXSPI_S27KS0641"></a>

## 119.15 `CONFIG_MEMC_MCUX_FLEXSPI_S27KS0641`

**提示（Prompt）**：MCUX FlexSPI Cypress S27KS0641 HyperRAM 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_FLEXSPI_S27KS0641_ENABLED && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MEMC_MCUX_FLEXSPI
```

**定义位置（Location）**：[`drivers/memc/Kconfig.mcux:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.mcux#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_MEMC_MCUX_FLEXSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC_MCUX_FLEXSPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MEMC_MCUX_FLEXSPI`。

<a id="CONFIG_MEMC_MCUX_FLEXSPI_W956A8MBYA"></a>

## 119.16 `CONFIG_MEMC_MCUX_FLEXSPI_W956A8MBYA`

**提示（Prompt）**：MCUX FlexSPI Winbond W956A8MBYA HyperRAM 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_FLEXSPI_W956A8MBYA_ENABLED && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MEMC_MCUX_FLEXSPI
```

**定义位置（Location）**：[`drivers/memc/Kconfig.mcux:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.mcux#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_MEMC_MCUX_FLEXSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC_MCUX_FLEXSPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MEMC_MCUX_FLEXSPI`。

<a id="CONFIG_MEMC_MCUX_FLEXSPI_WAIT_BUS_IDLE_TIMEOUT"></a>

## 119.17 `CONFIG_MEMC_MCUX_FLEXSPI_WAIT_BUS_IDLE_TIMEOUT`

**提示（Prompt）**：等待 FlexSPI 总线空闲的轮询次数（Poll Count）

**说明（Help）**

在电源域（Power Domain）唤醒后、清除各端口查找表（LUT）记账信息之前，等待 FlexSPI 总线空闲的最大轮询次数。它为唤醒路径设置边界，防止卡住的控制器使恢复过程挂起。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE && DT_HAS_NXP_IMX_FLEXSPI_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
100000
```

**定义位置（Location）**：[`drivers/memc/Kconfig.mcux:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.mcux#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)、[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)。

<a id="CONFIG_MEMC_MCUX_XSPI_INIT_XIP"></a>

## 119.18 `CONFIG_MEMC_MCUX_XSPI_INIT_XIP`

**提示（Prompt）**：使用设备进行就地执行（XIP）时初始化 XSPI

**说明（Help）**

即使 XSPI 设备正用于就地执行（XIP），也对其初始化。启用此 Kconfig 后，用户必须确保所用引脚控制状态不会重新配置与 XIP Flash 相连的引脚，而且 XSPI 配置与从该 Flash 执行 XIP 所需的配置兼容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_XSPI_ENABLED && CONFIG_MEMC
```

**定义位置（Location）**：[`drivers/memc/Kconfig.mcux:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.mcux#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)。

<a id="CONFIG_MEMC_MCUX_XSPI_PSRAM"></a>

## 119.19 `CONFIG_MEMC_MCUX_XSPI_PSRAM`

**提示（Prompt）**：MCUX XSPI PSRAM 驱动

**说明（Help）**

启用 MCUX XSPI PSRAM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_XSPI_PSRAM_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MEMC_MCUX_XSPI
```

**定义位置（Location）**：[`drivers/memc/Kconfig.mcux:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.mcux#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_MEMC_MCUX_XSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC_MCUX_XSPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MEMC_MCUX_XSPI`。

<a id="CONFIG_MEMC_MSPI"></a>

## 119.20 `CONFIG_MEMC_MSPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

已启用 MSPI MEMC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MEMC
```

**主动选择（Selects）**

```text
CONFIG_MSPI
```

**定义位置（Location）**：[`drivers/memc/Kconfig.mspi:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.mspi#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】 → MSPI MEMC 设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_MSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI)。

<a id="CONFIG_MEMC_MSPI_APS6404L"></a>

## 119.21 `CONFIG_MEMC_MSPI_APS6404L`

**提示（Prompt）**：MSPI AP Memory APS6404L pSRAM 驱动

**说明（Help）**：原库未提供帮助正文。

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
CONFIG_MEMC_MSPI
CONFIG_MSPI_AMBIQ_CONTROLLER
```

**定义位置（Location）**：[`drivers/memc/Kconfig.mspi:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.mspi#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】 → MSPI MEMC 设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MEMC_MSPI`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_MSPI)、[`CONFIG_MSPI_AMBIQ_CONTROLLER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_AMBIQ_CONTROLLER)。

<a id="CONFIG_MEMC_MSPI_APS_Z8"></a>

## 119.22 `CONFIG_MEMC_MSPI_APS_Z8`

**提示（Prompt）**：MSPI AP Memory gen Z8 pSRAM 驱动

**说明（Help）**：原库未提供帮助正文。

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
CONFIG_MEMC_MSPI
CONFIG_MSPI_AMBIQ_CONTROLLER
```

**定义位置（Location）**：[`drivers/memc/Kconfig.mspi:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.mspi#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】 → MSPI MEMC 设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MEMC_MSPI`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_MSPI)、[`CONFIG_MSPI_AMBIQ_CONTROLLER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_AMBIQ_CONTROLLER)。

<a id="CONFIG_MEMC_MSPI_IS66WV"></a>

## 119.23 `CONFIG_MEMC_MSPI_IS66WV`

**提示（Prompt）**：MSPI ISSI IS66WV pSRAM 驱动

**说明（Help）**：原库未提供帮助正文。

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
CONFIG_MEMC_MSPI
```

**定义位置（Location）**：[`drivers/memc/Kconfig.mspi:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.mspi#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】 → MSPI MEMC 设备驱动

**配置项引用（Symbol References）**：[`CONFIG_MEMC_MSPI`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_MSPI)。

<a id="CONFIG_MEMC_NXP_S32_QSPI"></a>

## 119.24 `CONFIG_MEMC_NXP_S32_QSPI`

**提示（Prompt）**：NXP S32 四线串行外设接口（Quad Serial Peripheral Interface，QSPI）控制器

**说明（Help）**

启用 NXP S32 四线串行外设接口（QSPI）控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_QSPI_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/memc/Kconfig.nxp_s32_qspi:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.nxp_s32_qspi#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_MEMC_NXP_S32_XSPI"></a>

## 119.25 `CONFIG_MEMC_NXP_S32_XSPI`

**提示（Prompt）**：NXP S32 扩展串行外设接口（eXpanded Serial Peripheral Interface，XSPI）控制器

**说明（Help）**

启用 NXP S32 扩展串行外设接口（XSPI）控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_XSPI_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/memc/Kconfig.nxp_s32_xspi:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.nxp_s32_xspi#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_MEMC_NXP_SRAMC"></a>

## 119.26 `CONFIG_MEMC_NXP_SRAMC`

**提示（Prompt）**：NXP AHB SRAM 控制器（SRAMC）

**说明（Help）**

启用 NXP AHB SRAM 控制器（SRAMC）驱动。这个仅执行初始化的驱动调用 MCUXpresso SDK 的 `fsl_sramc` 硬件抽象层（HAL），配置外部异步并行 SRAM 总线时序，使外部 SRAM 可作为内存映射区域（Memory-mapped Region）使用。用于 i.MX RT118x，例如 MIMXRT1189。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SRAMC_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/memc/Kconfig.nxp_sramc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.nxp_sramc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_MEMC_RENESAS_RA_SDRAM"></a>

## 119.27 `CONFIG_MEMC_RENESAS_RA_SDRAM`

**提示（Prompt）**：Renesas RA SDRAM 控制器

**说明（Help）**

启用 Renesas RA SDRAM 控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_SDRAM_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_SDRAM
```

**定义位置（Location）**：[`drivers/memc/Kconfig.renesas_ra:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.renesas_ra#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_USE_RA_FSP_SDRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_SDRAM)。

<a id="CONFIG_MEMC_SAM_SMC"></a>

## 119.28 `CONFIG_MEMC_SAM_SMC`

**提示（Prompt）**：Atmel 静态存储器控制器（Static Memory Controller，SMC）

**说明（Help）**

启用 Atmel 静态存储器控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_SMC_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/memc/Kconfig.sam:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.sam#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_MEMC_SILABS_SIWX91X_QSPI"></a>

## 119.29 `CONFIG_MEMC_SILABS_SIWX91X_QSPI`

**提示（Prompt）**：Silabs SiWx91x QSPI 存储器控制器

**说明（Help）**

启用 Silabs SiWx91x 四线串行外设接口（QSPI）存储器控制器。如果希望依赖链接器将符号放入此存储器，例如使用 `zephyr_code_relocate()` 或 `Z_GENERIC_SECTION()`，必须确保此驱动在 `KERNEL_INIT_PRIORITY_OBJECTS`（=30）之前初始化。此外，此驱动可能依赖时钟，此时还必须确保时钟先于此驱动启动，参见 `CLOCK_CONTROL_INIT_PRIORITY`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SIWX91X_QSPI_MEMORY_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/memc/Kconfig.siwx91x_qspi:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.siwx91x_qspi#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_MEMC_SMARTBOND"></a>

## 119.30 `CONFIG_MEMC_SMARTBOND`

**提示（Prompt）**：SmartBond NOR/PSRAM 存储器控制器

**说明（Help）**

启用 SmartBond NOR/PSRAM 存储器控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_NOR_PSRAM_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/memc/Kconfig.smartbond:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.smartbond#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)。

<a id="CONFIG_MEMC_STM32"></a>

## 119.31 `CONFIG_MEMC_STM32`

**提示（Prompt）**：STM32 灵活存储器控制器（Flexible Memory Controller，FMC）

**说明（Help）**

启用 STM32 灵活存储器控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_STM32_FMC_ENABLED || DT_HAS_ST_STM32H7_FMC_ENABLED) && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/memc/Kconfig.stm32:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.stm32#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_MEMC_STM32_NOR_PSRAM"></a>

## 119.32 `CONFIG_MEMC_STM32_NOR_PSRAM`

**提示（Prompt）**：STM32 FMC NOR/PSRAM 控制器

**说明（Help）**

启用 STM32 FMC NOR/PSRAM 控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_FMC_NOR_PSRAM_ENABLED && CONFIG_MEMC_STM32 && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_LL_FMC
CONFIG_USE_STM32_HAL_NOR
CONFIG_USE_STM32_HAL_SRAM
```

**定义位置（Location）**：[`drivers/memc/Kconfig.stm32:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.stm32#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】 → STM32 灵活存储器控制器（Flexible Memory Controller，FMC）

**配置项引用（Symbol References）**：[`CONFIG_MEMC_STM32`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_STM32)、[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_USE_STM32_LL_FMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_LL_FMC)、[`CONFIG_USE_STM32_HAL_NOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_NOR)、[`CONFIG_USE_STM32_HAL_SRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_SRAM)。

<a id="CONFIG_MEMC_STM32_OSPI_PSRAM"></a>

## 119.33 `CONFIG_MEMC_STM32_OSPI_PSRAM`

**提示（Prompt）**：STM32 OSPI PSRAM

**说明（Help）**

启用 STM32 OSPI PSRAM 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_OSPI_PSRAM_ENABLED && CONFIG_SOC_SERIES_STM32U5X && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_OSPI
CONFIG_USE_STM32_LL_DLYB
CONFIG_USE_STM32_HAL_DMA
CONFIG_USE_STM32_HAL_DMA_EX
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/memc/Kconfig.stm32:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.stm32#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_USE_STM32_HAL_OSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_OSPI)、[`CONFIG_USE_STM32_LL_DLYB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_LL_DLYB)、[`CONFIG_USE_STM32_HAL_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA)、[`CONFIG_USE_STM32_HAL_DMA_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA_EX)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32U5X`。

<a id="CONFIG_MEMC_STM32_SDRAM"></a>

## 119.34 `CONFIG_MEMC_STM32_SDRAM`

**提示（Prompt）**：STM32 FMC SDRAM 控制器

**说明（Help）**

启用 STM32 FMC SDRAM 控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_FMC_SDRAM_ENABLED && CONFIG_MEMC_STM32 && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_LL_FMC
CONFIG_USE_STM32_HAL_SDRAM
```

**定义位置（Location）**：[`drivers/memc/Kconfig.stm32:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.stm32#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】 → STM32 灵活存储器控制器（Flexible Memory Controller，FMC）

**配置项引用（Symbol References）**：[`CONFIG_MEMC_STM32`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_STM32)、[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_USE_STM32_LL_FMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_LL_FMC)、[`CONFIG_USE_STM32_HAL_SDRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_SDRAM)。

<a id="CONFIG_MEMC_STM32_XSPI_PSRAM"></a>

## 119.35 `CONFIG_MEMC_STM32_XSPI_PSRAM`

**提示（Prompt）**：STM32 XSPI PSRAM

**说明（Help）**

启用 STM32 XSPI 存储器控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_XSPI_PSRAM_ENABLED && CONFIG_MEMC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_XSPI
CONFIG_USE_STM32_LL_DLYB if CONFIG_SOC_SERIES_STM32H5X
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/memc/Kconfig.stm32:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/Kconfig.stm32#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 存储器控制器（Memory Controller）驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_USE_STM32_HAL_XSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_XSPI)、[`CONFIG_USE_STM32_LL_DLYB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_LL_DLYB)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32H5X`。

<!-- kconfig-navigation -->

[上一章](P118_drivers_mbox_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P120_drivers_mfd_配置项参考.md)
