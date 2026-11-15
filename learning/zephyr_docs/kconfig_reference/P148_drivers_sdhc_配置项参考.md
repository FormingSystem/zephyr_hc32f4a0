---
id: learning.zephyr-docs.kconfig-reference.page-148
title: "`drivers/sdhc`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第148章\_`drivers/sdhc`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/sdhc` 的 65 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_AMBIQ_SDIO_ASYNC"></a>

## 148.1 `CONFIG_AMBIQ_SDIO_ASYNC`

**提示（Prompt）**：Ambiq SDIO 异步模式（Async Mode）

**说明（Help）**

此选项启用 Ambiq SDIO 异步模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_SDIO_ENABLED && CONFIG_SDHC_AMBIQ && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.ambiq:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.ambiq#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → Ambiq SDHC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC_AMBIQ`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_AMBIQ)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_CDNS_DESC_COUNT"></a>

## 148.2 `CONFIG_CDNS_DESC_COUNT`

**提示（Prompt）**：分配的描述符数量（Descriptor Count）

**说明（Help）**

SD 主控制器进行读写操作前，需要准备 DMA。此选项创建可供高级 DMA（ADMA）使用的静态描述符。设备需要传输超过 `8*64Kb` 数据时，应配置此标志。译注：大小单位 `Kb` 按原文保留。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CDNS_SDHC && CONFIG_SDHC
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.sdhc_cdns:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.sdhc_cdns#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → Cadence SDHC

**配置项引用（Symbol References）**：[`CONFIG_CDNS_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_CDNS_SDHC)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_CDNS_SDHC"></a>

## 148.3 `CONFIG_CDNS_SDHC`

**提示（Prompt）**：Cadence SDHC

**说明（Help）**

启用 Cadence SDMMC 主控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CDNS_SDHC_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.sdhc_cdns:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.sdhc_cdns#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)。

<a id="CONFIG_HEAP_MEM_POOL_ADD_SIZE_SDHC_STM32_SDMMC"></a>

## 148.4 `CONFIG_HEAP_MEM_POOL_ADD_SIZE_SDHC_STM32_SDMMC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

STM32 SDHC/SDMMC 驱动为 DMA 对齐缓冲区分配所需的最小系统堆大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC_STM32_SDMMC && CONFIG_SDHC
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.stm32:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.stm32#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → STM32 SDMMC 驱动（SD/SDIO）

**配置项引用（Symbol References）**：[`CONFIG_SDHC_STM32_SDMMC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_STM32_SDMMC)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_HOST_ADMA2_DESC_SIZE"></a>

## 148.5 `CONFIG_HOST_ADMA2_DESC_SIZE`

**提示（Prompt）**：最大描述符大小（Max Descriptor SIZE）

**说明（Help）**

设置支持的最大描述符数量。译注：帮助正文使用数量，而标题使用大小；保留原文差异。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_XLNX_SDHC && CONFIG_SDHC
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.xlnx:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.xlnx#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → Xilinx SDHC 驱动

**配置项引用（Symbol References）**：[`CONFIG_XLNX_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_XLNX_SDHC)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_IMX_USDHC"></a>

## 148.6 `CONFIG_IMX_USDHC`

**提示（Prompt）**：NXP i.MX USDHC 驱动

**说明（Help）**

启用 NXP i.MX SD 主控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_USDHC_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SDHC_SUPPORTS_UHS
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
CONFIG_SDHC_SUPPORTS_SCATTER_GATHER_TRANSFER if CONFIG_IMX_USDHC_DMA_SUPPORT
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.imx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.imx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SDHC_SUPPORTS_UHS`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_UHS)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)、[`CONFIG_SDHC_SUPPORTS_SCATTER_GATHER_TRANSFER`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_SCATTER_GATHER_TRANSFER)、[`CONFIG_IMX_USDHC_DMA_SUPPORT`](P148_drivers_sdhc_配置项参考.md#CONFIG_IMX_USDHC_DMA_SUPPORT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_IMX_USDHC_DAT3_DETECT_RETRY"></a>

## 148.7 `CONFIG_IMX_USDHC_DAT3_DETECT_RETRY`

**提示（Prompt）**：基于 DAT3 的卡检测重试次数（Card Detection Retries）

**说明（Help）**

DAT3 卡检测的重试次数，用于减少误判为无卡（False Negative）的情况。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IMX_USDHC && CONFIG_SDHC
```

**默认值（Defaults）**

```text
1
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
10
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.imx:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.imx#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → NXP i.MX USDHC 驱动

**配置项引用（Symbol References）**：[`CONFIG_IMX_USDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_IMX_USDHC)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_IMX_USDHC_DAT3_PWR_TOGGLE"></a>

## 148.8 `CONFIG_IMX_USDHC_DAT3_PWR_TOGGLE`

**提示（Prompt）**：拉低 DAT3 线时切换电源（Toggle Power）

**说明（Help）**

拉低 DAT3 线时，通过切换 SD 卡电源清除 DAT3 上拉。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IMX_USDHC && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.imx:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.imx#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → NXP i.MX USDHC 驱动

**配置项引用（Symbol References）**：[`CONFIG_IMX_USDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_IMX_USDHC)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_IMX_USDHC_DMA_BUFFER_SIZE"></a>

## 148.9 `CONFIG_IMX_USDHC_DMA_BUFFER_SIZE`

**提示（Prompt）**：DMA 描述符缓冲区大小，单位为字节

**说明（Help）**

USDHC ADMA 描述符缓冲区大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IMX_USDHC_DMA_SUPPORT && CONFIG_IMX_USDHC && CONFIG_SDHC
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.imx:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.imx#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → NXP i.MX USDHC 驱动 → USDHC 的 DMA 支持

**配置项引用（Symbol References）**：[`CONFIG_IMX_USDHC_DMA_SUPPORT`](P148_drivers_sdhc_配置项参考.md#CONFIG_IMX_USDHC_DMA_SUPPORT)、[`CONFIG_IMX_USDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_IMX_USDHC)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_IMX_USDHC_DMA_SCATTER_GATHER_BUF_COUNT"></a>

## 148.10 `CONFIG_IMX_USDHC_DMA_SCATTER_GATHER_BUF_COUNT`

**提示（Prompt）**：分配的分散／聚集（Scatter-Gather）缓冲区数量

**说明（Help）**

分配的 USDHC 分散／聚集缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC_SCATTER_GATHER_TRANSFER && CONFIG_IMX_USDHC_DMA_SUPPORT && CONFIG_IMX_USDHC && CONFIG_SDHC
```

**默认值（Defaults）**

```text
36
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.imx:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.imx#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → NXP i.MX USDHC 驱动 → USDHC 的 DMA 支持

**配置项引用（Symbol References）**：[`CONFIG_SDHC_SCATTER_GATHER_TRANSFER`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SCATTER_GATHER_TRANSFER)、[`CONFIG_IMX_USDHC_DMA_SUPPORT`](P148_drivers_sdhc_配置项参考.md#CONFIG_IMX_USDHC_DMA_SUPPORT)、[`CONFIG_IMX_USDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_IMX_USDHC)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_IMX_USDHC_DMA_SUPPORT"></a>

## 148.11 `CONFIG_IMX_USDHC_DMA_SUPPORT`

**提示（Prompt）**：USDHC 的 DMA 支持

**说明（Help）**

启用 USDHC 的 DMA 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IMX_USDHC && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.imx:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.imx#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → NXP i.MX USDHC 驱动

**配置项引用（Symbol References）**：[`CONFIG_IMX_USDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_IMX_USDHC)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_INTEL_EMMC_HOST"></a>

## 148.12 `CONFIG_INTEL_EMMC_HOST`

**提示（Prompt）**：嵌入式多媒体卡（eMMC）驱动

**说明（Help）**

eMMC 驱动支持。虽然此驱动可较容易地移植到符合 eMMC 规范的任意硬件，但原文说明，目前仅使用 Intel eMMC 主控制器完成了验证。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_EMMC_HOST_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
CONFIG_EVENTS
CONFIG_PCIE if n
CONFIG_DYNAMIC_INTERRUPTS if n
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.intel:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.intel#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_PCIE`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)。

<a id="CONFIG_INTEL_EMMC_HOST_ADMA"></a>

## 148.13 `CONFIG_INTEL_EMMC_HOST_ADMA`

**提示（Prompt）**：eMMC 主控制器高级 DMA（ADMA）模式

**说明（Help）**

eMMC 主控制器 ADMA 模式支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INTEL_EMMC_HOST_DMA && CONFIG_INTEL_EMMC_HOST && CONFIG_SDHC
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.intel:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.intel#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → 嵌入式多媒体卡（eMMC）驱动 → eMMC 主控制器 DMA 模式

**配置项引用（Symbol References）**：[`CONFIG_INTEL_EMMC_HOST_DMA`](P148_drivers_sdhc_配置项参考.md#CONFIG_INTEL_EMMC_HOST_DMA)、[`CONFIG_INTEL_EMMC_HOST`](P148_drivers_sdhc_配置项参考.md#CONFIG_INTEL_EMMC_HOST)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_INTEL_EMMC_HOST_ADMA_DESC_SIZE"></a>

## 148.14 `CONFIG_INTEL_EMMC_HOST_ADMA_DESC_SIZE`

**提示（Prompt）**：eMMC 主控制器 ADMA 描述符大小

**说明（Help）**

eMMC 主控制器 ADMA 描述符大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_INTEL_EMMC_HOST_ADMA && CONFIG_INTEL_EMMC_HOST && CONFIG_SDHC
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.intel:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.intel#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → 嵌入式多媒体卡（eMMC）驱动 → eMMC 主控制器 DMA 模式 → eMMC 主控制器高级 DMA（ADMA）模式

**配置项引用（Symbol References）**：[`CONFIG_INTEL_EMMC_HOST_ADMA`](P148_drivers_sdhc_配置项参考.md#CONFIG_INTEL_EMMC_HOST_ADMA)、[`CONFIG_INTEL_EMMC_HOST`](P148_drivers_sdhc_配置项参考.md#CONFIG_INTEL_EMMC_HOST)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_INTEL_EMMC_HOST_AUTO_STOP"></a>

## 148.15 `CONFIG_INTEL_EMMC_HOST_AUTO_STOP`

**提示（Prompt）**：自动停止命令模式（Auto Stop Command Mode）

**说明（Help）**

自动停止命令模式支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INTEL_EMMC_HOST && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.intel:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.intel#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → 嵌入式多媒体卡（eMMC）驱动

**配置项引用（Symbol References）**：[`CONFIG_INTEL_EMMC_HOST`](P148_drivers_sdhc_配置项参考.md#CONFIG_INTEL_EMMC_HOST)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_INTEL_EMMC_HOST_BLOCK_GAP"></a>

## 148.16 `CONFIG_INTEL_EMMC_HOST_BLOCK_GAP`

**提示（Prompt）**：块间隙模式（Block Gap Mode）

**说明（Help）**

块间隙模式支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INTEL_EMMC_HOST_DMA && CONFIG_INTEL_EMMC_HOST && CONFIG_SDHC
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.intel:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.intel#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → 嵌入式多媒体卡（eMMC）驱动

**配置项引用（Symbol References）**：[`CONFIG_INTEL_EMMC_HOST_DMA`](P148_drivers_sdhc_配置项参考.md#CONFIG_INTEL_EMMC_HOST_DMA)、[`CONFIG_INTEL_EMMC_HOST`](P148_drivers_sdhc_配置项参考.md#CONFIG_INTEL_EMMC_HOST)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_INTEL_EMMC_HOST_DMA"></a>

## 148.17 `CONFIG_INTEL_EMMC_HOST_DMA`

**提示（Prompt）**：eMMC 主控制器 DMA 模式

**说明（Help）**

eMMC 主控制器 DMA 模式支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INTEL_EMMC_HOST && CONFIG_SDHC
```

**主动选择（Selects）**

```text
CONFIG_DCACHE
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.intel:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.intel#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → 嵌入式多媒体卡（eMMC）驱动

**配置项引用（Symbol References）**：[`CONFIG_INTEL_EMMC_HOST`](P148_drivers_sdhc_配置项参考.md#CONFIG_INTEL_EMMC_HOST)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)。

<a id="CONFIG_INTEL_EMMC_HOST_INTR"></a>

## 148.18 `CONFIG_INTEL_EMMC_HOST_INTR`

**提示（Prompt）**：eMMC 主控制器中断模式（Interrupt Mode）

**说明（Help）**

eMMC 主控制器中断模式支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INTEL_EMMC_HOST && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.intel:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.intel#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → 嵌入式多媒体卡（eMMC）驱动

**配置项引用（Symbol References）**：[`CONFIG_INTEL_EMMC_HOST`](P148_drivers_sdhc_配置项参考.md#CONFIG_INTEL_EMMC_HOST)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_INTEL_EMMC_HOST_TUNING"></a>

## 148.19 `CONFIG_INTEL_EMMC_HOST_TUNING`

**提示（Prompt）**：主机调谐（Host Tuning）

**说明（Help）**

主机调谐支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INTEL_EMMC_HOST && CONFIG_SDHC
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.intel:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.intel#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → 嵌入式多媒体卡（eMMC）驱动

**配置项引用（Symbol References）**：[`CONFIG_INTEL_EMMC_HOST`](P148_drivers_sdhc_配置项参考.md#CONFIG_INTEL_EMMC_HOST)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_MCUX_SDIF"></a>

## 148.20 `CONFIG_MCUX_SDIF`

**提示（Prompt）**：NXP MCUX SDIF 驱动

**说明（Help）**

启用 NXP SDIF 主控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_SDIF_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.mcux_sdif:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.mcux_sdif#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_MCUX_SDIF_DMA_BUFFER_SIZE"></a>

## 148.21 `CONFIG_MCUX_SDIF_DMA_BUFFER_SIZE`

**提示（Prompt）**：DMA 描述符缓冲区大小，单位为字节

**说明（Help）**

MCUX SDIF DMA 描述符缓冲区大小，单位为字节

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUX_SDIF_DMA_SUPPORT && CONFIG_MCUX_SDIF && CONFIG_SDHC
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.mcux_sdif:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.mcux_sdif#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → NXP MCUX SDIF 驱动 → MCUX SDIF 驱动的 DMA 支持

**配置项引用（Symbol References）**：[`CONFIG_MCUX_SDIF_DMA_SUPPORT`](P148_drivers_sdhc_配置项参考.md#CONFIG_MCUX_SDIF_DMA_SUPPORT)、[`CONFIG_MCUX_SDIF`](P148_drivers_sdhc_配置项参考.md#CONFIG_MCUX_SDIF)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_MCUX_SDIF_DMA_SUPPORT"></a>

## 148.22 `CONFIG_MCUX_SDIF_DMA_SUPPORT`

**提示（Prompt）**：MCUX SDIF 驱动的 DMA 支持

**说明（Help）**

启用 MCUX SDIF 驱动的 DMA 支持。可禁用此项，以减小驱动占用（Footprint）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUX_SDIF && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.mcux_sdif:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.mcux_sdif#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → NXP MCUX SDIF 驱动

**配置项引用（Symbol References）**：[`CONFIG_MCUX_SDIF`](P148_drivers_sdhc_配置项参考.md#CONFIG_MCUX_SDIF)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_RCAR_MMC"></a>

## 148.23 `CONFIG_RCAR_MMC`

**提示（Prompt）**：Renesas R-Car MMC 驱动

**说明（Help）**

Renesas R-Car MMC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RCAR_MMC_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
CONFIG_REGULATOR
CONFIG_GPIO
CONFIG_PINCTRL
CONFIG_SDHC_SUPPORTS_UHS if CONFIG_SDMMC_STACK
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.rcar:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.rcar#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SDHC_SUPPORTS_UHS`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_UHS)、[`CONFIG_SDMMC_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDMMC_STACK)。

<a id="CONFIG_RCAR_MMC_DMA_IRQ_DRIVEN_SUPPORT"></a>

## 148.24 `CONFIG_RCAR_MMC_DMA_IRQ_DRIVEN_SUPPORT`

**提示（Prompt）**：Renesas R-Car MMC 驱动的内部 DMA 中断驱动（IRQ-driven）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RCAR_MMC_DMA_SUPPORT && CONFIG_RCAR_MMC && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.rcar:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.rcar#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → Renesas R-Car MMC 驱动

**配置项引用（Symbol References）**：[`CONFIG_RCAR_MMC_DMA_SUPPORT`](P148_drivers_sdhc_配置项参考.md#CONFIG_RCAR_MMC_DMA_SUPPORT)、[`CONFIG_RCAR_MMC`](P148_drivers_sdhc_配置项参考.md#CONFIG_RCAR_MMC)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_RCAR_MMC_DMA_SUPPORT"></a>

## 148.25 `CONFIG_RCAR_MMC_DMA_SUPPORT`

**提示（Prompt）**：Renesas R-Car MMC 驱动的内部 DMA 支持

**说明（Help）**

Renesas R-Car MMC 驱动的内部 DMA 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RCAR_MMC && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CACHE_MANAGEMENT
CONFIG_DCACHE
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.rcar:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.rcar#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → Renesas R-Car MMC 驱动

**配置项引用（Symbol References）**：[`CONFIG_RCAR_MMC`](P148_drivers_sdhc_配置项参考.md#CONFIG_RCAR_MMC)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)。

<a id="CONFIG_RCAR_MMC_SCC_SUPPORT"></a>

## 148.26 `CONFIG_RCAR_MMC_SCC_SUPPORT`

**提示（Prompt）**：采样时钟控制器（SCC）支持

**说明（Help）**

为 Renesas R-Car MMC 驱动启用采样时钟控制器（Sampling Clock Controller，SCC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RCAR_MMC && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.rcar:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.rcar#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → Renesas R-Car MMC 驱动

**配置项引用（Symbol References）**：[`CONFIG_RCAR_MMC`](P148_drivers_sdhc_配置项参考.md#CONFIG_RCAR_MMC)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_SAM_HSMCI"></a>

## 148.27 `CONFIG_SAM_HSMCI`

**提示（Prompt）**：ATMEL SAM HSMCI 驱动

**说明（Help）**

启用 ATMEL SAM HSMCI MMC/SD 卡驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_HSMCI_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.sam_hsmci:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.sam_hsmci#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)。

<a id="CONFIG_SAM_HSMCI_PDCMODE"></a>

## 148.28 `CONFIG_SAM_HSMCI_PDCMODE`

**提示（Prompt）**：可用时使用外设 DMA 控制器（PDC）

**说明（Help）**

如果支持，则使用外设 DMA 控制器（Peripheral DMA Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SAM_HSMCI && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_SAM4E
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.sam_hsmci:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.sam_hsmci#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → ATMEL SAM HSMCI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SAM_HSMCI`](P148_drivers_sdhc_配置项参考.md#CONFIG_SAM_HSMCI)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SOC_SERIES_SAM4E`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_SAM4E)。

<a id="CONFIG_SAM_HSMCI_PWRSAVE"></a>

## 148.29 `CONFIG_SAM_HSMCI_PWRSAVE`

**提示（Prompt）**：卡非活动期间节能（Power Save）

**说明（Help）**

节能模式在 SD 卡不活动时降低时钟速度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SAM_HSMCI && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.sam_hsmci:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.sam_hsmci#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → ATMEL SAM HSMCI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SAM_HSMCI`](P148_drivers_sdhc_配置项参考.md#CONFIG_SAM_HSMCI)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_SAM_HSMCI_PWRSAVE_DIV"></a>

## 148.30 `CONFIG_SAM_HSMCI_PWRSAVE_DIV`

**提示（Prompt）**：节能模式下的时钟分频值（Divisor Value）

**说明（Help）**

SD 时钟频率除以 `2**(N+1)`，其中 N 是分频值。有效值为 0～7。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SAM_HSMCI_PWRSAVE && CONFIG_SAM_HSMCI && CONFIG_SDHC
```

**默认值（Defaults）**

```text
7
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.sam_hsmci:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.sam_hsmci#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → ATMEL SAM HSMCI 驱动 → 卡非活动期间节能（Power Save）

**配置项引用（Symbol References）**：[`CONFIG_SAM_HSMCI_PWRSAVE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SAM_HSMCI_PWRSAVE)、[`CONFIG_SAM_HSMCI`](P148_drivers_sdhc_配置项参考.md#CONFIG_SAM_HSMCI)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_SAM_SDMMC"></a>

## 148.31 `CONFIG_SAM_SDMMC`

**提示（Prompt）**：Microchip SAM SDMMC 驱动

**说明（Help）**

启用 Microchip SAM SDMMC MMC/SD 卡驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_SAMA7G5_SDMMC_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CACHE_MANAGEMENT
CONFIG_PINCTRL
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.sam_sdmmc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.sam_sdmmc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)。

<a id="CONFIG_SDHC"></a>

## 148.32 `CONFIG_SDHC`

**提示（Prompt）**：安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**说明（Help）**

纳入与 SD 卡交互的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_WIFI_NXP
CONFIG_SD_STACK
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NXP)、[`CONFIG_SD_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SD_STACK)。

<a id="CONFIG_SDHC_AMBIQ"></a>

## 148.33 `CONFIG_SDHC_AMBIQ`

**提示（Prompt）**：Ambiq SDHC 驱动

**说明（Help）**

此选项启用 Ambiq Apollo 系列的 SDHC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_SDIO_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_AMBIQ_HAL
CONFIG_AMBIQ_HAL_USE_SDIO
CONFIG_PINCTRL
CONFIG_GPIO
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.ambiq:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.ambiq#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_HAL_USE_SDIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_SDIO)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)。

<a id="CONFIG_SDHC_AMBIQ_HANDLE_CACHE"></a>

## 148.34 `CONFIG_SDHC_AMBIQ_HANDLE_CACHE`

**提示（Prompt）**：在 SDHC 驱动中开启缓存处理（Cache Handling）

**说明（Help）**

如果上层已处理缓存（Cache），则禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_MANAGEMENT && CONFIG_DCACHE && CONFIG_SDHC_AMBIQ && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.ambiq:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.ambiq#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → Ambiq SDHC 驱动

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_SDHC_AMBIQ`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_AMBIQ)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_SDHC_AMEBA"></a>

## 148.35 `CONFIG_SDHC_AMEBA`

**提示（Prompt）**：AMEBA SD 主控制器

**说明（Help）**

启用 Realtek Ameba SD 主控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_AMEBA_SDHOST_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_GPIO
CONFIG_REALTEK_AMEBA_OS_WRAPPER
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.ameba:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.ameba#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_REALTEK_AMEBA_OS_WRAPPER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REALTEK_AMEBA_OS_WRAPPER)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)。

<a id="CONFIG_SDHC_BFLB"></a>

## 148.36 `CONFIG_SDHC_BFLB`

**提示（Prompt）**：Bouffalo Lab SDHC 驱动

**说明（Help）**

启用 Bouffalo Lab SD 主控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_SDHC_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SDHC_BFLB_DMA"></a>

## 148.37 `CONFIG_SDHC_BFLB_DMA`

**提示（Prompt）**：Bouffalo Lab SDHC 使用 DMA

**说明（Help）**

使用 ADMA2，即 SDHC 控制器专用的 DMA 系统，取代轮询以加快数据传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC_BFLB && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.bflb:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.bflb#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → Bouffalo Lab SDHC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC_BFLB`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_BFLB)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_SDHC_BUFFER_ALIGNMENT"></a>

## 148.38 `CONFIG_SDHC_BUFFER_ALIGNMENT`

原库同名定义共 3 条；本项为数据库第 16514 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SDHC 缓冲区放入可缓存区域（Cacheable Region）时，应按 `DCACHE_LINE_SIZE` 的值对齐。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC_AMBIQ && CONFIG_SDHC
```

**默认值（Defaults）**

```text
CONFIG_DCACHE_LINE_SIZE if CONFIG_DCACHE
16
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.ambiq:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.ambiq#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → Ambiq SDHC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC_AMBIQ`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_AMBIQ)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_DCACHE_LINE_SIZE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE_LINE_SIZE)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)。

<a id="CONFIG_SDHC_BUFFER_ALIGNMENT--record-16515"></a>

## 148.39 `CONFIG_SDHC_BUFFER_ALIGNMENT`

原库同名定义共 3 条；本项为数据库第 16515 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

SDHC 缓冲区放入可缓存区域（Cacheable Region）时，应按 `DCACHE_LINE_SIZE` 的值对齐。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC_INFINEON_CAT1_PDL && CONFIG_SDHC
```

**默认值（Defaults）**

```text
CONFIG_DCACHE_LINE_SIZE if CONFIG_DCACHE
1
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.infineon:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.infineon#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → Infineon SDHC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC_INFINEON_CAT1_PDL`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_INFINEON_CAT1_PDL)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_DCACHE_LINE_SIZE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE_LINE_SIZE)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)。

<a id="CONFIG_SDHC_BUFFER_ALIGNMENT--record-16516"></a>

## 148.40 `CONFIG_SDHC_BUFFER_ALIGNMENT`

原库同名定义共 3 条；本项为数据库第 16516 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

部分 SD 主控制器要求数据缓冲区对齐，DMA 才能正确工作。有对齐要求的设备应更改此默认值；该值表示所需缓冲区对齐字节数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_SDHC_ESP32"></a>

## 148.41 `CONFIG_SDHC_ESP32`

**提示（Prompt）**：ESP32 SDHC 驱动

**说明（Help）**

启用 ESP32 SD 主控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_SDHC_SLOT_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.esp32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.esp32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SDHC_ESP32_SDIO"></a>

## 148.42 `CONFIG_SDHC_ESP32_SDIO`

**提示（Prompt）**：SDIO 主机支持，包括 CMD53 数据路径和卡中断

**说明（Help）**

启用 CMD53 数据阶段处理和异步 SDIO 卡中断投递，使 Zephyr SDIO 协议栈能够驱动连接到 ESP32 SDMMC 控制器的 SDIO 外设。不启用此项，CMD52 也可以工作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC_ESP32 && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y if CONFIG_SDIO_STACK
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.esp32:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.esp32#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → ESP32 SDHC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC_ESP32`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_ESP32)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SDIO_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDIO_STACK)。

<a id="CONFIG_SDHC_INFINEON_CAT1_PDL"></a>

## 148.43 `CONFIG_SDHC_INFINEON_CAT1_PDL`

**提示（Prompt）**：Infineon SDHC 驱动

**说明（Help）**

此选项启用 Infineon 系列基于外设驱动库（PDL）的 SDHC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_SDHC_SDIO_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_SDIO
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
CONFIG_SDHC_SUPPORTS_UHS
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.infineon:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.infineon#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_USE_INFINEON_SDIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_SDIO)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)、[`CONFIG_SDHC_SUPPORTS_UHS`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_UHS)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SDHC_INIT_PRIORITY"></a>

## 148.44 `CONFIG_SDHC_INIT_PRIORITY`

**提示（Prompt）**：SDHC 驱动初始化优先级

**说明（Help）**

SDHC 驱动的系统初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_SDHC_LITEX_LITESDCARD"></a>

## 148.45 `CONFIG_SDHC_LITEX_LITESDCARD`

**提示（Prompt）**：LiteX LiteSDCard SDHC 驱动

**说明（Help）**

LiteX LiteSDCard 的 SDHC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LITEX_MMC_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
CONFIG_EVENTS
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.litex:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.litex#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_SDHC_LITEX_LITESDCARD_NO_COHERENT_DMA"></a>

## 148.46 `CONFIG_SDHC_LITEX_LITESDCARD_NO_COHERENT_DMA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果 LiteSDCard 模块未连接到具备一致性（Coherent）的 DMA 总线，则需要启用此项，也就是在 DMA 操作前后需要管理缓存。

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
CONFIG_CACHE_MANAGEMENT
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.litex:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.litex#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → LiteX LiteSDCard SDHC 驱动

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)。

<a id="CONFIG_SDHC_MAX32"></a>

## 148.47 `CONFIG_SDHC_MAX32`

**提示（Prompt）**：Analog Devices MAX32 SDHC 驱动

**说明（Help）**

MAX32 系列的 SDHC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MAX32_SDHC_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.max32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.max32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)。

<a id="CONFIG_SDHC_MCHP_G1"></a>

## 148.48 `CONFIG_SDHC_MCHP_G1`

**提示（Prompt）**：Microchip SDHC G1 驱动

**说明（Help）**

启用 Microchip SDHC MMC/SD 卡 G1 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_SDHC_G1_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.mchp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.mchp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)。

<a id="CONFIG_SDHC_NUMAKER"></a>

## 148.49 `CONFIG_SDHC_NUMAKER`

**提示（Prompt）**：Nuvoton NuMaker SDHC 驱动

**说明（Help）**

启用 Nuvoton NuMaker 系列处理器的 SDHC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NUVOTON_NUMAKER_SDHC_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.numaker:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.numaker#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)。

<a id="CONFIG_SDHC_NUMAKER_CMD_RETRIES"></a>

## 148.50 `CONFIG_SDHC_NUMAKER_CMD_RETRIES`

**提示（Prompt）**：向卡发送命令的重试次数

**说明（Help）**

向 SD 卡发送命令失败时的重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC_NUMAKER && CONFIG_SDHC
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.numaker:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.numaker#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → Nuvoton NuMaker SDHC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC_NUMAKER`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_NUMAKER)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_SDHC_NUMAKER_CMD_TIMEOUT"></a>

## 148.51 `CONFIG_SDHC_NUMAKER_CMD_TIMEOUT`

**提示（Prompt）**：SD 命令超时，单位为毫秒

**说明（Help）**

SD 命令的默认超时时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC_NUMAKER && CONFIG_SDHC
```

**默认值（Defaults）**

```text
200
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.numaker:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.numaker#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → Nuvoton NuMaker SDHC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC_NUMAKER`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_NUMAKER)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_SDHC_RENESAS_RA"></a>

## 148.52 `CONFIG_SDHC_RENESAS_RA`

**提示（Prompt）**：Renesas RA SDHI 驱动

**说明（Help）**

启用 Renesas SD 主控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_SDHC_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
CONFIG_USE_RA_FSP_SDHI
CONFIG_USE_RA_FSP_DTC
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.renesas_ra:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.renesas_ra#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)、[`CONFIG_USE_RA_FSP_SDHI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_SDHI)、[`CONFIG_USE_RA_FSP_DTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_DTC)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SDHC_SCATTER_GATHER_TRANSFER"></a>

## 148.53 `CONFIG_SDHC_SCATTER_GATHER_TRANSFER`

**提示（Prompt）**：分散／聚集（Scatter-Gather）API

**说明（Help）**

启用 SDHC 分散／聚集 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC_SUPPORTS_SCATTER_GATHER_TRANSFER && CONFIG_SDHC
```

**被选择（Selected by）**

```text
CONFIG_NXP_WIFI_TX_RX_ZERO_COPY
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC_SUPPORTS_SCATTER_GATHER_TRANSFER`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_SCATTER_GATHER_TRANSFER)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_NXP_WIFI_TX_RX_ZERO_COPY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_WIFI_TX_RX_ZERO_COPY)。

<a id="CONFIG_SDHC_STM32_DMA_MODE"></a>

## 148.54 `CONFIG_SDHC_STM32_DMA_MODE`

**提示（Prompt）**：数据传输使用 DMA 模式

**说明（Help）**

启用数据传输 DMA。禁用后使用轮询模式（Polling Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC_STM32_SDMMC && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CACHE_MANAGEMENT if CONFIG_DCACHE
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.stm32:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.stm32#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → STM32 SDMMC 驱动（SD/SDIO）

**配置项引用（Symbol References）**：[`CONFIG_SDHC_STM32_SDMMC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_STM32_SDMMC)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)。

<a id="CONFIG_SDHC_STM32_SDMMC"></a>

## 148.55 `CONFIG_SDHC_STM32_SDMMC`

**提示（Prompt）**：STM32 SDMMC 驱动（SD/SDIO）

**说明（Help）**

启用 STM32 上通过 SDMMC 外设使用 SD/SDIO 设备的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_SDMMC_ENABLED && !CONFIG_SOC_SERIES_STM32F1X && !CONFIG_SOC_SERIES_STM32F2X && !CONFIG_SOC_SERIES_STM32F4X && !CONFIG_SOC_SERIES_STM32F7X && !CONFIG_SOC_SERIES_STM32L1X && (!CONFIG_SOC_SERIES_STM32L4X || CONFIG_SOC_LINE_STM32L4PLUS) && !CONFIG_SDMMC_STM32 && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_LL_SDMMC
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
CONFIG_PINCTRL
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.stm32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.stm32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32F1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F1X)、[`CONFIG_SOC_SERIES_STM32F2X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F2X)、[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32L1X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L1X)、[`CONFIG_SOC_SERIES_STM32L4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L4X)、[`CONFIG_SOC_LINE_STM32L4PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_LINE_STM32L4PLUS)、[`CONFIG_SDMMC_STM32`](P076_drivers_disk_配置项参考.md#CONFIG_SDMMC_STM32)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_USE_STM32_LL_SDMMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_LL_SDMMC)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F1X`、`CONFIG_SOC_SERIES_STM32F2X`、`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32L1X`、`CONFIG_SOC_SERIES_STM32L4X`。

<a id="CONFIG_SDHC_SUPPORTS_NATIVE_MODE"></a>

## 148.56 `CONFIG_SDHC_SUPPORTS_NATIVE_MODE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

需要原生 SD 模式支持时，由主控制器驱动选中此项，在 SD 协议栈中启用原生协议（Native Protocol）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC
```

**被选择（Selected by）**

```text
CONFIG_SDHC_AMBIQ
CONFIG_SDHC_AMEBA
CONFIG_SDHC_BFLB
CONFIG_SDHC_ESP32
CONFIG_IMX_USDHC
CONFIG_SDHC_INFINEON_CAT1_PDL
CONFIG_INTEL_EMMC_HOST
CONFIG_SDHC_LITEX_LITESDCARD
CONFIG_SDHC_MAX32
CONFIG_SDHC_MCHP_G1
CONFIG_MCUX_SDIF
CONFIG_SDHC_NUMAKER
CONFIG_RCAR_MMC
CONFIG_SDHC_RENESAS_RA
CONFIG_SAM_HSMCI
CONFIG_SAM_SDMMC
CONFIG_CDNS_SDHC
CONFIG_SDHC_STM32_SDMMC
CONFIG_SDHC_TI_AM654
CONFIG_XLNX_SDHC
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SDHC_AMBIQ`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_AMBIQ)、[`CONFIG_SDHC_AMEBA`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_AMEBA)、[`CONFIG_SDHC_BFLB`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_BFLB)、[`CONFIG_SDHC_ESP32`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_ESP32)、[`CONFIG_IMX_USDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_IMX_USDHC)、[`CONFIG_SDHC_INFINEON_CAT1_PDL`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_INFINEON_CAT1_PDL)、[`CONFIG_INTEL_EMMC_HOST`](P148_drivers_sdhc_配置项参考.md#CONFIG_INTEL_EMMC_HOST)、[`CONFIG_SDHC_LITEX_LITESDCARD`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_LITEX_LITESDCARD)、[`CONFIG_SDHC_MAX32`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_MAX32)、[`CONFIG_SDHC_MCHP_G1`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_MCHP_G1)、[`CONFIG_MCUX_SDIF`](P148_drivers_sdhc_配置项参考.md#CONFIG_MCUX_SDIF)、[`CONFIG_SDHC_NUMAKER`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_NUMAKER)、[`CONFIG_RCAR_MMC`](P148_drivers_sdhc_配置项参考.md#CONFIG_RCAR_MMC)、[`CONFIG_SDHC_RENESAS_RA`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_RENESAS_RA)、[`CONFIG_SAM_HSMCI`](P148_drivers_sdhc_配置项参考.md#CONFIG_SAM_HSMCI)、[`CONFIG_SAM_SDMMC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SAM_SDMMC)、[`CONFIG_CDNS_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_CDNS_SDHC)、[`CONFIG_SDHC_STM32_SDMMC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_STM32_SDMMC)、[`CONFIG_SDHC_TI_AM654`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_TI_AM654)、[`CONFIG_XLNX_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_XLNX_SDHC)。

<a id="CONFIG_SDHC_SUPPORTS_SCATTER_GATHER_TRANSFER"></a>

## 148.57 `CONFIG_SDHC_SUPPORTS_SCATTER_GATHER_TRANSFER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

具备分散／聚集传输支持时，由主控制器驱动选中此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC
```

**被选择（Selected by）**

```text
CONFIG_IMX_USDHC
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_IMX_USDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_IMX_USDHC)。

<a id="CONFIG_SDHC_SUPPORTS_SPI_MODE"></a>

## 148.58 `CONFIG_SDHC_SUPPORTS_SPI_MODE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

需要 SPI 模式支持时，由主控制器驱动选中此项，在 SD 协议栈中启用 SPI 协议。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC
```

**被选择（Selected by）**

```text
CONFIG_SPI_SDHC
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SPI_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SPI_SDHC)。

<a id="CONFIG_SDHC_SUPPORTS_UHS"></a>

## 148.59 `CONFIG_SDHC_SUPPORTS_UHS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

具备超高速（UHS）支持时，由主控制器驱动选中此项；启用协议栈的 UHS 部分需要此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC
```

**被选择（Selected by）**

```text
CONFIG_IMX_USDHC
CONFIG_SDHC_INFINEON_CAT1_PDL
CONFIG_RCAR_MMC
CONFIG_SDHC_TI_AM654
CONFIG_XLNX_SDHC
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_IMX_USDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_IMX_USDHC)、[`CONFIG_SDHC_INFINEON_CAT1_PDL`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_INFINEON_CAT1_PDL)、[`CONFIG_RCAR_MMC`](P148_drivers_sdhc_配置项参考.md#CONFIG_RCAR_MMC)、[`CONFIG_SDHC_TI_AM654`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_TI_AM654)、[`CONFIG_XLNX_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_XLNX_SDHC)。

<a id="CONFIG_SDHC_TI_AM654"></a>

## 148.60 `CONFIG_SDHC_TI_AM654`

**提示（Prompt）**：TI AM654 SDHC 驱动

**说明（Help）**

基于中断的 TI AM654 SD/eMMC 主控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_AM654_SDHCI_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
CONFIG_SDHC_SUPPORTS_UHS
CONFIG_EVENTS
CONFIG_REGULATOR
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.ti:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.ti#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)、[`CONFIG_SDHC_SUPPORTS_UHS`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_UHS)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_REGULATOR`](P144_drivers_regulator_配置项参考.md#CONFIG_REGULATOR)。

<a id="CONFIG_SDHC_TI_AM654_ADMA_DESC_LEN"></a>

## 148.61 `CONFIG_SDHC_TI_AM654_ADMA_DESC_LEN`

**提示（Prompt）**：最大 ADMA 描述符行数（Descriptor Lines）

**说明（Help）**

允许的最大 ADMA 描述符行数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC_TI_AM654 && CONFIG_SDHC
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.ti:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.ti#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → TI AM654 SDHC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC_TI_AM654`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_TI_AM654)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_SDHC_TI_AM654_ENABLE_ADMA"></a>

## 148.62 `CONFIG_SDHC_TI_AM654_ENABLE_ADMA`

**提示（Prompt）**：高级 DMA 2（ADMA2）

**说明（Help）**

为 TI AM654 SDHC 驱动启用 ADMA2。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC_TI_AM654 && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CACHE_MANAGEMENT if CONFIG_CPU_HAS_DCACHE
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.ti:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.ti#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → TI AM654 SDHC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC_TI_AM654`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_TI_AM654)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_CPU_HAS_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CPU_HAS_DCACHE)。

<a id="CONFIG_SDHC_TI_AM654_ENABLE_AUTO_STOP"></a>

## 148.63 `CONFIG_SDHC_TI_AM654_ENABLE_AUTO_STOP`

**提示（Prompt）**：自动停止命令（Auto-stop Commands）

**说明（Help）**

在多块事务（Multi-block Transaction）期间启用自动 CMD12/CMD23。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SDHC_TI_AM654 && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.ti:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.ti#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动 → TI AM654 SDHC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC_TI_AM654`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_TI_AM654)、[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)。

<a id="CONFIG_SPI_SDHC"></a>

## 148.64 `CONFIG_SPI_SDHC`

**提示（Prompt）**：通过 SPI 总线传输 SD 协议

**说明（Help）**

启用 SPI SD 主控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_SDHC_SPI_SLOT_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_CRC
CONFIG_SDHC_SUPPORTS_SPI_MODE
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.spi:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.spi#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)、[`CONFIG_SDHC_SUPPORTS_SPI_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_SPI_MODE)。

<a id="CONFIG_XLNX_SDHC"></a>

## 148.65 `CONFIG_XLNX_SDHC`

**提示（Prompt）**：Xilinx SDHC 驱动

**说明（Help）**

启用 Xilinx SD/eMMC 主控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_VERSAL_8_9A_ENABLED && CONFIG_SDHC
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SDHC_SUPPORTS_NATIVE_MODE
CONFIG_SDHC_SUPPORTS_UHS
CONFIG_EVENTS
CONFIG_CLOCK_CONTROL
CONFIG_CLOCK_CONTROL_FIXED_RATE_CLOCK
```

**定义位置（Location）**：[`drivers/sdhc/Kconfig.xlnx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sdhc/Kconfig.xlnx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 安全数字存储卡（Secure Digital，SD 卡）主控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC)、[`CONFIG_SDHC_SUPPORTS_NATIVE_MODE`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_NATIVE_MODE)、[`CONFIG_SDHC_SUPPORTS_UHS`](P148_drivers_sdhc_配置项参考.md#CONFIG_SDHC_SUPPORTS_UHS)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_CLOCK_CONTROL_FIXED_RATE_CLOCK`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_FIXED_RATE_CLOCK)。

<!-- kconfig-navigation -->

[上一章](P147_drivers_rtc_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P149_drivers_sensor_配置项参考_1.md)
