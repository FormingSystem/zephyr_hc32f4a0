---
id: learning.zephyr-docs.kconfig-reference.page-59
title: "`drivers/cache`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第59章\_`drivers/cache`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/cache` 的 17 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CACHE"></a>

## 59.1 `CONFIG_CACHE`

**提示（Prompt）**：外部缓存控制器驱动（External Cache Controller Drivers）

**说明（Help）**

启用外部缓存控制器（External Cache Controller）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y if CONFIG_CACHE_MANAGEMENT
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_AST10X0
```

**定义位置（Location）**：[`drivers/cache/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/cache/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_SOC_SERIES_AST10X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AST10X0)。

<a id="CONFIG_CACHE_ANDES"></a>

## 59.2 `CONFIG_CACHE_ANDES`

**提示（Prompt）**：Andes 外部缓存驱动（External Cache Driver）

**说明（Help）**

启用基于 Andes V5 内核的片上系统（SoC）的缓存（Cache）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_ANDESCORE_V5_ENABLED && CONFIG_CACHE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CACHE_HAS_DRIVER
CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT
CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT
```

**定义位置（Location）**：[`drivers/cache/Kconfig.andes:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/cache/Kconfig.andes#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CACHE`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE)、[`CONFIG_CACHE_HAS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_HAS_DRIVER)、[`CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT)、[`CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CACHE_HAS_DRIVER`。

<a id="CONFIG_CACHE_ANDES_INIT_PRIORITY"></a>

## 59.3 `CONFIG_CACHE_ANDES_INIT_PRIORITY`

**提示（Prompt）**：Andes 缓存驱动初始化优先级（Init Priority）

**说明（Help）**

控制缓存（Cache）初始化优先级。数值越小，初始化越早。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_ANDES && CONFIG_CACHE
```

**默认值（Defaults）**

```text
60
```

**定义位置（Location）**：[`drivers/cache/Kconfig.andes:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/cache/Kconfig.andes#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers） → Andes 外部缓存驱动（External Cache Driver）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_ANDES`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE_ANDES)、[`CONFIG_CACHE`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE)。

<a id="CONFIG_CACHE_ASPEED"></a>

## 59.4 `CONFIG_CACHE_ASPEED`

**提示（Prompt）**：ASPEED 外部缓存驱动（External Cache Driver）

**说明（Help）**

启用 ASPEED AST10X0 系列片上系统（SoC）的缓存（Cache）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_AST10X0 && CONFIG_SYSCON && CONFIG_CACHE
```

**主动选择（Selects）**

```text
CONFIG_CACHE_HAS_DRIVER
CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT
CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT
```

**被选择（Selected by）**

```text
CONFIG_SOC_SERIES_AST10X0
```

**定义位置（Location）**：[`drivers/cache/Kconfig.aspeed:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/cache/Kconfig.aspeed#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_AST10X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_AST10X0)、[`CONFIG_SYSCON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSCON)、[`CONFIG_CACHE`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE)、[`CONFIG_CACHE_HAS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_HAS_DRIVER)、[`CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE_LINE_SIZE_DETECT_SUPPORT)、[`CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ICACHE_LINE_SIZE_DETECT_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CACHE_HAS_DRIVER`。

<a id="CONFIG_CACHE_BFLB_L1C"></a>

## 59.5 `CONFIG_CACHE_BFLB_L1C`

**提示（Prompt）**：博流 L1C 缓存系统驱动（Bouffalolab Cache System Driver）

**说明（Help）**

启用博流（Bouffalolab）L1C 缓存系统（Cache System）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_L1C_ENABLED && CONFIG_CACHE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CACHE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/cache/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/cache/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CACHE`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE)、[`CONFIG_CACHE_HAS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CACHE_HAS_DRIVER`。

<a id="CONFIG_CACHE_ESP32"></a>

## 59.6 `CONFIG_CACHE_ESP32`

**提示（Prompt）**：乐鑫 ESP32 缓存驱动（Espressif Cache Driver）

**说明（Help）**

为具有回写式数据缓存（Writeback Data Cache）的乐鑫片上系统（Espressif SoC），即 ESP32-S2、S3、C5，启用数据缓存驱动，用于保持伪静态 RAM（PSRAM）与 DMA 缓冲区的一致性（Coherency）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_CACHE_MANAGEMENT && CONFIG_CACHE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CACHE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/cache/Kconfig.esp32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/cache/Kconfig.esp32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_CACHE`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE)、[`CONFIG_CACHE_HAS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`、`CONFIG_CACHE_HAS_DRIVER`。

<a id="CONFIG_CACHE_MAX32"></a>

## 59.7 `CONFIG_CACHE_MAX32`

**提示（Prompt）**：ADI MAX32 缓存控制器驱动（Cache Controller Driver）

**说明（Help）**

启用 ADI MAX32 缓存控制器（Cache Controller）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_MAX32 && CONFIG_CACHE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CACHE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/cache/Kconfig.max32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/cache/Kconfig.max32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)、[`CONFIG_CACHE`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE)、[`CONFIG_CACHE_HAS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32`、`CONFIG_CACHE_HAS_DRIVER`。

<a id="CONFIG_CACHE_NRF_CACHE"></a>

## 59.8 `CONFIG_CACHE_NRF_CACHE`

**提示（Prompt）**：nRF 缓存驱动（Cache Driver）

**说明（Help）**

启用 nRF 缓存（Cache）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_NRFX && CONFIG_CACHE_MANAGEMENT && CONFIG_CACHE
```

**主动选择（Selects）**

```text
CONFIG_CACHE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/cache/Kconfig.nrf:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/cache/Kconfig.nrf#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_NRFX)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_CACHE`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE)、[`CONFIG_CACHE_HAS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_NRFX`、`CONFIG_CACHE_HAS_DRIVER`。

<a id="CONFIG_CACHE_NRF_PATCH_LINEADDR"></a>

## 59.9 `CONFIG_CACHE_NRF_PATCH_LINEADDR`

**提示（Prompt）**：修补行地址（Patch lineaddr）

**说明（Help）**

在 TrustZone 安全构建（Secure Build）中，手动设置 `LINEADDR` 的第 28 位。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DCACHE && CONFIG_CACHE
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_NRF54H20
```

**定义位置（Location）**：[`drivers/cache/Kconfig.nrf:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/cache/Kconfig.nrf#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_CACHE`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE)、[`CONFIG_SOC_NRF54H20`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54H20)。

<a id="CONFIG_CACHE_NXP_LMEM_CACHE"></a>

## 59.10 `CONFIG_CACHE_NXP_LMEM_CACHE`

**提示（Prompt）**：恩智浦 LMEM 缓存驱动（NXP Cache Driver）

**说明（Help）**

启用恩智浦（NXP）片上系统（SoC）的 LMEM 缓存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX_LMEM_CACHE && CONFIG_CACHE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CACHE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/cache/Kconfig.nxp_lmem_cache:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/cache/Kconfig.nxp_lmem_cache#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX_LMEM_CACHE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX_LMEM_CACHE)、[`CONFIG_CACHE`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE)、[`CONFIG_CACHE_HAS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CACHE_HAS_DRIVER`。

<a id="CONFIG_CACHE_NXP_MCM_LPCAC"></a>

## 59.11 `CONFIG_CACHE_NXP_MCM_LPCAC`

**提示（Prompt）**：恩智浦 MCM LPCAC 代码缓存驱动（NXP Code Cache Driver）

**说明（Help）**

为以下恩智浦（NXP）片上系统（SoC）启用 LPCAC 代码缓存（Code Cache）驱动：其低功耗缓存控制器（Low Power Cache Controller）通过杂项控制模块（Miscellaneous Control Module，MCM）的 `CPCR2` 寄存器配置，例如 MCX W7x、KW45、KW47。这区别于通过 `SYSCON LPCAC_CTRL` 寄存器配置、由 `CACHE_NXP_SYSCON_LPCAC` 处理的控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX_MCM_LPCAC && CONFIG_CACHE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CACHE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/cache/Kconfig.nxp_mcm_lpcac:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/cache/Kconfig.nxp_mcm_lpcac#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX_MCM_LPCAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX_MCM_LPCAC)、[`CONFIG_CACHE`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE)、[`CONFIG_CACHE_HAS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CACHE_HAS_DRIVER`。

<a id="CONFIG_CACHE_NXP_SYSCON_LPCAC"></a>

## 59.12 `CONFIG_CACHE_NXP_SYSCON_LPCAC`

**提示（Prompt）**：恩智浦 SYSCON LPCAC 控制器外部缓存驱动（NXP External Cache Driver）

**说明（Help）**

启用恩智浦（NXP）片上系统（SoC）的 SYSCON LPCAC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX_SYSCON_LPCAC && CONFIG_CACHE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CACHE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/cache/Kconfig.nxp_syscon_lpcac:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/cache/Kconfig.nxp_syscon_lpcac#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX_SYSCON_LPCAC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX_SYSCON_LPCAC)、[`CONFIG_CACHE`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE)、[`CONFIG_CACHE_HAS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CACHE_HAS_DRIVER`。

<a id="CONFIG_CACHE_NXP_XCACHE"></a>

## 59.13 `CONFIG_CACHE_NXP_XCACHE`

**提示（Prompt）**：恩智浦 XCACHE 控制器外部缓存驱动（NXP External Cache Driver）

**说明（Help）**

启用恩智浦（NXP）片上系统（SoC）的 XCACHE 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_MCUX_XCACHE && CONFIG_CACHE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CACHE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/cache/Kconfig.nxp_xcache:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/cache/Kconfig.nxp_xcache#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX_XCACHE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX_XCACHE)、[`CONFIG_CACHE`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE)、[`CONFIG_CACHE_HAS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CACHE_HAS_DRIVER`。

<a id="CONFIG_CACHE_SILABS_SIWX91X"></a>

## 59.14 `CONFIG_CACHE_SILABS_SIWX91X`

**提示（Prompt）**：Silicon Labs SiWx91x 指令缓存驱动（Instruction Cache Driver）

**说明（Help）**

启用 SiWx91x 外部 AHB 指令缓存（Instruction Cache）支持。SiWx91x 为 QSPI 闪存提供只读指令缓存，没有数据缓存（Data Cache）。通过切换缓存时钟门控（Clock Gate）执行全缓存失效（Full Invalidation），不支持逐行或范围失效（Per-Line / Range Invalidation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_SILABS_SIWX91X && CONFIG_CACHE_MANAGEMENT && CONFIG_CACHE
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CACHE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/cache/Kconfig.siwx91x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/cache/Kconfig.siwx91x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_SILABS_SIWX91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIWX91X)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_CACHE`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE)、[`CONFIG_CACHE_HAS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_SIWX91X`、`CONFIG_CACHE_HAS_DRIVER`。

<a id="CONFIG_CACHE_STM32"></a>

## 59.15 `CONFIG_CACHE_STM32`

**提示（Prompt）**：STM32 缓存驱动（Cache Driver）

**说明（Help）**

启用部分 STM32 芯片所具有的指令缓存／数据缓存（ICACHE / DCACHE）外设支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_STM32 && CONFIG_CACHE_MANAGEMENT && CONFIG_CACHE
```

**主动选择（Selects）**

```text
CONFIG_CACHE_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/cache/Kconfig.stm32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/cache/Kconfig.stm32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_CACHE`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE)、[`CONFIG_CACHE_HAS_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_HAS_DRIVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`、`CONFIG_CACHE_HAS_DRIVER`。

<a id="CONFIG_CACHE_STM32_ICACHE_DIRECT_MAPPING"></a>

## 59.16 `CONFIG_CACHE_STM32_ICACHE_DIRECT_MAPPING`

**提示（Prompt）**：ICACHE 使用单路关联映射（1-Way Associative Mapping）

**说明（Help）**

让指令缓存（ICACHE）采用直接映射（Direct Mapping），即单路关联模式，替代默认的 n 路组相联缓存（n-Way Associative Cache）模式。此选项降低功耗，但会略微降低缓存性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_STM32 && CONFIG_CACHE
```

**默认值（Defaults）**

```text
n if CONFIG_SOC_SERIES_STM32L5X
y
```

**定义位置（Location）**：[`drivers/cache/Kconfig.stm32:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/cache/Kconfig.stm32#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers） → STM32 缓存驱动（Cache Driver）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_STM32`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE_STM32)、[`CONFIG_CACHE`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE)、[`CONFIG_SOC_SERIES_STM32L5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L5X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32L5X`。

<a id="CONFIG_L2C_INCLUSIVE_POLICY"></a>

## 59.17 `CONFIG_L2C_INCLUSIVE_POLICY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

当二级缓存（L2 Cache）包含一级缓存（L1 Cache）的内容，即采用包含式缓存（Inclusive Cache）时，CPU 只需对 L2 执行操作，而不必同时操作 L1 和 L2。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_L2C_ENABLED && CONFIG_CACHE_ANDES && CONFIG_CACHE
```

**定义位置（Location）**：[`drivers/cache/Kconfig.andes:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/cache/Kconfig.andes#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 外部缓存控制器驱动（External Cache Controller Drivers） → Andes 外部缓存驱动（External Cache Driver）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_ANDES`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE_ANDES)、[`CONFIG_CACHE`](P059_drivers_cache_配置项参考.md#CONFIG_CACHE)。

<!-- kconfig-navigation -->

[上一章](P058_drivers_buzzer_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P060_drivers_can_配置项参考.md)
