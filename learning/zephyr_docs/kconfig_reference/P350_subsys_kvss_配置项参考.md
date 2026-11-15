---
id: learning.zephyr-docs.kconfig-reference.page-350
title: "`subsys/kvss`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第350章\_`subsys/kvss`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/kvss` 的 15 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NVS"></a>

## 350.1 `CONFIG_NVS`

**提示（Prompt）**：非易失性存储（Non-volatile Storage）

**说明（Help）**

启用非易失性存储（Non-volatile Storage）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH && CONFIG_FLASH_PAGE_LAYOUT
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`subsys/kvss/nvs/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/kvss/nvs/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_PAGE_LAYOUT`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_PAGE_LAYOUT)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_NVS_DATA_CRC"></a>

## 350.2 `CONFIG_NVS_DATA_CRC`

**提示（Prompt）**：非易失性存储的数据 CRC 保护

**说明（Help）**

为每个非易失性存储（NVS）元素的数据部分启用 CRC-32。分配表项（ATE）的 CRC 不受影响，保持原样。CRC-32 透明地存储在 NVS 数据区的数据字段末尾，因此每个 NVS 元素额外需要 4 字节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NVS
```

**定义位置（Location）**：[`subsys/kvss/nvs/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/kvss/nvs/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → 非易失性存储（Non-volatile Storage）

**配置项引用（Symbol References）**：[`CONFIG_NVS`](P350_subsys_kvss_配置项参考.md#CONFIG_NVS)。

<a id="CONFIG_NVS_INIT_BAD_MEMORY_REGION"></a>

## 350.3 `CONFIG_NVS_INIT_BAD_MEMORY_REGION`

**提示（Prompt）**：非易失性存储的无效内存区域恢复（bad memory region recovery）

**说明（Help）**

允许在不含有效非易失性存储（NVS）的内存区域上自动初始化 NVS。NVS 无效可能源于数据损坏，或提供了非空区域。本选项确保能够创建新的 NVS。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NVS
```

**定义位置（Location）**：[`subsys/kvss/nvs/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/kvss/nvs/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → 非易失性存储（Non-volatile Storage）

**配置项引用（Symbol References）**：[`CONFIG_NVS`](P350_subsys_kvss_配置项参考.md#CONFIG_NVS)。

<a id="CONFIG_NVS_LOOKUP_CACHE"></a>

## 350.4 `CONFIG_NVS_LOOKUP_CACHE`

**提示（Prompt）**：非易失性存储查找缓存（lookup cache）

**说明（Help）**

启用非易失性存储（NVS）缓存，以缩短 NVS 数据查找时间。对于映射到同一缓存位置的所有 NVS ID，每个缓存项保存其中最新分配表项（allocation table entry，ATE）的地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NVS
```

**定义位置（Location）**：[`subsys/kvss/nvs/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/kvss/nvs/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → 非易失性存储（Non-volatile Storage）

**配置项引用（Symbol References）**：[`CONFIG_NVS`](P350_subsys_kvss_配置项参考.md#CONFIG_NVS)。

<a id="CONFIG_NVS_LOOKUP_CACHE_SIZE"></a>

## 350.5 `CONFIG_NVS_LOOKUP_CACHE_SIZE`

**提示（Prompt）**：非易失性存储查找缓存大小

**说明（Help）**

非易失性存储（NVS）查找缓存中的条目数量。建议为 2 的幂。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NVS_LOOKUP_CACHE && CONFIG_NVS
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[1, 65536]
```

**定义位置（Location）**：[`subsys/kvss/nvs/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/kvss/nvs/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → 非易失性存储（Non-volatile Storage） → 非易失性存储查找缓存（lookup cache）

**配置项引用（Symbol References）**：[`CONFIG_NVS_LOOKUP_CACHE`](P350_subsys_kvss_配置项参考.md#CONFIG_NVS_LOOKUP_CACHE)、[`CONFIG_NVS`](P350_subsys_kvss_配置项参考.md#CONFIG_NVS)。

<a id="CONFIG_ZMS"></a>

## 350.6 `CONFIG_ZMS`

**提示（Prompt）**：Zephyr 内存存储（Zephyr Memory Storage）

**说明（Help）**

启用 Zephyr 内存存储（Zephyr Memory Storage，ZMS）。它是为各类非易失性存储技术设计的键值存储系统（key-value storage system），支持传统片上 NOR 闪存，以及电阻式 RAM（RRAM）、磁阻式 RAM（MRAM）等新技术。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`subsys/kvss/zms/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/kvss/zms/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems）

**配置项引用（Symbol References）**：[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_ZMS_CUSTOMIZE_BLOCK_SIZE"></a>

## 350.7 `CONFIG_ZMS_CUSTOMIZE_BLOCK_SIZE`

**提示（Prompt）**：自定义内部读写缓冲区大小

**说明（Help）**

ZMS 使用内部缓冲区读取、写入和比较已存储数据。增大缓冲区时应谨慎，避免栈溢出（stack overflow）。增大后可支持具有较大 `write-block-size` 的存储设备，但原文指出这会降低 ZMS 性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZMS
```

**定义位置（Location）**：[`subsys/kvss/zms/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/kvss/zms/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → Zephyr 内存存储（Zephyr Memory Storage）

**配置项引用（Symbol References）**：[`CONFIG_ZMS`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS)。

<a id="CONFIG_ZMS_CUSTOM_BLOCK_SIZE"></a>

## 350.8 `CONFIG_ZMS_CUSTOM_BLOCK_SIZE`

**提示（Prompt）**：ZMS 内部缓冲区大小（internal buffer size）

**说明（Help）**

更改 ZMS 内部缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZMS_CUSTOMIZE_BLOCK_SIZE && CONFIG_ZMS
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/kvss/zms/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/kvss/zms/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → Zephyr 内存存储（Zephyr Memory Storage） → 自定义内部读写缓冲区大小

**配置项引用（Symbol References）**：[`CONFIG_ZMS_CUSTOMIZE_BLOCK_SIZE`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS_CUSTOMIZE_BLOCK_SIZE)、[`CONFIG_ZMS`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS)。

<a id="CONFIG_ZMS_DATA_CRC"></a>

## 350.9 `CONFIG_ZMS_DATA_CRC`

**提示（Prompt）**：ZMS 数据循环冗余校验（CRC）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ZMS_ID_64BIT && CONFIG_ZMS
```

**定义位置（Location）**：[`subsys/kvss/zms/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/kvss/zms/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → Zephyr 内存存储（Zephyr Memory Storage）

**配置项引用（Symbol References）**：[`CONFIG_ZMS_ID_64BIT`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS_ID_64BIT)、[`CONFIG_ZMS`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS)。

<a id="CONFIG_ZMS_ID_64BIT"></a>

## 350.10 `CONFIG_ZMS_ID_64BIT`

**提示（Prompt）**：64 位 ZMS 标识符（IDs）

**说明（Help）**

启用后，传给 ZMS API 的 `zms_id_t` 值改为 64 位，而不是默认的 32 位。同时会更改内存中分配表项（allocation table entries，ATEs）的格式，以容纳更大的 ID。当前，如果现有文件系统采用不同的 ATE 格式初始化，启用本项将使 ZMS 无法挂载它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZMS
```

**定义位置（Location）**：[`subsys/kvss/zms/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/kvss/zms/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → Zephyr 内存存储（Zephyr Memory Storage）

**配置项引用（Symbol References）**：[`CONFIG_ZMS`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS)。

<a id="CONFIG_ZMS_LOOKUP_CACHE"></a>

## 350.11 `CONFIG_ZMS_LOOKUP_CACHE`

**提示（Prompt）**：ZMS 查找缓存（lookup cache）

**说明（Help）**

启用 ZMS 缓存以缩短数据查找时间。对于映射到同一缓存位置的所有 ZMS ID，每个缓存项保存其中最新分配表项（allocation table entry，ATE）的地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZMS
```

**定义位置（Location）**：[`subsys/kvss/zms/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/kvss/zms/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → Zephyr 内存存储（Zephyr Memory Storage）

**配置项引用（Symbol References）**：[`CONFIG_ZMS`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS)。

<a id="CONFIG_ZMS_LOOKUP_CACHE_FOR_SETTINGS"></a>

## 350.12 `CONFIG_ZMS_LOOKUP_CACHE_FOR_SETTINGS`

**提示（Prompt）**：针对设置子系统优化的 ZMS 存储查找缓存（settings）

**说明（Help）**

启用基于散列（hashes）的查找缓存，以获得最佳 ZMS 性能，前提是 ZMS 仅用于提供设置子系统（settings）的后端。若还会绕过 settings 层直接写入 ZMS，则绝不能启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZMS_LOOKUP_CACHE && CONFIG_SETTINGS_ZMS && !CONFIG_ZMS_ID_64BIT && CONFIG_ZMS
```

**定义位置（Location）**：[`subsys/kvss/zms/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/kvss/zms/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → Zephyr 内存存储（Zephyr Memory Storage）

**配置项引用（Symbol References）**：[`CONFIG_ZMS_LOOKUP_CACHE`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS_LOOKUP_CACHE)、[`CONFIG_SETTINGS_ZMS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS_ZMS)、[`CONFIG_ZMS_ID_64BIT`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS_ID_64BIT)、[`CONFIG_ZMS`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS)。

<a id="CONFIG_ZMS_LOOKUP_CACHE_MANUAL"></a>

## 350.13 `CONFIG_ZMS_LOOKUP_CACHE_MANUAL`

**提示（Prompt）**：手动配置 ZMS 查找缓存（manual lookup cache）

**说明（Help）**

启用手动 ZMS 缓存配置，允许多个 ZMS 分区分别使用各自的缓存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZMS_LOOKUP_CACHE && CONFIG_ZMS
```

**定义位置（Location）**：[`subsys/kvss/zms/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/kvss/zms/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → Zephyr 内存存储（Zephyr Memory Storage） → ZMS 查找缓存（lookup cache）

**配置项引用（Symbol References）**：[`CONFIG_ZMS_LOOKUP_CACHE`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS_LOOKUP_CACHE)、[`CONFIG_ZMS`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS)。

<a id="CONFIG_ZMS_LOOKUP_CACHE_SIZE"></a>

## 350.14 `CONFIG_ZMS_LOOKUP_CACHE_SIZE`

**提示（Prompt）**：ZMS 查找缓存大小（lookup cache size）

**说明（Help）**

ZMS 查找缓存中的条目数量。每增加一个缓存项，消耗 8 字节 RAM。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ZMS_LOOKUP_CACHE && !CONFIG_ZMS_LOOKUP_CACHE_MANUAL && CONFIG_ZMS
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[1, 65536]
```

**定义位置（Location）**：[`subsys/kvss/zms/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/kvss/zms/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → Zephyr 内存存储（Zephyr Memory Storage） → ZMS 查找缓存（lookup cache）

**配置项引用（Symbol References）**：[`CONFIG_ZMS_LOOKUP_CACHE`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS_LOOKUP_CACHE)、[`CONFIG_ZMS_LOOKUP_CACHE_MANUAL`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS_LOOKUP_CACHE_MANUAL)、[`CONFIG_ZMS`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS)。

<a id="CONFIG_ZMS_NO_DOUBLE_WRITE"></a>

## 350.15 `CONFIG_ZMS_NO_DOUBLE_WRITE`

**提示（Prompt）**：避免向存储中重复写入相同数据

**说明（Help）**

某些存储技术的存储单元写入次数有限，应避免不必要的写操作。启用后，如果数据已存在，则不再重复写入。这会降低写入性能，因为每次写入之前都需要在整个存储区域中查找该数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZMS
```

**定义位置（Location）**：[`subsys/kvss/zms/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/kvss/zms/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 键值存储系统（Key-Value Storage Systems） → Zephyr 内存存储（Zephyr Memory Storage）

**配置项引用（Symbol References）**：[`CONFIG_ZMS`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS)。

<!-- kconfig-navigation -->

[上一章](P349_subsys_jwt_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P351_subsys_llext_配置项参考.md)
