---
id: learning.zephyr-docs.kconfig-reference.page-300
title: "`soc/raspberrypi`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第300章\_`soc/raspberrypi`配置项参考

本章翻译官方 Kconfig 数据库中 `soc/raspberrypi` 的 45 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_RP2_FLASH_AT25SF128A"></a>

## 300.1 `CONFIG_RP2_FLASH_AT25SF128A`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

将 RP2 配置为使用 AT25SF128A 或类似的 Flash 芯片。应由开发板定义选择，不应由用户选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RP2040 && CONFIG_SOC_FAMILY_RPI_PICO
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2040/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2040/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RP2040`](P300_soc_raspberrypi_配置项参考.md#CONFIG_SOC_SERIES_RP2040)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RP2_FLASH_GENERIC_03H"></a>

## 300.2 `CONFIG_RP2_FLASH_GENERIC_03H`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

将 RP2 配置为使用支持标准 03h 命令的 Flash 芯片。应由开发板定义选择，不应由用户选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RP2040 && CONFIG_SOC_FAMILY_RPI_PICO
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2040/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2040/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RP2040`](P300_soc_raspberrypi_配置项参考.md#CONFIG_SOC_SERIES_RP2040)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RP2_FLASH_IS25LP080"></a>

## 300.3 `CONFIG_RP2_FLASH_IS25LP080`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

将 RP2 配置为使用 IS25LP080 或类似的 Flash 芯片。应由开发板定义选择，不应由用户选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RP2040 && CONFIG_SOC_FAMILY_RPI_PICO
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2040/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2040/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RP2040`](P300_soc_raspberrypi_配置项参考.md#CONFIG_SOC_SERIES_RP2040)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RP2_FLASH_W25Q080"></a>

## 300.4 `CONFIG_RP2_FLASH_W25Q080`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

将 RP2 配置为使用 W25Q080 或类似的 Flash 芯片。应由开发板定义选择，不应由用户选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RP2040 && CONFIG_SOC_FAMILY_RPI_PICO
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2040/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2040/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RP2040`](P300_soc_raspberrypi_配置项参考.md#CONFIG_SOC_SERIES_RP2040)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RP2_FLASH_W25X10CL"></a>

## 300.5 `CONFIG_RP2_FLASH_W25X10CL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

将 RP2 配置为使用 W25X10CL 或类似的 Flash 芯片。应由开发板定义选择，不应由用户选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RP2040 && CONFIG_SOC_FAMILY_RPI_PICO
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2040/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2040/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RP2040`](P300_soc_raspberrypi_配置项参考.md#CONFIG_SOC_SERIES_RP2040)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RP2_REQUIRES_IMAGE_DEFINITION_BLOCK"></a>

## 300.6 `CONFIG_RP2_REQUIRES_IMAGE_DEFINITION_BLOCK`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

包含镜像定义块（Image Definition Block，`IMAGE_DEF`），使 RP23XX 器件的启动 ROM（boot ROM）将其视为 Flash 中的有效镜像。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_RP2350 && CONFIG_SOC_FAMILY_RPI_PICO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2350/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2350/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_RP2350)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_RP2350`、`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO"></a>

## 300.7 `CONFIG_RPI_PICO_BINARY_INFO`

**提示（Prompt）**：生成 Raspberry Pi Pico 二进制信息（binary info）

**说明（Help）**

二进制信息（binary info）可将机器可读信息与二进制程序一同嵌入 Flash，并可通过 [picotool](https://github.com/raspberrypi/picotool) 读取。启用此项后，会自动生成二进制信息。

启用此功能时，引脚控制组（pinctrl group）中的引脚必须具有同一种 `rpi_pico` 功能。换言之，SPI 的 MISO 和 MOSI 可以位于同一组，但不能将 I2C 的 SDA 加入该组。正常使用时很少遇到此问题，也可通过将引脚拆分到不同组来解决。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RPI_PICO
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_ATTRIBUTE_BUILD_TYPE"></a>

## 300.8 `CONFIG_RPI_PICO_BINARY_INFO_ATTRIBUTE_BUILD_TYPE`

**提示（Prompt）**：在二进制信息中生成构建类型属性（attribute_build_type）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_BOOT_STAGE2_NAME"></a>

## 300.9 `CONFIG_RPI_PICO_BINARY_INFO_BOOT_STAGE2_NAME`

**提示（Prompt）**：在二进制信息中生成第二阶段启动名称（boot_stage2_name）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_OVERRIDE_ATTRIBUTE_BUILD_TYPE"></a>

## 300.10 `CONFIG_RPI_PICO_BINARY_INFO_OVERRIDE_ATTRIBUTE_BUILD_TYPE`

**提示（Prompt）**：覆盖二进制信息中的构建类型属性（attribute_build_type）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO_ATTRIBUTE_BUILD_TYPE && CONFIG_RPI_PICO_BINARY_INFO_ATTRIBUTE_BUILD_TYPE && CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info） → 在二进制信息中生成构建类型属性（attribute_build_type）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO_ATTRIBUTE_BUILD_TYPE`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO_ATTRIBUTE_BUILD_TYPE)、[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_OVERRIDE_BOOT_STAGE2_NAME"></a>

## 300.11 `CONFIG_RPI_PICO_BINARY_INFO_OVERRIDE_BOOT_STAGE2_NAME`

**提示（Prompt）**：覆盖二进制信息中的第二阶段启动名称（boot_stage2_name）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO_BOOT_STAGE2_NAME && CONFIG_RPI_PICO_BINARY_INFO_BOOT_STAGE2_NAME && CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info） → 在二进制信息中生成第二阶段启动名称（boot_stage2_name）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO_BOOT_STAGE2_NAME`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO_BOOT_STAGE2_NAME)、[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_OVERRIDE_PICO_BOARD"></a>

## 300.12 `CONFIG_RPI_PICO_BINARY_INFO_OVERRIDE_PICO_BOARD`

**提示（Prompt）**：覆盖二进制信息中的 Pico 开发板标识（pico_board）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO_PICO_BOARD && CONFIG_RPI_PICO_BINARY_INFO_PICO_BOARD && CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info） → 在二进制信息中生成 Pico 开发板标识（pico_board）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO_PICO_BOARD`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO_PICO_BOARD)、[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_OVERRIDE_PROGRAM_BUILD_DATE"></a>

## 300.13 `CONFIG_RPI_PICO_BINARY_INFO_OVERRIDE_PROGRAM_BUILD_DATE`

**提示（Prompt）**：覆盖二进制信息中的程序构建日期（program_build_date）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_BUILD_DATE && CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_BUILD_DATE && CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info） → 在二进制信息中生成程序构建日期（program_build_date）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_BUILD_DATE`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_BUILD_DATE)、[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_OVERRIDE_PROGRAM_DESCRIPTION"></a>

## 300.14 `CONFIG_RPI_PICO_BINARY_INFO_OVERRIDE_PROGRAM_DESCRIPTION`

**提示（Prompt）**：覆盖二进制信息中的程序说明（program_description）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_DESCRIPTION && CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_DESCRIPTION && CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info） → 在二进制信息中生成程序说明（program_description）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_DESCRIPTION`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_DESCRIPTION)、[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_OVERRIDE_PROGRAM_NAME"></a>

## 300.15 `CONFIG_RPI_PICO_BINARY_INFO_OVERRIDE_PROGRAM_NAME`

**提示（Prompt）**：覆盖二进制信息中的程序名称（program_name）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_NAME && CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_NAME && CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info） → 在二进制信息中生成程序名称（program_name）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_NAME`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_NAME)、[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_OVERRIDE_PROGRAM_URL"></a>

## 300.16 `CONFIG_RPI_PICO_BINARY_INFO_OVERRIDE_PROGRAM_URL`

**提示（Prompt）**：覆盖二进制信息中的程序网址（program_url）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_URL && CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_URL && CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info） → 在二进制信息中生成程序网址（program_url）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_URL`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_URL)、[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_OVERRIDE_PROGRAM_VERSION_STRING"></a>

## 300.17 `CONFIG_RPI_PICO_BINARY_INFO_OVERRIDE_PROGRAM_VERSION_STRING`

**提示（Prompt）**：覆盖二进制信息中的程序版本字符串（program_version_string）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_VERSION_STRING && CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_VERSION_STRING && CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info） → 在二进制信息中生成程序版本字符串（program_version_string）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_VERSION_STRING`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_VERSION_STRING)、[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_OVERRIDE_SDK_VERSION_STRING"></a>

## 300.18 `CONFIG_RPI_PICO_BINARY_INFO_OVERRIDE_SDK_VERSION_STRING`

**提示（Prompt）**：覆盖二进制信息中的 SDK 版本字符串（sdk_version_string）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO_SDK_VERSION_STRING && CONFIG_RPI_PICO_BINARY_INFO_SDK_VERSION_STRING && CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info） → 在二进制信息中生成 SDK 版本字符串（sdk_version_string）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO_SDK_VERSION_STRING`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO_SDK_VERSION_STRING)、[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_PICO_BOARD"></a>

## 300.19 `CONFIG_RPI_PICO_BINARY_INFO_PICO_BOARD`

**提示（Prompt）**：在二进制信息中生成 Pico 开发板标识（pico_board）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_PIN_CONFIGURATIONS"></a>

## 300.20 `CONFIG_RPI_PICO_BINARY_INFO_PIN_CONFIGURATIONS`

**提示（Prompt）**：在二进制信息中生成引脚配置信息（pin configuration info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_BUILD_DATE"></a>

## 300.21 `CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_BUILD_DATE`

**提示（Prompt）**：在二进制信息中生成程序构建日期（program_build_date）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_DESCRIPTION"></a>

## 300.22 `CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_DESCRIPTION`

**提示（Prompt）**：在二进制信息中生成程序说明（program_description）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_NAME"></a>

## 300.23 `CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_NAME`

**提示（Prompt）**：在二进制信息中生成程序名称（program_name）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_URL"></a>

## 300.24 `CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_URL`

**提示（Prompt）**：在二进制信息中生成程序网址（program_url）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_VERSION_STRING"></a>

## 300.25 `CONFIG_RPI_PICO_BINARY_INFO_PROGRAM_VERSION_STRING`

**提示（Prompt）**：在二进制信息中生成程序版本字符串（program_version_string）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_BINARY_INFO_SDK_VERSION_STRING"></a>

## 300.26 `CONFIG_RPI_PICO_BINARY_INFO_SDK_VERSION_STRING`

**提示（Prompt）**：在二进制信息中生成 SDK 版本字符串（sdk_version_string）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPI_PICO_BINARY_INFO && CONFIG_SOC_FAMILY_RPI_PICO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/common/Kconfig.binary_info:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/common/Kconfig.binary_info#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 生成 Raspberry Pi Pico 二进制信息（binary info）

**配置项引用（Symbol References）**：[`CONFIG_RPI_PICO_BINARY_INFO`](P300_soc_raspberrypi_配置项参考.md#CONFIG_RPI_PICO_BINARY_INFO)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_SIGNING_KEY"></a>

## 300.27 `CONFIG_RPI_PICO_SIGNING_KEY`

**提示（Prompt）**：安全启动签名密钥（Secure boot signing key）

**说明（Help）**

提供私钥路径，用于为安全启动（secure boot）签署镜像。密钥必须采用 PEM 格式，并满足 picotool 工具的要求，详情请参阅 picotool 文档。设置此配置后，`west sign` 命令可生成已签名 ELF 文件。如果未提供此配置，则不能使用 `west sign`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RPI_PICO
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2350/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2350/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_RPI_PICO_USE_ROMFUNC"></a>

## 300.28 `CONFIG_RPI_PICO_USE_ROMFUNC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 ROM 函数的使用，并在需要时添加对应的内存保护单元条目（MPU entry）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NULL_POINTER_EXCEPTION_DETECTION_MPU && CONFIG_SOC_FAMILY_RPI_PICO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_NULL_POINTER_EXCEPTION_DETECTION_MPU`](P030_arch_arm_配置项参考_2.md#CONFIG_NULL_POINTER_EXCEPTION_DETECTION_MPU)、[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`。

<a id="CONFIG_SOC_RP2350A_HAZARD3"></a>

## 300.29 `CONFIG_SOC_RP2350A_HAZARD3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 RP2350A，并在两个内核位置（sockets）均选择 Hazard3 内核。此项已弃用，请改用 `SOC_RP2350A_HAZARD3_0`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_RP2350A_HAZARD3_0
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_RP2350A_HAZARD3_0`](P300_soc_raspberrypi_配置项参考.md#CONFIG_SOC_RP2350A_HAZARD3_0)。

<a id="CONFIG_SOC_RP2350A_HAZARD3_0"></a>

## 300.30 `CONFIG_SOC_RP2350A_HAZARD3_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 RP2350A，CPU0 为 Hazard3 内核。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_RP2350A
```

**被选择（Selected by）**

```text
CONFIG_BOARD_BEETLE_RP2350
CONFIG_BOARD_RPI_PICO2
CONFIG_BOARD_XIAO_RP2350
CONFIG_BOARD_RP2350_ZERO
CONFIG_BOARD_MOTION_2350_PRO
CONFIG_SOC_RP2350A_HAZARD3
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_RP2350A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350A)、[`CONFIG_BOARD_BEETLE_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_BEETLE_RP2350)、[`CONFIG_BOARD_RPI_PICO2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RPI_PICO2)、[`CONFIG_BOARD_XIAO_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XIAO_RP2350)、[`CONFIG_BOARD_RP2350_ZERO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RP2350_ZERO)、[`CONFIG_BOARD_MOTION_2350_PRO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MOTION_2350_PRO)、[`CONFIG_SOC_RP2350A_HAZARD3`](P300_soc_raspberrypi_配置项参考.md#CONFIG_SOC_RP2350A_HAZARD3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_RP2350A`、`CONFIG_BOARD_BEETLE_RP2350`、`CONFIG_BOARD_RPI_PICO2`、`CONFIG_BOARD_XIAO_RP2350`、`CONFIG_BOARD_RP2350_ZERO`、`CONFIG_BOARD_MOTION_2350_PRO`。

<a id="CONFIG_SOC_RP2350A_M33"></a>

## 300.31 `CONFIG_SOC_RP2350A_M33`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 RP2350A，并在两个内核位置（sockets）均选择 Cortex-M33 内核。此项已弃用，请改用 `SOC_RP2350A_M33_0`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_RP2350A_M33_0
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_RP2350A_M33_0`](P300_soc_raspberrypi_配置项参考.md#CONFIG_SOC_RP2350A_M33_0)。

<a id="CONFIG_SOC_RP2350A_M33_0"></a>

## 300.32 `CONFIG_SOC_RP2350A_M33_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 RP2350A，CPU0 为 Cortex-M33 内核。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_RP2350A
```

**被选择（Selected by）**

```text
CONFIG_BOARD_BEETLE_RP2350
CONFIG_BOARD_RPI_PICO2
CONFIG_BOARD_W5500_EVB_PICO2
CONFIG_BOARD_W6300_EVB_PICO2
CONFIG_BOARD_W6100_EVB_PICO2
CONFIG_BOARD_XIAO_RP2350
CONFIG_BOARD_RP2350_ZERO
CONFIG_BOARD_PICO2_SPE
CONFIG_BOARD_MOTION_2350_PRO
CONFIG_SOC_RP2350A_M33
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_RP2350A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350A)、[`CONFIG_BOARD_BEETLE_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_BEETLE_RP2350)、[`CONFIG_BOARD_RPI_PICO2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RPI_PICO2)、[`CONFIG_BOARD_W5500_EVB_PICO2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_W5500_EVB_PICO2)、[`CONFIG_BOARD_W6300_EVB_PICO2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_W6300_EVB_PICO2)、[`CONFIG_BOARD_W6100_EVB_PICO2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_W6100_EVB_PICO2)、[`CONFIG_BOARD_XIAO_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_XIAO_RP2350)、[`CONFIG_BOARD_RP2350_ZERO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RP2350_ZERO)、[`CONFIG_BOARD_PICO2_SPE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_PICO2_SPE)、[`CONFIG_BOARD_MOTION_2350_PRO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_MOTION_2350_PRO)、[`CONFIG_SOC_RP2350A_M33`](P300_soc_raspberrypi_配置项参考.md#CONFIG_SOC_RP2350A_M33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_RP2350A`、`CONFIG_BOARD_BEETLE_RP2350`、`CONFIG_BOARD_RPI_PICO2`、`CONFIG_BOARD_W5500_EVB_PICO2`、`CONFIG_BOARD_W6300_EVB_PICO2`、`CONFIG_BOARD_W6100_EVB_PICO2`、`CONFIG_BOARD_XIAO_RP2350`、`CONFIG_BOARD_RP2350_ZERO`、`CONFIG_BOARD_PICO2_SPE`、`CONFIG_BOARD_MOTION_2350_PRO`。

<a id="CONFIG_SOC_RP2350B_HAZARD3"></a>

## 300.33 `CONFIG_SOC_RP2350B_HAZARD3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 RP2350B，并在两个内核位置（sockets）均选择 Hazard3 内核。此项已弃用，请改用 `SOC_RP2350B_HAZARD3_0`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_RP2350B_HAZARD3_0
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_RP2350B_HAZARD3_0`](P300_soc_raspberrypi_配置项参考.md#CONFIG_SOC_RP2350B_HAZARD3_0)。

<a id="CONFIG_SOC_RP2350B_HAZARD3_0"></a>

## 300.34 `CONFIG_SOC_RP2350B_HAZARD3_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 RP2350B，CPU0 为 Hazard3 内核。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_RP2350B
```

**被选择（Selected by）**

```text
CONFIG_BOARD_CORE2350B
CONFIG_BOARD_RP2350B_PLUS_W
CONFIG_BOARD_PICO_PLUS2
CONFIG_BOARD_RP2350B_CORE
CONFIG_SOC_RP2350B_HAZARD3
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_RP2350B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350B)、[`CONFIG_BOARD_CORE2350B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CORE2350B)、[`CONFIG_BOARD_RP2350B_PLUS_W`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RP2350B_PLUS_W)、[`CONFIG_BOARD_PICO_PLUS2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_PICO_PLUS2)、[`CONFIG_BOARD_RP2350B_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RP2350B_CORE)、[`CONFIG_SOC_RP2350B_HAZARD3`](P300_soc_raspberrypi_配置项参考.md#CONFIG_SOC_RP2350B_HAZARD3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_RP2350B`、`CONFIG_BOARD_CORE2350B`、`CONFIG_BOARD_RP2350B_PLUS_W`、`CONFIG_BOARD_PICO_PLUS2`、`CONFIG_BOARD_RP2350B_CORE`。

<a id="CONFIG_SOC_RP2350B_M33"></a>

## 300.35 `CONFIG_SOC_RP2350B_M33`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 RP2350B，并在两个内核位置（sockets）均选择 Cortex-M33 内核。此项已弃用，请改用 `SOC_RP2350B_M33_0`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_RP2350B_M33_0
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_RP2350B_M33_0`](P300_soc_raspberrypi_配置项参考.md#CONFIG_SOC_RP2350B_M33_0)。

<a id="CONFIG_SOC_RP2350B_M33_0"></a>

## 300.36 `CONFIG_SOC_RP2350B_M33_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 RP2350B，CPU0 为 Cortex-M33 内核。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_RP2350B
```

**被选择（Selected by）**

```text
CONFIG_BOARD_ADAFRUIT_METRO_RP2350
CONFIG_BOARD_CORE2350B
CONFIG_BOARD_RP2350B_PLUS_W
CONFIG_BOARD_PICO_PLUS2
CONFIG_BOARD_RP2350B_CORE
CONFIG_SOC_RP2350B_M33
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_RP2350B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350B)、[`CONFIG_BOARD_ADAFRUIT_METRO_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_METRO_RP2350)、[`CONFIG_BOARD_CORE2350B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CORE2350B)、[`CONFIG_BOARD_RP2350B_PLUS_W`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RP2350B_PLUS_W)、[`CONFIG_BOARD_PICO_PLUS2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_PICO_PLUS2)、[`CONFIG_BOARD_RP2350B_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_RP2350B_CORE)、[`CONFIG_SOC_RP2350B_M33`](P300_soc_raspberrypi_配置项参考.md#CONFIG_SOC_RP2350B_M33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_RP2350B`、`CONFIG_BOARD_ADAFRUIT_METRO_RP2350`、`CONFIG_BOARD_CORE2350B`、`CONFIG_BOARD_RP2350B_PLUS_W`、`CONFIG_BOARD_PICO_PLUS2`、`CONFIG_BOARD_RP2350B_CORE`。

<a id="CONFIG_SOC_SERIES_RP2040"></a>

## 300.37 `CONFIG_SOC_SERIES_RP2040`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Raspberry Pi RP2040 微控制器系列支持（MCU series）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_RPI_PICO
```

**主动选择（Selects）**

```text
CONFIG_ARM
CONFIG_CPU_CORTEX_M0PLUS
CONFIG_CPU_CORTEX_M_HAS_SYSTICK
CONFIG_CPU_CORTEX_M_HAS_VTOR
CONFIG_CPU_HAS_ARM_MPU
CONFIG_HAS_RPI_PICO
CONFIG_HAS_SEGGER_RTT if CONFIG_ZEPHYR_SEGGER_MODULE
```

**被选择（Selected by）**

```text
CONFIG_SOC_RP2040
```

**弱选择（Implies）**

```text
CONFIG_XIP
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2040/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2040/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RPI_PICO)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_CPU_CORTEX_M0PLUS`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M0PLUS)、[`CONFIG_CPU_CORTEX_M_HAS_SYSTICK`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_SYSTICK)、[`CONFIG_CPU_CORTEX_M_HAS_VTOR`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_CORTEX_M_HAS_VTOR)、[`CONFIG_CPU_HAS_ARM_MPU`](P030_arch_arm_配置项参考_2.md#CONFIG_CPU_HAS_ARM_MPU)、[`CONFIG_HAS_RPI_PICO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_RPI_PICO)、[`CONFIG_HAS_SEGGER_RTT`](P249_modules_segger_配置项参考.md#CONFIG_HAS_SEGGER_RTT)、[`CONFIG_ZEPHYR_SEGGER_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_SEGGER_MODULE)、[`CONFIG_SOC_RP2040`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2040)、[`CONFIG_XIP`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XIP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RPI_PICO`、`CONFIG_HAS_RPI_PICO`、`CONFIG_ZEPHYR_SEGGER_MODULE`、`CONFIG_SOC_RP2040`。

<a id="SB_CONFIG_SOC_RP2350A_HAZARD3"></a>

## 300.38 `SB_CONFIG_SOC_RP2350A_HAZARD3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 RP2350A，并在两个内核位置（sockets）均选择 Hazard3 内核。此项已弃用，请改用 `SOC_RP2350A_HAZARD3_0`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_RP2350A_HAZARD3_0
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_RP2350A_HAZARD3_0`](P300_soc_raspberrypi_配置项参考.md#SB_CONFIG_SOC_RP2350A_HAZARD3_0)。

<a id="SB_CONFIG_SOC_RP2350A_HAZARD3_0"></a>

## 300.39 `SB_CONFIG_SOC_RP2350A_HAZARD3_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 RP2350A，CPU0 为 Hazard3 内核。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_RP2350A
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_BEETLE_RP2350
SB_CONFIG_BOARD_RPI_PICO2
SB_CONFIG_BOARD_XIAO_RP2350
SB_CONFIG_BOARD_RP2350_ZERO
SB_CONFIG_BOARD_MOTION_2350_PRO
SB_CONFIG_SOC_RP2350A_HAZARD3
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc#L24)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_RP2350A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_RP2350A)、[`SB_CONFIG_BOARD_BEETLE_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_BEETLE_RP2350)、[`SB_CONFIG_BOARD_RPI_PICO2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RPI_PICO2)、[`SB_CONFIG_BOARD_XIAO_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_XIAO_RP2350)、[`SB_CONFIG_BOARD_RP2350_ZERO`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RP2350_ZERO)、[`SB_CONFIG_BOARD_MOTION_2350_PRO`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MOTION_2350_PRO)、[`SB_CONFIG_SOC_RP2350A_HAZARD3`](P300_soc_raspberrypi_配置项参考.md#SB_CONFIG_SOC_RP2350A_HAZARD3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_RP2350A`、`SB_CONFIG_BOARD_BEETLE_RP2350`、`SB_CONFIG_BOARD_RPI_PICO2`、`SB_CONFIG_BOARD_XIAO_RP2350`、`SB_CONFIG_BOARD_RP2350_ZERO`、`SB_CONFIG_BOARD_MOTION_2350_PRO`。

<a id="SB_CONFIG_SOC_RP2350A_M33"></a>

## 300.40 `SB_CONFIG_SOC_RP2350A_M33`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 RP2350A，并在两个内核位置（sockets）均选择 Cortex-M33 内核。此项已弃用，请改用 `SOC_RP2350A_M33_0`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_RP2350A_M33_0
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc#L30)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_RP2350A_M33_0`](P300_soc_raspberrypi_配置项参考.md#SB_CONFIG_SOC_RP2350A_M33_0)。

<a id="SB_CONFIG_SOC_RP2350A_M33_0"></a>

## 300.41 `SB_CONFIG_SOC_RP2350A_M33_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 RP2350A，CPU0 为 Cortex-M33 内核。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_RP2350A
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_BEETLE_RP2350
SB_CONFIG_BOARD_RPI_PICO2
SB_CONFIG_BOARD_W5500_EVB_PICO2
SB_CONFIG_BOARD_W6300_EVB_PICO2
SB_CONFIG_BOARD_W6100_EVB_PICO2
SB_CONFIG_BOARD_XIAO_RP2350
SB_CONFIG_BOARD_RP2350_ZERO
SB_CONFIG_BOARD_PICO2_SPE
SB_CONFIG_BOARD_MOTION_2350_PRO
SB_CONFIG_SOC_RP2350A_M33
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc#L37)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_RP2350A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_RP2350A)、[`SB_CONFIG_BOARD_BEETLE_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_BEETLE_RP2350)、[`SB_CONFIG_BOARD_RPI_PICO2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RPI_PICO2)、[`SB_CONFIG_BOARD_W5500_EVB_PICO2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_W5500_EVB_PICO2)、[`SB_CONFIG_BOARD_W6300_EVB_PICO2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_W6300_EVB_PICO2)、[`SB_CONFIG_BOARD_W6100_EVB_PICO2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_W6100_EVB_PICO2)、[`SB_CONFIG_BOARD_XIAO_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_XIAO_RP2350)、[`SB_CONFIG_BOARD_RP2350_ZERO`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RP2350_ZERO)、[`SB_CONFIG_BOARD_PICO2_SPE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_PICO2_SPE)、[`SB_CONFIG_BOARD_MOTION_2350_PRO`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MOTION_2350_PRO)、[`SB_CONFIG_SOC_RP2350A_M33`](P300_soc_raspberrypi_配置项参考.md#SB_CONFIG_SOC_RP2350A_M33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_RP2350A`、`SB_CONFIG_BOARD_BEETLE_RP2350`、`SB_CONFIG_BOARD_RPI_PICO2`、`SB_CONFIG_BOARD_W5500_EVB_PICO2`、`SB_CONFIG_BOARD_W6300_EVB_PICO2`、`SB_CONFIG_BOARD_W6100_EVB_PICO2`、`SB_CONFIG_BOARD_XIAO_RP2350`、`SB_CONFIG_BOARD_RP2350_ZERO`、`SB_CONFIG_BOARD_PICO2_SPE`、`SB_CONFIG_BOARD_MOTION_2350_PRO`。

<a id="SB_CONFIG_SOC_RP2350B_HAZARD3"></a>

## 300.42 `SB_CONFIG_SOC_RP2350B_HAZARD3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 RP2350B，并在两个内核位置（sockets）均选择 Hazard3 内核。此项已弃用，请改用 `SOC_RP2350B_HAZARD3_0`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_RP2350B_HAZARD3_0
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc#L47)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_RP2350B_HAZARD3_0`](P300_soc_raspberrypi_配置项参考.md#SB_CONFIG_SOC_RP2350B_HAZARD3_0)。

<a id="SB_CONFIG_SOC_RP2350B_HAZARD3_0"></a>

## 300.43 `SB_CONFIG_SOC_RP2350B_HAZARD3_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 RP2350B，CPU0 为 Hazard3 内核。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_RP2350B
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_CORE2350B
SB_CONFIG_BOARD_RP2350B_PLUS_W
SB_CONFIG_BOARD_PICO_PLUS2
SB_CONFIG_BOARD_RP2350B_CORE
SB_CONFIG_SOC_RP2350B_HAZARD3
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc#L54)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_RP2350B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_RP2350B)、[`SB_CONFIG_BOARD_CORE2350B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CORE2350B)、[`SB_CONFIG_BOARD_RP2350B_PLUS_W`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RP2350B_PLUS_W)、[`SB_CONFIG_BOARD_PICO_PLUS2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_PICO_PLUS2)、[`SB_CONFIG_BOARD_RP2350B_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RP2350B_CORE)、[`SB_CONFIG_SOC_RP2350B_HAZARD3`](P300_soc_raspberrypi_配置项参考.md#SB_CONFIG_SOC_RP2350B_HAZARD3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_RP2350B`、`SB_CONFIG_BOARD_CORE2350B`、`SB_CONFIG_BOARD_RP2350B_PLUS_W`、`SB_CONFIG_BOARD_PICO_PLUS2`、`SB_CONFIG_BOARD_RP2350B_CORE`。

<a id="SB_CONFIG_SOC_RP2350B_M33"></a>

## 300.44 `SB_CONFIG_SOC_RP2350B_M33`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 RP2350B，并在两个内核位置（sockets）均选择 Cortex-M33 内核。此项已弃用，请改用 `SOC_RP2350B_M33_0`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_RP2350B_M33_0
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc#L60)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_RP2350B_M33_0`](P300_soc_raspberrypi_配置项参考.md#SB_CONFIG_SOC_RP2350B_M33_0)。

<a id="SB_CONFIG_SOC_RP2350B_M33_0"></a>

## 300.45 `SB_CONFIG_SOC_RP2350B_M33_0`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用 RP2350B，CPU0 为 Cortex-M33 内核。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_RP2350B
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ADAFRUIT_METRO_RP2350
SB_CONFIG_BOARD_CORE2350B
SB_CONFIG_BOARD_RP2350B_PLUS_W
SB_CONFIG_BOARD_PICO_PLUS2
SB_CONFIG_BOARD_RP2350B_CORE
SB_CONFIG_SOC_RP2350B_M33
```

**定义位置（Location）**：[`soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/raspberrypi/rpi_pico/rp2350/Kconfig.soc#L67)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_RP2350B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_RP2350B)、[`SB_CONFIG_BOARD_ADAFRUIT_METRO_RP2350`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_METRO_RP2350)、[`SB_CONFIG_BOARD_CORE2350B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CORE2350B)、[`SB_CONFIG_BOARD_RP2350B_PLUS_W`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RP2350B_PLUS_W)、[`SB_CONFIG_BOARD_PICO_PLUS2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_PICO_PLUS2)、[`SB_CONFIG_BOARD_RP2350B_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RP2350B_CORE)、[`SB_CONFIG_SOC_RP2350B_M33`](P300_soc_raspberrypi_配置项参考.md#SB_CONFIG_SOC_RP2350B_M33)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_RP2350B`、`SB_CONFIG_BOARD_ADAFRUIT_METRO_RP2350`、`SB_CONFIG_BOARD_CORE2350B`、`SB_CONFIG_BOARD_RP2350B_PLUS_W`、`SB_CONFIG_BOARD_PICO_PLUS2`、`SB_CONFIG_BOARD_RP2350B_CORE`。

<!-- kconfig-navigation -->

[上一章](P299_soc_quicklogic_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P301_soc_realtek_配置项参考.md)
