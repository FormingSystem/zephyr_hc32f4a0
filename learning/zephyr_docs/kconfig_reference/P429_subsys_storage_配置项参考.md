---
id: learning.zephyr-docs.kconfig-reference.page-429
title: "`subsys/storage`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第429章\_`subsys/storage`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/storage` 的 11 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_FLASH_AREA_CHECK_INTEGRITY"></a>

## 429.1 `CONFIG_FLASH_AREA_CHECK_INTEGRITY`

**提示（Prompt）**：闪存检查函数（Flash check functions）

**说明（Help）**

启用后，提供使用 SHA-256 校验算法检查闪存完整性（Flash integrity）的后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MAP
```

**主动选择（Selects）**

```text
CONFIG_PSA_CRYPTO
CONFIG_PSA_WANT_ALG_SHA_256
```

**被选择（Selected by）**

```text
CONFIG_IMG_ENABLE_IMAGE_CHECK
```

**定义位置（Location）**：[`subsys/storage/flash_map/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/storage/flash_map/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 存储（Storage） → 闪存映射抽象模块（Flash map abstraction module）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MAP`](P429_subsys_storage_配置项参考.md#CONFIG_FLASH_MAP)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_IMG_ENABLE_IMAGE_CHECK`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_ENABLE_IMAGE_CHECK)。

<a id="CONFIG_FLASH_MAP"></a>

## 429.2 `CONFIG_FLASH_MAP`

**提示（Prompt）**：闪存映射抽象模块（Flash map abstraction module）

**说明（Help）**

启用闪存映射抽象（Flash map abstraction）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_HAS_DRIVER_ENABLED
```

**被选择（Selected by）**

```text
CONFIG_DISK_DRIVER_FLASH
CONFIG_DISK_DRIVER_FTL
CONFIG_DEBUG_COREDUMP_BACKEND_FLASH_PARTITION
```

**被弱选择（Implied by）**

```text
CONFIG_OPENTHREAD
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`subsys/storage/flash_map/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/storage/flash_map/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 存储（Storage）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_HAS_DRIVER_ENABLED`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_DRIVER_ENABLED)、[`CONFIG_DISK_DRIVER_FLASH`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_FLASH)、[`CONFIG_DISK_DRIVER_FTL`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_FTL)、[`CONFIG_DEBUG_COREDUMP_BACKEND_FLASH_PARTITION`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND_FLASH_PARTITION)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_FLASH_MAP_CUSTOM"></a>

## 429.3 `CONFIG_FLASH_MAP_CUSTOM`

**提示（Prompt）**：自定义闪存映射描述（Custom flash map description）

**说明（Help）**

启用自定义闪存映射描述（Flash map description）。启用后，用户必须提供自己的描述，替代默认描述。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MAP
```

**定义位置（Location）**：[`subsys/storage/flash_map/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/storage/flash_map/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 存储（Storage） → 闪存映射抽象模块（Flash map abstraction module）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MAP`](P429_subsys_storage_配置项参考.md#CONFIG_FLASH_MAP)。

<a id="CONFIG_FLASH_MAP_LABELS"></a>

## 429.4 `CONFIG_FLASH_MAP_LABELS`

**提示（Prompt）**：运行时访问闪存区域标签（Flash area label）

**说明（Help）**

启用后，可在运行时获取闪存映射（Flash map）的 label 属性。`flash_map list` 命令也会显示可用标签。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MAP
```

**被弱选择（Implied by）**

```text
CONFIG_FLASH_MAP_SHELL
```

**定义位置（Location）**：[`subsys/storage/flash_map/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/storage/flash_map/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 存储（Storage） → 闪存映射抽象模块（Flash map abstraction module）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MAP`](P429_subsys_storage_配置项参考.md#CONFIG_FLASH_MAP)、[`CONFIG_FLASH_MAP_SHELL`](P429_subsys_storage_配置项参考.md#CONFIG_FLASH_MAP_SHELL)。

<a id="CONFIG_FLASH_MAP_SHELL"></a>

## 429.5 `CONFIG_FLASH_MAP_SHELL`

**提示（Prompt）**：闪存映射命令行接口（Flash map shell interface）

**说明（Help）**

启用用于列出和测试闪存映射（Flash map）的命令行命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_FLASH_MAP
```

**弱选择（Implies）**

```text
CONFIG_FLASH_MAP_LABELS
```

**定义位置（Location）**：[`subsys/storage/flash_map/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/storage/flash_map/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 存储（Storage） → 闪存映射抽象模块（Flash map abstraction module）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_FLASH_MAP`](P429_subsys_storage_配置项参考.md#CONFIG_FLASH_MAP)、[`CONFIG_FLASH_MAP_LABELS`](P429_subsys_storage_配置项参考.md#CONFIG_FLASH_MAP_LABELS)。

<a id="CONFIG_STREAM_FLASH"></a>

## 429.6 `CONFIG_STREAM_FLASH`

**提示（Prompt）**：流式写入闪存（Stream to flash）

**说明（Help）**

启用流式闪存写入 API（Stream to flash API）支持

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_DEBUG_COREDUMP_BACKEND_FLASH_PARTITION
```

**定义位置（Location）**：[`subsys/storage/stream/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/storage/stream/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 存储（Storage）

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP_BACKEND_FLASH_PARTITION`](P338_subsys_debug_配置项参考.md#CONFIG_DEBUG_COREDUMP_BACKEND_FLASH_PARTITION)。

<a id="CONFIG_STREAM_FLASH_ERASE"></a>

## 429.7 `CONFIG_STREAM_FLASH_ERASE`

**提示（Prompt）**：执行擦除操作（Erase operation）

**说明（Help）**

禁用时，必须由外部组件擦除将要写入的闪存区域（Flash area）。仅当配置中至少有一个设备要求写入前擦除时，才提供此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_HAS_EXPLICIT_ERASE && CONFIG_STREAM_FLASH
```

**被选择（Selected by）**

```text
CONFIG_IMG_ERASE_PROGRESSIVELY
```

**定义位置（Location）**：[`subsys/storage/stream/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/storage/stream/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 存储（Storage） → 流式写入闪存（Stream to flash）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_STREAM_FLASH`](P429_subsys_storage_配置项参考.md#CONFIG_STREAM_FLASH)、[`CONFIG_IMG_ERASE_PROGRESSIVELY`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_ERASE_PROGRESSIVELY)。

<a id="CONFIG_STREAM_FLASH_ERASE_ONLY_WHEN_SUPPORTED"></a>

## 429.8 `CONFIG_STREAM_FLASH_ERASE_ONLY_WHEN_SUPPORTED`

**提示（Prompt）**：尝试擦除前检查设备是否支持擦除（Erase）

**说明（Help）**

用于流式闪存（Stream Flash）代码，避免对既不要求写入前擦除、也不支持通过擦除提高写入速度的设备调用擦除操作。仅当配置同时包含支持擦除和不支持擦除的设备时，才提供此选项。如果确定不会将 Stream Flash 用于不支持擦除的设备，可禁用此项，从最终应用中省去少量代码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STREAM_FLASH_ERASE && CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE && CONFIG_STREAM_FLASH
```

**定义位置（Location）**：[`subsys/storage/stream/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/storage/stream/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 存储（Storage） → 流式写入闪存（Stream to flash） → 执行擦除操作（Erase operation）

**配置项引用（Symbol References）**：[`CONFIG_STREAM_FLASH_ERASE`](P429_subsys_storage_配置项参考.md#CONFIG_STREAM_FLASH_ERASE)、[`CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE)、[`CONFIG_STREAM_FLASH`](P429_subsys_storage_配置项参考.md#CONFIG_STREAM_FLASH)。

<a id="CONFIG_STREAM_FLASH_INSPECT"></a>

## 429.9 `CONFIG_STREAM_FLASH_INSPECT`

**提示（Prompt）**：检查设备布局是否适合流式闪存（Stream Flash）配置

**说明（Help）**

通过检查缓冲区大小能否容纳在页（Page）内，简单验证给定设备是否适用于流式闪存（Stream Flash）。配置正确并经过测试后，可禁用此选项，减少不再需要的检查代码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_PAGE_LAYOUT && CONFIG_STREAM_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/storage/stream/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/storage/stream/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 存储（Storage） → 流式写入闪存（Stream to flash）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_PAGE_LAYOUT`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_PAGE_LAYOUT)、[`CONFIG_STREAM_FLASH`](P429_subsys_storage_配置项参考.md#CONFIG_STREAM_FLASH)。

<a id="CONFIG_STREAM_FLASH_POST_WRITE_CALLBACK"></a>

## 429.10 `CONFIG_STREAM_FLASH_POST_WRITE_CALLBACK`

**提示（Prompt）**：写入完成回调（Write-complete callback）

**说明（Help）**

启用回调（Callback），在数据从流（Stream）同步到设备后调用。不使用回调时，禁用可节省部分代码存储空间和 RAM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STREAM_FLASH
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/storage/stream/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/storage/stream/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 存储（Storage） → 流式写入闪存（Stream to flash）

**配置项引用（Symbol References）**：[`CONFIG_STREAM_FLASH`](P429_subsys_storage_配置项参考.md#CONFIG_STREAM_FLASH)。

<a id="CONFIG_STREAM_FLASH_PROGRESS"></a>

## 429.11 `CONFIG_STREAM_FLASH_PROGRESS`

**提示（Prompt）**：持久保存流式写入进度（Persistent stream write progress）

**说明（Help）**

启用通过设置子系统（Settings subsystem）将当前写入进度保存到闪存并重新加载的 API。断电或设备复位后，可用该 API 从最近保存的状态继续写入。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS && !CONFIG_SETTINGS_NONE && CONFIG_STREAM_FLASH
```

**定义位置（Location）**：[`subsys/storage/stream/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/storage/stream/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 存储（Storage） → 流式写入闪存（Stream to flash）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)、[`CONFIG_SETTINGS_NONE`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_NONE)、[`CONFIG_STREAM_FLASH`](P429_subsys_storage_配置项参考.md#CONFIG_STREAM_FLASH)。

<!-- kconfig-navigation -->

[上一章](P428_subsys_stats_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P430_subsys_task_wdt_配置项参考.md)
