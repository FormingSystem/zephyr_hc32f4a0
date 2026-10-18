---
id: learning.zephyr-docs.kconfig-reference.page-339
title: "`subsys/dfu`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第339章\_`subsys/dfu`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/dfu` 的 10 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_IMG_BLOCK_BUF_SIZE"></a>

## 339.1 `CONFIG_IMG_BLOCK_BUF_SIZE`

**提示（Prompt）**：映像写入器缓冲区大小（Image writer buffer size）

**说明（Help）**

映像写入器（image writer）的缓冲区大小，单位为字节，必须是所用闪存驱动要求的访问对齐（access alignment）大小的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUBOOT_IMG_MANAGER && CONFIG_IMG_MANAGER
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`subsys/dfu/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dfu/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备固件更新映像管理器（DFU image manager）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_MCUBOOT_IMG_MANAGER)、[`CONFIG_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_MANAGER)。

<a id="CONFIG_IMG_CUSTOM_SECTOR_SIZE"></a>

## 339.2 `CONFIG_IMG_CUSTOM_SECTOR_SIZE`

**提示（Prompt）**：MCUboot 映像的扇区大小（sector size）

**说明（Help）**

为采用偏移交换（swap-using-offset）的映像设置自定义偏移扇区大小。值为 `0` 时，通过查询闪存区域取得其默认扇区大小。仅当高级用户为了优化，在 MCUboot 映像中使用不同的擦除扇区大小时才应手动设置，例如为了减小交换状态区域（swap status area）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_OFFSET && CONFIG_MCUBOOT_IMG_MANAGER && CONFIG_IMG_MANAGER
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4294967295]
```

**定义位置（Location）**：[`subsys/dfu/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dfu/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备固件更新映像管理器（DFU image manager）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_OFFSET`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_OFFSET)、[`CONFIG_MCUBOOT_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_MCUBOOT_IMG_MANAGER)、[`CONFIG_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_MANAGER)。

<a id="CONFIG_IMG_ENABLE_IMAGE_CHECK"></a>

## 339.3 `CONFIG_IMG_ENABLE_IMAGE_CHECK`

**提示（Prompt）**：映像检查函数（Image check functions）

**说明（Help）**

启用后提供检查闪存完整性（flash integrity）的函数，可用于接收新固件后验证闪存完整性，从而避免通过重启固件再测试的方式检查。还可用于确认从互联网服务器到闪存槽位（flash slot）的固件升级例程正常工作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUBOOT_IMG_MANAGER && CONFIG_IMG_MANAGER
```

**主动选择（Selects）**

```text
CONFIG_FLASH_AREA_CHECK_INTEGRITY
```

**被选择（Selected by）**

```text
CONFIG_HAWKBIT
CONFIG_FOTA_HTTP_SHA256_CHECK
CONFIG_UPDATEHUB
```

**定义位置（Location）**：[`subsys/dfu/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dfu/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备固件更新映像管理器（DFU image manager）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_MCUBOOT_IMG_MANAGER)、[`CONFIG_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_MANAGER)、[`CONFIG_FLASH_AREA_CHECK_INTEGRITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_AREA_CHECK_INTEGRITY)、[`CONFIG_HAWKBIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAWKBIT)、[`CONFIG_FOTA_HTTP_SHA256_CHECK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP_SHA256_CHECK)、[`CONFIG_UPDATEHUB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UPDATEHUB)。

<a id="CONFIG_IMG_ERASE_PROGRESSIVELY"></a>

## 339.4 `CONFIG_IMG_ERASE_PROGRESSIVELY`

**提示（Prompt）**：接收新固件时逐步擦除闪存（progressive erase）

**说明（Help）**

启用后，在接收新固件时按需擦除闪存，而不是一次擦除整个映像槽位（image slot）。某些硬件的擦除时间较长，需要此功能来避免设备固件更新（DFU）开始时长时间等待。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUBOOT_IMG_MANAGER && CONFIG_IMG_MANAGER
```

**主动选择（Selects）**

```text
CONFIG_STREAM_FLASH_ERASE if CONFIG_FLASH_HAS_EXPLICIT_ERASE
```

**被选择（Selected by）**

```text
CONFIG_HAWKBIT
CONFIG_FOTA_HTTP
CONFIG_USB_DFU_CLASS
```

**定义位置（Location）**：[`subsys/dfu/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dfu/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备固件更新映像管理器（DFU image manager）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_MCUBOOT_IMG_MANAGER)、[`CONFIG_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_MANAGER)、[`CONFIG_STREAM_FLASH_ERASE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STREAM_FLASH_ERASE)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_HAWKBIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAWKBIT)、[`CONFIG_FOTA_HTTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP)、[`CONFIG_USB_DFU_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DFU_CLASS)。

<a id="CONFIG_IMG_MANAGER"></a>

## 339.5 `CONFIG_IMG_MANAGER`

**提示（Prompt）**：设备固件更新映像管理器（DFU image manager）

**说明（Help）**

启用设备固件更新（DFU）映像管理支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STREAM_FLASH && (!CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD || CONFIG_RETENTION_BOOTLOADER_INFO_OUTPUT_FUNCTION) && (!CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT || CONFIG_RETENTION_BOOTLOADER_INFO_OUTPUT_FUNCTION)
```

**定义位置（Location）**：[`subsys/dfu/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dfu/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_STREAM_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STREAM_FLASH)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD)、[`CONFIG_RETENTION_BOOTLOADER_INFO_OUTPUT_FUNCTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RETENTION_BOOTLOADER_INFO_OUTPUT_FUNCTION)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT)。

<a id="CONFIG_MCUBOOT_IMG_MANAGER"></a>

## 339.6 `CONFIG_MCUBOOT_IMG_MANAGER`

**提示（Prompt）**：MCUboot 映像管理器（Image manager）

**说明（Help）**

启用对使用 MCUboot 下载的设备固件更新（DFU）映像的管理支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MAP && <choice>
```

**主动选择（Selects）**

```text
CONFIG_MCUBOOT_BOOTUTIL_LIB
```

**定义位置（Location）**：[`subsys/dfu/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dfu/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备固件更新映像管理器（DFU image manager） → 映像管理器（Image manager）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MAP)、[`CONFIG_MCUBOOT_BOOTUTIL_LIB`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTUTIL_LIB)。

<a id="CONFIG_MCUBOOT_SHELL"></a>

## 339.7 `CONFIG_MCUBOOT_SHELL`

**提示（Prompt）**：MCUboot 命令行（shell）

**说明（Help）**

启用命令行模块（shell module），用于提供映像槽位（image slots）信息，并执行确认（confirm）、擦除（erase）和请求升级（request upgrade）等操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_MCUBOOT_IMG_MANAGER && CONFIG_IMG_MANAGER
```

**定义位置（Location）**：[`subsys/dfu/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dfu/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备固件更新映像管理器（DFU image manager）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_MCUBOOT_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_MCUBOOT_IMG_MANAGER)、[`CONFIG_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_MANAGER)。

<a id="CONFIG_MCUBOOT_TRAILER_SWAP_TYPE"></a>

## 339.8 `CONFIG_MCUBOOT_TRAILER_SWAP_TYPE`

**提示（Prompt）**：使用尾部信息（trailer）的 swap_type 字段

**说明（Help）**

启用交换类型字段（swap type field）。应用 MCUboot 的“修复回退中断后的双重交换（Fix double swap on interrupted revert）”补丁后需要使用此字段，见 https://github.com/JuulLabs-OSS/mcuboot/pull/485 。若需兼容较早版本的 MCUboot，请禁用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUBOOT_IMG_MANAGER && CONFIG_IMG_MANAGER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/dfu/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dfu/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备固件更新映像管理器（DFU image manager）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_MCUBOOT_IMG_MANAGER)、[`CONFIG_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_MANAGER)。

<a id="CONFIG_MCUBOOT_UPDATE_FOOTER_SIZE"></a>

## 339.9 `CONFIG_MCUBOOT_UPDATE_FOOTER_SIZE`

**提示（Prompt）**：估计的更新尾部大小（update footer size）

**说明（Help）**

更新映像数据的估计大小，用于防止加载因过大而无法由 MCUboot 更新的固件。应由系统构建（sysbuild）设置，且仅在启用 `MCUMGR_GRP_IMG_TOO_LARGE_SYSBUILD` 时使用。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUBOOT_IMG_MANAGER && CONFIG_IMG_MANAGER
```

**默认值（Defaults）**

```text
0x0
```

**定义位置（Location）**：[`subsys/dfu/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dfu/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备固件更新映像管理器（DFU image manager）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_MCUBOOT_IMG_MANAGER)、[`CONFIG_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_MANAGER)。

<a id="CONFIG_UPDATEABLE_IMAGE_NUMBER"></a>

## 339.10 `CONFIG_UPDATEABLE_IMAGE_NUMBER`

**提示（Prompt）**：可更新映像数量（Number of updateable images）

**说明（Help）**

若设为 `2` 或更大值，则启用应用结合 MCUboot 多映像启动（multi-image boot）所需的支持。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_MCUBOOT && CONFIG_IMG_MANAGER
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`subsys/dfu/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dfu/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备固件更新映像管理器（DFU image manager）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT)、[`CONFIG_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_MANAGER)。

<!-- kconfig-navigation -->

[上一章](P338_subsys_debug_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P340_subsys_disk_配置项参考.md)
