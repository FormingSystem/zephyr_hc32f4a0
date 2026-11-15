---
id: learning.zephyr-docs.kconfig-reference.page-80
title: "`drivers/dma`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第80章\_`drivers/dma`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `drivers/dma` 的 48 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_DMA_NXP_SOF_HOST_DMA_ALIGN"></a>

## 80.1 `CONFIG_DMA_NXP_SOF_HOST_DMA_ALIGN`

**提示（Prompt）**：传给本驱动的内存区域所需的对齐（Alignment），以字节为单位

**说明（Help）**

设置所需的对齐（Alignment），以字节为单位。使用本驱动的组件据此调整内存区域的大小和基地址（Base Address）。由于此驱动实际上并无对应的硬件，而 `memcpy` 也不施加对齐限制，因此此配置本身意义不大。不过，驱动需要表现得如同在控制 DMA 引擎（DMA Engine），所以仍然需要此配置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_NXP_SOF_HOST_DMA && CONFIG_DMA
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/dma/Kconfig.nxp_sof_host_dma:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.nxp_sof_host_dma#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → SOF 主机组件（Host Component）使用的 NXP DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_NXP_SOF_HOST_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_NXP_SOF_HOST_DMA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_PL330"></a>

## 80.2 `CONFIG_DMA_PL330`

**提示（Prompt）**：PL330 DMA 驱动

**说明（Help）**

此选项启用 PL330 DMA 控制器（DMA Controller）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_DMA_PL330_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.dma_pl330:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.dma_pl330#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_RENESAS_RA"></a>

## 80.3 `CONFIG_DMA_RENESAS_RA`

**提示（Prompt）**：瑞萨（Renesas）RA DMAC

**说明（Help）**

启用瑞萨（Renesas）RA DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_DMA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.renesas_ra:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.renesas_ra#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_USE_RA_FSP_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_DMA)。

<a id="CONFIG_DMA_RENESAS_RZA2M_DMA"></a>

## 80.4 `CONFIG_DMA_RENESAS_RZA2M_DMA`

**提示（Prompt）**：瑞萨（Renesas）RZA2M DMA

**说明（Help）**

启用瑞萨（Renesas）RZA2M DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZA2M_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SYS_MEM_BLOCKS
```

**定义位置（Location）**：[`drivers/dma/Kconfig.renesas_rz:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.renesas_rz#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_SYS_MEM_BLOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYS_MEM_BLOCKS)。

<a id="CONFIG_DMA_RENESAS_RZ_DMAC"></a>

## 80.5 `CONFIG_DMA_RENESAS_RZ_DMAC`

**提示（Prompt）**：瑞萨（Renesas）RZ DMAC

**说明（Help）**

启用瑞萨（Renesas）RZ DMAC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_DMAC_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_DMAC
```

**定义位置（Location）**：[`drivers/dma/Kconfig.renesas_rz:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.renesas_rz#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_USE_RZ_FSP_DMAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_DMAC)。

<a id="CONFIG_DMA_RENESAS_RZ_DMAC_B"></a>

## 80.6 `CONFIG_DMA_RENESAS_RZ_DMAC_B`

**提示（Prompt）**：瑞萨（Renesas）RZ DMAC_B

**说明（Help）**

启用瑞萨（Renesas）RZ DMAC_B 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_DMAC_B_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_DMAC_B
```

**定义位置（Location）**：[`drivers/dma/Kconfig.renesas_rz:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.renesas_rz#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_USE_RZ_FSP_DMAC_B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_DMAC_B)。

<a id="CONFIG_DMA_RPI_PICO"></a>

## 80.7 `CONFIG_DMA_RPI_PICO`

**提示（Prompt）**：树莓派（Raspberry Pi）Pico DMA 驱动

**说明（Help）**

树莓派（Raspberry Pi）Pico 的 DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_DMA_ENABLED && CONFIG_RESET && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PICOSDK_USE_DMA
CONFIG_PICOSDK_USE_CLAIM
```

**定义位置（Location）**：[`drivers/dma/Kconfig.rpi_pico:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.rpi_pico#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_PICOSDK_USE_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_DMA)、[`CONFIG_PICOSDK_USE_CLAIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_CLAIM)。

<a id="CONFIG_DMA_RZA2M_DESCRS_CHUNKS"></a>

## 80.8 `CONFIG_DMA_RZA2M_DESCRS_CHUNKS`

**提示（Prompt）**：RZA2M DMA 描述符池（Descriptor Pool）的最大内存块（Chunk）数量

**说明（Help）**

此配置指定内存块（Chunk）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_RENESAS_RZA2M_DMA && CONFIG_DMA
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/dma/Kconfig.renesas_rz:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.renesas_rz#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → 瑞萨（Renesas）RZA2M DMA

**配置项引用（Symbol References）**：[`CONFIG_DMA_RENESAS_RZA2M_DMA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_RENESAS_RZA2M_DMA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_RZA2M_MAX_DESCRS"></a>

## 80.9 `CONFIG_DMA_RZA2M_MAX_DESCRS`

**提示（Prompt）**：RZA2M DMA 每通道最大描述符（Descriptor）数量

**说明（Help）**

此配置描述每个已分配内存块（Chunk）中可分配给各通道的描述符（Descriptor）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_RENESAS_RZA2M_DMA && CONFIG_DMA
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/dma/Kconfig.renesas_rz:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.renesas_rz#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → 瑞萨（Renesas）RZA2M DMA

**配置项引用（Symbol References）**：[`CONFIG_DMA_RENESAS_RZA2M_DMA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_RENESAS_RZA2M_DMA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_SAM0"></a>

## 80.10 `CONFIG_DMA_SAM0`

**提示（Prompt）**：Atmel SAM0 系列 DMAC 驱动

**说明（Help）**

Atmel SAM0 系列微控制器（MCU）的 DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM0_DMAC_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.sam0:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.sam0#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_SAM_XDMAC"></a>

## 80.11 `CONFIG_DMA_SAM_XDMAC`

**提示（Prompt）**：Atmel SAM DMA（XDMAC）驱动

**说明（Help）**

启用 Atmel SAM 微控制器（MCU）系列的直接内存访问（Direct Memory Access，XDMAC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_XDMAC_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.sam_xdmac:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.sam_xdmac#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_SEDI"></a>

## 80.12 `CONFIG_DMA_SEDI`

**提示（Prompt）**：SEDI DMA 驱动

**说明（Help）**

此选项启用 Intel SEDI DMA 驱动。这是一个适配层驱动（Shim Driver），构建于 `hal-intel` 模块中的 SEDI 裸机 DMA 驱动（Bare-Metal DMA Driver）之上。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_SEDI_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA_64BIT
```

**定义位置（Location）**：[`drivers/dma/Kconfig.sedi:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.sedi#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_DMA_64BIT`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_64BIT)。

<a id="CONFIG_DMA_SF32LB"></a>

## 80.13 `CONFIG_DMA_SF32LB`

**提示（Prompt）**：思澈（SiFli）SF32LB DMA 驱动

**说明（Help）**

启用思澈（SiFli）SF32LB 的 DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_DMAC_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.sf32lb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.sf32lb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_SI32"></a>

## 80.14 `CONFIG_DMA_SI32`

**提示（Prompt）**：Si32 DMA 控制器驱动（DMA Controller Driver）

**说明（Help）**

为 Si32 系列微控制器（MCU）启用 DMA 控制器驱动（DMA Controller Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SI32_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.si32:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.si32#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_SILABS_LDMA"></a>

## 80.15 `CONFIG_DMA_SILABS_LDMA`

**提示（Prompt）**：Silabs DMA 驱动

**说明（Help）**

Silabs DMA 的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_LDMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SYS_MEM_BLOCKS
CONFIG_SILABS_SISDK_LDMA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.silabs:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.silabs#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_SYS_MEM_BLOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYS_MEM_BLOCKS)、[`CONFIG_SILABS_SISDK_LDMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_LDMA)。

<a id="CONFIG_DMA_SILABS_SIWX91X_GPDMA"></a>

## 80.16 `CONFIG_DMA_SILABS_SIWX91X_GPDMA`

**提示（Prompt）**：Silabs SiWx91x GPDMA 驱动

**说明（Help）**

启用 Silabs SiWx91x SoC 系列的 GDMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_GPDMA_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SYS_MEM_BLOCKS
```

**定义位置（Location）**：[`drivers/dma/Kconfig.siwx91x:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.siwx91x#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_SYS_MEM_BLOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYS_MEM_BLOCKS)。

<a id="CONFIG_DMA_SILABS_SIWX91X_GPDMA_DESCR_COUNT"></a>

## 80.17 `CONFIG_DMA_SILABS_SIWX91X_GPDMA_DESCR_COUNT`

**提示（Prompt）**：GPDMA 描述符（Descriptor）的最大数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_SILABS_SIWX91X_GPDMA && CONFIG_DMA
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`drivers/dma/Kconfig.siwx91x:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.siwx91x#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Silabs SiWx91x GPDMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_SILABS_SIWX91X_GPDMA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_SILABS_SIWX91X_GPDMA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_SILABS_SIWX91X_UDMA"></a>

## 80.18 `CONFIG_DMA_SILABS_SIWX91X_UDMA`

**提示（Prompt）**：Silabs SiWx91x UDMA 驱动

**说明（Help）**

启用 Silabs SiWx91x SoC 系列的高功耗（High Power，HP）/超低功耗（Ultra Low Power，ULP）UDMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_UDMA_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SYS_MEM_BLOCKS
```

**定义位置（Location）**：[`drivers/dma/Kconfig.siwx91x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.siwx91x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_SYS_MEM_BLOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYS_MEM_BLOCKS)。

<a id="CONFIG_DMA_SILABS_SIWX91X_UDMA_DESCR_COUNT"></a>

## 80.19 `CONFIG_DMA_SILABS_SIWX91X_UDMA_DESCR_COUNT`

**提示（Prompt）**：UDMA 描述符（Descriptor）的最大数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_SILABS_SIWX91X_UDMA && CONFIG_DMA
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`drivers/dma/Kconfig.siwx91x:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.siwx91x#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Silabs SiWx91x UDMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_SILABS_SIWX91X_UDMA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_SILABS_SIWX91X_UDMA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_SMARTBOND"></a>

## 80.20 `CONFIG_DMA_SMARTBOND`

**提示（Prompt）**：Smartbond DMA 加速器驱动（DMA Accelerator Driver）

**说明（Help）**

启用 Smartbond DMA 加速器驱动（DMA Accelerator Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.smartbond:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.smartbond#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_STM32"></a>

## 80.21 `CONFIG_DMA_STM32`

**提示（Prompt）**：STM32 DMA 驱动

**说明（Help）**

用于 STM32 DMA V1、V2、V2bis 和 BDMA 类型的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_STM32_DMA_V1_ENABLED || DT_HAS_ST_STM32_DMA_V2_ENABLED || DT_HAS_ST_STM32_DMA_V2BIS_ENABLED || DT_HAS_ST_STM32_BDMA_ENABLED) && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_LL_DMA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.stm32:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.stm32#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_USE_STM32_LL_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_LL_DMA)。

<a id="CONFIG_DMA_STM32U5"></a>

## 80.22 `CONFIG_DMA_STM32U5`

**提示（Prompt）**：STM32U5 系列 DMA 驱动

**说明（Help）**

启用主要面向 STM32U5 系列的 DMA 支持。由于使用了通用 DMA（GPDMA）外设，它与原有 DMA 驱动不同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32U5_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_LL_DMA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.stm32:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.stm32#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_USE_STM32_LL_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_LL_DMA)。

<a id="CONFIG_DMA_STM32_BDMA"></a>

## 80.23 `CONFIG_DMA_STM32_BDMA`

**提示（Prompt）**：STM32 BDMA 驱动

**说明（Help）**

STM32H7 系列 SoC 的 BDMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_BDMA_ENABLED && CONFIG_DMA_STM32 && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_LL_BDMA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.stm32:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.stm32#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_STM32`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_STM32)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_USE_STM32_LL_BDMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_LL_BDMA)。

<a id="CONFIG_DMA_STM32_SHARED_IRQS"></a>

## 80.24 `CONFIG_DMA_STM32_SHARED_IRQS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在多个通道共享一个中断请求（IRQ）的设备上，启用共享 IRQ 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_STM32C0X || CONFIG_SOC_SERIES_STM32F0X || CONFIG_SOC_SERIES_STM32G0X || CONFIG_SOC_SERIES_STM32L0X || CONFIG_SOC_SERIES_STM32U0X || CONFIG_SOC_SERIES_STM32WB0X || CONFIG_SOC_SERIES_STM32WL3X) && CONFIG_DMA_STM32 && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.stm32:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.stm32#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32C0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32C0X)、[`CONFIG_SOC_SERIES_STM32F0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F0X)、[`CONFIG_SOC_SERIES_STM32G0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G0X)、[`CONFIG_SOC_SERIES_STM32L0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L0X)、[`CONFIG_SOC_SERIES_STM32U0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U0X)、[`CONFIG_SOC_SERIES_STM32WB0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WB0X)、[`CONFIG_SOC_SERIES_STM32WL3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32WL3X)、[`CONFIG_DMA_STM32`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_STM32)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32C0X`、`CONFIG_SOC_SERIES_STM32F0X`、`CONFIG_SOC_SERIES_STM32G0X`、`CONFIG_SOC_SERIES_STM32L0X`、`CONFIG_SOC_SERIES_STM32U0X`、`CONFIG_SOC_SERIES_STM32WB0X`、`CONFIG_SOC_SERIES_STM32WL3X`。

<a id="CONFIG_DMA_STM32_V1"></a>

## 80.25 `CONFIG_DMA_STM32_V1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 DMA V1 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_DMA_V1_ENABLED && CONFIG_DMA_STM32 && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.stm32:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.stm32#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_STM32`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_STM32)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_STM32_V2"></a>

## 80.26 `CONFIG_DMA_STM32_V2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 DMA V2 或 DMA V2bis 支持。对于 DMA V2，必须在 DMA 描述单元（DMA Cell）的 `dma slot` 中指定外设请求（Peripheral Request）；对于 DMA V2bis，外设请求（`slot`）不是 `dma-cell` 的参数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_STM32_DMA_V2_ENABLED || DT_HAS_ST_STM32_DMA_V2BIS_ENABLED) && CONFIG_DMA_STM32 && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.stm32:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.stm32#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_STM32`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_STM32)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_TCD_QUEUE_SIZE"></a>

## 80.27 `CONFIG_DMA_TCD_QUEUE_SIZE`

**提示（Prompt）**：分散/聚集（SG）模式下队列中的 TCD 数量

**说明（Help）**

分散/聚集（SG）模式下队列中的 TCD 数量。MCUX SAI I2S 驱动预先加载 3 个接收（RX）DMA 块，还需要额外的队列空间用于发送（TX），因此要求此队列大小大于 `3`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_DMA_MCUX_EDMA || CONFIG_DMA_MCUX_EDMA_V3 || CONFIG_DMA_MCUX_EDMA_V4) && CONFIG_DMA
```

**默认值（Defaults）**

```text
4 if CONFIG_I2S_MCUX_SAI
2
```

**定义位置（Location）**：[`drivers/dma/Kconfig.mcux_edma:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.mcux_edma#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_MCUX_EDMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_MCUX_EDMA)、[`CONFIG_DMA_MCUX_EDMA_V3`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_MCUX_EDMA_V3)、[`CONFIG_DMA_MCUX_EDMA_V4`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_MCUX_EDMA_V4)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_I2S_MCUX_SAI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2S_MCUX_SAI)。

<a id="CONFIG_DMA_TI_CC23X0"></a>

## 80.28 `CONFIG_DMA_TI_CC23X0`

**提示（Prompt）**：TI CC23X0 DMA 驱动

**说明（Help）**

TI CC23X0 微控制器（MCU）的 DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC23X0_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.ti_cc23x0:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.ti_cc23x0#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_TI_MSPM0"></a>

## 80.29 `CONFIG_DMA_TI_MSPM0`

**提示（Prompt）**：德州仪器（Texas Instruments）MSPM0 DMA 控制器驱动（DMA Controller Driver）

**说明（Help）**

启用德州仪器（Texas Instruments）MSPM0 系列 DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_MSPM0_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_MSPM0_DL_DMA
```

**定义位置（Location）**：[`drivers/dma/Kconfig.ti_mspm0:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.ti_mspm0#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_USE_MSPM0_DL_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_MSPM0_DL_DMA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_USE_MSPM0_DL_DMA`。

<a id="CONFIG_DMA_WCH"></a>

## 80.30 `CONFIG_DMA_WCH`

**提示（Prompt）**：CH32V DMA 驱动

**说明（Help）**

沁恒（WCH）CH32V SoC 系列的 DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_WCH_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.wch:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.wch#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_XILINX_ADMA"></a>

## 80.31 `CONFIG_DMA_XILINX_ADMA`

**提示（Prompt）**：使用 Xilinx ADMA 驱动

**说明（Help）**

Xilinx ADMA 的 DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_XLNX_ZYNQMP_DMA_1_0_ENABLED || DT_HAS_AMD_VERSAL2_DMA_1_0_ENABLED) && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CACHE_MANAGEMENT
CONFIG_SYS_MEM_BLOCKS
```

**定义位置（Location）**：[`drivers/dma/Kconfig.xilinx_adma:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.xilinx_adma#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_SYS_MEM_BLOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYS_MEM_BLOCKS)。

<a id="CONFIG_DMA_XILINX_ADMA_DESC_POOL_ALIGNMENT"></a>

## 80.32 `CONFIG_DMA_XILINX_ADMA_DESC_POOL_ALIGNMENT`

**提示（Prompt）**：DMA 描述符池对齐（Descriptor Pool Alignment），以字节为单位

**说明（Help）**

分配 DMA 描述符池（Descriptor Pool）时的内存对齐（Memory Alignment）要求。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_XILINX_ADMA && CONFIG_DMA
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`drivers/dma/Kconfig.xilinx_adma:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.xilinx_adma#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → 使用 Xilinx ADMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_XILINX_ADMA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_XILINX_ADMA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_XILINX_ADMA_SG_BUFFER_COUNT"></a>

## 80.33 `CONFIG_DMA_XILINX_ADMA_SG_BUFFER_COUNT`

**提示（Prompt）**：每个通道的最大分散/聚集描述符（Scatter-Gather Descriptor）数量

**说明（Help）**

描述符内存池（Descriptor Memory Pool）中为每个 DMA 通道分配的分散/聚集描述符槽位（Scatter-Gather Descriptor Slot）数量。每个条目保存单个 SG 块所需的一对源硬件描述符和目标硬件描述符（Source and Destination Hardware Descriptor）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_XILINX_ADMA && CONFIG_DMA
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`drivers/dma/Kconfig.xilinx_adma:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.xilinx_adma#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → 使用 Xilinx ADMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_XILINX_ADMA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_XILINX_ADMA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_XILINX_AXI_DMA"></a>

## 80.34 `CONFIG_DMA_XILINX_AXI_DMA`

**提示（Prompt）**：Xilinx AXI DMA LogiCORE IP 驱动

**说明（Help）**

Xilinx AXI DMA 的驱动，此类 DMA 通常位于 FPGA 上。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_XLNX_AXI_DMA_1_00_A_ENABLED || DT_HAS_XLNX_ETH_DMA_ENABLED) && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.xilinx_axi_dma:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.xilinx_axi_dma#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_XILINX_AXI_DMA_DISABLE_CACHE_WHEN_ACCESSING_SG_DESCRIPTORS"></a>

## 80.35 `CONFIG_DMA_XILINX_AXI_DMA_DISABLE_CACHE_WHEN_ACCESSING_SG_DESCRIPTORS`

**提示（Prompt）**：改用 `DMA_XILINX_AXI_DMA_MANUAL_CACHE_COHERENCY`【已弃用（Deprecated）】

**说明（Help）**

已弃用（Deprecated）。此选项已重命名为 `DMA_XILINX_AXI_DMA_MANUAL_CACHE_COHERENCY`，因为它控制描述符和缓冲区两者的缓存维护（Cache Maintenance），并非只控制分散/聚集描述符。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_XILINX_AXI_DMA && CONFIG_CACHE_MANAGEMENT && CONFIG_DCACHE && CONFIG_DMA
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
CONFIG_DMA_XILINX_AXI_DMA_MANUAL_CACHE_COHERENCY
```

**定义位置（Location）**：[`drivers/dma/Kconfig.xilinx_axi_dma:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.xilinx_axi_dma#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Xilinx AXI DMA LogiCORE IP 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_XILINX_AXI_DMA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_XILINX_AXI_DMA)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)、[`CONFIG_DMA_XILINX_AXI_DMA_MANUAL_CACHE_COHERENCY`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_XILINX_AXI_DMA_MANUAL_CACHE_COHERENCY)。

<a id="CONFIG_DMA_XILINX_AXI_DMA_INTERRUPT_THRESHOLD"></a>

## 80.36 `CONFIG_DMA_XILINX_AXI_DMA_INTERRUPT_THRESHOLD`

**提示（Prompt）**：触发中断前需完成的事务数量（Completed Transaction Count）

**说明（Help）**

触发中断（Interrupt）之前需要完成的事务（Transaction）数量。减小此值可降低延迟；增大此值可减少中断引入的开销。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_XILINX_AXI_DMA && CONFIG_DMA
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`drivers/dma/Kconfig.xilinx_axi_dma:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.xilinx_axi_dma#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Xilinx AXI DMA LogiCORE IP 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_XILINX_AXI_DMA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_XILINX_AXI_DMA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_XILINX_AXI_DMA_INTERRUPT_TIMEOUT"></a>

## 80.37 `CONFIG_DMA_XILINX_AXI_DMA_INTERRUPT_TIMEOUT`

**提示（Prompt）**：触发中断的超时时间（Interrupt Timeout）

**说明（Help）**

最迟在 `CONFIG_DMA_XILINX_AXI_DMA_INTERRUPT_TIMEOUT * 125 * DMA_CLOCK_PERIOD` 个周期之后触发中断（Interrupt）。此设置可与 `DMA_XILINX_AXI_DMA_INTERRUPT_THRESHOLD` 配合使用：DMA 能在达到阈值（Threshold）之前发出中断，从而在每秒仅完成少量事务的场景下降低延迟。设为 `0` 可禁用此功能，即仅在达到阈值时发出中断。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_XILINX_AXI_DMA && CONFIG_DMA
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/dma/Kconfig.xilinx_axi_dma:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.xilinx_axi_dma#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Xilinx AXI DMA LogiCORE IP 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_XILINX_AXI_DMA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_XILINX_AXI_DMA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_XILINX_AXI_DMA_LOCK_ALL_IRQS"></a>

## 80.38 `CONFIG_DMA_XILINX_AXI_DMA_LOCK_ALL_IRQS`

**提示（Prompt）**：锁定全部中断请求（Lock All IRQs）

**说明（Help）**

在 `dma_start` 期间修改通道数据时，锁定全部中断（Interrupt），例如定时器和调度器中断。在发送/接收（TX/RX）回调之外调用 `dma_start` 时，必须这样做。此选项最安全，也是默认值；如果不确定应选哪项，请选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/dma/Kconfig.xilinx_axi_dma:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.xilinx_axi_dma#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Xilinx AXI DMA LogiCORE IP 驱动 → 在 `dma_start` 期间操作各通道的数据结构（Per-Channel Data Structure）时，需要锁定的中断请求（IRQ）。

<a id="CONFIG_DMA_XILINX_AXI_DMA_LOCK_CHANNEL_IRQ"></a>

## 80.39 `CONFIG_DMA_XILINX_AXI_DMA_LOCK_CHANNEL_IRQ`

**提示（Prompt）**：锁定 DMA 通道的中断请求（IRQ）

**说明（Help）**

仅锁定 `dma_start` 期间要修改数据的那个 DMA 通道的中断（Interrupt）。只有在能够保证 `dma_start` 仅从为同一通道注册的回调（Callback）中调用时，才选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/dma/Kconfig.xilinx_axi_dma:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.xilinx_axi_dma#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Xilinx AXI DMA LogiCORE IP 驱动 → 在 `dma_start` 期间操作各通道的数据结构（Per-Channel Data Structure）时，需要锁定的中断请求（IRQ）。

<a id="CONFIG_DMA_XILINX_AXI_DMA_LOCK_DMA_IRQS"></a>

## 80.40 `CONFIG_DMA_XILINX_AXI_DMA_LOCK_DMA_IRQS`

**提示（Prompt）**：锁定发送和接收中断请求（TX and RX IRQs）

**说明（Help）**

在 `dma_start` 期间修改通道数据时，锁定此 DMA 设备的全部中断（Interrupt）。只有当 `dma_start` 仅从发送/接收（TX/RX）回调中调用时，这样做才安全；允许另外在 DMA 初始化刚完成后直接调用一次。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/dma/Kconfig.xilinx_axi_dma:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.xilinx_axi_dma#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Xilinx AXI DMA LogiCORE IP 驱动 → 在 `dma_start` 期间操作各通道的数据结构（Per-Channel Data Structure）时，需要锁定的中断请求（IRQ）。

<a id="CONFIG_DMA_XILINX_AXI_DMA_MANUAL_CACHE_COHERENCY"></a>

## 80.41 `CONFIG_DMA_XILINX_AXI_DMA_MANUAL_CACHE_COHERENCY`

**提示（Prompt）**：手动刷新或失效 DMA 描述符和缓冲区对应的数据缓存（Flush/Invalidate Data Cache）

**说明（Help）**

控制访问 DMA 描述符（Descriptor）或缓冲区时，是否显式刷新（Flush）或失效（Invalidate）数据缓存（Data Cache）。这使 DMA 可用于不为 DMA 访问提供一致性（Coherency）的架构。如果不确定是否需要此功能，应在此选择 `n`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_XILINX_AXI_DMA && CONFIG_CACHE_MANAGEMENT && CONFIG_DCACHE && CONFIG_DMA
```

**被选择（Selected by）**

```text
CONFIG_DMA_XILINX_AXI_DMA_DISABLE_CACHE_WHEN_ACCESSING_SG_DESCRIPTORS
```

**定义位置（Location）**：[`drivers/dma/Kconfig.xilinx_axi_dma:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.xilinx_axi_dma#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Xilinx AXI DMA LogiCORE IP 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_XILINX_AXI_DMA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_XILINX_AXI_DMA)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_DMA_XILINX_AXI_DMA_DISABLE_CACHE_WHEN_ACCESSING_SG_DESCRIPTORS`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_XILINX_AXI_DMA_DISABLE_CACHE_WHEN_ACCESSING_SG_DESCRIPTORS)。

<a id="CONFIG_DMA_XILINX_AXI_DMA_SG_DESCRIPTOR_NUM_RX"></a>

## 80.42 `CONFIG_DMA_XILINX_AXI_DMA_SG_DESCRIPTOR_NUM_RX`

**提示（Prompt）**：为接收（RX）分配的传输描述符（Transfer Descriptor）数量。

**说明（Help）**

AXI DMA 驱动目前为每次接收（RX）传输分配一个 DMA 描述符（Descriptor），因为传输需要由上层驱动（Upstream Driver）启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_XILINX_AXI_DMA && CONFIG_DMA
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/dma/Kconfig.xilinx_axi_dma:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.xilinx_axi_dma#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Xilinx AXI DMA LogiCORE IP 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_XILINX_AXI_DMA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_XILINX_AXI_DMA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_XILINX_AXI_DMA_SG_DESCRIPTOR_NUM_TX"></a>

## 80.43 `CONFIG_DMA_XILINX_AXI_DMA_SG_DESCRIPTOR_NUM_TX`

**提示（Prompt）**：为发送（TX）分配的传输描述符（Transfer Descriptor）数量。

**说明（Help）**

Xilinx AXI DMA 使用位于内存中的 DMA 描述符环（Descriptor Ring）；这些描述符引用包含网络数据包以及控制和状态信息的缓冲区。增加描述符数量可以增加在途数据包（Packets in Flight）数量，有利于性能，但同时会增加内存用量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_XILINX_AXI_DMA && CONFIG_DMA
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/dma/Kconfig.xilinx_axi_dma:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.xilinx_axi_dma#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Xilinx AXI DMA LogiCORE IP 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_XILINX_AXI_DMA`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_XILINX_AXI_DMA)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_XMC4XXX"></a>

## 80.44 `CONFIG_DMA_XMC4XXX`

**提示（Prompt）**：Infineon XMC4xxx 系列 DMA 驱动

**说明（Help）**

英飞凌（Infineon）XMC4xxx 系列微控制器（MCU）的 DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_XMC4XXX_DMA_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.xmc4xxx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.xmc4xxx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_DMA_XMC4XXX_NUM_DESCRIPTORS"></a>

## 80.45 `CONFIG_DMA_XMC4XXX_NUM_DESCRIPTORS`

**提示（Prompt）**：链表（Linked List）中的最大 DMA 描述符（Descriptor）数量

**说明（Help）**

DMA 块传输配置（Block Transfer Configuration）中的最大块数。仅 `dma0` 的通道 `0` 和 `1` 支持此功能。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_XMC4XXX && CONFIG_DMA
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/dma/Kconfig.xmc4xxx:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.xmc4xxx#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → Infineon XMC4xxx 系列 DMA 驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_XMC4XXX`](P080_drivers_dma_配置项参考_2.md#CONFIG_DMA_XMC4XXX)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_INFINEON_DESCRIPTOR_POOL_SIZE"></a>

## 80.46 `CONFIG_INFINEON_DESCRIPTOR_POOL_SIZE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项指定 DMA PDL 驱动使用的描述符池大小（Descriptor Pool Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DMA_INFINEON_CAT1_PDL && CONFIG_DMA
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/dma/Kconfig.infineon:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.infineon#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA_INFINEON_CAT1_PDL`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INFINEON_CAT1_PDL)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_INFINEON_DMA_MAX_XFERS"></a>

## 80.47 `CONFIG_INFINEON_DMA_MAX_XFERS`

**提示（Prompt）**：最大传输块数（Maximum Blocks to Transfer）

**说明（Help）**

此选项指定为 DMAC 分配的最大块（Block）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_DMAC_ENABLED && CONFIG_DMA
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/dma/Kconfig.infineon:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.infineon#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_MCUX_PXP"></a>

## 80.48 `CONFIG_MCUX_PXP`

**提示（Prompt）**：MCUX PXP DMA 驱动

**说明（Help）**

NXP SoC 的 PXP DMA 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PXP_ENABLED && CONFIG_DISPLAY && CONFIG_DMA
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/dma/Kconfig.mcux_pxp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/dma/Kconfig.mcux_pxp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<!-- kconfig-navigation -->

[上一章](P079_drivers_dma_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P081_drivers_dp_配置项参考.md)
