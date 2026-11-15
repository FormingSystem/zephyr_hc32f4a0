---
id: learning.zephyr-docs.kconfig-reference.page-129
title: "`drivers/mspi`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第129章\_`drivers/mspi`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/mspi` 的 34 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_HEAP_MEM_POOL_ADD_SIZE_MSPI_STM32_XSPI"></a>

## 129.1 `CONFIG_HEAP_MEM_POOL_ADD_SIZE_MSPI_STM32_XSPI`

**提示（Prompt）**：STM32 XSPI 控制器堆内存池大小（Heap Memory Pool Size）

**说明（Help）**

XSPI 驱动为每个 DMA 数据包从系统堆分配与包长相同的中转缓冲区（Bounce Buffer），并将数据接收到其中，因此堆必须能够容纳应用发起的最大读取。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI_STM32_XSPI && CONFIG_MSPI_DMA && CONFIG_MSPI_STM32_CONTROLLER && CONFIG_MSPI
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.stm32:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.stm32#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → STM32 MSPI 控制器驱动【实验性（EXPERIMENTAL）】 → STM32 XSPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI_STM32_XSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_XSPI)、[`CONFIG_MSPI_DMA`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_DMA)、[`CONFIG_MSPI_STM32_CONTROLLER`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_CONTROLLER)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)。

<a id="CONFIG_MSPI"></a>

## 129.2 `CONFIG_MSPI`

**提示（Prompt）**：多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动

**说明（Help）**

启用 MSPI 硬件总线支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_FLASH_MSPI
CONFIG_MEMC_MSPI
```

**定义位置（Location）**：[`drivers/mspi/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MSPI`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MSPI)、[`CONFIG_MEMC_MSPI`](P119_drivers_memc_配置项参考.md#CONFIG_MEMC_MSPI)。

<a id="CONFIG_MSPI_AMBIQ_AP3"></a>

## 129.3 `CONFIG_MSPI_AMBIQ_AP3`

**提示（Prompt）**：Ambiq Apollo3 系列 MSPI 控制器驱动

**说明（Help）**

启用 Ambiq MSPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_APOLLO3X && CONFIG_MSPI_AMBIQ_CONTROLLER && CONFIG_MSPI
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_MSPI_MEMMAP
CONFIG_MSPI_SCRAMBLE
CONFIG_MSPI_TIMING if CONFIG_SOC_APOLLO3P_BLUE
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.ambiq:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.ambiq#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → Ambiq MSPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_APOLLO3X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO3X)、[`CONFIG_MSPI_AMBIQ_CONTROLLER`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_AMBIQ_CONTROLLER)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_MSPI_MEMMAP`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_MEMMAP)、[`CONFIG_MSPI_SCRAMBLE`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_SCRAMBLE)、[`CONFIG_MSPI_TIMING`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_TIMING)、[`CONFIG_SOC_APOLLO3P_BLUE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_APOLLO3P_BLUE)。

<a id="CONFIG_MSPI_AMBIQ_AP5"></a>

## 129.4 `CONFIG_MSPI_AMBIQ_AP5`

**提示（Prompt）**：Ambiq Apollo5 系列 MSPI 控制器驱动

**说明（Help）**

启用 Ambiq MSPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_APOLLO5X && CONFIG_MSPI_AMBIQ_CONTROLLER && CONFIG_MSPI
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_MSPI_MEMMAP
CONFIG_MSPI_SCRAMBLE
CONFIG_MSPI_TIMING
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.ambiq:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.ambiq#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → Ambiq MSPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_APOLLO5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_APOLLO5X)、[`CONFIG_MSPI_AMBIQ_CONTROLLER`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_AMBIQ_CONTROLLER)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_MSPI_MEMMAP`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_MEMMAP)、[`CONFIG_MSPI_SCRAMBLE`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_SCRAMBLE)、[`CONFIG_MSPI_TIMING`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_TIMING)。

<a id="CONFIG_MSPI_AMBIQ_BUFF_ALIGNMENT"></a>

## 129.5 `CONFIG_MSPI_AMBIQ_BUFF_ALIGNMENT`

**提示（Prompt）**：MSPI 缓冲区字节对齐（Byte Alignment）

**说明（Help）**

此选项指定 MSPI 缓冲区对齐要求。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI_AMBIQ_CONTROLLER && CONFIG_MSPI
```

**默认值（Defaults）**

```text
8 if CONFIG_MSPI_AMBIQ_AP3
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.ambiq:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.ambiq#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → Ambiq MSPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI_AMBIQ_CONTROLLER`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_AMBIQ_CONTROLLER)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_MSPI_AMBIQ_AP3`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_AMBIQ_AP3)。

<a id="CONFIG_MSPI_AMBIQ_BUFF_RAM_LOCATION"></a>

## 129.6 `CONFIG_MSPI_AMBIQ_BUFF_RAM_LOCATION`

**提示（Prompt）**：相对于 `SRAM_BASE_ADDRESS` 的字节偏移（Byte Offset）

**说明（Help）**

此选项指定 MSPI 缓冲区／堆的起始地址。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI_AMBIQ_CONTROLLER && CONFIG_MSPI
```

**默认值（Defaults）**

```text
0x40000 if CONFIG_SOC_APOLLO3_BLUE
0x50000
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.ambiq:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.ambiq#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → Ambiq MSPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI_AMBIQ_CONTROLLER`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_AMBIQ_CONTROLLER)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_SOC_APOLLO3_BLUE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_APOLLO3_BLUE)。

<a id="CONFIG_MSPI_AMBIQ_CONTROLLER"></a>

## 129.7 `CONFIG_MSPI_AMBIQ_CONTROLLER`

**提示（Prompt）**：Ambiq MSPI 控制器驱动

**说明（Help）**

已启用 Ambiq MSPI 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_MSPI_CONTROLLER_ENABLED && CONFIG_MSPI
```

**主动选择（Selects）**

```text
CONFIG_AMBIQ_HAL
CONFIG_AMBIQ_HAL_USE_MSPI
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.ambiq:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.ambiq#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_HAL_USE_MSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_MSPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_MSPI_AMBIQ_TIMING_SCAN"></a>

## 129.8 `CONFIG_MSPI_AMBIQ_TIMING_SCAN`

**提示（Prompt）**：开启 Ambiq 时序扫描工具（Timing Scan Utility）

**说明（Help）**

启用时序扫描会在初始化期间消耗时间和空间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI_TIMING && CONFIG_MSPI_AMBIQ_CONTROLLER && CONFIG_MSPI
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.ambiq:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.ambiq#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → Ambiq MSPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI_TIMING`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_TIMING)、[`CONFIG_MSPI_AMBIQ_CONTROLLER`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_AMBIQ_CONTROLLER)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)。

<a id="CONFIG_MSPI_AMBIQ_TIMING_SCAN_BUFFER_SIZE"></a>

## 129.9 `CONFIG_MSPI_AMBIQ_TIMING_SCAN_BUFFER_SIZE`

**提示（Prompt）**：时序扫描缓冲区大小，单位为字节

**说明（Help）**

此选项指定时序扫描所用内存缓冲区大小。应在几 KB 至数百 KB 之间谨慎调整，以平衡耗时与精度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI_AMBIQ_TIMING_SCAN && CONFIG_MSPI_AMBIQ_CONTROLLER && CONFIG_MSPI
```

**默认值（Defaults）**

```text
131072
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.ambiq:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.ambiq#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → Ambiq MSPI 控制器驱动 → 开启 Ambiq 时序扫描工具（Timing Scan Utility）

**配置项引用（Symbol References）**：[`CONFIG_MSPI_AMBIQ_TIMING_SCAN`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_AMBIQ_TIMING_SCAN)、[`CONFIG_MSPI_AMBIQ_CONTROLLER`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_AMBIQ_CONTROLLER)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)。

<a id="CONFIG_MSPI_AMBIQ_TIMING_SCAN_DATA_SIZE"></a>

## 129.10 `CONFIG_MSPI_AMBIQ_TIMING_SCAN_DATA_SIZE`

**提示（Prompt）**：时序扫描使用的总数据量，单位为字节

**说明（Help）**

此选项指定时序扫描使用的总数据量，必须能被 `MSPI_AMBIQ_TIMING_SCAN_BUFFER_SIZE` 整除。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI_AMBIQ_TIMING_SCAN && CONFIG_MSPI_AMBIQ_CONTROLLER && CONFIG_MSPI
```

**默认值（Defaults）**

```text
131072
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.ambiq:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.ambiq#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → Ambiq MSPI 控制器驱动 → 开启 Ambiq 时序扫描工具（Timing Scan Utility）

**配置项引用（Symbol References）**：[`CONFIG_MSPI_AMBIQ_TIMING_SCAN`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_AMBIQ_TIMING_SCAN)、[`CONFIG_MSPI_AMBIQ_CONTROLLER`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_AMBIQ_CONTROLLER)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)。

<a id="CONFIG_MSPI_ASYNC"></a>

## 129.11 `CONFIG_MSPI_ASYNC`

**提示（Prompt）**：异步调用支持（Asynchronous Call Support）

**说明（Help）**

启用异步 API 调用（Asynchronous API Calls）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI
```

**主动选择（Selects）**

```text
CONFIG_POLL
```

**定义位置（Location）**：[`drivers/mspi/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_POLL`](P002_kernel_配置项参考_2.md#CONFIG_POLL)。

<a id="CONFIG_MSPI_CDNS"></a>

## 129.12 `CONFIG_MSPI_CDNS`

**提示（Prompt）**：Cadence MSPI 驱动

**说明（Help）**

启用 Cadence MSPI 外设驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CDNS_XSPI_NOR_ENABLED && CONFIG_MSPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_PINCTRL
```

**弱选择（Implies）**

```text
CONFIG_MSPI_TIMING
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.cadence:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.cadence#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_MSPI_TIMING`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_TIMING)。

<a id="CONFIG_MSPI_COMPLETION_TIMEOUT_TOLERANCE"></a>

## 129.13 `CONFIG_MSPI_COMPLETION_TIMEOUT_TOLERANCE`

**提示（Prompt）**：完成超时容差（Completion Timeout Tolerance，毫秒）

**说明（Help）**

MSPI 完成超时逻辑的容差值，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI
```

**默认值（Defaults）**

```text
200
```

**定义位置（Location）**：[`drivers/mspi/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)。

<a id="CONFIG_MSPI_DMA"></a>

## 129.14 `CONFIG_MSPI_DMA`

**提示（Prompt）**：直接内存访问支持（DMA Support）

**说明（Help）**

启用 DMA 能力，具体取决于驱动及运行硬件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/mspi/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_MSPI_DW"></a>

## 129.15 `CONFIG_MSPI_DW`

**提示（Prompt）**：DesignWare 同步串行接口（SSI）控制器驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SNPS_DESIGNWARE_SSI_ENABLED && CONFIG_MSPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL if n
```

**弱选择（Implies）**

```text
CONFIG_MSPI_TIMING
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.dw:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.dw#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_MSPI_TIMING`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_TIMING)。

<a id="CONFIG_MSPI_DW_DDR"></a>

## 129.16 `CONFIG_MSPI_DW_DDR`

**提示（Prompt）**：双倍数据速率（Dual Data-Rate，DDR）能力

**说明（Help）**

部分设备支持双倍数据速率，需要在 IP 中启用特定寄存器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI_DW && CONFIG_MSPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.dw:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.dw#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → DesignWare 同步串行接口（SSI）控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI_DW`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_DW)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)。

<a id="CONFIG_MSPI_DW_HANDLE_FIFOS_IN_SYSTEM_WORKQUEUE"></a>

## 129.17 `CONFIG_MSPI_DW_HANDLE_FIFOS_IN_SYSTEM_WORKQUEUE`

**提示（Prompt）**：在系统工作队列（System Workqueue）中处理 FIFO

**说明（Help）**

驱动不使用 DMA 向 SSI FIFO 传输数据或从中读取数据时，FIFO 处理可能耗费较长时间。如果这些时间都花在中断上下文中，可能严重影响部分应用。此选项允许将工作交给系统工作队列处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING && CONFIG_MSPI_DW && CONFIG_MSPI
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.dw:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.dw#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → DesignWare 同步串行接口（SSI）控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_MSPI_DW`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_DW)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)。

<a id="CONFIG_MSPI_DW_TXD_DIV"></a>

## 129.18 `CONFIG_MSPI_DW_TXD_DIV`

**提示（Prompt）**：DesignWare SSI 发送驱动边沿除数（TX Drive Edge Divisor）

**说明（Help）**

DDR 模式下，将计算出的 `BAUDR` 值写入 `TXD_DRIVE_EDGE` 寄存器时应用的除法因子。注意，此寄存器最大值为 `(BAUDR / 2) - 1`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI_DW_DDR && CONFIG_MSPI_DW && CONFIG_MSPI
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.dw:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.dw#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → DesignWare 同步串行接口（SSI）控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI_DW_DDR`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_DW_DDR)、[`CONFIG_MSPI_DW`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_DW)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)。

<a id="CONFIG_MSPI_DW_TXD_MUL"></a>

## 129.19 `CONFIG_MSPI_DW_TXD_MUL`

**提示（Prompt）**：DesignWare SSI 发送驱动边沿乘数（TX Drive Edge Multiplier）

**说明（Help）**

DDR 模式下，将计算出的 `BAUDR` 值写入 `TXD_DRIVE_EDGE` 寄存器时应用的乘法因子。注意，此寄存器最大值为 `(BAUDR / 2) - 1`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI_DW_DDR && CONFIG_MSPI_DW && CONFIG_MSPI
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.dw:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.dw#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → DesignWare 同步串行接口（SSI）控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI_DW_DDR`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_DW_DDR)、[`CONFIG_MSPI_DW`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_DW)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)。

<a id="CONFIG_MSPI_EMUL"></a>

## 129.20 `CONFIG_MSPI_EMUL`

**提示（Prompt）**：MSPI 仿真器（Emulator）

**说明（Help）**

启用 MSPI 仿真器驱动。这是一个不与真实硬件通信的模拟驱动，而是与仿真驱动通信，后者扮演仿真 MSPI 总线上的设备。它用于测试 MSPI 设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_MSPI_EMUL_CONTROLLER_ENABLED && CONFIG_EMUL && CONFIG_MSPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MSPI_MEMMAP
CONFIG_MSPI_SCRAMBLE
CONFIG_MSPI_TIMING
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.mspi_emul:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.mspi_emul#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_MSPI_MEMMAP`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_MEMMAP)、[`CONFIG_MSPI_SCRAMBLE`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_SCRAMBLE)、[`CONFIG_MSPI_TIMING`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_TIMING)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_MSPI_INIT_PRIORITY"></a>

## 129.21 `CONFIG_MSPI_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI
```

**默认值（Defaults）**

```text
70
```

**定义位置（Location）**：[`drivers/mspi/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)。

<a id="CONFIG_MSPI_MCHP_XEC_QMSPI"></a>

## 129.22 `CONFIG_MSPI_MCHP_XEC_QMSPI`

**提示（Prompt）**：Microchip XEC QMSPI MSPI 控制器驱动

**说明（Help）**

启用 Microchip MEC174x/MEC175x/MEC165xB QMSPI 控制器的 MSPI 驱动。支持通过描述符（Descriptor）和 8 字节收发 FIFO 进行程序控制 I/O（PIO）传输。使用 `soc/microchip/mec/common/reg/mec_qmspi.h` 中的寄存器定义。引脚分配因开发板而异；应在开发板 DTS 中添加 QMSPI 引脚控制（Pinctrl）节点，并在 `qspi0` 节点上通过 `pinctrl-0` 引用它们。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_QMSPI_CONTROLLER_ENABLED && CONFIG_MSPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_PINCTRL_KEEP_SLEEP_STATE
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.mchp_xec:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.mchp_xec#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_PINCTRL_KEEP_SLEEP_STATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL_KEEP_SLEEP_STATE)。

<a id="CONFIG_MSPI_MCHP_XEC_QMSPI_LDMA"></a>

## 129.23 `CONFIG_MSPI_MCHP_XEC_QMSPI_LDMA`

**提示（Prompt）**：QMSPI 本地 DMA 数据路径（Local-DMA Data Path）

**说明（Help）**

当 MSPI 请求指定 `xfer_mode=MSPI_DMA` 时，在命令、地址和数据阶段使用 QMSPI 控制器的三个发送与三个接收本地 DMA 通道。各通道的长度覆盖（Length-override）决定字节数，绕过描述符中 15 位 `NQUNITS` 的限制。禁用后，拒绝 `MSPI_DMA` 请求，并且只构建 PIO（FIFO）路径。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI_DMA && CONFIG_MSPI_MCHP_XEC_QMSPI && CONFIG_MSPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.mchp_xec:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.mchp_xec#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → Microchip XEC QMSPI MSPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI_DMA`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_DMA)、[`CONFIG_MSPI_MCHP_XEC_QMSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_MCHP_XEC_QMSPI)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)。

<a id="CONFIG_MSPI_MEMMAP"></a>

## 129.24 `CONFIG_MSPI_MEMMAP`

**提示（Prompt）**：内存映射设备访问（Memory-mapped Device Access）

**说明（Help）**

描述控制器硬件的内存映射能力，并启用设备驱动中的 `mspi_memmap_config` 调用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI
```

**被选择（Selected by）**

```text
CONFIG_MSPI_EMUL
```

**被弱选择（Implied by）**

```text
CONFIG_MSPI_AMBIQ_AP3
CONFIG_MSPI_AMBIQ_AP5
```

**定义位置（Location）**：[`drivers/mspi/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_MSPI_EMUL`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_EMUL)、[`CONFIG_MSPI_AMBIQ_AP3`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_AMBIQ_AP3)、[`CONFIG_MSPI_AMBIQ_AP5`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_AMBIQ_AP5)。

<a id="CONFIG_MSPI_NXP_QSPI"></a>

## 129.25 `CONFIG_MSPI_NXP_QSPI`

**提示（Prompt）**：NXP QSPI 控制器驱动

**说明（Help）**

启用 NXP QSPI 控制器的 MSPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_QSPI_ENABLED && CONFIG_MSPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.nxp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.nxp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_MSPI_NXP_QSPI_BUSY_TIMEOUT_US"></a>

## 129.26 `CONFIG_MSPI_NXP_QSPI_BUSY_TIMEOUT_US`

**提示（Prompt）**：NXP QSPI 忙等待超时（Busy-wait Timeout），单位为微秒

**说明（Help）**

等待 QSPI 控制器完成 IP 命令或发送 FIFO 排空的最长时间，单位为微秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI_NXP_QSPI && CONFIG_MSPI
```

**默认值（Defaults）**

```text
1000000
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.nxp:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.nxp#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → NXP QSPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI_NXP_QSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_NXP_QSPI)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)。

<a id="CONFIG_MSPI_PERIPHERAL"></a>

## 129.27 `CONFIG_MSPI_PERIPHERAL`

**提示（Prompt）**：外设模式（Peripheral Mode）支持

**说明（Help）**

启用驱动的 MSPI 外设模式操作。外设模式支持取决于驱动及其运行硬件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI
```

**定义位置（Location）**：[`drivers/mspi/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)。

<a id="CONFIG_MSPI_SCRAMBLE"></a>

## 129.28 `CONFIG_MSPI_SCRAMBLE`

**提示（Prompt）**：扰码（Scrambling）支持

**说明（Help）**

描述控制器硬件的扰码能力，并启用设备驱动中的 `mspi_scramble_config` 调用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI
```

**被选择（Selected by）**

```text
CONFIG_MSPI_EMUL
```

**被弱选择（Implied by）**

```text
CONFIG_MSPI_AMBIQ_AP3
CONFIG_MSPI_AMBIQ_AP5
```

**定义位置（Location）**：[`drivers/mspi/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_MSPI_EMUL`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_EMUL)、[`CONFIG_MSPI_AMBIQ_AP3`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_AMBIQ_AP3)、[`CONFIG_MSPI_AMBIQ_AP5`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_AMBIQ_AP5)。

<a id="CONFIG_MSPI_STM32_BUFFER_ALIGNMENT"></a>

## 129.29 `CONFIG_MSPI_STM32_BUFFER_ALIGNMENT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

某些 MSPI 主机控制器要求数据缓冲区对齐，DMA 才能正确工作。此值表示所需的缓冲区对齐字节数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI_STM32_CONTROLLER && CONFIG_MSPI
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.stm32:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.stm32#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → STM32 MSPI 控制器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MSPI_STM32_CONTROLLER`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_CONTROLLER)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)。

<a id="CONFIG_MSPI_STM32_CONTROLLER"></a>

## 129.30 `CONFIG_MSPI_STM32_CONTROLLER`

**提示（Prompt）**：STM32 MSPI 控制器驱动【实验性（EXPERIMENTAL）】

**说明（Help）**

当设备树中至少存在一个 OSPI、QSPI 或 XSPI 控制器时，此顶层选项启用所有 STM32 MSPI 控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_STM32_OSPI_CONTROLLER_ENABLED || DT_HAS_ST_STM32_QSPI_CONTROLLER_ENABLED || DT_HAS_ST_STM32_XSPI_CONTROLLER_ENABLED) && CONFIG_MSPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.stm32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.stm32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_MSPI_STM32_OSPI"></a>

## 129.31 `CONFIG_MSPI_STM32_OSPI`

**提示（Prompt）**：STM32 OSPI 控制器驱动

**说明（Help）**

启用 STM32 系列处理器的 OSPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_OSPI_CONTROLLER_ENABLED && CONFIG_MSPI_STM32_CONTROLLER && CONFIG_MSPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO if n
CONFIG_USE_STM32_HAL_OSPI if !CONFIG_SOC_SERIES_STM32H5X
CONFIG_USE_STM32_LL_DLYB if CONFIG_SOC_SERIES_STM32H5X || CONFIG_SOC_SERIES_STM32U5X
CONFIG_USE_STM32_HAL_MDMA if CONFIG_SOC_SERIES_STM32H7X
CONFIG_USE_STM32_HAL_DMA
CONFIG_USE_STM32_HAL_DMA_EX
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.stm32:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.stm32#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → STM32 MSPI 控制器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MSPI_STM32_CONTROLLER`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_CONTROLLER)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_USE_STM32_HAL_OSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_OSPI)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_USE_STM32_LL_DLYB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_LL_DLYB)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_USE_STM32_HAL_MDMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_MDMA)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_USE_STM32_HAL_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA)、[`CONFIG_USE_STM32_HAL_DMA_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA_EX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32U5X`、`CONFIG_SOC_SERIES_STM32H7X`。

<a id="CONFIG_MSPI_STM32_QSPI"></a>

## 129.32 `CONFIG_MSPI_STM32_QSPI`

**提示（Prompt）**：STM32 QSPI 控制器驱动

**说明（Help）**

启用 STM32 系列处理器的 QSPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_QSPI_CONTROLLER_ENABLED && CONFIG_MSPI_STM32_CONTROLLER && CONFIG_MSPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO if n
CONFIG_USE_STM32_HAL_QSPI
CONFIG_USE_STM32_HAL_MDMA if CONFIG_SOC_SERIES_STM32H7X
CONFIG_USE_STM32_HAL_DMA
CONFIG_USE_STM32_HAL_DMA_EX
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.stm32:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.stm32#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → STM32 MSPI 控制器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MSPI_STM32_CONTROLLER`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_CONTROLLER)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_USE_STM32_HAL_QSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_QSPI)、[`CONFIG_USE_STM32_HAL_MDMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_MDMA)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_USE_STM32_HAL_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA)、[`CONFIG_USE_STM32_HAL_DMA_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA_EX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32H7X`。

<a id="CONFIG_MSPI_STM32_XSPI"></a>

## 129.33 `CONFIG_MSPI_STM32_XSPI`

**提示（Prompt）**：STM32 XSPI 控制器驱动

**说明（Help）**

启用 STM32 系列处理器的 XSPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_XSPI_CONTROLLER_ENABLED && CONFIG_MSPI_STM32_CONTROLLER && CONFIG_MSPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO if n
CONFIG_USE_STM32_HAL_XSPI
CONFIG_USE_STM32_LL_DLYB
CONFIG_USE_STM32_HAL_DMA
CONFIG_USE_STM32_HAL_DMA_EX
```

**定义位置（Location）**：[`drivers/mspi/Kconfig.stm32:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig.stm32#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → STM32 MSPI 控制器驱动【实验性（EXPERIMENTAL）】

**配置项引用（Symbol References）**：[`CONFIG_MSPI_STM32_CONTROLLER`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_STM32_CONTROLLER)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_USE_STM32_HAL_XSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_XSPI)、[`CONFIG_USE_STM32_LL_DLYB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_LL_DLYB)、[`CONFIG_USE_STM32_HAL_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA)、[`CONFIG_USE_STM32_HAL_DMA_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA_EX)。

<a id="CONFIG_MSPI_TIMING"></a>

## 129.34 `CONFIG_MSPI_TIMING`

**提示（Prompt）**：时序（Timing）支持

**说明（Help）**

为需要配置时序才能在高频下正确工作的控制器，启用设备驱动中的 `mspi_timing_config` 调用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MSPI
```

**被选择（Selected by）**

```text
CONFIG_MSPI_EMUL
```

**被弱选择（Implied by）**

```text
CONFIG_MSPI_AMBIQ_AP3
CONFIG_MSPI_AMBIQ_AP5
CONFIG_MSPI_CDNS
CONFIG_MSPI_DW
```

**定义位置（Location）**：[`drivers/mspi/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mspi/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_MSPI_EMUL`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_EMUL)、[`CONFIG_MSPI_AMBIQ_AP3`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_AMBIQ_AP3)、[`CONFIG_MSPI_AMBIQ_AP5`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_AMBIQ_AP5)、[`CONFIG_MSPI_CDNS`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_CDNS)、[`CONFIG_MSPI_DW`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI_DW)。

<!-- kconfig-navigation -->

[上一章](P128_drivers_modem_配置项参考_4.md) · [返回大纲](大纲.md) · [下一章](P130_drivers_mux_配置项参考.md)
