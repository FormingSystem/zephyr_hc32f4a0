---
id: learning.zephyr-docs.kconfig-reference.page-423
title: "`subsys/settings`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第423章\_`subsys/settings`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/settings` 的 38 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SETTINGS"></a>

## 423.1 `CONFIG_SETTINGS`

**提示（Prompt）**：设置（Settings）。

**说明（Help）**

设置子系统（Settings subsystem）让使用者能够将内存中的状态序列化（Serialize）到非易失性存储器，并从中反序列化（Deserialize）恢复。支持多种后端保存和加载序列化数据，并能针对全部相关模块原子地（Atomically）执行这些操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD
CONFIG_OPENTHREAD
CONFIG_BT_DIS_SETTINGS
```

**定义位置（Location）**：[`subsys/settings/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_BT_DIS_SETTINGS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_DIS_SETTINGS)。

<a id="CONFIG_SETTINGS_BACKEND"></a>

## 423.2 `CONFIG_SETTINGS_BACKEND`

**提示（Prompt）**：存储后端（Storage backend）

**说明（Help）**

设置子系统（Settings subsystem）使用的存储后端（Storage backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS
```

**默认值（Defaults）**

```text
CONFIG_SETTINGS_ZMS if CONFIG_ZMS
CONFIG_SETTINGS_NVS if CONFIG_NVS
CONFIG_SETTINGS_FCB if CONFIG_FCB
CONFIG_SETTINGS_FILE if CONFIG_FILE_SYSTEM
CONFIG_SETTINGS_RETENTION if CONFIG_SETTINGS_SUPPORTED_RETENTION
CONFIG_SETTINGS_NONE
```

**可选项（Choices）**

```text
CONFIG_SETTINGS_ZMS
CONFIG_SETTINGS_FCB
CONFIG_SETTINGS_FILE
CONFIG_SETTINGS_NVS
CONFIG_SETTINGS_RETENTION
CONFIG_SETTINGS_CUSTOM
CONFIG_SETTINGS_TFM_PSA
CONFIG_SETTINGS_NONE
```

**定义位置（Location）**：[`subsys/settings/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)、[`CONFIG_SETTINGS_ZMS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_ZMS)、[`CONFIG_ZMS`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS)、[`CONFIG_SETTINGS_NVS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_NVS)、[`CONFIG_NVS`](P350_subsys_kvss_配置项参考.md#CONFIG_NVS)、[`CONFIG_SETTINGS_FCB`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_FCB)、[`CONFIG_FCB`](P344_subsys_fs_配置项参考.md#CONFIG_FCB)、[`CONFIG_SETTINGS_FILE`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_FILE)、[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)、[`CONFIG_SETTINGS_RETENTION`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_RETENTION)、[`CONFIG_SETTINGS_SUPPORTED_RETENTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS_SUPPORTED_RETENTION)、[`CONFIG_SETTINGS_NONE`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_NONE)、[`CONFIG_SETTINGS_CUSTOM`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_CUSTOM)、[`CONFIG_SETTINGS_TFM_PSA`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_TFM_PSA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SETTINGS_SUPPORTED_RETENTION`。

<a id="CONFIG_SETTINGS_CUSTOM"></a>

## 423.3 `CONFIG_SETTINGS_CUSTOM`

**提示（Prompt）**：自定义（CUSTOM）

**说明（Help）**

使用自定义的设置存储后端（Settings storage backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SETTINGS_BACKEND>
```

**定义位置（Location）**：[`subsys/settings/Kconfig:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 存储后端（Storage backend）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_BACKEND`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_BACKEND)。

<a id="CONFIG_SETTINGS_DYNAMIC_HANDLERS"></a>

## 423.4 `CONFIG_SETTINGS_DYNAMIC_HANDLERS`

**提示（Prompt）**：动态设置处理程序（Dynamic settings handlers）

**说明（Help）**

启用动态设置处理程序（Dynamic settings handler）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/settings/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_FCB"></a>

## 423.5 `CONFIG_SETTINGS_FCB`

**提示（Prompt）**：闪存循环缓冲区（Flash Circular Buffer，FCB）

**说明（Help）**

使用闪存循环缓冲区（FCB）作为设置存储后端（Settings storage backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FCB && <choice CONFIG_SETTINGS_BACKEND>
```

**定义位置（Location）**：[`subsys/settings/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 存储后端（Storage backend）

**配置项引用（Symbol References）**：[`CONFIG_FCB`](P344_subsys_fs_配置项参考.md#CONFIG_FCB)、[`CONFIG_SETTINGS_BACKEND`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_BACKEND)。

<a id="CONFIG_SETTINGS_FCB_MAGIC"></a>

## 423.6 `CONFIG_SETTINGS_FCB_MAGIC`

**提示（Prompt）**：设置子系统的 FCB 魔数（Magic）

**说明（Help）**

用于标识有效设置存储区（Settings area）的 32 位魔数（Magic word）。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_FCB && CONFIG_SETTINGS
```

**默认值（Defaults）**

```text
0xc0ffeeee
```

**定义位置（Location）**：[`subsys/settings/Kconfig:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_FCB`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_FCB)、[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_FCB_NUM_AREAS"></a>

## 423.7 `CONFIG_SETTINGS_FCB_NUM_AREAS`

**提示（Prompt）**：设置子系统使用的闪存区域（Flash area）数量

**说明（Help）**

在设置子系统的闪存循环缓冲区（FCB）中分配的区域数量。如果闪存硬件不支持指定数量，则使用较小的数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_FCB && CONFIG_SETTINGS
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/settings/Kconfig:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_FCB`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_FCB)、[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_FILE"></a>

## 423.8 `CONFIG_SETTINGS_FILE`

**提示（Prompt）**：文件（File）

**说明（Help）**

使用已挂载文件系统中的文件（File）作为设置存储后端（Settings storage backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM && <choice CONFIG_SETTINGS_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_SETTINGS_ENCODE_LEN
```

**定义位置（Location）**：[`subsys/settings/Kconfig:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 存储后端（Storage backend）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)、[`CONFIG_SETTINGS_BACKEND`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_BACKEND)、[`CONFIG_SETTINGS_ENCODE_LEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS_ENCODE_LEN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SETTINGS_ENCODE_LEN`。

<a id="CONFIG_SETTINGS_FILE_MAX_LINES"></a>

## 423.9 `CONFIG_SETTINGS_FILE_MAX_LINES`

**提示（Prompt）**：压缩阈值（Compression threshold）

**说明（Help）**

限制文件中存储多少个条目后进行压缩（Compression）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_FILE && CONFIG_SETTINGS
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/settings/Kconfig:194`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L194)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_FILE`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_FILE)、[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_FILE_PATH"></a>

## 423.10 `CONFIG_SETTINGS_FILE_PATH`

**提示（Prompt）**：默认设置文件（Default settings file）

**说明（Help）**

默认设置文件（Default settings file）的完整路径。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_FILE && CONFIG_SETTINGS
```

**默认值（Defaults）**

```text
"/settings/run"
```

**定义位置（Location）**：[`subsys/settings/Kconfig:187`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L187)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_FILE`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_FILE)、[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_NONE"></a>

## 423.11 `CONFIG_SETTINGS_NONE`

**提示（Prompt）**：无（NONE）

**说明（Help）**

不使用存储后端（Storage backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SETTINGS_BACKEND>
```

**定义位置（Location）**：[`subsys/settings/Kconfig:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 存储后端（Storage backend）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_BACKEND`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_BACKEND)。

<a id="CONFIG_SETTINGS_NVS"></a>

## 423.12 `CONFIG_SETTINGS_NVS`

**提示（Prompt）**：非易失性存储（Non-Volatile Storage，NVS）支持

**说明（Help）**

启用非易失性存储（NVS）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NVS && CONFIG_FLASH_MAP && <choice CONFIG_SETTINGS_BACKEND>
```

**定义位置（Location）**：[`subsys/settings/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 存储后端（Storage backend）

**配置项引用（Symbol References）**：[`CONFIG_NVS`](P350_subsys_kvss_配置项参考.md#CONFIG_NVS)、[`CONFIG_FLASH_MAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MAP)、[`CONFIG_SETTINGS_BACKEND`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_BACKEND)。

<a id="CONFIG_SETTINGS_NVS_NAME_CACHE"></a>

## 423.13 `CONFIG_SETTINGS_NVS_NAME_CACHE`

**提示（Prompt）**：NVS 名称查找缓存（Name lookup cache）

**说明（Help）**

启用 NVS 名称查找缓存（Name lookup cache），以缩短设置项（Settings）名称查找时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_NVS && <choice CONFIG_SETTINGS_BACKEND>
```

**定义位置（Location）**：[`subsys/settings/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 存储后端（Storage backend） → 非易失性存储（Non-Volatile Storage，NVS）支持

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_NVS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_NVS)、[`CONFIG_SETTINGS_BACKEND`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_BACKEND)。

<a id="CONFIG_SETTINGS_NVS_NAME_CACHE_SIZE"></a>

## 423.14 `CONFIG_SETTINGS_NVS_NAME_CACHE_SIZE`

**提示（Prompt）**：NVS 名称查找缓存大小（Name lookup cache size）

**说明（Help）**

设置子系统 NVS 名称缓存（Name cache）中的表项数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_NVS_NAME_CACHE && CONFIG_SETTINGS_NVS && <choice CONFIG_SETTINGS_BACKEND>
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`subsys/settings/Kconfig:130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L130)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 存储后端（Storage backend） → 非易失性存储（Non-Volatile Storage，NVS）支持 → NVS 名称查找缓存（Name lookup cache）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_NVS_NAME_CACHE`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_NVS_NAME_CACHE)、[`CONFIG_SETTINGS_NVS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_NVS)、[`CONFIG_SETTINGS_BACKEND`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_BACKEND)。

<a id="CONFIG_SETTINGS_NVS_SECTOR_COUNT"></a>

## 423.15 `CONFIG_SETTINGS_NVS_SECTOR_COUNT`

**提示（Prompt）**：NVS 设置区域（Settings area）的扇区数量

**说明（Help）**

NVS 设置区域（Settings area）使用的扇区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_NVS && CONFIG_SETTINGS
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/settings/Kconfig:209`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L209)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_NVS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_NVS)、[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_NVS_SECTOR_SIZE_MULT"></a>

## 423.16 `CONFIG_SETTINGS_NVS_SECTOR_SIZE_MULT`

**提示（Prompt）**：NVS 设置区域（Settings area）的扇区大小

**说明（Help）**

NVS 设置区域（Settings area）的扇区大小，以 `FLASH_ERASE_BLOCK_SIZE` 的倍数表示。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_NVS && CONFIG_SETTINGS
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/settings/Kconfig:201`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L201)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_NVS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_NVS)、[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_RETENTION"></a>

## 423.17 `CONFIG_SETTINGS_RETENTION`

**提示（Prompt）**：保留存储（Retention storage）支持

**说明（Help）**

启用保留存储（Retention storage）支持，目前仅支持批量加载与保存（Bulk load/save）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_SUPPORTED_RETENTION && <choice CONFIG_SETTINGS_BACKEND>
```

**定义位置（Location）**：[`subsys/settings/Kconfig:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 存储后端（Storage backend）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_SUPPORTED_RETENTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS_SUPPORTED_RETENTION)、[`CONFIG_SETTINGS_BACKEND`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_BACKEND)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SETTINGS_SUPPORTED_RETENTION`。

<a id="CONFIG_SETTINGS_RUNTIME"></a>

## 423.18 `CONFIG_SETTINGS_RUNTIME`

**提示（Prompt）**：运行时存储后端（Runtime storage backend）

**说明（Help）**

启用运行时存储后端（Runtime storage backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS
```

**定义位置（Location）**：[`subsys/settings/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_SAVE_SINGLE_SUBTREE_WITHOUT_MODIFICATION"></a>

## 423.19 `CONFIG_SETTINGS_SAVE_SINGLE_SUBTREE_WITHOUT_MODIFICATION`

**提示（Prompt）**：不修改值地保存单项或子树（Single/subtree）的函数

**说明（Help）**

包含 `settings_save_subtree_or_single_without_modification()` 函数，可在不改变值的情况下保存一个设置项（Setting）或一棵设置子树（Subtree）。保存单项时，原文要求该设置项支持通过 `h_get()` 函数指针进行读写，并支持读取到足够大的缓冲区中。

译注：原文在此将读写支持都关联到 `h_get()`，这里保留这一表述。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS
```

**定义位置（Location）**：[`subsys/settings/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_SAVE_SINGLE_SUBTREE_WITHOUT_MODIFICATION_VALUE_SIZE"></a>

## 423.20 `CONFIG_SETTINGS_SAVE_SINGLE_SUBTREE_WITHOUT_MODIFICATION_VALUE_SIZE`

**提示（Prompt）**：不修改值地保存单项或子树时的最大值大小（Maximum value size）

**说明（Help）**

使用 `settings_save_subtree_or_single_without_modification()` 可保存的单个设置项（Setting）的最大大小。注意，这会使用栈内存（Stack memory）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_SAVE_SINGLE_SUBTREE_WITHOUT_MODIFICATION && CONFIG_SETTINGS
```

**默认值（Defaults）**

```text
65
```

**定义位置（Location）**：[`subsys/settings/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 不修改值地保存单项或子树（Single/subtree）的函数

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_SAVE_SINGLE_SUBTREE_WITHOUT_MODIFICATION`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_SAVE_SINGLE_SUBTREE_WITHOUT_MODIFICATION)、[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_SHELL"></a>

## 423.21 `CONFIG_SETTINGS_SHELL`

**提示（Prompt）**：设置命令行（Settings shell）

**说明（Help）**

启用列出和读取设置项（Settings）的命令行命令（Shell command）。读取设置项需要较大的栈缓冲区，因此可能要增大命令行线程的栈大小以支持此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_SETTINGS
```

**定义位置（Location）**：[`subsys/settings/Kconfig:267`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L267)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_TFM_PSA"></a>

## 423.22 `CONFIG_SETTINGS_TFM_PSA`

**提示（Prompt）**：可信固件 M（TF-M）PSA 后端［实验性，Experimental］

**说明（Help）**

启用 PSA 设置后端（Settings backend），用于采用可信固件 M（TF-M）、无法通过其他方式使用持久存储的开发板。此后端通过 PSA 内部可信存储（ITS）或受保护存储（PS）服务保存设置数据。

注意：它将设置数据压缩到尽可能少的安全存储节点中，每次保存都将整个设置数组写入安全存储。为避免保存造成过长延迟，使用内核工作项（Work item）延迟保存。所有设置始终保留在 RAM 中，RAM 消耗由 `CONFIG_SETTINGS_TFM_PSA_NUM_ENTRIES` 控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM && <choice CONFIG_SETTINGS_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_PSA_CRYPTO
```

**定义位置（Location）**：[`subsys/settings/Kconfig:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L151)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 存储后端（Storage backend）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_SETTINGS_BACKEND`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_BACKEND)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)。

<a id="CONFIG_SETTINGS_TFM_PSA_BACKEND"></a>

## 423.23 `CONFIG_SETTINGS_TFM_PSA_BACKEND`

**提示（Prompt）**：TF-M PSA 设置后端（Settings backend）

**说明（Help）**

PSA 设置后端（Settings backend）使用的 PSA 存储选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_TFM_PSA && CONFIG_SETTINGS
```

**默认值（Defaults）**

```text
CONFIG_SETTINGS_TFM_PSA_BACKEND_ITS
```

**可选项（Choices）**

```text
CONFIG_SETTINGS_TFM_PSA_BACKEND_PS
CONFIG_SETTINGS_TFM_PSA_BACKEND_ITS
```

**定义位置（Location）**：[`subsys/settings/Kconfig:278`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L278)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_TFM_PSA`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_TFM_PSA)、[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)、[`CONFIG_SETTINGS_TFM_PSA_BACKEND_ITS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_TFM_PSA_BACKEND_ITS)、[`CONFIG_SETTINGS_TFM_PSA_BACKEND_PS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_TFM_PSA_BACKEND_PS)。

<a id="CONFIG_SETTINGS_TFM_PSA_BACKEND_ITS"></a>

## 423.24 `CONFIG_SETTINGS_TFM_PSA_BACKEND_ITS`

**提示（Prompt）**：PSA 内部可信存储（Internal Trusted Storage，ITS）

**说明（Help）**

使用 PSA 内部可信存储（ITS）作为设置存储后端（Settings storage backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_INTERNAL_TRUSTED_STORAGE && <choice CONFIG_SETTINGS_TFM_PSA_BACKEND>
```

**定义位置（Location）**：[`subsys/settings/Kconfig:290`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L290)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → TF-M PSA 设置后端（Settings backend）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_INTERNAL_TRUSTED_STORAGE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_INTERNAL_TRUSTED_STORAGE)、[`CONFIG_SETTINGS_TFM_PSA_BACKEND`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_TFM_PSA_BACKEND)。

<a id="CONFIG_SETTINGS_TFM_PSA_BACKEND_PS"></a>

## 423.25 `CONFIG_SETTINGS_TFM_PSA_BACKEND_PS`

**提示（Prompt）**：PSA 受保护存储（Protected Storage，PS）

**说明（Help）**

使用 PSA 受保护存储（PS）作为设置存储后端（Settings storage backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_PROTECTED_STORAGE && <choice CONFIG_SETTINGS_TFM_PSA_BACKEND>
```

**定义位置（Location）**：[`subsys/settings/Kconfig:284`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L284)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → TF-M PSA 设置后端（Settings backend）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_PROTECTED_STORAGE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_PROTECTED_STORAGE)、[`CONFIG_SETTINGS_TFM_PSA_BACKEND`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_TFM_PSA_BACKEND)。

<a id="CONFIG_SETTINGS_TFM_PSA_CHUNK_DELAY_MS"></a>

## 423.26 `CONFIG_SETTINGS_TFM_PSA_CHUNK_DELAY_MS`

**提示（Prompt）**：写入设置数据块（Chunk）之间的延迟（毫秒）

**说明（Help）**

设置各次写入设置数据块（Settings data chunk）之间的延迟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_TFM_PSA && CONFIG_SETTINGS
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`subsys/settings/Kconfig:321`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L321)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_TFM_PSA`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_TFM_PSA)、[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_TFM_PSA_LAZY_PERSIST_DELAY_MS"></a>

## 423.27 `CONFIG_SETTINGS_TFM_PSA_LAZY_PERSIST_DELAY_MS`

**提示（Prompt）**：持久保存设置（Persist settings）前的延迟（毫秒）

**说明（Help）**

PSA 安全存储 API（Secure Storage API）写入闪存时可能长时间阻塞，这对时间敏感事件可能不可接受。因此，始终使用 `k_work_delayable` 将数据持久保存到安全存储，而不在 `settings_save` 的同一上下文中执行。本选项设置工作项（Work item）调度前的延迟。写入可能阻塞时间敏感事件时，此延迟很有用，例如蓝牙配对（Bluetooth pairing）需要连续写入多个设置项。注意，本选项只控制初始延迟；各设置数据块写入之间的延迟由 `CONFIG_SETTINGS_TFM_PSA_CHUNK_DELAY_MS` 控制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_TFM_PSA && CONFIG_SETTINGS
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`subsys/settings/Kconfig:307`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L307)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_TFM_PSA`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_TFM_PSA)、[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_TFM_PSA_NUM_ENTRIES"></a>

## 423.28 `CONFIG_SETTINGS_TFM_PSA_NUM_ENTRIES`

**提示（Prompt）**：设置表项（Settings entry）的最大数量

**说明（Help）**

配置可同时存储的设置表项（Settings entry）最大数量。注意，此值决定静态分配缓冲区的大小，该缓冲区始终在 RAM 中保存全部设置表项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_TFM_PSA && CONFIG_SETTINGS
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 1000]
```

**定义位置（Location）**：[`subsys/settings/Kconfig:298`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L298)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_TFM_PSA`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_TFM_PSA)、[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_ZMS"></a>

## 423.29 `CONFIG_SETTINGS_ZMS`

**提示（Prompt）**：Zephyr 内存存储（Zephyr Memory Storage，ZMS）

**说明（Help）**

使用 Zephyr 内存存储（ZMS）作为设置存储后端（Settings storage backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZMS && CONFIG_FLASH_MAP && <choice CONFIG_SETTINGS_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_SYS_HASH_FUNC32
```

**定义位置（Location）**：[`subsys/settings/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 存储后端（Storage backend）

**配置项引用（Symbol References）**：[`CONFIG_ZMS`](P350_subsys_kvss_配置项参考.md#CONFIG_ZMS)、[`CONFIG_FLASH_MAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MAP)、[`CONFIG_SETTINGS_BACKEND`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_BACKEND)、[`CONFIG_SYS_HASH_FUNC32`](P198_lib_配置项参考_2.md#CONFIG_SYS_HASH_FUNC32)。

<a id="CONFIG_SETTINGS_ZMS_CUSTOM_SECTOR_COUNT"></a>

## 423.30 `CONFIG_SETTINGS_ZMS_CUSTOM_SECTOR_COUNT`

**提示（Prompt）**：自定义 ZMS 设置分区的扇区数量（Sector count）

**说明（Help）**

默认使用设置存储分区（Settings storage partition）能够容纳的最大扇区数量。启用本选项后，可以自定义使用的扇区数量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_ZMS && CONFIG_SETTINGS
```

**定义位置（Location）**：[`subsys/settings/Kconfig:224`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L224)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_ZMS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_ZMS)、[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_ZMS_FORCE_MOUNT"></a>

## 423.31 `CONFIG_SETTINGS_ZMS_FORCE_MOUNT`

**提示（Prompt）**：ZMS 强制挂载（Force mount）

**说明（Help）**

启用强制挂载 ZMS 存储（Force mount）；必要时擦除分区，以从数据损坏中恢复。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_ZMS && <choice CONFIG_SETTINGS_BACKEND>
```

**定义位置（Location）**：[`subsys/settings/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 存储后端（Storage backend） → Zephyr 内存存储（Zephyr Memory Storage，ZMS）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_ZMS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_ZMS)、[`CONFIG_SETTINGS_BACKEND`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_BACKEND)。

<a id="CONFIG_SETTINGS_ZMS_LL_CACHE"></a>

## 423.32 `CONFIG_SETTINGS_ZMS_LL_CACHE`

**提示（Prompt）**：ZMS 链表查找缓存（Linked-list lookup cache）

**说明（Help）**

启用 ZMS 链表查找缓存（Linked-list lookup cache），使多数链表元素已在缓存中，从而缩短设置（Settings）加载时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_ZMS && <choice CONFIG_SETTINGS_BACKEND>
```

**定义位置（Location）**：[`subsys/settings/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 存储后端（Storage backend） → Zephyr 内存存储（Zephyr Memory Storage，ZMS）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_ZMS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_ZMS)、[`CONFIG_SETTINGS_BACKEND`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_BACKEND)。

<a id="CONFIG_SETTINGS_ZMS_LL_CACHE_SIZE"></a>

## 423.33 `CONFIG_SETTINGS_ZMS_LL_CACHE_SIZE`

**提示（Prompt）**：ZMS 链表查找缓存大小（Linked-list lookup cache size）

**说明（Help）**

设置子系统 ZMS 链表缓存（Linked-list cache）的表项数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_ZMS_LL_CACHE && CONFIG_SETTINGS_ZMS && <choice CONFIG_SETTINGS_BACKEND>
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[1, 4294967295]
```

**定义位置（Location）**：[`subsys/settings/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 存储后端（Storage backend） → Zephyr 内存存储（Zephyr Memory Storage，ZMS） → ZMS 链表查找缓存（Linked-list lookup cache）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_ZMS_LL_CACHE`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_ZMS_LL_CACHE)、[`CONFIG_SETTINGS_ZMS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_ZMS)、[`CONFIG_SETTINGS_BACKEND`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_BACKEND)。

<a id="CONFIG_SETTINGS_ZMS_LOAD_SUBTREE_PATH"></a>

## 423.34 `CONFIG_SETTINGS_ZMS_LOAD_SUBTREE_PATH`

**提示（Prompt）**：提供子树路径（Subtree path）时仅加载该路径

**说明（Help）**

先加载子树路径（Subtree path）定义的键（Key）。如果回调处理程序返回 0，则继续查找该子树路径下的全部键。原文接着表示：如果回调返回非负值（Non-negative value），则立即返回。

译注：0 也是非负值，因此原文的两个条件相互重叠。这里保留原文，未擅自将后一条件改成“非零”。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS
```

**定义位置（Location）**：[`subsys/settings/Kconfig:258`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L258)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_ZMS_MAX_COLLISIONS_BITS"></a>

## 423.35 `CONFIG_SETTINGS_ZMS_MAX_COLLISIONS_BITS`

**提示（Prompt）**：为处理哈希值冲突（Hash collision）保留的位数

**说明（Help）**

应根据要存入 ZMS 的数据及其哈希值（Hash value），合理确定可处理的哈希冲突（Hash collision）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_ZMS && CONFIG_SETTINGS
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/settings/Kconfig:239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L239)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_ZMS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_ZMS)、[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_ZMS_NO_LL_DELETE"></a>

## 423.36 `CONFIG_SETTINGS_ZMS_NO_LL_DELETE`

**提示（Prompt）**：禁用链表哈希项（Linked-list hashes）的删除

**说明（Help）**

某些应用中，设置项（Settings）删除操作需要更新链表（Linked list），导致 ZMS 删除耗时过长。为提高性能，可不更新链表；代价是部分节点不再使用，却仍占用存储空间。再次创建同一个已删除设置元素时，这些节点将重新使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS
```

**定义位置（Location）**：[`subsys/settings/Kconfig:247`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L247)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_ZMS_SECTOR_COUNT"></a>

## 423.37 `CONFIG_SETTINGS_ZMS_SECTOR_COUNT`

**提示（Prompt）**：ZMS 设置区域（Settings area）的扇区数量

**说明（Help）**

ZMS 设置区域（Settings area）使用的扇区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_ZMS && CONFIG_SETTINGS_ZMS_CUSTOM_SECTOR_COUNT && CONFIG_SETTINGS
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/settings/Kconfig:232`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L232)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。 → 自定义 ZMS 设置分区的扇区数量（Sector count）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_ZMS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_ZMS)、[`CONFIG_SETTINGS_ZMS_CUSTOM_SECTOR_COUNT`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_ZMS_CUSTOM_SECTOR_COUNT)、[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<a id="CONFIG_SETTINGS_ZMS_SECTOR_SIZE_MULT"></a>

## 423.38 `CONFIG_SETTINGS_ZMS_SECTOR_SIZE_MULT`

**提示（Prompt）**：ZMS 设置区域（Settings area）的扇区大小

**说明（Help）**

ZMS 设置区域（Settings area）的扇区大小，以 `FLASH_ERASE_BLOCK_SIZE` 的倍数表示。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS_ZMS && CONFIG_SETTINGS
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/settings/Kconfig:216`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/settings/Kconfig#L216)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设置（Settings）。

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS_ZMS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS_ZMS)、[`CONFIG_SETTINGS`](P423_subsys_settings_配置项参考.md#CONFIG_SETTINGS)。

<!-- kconfig-navigation -->

[上一章](P422_subsys_sensing_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P424_subsys_shell_配置项参考_1.md)
