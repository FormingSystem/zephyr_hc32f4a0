---
id: learning.zephyr-docs.kconfig-reference.page-93
title: "`drivers/flash`配置项参考（2/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第93章\_`drivers/flash`配置项参考（2/3）

本章翻译官方 Kconfig 数据库中 `drivers/flash` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_FLASH_NXP_S32_QSPI_LAYOUT_PAGE_SIZE"></a>

## 93.1 `CONFIG_FLASH_NXP_S32_QSPI_LAYOUT_PAGE_SIZE`

**提示（Prompt）**：`FLASH_LAYOUT` 功能使用的页大小（Page Size）

**说明（Help）**

使用 `CONFIG_FLASH_PAGE_LAYOUT` 时，此驱动支持对应 API。对于 NOR 闪存，默认页大小（Page Size）等于扇区大小（Sector Size）`4096`。其他选项可包括 32 KB 擦除大小 `32768`、块大小（Block Size）`65536`，或扇区大小的任意非零整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_FLASH_NXP_S32_QSPI_NOR || CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH) && CONFIG_FLASH
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nxp_s32_qspi:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nxp_s32_qspi#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_NXP_S32_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_NXP_S32_QSPI_NOR)、[`CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_NXP_S32_QSPI_NOR"></a>

## 93.2 `CONFIG_FLASH_NXP_S32_QSPI_NOR`

**提示（Prompt）**：NXP S32 QSPI NOR 驱动

**说明（Help）**

启用用于连接到 NXP S32 QSPI 总线的 NOR 串行闪存设备（Serial Flash Memory Device）的闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_QSPI_NOR_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MEMC
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_JESD216
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nxp_s32_qspi:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nxp_s32_qspi#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_MEMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_FLASH_NXP_S32_QSPI_SFDP_RUNTIME"></a>

## 93.3 `CONFIG_FLASH_NXP_S32_QSPI_SFDP_RUNTIME`

**提示（Prompt）**：运行时读取闪存参数（Read Flash Parameters at Runtime）

**说明（Help）**

运行时从设备读取闪存设备特征（Flash Device Characteristics）。此选项应能为所有受支持的 JESD216 兼容器件提供功能，但需注意：

- SFDP 表中必须存在四线使能要求位域（Quad Enable Requirements，DW15），才能配置四线模式（Quad Mode）；否则根据器件支持情况，默认使用双线（Dual）或单线（Single）模式。
- SFDP 表中必须存在软复位位域（Soft Reset，DW16），才能在初始化时自动复位设备。
- 硬件抽象层（HAL）尚未实现 `0-X-X` 模式探测（Mode Discovery）。

未选择此项时，驱动使用固定配置，假定页大小为 256 字节，并支持 4 KiB、32 KiB 和 64 KiB 擦除指令。必须在设备树（Devicetree）节点中设置器件大小和 `jedec-id` 属性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_NXP_S32_QSPI_NOR && (CONFIG_FLASH_NXP_S32_QSPI_NOR || CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH) && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nxp_s32_qspi:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nxp_s32_qspi#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_NXP_S32_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_NXP_S32_QSPI_NOR)、[`CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_NXP_S32_QSPI_VERIFY_ERASE"></a>

## 93.4 `CONFIG_FLASH_NXP_S32_QSPI_VERIFY_ERASE`

**提示（Prompt）**：擦除后验证存储器（Verify After Erase）

**说明（Help）**

擦除后验证存储器内容（Memory Contents）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_FLASH_NXP_S32_QSPI_NOR || CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH) && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nxp_s32_qspi:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nxp_s32_qspi#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_NXP_S32_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_NXP_S32_QSPI_NOR)、[`CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_NXP_S32_QSPI_VERIFY_WRITE"></a>

## 93.5 `CONFIG_FLASH_NXP_S32_QSPI_VERIFY_WRITE`

**提示（Prompt）**：写入后验证存储器（Verify After Write）

**说明（Help）**

写入后验证存储器内容（Memory Contents）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_FLASH_NXP_S32_QSPI_NOR || CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH) && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nxp_s32_qspi:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nxp_s32_qspi#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_NXP_S32_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_NXP_S32_QSPI_NOR)、[`CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_NXP_S32_QSPI_HYPERFLASH)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_NXP_S32_XSPI_HYPERRAM"></a>

## 93.6 `CONFIG_FLASH_NXP_S32_XSPI_HYPERRAM`

**提示（Prompt）**：NXP S32 XSPI HYPERRAM 驱动

**说明（Help）**

启用用于连接到 NXP S32 XSPI 总线的 HyperRAM 存储器设备（Memory Device）的闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_XSPI_HYPERRAM_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MEMC
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nxp_s32_xspi:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nxp_s32_xspi#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_MEMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_FLASH_NXP_S32_XSPI_LAYOUT_PAGE_SIZE"></a>

## 93.7 `CONFIG_FLASH_NXP_S32_XSPI_LAYOUT_PAGE_SIZE`

**提示（Prompt）**：`FLASH_LAYOUT` 功能使用的页大小（Page Size）

**说明（Help）**

使用 `CONFIG_FLASH_PAGE_LAYOUT` 时，此驱动支持对应 API。默认页大小（Page Size）设为 4096 字节。HyperRAM 是易失性存储器（Volatile Memory），不需要像 NOR 闪存那样执行擦除操作；此页大小仅用于报告内存布局（Memory Layout）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_NXP_S32_XSPI_HYPERRAM && CONFIG_FLASH
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nxp_s32_xspi:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nxp_s32_xspi#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → NXP S32 XSPI HYPERRAM 驱动

**配置项引用（Symbol References）**：[`CONFIG_FLASH_NXP_S32_XSPI_HYPERRAM`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_NXP_S32_XSPI_HYPERRAM)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_PAGE_LAYOUT"></a>

## 93.8 `CONFIG_FLASH_PAGE_LAYOUT`

**提示（Prompt）**：用于获取页布局的 API（Page Layout API）

**说明（Help）**

启用用于获取闪存页布局（Flash Memory Page Layout）的 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT && CONFIG_FLASH
```

**默认值（Defaults）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
```

**被选择（Selected by）**

```text
CONFIG_SOC_FLASH_RENESAS_RA_HP
CONFIG_SOC_FLASH_RENESAS_RA_LP
CONFIG_SOC_FLASH_RENESAS_RA_MRAM
```

**定义位置（Location）**：[`drivers/flash/Kconfig:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_SOC_FLASH_RENESAS_RA_HP`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RA_HP)、[`CONFIG_SOC_FLASH_RENESAS_RA_LP`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RA_LP)、[`CONFIG_SOC_FLASH_RENESAS_RA_MRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RA_MRAM)。

<a id="CONFIG_FLASH_RENESAS_RA_HP_BGO"></a>

## 93.9 `CONFIG_FLASH_RENESAS_RA_HP_BGO`

**提示（Prompt）**：后台操作功能（Background Operations）

**说明（Help）**

启用后台操作（Background Operations，BGO）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_RENESAS_RA_HP && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.renesas_ra:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.renesas_ra#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → RA 高性能闪存（Flash HP）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_RENESAS_RA_HP`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RA_HP)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_RENESAS_RA_HP_CHECK_BEFORE_READING"></a>

## 93.10 `CONFIG_FLASH_RENESAS_RA_HP_CHECK_BEFORE_READING`

**提示（Prompt）**：读取区域之前先验证（Verify Before Reading）

**说明（Help）**

读取区域之前，先执行空白检查闪存命令（Blank Check Flash Command）。此功能可防止错误读取。从已经擦除但尚未编程的数据闪存（Data Flash）区域读取的值是未定义的（Undefined）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_RENESAS_RA_HP && CONFIG_FLASH
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.renesas_ra:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.renesas_ra#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → RA 高性能闪存（Flash HP）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_RENESAS_RA_HP`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RA_HP)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_RENESAS_RA_LP_BGO"></a>

## 93.11 `CONFIG_FLASH_RENESAS_RA_LP_BGO`

**提示（Prompt）**：后台操作功能（Background Operations）

**说明（Help）**

启用后台操作（Background Operations，BGO）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_RENESAS_RA_LP && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.renesas_ra:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.renesas_ra#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → RA 低功耗闪存（Flash LP）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_RENESAS_RA_LP`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RA_LP)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_RENESAS_RA_OSPI_B"></a>

## 93.12 `CONFIG_FLASH_RENESAS_RA_OSPI_B`

**提示（Prompt）**：瑞萨（Renesas）RA 八线 SPI 驱动（Octal-SPI Driver）

**说明（Help）**

为 RA 系列启用八线 SPI（Octal-SPI）NOR 闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_OSPI_B_NOR_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_USE_RA_FSP_OSPI_B_NOR_FLASH
CONFIG_FLASH_JESD216
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/flash/Kconfig.renesas_ra_ospi:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.renesas_ra_ospi#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_USE_RA_FSP_OSPI_B_NOR_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_OSPI_B_NOR_FLASH)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_FLASH_RENESAS_RA_QSPI"></a>

## 93.13 `CONFIG_FLASH_RENESAS_RA_QSPI`

**提示（Prompt）**：RA 四线 SPI 驱动（Quad-SPI Driver）

**说明（Help）**

为 RA 系列启用四线 SPI（Quad-SPI）NOR 闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_QSPI_NOR_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_USE_RA_FSP_QSPI_NOR_FLASH
CONFIG_FLASH_HAS_EX_OP
CONFIG_FLASH_JESD216
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/flash/Kconfig.renesas_ra_qspi:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.renesas_ra_qspi#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_USE_RA_FSP_QSPI_NOR_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_QSPI_NOR_FLASH)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_FLASH_RENESAS_RX_BGO_ENABLED"></a>

## 93.14 `CONFIG_FLASH_RENESAS_RX_BGO_ENABLED`

**提示（Prompt）**：RX 闪存后台操作功能（Flash BGO）

**说明（Help）**

瑞萨（Renesas）RX 系列的闪存后台操作（Background Operation，BGO）功能。它允许闪存驱动在 CPU 执行其他任务时进行擦除和写入等后台操作。此功能仅适用于数据闪存区域（Data Flash Region）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_RENESAS_RX && CONFIG_FLASH
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.renesas_rx:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.renesas_rx#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → RX 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_RENESAS_RX`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RX)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_RENESAS_RZA2M_QSPI_SPIBSC"></a>

## 93.15 `CONFIG_FLASH_RENESAS_RZA2M_QSPI_SPIBSC`

**提示（Prompt）**：瑞萨（Renesas）RZA2M 四线 SPI SPIBSC 驱动（Quad-SPI SPIBSC Driver）

**说明（Help）**

为 RZA2M 系列启用四线 SPI（Quad-SPI）SPIBSC NOR 闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZA2M_QSPI_SPIBSC_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_JESD216
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/flash/Kconfig.renesas_rz_qspi:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.renesas_rz_qspi#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_FLASH_RENESAS_RZ_MIRROR_OFFSET"></a>

## 93.16 `CONFIG_FLASH_RENESAS_RZ_MIRROR_OFFSET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

闪存中镜像区域偏移（Mirror Area Offset）

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH
```

**默认值（Defaults）**

```text
0x0 if CONFIG_SOC_SERIES_RZA3UL
0x20000000 if CONFIG_SOC_SERIES_RZT2M || CONFIG_SOC_SERIES_RZN2L || CONFIG_SOC_SERIES_RZT2L
```

**定义位置（Location）**：[`drivers/flash/Kconfig.renesas_rz_qspi:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.renesas_rz_qspi#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_SOC_SERIES_RZA3UL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZA3UL)、[`CONFIG_SOC_SERIES_RZT2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2M)、[`CONFIG_SOC_SERIES_RZN2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZN2L)、[`CONFIG_SOC_SERIES_RZT2L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RZT2L)。

<a id="CONFIG_FLASH_RENESAS_RZ_QSPI_SPIBSC"></a>

## 93.17 `CONFIG_FLASH_RENESAS_RZ_QSPI_SPIBSC`

**提示（Prompt）**：瑞萨（Renesas）RZ 四线 SPI SPIBSC 驱动（Quad-SPI SPIBSC Driver）

**说明（Help）**

为 RZ 系列启用四线 SPI（Quad-SPI）SPIBSC NOR 闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_QSPI_SPIBSC_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_USE_RZ_FSP_QSPI_SPIBSC
CONFIG_FLASH_JESD216
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/flash/Kconfig.renesas_rz_qspi:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.renesas_rz_qspi#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_USE_RZ_FSP_QSPI_SPIBSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_QSPI_SPIBSC)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_FLASH_RENESAS_RZ_QSPI_XSPI"></a>

## 93.18 `CONFIG_FLASH_RENESAS_RZ_QSPI_XSPI`

**提示（Prompt）**：瑞萨（Renesas）RZ 四线 SPI XSPI 驱动（Quad-SPI XSPI Driver）

**说明（Help）**

为 RZ 系列启用四线 SPI（Quad-SPI）XSPI NOR 闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_QSPI_XSPI_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_USE_RZ_FSP_QSPI_XSPI
CONFIG_FLASH_JESD216
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/flash/Kconfig.renesas_rz_qspi:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.renesas_rz_qspi#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_USE_RZ_FSP_QSPI_XSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_QSPI_XSPI)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_FLASH_RPI_PICO"></a>

## 93.19 `CONFIG_FLASH_RPI_PICO`

**提示（Prompt）**：树莓派（Raspberry Pi）Pico 闪存驱动（Flash Driver）

**说明（Help）**

启用树莓派（Raspberry Pi）Pico 闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_PICO_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_PICOSDK_USE_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.rpi_pico:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.rpi_pico#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_PICOSDK_USE_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOSDK_USE_FLASH)。

<a id="CONFIG_FLASH_RPI_PICO_READ_UNTRANSLATED"></a>

## 93.20 `CONFIG_FLASH_RPI_PICO_READ_UNTRANSLATED`

**提示（Prompt）**：使用未转换窗口（Untranslated Window）读取闪存

**说明（Help）**

读取闪存时，绕过原地执行（XIP）缓存与地址转换硬件（Address Translation Hardware）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_RPI_PICO && CONFIG_SOC_SERIES_RP2350 && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.rpi_pico:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.rpi_pico#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 树莓派（Raspberry Pi）Pico 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_RPI_PICO`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_RPI_PICO)、[`CONFIG_SOC_SERIES_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2350)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RP2350`。

<a id="CONFIG_FLASH_S3AXX04"></a>

## 93.21 `CONFIG_FLASH_S3AXX04`

**提示（Prompt）**：Netsol S3Axx04 磁阻式随机存取存储器（MRAM）

**说明（Help）**

为 Netsol S3Axx04 SPI MRAM 启用基于闪存 API（Flash API）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NETSOL_S3AXX04_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.s3axx04:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.s3axx04#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE)。

<a id="CONFIG_FLASH_SEMIHOST"></a>

## 93.22 `CONFIG_FLASH_SEMIHOST`

**提示（Prompt）**：以半主机文件为存储的闪存驱动（Semihost File-Backed Flash Driver）

**说明（Help）**

启用一个以半主机（Semihosting）主机上的文件作为存储的闪存驱动，适用于 QEMU 目标。闪存数据在不同运行之间持久保存在主机文件中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_SEMIHOST_FLASH_ENABLED && CONFIG_SEMIHOST && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.semihost:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.semihost#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SEMIHOST`](P032_arch_common_配置项参考.md#CONFIG_SEMIHOST)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_FLASH_SF32LB_MPI_QSPI_NOR"></a>

## 93.23 `CONFIG_FLASH_SF32LB_MPI_QSPI_NOR`

**提示（Prompt）**：思澈（SiFli）SF32LB MPI QSPI NOR 驱动

**说明（Help）**

启用用于连接到思澈（SiFli）SF32LB MPI 外设的 NOR 串行闪存设备（Serial Flash Memory Device）的闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_MPI_QSPI_NOR_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_FLASH_JESD216
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/flash/Kconfig.sf32lb_mpi_qspi_nor:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.sf32lb_mpi_qspi_nor#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_FLASH_SHELL"></a>

## 93.24 `CONFIG_FLASH_SHELL`

**提示（Prompt）**：闪存命令行（Flash Shell）

**说明（Help）**

启用闪存命令行（Flash Shell），提供测试（Test）、写入（Write）、读取（Read）和擦除（Erase）等闪存相关命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_FLASH_PAGE_LAYOUT && CONFIG_FLASH
```

**主动选择（Selects）**

```text
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`drivers/flash/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_FLASH_PAGE_LAYOUT`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_PAGE_LAYOUT)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<a id="CONFIG_FLASH_SHELL_BUFFER_SIZE"></a>

## 93.25 `CONFIG_FLASH_SHELL_BUFFER_SIZE`

**提示（Prompt）**：闪存命令行缓冲区大小（Shell Buffer Size）

**说明（Help）**

闪存命令所用缓冲区（Buffer）的大小，决定读写测试可以使用的最大大小。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_SHELL && CONFIG_FLASH
```

**默认值（Defaults）**

```text
0x4000 if CONFIG_FLASH_SHELL_TEST_COMMANDS
0x1000
```

**取值范围（Ranges）**

```text
[0x400, 0x1000000]
```

**定义位置（Location）**：[`drivers/flash/Kconfig:142`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig#L142)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存命令行（Flash Shell）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_SHELL`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SHELL)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_SHELL_TEST_COMMANDS`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SHELL_TEST_COMMANDS)。

<a id="CONFIG_FLASH_SHELL_TEST_COMMANDS"></a>

## 93.26 `CONFIG_FLASH_SHELL_TEST_COMMANDS`

**提示（Prompt）**：闪存读写擦除测试命令（Read/Write/Erase Test Commands）

**说明（Help）**

启用额外的闪存命令行（Flash Shell）命令，用于执行读写擦除测试，并输出速度信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_SHELL && CONFIG_FLASH
```

**主动选择（Selects）**

```text
CONFIG_CBPRINTF_FP_SUPPORT
CONFIG_TIMING_FUNCTIONS
```

**定义位置（Location）**：[`drivers/flash/Kconfig:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存命令行（Flash Shell）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_SHELL`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SHELL)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_CBPRINTF_FP_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CBPRINTF_FP_SUPPORT)、[`CONFIG_TIMING_FUNCTIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TIMING_FUNCTIONS)。

<a id="CONFIG_FLASH_SIMULATOR"></a>

## 93.27 `CONFIG_FLASH_SIMULATOR`

**提示（Prompt）**：闪存模拟器（Flash Simulator）

**说明（Help）**

启用闪存模拟器（Flash Simulator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_SIM_FLASH_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
```

**定义位置（Location）**：[`drivers/flash/Kconfig.simulator:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.simulator#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)。

<a id="CONFIG_FLASH_SIMULATOR_CALLBACKS"></a>

## 93.28 `CONFIG_FLASH_SIMULATOR_CALLBACKS`

**提示（Prompt）**：提供回调机制（Callback Mechanism）

**说明（Help）**

选择此项时，实现 `flash_simulator_set_callbacks`，允许改变写入和擦除函数的行为。此选项用于测试模块对存储器中不同写入/擦除（Write/Erase）错误的反应。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_SIMULATOR && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.simulator:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.simulator#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存模拟器（Flash Simulator）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_SIMULATOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_SIMULATOR_DOUBLE_WRITES"></a>

## 93.29 `CONFIG_FLASH_SIMULATOR_DOUBLE_WRITES`

**提示（Prompt）**：允许编程单元（Program Unit）被多次编程

**说明（Help）**

选择此项时，写入尚未擦除的编程单元（Program Unit）会成功；否则返回错误。写操作只能把位从擦除值（Erase Value）改变为相反值。此选项不影响 `FLASH_SIMULATOR_RAMLIKE`。选中 `FLASH_SIMULATOR_EXPLICIT_ERASE` 时，同一位即使被多次写入，也只记录从擦除值到相反值的变化。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_SIMULATOR && CONFIG_FLASH
```

**被选择（Selected by）**

```text
CONFIG_FLASH_SIMULATOR_RAMLIKE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.simulator:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.simulator#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存模拟器（Flash Simulator）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_SIMULATOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_SIMULATOR_RAMLIKE`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR_RAMLIKE)。

<a id="CONFIG_FLASH_SIMULATOR_EXPLICIT_ERASE"></a>

## 93.30 `CONFIG_FLASH_SIMULATOR_EXPLICIT_ERASE`

**提示（Prompt）**：编程－擦除设备（Program-Erase Device）

**说明（Help）**

需要显式擦除（Explicit Erase）、不具备写时擦除（Erase-on-Write）的闪存。此类设备只允许将位从擦除值（Erase Value）改变为相反值，因此写入之前需要先擦除到擦除值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_SIMULATOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.simulator:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.simulator#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存模拟器（Flash Simulator）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_SIMULATOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_FLASH_SIMULATOR_EX_OP"></a>

## 93.31 `CONFIG_FLASH_SIMULATOR_EX_OP`

**提示（Prompt）**：扩展操作 API（Extended Operations API）

**说明（Help）**

闪存扩展操作 API（Flash Extended Operations API）可用于执行非标准操作。例如，模拟 NAND 闪存转换层（Flash Translation Layer）所需的坏块管理（Bad Block Management）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_SIMULATOR && CONFIG_FLASH
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_EX_OP
```

**定义位置（Location）**：[`drivers/flash/Kconfig.simulator:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.simulator#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存模拟器（Flash Simulator）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_SIMULATOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)。

<a id="CONFIG_FLASH_SIMULATOR_MIN_ERASE_TIME_US"></a>

## 93.32 `CONFIG_FLASH_SIMULATOR_MIN_ERASE_TIME_US`

**提示（Prompt）**：最小擦除时间（Minimum Erase Time），以微秒（µs）为单位

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_SIMULATOR_SIMULATE_TIMING && CONFIG_FLASH_SIMULATOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
2000
```

**取值范围（Ranges）**

```text
[1, 1000000]
```

**定义位置（Location）**：[`drivers/flash/Kconfig.simulator:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.simulator#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存模拟器（Flash Simulator） → 硬件时序模拟（Hardware Timing Simulation）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_SIMULATOR_SIMULATE_TIMING`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR_SIMULATE_TIMING)、[`CONFIG_FLASH_SIMULATOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_SIMULATOR_MIN_READ_TIME_US"></a>

## 93.33 `CONFIG_FLASH_SIMULATOR_MIN_READ_TIME_US`

**提示（Prompt）**：最小读取时间（Minimum Read Time），单位为微秒（µs）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_SIMULATOR_SIMULATE_TIMING && CONFIG_FLASH_SIMULATOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 1000000]
```

**定义位置（Location）**：[`drivers/flash/Kconfig.simulator:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.simulator#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存模拟器（Flash Simulator） → 硬件时序模拟（Hardware Timing Simulation）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_SIMULATOR_SIMULATE_TIMING`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR_SIMULATE_TIMING)、[`CONFIG_FLASH_SIMULATOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_SIMULATOR_MIN_WRITE_TIME_US"></a>

## 93.34 `CONFIG_FLASH_SIMULATOR_MIN_WRITE_TIME_US`

**提示（Prompt）**：最小写入时间（Minimum Write Time），单位为微秒（µs）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_SIMULATOR_SIMULATE_TIMING && CONFIG_FLASH_SIMULATOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[1, 1000000]
```

**定义位置（Location）**：[`drivers/flash/Kconfig.simulator:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.simulator#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存模拟器（Flash Simulator） → 硬件时序模拟（Hardware Timing Simulation）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_SIMULATOR_SIMULATE_TIMING`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR_SIMULATE_TIMING)、[`CONFIG_FLASH_SIMULATOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_SIMULATOR_RAMLIKE"></a>

## 93.35 `CONFIG_FLASH_SIMULATOR_RAMLIKE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于设置 `FLASH_HAS_NO_EXPLICIT_ERASE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_SIMULATOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y if !CONFIG_FLASH_SIMULATOR_EXPLICIT_ERASE
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE
CONFIG_FLASH_SIMULATOR_DOUBLE_WRITES
```

**定义位置（Location）**：[`drivers/flash/Kconfig.simulator:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.simulator#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存模拟器（Flash Simulator）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_SIMULATOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_SIMULATOR_EXPLICIT_ERASE`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR_EXPLICIT_ERASE)、[`CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE)、[`CONFIG_FLASH_SIMULATOR_DOUBLE_WRITES`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR_DOUBLE_WRITES)。

<a id="CONFIG_FLASH_SIMULATOR_SIMULATE_TIMING"></a>

## 93.36 `CONFIG_FLASH_SIMULATOR_SIMULATE_TIMING`

**提示（Prompt）**：硬件时序模拟（Hardware Timing Simulation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_SIMULATOR && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.simulator:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.simulator#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存模拟器（Flash Simulator）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_SIMULATOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_SIMULATOR_STATS"></a>

## 93.37 `CONFIG_FLASH_SIMULATOR_STATS`

**提示（Prompt）**：闪存操作统计（Flash Operations Statistics）

**说明（Help）**

使用统计子系统（Statistics Subsystem）收集闪存模拟器（Flash Simulator）操作的统计测量数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_SIMULATOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_STATS
CONFIG_STATS_NAMES
```

**定义位置（Location）**：[`drivers/flash/Kconfig.simulator:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.simulator#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存模拟器（Flash Simulator）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_SIMULATOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STATS)、[`CONFIG_STATS_NAMES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STATS_NAMES)。

<a id="CONFIG_FLASH_SIMULATOR_STAT_PAGE_COUNT"></a>

## 93.38 `CONFIG_FLASH_SIMULATOR_STAT_PAGE_COUNT`

**提示（Prompt）**：参与统计的页（Pages under Statistics）

**说明（Help）**

捕获专门的闪存操作和阈值（Threshold）时，仅跟踪最前面不超过此数量的页。此数量不能自动确定，因为实现使用 `UNTIL_REPEAT()` 宏，而该宏要求显式给出迭代次数。因此，无法使用预处理器（Preprocessor）根据设备树（DT）属性计算页数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_SIMULATOR_STATS && CONFIG_FLASH_SIMULATOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`drivers/flash/Kconfig.simulator:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.simulator#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存模拟器（Flash Simulator） → 闪存操作统计（Flash Operations Statistics）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_SIMULATOR_STATS`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR_STATS)、[`CONFIG_FLASH_SIMULATOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_SIMULATOR_UNALIGNED_READ"></a>

## 93.39 `CONFIG_FLASH_SIMULATOR_UNALIGNED_READ`

**提示（Prompt）**：允许非对齐读取访问（Unaligned Read Access）

**说明（Help）**

选择此项时，读操作不检查访问是否对齐（Aligned）。只有在需要模拟某种要求读取访问对齐的特定闪存接口（Flash Interface）时，才应禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_SIMULATOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.simulator:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.simulator#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存模拟器（Flash Simulator）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_SIMULATOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_SIMULATOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_SOC_CH32V"></a>

## 93.40 `CONFIG_FLASH_SOC_CH32V`

**提示（Prompt）**：沁恒（WCH）CH32V 闪存驱动（Flash Driver）

**说明（Help）**

启用沁恒（WCH）CH32V 系列的片上闪存驱动（On-Chip Flash Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WCH_CH32V_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.wch:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.wch#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_FLASH_SOC_LPC84X_IAP"></a>

## 93.41 `CONFIG_FLASH_SOC_LPC84X_IAP`

**提示（Prompt）**：NXP LPC84x ROM IAP 与 FMC MMIO 闪存驱动

**说明（Help）**

NXP LPC844/LPC845 器件的闪存驱动（Flash Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IAP_FMC84X_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.lpc84x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.lpc84x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_FLASH_STM32_ACCEPT_UNALIGNED_WRITES"></a>

## 93.42 `CONFIG_FLASH_STM32_ACCEPT_UNALIGNED_WRITES`

**提示（Prompt）**：用于 STM32 SoC 处理非对齐偏移和长度（Unaligned Offsets and Lengths）的扩展操作。

**说明（Help）**

支持传给 `flash_write()` 的偏移和长度未对齐的调用。**不了解目标闪存硬件的实现细节和限制时，不要启用此选项。**

启用后，非对齐写入（Unaligned Write）通过写入 `[offset; offset + length]` 范围内的全部块来处理。如果某个块只提供了部分内容，则在写入之前用闪存的擦除值（Erase Value）填充其余部分。**这不是读－改－写（Read-Modify-Write）操作！** 预期目标闪存地址在写入前已经擦除。非对齐写入后的闪存内容取决于具体硬件细节，操作可能引发故障（Fault）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_STM32WBA65XX && CONFIG_SOC_FLASH_STM32 && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → STM32 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_STM32WBA65XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_STM32WBA65XX)、[`CONFIG_SOC_FLASH_STM32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_STM32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_STM32WBA65XX`。

<a id="CONFIG_FLASH_STM32_BLOCK_REGISTERS"></a>

## 93.43 `CONFIG_FLASH_STM32_BLOCK_REGISTERS`

**提示（Prompt）**：封锁选项寄存器和控制寄存器的扩展操作（Block Option and Control Registers）

**说明（Help）**

启用闪存扩展操作（Flash Extended Operations），用于禁止访问选项寄存器和控制寄存器（Option and Control Registers），直到复位。禁用对这些寄存器的访问可提高系统安全性，因为即使发现了可利用的漏洞，闪存内容或保护设置也无法再被改变。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_STM32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_EX_OP
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → STM32 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_STM32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_STM32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)。

<a id="CONFIG_FLASH_STM32_NOR_MEMMAP"></a>

## 93.44 `CONFIG_FLASH_STM32_NOR_MEMMAP`

**提示（Prompt）**：内存映射模式的外部闪存（External Flash in Memory-Mapped Mode）

**说明（Help）**

为 STM32 开发板上的外部 NOR 闪存启用内存映射模式（Memory-Mapped Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_STM32_QSPI_NOR_ENABLED || DT_HAS_ST_STM32_OSPI_NOR_ENABLED || DT_HAS_ST_STM32_XSPI_NOR_ENABLED || (CONFIG_MSPI_MEMMAP && DT_HAS_ST_NOR_ENABLED && n)) && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MSPI_MEMMAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_MEMMAP)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_STM32_OPTION_BYTES"></a>

## 93.45 `CONFIG_FLASH_STM32_OPTION_BYTES`

**提示（Prompt）**：访问选项字节的扩展操作（Option Bytes Access）

**说明（Help）**

启用闪存扩展操作（Flash Extended Operations），用于读取和写入 STM32 选项字节（Option Bytes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_STM32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_EX_OP
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → STM32 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_STM32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_STM32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)。

<a id="CONFIG_FLASH_STM32_OSPI"></a>

## 93.46 `CONFIG_FLASH_STM32_OSPI`

**提示（Prompt）**：STM32 八线 SPI 闪存驱动（Octo SPI Flash Driver）

**说明（Help）**

为 STM32 系列处理器启用 OSPI-NOR 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_OSPI_NOR_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_OSPI
CONFIG_USE_STM32_LL_DLYB if CONFIG_SOC_SERIES_STM32U5X
CONFIG_USE_STM32_HAL_MDMA if CONFIG_SOC_SERIES_STM32H7X
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_JESD216
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_PINCTRL
CONFIG_DMA if n
CONFIG_GPIO if n
CONFIG_USE_STM32_HAL_DMA if n
CONFIG_USE_STM32_HAL_DMA_EX if CONFIG_SOC_SERIES_STM32U5X && n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32_ospi:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32_ospi#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_USE_STM32_HAL_OSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_OSPI)、[`CONFIG_USE_STM32_LL_DLYB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_LL_DLYB)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_USE_STM32_HAL_MDMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_MDMA)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)、[`CONFIG_USE_STM32_HAL_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA)、[`CONFIG_USE_STM32_HAL_DMA_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA_EX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32U5X`、`CONFIG_SOC_SERIES_STM32H7X`。

<a id="CONFIG_FLASH_STM32_QSPI"></a>

## 93.47 `CONFIG_FLASH_STM32_QSPI`

**提示（Prompt）**：STM32 四线 SPI 闪存驱动（Quad SPI Flash Driver）

**说明（Help）**

为 STM32 系列处理器启用 QSPI-NOR 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_QSPI_NOR_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_QSPI
CONFIG_USE_STM32_HAL_MDMA if CONFIG_SOC_SERIES_STM32H7X
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_JESD216
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_PINCTRL
CONFIG_GPIO if n
CONFIG_DMA if n
CONFIG_USE_STM32_HAL_DMA if n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32_qspi:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32_qspi#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_USE_STM32_HAL_QSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_QSPI)、[`CONFIG_USE_STM32_HAL_MDMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_MDMA)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_USE_STM32_HAL_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32H7X`。

<a id="CONFIG_FLASH_STM32_QSPI_GENERIC_READ"></a>

## 93.48 `CONFIG_FLASH_STM32_QSPI_GENERIC_READ`

**提示（Prompt）**：通用读取命令扩展操作（Generic Read Command Extended Operation）

**说明（Help）**

启用闪存扩展操作（Flash Extended Operation），用于发送自定义命令（Custom Command），并将读取结果存入用户提供的缓冲区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_STM32_QSPI && CONFIG_FLASH
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_EX_OP
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32_qspi:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32_qspi#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → STM32 四线 SPI 闪存驱动（Quad SPI Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_STM32_QSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_QSPI)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)。

<a id="CONFIG_FLASH_STM32_QSPI_GENERIC_WRITE"></a>

## 93.49 `CONFIG_FLASH_STM32_QSPI_GENERIC_WRITE`

**提示（Prompt）**：通用写入命令扩展操作（Generic Write Command Extended Operation）

**说明（Help）**

启用闪存扩展操作（Flash Extended Operation），用于发送自定义命令（Custom Command），并写入从用户提供的缓冲区取得的数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_STM32_QSPI && CONFIG_FLASH
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_EX_OP
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32_qspi:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32_qspi#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → STM32 四线 SPI 闪存驱动（Quad SPI Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_STM32_QSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_QSPI)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)。

<a id="CONFIG_FLASH_STM32_READOUT_PROTECTION"></a>

## 93.50 `CONFIG_FLASH_STM32_READOUT_PROTECTION`

**提示（Prompt）**：闪存读出保护控制扩展操作（Readout Protection Control）

**说明（Help）**

启用用于开启或关闭闪存读出保护（Readout Protection）的闪存扩展操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_STM32F4X || CONFIG_SOC_SERIES_STM32F7X || CONFIG_SOC_SERIES_STM32G0X || CONFIG_SOC_SERIES_STM32G4X || CONFIG_SOC_SERIES_STM32H7X || CONFIG_SOC_SERIES_STM32L4X || CONFIG_SOC_SERIES_STM32L5X || CONFIG_SOC_SERIES_STM32U5X) && CONFIG_SOC_FLASH_STM32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_EX_OP
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → STM32 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32G0X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G0X)、[`CONFIG_SOC_SERIES_STM32G4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32G4X)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_SERIES_STM32L4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L4X)、[`CONFIG_SOC_SERIES_STM32L5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L5X)、[`CONFIG_SOC_SERIES_STM32U5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32U5X)、[`CONFIG_SOC_FLASH_STM32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_STM32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32G0X`、`CONFIG_SOC_SERIES_STM32G4X`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_SERIES_STM32L4X`、`CONFIG_SOC_SERIES_STM32L5X`、`CONFIG_SOC_SERIES_STM32U5X`。

<a id="CONFIG_FLASH_STM32_READOUT_PROTECTION_DISABLE_ALLOW"></a>

## 93.51 `CONFIG_FLASH_STM32_READOUT_PROTECTION_DISABLE_ALLOW`

**提示（Prompt）**：允许禁用读出保护（Allow Disabling Readout Protection）

**说明（Help）**

启用此选项后，将允许禁用读出保护（Readout Protection）。**在 STM32 器件上，这会触发闪存全片擦除（Mass Erase）！**

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_STM32_READOUT_PROTECTION && CONFIG_SOC_FLASH_STM32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → STM32 闪存驱动（Flash Driver） → 闪存读出保护控制扩展操作（Readout Protection Control）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_STM32_READOUT_PROTECTION`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_READOUT_PROTECTION)、[`CONFIG_SOC_FLASH_STM32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_STM32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_STM32_READOUT_PROTECTION_PERMANENT_ALLOW"></a>

## 93.52 `CONFIG_FLASH_STM32_READOUT_PROTECTION_PERMANENT_ALLOW`

**提示（Prompt）**：允许永久启用读出保护（Allow Permanent Readout Protection）

**说明（Help）**

启用此选项后，将允许永久启用读出保护（Readout Protection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_STM32_READOUT_PROTECTION && CONFIG_SOC_FLASH_STM32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → STM32 闪存驱动（Flash Driver） → 闪存读出保护控制扩展操作（Readout Protection Control）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_STM32_READOUT_PROTECTION`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_READOUT_PROTECTION)、[`CONFIG_SOC_FLASH_STM32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_STM32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_STM32_WRITE_PROTECT"></a>

## 93.53 `CONFIG_FLASH_STM32_WRITE_PROTECT`

**提示（Prompt）**：闪存写保护控制扩展操作（Write Protection Control）

**说明（Help）**

启用用于开启或关闭闪存写保护（Write Protection）的闪存扩展操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_STM32F4X || CONFIG_SOC_SERIES_STM32H7X) && CONFIG_SOC_FLASH_STM32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_EX_OP
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → STM32 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_FLASH_STM32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_STM32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_EX_OP`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EX_OP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32F4X`、`CONFIG_SOC_SERIES_STM32H7X`。

<a id="CONFIG_FLASH_STM32_WRITE_PROTECT_DISABLE_PREVENTION"></a>

## 93.54 `CONFIG_FLASH_STM32_WRITE_PROTECT_DISABLE_PREVENTION`

**提示（Prompt）**：禁止关闭闪存写保护（Prevent Disabling Write Protection）

**说明（Help）**

启用后，阻止所有关闭闪存写保护（Write Protection）的请求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_STM32_WRITE_PROTECT && CONFIG_SOC_FLASH_STM32 && CONFIG_FLASH
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → STM32 闪存驱动（Flash Driver） → 闪存写保护控制扩展操作（Write Protection Control）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_STM32_WRITE_PROTECT`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_WRITE_PROTECT)、[`CONFIG_SOC_FLASH_STM32`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_STM32)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_FLASH_STM32_XSPI"></a>

## 93.55 `CONFIG_FLASH_STM32_XSPI`

**提示（Prompt）**：STM32 XSPI 闪存驱动（Flash Driver）

**说明（Help）**

为 STM32 系列处理器启用 XSPI-NOR 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_XSPI_ENABLED && DT_HAS_ST_STM32_XSPI_NOR_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_XSPI
CONFIG_USE_STM32_LL_DLYB
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_JESD216
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_PINCTRL
CONFIG_GPIO if n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32_xspi:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32_xspi#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_USE_STM32_HAL_XSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_XSPI)、[`CONFIG_USE_STM32_LL_DLYB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_LL_DLYB)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_FLASH_STM32_XSPI_DMA"></a>

## 93.56 `CONFIG_FLASH_STM32_XSPI_DMA`

**提示（Prompt）**：STM32 XSPI 闪存的 DMA 支持

**说明（Help）**

为 XSPI 闪存驱动实例启用直接内存访问（DMA）模式。

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
CONFIG_USE_STM32_HAL_DMA
CONFIG_USE_STM32_HAL_DMA_EX
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32_xspi:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32_xspi#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → STM32 XSPI 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_USE_STM32_HAL_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA)、[`CONFIG_USE_STM32_HAL_DMA_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA_EX)。

<a id="CONFIG_FLASH_STM32_XSPI_RAM_RELOCATION"></a>

## 93.57 `CONFIG_FLASH_STM32_XSPI_RAM_RELOCATION`

**提示（Prompt）**：为外部闪存原地执行（XIP）重定位 STM32 XSPI 驱动代码【实验性】

**说明（Help）**

将 STM32 XSPI 驱动代码重定位（Relocate）到外部闪存之外，使系统从外部闪存执行代码时仍可进行擦除和写入。启用后，驱动还会在禁用内存映射模式（Memory-Mapped Mode）的关键时间窗口内锁定中断（Lock Interrupts）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XIP && CONFIG_STM32_APP_IN_EXT_FLASH && (CONFIG_SOC_SERIES_STM32N6X || CONFIG_SOC_SERIES_STM32H7RSX) && CONFIG_CPU_CORTEX_M_HAS_DWT && CONFIG_FLASH_STM32_XSPI && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_CODE_DATA_RELOCATION
CONFIG_CODE_DATA_RELOCATION_SRAM
CONFIG_CORTEX_M_DWT
```

**定义位置（Location）**：[`drivers/flash/Kconfig.stm32_xspi:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.stm32_xspi#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → STM32 XSPI 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)、[`CONFIG_STM32_APP_IN_EXT_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32_APP_IN_EXT_FLASH)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_SOC_SERIES_STM32H7RSX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7RSX)、[`CONFIG_CPU_CORTEX_M_HAS_DWT`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_DWT)、[`CONFIG_FLASH_STM32_XSPI`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_STM32_XSPI)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_CODE_DATA_RELOCATION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CODE_DATA_RELOCATION)、[`CONFIG_CODE_DATA_RELOCATION_SRAM`](P029_arch_arm_配置项参考_1.md#CONFIG_CODE_DATA_RELOCATION_SRAM)、[`CONFIG_CORTEX_M_DWT`](P029_arch_arm_配置项参考_1.md#CONFIG_CORTEX_M_DWT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32N6X`、`CONFIG_SOC_SERIES_STM32H7RSX`。

<a id="CONFIG_GD32_NV_FLASH_V1"></a>

## 93.58 `CONFIG_GD32_NV_FLASH_V1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 FMC v1 闪存驱动的通用后端（Generic Backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_NV_FLASH_V1_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.gd32:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.gd32#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_GD32_NV_FLASH_V2"></a>

## 93.59 `CONFIG_GD32_NV_FLASH_V2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 FMC v2 闪存驱动的通用后端（Generic Backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_NV_FLASH_V2_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.gd32:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.gd32#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_GD32_NV_FLASH_V3"></a>

## 93.60 `CONFIG_GD32_NV_FLASH_V3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 GD32 FMC v3 闪存驱动的通用后端（Generic Backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GD_GD32_NV_FLASH_V3_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.gd32:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.gd32#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_INFINEON_CAT1_QSPI_FLASH"></a>

## 93.61 `CONFIG_INFINEON_CAT1_QSPI_FLASH`

**提示（Prompt）**：Infineon CAT1 QSPI 闪存驱动（Flash Driver）

**说明（Help）**

启用英飞凌（Infineon）CAT1 系列的 QSPI 闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_QSPI_FLASH_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_USE_INFINEON_FLASH
CONFIG_USE_INFINEON_SMIF
CONFIG_USE_INFINEON_DMA
CONFIG_PINCTRL
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.infineon:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.infineon#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_USE_INFINEON_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_FLASH)、[`CONFIG_USE_INFINEON_SMIF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_SMIF)、[`CONFIG_USE_INFINEON_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_DMA)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_MCUX_FLASH_K4_API"></a>

## 93.62 `CONFIG_MCUX_FLASH_K4_API`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果平台计划使用 `flash_k4` SDK 的在应用编程（IAP）API，则由 SoC 层配置设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_MCUX && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.mcux:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.mcux#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → MCUX 闪存适配层驱动（Flash Shim Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_MCUX`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_MCUX)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_NORDIC_QSPI_NOR"></a>

## 93.63 `CONFIG_NORDIC_QSPI_NOR`

**提示（Prompt）**：QSPI NOR 闪存（Flash）

**说明（Help）**

启用带 EasyDMA 的 nrfx QSPI 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_QSPI_NOR_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_NRFX_QSPI
CONFIG_FLASH_JESD216
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nordic_qspi_nor:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nordic_qspi_nor#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_NRFX_QSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_QSPI)、[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_NORDIC_QSPI_NOR_ACTIVE_DWELL_MS"></a>

## 93.64 `CONFIG_NORDIC_QSPI_NOR_ACTIVE_DWELL_MS`

**提示（Prompt）**：最后一次使用后保持活动模式的停留时间（Dwell Period），以毫秒为单位

**说明（Help）**

闪存访问通常成批发生。如果每次访问之间都进入并退出深度掉电模式（Deep Power-Down，DPD），总操作时间会显著增加。此选项控制每次 API 调用后保持活动模式（Active Mode）的时长；如果下一次事务在停留时间（Dwell Period）结束前发生，就可省去“活动→空闲→活动”的状态转换过程。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PM_DEVICE_RUNTIME && CONFIG_NORDIC_QSPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nordic_qspi_nor:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nordic_qspi_nor#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → QSPI NOR 闪存（Flash）

**配置项引用（Symbol References）**：[`CONFIG_PM_DEVICE_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE_RUNTIME)、[`CONFIG_NORDIC_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_NORDIC_QSPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_NORDIC_QSPI_NOR_FLASH_LAYOUT_PAGE_SIZE"></a>

## 93.65 `CONFIG_NORDIC_QSPI_NOR_FLASH_LAYOUT_PAGE_SIZE`

**提示（Prompt）**：`FLASH_LAYOUT` 功能使用的页大小（Page Size）

**说明（Help）**

使用 `CONFIG_FLASH_PAGE_LAYOUT` 时，此驱动支持对应 API。默认页大小（Page Size）等于块大小（Block Size）`65536`。其他选项包括扇区大小（Sector Size）`4096`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NORDIC_QSPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
65536
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nordic_qspi_nor:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nordic_qspi_nor#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → QSPI NOR 闪存（Flash）

**配置项引用（Symbol References）**：[`CONFIG_NORDIC_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_NORDIC_QSPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_NORDIC_QSPI_NOR_INIT_PRIORITY"></a>

## 93.66 `CONFIG_NORDIC_QSPI_NOR_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

设备驱动初始化优先级（Device Driver Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NORDIC_QSPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
41
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nordic_qspi_nor:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nordic_qspi_nor#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → QSPI NOR 闪存（Flash）

**配置项引用（Symbol References）**：[`CONFIG_NORDIC_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_NORDIC_QSPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_NORDIC_QSPI_NOR_STACK_WRITE_BUFFER_SIZE"></a>

## 93.67 `CONFIG_NORDIC_QSPI_NOR_STACK_WRITE_BUFFER_SIZE`

**提示（Prompt）**：用于处理 QSPI 不直接支持的写入的栈缓冲区大小（Stack-Based Buffer Size）

**说明（Help）**

QSPI 外设使用 DMA，只能写入从 RAM 中按字对齐（Word-Aligned）位置读取的数据。此值非零时，为不满足这些限制的源数据启用栈缓冲区（Stack Buffer）。数据先复制到此缓冲区，以便继续写入；如果数据大于配置的大小，则发起多次传输。数值必须是 `4` 的整数倍。设为 `0` 时禁用此功能。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NORDIC_QSPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nordic_qspi_nor:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nordic_qspi_nor#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → QSPI NOR 闪存（Flash）

**配置项引用（Symbol References）**：[`CONFIG_NORDIC_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_NORDIC_QSPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_NORDIC_QSPI_NOR_TIMEOUT_MS"></a>

## 93.68 `CONFIG_NORDIC_QSPI_NOR_TIMEOUT_MS`

**提示（Prompt）**：QSPI 操作超时时间（Operation Timeout），以毫秒为单位

**说明（Help）**

QSPI 外设的操作超时时间（Operation Timeout），以毫秒为单位。主要用于闪存扇区擦除（Sector Erase）等耗时较长的操作。默认值 500 ms 足以让大多数常见 NOR 闪存芯片完成一次扇区擦除。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NORDIC_QSPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nordic_qspi_nor:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nordic_qspi_nor#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → QSPI NOR 闪存（Flash）

**配置项引用（Symbol References）**：[`CONFIG_NORDIC_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_NORDIC_QSPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_NORDIC_QSPI_NOR_XIP"></a>

## 93.69 `CONFIG_NORDIC_QSPI_NOR_XIP`

**提示（Prompt）**：原地执行（Execute in Place，XIP）

**说明（Help）**

启用对 QSPI NOR 驱动的相应设置，允许执行存储在 QSPI XIP 区域中的代码。要使此功能正常工作，必须正确设置 QSPI NOR 初始化优先级（Init Priority），确保驱动完成设置之前不会执行 QSPI NOR 闪存芯片中的任何 XIP 代码。此项还会禁用该闪存芯片的电源管理（Power Management）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_NRF5340_CPUAPP && CONFIG_NORDIC_QSPI_NOR && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nordic_qspi_nor:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nordic_qspi_nor#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → QSPI NOR 闪存（Flash）

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_NORDIC_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_NORDIC_QSPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_NRF5340_CPUAPP`。

<a id="CONFIG_NORDIC_QSPI_NOR_XIP_FLASH_SCHED_LOCK"></a>

## 93.70 `CONFIG_NORDIC_QSPI_NOR_XIP_FLASH_SCHED_LOCK`

**提示（Prompt）**：原地执行（XIP）时，在 QSPI NOR 编程/擦除期间保持调度器锁（Scheduler Lock）

**说明（Help）**

从外部 QSPI 闪存执行代码（XIP）时，如果该设备正在编程或擦除，其他线程不得从同一设备取指（Fetch Instructions）。在每次闪存操作期间持有调度器锁（Scheduler Lock），可防止其他线程并发运行 XIP 代码。写入进行中（WIP）状态的轮询采用忙等待（Busy Wait），而不休眠，从而不违反该锁的约束。对于分离式 XIP 与设备固件升级（DFU）工作负载，应启用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NORDIC_QSPI_NOR_XIP && CONFIG_MULTITHREADING && CONFIG_NORDIC_QSPI_NOR && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nordic_qspi_nor:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nordic_qspi_nor#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → QSPI NOR 闪存（Flash） → 原地执行（Execute in Place，XIP）

**配置项引用（Symbol References）**：[`CONFIG_NORDIC_QSPI_NOR_XIP`](P093_drivers_flash_配置项参考_2.md#CONFIG_NORDIC_QSPI_NOR_XIP)、[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_NORDIC_QSPI_NOR`](P093_drivers_flash_配置项参考_2.md#CONFIG_NORDIC_QSPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_NRF_MRAMC_MAX_RETRIES"></a>

## 93.71 `CONFIG_NRF_MRAMC_MAX_RETRIES`

**提示（Prompt）**：MRAM 写入/擦除操作的最大重试次数（Maximum Retries）

**说明（Help）**

此选项设置 MRAM 写入和擦除操作在验证失败时允许的最大重试次数（Retry Attempts）。每次重试都会尝试重新写入或重新擦除数据，以确保可靠性。较大的值可提高可靠性，但在持续失败时可能影响性能。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_NRF_MRAMC && CONFIG_FLASH
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_mramc:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_mramc#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF_MRAMC`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_MRAMC)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_NRF_MRAMC_REGION_ADDRESS_RESOLUTION"></a>

## 93.72 `CONFIG_NRF_MRAMC_REGION_ADDRESS_RESOLUTION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

MRAM 控制器（MRAMC）区域保护的地址分辨率（Address Resolution），适用于起始地址可配置的区域。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH
```

**默认值（Defaults）**

```text
0x400
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_mramc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_mramc#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_NRF_MRAMC_REGION_SIZE_UNIT"></a>

## 93.73 `CONFIG_NRF_MRAMC_REGION_SIZE_UNIT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

MRAM 控制器（MRAMC）区域保护大小的基本单位（Base Unit）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH
```

**默认值（Defaults）**

```text
0x400
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_mramc:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_mramc#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_NRF_MRAM_MAX_RETRIES"></a>

## 93.74 `CONFIG_NRF_MRAM_MAX_RETRIES`

**提示（Prompt）**：MRAM 写入/擦除操作的最大重试次数（Maximum Retries）

**说明（Help）**

此选项设置 MRAM 写入和擦除操作在验证失败时允许的最大重试次数（Retry Attempts）。每次重试都会尝试重新写入或重新擦除数据，以确保可靠性。较大的值可提高可靠性，但在持续失败时可能影响性能。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_NRF_MRAM && CONFIG_FLASH
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_mram:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_mram#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor 用于 MRAM 的闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF_MRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_MRAM)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_NRF_RRAM_FILL_SKIP_IF_FILLED"></a>

## 93.75 `CONFIG_NRF_RRAM_FILL_SKIP_IF_FILLED`

**提示（Prompt）**：跳过已具有目标填充值的写入行（Skip Lines Already Holding Fill Value）

**说明（Help）**

启用后，`api->fill` 回调以 16 字节写入行（Write Line）为粒度扫描目标区域，只写入当前内容与请求填充值不同的行。此回调用于 `flash_fill()`，并间接用于无需擦除的设备上的 `flash_flatten()`。连续的待修改行（Dirty Line）合并为一次底层写入。此优化适用于任意填充值，包括但不限于设备的 `ERASE_VALUE`。

对于上层反复重新填充已经具有一致内容的区域的场景，此功能很有用，例如 NVS/ZMS 扇区轮换（Sector Rotation）、MCUboot 再次平整先前已扰乱内容的镜像槽（Slot）、FCB 垃圾回收（GC）和设置维护（Settings Housekeeping）。在这些工作负载下，它能显著提高写入耐久性（Write Endurance），代价是每页需要几微秒的内存映射读取扫描（Memory-Mapped Read Scan）。

此选项默认禁用，因为它会改变填充操作的最坏情况延迟特征（Worst-Case Latency Profile）。**注意**：此功能不能防护对所扫描区域的并发写入。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_NRF_RRAM && CONFIG_FLASH
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_rram:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_rram#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor 用于 nRF RRAM 的闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF_RRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RRAM)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_NRF_RRAM_READYNEXT_TIMEOUT_VALUE"></a>

## 93.76 `CONFIG_NRF_RRAM_READYNEXT_TIMEOUT_VALUE`

**提示（Prompt）**：等待下一次写入的预加载超时值（Preload Timeout），以 RRAMC 时钟周期为单位

**说明（Help）**

设为 `0` 可禁用等待下一次就绪的超时计数器（Ready Next Timeout Counter）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_NRF_RRAM && CONFIG_FLASH
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[0, 4095]
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_rram:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_rram#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor 用于 nRF RRAM 的闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF_RRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RRAM)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_NRF_RRAM_REGION_ADDRESS_RESOLUTION"></a>

## 93.77 `CONFIG_NRF_RRAM_REGION_ADDRESS_RESOLUTION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RRAM 控制器（RRAMC）区域保护的地址分辨率（Address Resolution），适用于起始地址可配置的区域。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_NRF_RRAM && CONFIG_FLASH
```

**默认值（Defaults）**

```text
0x400
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_rram:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_rram#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor 用于 nRF RRAM 的闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF_RRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RRAM)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_NRF_RRAM_REGION_SIZE_UNIT"></a>

## 93.78 `CONFIG_NRF_RRAM_REGION_SIZE_UNIT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RRAM 控制器（RRAMC）区域保护大小的基本单位（Base Unit）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_NRF_RRAM && CONFIG_FLASH
```

**默认值（Defaults）**

```text
0x400
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_rram:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_rram#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor 用于 nRF RRAM 的闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF_RRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RRAM)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_NRF_RRAM_THROTTLING_DATA_BLOCK"></a>

## 93.79 `CONFIG_NRF_RRAM_THROTTLING_DATA_BLOCK`

**提示（Prompt）**：每次闪存写操作的数据块数量（Data Block Count）

**说明（Help）**

启用节流（Throttling）时，每次闪存写操作的数据块数量，以 128 位字（128-Bit Word）的个数计。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_NRF_THROTTLING && CONFIG_SOC_FLASH_NRF_RRAM && CONFIG_FLASH
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_rram:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_rram#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor 用于 nRF RRAM 的闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF_THROTTLING`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_THROTTLING)、[`CONFIG_SOC_FLASH_NRF_RRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RRAM)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_NRF_RRAM_THROTTLING_DELAY"></a>

## 93.80 `CONFIG_NRF_RRAM_THROTTLING_DELAY`

**提示（Prompt）**：闪存写操作之间的延迟（Delay between Writes）

**说明（Help）**

启用节流（Throttling）时，连续闪存写操作之间的延迟，以微秒为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_NRF_THROTTLING && CONFIG_SOC_FLASH_NRF_RRAM && CONFIG_FLASH
```

**默认值（Defaults）**

```text
2000
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_rram:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_rram#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor 用于 nRF RRAM 的闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF_THROTTLING`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_THROTTLING)、[`CONFIG_SOC_FLASH_NRF_RRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RRAM)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_NRF_RRAM_WRITE_BUFFER_SIZE"></a>

## 93.81 `CONFIG_NRF_RRAM_WRITE_BUFFER_SIZE`

**提示（Prompt）**：内部写缓冲区大小（Internal Write-Buffer Size）

**说明（Help）**

128 位字（128-Bit Word）的数量。缓冲区最大可配置为 32 个 128 位字。设为 `0` 可禁用写缓冲区（Write Buffer）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_NRF_RRAM && CONFIG_FLASH
```

**默认值（Defaults）**

```text
32 if CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE
1
```

**取值范围（Ranges）**

```text
[0, 32]
```

**定义位置（Location）**：[`drivers/flash/Kconfig.nrf_rram:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.nrf_rram#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Nordic Semiconductor 用于 nRF RRAM 的闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_NRF_RRAM`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RRAM)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_NRF_RADIO_SYNC_NONE)。

<a id="CONFIG_QSPI_ADDR_BYTES"></a>

## 93.82 `CONFIG_QSPI_ADDR_BYTES`

**提示（Prompt）**：访问 QSPI 的地址存储空间大小（Address Memory Size），以字节为单位

**说明（Help）**

设置访问 QSPI 时的地址存储空间大小（Address Memory Size），以字节为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_CAD_QSPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/flash/Kconfig.cadence_qspi_nor:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.cadence_qspi_nor#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Cadence 四线 SPI 闪存驱动（Quad SPI Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_CAD_QSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_CAD_QSPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_QSPI_BYTES_PER_BLOCK"></a>

## 93.83 `CONFIG_QSPI_BYTES_PER_BLOCK`

**提示（Prompt）**：设置 QSPI 每块读写的字节数（Bytes Per Block）

**说明（Help）**

设置 QSPI 每个块（Block）的读写大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_CAD_QSPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`drivers/flash/Kconfig.cadence_qspi_nor:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.cadence_qspi_nor#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Cadence 四线 SPI 闪存驱动（Quad SPI Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_CAD_QSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_CAD_QSPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_QSPI_BYTES_PER_DEV"></a>

## 93.84 `CONFIG_QSPI_BYTES_PER_DEV`

**提示（Prompt）**：设置 QSPI 每个设备读写的字节数（Bytes Per Device）

**说明（Help）**

设置 QSPI 每个设备（Device）的读写大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_CAD_QSPI_NOR && CONFIG_FLASH
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/flash/Kconfig.cadence_qspi_nor:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.cadence_qspi_nor#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Cadence 四线 SPI 闪存驱动（Quad SPI Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_CAD_QSPI_NOR`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_CAD_QSPI_NOR)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_RX_FLASH_TYPE1"></a>

## 93.85 `CONFIG_RX_FLASH_TYPE1`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RX 闪存驱动类型 1（Flash Driver Type 1）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_RX130 || CONFIG_SOC_SERIES_RX261 || CONFIG_SOC_SERIES_RX140 || CONFIG_SOC_SERIES_RX14T) && CONFIG_SOC_FLASH_RENESAS_RX && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.renesas_rx:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.renesas_rx#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → RX 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RX130`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX130)、[`CONFIG_SOC_SERIES_RX261`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX261)、[`CONFIG_SOC_SERIES_RX140`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX140)、[`CONFIG_SOC_SERIES_RX14T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX14T)、[`CONFIG_SOC_FLASH_RENESAS_RX`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RX)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_RX_FLASH_TYPE5"></a>

## 93.86 `CONFIG_RX_FLASH_TYPE5`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

RX 闪存驱动类型 1（Flash Driver Type 1）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RX26T && CONFIG_SOC_FLASH_RENESAS_RX && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/flash/Kconfig.renesas_rx:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.renesas_rx#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → RX 闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RX26T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RX26T)、[`CONFIG_SOC_FLASH_RENESAS_RX`](P094_drivers_flash_配置项参考_3.md#CONFIG_SOC_FLASH_RENESAS_RX)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_SOC_FLASH_AMEBA"></a>

## 93.87 `CONFIG_SOC_FLASH_AMEBA`

**提示（Prompt）**：AMEBA 闪存驱动（Flash Driver）

**说明（Help）**

启用 AMEBA 内部闪存驱动（Internal Flash Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_AMEBA_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.ameba:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.ameba#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_SOC_FLASH_BEE_NOR"></a>

## 93.88 `CONFIG_SOC_FLASH_BEE_NOR`

**提示（Prompt）**：Realtek Bee NOR 闪存驱动（NOR Flash Driver）

**说明（Help）**

启用瑞昱（Realtek）Bee NOR 闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_REALTEK_BEE_NOR_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.bee_nor:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.bee_nor#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_SOC_FLASH_BEE_NOR_1BIT_MODE"></a>

## 93.89 `CONFIG_SOC_FLASH_BEE_NOR_1BIT_MODE`

**提示（Prompt）**：闪存单比特模式（1-Bit Mode）

**说明（Help）**

将瑞昱（Realtek）Bee NOR 闪存设为默认的单比特模式（1-Bit Mode）。这是使用 `CLK`、`CS#`、`DI` 和 `DO` 引脚的标准 SPI 模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/flash/Kconfig.bee_nor:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.bee_nor#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Realtek Bee NOR 闪存驱动（NOR Flash Driver） → Realtek Bee NOR 闪存位模式（Bit Mode）

<a id="CONFIG_SOC_FLASH_BEE_NOR_2BIT_MODE"></a>

## 93.90 `CONFIG_SOC_FLASH_BEE_NOR_2BIT_MODE`

**提示（Prompt）**：闪存双比特模式（2-Bit Mode，Dual）

**说明（Help）**

将瑞昱（Realtek）Bee NOR 闪存设为双比特（Dual）模式，分别使用 `DI` 和 `DO` 作为 `IO0` 和 `IO1`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.bee_nor:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.bee_nor#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Realtek Bee NOR 闪存驱动（NOR Flash Driver） → Realtek Bee NOR 闪存位模式（Bit Mode）

<a id="CONFIG_SOC_FLASH_BEE_NOR_4BIT_MODE"></a>

## 93.91 `CONFIG_SOC_FLASH_BEE_NOR_4BIT_MODE`

**提示（Prompt）**：闪存四比特模式（4-Bit Mode，Quad）

**说明（Help）**

将瑞昱（Realtek）Bee NOR 闪存设为四比特（Quad）模式。原文描述使用全部六根引脚，并列出 `DI`、`DO`、`WP#` 和 `HOLD#` 作为 `IO0` 至 `IO3`。注意：Bee 系列 SoC 所用的闪存仅部分支持四线读取模式（Quad-Read Mode）；用户应事先核实闪存型号及特征。

> 译注：原文的“six pins”与括号内仅列出的四个信号数量不一致，此处保留两项信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.bee_nor:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.bee_nor#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Realtek Bee NOR 闪存驱动（NOR Flash Driver） → Realtek Bee NOR 闪存位模式（Bit Mode）

<a id="CONFIG_SOC_FLASH_BEE_NOR_DTR_4BIT_MODE"></a>

## 93.92 `CONFIG_SOC_FLASH_BEE_NOR_DTR_4BIT_MODE`

**提示（Prompt）**：闪存四比特双倍传输速率模式（4-Bit DTR Mode，Quad）

**说明（Help）**

将瑞昱（Realtek）Bee NOR 闪存设为四比特双倍传输速率（Double Transfer Rate，DTR）模式。此模式性能更高，但需要闪存硬件支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.bee_nor:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.bee_nor#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → Realtek Bee NOR 闪存驱动（NOR Flash Driver） → Realtek Bee NOR 闪存位模式（Bit Mode）

<a id="CONFIG_SOC_FLASH_BFLB"></a>

## 93.93 `CONFIG_SOC_FLASH_BFLB`

**提示（Prompt）**：博流（Bouffalo Lab）闪存驱动（Flash Driver）

**说明（Help）**

为闪存控制器（Flash Controller）启用博流（Bouffalo Lab）闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_SF_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**弱选择（Implies）**

```text
CONFIG_CODE_DATA_RELOCATION
```

**定义位置（Location）**：[`drivers/flash/Kconfig.bflb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.bflb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_CODE_DATA_RELOCATION`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CODE_DATA_RELOCATION)。

<a id="CONFIG_SOC_FLASH_BFLB_DIRECT_ACCESS"></a>

## 93.94 `CONFIG_SOC_FLASH_BFLB_DIRECT_ACCESS`

**提示（Prompt）**：博流（Bouffalo Lab）闪存驱动读取模式（Read Mode）

**说明（Help）**

启用通过控制器直接访问闪存，而不通过缓存（Cache）和原地执行（XIP）映射访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_BFLB && CONFIG_FLASH
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/flash/Kconfig.bflb:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.bflb#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 博流（Bouffalo Lab）闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_BFLB`](P093_drivers_flash_配置项参考_2.md#CONFIG_SOC_FLASH_BFLB)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)。

<a id="CONFIG_SOC_FLASH_BFLB_SFDP"></a>

## 93.95 `CONFIG_SOC_FLASH_BFLB_SFDP`

**提示（Prompt）**：BFLB 串行闪存（SF）控制器上的 SFDP

**说明（Help）**

启用通过控制器直接访问闪存，而不通过缓存（Cache）和原地执行（XIP）映射访问。

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
CONFIG_FLASH_JESD216
```

**定义位置（Location）**：[`drivers/flash/Kconfig.bflb:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.bflb#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 博流（Bouffalo Lab）闪存驱动（Flash Driver）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_JESD216`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_JESD216)。

<a id="CONFIG_SOC_FLASH_CC13XX_CC26XX"></a>

## 93.96 `CONFIG_SOC_FLASH_CC13XX_CC26XX`

**提示（Prompt）**：TI SimpleLink CC13xx/CC26xx 闪存控制器驱动（Flash Controller Driver）

**说明（Help）**

启用 TI SimpleLink CC13xx/CC26xx 闪存控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC13XX_CC26XX_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`drivers/flash/Kconfig.cc13xx_cc26xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.cc13xx_cc26xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<a id="CONFIG_SOC_FLASH_CC23X0"></a>

## 93.97 `CONFIG_SOC_FLASH_CC23X0`

**提示（Prompt）**：TI SimpleLink CC23x0 闪存控制器驱动（Flash Controller Driver）

**说明（Help）**

启用 TI SimpleLink CC23x0 闪存控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC23X0_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`drivers/flash/Kconfig.cc23x0:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.cc23x0#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<a id="CONFIG_SOC_FLASH_ESP32"></a>

## 93.98 `CONFIG_SOC_FLASH_ESP32`

**提示（Prompt）**：乐鑫（Espressif）ESP32 闪存驱动（Flash Driver）

**说明（Help）**

启用 ESP32 内部闪存驱动（Internal Flash Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**定义位置（Location）**：[`drivers/flash/Kconfig.esp32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.esp32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)。

<a id="CONFIG_SOC_FLASH_GD32"></a>

## 93.99 `CONFIG_SOC_FLASH_GD32`

**提示（Prompt）**：兆易创新（GigaDevice）GD32 闪存驱动（Flash Driver）

**说明（Help）**

启用兆易创新（GigaDevice）GD32 闪存驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_GD32_NV_FLASH_V1 || CONFIG_GD32_NV_FLASH_V2 || CONFIG_GD32_NV_FLASH_V3) && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`drivers/flash/Kconfig.gd32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.gd32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GD32_NV_FLASH_V1`](P093_drivers_flash_配置项参考_2.md#CONFIG_GD32_NV_FLASH_V1)、[`CONFIG_GD32_NV_FLASH_V2`](P093_drivers_flash_配置项参考_2.md#CONFIG_GD32_NV_FLASH_V2)、[`CONFIG_GD32_NV_FLASH_V3`](P093_drivers_flash_配置项参考_2.md#CONFIG_GD32_NV_FLASH_V3)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<a id="CONFIG_SOC_FLASH_GECKO"></a>

## 93.100 `CONFIG_SOC_FLASH_GECKO`

**提示（Prompt）**：Silicon Labs Gecko 闪存驱动（Flash Driver）

**说明（Help）**

启用 Silicon Labs Gecko 系列内部闪存驱动（Internal Flash Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_GECKO_FLASH_CONTROLLER_ENABLED && CONFIG_FLASH
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
CONFIG_FLASH_HAS_PAGE_LAYOUT
CONFIG_SILABS_GECKO_MSC
CONFIG_FLASH_HAS_EXPLICIT_ERASE
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`drivers/flash/Kconfig.gecko:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/Kconfig.gecko#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_FLASH_HAS_PAGE_LAYOUT`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_PAGE_LAYOUT)、[`CONFIG_SILABS_GECKO_MSC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_GECKO_MSC)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<!-- kconfig-navigation -->

[上一章](P092_drivers_flash_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P094_drivers_flash_配置项参考_3.md)
