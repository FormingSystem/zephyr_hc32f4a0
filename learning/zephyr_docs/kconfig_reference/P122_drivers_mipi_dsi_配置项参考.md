---
id: learning.zephyr-docs.kconfig-reference.page-122
title: "`drivers/mipi_dsi`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第122章\_`drivers/mipi_dsi`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/mipi_dsi` 的 12 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MIPI_DSI"></a>

## 122.1 `CONFIG_MIPI_DSI`

**提示（Prompt）**：MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】

**说明（Help）**

添加 MIPI-DSI 主机控制器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_ADV7535
CONFIG_EK79007
CONFIG_DISPLAY_ESP32_DSI
CONFIG_HX8379C
CONFIG_ILI9806E_DSI
CONFIG_ILI9881C_DSI
CONFIG_NT35510
CONFIG_OTM8009A
CONFIG_RM67162
CONFIG_RM67199
CONFIG_RM692C9
CONFIG_ST7701
CONFIG_WAVESHARE_DSI2DPI
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/rk055hdmipi4m/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk055hdmipi4m/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rk055hdmipi4ma0/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk055hdmipi4ma0/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rtkapplcdms02001be/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkapplcdms02001be/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rtkmipilcdb00000be/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/mipi_dsi/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dsi/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_ADV7535`](P077_drivers_display_配置项参考_1.md#CONFIG_ADV7535)、[`CONFIG_EK79007`](P077_drivers_display_配置项参考_1.md#CONFIG_EK79007)、[`CONFIG_DISPLAY_ESP32_DSI`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_ESP32_DSI)、[`CONFIG_HX8379C`](P077_drivers_display_配置项参考_1.md#CONFIG_HX8379C)、[`CONFIG_ILI9806E_DSI`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9806E_DSI)、[`CONFIG_ILI9881C_DSI`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9881C_DSI)、[`CONFIG_NT35510`](P077_drivers_display_配置项参考_1.md#CONFIG_NT35510)、[`CONFIG_OTM8009A`](P077_drivers_display_配置项参考_1.md#CONFIG_OTM8009A)、[`CONFIG_RM67162`](P078_drivers_display_配置项参考_2.md#CONFIG_RM67162)、[`CONFIG_RM67199`](P078_drivers_display_配置项参考_2.md#CONFIG_RM67199)、[`CONFIG_RM692C9`](P078_drivers_display_配置项参考_2.md#CONFIG_RM692C9)、[`CONFIG_ST7701`](P078_drivers_display_配置项参考_2.md#CONFIG_ST7701)、[`CONFIG_WAVESHARE_DSI2DPI`](P078_drivers_display_配置项参考_2.md#CONFIG_WAVESHARE_DSI2DPI)。

<a id="CONFIG_MIPI_DSI_ESP32"></a>

## 122.2 `CONFIG_MIPI_DSI_ESP32`

**提示（Prompt）**：ESP32 MIPI DSI 主机控制器

**说明（Help）**

启用 ESP32 MIPI DSI 主机控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP_MIPI_DSI_ENABLED && CONFIG_SOC_SERIES_ESP32P4 && CONFIG_DISPLAY_ESP32_DSI && CONFIG_MIPI_DSI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mipi_dsi/Kconfig.esp32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dsi/Kconfig.esp32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_DISPLAY_ESP32_DSI`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_ESP32_DSI)、[`CONFIG_MIPI_DSI`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`。

<a id="CONFIG_MIPI_DSI_INIT_PRIORITY"></a>

## 122.3 `CONFIG_MIPI_DSI_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Initialization Priority）

**说明（Help）**

MIPI-DSI 主机控制器初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MIPI_DSI
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`drivers/mipi_dsi/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dsi/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DSI`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI)。

<a id="CONFIG_MIPI_DSI_MCUX"></a>

## 122.4 `CONFIG_MIPI_DSI_MCUX`

**提示（Prompt）**：NXP MCUX MIPI-DSI 主机控制器

**说明（Help）**

NXP MIPI DSI 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_MIPI_DSI_ENABLED && CONFIG_MIPI_DSI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mipi_dsi/Kconfig.mcux:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dsi/Kconfig.mcux#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DSI`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI)。

<a id="CONFIG_MIPI_DSI_MCUX_2L"></a>

## 122.5 `CONFIG_MIPI_DSI_MCUX_2L`

**提示（Prompt）**：NXP MCUX MIPI-DSI 2L 控制器

**说明（Help）**

NXP MIPI DSI 2L 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MIPI_DSI_2L_ENABLED && CONFIG_MIPI_DSI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mipi_dsi/Kconfig.mcux:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dsi/Kconfig.mcux#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DSI`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI)。

<a id="CONFIG_MIPI_DSI_MCUX_2L_SMARTDMA"></a>

## 122.6 `CONFIG_MIPI_DSI_MCUX_2L_SMARTDMA`

**提示（Prompt）**：MIPI DSI 使用 smartDMA 控制器

**说明（Help）**

使用 SMARTDMA。此加速器会自动将 RGB565 输入数据转换为 RGB565X，并写入 MIPI DSI。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_MCUX_SMARTDMA && CONFIG_MIPI_DSI_MCUX_2L && CONFIG_MIPI_DSI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mipi_dsi/Kconfig.mcux:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dsi/Kconfig.mcux#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】 → NXP MCUX MIPI-DSI 2L 控制器

**配置项引用（Symbol References）**：[`CONFIG_DMA_MCUX_SMARTDMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_MCUX_SMARTDMA)、[`CONFIG_MIPI_DSI_MCUX_2L`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI_MCUX_2L)、[`CONFIG_MIPI_DSI`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI)。

<a id="CONFIG_MIPI_DSI_MCUX_2L_SWAP16"></a>

## 122.7 `CONFIG_MIPI_DSI_MCUX_2L_SWAP16`

**提示（Prompt）**：交换 16 字节颜色（Swap 16 Byte Color）

**说明（Help）**

将 16 字节颜色数据从小端序（Little Endian）交换为大端序（Big Endian）。启用此 Kconfig 后，DSI 预期输入小端 RGB565 数据，随后进行字节交换。译注：原文写作“16 byte”，同时描述 RGB565；这里保留原文单位及其与格式说明的差异。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MIPI_DSI_MCUX_2L && CONFIG_MIPI_DSI
```

**定义位置（Location）**：[`drivers/mipi_dsi/Kconfig.mcux:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dsi/Kconfig.mcux#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】 → NXP MCUX MIPI-DSI 2L 控制器

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DSI_MCUX_2L`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI_MCUX_2L)、[`CONFIG_MIPI_DSI`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI)。

<a id="CONFIG_MIPI_DSI_MCUX_NXP_DCNANO_LCDIF"></a>

## 122.8 `CONFIG_MIPI_DSI_MCUX_NXP_DCNANO_LCDIF`

**提示（Prompt）**：MIPI DSI 使用 NXP DCNano DBI 控制器

**说明（Help）**

使用 DCNano DBI 控制器进行数据传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MIPI_DBI_DCNANO_LCDIF_ENABLED && CONFIG_MIPI_DSI_MCUX_2L && CONFIG_MIPI_DSI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
```

**定义位置（Location）**：[`drivers/mipi_dsi/Kconfig.mcux:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dsi/Kconfig.mcux#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】 → NXP MCUX MIPI-DSI 2L 控制器

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DSI_MCUX_2L`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI_MCUX_2L)、[`CONFIG_MIPI_DSI`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI)、[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)。

<a id="CONFIG_MIPI_DSI_NXP_DWC"></a>

## 122.9 `CONFIG_MIPI_DSI_NXP_DWC`

**提示（Prompt）**：NXP DWC MIPI-DSI 主机控制器

**说明（Help）**

NXP MIPI DSI DWC 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MIPI_DSI_DWC_ENABLED && CONFIG_MIPI_DSI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mipi_dsi/Kconfig.mcux:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dsi/Kconfig.mcux#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DSI`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI)。

<a id="CONFIG_MIPI_DSI_RENESAS_RA"></a>

## 122.10 `CONFIG_MIPI_DSI_RENESAS_RA`

**提示（Prompt）**：Renesas RA MIPI-DSI 主机控制器

**说明（Help）**

Renesas RA MIPI DSI 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_MIPI_DSI_ENABLED && CONFIG_MIPI_DSI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_MIPI_DSI
```

**定义位置（Location）**：[`drivers/mipi_dsi/Kconfig.renesas_ra:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dsi/Kconfig.renesas_ra#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DSI`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI)、[`CONFIG_USE_RA_FSP_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_MIPI_DSI)。

<a id="CONFIG_MIPI_DSI_RENESAS_RZ"></a>

## 122.11 `CONFIG_MIPI_DSI_RENESAS_RZ`

**提示（Prompt）**：Renesas RZ MIPI-DSI 主机控制器

**说明（Help）**

Renesas RZ MIPI DSI 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_MIPI_DSI_ENABLED && CONFIG_MIPI_DSI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_MIPI_DSI
```

**定义位置（Location）**：[`drivers/mipi_dsi/Kconfig.renesas_rz:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dsi/Kconfig.renesas_rz#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DSI`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI)、[`CONFIG_USE_RZ_FSP_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_MIPI_DSI)。

<a id="CONFIG_MIPI_DSI_STM32"></a>

## 122.12 `CONFIG_MIPI_DSI_STM32`

**提示（Prompt）**：STM32 MIPI-DSI 主机控制器

**说明（Help）**

STM32 MIPI DSI 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_MIPI_DSI_ENABLED && DT_HAS_ST_STM32_LTDC_ENABLED && CONFIG_MIPI_DSI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RESET
CONFIG_USE_STM32_HAL_DSI
```

**定义位置（Location）**：[`drivers/mipi_dsi/Kconfig.stm32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dsi/Kconfig.stm32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DSI`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_USE_STM32_HAL_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DSI)。

<!-- kconfig-navigation -->

[上一章](P121_drivers_mipi_dbi_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P123_drivers_misc_配置项参考.md)
