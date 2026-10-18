---
id: learning.zephyr-docs.kconfig-reference.page-121
title: "`drivers/mipi_dbi`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第121章\_`drivers/mipi_dbi`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/mipi_dbi` 的 18 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MIPI_DBI"></a>

## 121.1 `CONFIG_MIPI_DBI`

**提示（Prompt）**：MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】

**说明（Help）**

添加兼容 MIPI-DBI 的主机控制器（Host Controller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_AC057TC1
CONFIG_ED2208_GCA
CONFIG_GC9X01X
CONFIG_HX8353E
CONFIG_ILI9163C
CONFIG_ILI9340
CONFIG_ILI9341
CONFIG_ILI9342C
CONFIG_ILI9488
CONFIG_PCD8544
CONFIG_SSD1322
CONFIG_SSD1327_5
CONFIG_SSD1331
CONFIG_SSD135X
CONFIG_SSD16XX
CONFIG_ST730X
CONFIG_ST75256
CONFIG_ST7586S
CONFIG_ST7735R
CONFIG_ST7789V
CONFIG_ST7796S
CONFIG_UC81XX
CONFIG_MIPI_DSI_MCUX_NXP_DCNANO_LCDIF
```

**定义位置（Location）**：[`drivers/mipi_dbi/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_AC057TC1`](P077_drivers_display_配置项参考_1.md#CONFIG_AC057TC1)、[`CONFIG_ED2208_GCA`](P077_drivers_display_配置项参考_1.md#CONFIG_ED2208_GCA)、[`CONFIG_GC9X01X`](P077_drivers_display_配置项参考_1.md#CONFIG_GC9X01X)、[`CONFIG_HX8353E`](P077_drivers_display_配置项参考_1.md#CONFIG_HX8353E)、[`CONFIG_ILI9163C`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9163C)、[`CONFIG_ILI9340`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9340)、[`CONFIG_ILI9341`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9341)、[`CONFIG_ILI9342C`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9342C)、[`CONFIG_ILI9488`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9488)、[`CONFIG_PCD8544`](P077_drivers_display_配置项参考_1.md#CONFIG_PCD8544)、[`CONFIG_SSD1322`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1322)、[`CONFIG_SSD1327_5`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1327_5)、[`CONFIG_SSD1331`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1331)、[`CONFIG_SSD135X`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD135X)、[`CONFIG_SSD16XX`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD16XX)、[`CONFIG_ST730X`](P078_drivers_display_配置项参考_2.md#CONFIG_ST730X)、[`CONFIG_ST75256`](P078_drivers_display_配置项参考_2.md#CONFIG_ST75256)、[`CONFIG_ST7586S`](P078_drivers_display_配置项参考_2.md#CONFIG_ST7586S)、[`CONFIG_ST7735R`](P078_drivers_display_配置项参考_2.md#CONFIG_ST7735R)、[`CONFIG_ST7789V`](P078_drivers_display_配置项参考_2.md#CONFIG_ST7789V)、[`CONFIG_ST7796S`](P078_drivers_display_配置项参考_2.md#CONFIG_ST7796S)、[`CONFIG_UC81XX`](P078_drivers_display_配置项参考_2.md#CONFIG_UC81XX)、[`CONFIG_MIPI_DSI_MCUX_NXP_DCNANO_LCDIF`](P122_drivers_mipi_dsi_配置项参考.md#CONFIG_MIPI_DSI_MCUX_NXP_DCNANO_LCDIF)。

<a id="CONFIG_MIPI_DBI_BFLB"></a>

## 121.2 `CONFIG_MIPI_DBI_BFLB`

**提示（Prompt）**：Bouffalolab MIPI DBI 驱动

**说明（Help）**

启用 Bouffalolab DBI 控制器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_DBI_ENABLED && CONFIG_MIPI_DBI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/mipi_dbi/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_MIPI_DBI_BFLB_ASSUME_HOLD_ON_CS"></a>

## 121.3 `CONFIG_MIPI_DBI_BFLB_ASSUME_HOLD_ON_CS`

**提示（Prompt）**：默认使用保持片选（HOLD_ON_CS）模式

**说明（Help）**

按预期，表现得像显示驱动已经传入 `SPI_HOLD_ON_CS` 一样。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MIPI_DBI_BFLB && CONFIG_MIPI_DBI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mipi_dbi/Kconfig.bflb:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/Kconfig.bflb#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】 → Bouffalolab MIPI DBI 驱动

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI_BFLB`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI_BFLB)、[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)。

<a id="CONFIG_MIPI_DBI_BITBANG"></a>

## 121.4 `CONFIG_MIPI_DBI_BITBANG`

**提示（Prompt）**：MIPI DBI 位操作模拟（Bit Banging）驱动

**说明（Help）**

启用 MIPI DBI 位操作模拟驱动支持。此驱动使用 GPIO 实现兼容 MIPI-DBI 模式 A 和模式 B 的控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_MIPI_DBI_BITBANG_ENABLED && CONFIG_MIPI_DBI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/mipi_dbi/Kconfig.bitbang:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/Kconfig.bitbang#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_MIPI_DBI_ESP32"></a>

## 121.5 `CONFIG_MIPI_DBI_ESP32`

**提示（Prompt）**：ESP32 LCD-CAM 显示接口的 MIPI DBI 驱动

**说明（Help）**

启用 ESP32 LCD-CAM 显示接口支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_LCD_CAM_MIPI_DBI_ENABLED && CONFIG_MIPI_DBI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/mipi_dbi/Kconfig.esp32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/Kconfig.esp32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_MIPI_DBI_INIT_PRIORITY"></a>

## 121.6 `CONFIG_MIPI_DBI_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Initialization Priority）

**说明（Help）**

MIPI-DBI 主机控制器初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MIPI_DBI
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/mipi_dbi/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)。

<a id="CONFIG_MIPI_DBI_NXP_DCNANO_LCDIF"></a>

## 121.7 `CONFIG_MIPI_DBI_NXP_DCNANO_LCDIF`

**提示（Prompt）**：NXP DCnano LCDIF 的 MIPI DBI 驱动

**说明（Help）**

启用 NXP 基于 FlexIO 的 LCDIF 控制器的 MIPI DBI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MIPI_DBI_DCNANO_LCDIF_ENABLED && CONFIG_MIPI_DBI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/mipi_dbi/Kconfig.nxp_dcnano_lcdif:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/Kconfig.nxp_dcnano_lcdif#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_MIPI_DBI_NXP_FLEXIO_LCDIF"></a>

## 121.8 `CONFIG_MIPI_DBI_NXP_FLEXIO_LCDIF`

**提示（Prompt）**：NXP FlexIO LCDIF 的 MIPI DBI 驱动

**说明（Help）**

启用 NXP 基于 FlexIO 的 LCDIF 控制器的 MIPI DBI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MIPI_DBI_FLEXIO_LCDIF_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_MIPI_DBI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MCUX_FLEXIO
CONFIG_DMA
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/mipi_dbi/Kconfig.nxp_flexio_lcdif:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/Kconfig.nxp_flexio_lcdif#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)、[`CONFIG_MCUX_FLEXIO`](P123_drivers_misc_配置项参考.md#CONFIG_MCUX_FLEXIO)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_MIPI_DBI_NXP_FLEXIO_LCDIF_SMARTDMA"></a>

## 121.9 `CONFIG_MIPI_DBI_NXP_FLEXIO_LCDIF_SMARTDMA`

**提示（Prompt）**：FlexIO LCDIF 使用 SMARTDMA 控制器

**说明（Help）**

使用 SMARTDMA 加速 FlexIO LCDIF 数据传输，取代通用 DMA 控制器，例如 eDMA。当 FlexIO LCDIF 实例自身的 `dmas`/`dma-names` 设备树属性将它连接到 SMARTDMA 控制器时，此项自动启用；这与 `DMA_MCUX_EDMA` 根据 eDMA 控制器自身设备树节点自动启用的方式对应。此项不直接由 `DMA_MCUX_SMARTDMA` 驱动，因为部分开发板为其他外设（例如 MIPI DSI）启用了该选项，却仍将 FlexIO LCDIF 实例连接到通用 DMA 控制器。某些 SoC 还需一条 INPUTMUX 路由（见 `mux-states` 设备树属性），把 FlexIO 中断请求（IRQ）连接到 SmartDMA 触发输入。使用此路由的开发板必须自行启用 `CONFIG_MUX` 和 `CONFIG_MUX_NXP_INPUTMUX`；若在此处使用 `select`，会经由 `DMA_MCUX_SMARTDMA -> DMA` 形成 Kconfig 依赖环。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_MCUX_SMARTDMA && CONFIG_MIPI_DBI_NXP_FLEXIO_LCDIF && CONFIG_MIPI_DBI
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`drivers/mipi_dbi/Kconfig.nxp_flexio_lcdif:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/Kconfig.nxp_flexio_lcdif#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】 → NXP FlexIO LCDIF 的 MIPI DBI 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_MCUX_SMARTDMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_MCUX_SMARTDMA)、[`CONFIG_MIPI_DBI_NXP_FLEXIO_LCDIF`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI_NXP_FLEXIO_LCDIF)、[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)。

<a id="CONFIG_MIPI_DBI_NXP_LCDIC"></a>

## 121.10 `CONFIG_MIPI_DBI_NXP_LCDIC`

**提示（Prompt）**：NXP MIPI DBI LCDIC 驱动

**说明（Help）**

启用 NXP SPI LCDIC 显示控制器驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LCDIC_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_MIPI_DBI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/mipi_dbi/Kconfig.nxp_lcdic:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/Kconfig.nxp_lcdic#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_MIPI_DBI_NXP_LCDIC_DMA"></a>

## 121.11 `CONFIG_MIPI_DBI_NXP_LCDIC_DMA`

**提示（Prompt）**：LCDIC 驱动传输使用 DMA

**说明（Help）**

LCDIC 驱动发送数据时使用 DMA 传输。命令仍以轮询模式（Polling Mode）发送。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MIPI_DBI_NXP_LCDIC && CONFIG_MIPI_DBI
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/mipi_dbi/Kconfig.nxp_lcdic:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/Kconfig.nxp_lcdic#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】 → NXP MIPI DBI LCDIC 驱动

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI_NXP_LCDIC`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI_NXP_LCDIC)、[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_MIPI_DBI_RPI_PICO_PIO"></a>

## 121.12 `CONFIG_MIPI_DBI_RPI_PICO_PIO`

**提示（Prompt）**：使用 PIO 的 MIPI DBI 驱动

**说明（Help）**

启用 MIPI DBI 驱动支持。此驱动使用可编程 I/O（PIO）和 DMA 实现兼容 MIPI-DBI 模式 B 的控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_MIPI_DBI_PIO_ENABLED && CONFIG_MIPI_DBI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_PICOSDK_USE_PIO
CONFIG_PICOSDK_USE_DMA
```

**定义位置（Location）**：[`drivers/mipi_dbi/Kconfig.rpi_pico:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/Kconfig.rpi_pico#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PICOSDK_USE_PIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_PIO)、[`CONFIG_PICOSDK_USE_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_DMA)。

<a id="CONFIG_MIPI_DBI_SF32LB"></a>

## 121.13 `CONFIG_MIPI_DBI_SF32LB`

**提示（Prompt）**：SF32LB MIPI DBI 驱动

**说明（Help）**

启用 SF32LB MIPI DBI 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_LCDC_MIPI_DBI_ENABLED && CONFIG_MIPI_DBI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mipi_dbi/Kconfig.sf32lb_lcdc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/Kconfig.sf32lb_lcdc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)。

<a id="CONFIG_MIPI_DBI_SMARTBOND"></a>

## 121.14 `CONFIG_MIPI_DBI_SMARTBOND`

**提示（Prompt）**：SmartBond MIPI DBI 主机控制器驱动

**说明（Help）**

启用 SmartBond MIPI DBI 主机控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_MIPI_DBI_ENABLED && CONFIG_MIPI_DBI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/mipi_dbi/Kconfig.smartbond:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/Kconfig.smartbond#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_MIPI_DBI_SPI"></a>

## 121.15 `CONFIG_MIPI_DBI_SPI`

**提示（Prompt）**：MIPI DBI SPI 驱动

**说明（Help）**

启用 MIPI DBI SPI 驱动支持。此驱动使用 SPI 设备，以及用于复位和数据／命令（D/C）信号的 GPIO 输出，实现兼容 MIPI-DBI 模式 C 的控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_MIPI_DBI_SPI_ENABLED && CONFIG_MIPI_DBI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/mipi_dbi/Kconfig.spi:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/Kconfig.spi#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_MIPI_DBI_SPI_3WIRE"></a>

## 121.16 `CONFIG_MIPI_DBI_SPI_3WIRE`

**提示（Prompt）**：模拟三线 SPI（Emulated 3-wire SPI）支持

**说明（Help）**

在 MIPI DBI SPI 驱动中支持三线 MIPI DBI（模式 C 选项 2）。这需要手动为每个字节打包一个数据／命令位，可能降低显示数据传输速度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MIPI_DBI_SPI && CONFIG_MIPI_DBI
```

**定义位置（Location）**：[`drivers/mipi_dbi/Kconfig.spi:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/Kconfig.spi#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】 → MIPI DBI SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI_SPI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI_SPI)、[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)。

<a id="CONFIG_MIPI_DBI_STM32_FMC"></a>

## 121.17 `CONFIG_MIPI_DBI_STM32_FMC`

**提示（Prompt）**：STM32 FMC 的 MIPI DBI 驱动

**说明（Help）**

启用基于 STM32 FMC 的控制器的 MIPI DBI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_FMC_MIPI_DBI_ENABLED && CONFIG_MIPI_DBI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MEMC
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/mipi_dbi/Kconfig.stm32_fmc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/Kconfig.stm32_fmc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)、[`CONFIG_MEMC`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_MIPI_DBI_STM32_FMC_MEM_BARRIER"></a>

## 121.18 `CONFIG_MIPI_DBI_STM32_FMC_MEM_BARRIER`

**提示（Prompt）**：每次访问地址寄存器和数据寄存器后添加内存屏障（Memory Barrier）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MIPI_DBI_STM32_FMC && CONFIG_MIPI_DBI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mipi_dbi/Kconfig.stm32_fmc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mipi_dbi/Kconfig.stm32_fmc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示总线接口（MIPI-DBI）主机控制器驱动【实验性】 → STM32 FMC 的 MIPI DBI 驱动

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DBI_STM32_FMC`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI_STM32_FMC)、[`CONFIG_MIPI_DBI`](P121_drivers_mipi_dbi_配置项参考.md#CONFIG_MIPI_DBI)。

<!-- kconfig-navigation -->

[上一章](P120_drivers_mfd_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P122_drivers_mipi_dsi_配置项参考.md)
