---
id: learning.zephyr-docs.kconfig-reference.page-173
title: "`drivers/spi`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第173章\_`drivers/spi`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `drivers/spi` 的 98 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SPI_NXP_LPSPI_DMA"></a>

## 173.1 `CONFIG_SPI_NXP_LPSPI_DMA`

**提示（Prompt）**：基于 DMA 的 NXP LPSPI 驱动

**说明（Help）**

为设备树（DT）节点指定了 `dmas` 属性的 LPSPI 外设启用 DMA 传输。基于 DMA 的驱动更重视带宽，而非延迟，因为 DMA 对较大数据传输效率更高，可避免 CPU 承担传输工作。不过，配置 DMA 传输比直接用 CPU 启动传输更复杂，因此从提出传输请求到实际开始传输的延迟可能更大。

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
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/spi/spi_nxp_lpspi/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/spi_nxp_lpspi/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → NXP LPSPI 外设（Peripheral）

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_SPI_NXP_LPSPI_ERR050456"></a>

## 173.2 `CONFIG_SPI_NXP_LPSPI_ERR050456`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示 LPSPI 模块受勘误 050456（Erratum 050456）影响。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_NXP_LPSPI && CONFIG_SPI
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_MCXE31X
CONFIG_SOC_SERIES_S32K3
```

**定义位置（Location）**：[`drivers/spi/spi_nxp_lpspi/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/spi_nxp_lpspi/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → NXP LPSPI 外设（Peripheral）

**配置项引用（Symbol References）**：[`CONFIG_SPI_NXP_LPSPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NXP_LPSPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SOC_SERIES_MCXE31X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MCXE31X)、[`CONFIG_SOC_SERIES_S32K3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_S32K3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_MCXE31X`、`CONFIG_SOC_SERIES_S32K3`。

<a id="CONFIG_SPI_NXP_LPSPI_MAX_SCK_FREQUENCY"></a>

## 173.3 `CONFIG_SPI_NXP_LPSPI_MAX_SCK_FREQUENCY`

**提示（Prompt）**：最大 SPI SCK 频率，单位为 Hz

**说明（Help）**

此选项指定硬件支持的最大 SPI SCK 时钟频率。默认值 30 MHz 是许多 LPSPI 外设常见的最大频率，但实际最大频率可能因具体 LPSPI 实例和片上系统（SoC）而异。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_NXP_LPSPI && CONFIG_SPI
```

**默认值（Defaults）**

```text
30000000
```

**定义位置（Location）**：[`drivers/spi/spi_nxp_lpspi/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/spi_nxp_lpspi/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → NXP LPSPI 外设（Peripheral）

**配置项引用（Symbol References）**：[`CONFIG_SPI_NXP_LPSPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NXP_LPSPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_NXP_LPSPI_RTIO_DMA"></a>

## 173.4 `CONFIG_SPI_NXP_LPSPI_RTIO_DMA`

**提示（Prompt）**：NXP LPSPI RTIO DMA 支持

**说明（Help）**

为大于 DMA 阈值的 RTIO 传输启用 DMA 传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_NXP_LPSPI_CPU_RTIO && n && CONFIG_SPI_NXP_LPSPI && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/spi/spi_nxp_lpspi/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/spi_nxp_lpspi/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → NXP LPSPI 外设（Peripheral） → 基于 RTIO 的 NXP LPSPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_NXP_LPSPI_CPU_RTIO`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NXP_LPSPI_CPU_RTIO)、[`CONFIG_SPI_NXP_LPSPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NXP_LPSPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_SPI_NXP_LPSPI_RTIO_DMA_OVERRIDE_THRESHOLD"></a>

## 173.5 `CONFIG_SPI_NXP_LPSPI_RTIO_DMA_OVERRIDE_THRESHOLD`

**提示（Prompt）**：覆盖 LPSPI RTIO DMA 阈值

**说明（Help）**

启用此选项后，使用自定义阈值判断 RTIO SPI 事务是否应由 DMA 处理。默认情况下，事务大小超过 LPSPI 接收 FIFO（RX FIFO）深度时使用 DMA。此选项允许按应用的性能需求调整阈值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_NXP_LPSPI && CONFIG_SPI
```

**定义位置（Location）**：[`drivers/spi/spi_nxp_lpspi/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/spi_nxp_lpspi/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → NXP LPSPI 外设（Peripheral）

**配置项引用（Symbol References）**：[`CONFIG_SPI_NXP_LPSPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NXP_LPSPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_NXP_LPSPI_RTIO_DMA_THRESHOLD"></a>

## 173.6 `CONFIG_SPI_NXP_LPSPI_RTIO_DMA_THRESHOLD`

**提示（Prompt）**：LPSPI RTIO DMA 阈值

**说明（Help）**

自定义阈值，以字（Word）为单位，用于在 CPU 驱动与 DMA 驱动的 RTIO 传输之间选择。大于此阈值的 RTIO 事务由 DMA 处理，小于或等于此阈值的事务由 CPU 处理。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_NXP_LPSPI_RTIO_DMA_OVERRIDE_THRESHOLD && CONFIG_SPI_NXP_LPSPI && CONFIG_SPI
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/spi/spi_nxp_lpspi/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/spi_nxp_lpspi/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → NXP LPSPI 外设（Peripheral） → 覆盖 LPSPI RTIO DMA 阈值

**配置项引用（Symbol References）**：[`CONFIG_SPI_NXP_LPSPI_RTIO_DMA_OVERRIDE_THRESHOLD`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_NXP_LPSPI_RTIO_DMA_OVERRIDE_THRESHOLD)、[`CONFIG_SPI_NXP_LPSPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NXP_LPSPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_NXP_LPSPI_TXFIFO_WAIT_CYCLES"></a>

## 173.7 `CONFIG_SPI_NXP_LPSPI_TXFIFO_WAIT_CYCLES`

**提示（Prompt）**：等待发送 FIFO 变空的 CPU 周期数

**说明（Help）**

通常无需修改此选项。驱动往往需要通过检查发送 FIFO（TX FIFO）是否清空，确认硬件已消耗发送命令。此选项指定执行该检查时最多等待多少 CPU 周期。特殊值 0 表示无限等待；当编程错误导致发送 FIFO 无法清空时，这可能有助于调试。默认值 10000 是任意选取的值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_NXP_LPSPI && CONFIG_SPI
```

**默认值（Defaults）**

```text
0 if CONFIG_DEBUG
10000
```

**定义位置（Location）**：[`drivers/spi/spi_nxp_lpspi/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/spi_nxp_lpspi/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → NXP LPSPI 外设（Peripheral）

**配置项引用（Symbol References）**：[`CONFIG_SPI_NXP_LPSPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NXP_LPSPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DEBUG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEBUG)。

<a id="CONFIG_SPI_NXP_RTIO_SQ_SIZE"></a>

## 173.8 `CONFIG_SPI_NXP_RTIO_SQ_SIZE`

**提示（Prompt）**：可用提交队列条目（Submission Queue Entries）数量

**说明（Help）**

SPI 使用实时输入输出（RTIO）时，每个驱动都持有一个上下文，阻塞式 API 调用通过该上下文执行 SPI 事务。使用等长缓冲区的普通 SPI 操作时，此队列的深度至少应容纳所使用的最长 `spi_buf_sets` 集合。发送／接收 SPI 缓冲区集合的长度并不总是相等时，可能需要稍大的队列深度，因为它们会被转换为普通收发操作（Transceives）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_NXP_LPSPI_CPU_RTIO && CONFIG_SPI_NXP_LPSPI && CONFIG_SPI
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/spi/spi_nxp_lpspi/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/spi_nxp_lpspi/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → NXP LPSPI 外设（Peripheral）

**配置项引用（Symbol References）**：[`CONFIG_SPI_NXP_LPSPI_CPU_RTIO`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NXP_LPSPI_CPU_RTIO)、[`CONFIG_SPI_NXP_LPSPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_NXP_LPSPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_OC_SIMPLE"></a>

## 173.9 `CONFIG_SPI_OC_SIMPLE`

**提示（Prompt）**：OpenCores Simple SPI 控制器驱动

**说明（Help）**

启用 Simple SPI 控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_OPENCORES_SPI_SIMPLE_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.oc_simple:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.oc_simple#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_OMAP_MCSPI"></a>

## 173.10 `CONFIG_SPI_OMAP_MCSPI`

**提示（Prompt）**：OMAP 和 K3 器件的 MCSPI 驱动

**说明（Help）**

启用 TI OMAP MCSPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_OMAP_MCSPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.omap:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.omap#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_OPENTITAN"></a>

## 173.11 `CONFIG_SPI_OPENTITAN`

**提示（Prompt）**：OpenTitan SPI 控制器驱动

**说明（Help）**

启用 OpenTitan 上的 SPI 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LOWRISC_OPENTITAN_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.opentitan:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.opentitan#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_PERIPHERAL"></a>

## 173.12 `CONFIG_SPI_PERIPHERAL`

**提示（Prompt）**：外设角色支持（Peripheral Support）［实验性，EXPERIMENTAL］

**说明（Help）**

启用驱动的 SPI 外设角色操作（Peripheral Operations）。外设角色支持取决于驱动及其运行的硬件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_SPI_SLAVE
CONFIG_ESP32_SPI_TARGET
CONFIG_SPI_NRFX_SPIS
```

**定义位置（Location）**：[`drivers/spi/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_SPI_SLAVE`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_SLAVE)、[`CONFIG_ESP32_SPI_TARGET`](P172_drivers_spi_配置项参考_1.md#CONFIG_ESP32_SPI_TARGET)、[`CONFIG_SPI_NRFX_SPIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_NRFX_SPIS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SPI_NRFX_SPIS`。

<a id="CONFIG_SPI_PL022"></a>

## 173.13 `CONFIG_SPI_PL022`

**提示（Prompt）**：ARM PL022 SPI 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_PL022_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL if n
```

**定义位置（Location）**：[`drivers/spi/Kconfig.pl022:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.pl022#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_PL022_DMA"></a>

## 173.14 `CONFIG_SPI_PL022_DMA`

**提示（Prompt）**：PL022 直接内存访问（DMA）模式

**说明（Help）**

为 PL022 SPI 驱动启用直接内存访问（DMA）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_PL022 && CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/spi/Kconfig.pl022:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.pl022#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → ARM PL022 SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_PL022`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_PL022)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_SPI_PL022_INTERRUPT"></a>

## 173.15 `CONFIG_SPI_PL022_INTERRUPT`

**提示（Prompt）**：PL022 中断模式（Interrupt Mode）

**说明（Help）**

为 PL022 SPI 驱动启用中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_PL022 && CONFIG_SPI
```

**定义位置（Location）**：[`drivers/spi/Kconfig.pl022:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.pl022#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → ARM PL022 SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_PL022`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_PL022)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_PSOC6"></a>

## 173.16 `CONFIG_SPI_PSOC6`

**提示（Prompt）**：PSOC 6 MCU SCB SPI 驱动

**说明（Help）**

此选项为 PSOC 6 片上系统（SoC）系列启用 SCB[SPI] 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CYPRESS_PSOC6_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_SPI
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.psoc6:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.psoc6#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_USE_INFINEON_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_PW"></a>

## 173.17 `CONFIG_SPI_PW`

**提示（Prompt）**：Penwell SPI 驱动

**说明（Help）**

启用 Penwell SPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_PENWELL_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PCIE if n
```

**定义位置（Location）**：[`drivers/spi/Kconfig.pw:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.pw#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PCIE`](P134_drivers_pcie_配置项参考.md#CONFIG_PCIE)。

<a id="CONFIG_SPI_PW_INTERRUPT"></a>

## 173.18 `CONFIG_SPI_PW_INTERRUPT`

**提示（Prompt）**：Penwell SPI 中断模式（Interrupt Mode）支持

**说明（Help）**

启用 SPI 驱动的中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_PW && CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_DYNAMIC_INTERRUPTS if n
```

**定义位置（Location）**：[`drivers/spi/Kconfig.pw:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.pw#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Penwell SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_PW`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_PW)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)。

<a id="CONFIG_SPI_PW_LPSS_DMA"></a>

## 173.19 `CONFIG_SPI_PW_LPSS_DMA`

**提示（Prompt）**：同步传输（Synchronous Transfers）使用 SPI DMA

**说明（Help）**

此选项允许同步数据传输使用 SPI 直接内存访问（DMA）功能。所有发送（TX）操作使用 DMA 通道 0，所有接收（RX）操作使用 DMA 通道 1。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_PW_INTERRUPT && CONFIG_SPI_PW && CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_DMA
CONFIG_DMA_INTEL_LPSS
```

**定义位置（Location）**：[`drivers/spi/Kconfig.pw:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.pw#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Penwell SPI 驱动 → Penwell SPI 中断模式（Interrupt Mode）支持

**配置项引用（Symbol References）**：[`CONFIG_SPI_PW_INTERRUPT`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_PW_INTERRUPT)、[`CONFIG_SPI_PW`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_PW)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_DMA_INTEL_LPSS`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA_INTEL_LPSS)。

<a id="CONFIG_SPI_RA_DTC"></a>

## 173.20 `CONFIG_SPI_RA_DTC`

**提示（Prompt）**：RA MCU SPI 数据传输控制器（DTC）支持

**说明（Help）**

为 SPI 实例启用数据传输控制器（DTC）模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RENESAS_RA && CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_DTC
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_ra:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_ra#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RA SPI

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RA`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_USE_RA_FSP_DTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_DTC)。

<a id="CONFIG_SPI_REALTEK_RTS5912"></a>

## 173.21 `CONFIG_SPI_REALTEK_RTS5912`

**提示（Prompt）**：REALTEK RTS5912 SPI 驱动

**说明（Help）**

启用 Realtek RTS5912 SPI 控制器驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5912_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.rts5912:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.rts5912#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_RENESAS_RA"></a>

## 173.22 `CONFIG_SPI_RENESAS_RA`

**提示（Prompt）**：Renesas RA SPI

**说明（Help）**

启用 Renesas RA SPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_SPI
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_ra:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_ra#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_USE_RA_FSP_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_RENESAS_RA8"></a>

## 173.23 `CONFIG_SPI_RENESAS_RA8`

**提示（Prompt）**：Renesas RA SPI B

**说明（Help）**

启用 Renesas RA SPI B 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA8_SPI_B_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_SPI_B
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_ra8:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_ra8#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_USE_RA_FSP_SPI_B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_SPI_B)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_RENESAS_RA_SCI"></a>

## 173.24 `CONFIG_SPI_RENESAS_RA_SCI`

**提示（Prompt）**：Renesas RA SCI SPI

**说明（Help）**

启用 Renesas RA SCI SPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_SPI_SCI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI_RENESAS_RA_SCI_INTERRUPT if CONFIG_SPI_ASYNC
CONFIG_USE_RA_FSP_SCI_SPI
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_ra:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_ra#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_RENESAS_RA_SCI_INTERRUPT`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA_SCI_INTERRUPT)、[`CONFIG_SPI_ASYNC`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_ASYNC)、[`CONFIG_USE_RA_FSP_SCI_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_SCI_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_RENESAS_RA_SCI_B"></a>

## 173.25 `CONFIG_SPI_RENESAS_RA_SCI_B`

**提示（Prompt）**：Renesas RA SCI B SPI

**说明（Help）**

启用 Renesas RA SCI B SPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_SPI_SCI_B_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_SCI_B_SPI
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_ra:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_ra#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_USE_RA_FSP_SCI_B_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_SCI_B_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_RENESAS_RA_SCI_B_DMAC"></a>

## 173.26 `CONFIG_SPI_RENESAS_RA_SCI_B_DMAC`

**提示（Prompt）**：RA MCU SCI B SPI 直接内存访问控制器（DMAC）支持

**说明（Help）**

为 RA 系列 SCI B SPI 驱动启用直接内存访问控制器（Direct Memory Access Controller，DMAC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RENESAS_RA_SCI_B_INTERRUPT && CONFIG_SPI_RENESAS_RA_SCI_B && CONFIG_SPI
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_DMA
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_ra:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_ra#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RA SCI B SPI

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RA_SCI_B_INTERRUPT`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA_SCI_B_INTERRUPT)、[`CONFIG_SPI_RENESAS_RA_SCI_B`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA_SCI_B)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_USE_RA_FSP_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_DMA)。

<a id="CONFIG_SPI_RENESAS_RA_SCI_B_DTC"></a>

## 173.27 `CONFIG_SPI_RENESAS_RA_SCI_B_DTC`

**提示（Prompt）**：RA MCU SCI B SPI 数据传输控制（DTC）支持

**说明（Help）**

为 RA 系列 SCI B SPI 驱动启用数据传输控制（Data Transfer Control，DTC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RENESAS_RA_SCI_B_INTERRUPT && CONFIG_SPI_RENESAS_RA_SCI_B && CONFIG_SPI
```

**默认值（Defaults）**

```text
n || n
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_DTC
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_ra:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_ra#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RA SCI B SPI

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RA_SCI_B_INTERRUPT`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA_SCI_B_INTERRUPT)、[`CONFIG_SPI_RENESAS_RA_SCI_B`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA_SCI_B)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_USE_RA_FSP_DTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_DTC)。

<a id="CONFIG_SPI_RENESAS_RA_SCI_B_INTERRUPT"></a>

## 173.28 `CONFIG_SPI_RENESAS_RA_SCI_B_INTERRUPT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

为 RA 系列 SCI B SPI 驱动启用中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_ASYNC && CONFIG_SPI_RENESAS_RA_SCI_B && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_ra:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_ra#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RA SCI B SPI

**配置项引用（Symbol References）**：[`CONFIG_SPI_ASYNC`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_ASYNC)、[`CONFIG_SPI_RENESAS_RA_SCI_B`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA_SCI_B)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_RENESAS_RA_SCI_DTC"></a>

## 173.29 `CONFIG_SPI_RENESAS_RA_SCI_DTC`

**提示（Prompt）**：RA MCU SCI SPI 数据传输控制（DTC）支持

**说明（Help）**

为 RA 系列 SCI SPI 驱动启用数据传输控制（DTC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RENESAS_RA_SCI_INTERRUPT && CONFIG_SPI_RENESAS_RA_SCI && CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_DTC
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_ra:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_ra#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RA SCI SPI → RENESAS RA SCI SPI 中断支持（Interrupt Support）

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RA_SCI_INTERRUPT`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA_SCI_INTERRUPT)、[`CONFIG_SPI_RENESAS_RA_SCI`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA_SCI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_USE_RA_FSP_DTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_DTC)。

<a id="CONFIG_SPI_RENESAS_RA_SCI_INTERRUPT"></a>

## 173.30 `CONFIG_SPI_RENESAS_RA_SCI_INTERRUPT`

**提示（Prompt）**：RENESAS RA SCI SPI 中断支持（Interrupt Support）

**说明（Help）**

为 RA 系列 SCI SPI 驱动启用中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_ASYNC && CONFIG_SPI_RENESAS_RA_SCI && CONFIG_SPI
```

**被选择（Selected by）**

```text
CONFIG_SPI_RENESAS_RA_SCI
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_ra:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_ra#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RA SCI SPI

**配置项引用（Symbol References）**：[`CONFIG_SPI_ASYNC`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_ASYNC)、[`CONFIG_SPI_RENESAS_RA_SCI`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA_SCI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_RENESAS_RX"></a>

## 173.31 `CONFIG_SPI_RENESAS_RX`

**提示（Prompt）**：Renesas RX 系列 SPI 驱动

**说明（Help）**

启用 Renesas RX 系列 SPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_RSPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RX_RDP_RSPI
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_rx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_rx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_USE_RX_RDP_RSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RX_RDP_RSPI)。

<a id="CONFIG_SPI_RENESAS_RX_16BITS_FRAME"></a>

## 173.32 `CONFIG_SPI_RENESAS_RX_16BITS_FRAME`

**提示（Prompt）**：测试回环（Test Loopback）：16 位

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RENESAS_RX && CONFIG_SPI
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_rx:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_rx#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RX 系列 SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RX`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RX)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_RENESAS_RX_DTC"></a>

## 173.33 `CONFIG_SPI_RENESAS_RX_DTC`

**提示（Prompt）**：启用 RSPI 数据传输控制器（DTC）

**说明（Help）**

在 RX 系列的 RSPI 传输中使用数据传输控制器（DTC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RX_DTC_ENABLED && CONFIG_SPI_RENESAS_RX && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RENESAS_RX_DTC
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_rx:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_rx#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RX 系列 SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RX`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RX)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_RENESAS_RX_DTC`](P123_drivers_misc_配置项参考.md#CONFIG_RENESAS_RX_DTC)。

<a id="CONFIG_SPI_RENESAS_RX_HIGH_SPEED_READ"></a>

## 173.34 `CONFIG_SPI_RENESAS_RX_HIGH_SPEED_READ`

**提示（Prompt）**：RX MCU RSPI 高速读取模式（High Speed Read Mode）

**说明（Help）**

启用 RX 系列 RSPI 驱动的高速读取模式（High Speed Read Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RENESAS_RX && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_rx:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_rx#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RX 系列 SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RX`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RX)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_RENESAS_RX_INTERRUPT"></a>

## 173.35 `CONFIG_SPI_RENESAS_RX_INTERRUPT`

**提示（Prompt）**：RX MCU RSPI 中断支持（Interrupt Support）

**说明（Help）**

为 RX 系列 RSPI 驱动启用中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RENESAS_RX && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_rx:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_rx#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RX 系列 SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RX`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RX)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_RENESAS_RX_USE_HW_SS"></a>

## 173.36 `CONFIG_SPI_RENESAS_RX_USE_HW_SS`

**提示（Prompt）**：RX MCU RSPI 硬件片选（Hardware Chip Select）支持

**说明（Help）**

使用片选引脚（Chip Select Pin）代替软件片选（Software Chip Select）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RENESAS_RX && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_rx:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_rx#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RX 系列 SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RX`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RX)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_RENESAS_RZ"></a>

## 173.37 `CONFIG_SPI_RENESAS_RZ`

**提示（Prompt）**：Renesas RZ SPI

**说明（Help）**

启用 Renesas RZ SPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_SPI
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_rz:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_rz#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_USE_RZ_FSP_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_RENESAS_RZ_DMA"></a>

## 173.38 `CONFIG_SPI_RENESAS_RZ_DMA`

**提示（Prompt）**：RZ SPI 直接内存访问（DMA）支持

**说明（Help）**

为 SPI 实例启用直接内存访问（DMA）模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SPI_RENESAS_RZ || CONFIG_SPI_RENESAS_RZ_SPI_B) && CONFIG_SPI
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_SPI_RENESAS_RZ_INTERRUPT
CONFIG_USE_RZ_FSP_DMAC if CONFIG_SOC_SERIES_RZT2L || CONFIG_SOC_SERIES_RZT2M || CONFIG_SOC_SERIES_RZN2L
CONFIG_USE_RZ_FSP_DMAC_B if CONFIG_SOC_SERIES_RZV2N || CONFIG_SOC_SERIES_RZV2H
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_rz:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_rz#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RZ`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ)、[`CONFIG_SPI_RENESAS_RZ_SPI_B`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ_SPI_B)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_RENESAS_RZ_INTERRUPT`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ_INTERRUPT)、[`CONFIG_USE_RZ_FSP_DMAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_DMAC)、[`CONFIG_SOC_SERIES_RZT2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2L)、[`CONFIG_SOC_SERIES_RZT2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2M)、[`CONFIG_SOC_SERIES_RZN2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2L)、[`CONFIG_USE_RZ_FSP_DMAC_B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_DMAC_B)、[`CONFIG_SOC_SERIES_RZV2N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2N)、[`CONFIG_SOC_SERIES_RZV2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2H)。

<a id="CONFIG_SPI_RENESAS_RZ_INTERRUPT"></a>

## 173.39 `CONFIG_SPI_RENESAS_RZ_INTERRUPT`

**提示（Prompt）**：RZ SPI 中断支持（Interrupt Support）

**说明（Help）**

启用 SPI 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SPI_RENESAS_RZ || CONFIG_SPI_RENESAS_RZ_SPI_B) && CONFIG_SPI
```

**被选择（Selected by）**

```text
CONFIG_SPI_RENESAS_RZ_DMA
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_rz:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_rz#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RZ`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ)、[`CONFIG_SPI_RENESAS_RZ_SPI_B`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ_SPI_B)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_RENESAS_RZ_DMA`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ_DMA)。

<a id="CONFIG_SPI_RENESAS_RZ_RSPI"></a>

## 173.40 `CONFIG_SPI_RENESAS_RZ_RSPI`

**提示（Prompt）**：Renesas RZ RSPI SPI

**说明（Help）**

启用 Renesas RZ RSPI SPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_RSPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_RSPI_SPI
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_rz:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_rz#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_USE_RZ_FSP_RSPI_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_RSPI_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_RENESAS_RZ_RSPI_DMAC"></a>

## 173.41 `CONFIG_SPI_RENESAS_RZ_RSPI_DMAC`

**提示（Prompt）**：RZ SPI 直接内存访问（DMA）支持

**说明（Help）**

为 SPI 实例启用直接内存访问（DMA）模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RENESAS_RZ_RSPI && CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_DMAC_B if CONFIG_SOC_SERIES_RZG2L || CONFIG_SOC_SERIES_RZG2UL || CONFIG_SOC_SERIES_RZG3S || CONFIG_SOC_SERIES_RZV2L
CONFIG_USE_RZ_FSP_DMAC if CONFIG_SOC_SERIES_RZA3UL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_rz:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_rz#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RZ RSPI SPI

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RZ_RSPI`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ_RSPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_USE_RZ_FSP_DMAC_B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_DMAC_B)、[`CONFIG_SOC_SERIES_RZG2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG2L)、[`CONFIG_SOC_SERIES_RZG2UL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG2UL)、[`CONFIG_SOC_SERIES_RZG3S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZG3S)、[`CONFIG_SOC_SERIES_RZV2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2L)、[`CONFIG_USE_RZ_FSP_DMAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_DMAC)、[`CONFIG_SOC_SERIES_RZA3UL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZA3UL)。

<a id="CONFIG_SPI_RENESAS_RZ_RSPI_INTERRUPT"></a>

## 173.42 `CONFIG_SPI_RENESAS_RZ_RSPI_INTERRUPT`

**提示（Prompt）**：RZ RSPI 中断支持（Interrupt Support）

**说明（Help）**

启用 RSPI 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RENESAS_RZ_RSPI && CONFIG_SPI
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_rz:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_rz#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RZ RSPI SPI

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RZ_RSPI`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ_RSPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_RENESAS_RZ_SPI_B"></a>

## 173.43 `CONFIG_SPI_RENESAS_RZ_SPI_B`

**提示（Prompt）**：Renesas RZ SPI B

**说明（Help）**

启用 Renesas RZ SPI B 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_SPI_B_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_SPI_B
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_rz:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_rz#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_USE_RZ_FSP_SPI_B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_SPI_B)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_RENESAS_RZ_USE_INTERRUPT_SELECT"></a>

## 173.44 `CONFIG_SPI_RENESAS_RZ_USE_INTERRUPT_SELECT`

**提示（Prompt）**：RZ SPI 中断选择（Interrupt Select）支持

**说明（Help）**

支持 SPI 中断选择（Interrupt Select）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_RZV2N || CONFIG_SOC_SERIES_RZV2H) && (CONFIG_SPI_RENESAS_RZ || CONFIG_SPI_RENESAS_RZ_SPI_B) && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_rz:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_rz#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RZV2N`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2N)、[`CONFIG_SOC_SERIES_RZV2H`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZV2H)、[`CONFIG_SPI_RENESAS_RZ`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ)、[`CONFIG_SPI_RENESAS_RZ_SPI_B`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ_SPI_B)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_RPI_PICO_PIO"></a>

## 173.45 `CONFIG_SPI_RPI_PICO_PIO`

**提示（Prompt）**：Raspberry Pi Pico PIO SPI 控制器驱动

**说明（Help）**

在 Raspberry Pi Pico 上启用通过可编程输入输出（PIO）驱动的 SPI。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_SPI_PIO_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PICOSDK_USE_PIO
CONFIG_PICOSDK_USE_CLAIM
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.rpi_pico:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.rpi_pico#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PICOSDK_USE_PIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_PIO)、[`CONFIG_PICOSDK_USE_CLAIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_CLAIM)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_RPI_PICO_PIO_DMA"></a>

## 173.46 `CONFIG_SPI_RPI_PICO_PIO_DMA`

**提示（Prompt）**：Raspberry Pi Pico PIO SPI 直接内存访问（DMA）模式

**说明（Help）**

为 Raspberry Pi Pico PIO SPI 驱动启用直接内存访问（DMA）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RPI_PICO_PIO && CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/spi/Kconfig.rpi_pico:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.rpi_pico#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Raspberry Pi Pico PIO SPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_RPI_PICO_PIO`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RPI_PICO_PIO)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_SPI_RTIO"></a>

## 173.47 `CONFIG_SPI_RTIO`

**提示（Prompt）**：实时输入输出（RTIO）支持［实验性，EXPERIMENTAL］

**说明（Help）**

此选项启用实时输入输出（RTIO）API 调用。由于 API 本身尚不稳定，RTIO 支持仍属实验性功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_RTIO
CONFIG_RTIO_WORKQ
```

**被选择（Selected by）**

```text
CONFIG_ADIS1647X
CONFIG_BMI08X
CONFIG_AFBR_S50
CONFIG_PAA3905
CONFIG_PAT9136
CONFIG_IIS3DWB
CONFIG_LIS2DUX12
CONFIG_LSM6DSV16X
CONFIG_LSM6DSVXXX
CONFIG_ICM45686
CONFIG_ICM566XX
```

**定义位置（Location）**：[`drivers/spi/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO)、[`CONFIG_RTIO_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_WORKQ)、[`CONFIG_ADIS1647X`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADIS1647X)、[`CONFIG_BMI08X`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI08X)、[`CONFIG_AFBR_S50`](P150_drivers_sensor_配置项参考_2.md#CONFIG_AFBR_S50)、[`CONFIG_PAA3905`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PAA3905)、[`CONFIG_PAT9136`](P160_drivers_sensor_配置项参考_12.md#CONFIG_PAT9136)、[`CONFIG_IIS3DWB`](P155_drivers_sensor_配置项参考_7.md#CONFIG_IIS3DWB)、[`CONFIG_LIS2DUX12`](P156_drivers_sensor_配置项参考_8.md#CONFIG_LIS2DUX12)、[`CONFIG_LSM6DSV16X`](P157_drivers_sensor_配置项参考_9.md#CONFIG_LSM6DSV16X)、[`CONFIG_LSM6DSVXXX`](P158_drivers_sensor_配置项参考_10.md#CONFIG_LSM6DSVXXX)、[`CONFIG_ICM45686`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM45686)、[`CONFIG_ICM566XX`](P154_drivers_sensor_配置项参考_6.md#CONFIG_ICM566XX)。

<a id="CONFIG_SPI_RTIO_CQ_SIZE"></a>

## 173.48 `CONFIG_SPI_RTIO_CQ_SIZE`

**提示（Prompt）**：可用完成队列条目（Completion Queue Entries）数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RTIO && CONFIG_SPI
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_rz:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_rz#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_RTIO`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RTIO)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_RTIO_FALLBACK_MSGS"></a>

## 173.49 `CONFIG_SPI_RTIO_FALLBACK_MSGS`

**提示（Prompt）**：默认处理程序可使用的 `spi_buf` 结构体数量

**说明（Help）**

当 RTIO 与尚未原生实现提交 API（Submit API）的驱动配合使用时，提交内容会转换回 `struct spi_buf` 值，再交给 `spi_transfer`。这要求栈上预留一定数量的消息对象，用于接收转换后的提交内容。MISRA 规则要求提前知道此数量。通常 4 个即可满足需求；如果使用 RTIO 时，驱动没有原生实现提交 API，并出现 SPI 消息数量不足的错误，则应调整此 Kconfig 选项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RTIO && CONFIG_SPI
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/spi/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → 实时输入输出（RTIO）支持［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_SPI_RTIO`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RTIO)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_RTIO_SQ_SIZE"></a>

## 173.50 `CONFIG_SPI_RTIO_SQ_SIZE`

**提示（Prompt）**：可用提交队列条目（Submission Queue Entries）数量

**说明（Help）**

SPI 使用实时输入输出（RTIO）时，每个驱动都持有一个上下文，阻塞式 API 调用通过该上下文执行 SPI 事务。使用等长缓冲区的普通 SPI 操作时，此队列的深度至少应容纳所使用的最长 `spi_buf_sets` 集合。发送／接收 SPI 缓冲区集合的长度并不总是相等时，可能需要稍大的队列深度，因为它们会被转换为普通收发操作（Transceives）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RTIO && CONFIG_SPI
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_rz:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_rz#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_RTIO`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RTIO)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_RTS5817"></a>

## 173.51 `CONFIG_SPI_RTS5817`

**提示（Prompt）**：RTS5817 SPI 控制器（Controller）驱动

**说明（Help）**

此选项启用 RTS5817 SPI 控制器封装驱动（Wrapper Driver）。封装位于 DesignWare SSI 核心 `spi_dw` 之上，通过控制器寄存器块驱动 DMA 传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_RTS5817_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_SPI_DW
```

**定义位置（Location）**：[`drivers/spi/Kconfig.rts5817:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.rts5817#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SPI_DW`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_DW)。

<a id="CONFIG_SPI_RTS5817_INIT_PRIORITY"></a>

## 173.52 `CONFIG_SPI_RTS5817_INIT_PRIORITY`

**提示（Prompt）**：RTS5817 SPI 封装初始化优先级（Wrapper Init Priority）

**说明（Help）**

RTS5817 SPI 封装的初始化优先级。必须大于 `CONFIG_SPI_INIT_PRIORITY`，以确保封装访问 DW 寄存器块之前，底层 `snps,designware-spi` 设备已就绪，包括时钟已启用、内存映射输入输出（MMIO）已映射。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RTS5817 && CONFIG_SPI
```

**默认值（Defaults）**

```text
51
```

**定义位置（Location）**：[`drivers/spi/Kconfig.rts5817:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.rts5817#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → RTS5817 SPI 控制器（Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_RTS5817`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RTS5817)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_RTS5817_INTERRUPT"></a>

## 173.53 `CONFIG_SPI_RTS5817_INTERRUPT`

**提示（Prompt）**：RTS5817 SPI 中断模式（Interrupt Mode）

**说明（Help）**

启用 RTS5817 SPI 控制器封装驱动的中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RTS5817 && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.rts5817:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.rts5817#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → RTS5817 SPI 控制器（Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_RTS5817`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RTS5817)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_RV32M1_LPSPI"></a>

## 173.54 `CONFIG_SPI_RV32M1_LPSPI`

**提示（Prompt）**：RV32M1 LPSPI 驱动

**说明（Help）**

启用 RV32M1 LPSPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_OPENISA_RV32M1_LPSPI_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.rv32m1_lpspi:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.rv32m1_lpspi#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_SAM"></a>

## 173.55 `CONFIG_SPI_SAM`

**提示（Prompt）**：Atmel SAM 系列 SPI 驱动

**说明（Help）**

启用 SAM SPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/spi/Kconfig.sam:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.sam#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_SPI_SAM0"></a>

## 173.56 `CONFIG_SPI_SAM0`

**提示（Prompt）**：Atmel SAM0 系列 SERCOM SPI 驱动

**说明（Help）**

启用 SAM0 SERCOM SPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ATMEL_SAM0_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.sam0:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.sam0#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_SAM0_DMA"></a>

## 173.57 `CONFIG_SPI_SAM0_DMA`

**提示（Prompt）**：Atmel SAM0 直接内存访问（DMA）支持

**说明（Help）**

为 Atmel SAM0 SPI 驱动启用基于 DMA 的数据传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.sam0:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.sam0#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

<a id="CONFIG_SPI_SAM_DMA"></a>

## 173.58 `CONFIG_SPI_SAM_DMA`

**提示（Prompt）**：SPI SAM 直接内存访问（DMA）支持

**说明（Help）**

对于在设备树节点中启用了 DMA 通道的 SPI 实例，启用 SPI 直接内存访问（DMA）传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_SAM && CONFIG_SPI
```

**默认值（Defaults）**

```text
y if CONFIG_SPI_RTIO
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/spi/Kconfig.sam:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.sam#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Atmel SAM 系列 SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_SAM`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_SAM)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_RTIO`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RTIO)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_SPI_SAM_RTIO_SQ_SIZE"></a>

## 173.59 `CONFIG_SPI_SAM_RTIO_SQ_SIZE`

**提示（Prompt）**：可用提交队列条目（Submission Queue Entries）数量

**说明（Help）**

SPI 使用实时输入输出（RTIO）时，每个驱动都持有一个上下文，阻塞式 API 调用通过该上下文执行 SPI 事务。使用等长缓冲区的普通 SPI 操作时，此队列的深度至少应容纳所使用的最长 `spi_buf_sets` 集合。发送／接收 SPI 缓冲区集合的长度并不总是相等时，可能需要稍大的队列深度，因为它们会被转换为普通收发操作（Transceives）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RTIO && CONFIG_SPI_SAM && CONFIG_SPI
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/spi/Kconfig.sam:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.sam#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Atmel SAM 系列 SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_RTIO`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RTIO)、[`CONFIG_SPI_SAM`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_SAM)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_SC18IS606"></a>

## 173.60 `CONFIG_SPI_SC18IS606`

**提示（Prompt）**：NXP SC18IS606 SPI 控制器驱动

**说明（Help）**

启用 NXP SC18IS606 SPI 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_SC18IS606_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MFD
```

**定义位置（Location）**：[`drivers/spi/Kconfig.sc18is606:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.sc18is606#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_MFD`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD)。

<a id="CONFIG_SPI_SC18IS606_INIT_PRIORITY"></a>

## 173.61 `CONFIG_SPI_SC18IS606_INIT_PRIORITY`

**提示（Prompt）**：SC18IS606 SPI 初始化优先级（Init Priority）

**说明（Help）**

SC18IS606 SPI 控制器的初始化优先级。注意：该值必须大于 I2C 初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_SC18IS606 && CONFIG_SPI
```

**默认值（Defaults）**

```text
99
```

**定义位置（Location）**：[`drivers/spi/Kconfig.sc18is606:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.sc18is606#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → NXP SC18IS606 SPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_SC18IS606`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_SC18IS606)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_SEDI"></a>

## 173.62 `CONFIG_SPI_SEDI`

**提示（Prompt）**：Intel SEDI SPI 驱动

**说明（Help）**

此选项启用 Intel SEDI SPI 驱动。该驱动是一个轻量适配驱动（Shim Driver），构建于 `hal-intel` 模块中的 SEDI 裸机 SPI 驱动（Bare Metal SPI Driver）之上。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_SEDI_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.sedi:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.sedi#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_SF32LB"></a>

## 173.63 `CONFIG_SPI_SF32LB`

**提示（Prompt）**：SF32LB MCU 系列的 SPI 驱动

**说明（Help）**

为 SF32LB 微控制器（MCU）启用 SPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA if n
```

**定义位置（Location）**：[`drivers/spi/Kconfig.sf32lb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.sf32lb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_SPI_SHELL"></a>

## 173.64 `CONFIG_SPI_SHELL`

**提示（Prompt）**：SPI 命令行（Shell）

**说明（Help）**

启用 SPI 命令行（Shell）。当前 SPI 命令行支持简单的 SPI 写入／读取，即收发（Transceive）操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_SPI
```

**定义位置（Location）**：[`drivers/spi/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_SHELL_MAX_DEVICE_SLOTS"></a>

## 173.65 `CONFIG_SPI_SHELL_MAX_DEVICE_SLOTS`

**提示（Prompt）**：SPI 命令行中的空设备槽位数量

**说明（Help）**

SPI 命令行（Shell）中的空设备槽位数量。如果使用了许多 SPI 设备，并在使用 SPI 命令行时看到 `ERROR: not enough space` 错误消息，请增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_SHELL && CONFIG_SPI
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/spi/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_SHELL`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_SHELL)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_SIFIVE"></a>

## 173.66 `CONFIG_SPI_SIFIVE`

**提示（Prompt）**：SiFive SPI 控制器驱动

**说明（Help）**

启用 SiFive Freedom 处理器上的 SPI 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFIVE_SPI0_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL if CONFIG_SOC_SERIES_FE300
```

**定义位置（Location）**：[`drivers/spi/Kconfig.sifive:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.sifive#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SOC_SERIES_FE300`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_FE300)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_FE300`。

<a id="CONFIG_SPI_SILABS_EUSART"></a>

## 173.67 `CONFIG_SPI_SILABS_EUSART`

**提示（Prompt）**：Silabs EUSART SPI 控制器驱动

**说明（Help）**

启用 EUSART SPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_EUSART_SPI_ENABLED && CONFIG_GPIO && CONFIG_CLOCK_CONTROL && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SISDK_EUSART
CONFIG_PINCTRL if CONFIG_SOC_FAMILY_SILABS_S2
```

**定义位置（Location）**：[`drivers/spi/Kconfig.silabs_eusart:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.silabs_eusart#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SILABS_SISDK_EUSART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_EUSART)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="CONFIG_SPI_SILABS_EUSART_DMA"></a>

## 173.68 `CONFIG_SPI_SILABS_EUSART_DMA`

**提示（Prompt）**：Silabs EUSART SPI 控制器驱动的 DMA 传输

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_SILABS_EUSART && CONFIG_SPI
```

**默认值（Defaults）**

```text
y if CONFIG_SPI_ASYNC
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/spi/Kconfig.silabs_eusart:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.silabs_eusart#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Silabs EUSART SPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_SILABS_EUSART`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_SILABS_EUSART)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_ASYNC`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_ASYNC)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_SPI_SILABS_EUSART_DMA_MAX_BLOCKS"></a>

## 173.69 `CONFIG_SPI_SILABS_EUSART_DMA_MAX_BLOCKS`

**提示（Prompt）**：Silabs EUSART SPI 控制器驱动在一次事务中每个通道允许的最大 DMA 传输块数。

**说明（Help）**

SPI 事务中的每个数据块（Chunk），以及每 2048 字节，都需要一个传输块。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_SILABS_EUSART_DMA && CONFIG_SPI
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/spi/Kconfig.silabs_eusart:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.silabs_eusart#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Silabs EUSART SPI 控制器驱动 → Silabs EUSART SPI 控制器驱动的 DMA 传输

**配置项引用（Symbol References）**：[`CONFIG_SPI_SILABS_EUSART_DMA`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_SILABS_EUSART_DMA)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_SILABS_SIWX91X_GSPI"></a>

## 173.70 `CONFIG_SPI_SILABS_SIWX91X_GSPI`

**提示（Prompt）**：Silabs GSPI SPI 主控制器（Primary Controller）驱动

**说明（Help）**

为 Silabs SiWx91x 片上系统（SoC）系列启用 GSPI SPI 主控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_GSPI_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_SPI
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

**定义位置（Location）**：[`drivers/spi/Kconfig.silabs_siwx91x_gspi:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.silabs_siwx91x_gspi#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_SILABS_SIWX91X_GSPI_DMA_DESCR_COUNT"></a>

## 173.71 `CONFIG_SPI_SILABS_SIWX91X_GSPI_DMA_DESCR_COUNT`

**提示（Prompt）**：每个通道的最大 DMA 描述符（Descriptor）数量

**说明（Help）**

事务中的每个 SPI 缓冲区需要一个描述符（Descriptor），另需一个描述符用于填充（Padding）。设为 0 可禁用 DMA 支持。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_SILABS_SIWX91X_GSPI && CONFIG_SPI
```

**默认值（Defaults）**

```text
3 if CONFIG_DMA
0
```

**定义位置（Location）**：[`drivers/spi/Kconfig.silabs_siwx91x_gspi:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.silabs_siwx91x_gspi#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Silabs GSPI SPI 主控制器（Primary Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_SILABS_SIWX91X_GSPI`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_SILABS_SIWX91X_GSPI)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_SPI_SILABS_USART"></a>

## 173.72 `CONFIG_SPI_SILABS_USART`

**提示（Prompt）**：Silabs USART SPI 控制器驱动

**说明（Help）**

启用 USART SPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_USART_SPI_ENABLED && CONFIG_GPIO && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_GECKO_USART if CONFIG_SOC_FAMILY_SILABS_S0 || CONFIG_SOC_FAMILY_SILABS_S1
CONFIG_SILABS_SISDK_USART if CONFIG_SOC_FAMILY_SILABS_S2
CONFIG_CLOCK_CONTROL_SILABS_SERIES if CONFIG_SOC_FAMILY_SILABS_S2
CONFIG_PINCTRL if CONFIG_SOC_FAMILY_SILABS_S2
```

**定义位置（Location）**：[`drivers/spi/Kconfig.silabs_usart:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.silabs_usart#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SILABS_GECKO_USART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_GECKO_USART)、[`CONFIG_SOC_FAMILY_SILABS_S0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S0)、[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SILABS_SISDK_USART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_USART)、[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_CLOCK_CONTROL_SILABS_SERIES`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_SILABS_SERIES)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S0`、`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_FAMILY_SILABS_S2`。

<a id="CONFIG_SPI_SLAVE"></a>

## 173.73 `CONFIG_SPI_SLAVE`

**提示（Prompt）**：外设角色支持（已弃用别名，Deprecated Alias）［已弃用，DEPRECATED］

**说明（Help）**

`SPI_PERIPHERAL` 的已弃用别名，请改用 `SPI_PERIPHERAL`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
CONFIG_SPI_PERIPHERAL
```

**定义位置（Location）**：[`drivers/spi/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)、[`CONFIG_SPI_PERIPHERAL`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_PERIPHERAL)。

<a id="CONFIG_SPI_SMARTBOND"></a>

## 173.74 `CONFIG_SPI_SMARTBOND`

**提示（Prompt）**：Renesas SmartBond™ SPI 驱动

**说明（Help）**

为 Renesas SmartBond™ DA1469x 系列微控制器（MCU）启用 SPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.smartbond:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.smartbond#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_SMARTBOND_DMA"></a>

## 173.75 `CONFIG_SPI_SMARTBOND_DMA`

**提示（Prompt）**：带 DMA 加速的 Renesas SmartBond™ SPI

**说明（Help）**

启用 DMA 引擎以代替中断驱动方式（Interrupt-driven Approach）。此加速仅适用于同步传输（Synchronous Transfers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_SMARTBOND && CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/spi/Kconfig.smartbond:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.smartbond#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas SmartBond™ SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_SMARTBOND`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_SMARTBOND)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_SPI_STATS"></a>

## 173.76 `CONFIG_SPI_STATS`

**提示（Prompt）**：SPI 设备统计（Device Statistics）

**说明（Help）**

启用 SPI 设备统计（Device Statistics）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STATS && CONFIG_SPI
```

**定义位置（Location）**：[`drivers/spi/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STATS)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_STM32"></a>

## 173.77 `CONFIG_SPI_STM32`

**提示（Prompt）**：STM32 MCU SPI 控制器驱动

**说明（Help）**

为 STM32 系列处理器启用 SPI 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_GPIO if n
```

**定义位置（Location）**：[`drivers/spi/Kconfig.stm32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.stm32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_SPI_STM32_BUSY_FLAG_TIMEOUT"></a>

## 173.78 `CONFIG_SPI_STM32_BUSY_FLAG_TIMEOUT`

**提示（Prompt）**：STM32 忙标志变通方案的超时时间，单位为微秒

**说明（Help）**

DMA 传输后等待 SPI 忙标志 `BSY`（Busy）清除的最长时间，单位为微秒。这是针对 STM32F7 和 STM32L4 器件勘误的变通方案（Workaround）：在外设模式（Peripheral Mode）下发送完最后一个字节后，BSY 可能仍保持置位。

驱动轮询 BSY 和 TXE 标志，并在循环迭代之间调用 `k_yield()`。如果标志未在此时间内清除，驱动仍继续执行。在负载较高的系统或较低 SPI 时钟速率下运行时，可增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_STM32_ERRATA_BUSY && CONFIG_SPI_STM32 && CONFIG_SPI
```

**默认值（Defaults）**

```text
10000
```

**定义位置（Location）**：[`drivers/spi/Kconfig.stm32:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.stm32#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → STM32 MCU SPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_STM32_ERRATA_BUSY`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_STM32_ERRATA_BUSY)、[`CONFIG_SPI_STM32`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_STM32)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_STM32_DMA"></a>

## 173.79 `CONFIG_SPI_STM32_DMA`

**提示（Prompt）**：STM32 MCU SPI 直接内存访问（DMA）支持

**说明（Help）**

为在设备树节点中启用了 DMA 通道的 SPI 实例，启用直接内存访问（DMA）模式。可与 `SPI_RTIO` 配置组合，使 SPI 事务同时使用 DMA 和 RTIO。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_STM32 && CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_DMA
CONFIG_CACHE_MANAGEMENT if CONFIG_DCACHE
```

**被选择（Selected by）**

```text
CONFIG_WIFI_ST67W611M1
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/x_nucleo_gfx01m2/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/x_nucleo_gfx01m2/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.stm32:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.stm32#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → STM32 MCU SPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_STM32`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_STM32)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_WIFI_ST67W611M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ST67W611M1)。

<a id="CONFIG_SPI_STM32_ERRATA_BUSY"></a>

## 173.80 `CONFIG_SPI_STM32_ERRATA_BUSY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

处理“从机模式（Slave Mode）下数据传输结束时 BSY 位可能保持高电平”的勘误（Erratum），例如勘误文档 0290 第 2.11.2 节所述问题。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_STM32F7X || CONFIG_SOC_SERIES_STM32L4X) && CONFIG_SPI_STM32 && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.stm32:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.stm32#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → STM32 MCU SPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32L4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L4X)、[`CONFIG_SPI_STM32`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_STM32)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32L4X`。

<a id="CONFIG_SPI_STM32_INTERRUPT"></a>

## 173.81 `CONFIG_SPI_STM32_INTERRUPT`

**提示（Prompt）**：STM32 MCU SPI 中断支持（Interrupt Support）

**说明（Help）**

为 STM32 系列 SPI 驱动启用中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_STM32 && CONFIG_SPI
```

**默认值（Defaults）**

```text
y if CONFIG_SPI_RTIO
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/x_nucleo_gfx01m2/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/x_nucleo_gfx01m2/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/x_nucleo_wb05kn1/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/x_nucleo_wb05kn1/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/x_nucleo_wba25a1/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/x_nucleo_wba25a1/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.stm32:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.stm32#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → STM32 MCU SPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_STM32`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_STM32)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_SPI_RTIO`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RTIO)。

<a id="CONFIG_SPI_STM32_RTIO_CQ_SIZE"></a>

## 173.82 `CONFIG_SPI_STM32_RTIO_CQ_SIZE`

**提示（Prompt）**：可用完成队列条目（Completion Queue Entries）数量

**说明（Help）**

SPI 使用实时输入输出（RTIO）时，每个驱动都持有一个上下文，通过其阻塞式 API 调用执行 SPI 事务。使用等长缓冲区的普通 SPI 操作时，此队列的深度至少应容纳所使用的最长 `spi_buf_set` 集合。发送／接收 SPI 缓冲区集合的长度并不总是相等时，可能需要稍大的队列深度，因为它们会被转换为普通收发操作（Transceives）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RTIO && CONFIG_SPI_STM32 && CONFIG_SPI
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/spi/Kconfig.stm32:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.stm32#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → STM32 MCU SPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_RTIO`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RTIO)、[`CONFIG_SPI_STM32`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_STM32)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_STM32_RTIO_SQ_SIZE"></a>

## 173.83 `CONFIG_SPI_STM32_RTIO_SQ_SIZE`

**提示（Prompt）**：可用提交队列条目（Submission Queue Entries）数量

**说明（Help）**

SPI 使用实时输入输出（RTIO）时，每个驱动都持有一个上下文，通过其阻塞式 API 调用执行 SPI 事务。使用等长缓冲区的普通 SPI 操作时，此队列的深度至少应容纳所使用的最长 `spi_buf_set` 集合。发送／接收 SPI 缓冲区集合的长度并不总是相等时，可能需要稍大的队列深度，因为它们会被转换为普通收发操作（Transceives）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_RTIO && CONFIG_SPI_STM32 && CONFIG_SPI
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/spi/Kconfig.stm32:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.stm32#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → STM32 MCU SPI 控制器驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_RTIO`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RTIO)、[`CONFIG_SPI_STM32`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_STM32)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_SY1XX"></a>

## 173.84 `CONFIG_SPI_SY1XX`

**提示（Prompt）**：Sensry SY1xx SPI 驱动

**说明（Help）**

Sensry SY1xx 系列 SPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SENSRY_SY1XX_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.sy1xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.sy1xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_SY1XX_BUFFER_SIZE"></a>

## 173.85 `CONFIG_SPI_SY1XX_BUFFER_SIZE`

**提示（Prompt）**：SY1XX SPI 缓冲区大小

**说明（Help）**

SY1XX SPI 驱动用于分块传输（Chunked Transfers）的默认缓冲区大小，单位为字节。必须是 4 的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_SY1XX && CONFIG_SPI
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`drivers/spi/Kconfig.sy1xx:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.sy1xx#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Sensry SY1xx SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_SY1XX`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_SY1XX)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_TELINK_B91"></a>

## 173.86 `CONFIG_SPI_TELINK_B91`

**提示（Prompt）**：Telink Semiconductor B91 SPI 驱动

**说明（Help）**

启用 Telink B91 SPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TELINK_B91_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/spi/Kconfig.b91:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.b91#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_USE_HW_SS"></a>

## 173.87 `CONFIG_SPI_USE_HW_SS`

原库同名定义共 2 条；本项为数据库第 18380 条记录，各定义分别保留。

**提示（Prompt）**：RA MCU SPI 硬件外设选择（Hardware Peripheral Select）支持

**说明（Help）**

使用硬件外设选择（Hardware Peripheral Select）代替软件外设选择（Software Peripheral Select）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!(CONFIG_SOC_SERIES_RA2A1 || CONFIG_SOC_SERIES_RA2L1 || CONFIG_SOC_SERIES_RA4M1) && CONFIG_SPI_RENESAS_RA && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_ra:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_ra#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → Renesas RA SPI

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RA2A1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2A1)、[`CONFIG_SOC_SERIES_RA2L1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA2L1)、[`CONFIG_SOC_SERIES_RA4M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RA4M1)、[`CONFIG_SPI_RENESAS_RA`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RA)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RA2L1`。

<a id="CONFIG_SPI_USE_HW_SS--record-18381"></a>

## 173.88 `CONFIG_SPI_USE_HW_SS`

原库同名定义共 2 条；本项为数据库第 18381 条记录，各定义分别保留。

**提示（Prompt）**：RZ SPI 硬件外设选择（Hardware Peripheral Select）支持

**说明（Help）**

使用硬件外设选择（Hardware Peripheral Select）代替软件外设选择（Software Peripheral Select）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SPI_RENESAS_RZ || CONFIG_SPI_RENESAS_RZ_SPI_B) && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.renesas_rz:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.renesas_rz#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_RENESAS_RZ`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ)、[`CONFIG_SPI_RENESAS_RZ_SPI_B`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_RENESAS_RZ_SPI_B)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_VIRTIO"></a>

## 173.89 `CONFIG_SPI_VIRTIO`

**提示（Prompt）**：VIRTIO SPI 驱动

**说明（Help）**

启用 VIRTIO SPI 设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_VIRTIO_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_VIRTIO
```

**定义位置（Location）**：[`drivers/spi/Kconfig.virtio:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.virtio#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_VIRTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIRTIO)。

<a id="CONFIG_SPI_WCH"></a>

## 173.90 `CONFIG_SPI_WCH`

**提示（Prompt）**：WCH SPI 控制器（Controller）

**说明（Help）**

启用 CH32 系列上的 SPI 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_SPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.wch:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.wch#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_XEC_QMSPI"></a>

## 173.91 `CONFIG_SPI_XEC_QMSPI`

**提示（Prompt）**：Microchip MEC15xx XEC QMSPI 驱动

**说明（Help）**

启用 Microchip MEC15xx XEC QMSPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_QMSPI_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA if CONFIG_SPI_ASYNC
```

**定义位置（Location）**：[`drivers/spi/Kconfig.xec_qmspi:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.xec_qmspi#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_SPI_ASYNC`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI_ASYNC)。

<a id="CONFIG_SPI_XEC_QMSPI_LDMA"></a>

## 173.92 `CONFIG_SPI_XEC_QMSPI_LDMA`

**提示（Prompt）**：Microchip XEC MEC17xx QMSPI 本地 DMA（LDMA）驱动

**说明（Help）**

启用带本地直接内存访问（Local DMA）的 Microchip MEC17xx QMSPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MICROCHIP_XEC_QMSPI_LDMA_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/spi/Kconfig.xec_qmspi:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.xec_qmspi#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_XLNX_AXI_QUADSPI"></a>

## 173.93 `CONFIG_SPI_XLNX_AXI_QUADSPI`

**提示（Prompt）**：Xilinx AXI Quad SPI 驱动

**说明（Help）**

启用 Xilinx AXI Quad SPI v3.2 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_XPS_SPI_2_00_A_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
```

**定义位置（Location）**：[`drivers/spi/Kconfig.xlnx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.xlnx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_SPI_XLNX_ZYNQMP_GQSPI"></a>

## 173.94 `CONFIG_SPI_XLNX_ZYNQMP_GQSPI`

**提示（Prompt）**：Xilinx ZynqMP GQSPI 驱动

**说明（Help）**

启用 Xilinx ZynqMP 通用四线 SPI（Generic Quad SPI）驱动。它通常用于 QSPI 闪存设备，也可用于其他 SPI 设备。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_ZYNQMP_QSPI_1_0_ENABLED && CONFIG_SPI
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
```

**定义位置（Location）**：[`drivers/spi/Kconfig.xlnx_zynqmp_gqspi:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.xlnx_zynqmp_gqspi#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_SPI_XMC4XXX"></a>

## 173.95 `CONFIG_SPI_XMC4XXX`

**提示（Prompt）**：XMC4XX SPI 驱动

**说明（Help）**

启用 XMC4XXX SPI 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_XMC4XXX_SPI_ENABLED && CONFIG_SPI
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

**定义位置（Location）**：[`drivers/spi/Kconfig.xmc4xxx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.xmc4xxx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_SPI_XMC4XXX_DMA"></a>

## 173.96 `CONFIG_SPI_XMC4XXX_DMA`

**提示（Prompt）**：XMC4XXX SPI 直接内存访问（DMA）支持

**说明（Help）**

为 SPI 传输启用直接内存访问（DMA）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_XMC4XXX && CONFIG_SPI
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/spi/Kconfig.xmc4xxx:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.xmc4xxx#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → XMC4XX SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_XMC4XXX`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_XMC4XXX)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_SPI_XMC4XXX_DMA_TIMEOUT_MSEC"></a>

## 173.97 `CONFIG_SPI_XMC4XXX_DMA_TIMEOUT_MSEC`

**提示（Prompt）**：使用 DMA 时 SPI 事务完成的超时时间，单位为毫秒

**说明（Help）**

设置使用 DMA 时等待 SPI 事务完成的超时时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_XMC4XXX_DMA && CONFIG_SPI_XMC4XXX && CONFIG_SPI
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/spi/Kconfig.xmc4xxx:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.xmc4xxx#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → XMC4XX SPI 驱动 → XMC4XXX SPI 直接内存访问（DMA）支持

**配置项引用（Symbol References）**：[`CONFIG_SPI_XMC4XXX_DMA`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_XMC4XXX_DMA)、[`CONFIG_SPI_XMC4XXX`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_XMC4XXX)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_SPI_XMC4XXX_INTERRUPT"></a>

## 173.98 `CONFIG_SPI_XMC4XXX_INTERRUPT`

**提示（Prompt）**：XMC4XXX SPI 中断模式（Interrupt Mode）

**说明（Help）**

启用 XMC4XXX SPI 驱动的中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPI_XMC4XXX && CONFIG_SPI
```

**定义位置（Location）**：[`drivers/spi/Kconfig.xmc4xxx:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/spi/Kconfig.xmc4xxx#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行外设接口（Serial Peripheral Interface，SPI）总线驱动 → XMC4XX SPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_SPI_XMC4XXX`](P173_drivers_spi_配置项参考_2.md#CONFIG_SPI_XMC4XXX)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<!-- kconfig-navigation -->

[上一章](P172_drivers_spi_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P174_drivers_stepper_配置项参考.md)
