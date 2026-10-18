---
id: learning.zephyr-docs.kconfig-reference.page-344
title: "`subsys/fs`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第344章\_`subsys/fs`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/fs` 的 83 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_APP_LINK_WITH_FS"></a>

## 344.1 `CONFIG_APP_LINK_WITH_FS`

**提示（Prompt）**：将 app 与文件系统（FS）链接

**说明（Help）**

将文件系统（FS）头文件添加到 `app` 的包含路径（include path）。如果 FS 包含路径导致 `app` 出现别名冲突（aliasing issues），可禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/fs/Kconfig:177`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L177)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_EXT2_DISK_STARTING_SECTOR"></a>

## 344.2 `CONFIG_EXT2_DISK_STARTING_SECTOR`

**提示（Prompt）**：Ext2 起始扇区（starting sector）

**说明（Help）**

当前 Ext2 实现不支持 GUID 分区表（GUID Partition Table，GPT），必须通过本选项指定文件系统的起始扇区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_EXT2 && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/fs/ext2/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/ext2/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Ext2 文件系统支持 → Ext2 文件系统设置（Settings）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_EXT2`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_EXT2)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_EXT2_FSTAB_AUTOMOUNT"></a>

## 344.3 `CONFIG_EXT2_FSTAB_AUTOMOUNT`

**提示（Prompt）**：支持 fstab 自动挂载（auto-mounting）

**说明（Help）**

启用启动时自动挂载（automatic mounting）Ext2 文件系统。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/fs/ext2/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/ext2/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Ext2 文件系统支持 → Ext2 文件系统设置（Settings）

<a id="CONFIG_EXT2_MAX_BLOCK_COUNT"></a>

## 344.4 `CONFIG_EXT2_MAX_BLOCK_COUNT`

**提示（Prompt）**：可能使用的块数量上限（Maximum number of blocks）

**说明（Help）**

此配置用于确定存储已读取块（fetched blocks）的内部结构大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_EXT2 && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/fs/ext2/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/ext2/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Ext2 文件系统支持 → Ext2 文件系统设置（Settings）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_EXT2`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_EXT2)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_EXT2_MAX_BLOCK_SIZE"></a>

## 344.5 `CONFIG_EXT2_MAX_BLOCK_SIZE`

**提示（Prompt）**：支持的最大块大小（block size）

**说明（Help）**

此配置用于确定存储已读取块（fetched blocks）的内部结构大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_EXT2 && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
4096
```

**取值范围（Ranges）**

```text
[1024, 4096]
```

**定义位置（Location）**：[`subsys/fs/ext2/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/ext2/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Ext2 文件系统支持 → Ext2 文件系统设置（Settings）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_EXT2`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_EXT2)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_EXT2_MAX_FILES"></a>

## 344.6 `CONFIG_EXT2_MAX_FILES`

**提示（Prompt）**：已打开索引节点（inodes）的数量上限

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_EXT2 && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/fs/ext2/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/ext2/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Ext2 文件系统支持 → Ext2 文件系统设置（Settings）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_EXT2`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_EXT2)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_EXT2_SUPERBLOCK_ALIGNMENT"></a>

## 344.7 `CONFIG_EXT2_SUPERBLOCK_ALIGNMENT`

**提示（Prompt）**：Ext2 超级块对齐（superblock alignment）

**说明（Help）**

某些 SD 主机控制器要求数据缓冲区对齐，才能使直接存储器访问（DMA）正常工作。设备若有对齐要求，应更改此默认值。本项表示 `struct ext2_disk_superblock` 的对齐大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_EXT2 && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/fs/ext2/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/ext2/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Ext2 文件系统支持 → Ext2 文件系统设置（Settings）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_EXT2`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_EXT2)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FAT_FILESYSTEM_ELM"></a>

## 344.8 `CONFIG_FAT_FILESYSTEM_ELM`

**提示（Prompt）**：ELM FAT 文件系统支持

**说明（Help）**

使用 ELM FAT 文件系统实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LIB_LINK && CONFIG_FILE_SYSTEM_LIB_LINK
```

**主动选择（Selects）**

```text
CONFIG_DISK_ACCESS
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)、[`CONFIG_DISK_ACCESS`](P340_subsys_disk_配置项参考.md#CONFIG_DISK_ACCESS)。

<a id="CONFIG_FCB"></a>

## 344.9 `CONFIG_FCB`

**提示（Prompt）**：闪存循环缓冲区支持（Flash Circular Buffer）

**说明（Help）**

启用闪存循环缓冲区（Flash Circular Buffer）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MAP && CONFIG_FLASH_PAGE_LAYOUT
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`subsys/fs/fcb/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/fcb/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MAP)、[`CONFIG_FLASH_PAGE_LAYOUT`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_PAGE_LAYOUT)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_FCB_ALLOW_FIXED_ENDMARKER"></a>

## 344.10 `CONFIG_FCB_ALLOW_FIXED_ENDMARKER`

**提示（Prompt）**：允许 FCB 实例使用固定结束标记（endmarker）

**说明（Help）**

允许闪存循环缓冲区（FCB）实例禁用循环冗余校验（CRC），以提高写入吞吐量（write throughput）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FCB
```

**定义位置（Location）**：[`subsys/fs/fcb/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/fcb/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 闪存循环缓冲区支持（Flash Circular Buffer）

**配置项引用（Symbol References）**：[`CONFIG_FCB`](P344_subsys_fs_配置项参考.md#CONFIG_FCB)。

<a id="CONFIG_FILE_SYSTEM"></a>

## 344.11 `CONFIG_FILE_SYSTEM`

**提示（Prompt）**：文件系统支持（File system support）

**说明（Help）**

启用文件系统（file system）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_FILE_SYSTEM_LIB_LINK
```

**被选择（Selected by）**

```text
CONFIG_MODEM_HL7800_FW_UPDATE
CONFIG_POSIX_FILE_SYSTEM_R
CONFIG_POSIX_FILE_SYSTEM
```

**定义位置（Location）**：[`subsys/fs/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)、[`CONFIG_MODEM_HL7800_FW_UPDATE`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL7800_FW_UPDATE)、[`CONFIG_POSIX_FILE_SYSTEM_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_FILE_SYSTEM_R)、[`CONFIG_POSIX_FILE_SYSTEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_FILE_SYSTEM)。

<a id="CONFIG_FILE_SYSTEM_EXT2"></a>

## 344.12 `CONFIG_FILE_SYSTEM_EXT2`

**提示（Prompt）**：Ext2 文件系统支持

**说明（Help）**

启用 Ext2 文件系统支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LIB_LINK && CONFIG_FILE_SYSTEM_LIB_LINK
```

**定义位置（Location）**：[`subsys/fs/ext2/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/ext2/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FILE_SYSTEM_GC"></a>

## 344.13 `CONFIG_FILE_SYSTEM_GC`

**提示（Prompt）**：允许显式调用垃圾回收器（garbage collector）

**说明（Help）**

启用 `fs_gc` 函数，以便主动运行垃圾回收器（garbage collector）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM
```

**定义位置（Location）**：[`subsys/fs/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统支持（File system support）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)。

<a id="CONFIG_FILE_SYSTEM_INIT_PRIORITY"></a>

## 344.14 `CONFIG_FILE_SYSTEM_INIT_PRIORITY`

**提示（Prompt）**：文件系统初始化优先级（initialization priority）

**说明（Help）**

指定文件系统初始化优先级。若启用自动挂载（automount），应在底层存储设备初始化之后进行文件系统初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM
```

**默认值（Defaults）**

```text
99
```

**定义位置（Location）**：[`subsys/fs/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统支持（File system support）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)。

<a id="CONFIG_FILE_SYSTEM_LIB_LINK"></a>

## 344.15 `CONFIG_FILE_SYSTEM_LIB_LINK`

**提示（Prompt）**：将文件系统库链接到构建中

**说明（Help）**

链接底层文件系统库（file system libraries）。即使未启用 `CONFIG_FILE_SYSTEM`，也可启用此项，让应用直接使用底层文件系统库。当只使用部分功能时，这可避免通过 `struct fs_file_system_t` 将整个文件系统实现链接进来。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_FILE_SYSTEM
```

**定义位置（Location）**：[`subsys/fs/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)。

<a id="CONFIG_FILE_SYSTEM_LITTLEFS"></a>

## 344.16 `CONFIG_FILE_SYSTEM_LITTLEFS`

**提示（Prompt）**：LittleFS 支持

**说明（Help）**

启用 LittleFS 文件系统支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LIB_LINK && CONFIG_ZEPHYR_LITTLEFS_MODULE && CONFIG_FILE_SYSTEM_LIB_LINK
```

**定义位置（Location）**：[`subsys/fs/Kconfig.littlefs:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.littlefs#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)、[`CONFIG_ZEPHYR_LITTLEFS_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_LITTLEFS_MODULE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_LITTLEFS_MODULE`。

<a id="CONFIG_FILE_SYSTEM_MAX_FILE_NAME"></a>

## 344.17 `CONFIG_FILE_SYSTEM_MAX_FILE_NAME`

**提示（Prompt）**：可选覆盖最大文件名长度（maximum file name length）

**说明（Help）**

指定所有已启用文件系统类型共同允许的最大文件名长度。零或负值表示使用已启用的树内文件系统（in-tree file systems）所支持的最大文件名长度。注册树外文件系统（out-of-tree file system）时，此默认值可能不合适。若设置值小于某文件系统实际支持的长度，可能导致内存访问违规（memory access violations）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM
```

**默认值（Defaults）**

```text
-1
```

**定义位置（Location）**：[`subsys/fs/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统支持（File system support）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)。

<a id="CONFIG_FILE_SYSTEM_MAX_TYPES"></a>

## 344.18 `CONFIG_FILE_SYSTEM_MAX_TYPES`

**提示（Prompt）**：允许的不同文件系统类型数量上限

**说明（Help）**

Zephyr 提供 FatFS、LittleFS 等文件系统类型，也允许定义并注册额外类型。每种类型需要一个槽位（slot）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/fs/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统支持（File system support）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)。

<a id="CONFIG_FILE_SYSTEM_MKFS"></a>

## 344.19 `CONFIG_FILE_SYSTEM_MKFS`

**提示（Prompt）**：允许格式化文件系统（format file system）

**说明（Help）**

启用 `fs_mkfs` 函数，用于格式化存储设备（storage device）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM
```

**定义位置（Location）**：[`subsys/fs/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统支持（File system support）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)。

<a id="CONFIG_FILE_SYSTEM_NATIVE_MOUNT"></a>

## 344.20 `CONFIG_FILE_SYSTEM_NATIVE_MOUNT`

**提示（Prompt）**：将原生模拟器（Native Simulator）主机文件系统挂载到 Zephyr

**说明（Help）**

将主机文件系统中的路径挂载到 Zephyr，使 Zephyr 能够像访问其他嵌入式挂载点（mount point）一样访问、修改主机文件和文件夹。在运行可执行文件时传入以下命令行参数：

```text
-volume=/host/dir:/dir
```

这会将主机的 `/host/dir` 挂载为 Zephyr 中的 `/dir`。译注：这两个路径是官方命令语法中的示例占位路径，分别属于主机文件系统和 Zephyr 挂载命名空间，不代表本仓库的位置；使用时按实际挂载需求替换。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_POSIX && CONFIG_FILE_SYSTEM
```

**主动选择（Selects）**

```text
CONFIG_NATIVE_USE_NSI_FCNTL
CONFIG_NATIVE_USE_NSI_ERRNO
```

**定义位置（Location）**：[`subsys/fs/Kconfig:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统支持（File system support）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)、[`CONFIG_NATIVE_USE_NSI_FCNTL`](P033_arch_posix_配置项参考.md#CONFIG_NATIVE_USE_NSI_FCNTL)、[`CONFIG_NATIVE_USE_NSI_ERRNO`](P033_arch_posix_配置项参考.md#CONFIG_NATIVE_USE_NSI_ERRNO)。

<a id="CONFIG_FILE_SYSTEM_RPMSGFS"></a>

## 344.21 `CONFIG_FILE_SYSTEM_RPMSGFS`

**提示（Prompt）**：RPMsgFS 文件系统支持

**说明（Help）**

RPMsgFS 允许使用远程处理器消息传递（RPMsg）挂载远程核心上的目录。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENAMP && CONFIG_FILE_SYSTEM
```

**定义位置（Location）**：[`subsys/fs/Kconfig:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统支持（File system support）

**配置项引用（Symbol References）**：[`CONFIG_OPENAMP`](P208_modules_Kconfig.open-amp_配置项参考.md#CONFIG_OPENAMP)、[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)。

<a id="CONFIG_FILE_SYSTEM_RPMSGFS_MAX_MOUNTS"></a>

## 344.22 `CONFIG_FILE_SYSTEM_RPMSGFS_MAX_MOUNTS`

**提示（Prompt）**：RPMsgFS 最大挂载数（max mounts）

**说明（Help）**

指定可同时挂载的 RPMsgFS 文件系统实例数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_RPMSGFS && CONFIG_FILE_SYSTEM
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/fs/Kconfig:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统支持（File system support） → RPMsgFS 文件系统支持

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_RPMSGFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_RPMSGFS)、[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)。

<a id="CONFIG_FILE_SYSTEM_RPMSGFS_SINGLE_CHANNEL"></a>

## 344.23 `CONFIG_FILE_SYSTEM_RPMSGFS_SINGLE_CHANNEL`

**提示（Prompt）**：为所有 RPMsgFS 挂载使用一个 RPMsg 通道（channel）

**说明（Help）**

所有 RPMsgFS 挂载共享一个远程处理器消息传递（RPMsg）通道。首次挂载时创建通道，后续挂载期间持续保持活动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_RPMSGFS && CONFIG_FILE_SYSTEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/fs/Kconfig:154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L154)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统支持（File system support） → RPMsgFS 文件系统支持

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_RPMSGFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_RPMSGFS)、[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)。

<a id="CONFIG_FILE_SYSTEM_SHELL"></a>

## 344.24 `CONFIG_FILE_SYSTEM_SHELL`

**提示（Prompt）**：文件系统命令行（File system shell）

**说明（Help）**

此命令行（shell）提供浏览文件系统内容的基本功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_FILE_SYSTEM
```

**定义位置（Location）**：[`subsys/fs/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统支持（File system support）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)。

<a id="CONFIG_FILE_SYSTEM_SHELL_BUFFER_SIZE"></a>

## 344.25 `CONFIG_FILE_SYSTEM_SHELL_BUFFER_SIZE`

**提示（Prompt）**：文件系统命令行缓冲区大小（buffer size）

**说明（Help）**

文件系统命令所用的缓冲区大小，决定读写测试可使用的最大大小。注意，此缓冲区位于栈（stack）上。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_SHELL_TEST_COMMANDS && CONFIG_FILE_SYSTEM_SHELL && CONFIG_FILE_SYSTEM
```

**默认值（Defaults）**

```text
0x100
```

**取值范围（Ranges）**

```text
[0x20, 0x1000000]
```

**定义位置（Location）**：[`subsys/fs/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统支持（File system support） → 文件系统命令行（File system shell） → 文件系统命令行的读／写／擦除测试命令

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_SHELL_TEST_COMMANDS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_SHELL_TEST_COMMANDS)、[`CONFIG_FILE_SYSTEM_SHELL`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_SHELL)、[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)。

<a id="CONFIG_FILE_SYSTEM_SHELL_LS_SIZE"></a>

## 344.26 `CONFIG_FILE_SYSTEM_SHELL_LS_SIZE`

**提示（Prompt）**：文件系统命令行的 ls 命令同时列出大小

**说明（Help）**

在文件系统命令行（shell）中列出文件时，同时列出每个文件的大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_SHELL && CONFIG_FILE_SYSTEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/fs/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统支持（File system support） → 文件系统命令行（File system shell）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_SHELL`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_SHELL)、[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)。

<a id="CONFIG_FILE_SYSTEM_SHELL_MOUNT_COMMAND"></a>

## 344.27 `CONFIG_FILE_SYSTEM_SHELL_MOUNT_COMMAND`

**提示（Prompt）**：文件系统命令行的 mount 挂载命令

**说明（Help）**

启用用于挂载文件系统的命令行命令（shell command）。这要求提供堆（heap）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_FAT_FILESYSTEM_ELM || CONFIG_FILE_SYSTEM_LITTLEFS || CONFIG_FILE_SYSTEM_RPMSGFS) && CONFIG_HEAP_MEM_POOL_SIZE > 0 && CONFIG_FILE_SYSTEM_SHELL && CONFIG_FILE_SYSTEM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/fs/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统支持（File system support） → 文件系统命令行（File system shell）

**配置项引用（Symbol References）**：[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LITTLEFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LITTLEFS)、[`CONFIG_FILE_SYSTEM_RPMSGFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_RPMSGFS)、[`CONFIG_HEAP_MEM_POOL_SIZE`](P001_kernel_配置项参考_1.md#CONFIG_HEAP_MEM_POOL_SIZE)、[`CONFIG_FILE_SYSTEM_SHELL`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_SHELL)、[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)。

<a id="CONFIG_FILE_SYSTEM_SHELL_TEST_COMMANDS"></a>

## 344.28 `CONFIG_FILE_SYSTEM_SHELL_TEST_COMMANDS`

**提示（Prompt）**：文件系统命令行的读／写／擦除测试命令

**说明（Help）**

启用附加的文件系统命令行命令，执行读／写／擦除测试并输出速度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_SHELL && CONFIG_FILE_SYSTEM
```

**主动选择（Selects）**

```text
CONFIG_CBPRINTF_FP_SUPPORT
```

**定义位置（Location）**：[`subsys/fs/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统支持（File system support） → 文件系统命令行（File system shell）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_SHELL`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_SHELL)、[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)、[`CONFIG_CBPRINTF_FP_SUPPORT`](P197_lib_配置项参考_1.md#CONFIG_CBPRINTF_FP_SUPPORT)。

<a id="CONFIG_FILE_SYSTEM_VIRTIOFS"></a>

## 344.29 `CONFIG_FILE_SYSTEM_VIRTIOFS`

**提示（Prompt）**：Virtiofs 文件系统支持

**说明（Help）**

启用 virtiofs 文件系统支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**主动选择（Selects）**

```text
CONFIG_FUSE_CLIENT
CONFIG_VIRTIO
```

**定义位置（Location）**：[`subsys/fs/virtiofs/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/virtiofs/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)、[`CONFIG_FUSE_CLIENT`](P344_subsys_fs_配置项参考.md#CONFIG_FUSE_CLIENT)、[`CONFIG_VIRTIO`](P183_drivers_virtio_配置项参考.md#CONFIG_VIRTIO)。

<a id="CONFIG_FS_FATFS_CODEPAGE"></a>

## 344.30 `CONFIG_FS_FATFS_CODEPAGE`

**提示（Prompt）**：FatFS 代码页（code page，字符集）

**说明（Help）**

有效的代码页（code page）值如下：

| 值 | 字符集（Character set） |
| --- | --- |
| 437 | 美国（U.S.） |
| 720 | 阿拉伯语（Arabic） |
| 737 | 希腊语（Greek） |
| 771 | KBL |
| 775 | 波罗的海语系（Baltic） |
| 850 | 拉丁 1（Latin 1） |
| 852 | 拉丁 2（Latin 2） |
| 855 | 西里尔字母（Cyrillic） |
| 857 | 土耳其语（Turkish） |
| 860 | 葡萄牙语（Portuguese） |
| 861 | 冰岛语（Icelandic） |
| 862 | 希伯来语（Hebrew） |
| 863 | 加拿大法语（Canadian French） |
| 864 | 阿拉伯语（Arabic） |
| 865 | 北欧（Nordic） |
| 866 | 俄语（Russian） |
| 869 | 希腊语 2（Greek 2） |
| 932 | 日语，双字节字符集（Japanese，DBCS） |
| 936 | 简体中文，双字节字符集（Simplified Chinese，DBCS） |
| 949 | 韩语，双字节字符集（Korean，DBCS） |
| 950 | 繁体中文，双字节字符集（Traditional Chinese，DBCS） |
| 0 | 包含所有受支持的代码页（all supported code pages） |

此选项影响 ELM FAT 模块内部 `ffconf.h` 中定义的 `FF_CODE_PAGE`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
437
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_FATFS_CUSTOM_MOUNT_POINTS"></a>

## 344.31 `CONFIG_FS_FATFS_CUSTOM_MOUNT_POINTS`

**提示（Prompt）**：使用 FatFS 时支持自定义挂载点（custom mountpoints）

**说明（Help）**

允许指定可挂载 FatFS 文件系统的自定义挂载点（mount points）。必须以逗号分隔的列表定义，不能包含空白，也不能以逗号结尾。例如：

```text
"RAM,SD,SD2,NAND"
```

还必须通过 `FS_FATFS_CUSTOM_MOUNT_POINT_COUNT` 指定列表中的挂载点数量。启用此项后，列表以外的任何挂载点都不能用于挂载 FatFS 文件系统。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_FS_FATFS_CUSTOM_MOUNT_POINT_COUNT > 0 && CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:289`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L289)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FS_FATFS_CUSTOM_MOUNT_POINT_COUNT`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_CUSTOM_MOUNT_POINT_COUNT)、[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_FATFS_CUSTOM_MOUNT_POINT_COUNT"></a>

## 344.32 `CONFIG_FS_FATFS_CUSTOM_MOUNT_POINT_COUNT`

**提示（Prompt）**：自定义挂载点数量（Count of custom mount points）

**说明（Help）**

必须与 `FS_FATFS_CUSTOM_MOUNT_POINTS` 一起使用，指定自定义挂载点字符串中定义的挂载点数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:280`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L280)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_FATFS_EXFAT"></a>

## 344.33 `CONFIG_FS_FATFS_EXFAT`

**提示（Prompt）**：exFAT 支持

**说明（Help）**

为 FatFs 启用 exFAT 格式支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**主动选择（Selects）**

```text
CONFIG_FS_FATFS_LFN
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)、[`CONFIG_FS_FATFS_LFN`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_LFN)。

<a id="CONFIG_FS_FATFS_EXTRA_NATIVE_API"></a>

## 344.34 `CONFIG_FS_FATFS_EXTRA_NATIVE_API`

**提示（Prompt）**：附加的原生 API 函数（native API functions）

**说明（Help）**

启用以下附加原生 API 函数；Zephyr 虚拟文件系统（VFS）API 中没有与之等价的接口：

- `f_getlabel`
- `f_setlabel`
- `f_expand`
- `f_findfirst`
- `f_findnext`

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_FATFS_FF_USE_LFN"></a>

## 344.35 `CONFIG_FS_FATFS_FF_USE_LFN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

将 `FS_FATFS_LFN_MODE` 的选择映射为 ELM FAT 模块内部 `ffconf.h` 中定义的 `FF_USE_LFN`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FS_FATFS_LFN && CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
1 if CONFIG_FS_FATFS_LFN_MODE_BSS
2 if CONFIG_FS_FATFS_LFN_MODE_STACK
3 if CONFIG_FS_FATFS_LFN_MODE_HEAP
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings） → 长文件名（Long filenames，LFN）

**配置项引用（Symbol References）**：[`CONFIG_FS_FATFS_LFN`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_LFN)、[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)、[`CONFIG_FS_FATFS_LFN_MODE_BSS`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_LFN_MODE_BSS)、[`CONFIG_FS_FATFS_LFN_MODE_STACK`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_LFN_MODE_STACK)、[`CONFIG_FS_FATFS_LFN_MODE_HEAP`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_LFN_MODE_HEAP)。

<a id="CONFIG_FS_FATFS_FSTAB_AUTOMOUNT"></a>

## 344.36 `CONFIG_FS_FATFS_FSTAB_AUTOMOUNT`

**提示（Prompt）**：支持 fstab 自动挂载（auto-mounting）

**说明（Help）**

启用 FatFS 对设备树（devicetree）fstab 自动挂载功能的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:302`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L302)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

<a id="CONFIG_FS_FATFS_HAS_RTC"></a>

## 344.37 `CONFIG_FS_FATFS_HAS_RTC`

**提示（Prompt）**：时间戳支持（Timestamping support）

**说明（Help）**

启用文件系统时间戳（timestamping），不再对所有操作使用写死的日期。应用必须提供 `get_fattime` 实现。`uint32_t` 的位域格式如下：

| 位范围 | 含义 |
| --- | --- |
| 31:25 | 自 1980 年起的年份差（Year from 1980） |
| 24:21 | 月（Month），1..12 |
| 20:16 | 日（Day of month），1..31 |
| 15:11 | 时（Hour），0..23 |
| 10:5 | 分（Minute），0..59 |
| 4:0 | 秒数除以 2（Seconds/2），0..29 |

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_FATFS_LBA64"></a>

## 344.38 `CONFIG_FS_FATFS_LBA64`

**提示（Prompt）**：支持 64 位逻辑块寻址（LBA）

**说明（Help）**

启用 64 位逻辑块寻址（LBA）支持，同时启用 GUID 分区表（GPT）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FS_FATFS_EXFAT && CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:258`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L258)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FS_FATFS_EXFAT`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_EXFAT)、[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_FATFS_LFN"></a>

## 344.39 `CONFIG_FS_FATFS_LFN`

**提示（Prompt）**：长文件名（Long filenames，LFN）

**说明（Help）**

未启用长文件名（LFN）时，文件名限制为 8.3 格式。启用本项会增大工作缓冲区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**被选择（Selected by）**

```text
CONFIG_FS_FATFS_EXFAT
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)、[`CONFIG_FS_FATFS_EXFAT`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_EXFAT)。

<a id="CONFIG_FS_FATFS_LFN_MODE"></a>

## 344.40 `CONFIG_FS_FATFS_LFN_MODE`

**提示（Prompt）**：长文件名（LFN）内存模式

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FS_FATFS_LFN && CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
CONFIG_FS_FATFS_LFN_MODE_BSS
```

**可选项（Choices）**

```text
CONFIG_FS_FATFS_LFN_MODE_BSS
CONFIG_FS_FATFS_LFN_MODE_STACK
CONFIG_FS_FATFS_LFN_MODE_HEAP
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings） → 长文件名（Long filenames，LFN）

**配置项引用（Symbol References）**：[`CONFIG_FS_FATFS_LFN`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_LFN)、[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)、[`CONFIG_FS_FATFS_LFN_MODE_BSS`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_LFN_MODE_BSS)、[`CONFIG_FS_FATFS_LFN_MODE_STACK`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_LFN_MODE_STACK)、[`CONFIG_FS_FATFS_LFN_MODE_HEAP`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_LFN_MODE_HEAP)。

<a id="CONFIG_FS_FATFS_LFN_MODE_BSS"></a>

## 344.41 `CONFIG_FS_FATFS_LFN_MODE_BSS`

**提示（Prompt）**：静态缓冲区（Static buffer）

**说明（Help）**

使用 BSS 段中的静态工作缓冲区启用长文件名（LFN）。始终不具备线程安全性（NOT thread-safe）。此项将 ELM FAT 模块内部 `ffconf.h` 定义的 `FF_USE_LFN` 设为 `1`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FS_FATFS_LFN_MODE>
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings） → 长文件名（Long filenames，LFN） → 长文件名（LFN）内存模式

**配置项引用（Symbol References）**：[`CONFIG_FS_FATFS_LFN_MODE`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_LFN_MODE)。

<a id="CONFIG_FS_FATFS_LFN_MODE_HEAP"></a>

## 344.42 `CONFIG_FS_FATFS_LFN_MODE_HEAP`

**提示（Prompt）**：堆缓冲区（Heap buffer）

**说明（Help）**

使用堆（HEAP）上的动态工作缓冲区启用长文件名（LFN）。此项将 ELM FAT 模块内部 `ffconf.h` 定义的 `FF_USE_LFN` 设为 `3`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HEAP_MEM_POOL_SIZE > 0 && <choice CONFIG_FS_FATFS_LFN_MODE>
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:142`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L142)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings） → 长文件名（Long filenames，LFN） → 长文件名（LFN）内存模式

**配置项引用（Symbol References）**：[`CONFIG_HEAP_MEM_POOL_SIZE`](P001_kernel_配置项参考_1.md#CONFIG_HEAP_MEM_POOL_SIZE)、[`CONFIG_FS_FATFS_LFN_MODE`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_LFN_MODE)。

<a id="CONFIG_FS_FATFS_LFN_MODE_STACK"></a>

## 344.43 `CONFIG_FS_FATFS_LFN_MODE_STACK`

**提示（Prompt）**：栈缓冲区（Stack buffer）

**说明（Help）**

使用栈（STACK）上的动态工作缓冲区启用长文件名（LFN）。此项将 ELM FAT 模块内部 `ffconf.h` 定义的 `FF_USE_LFN` 设为 `2`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FS_FATFS_LFN_MODE>
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:135`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L135)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings） → 长文件名（Long filenames，LFN） → 长文件名（LFN）内存模式

**配置项引用（Symbol References）**：[`CONFIG_FS_FATFS_LFN_MODE`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_LFN_MODE)。

<a id="CONFIG_FS_FATFS_MAX_LFN"></a>

## 344.44 `CONFIG_FS_FATFS_MAX_LFN`

**提示（Prompt）**：最大文件名长度（Max filename length）

**说明（Help）**

工作缓冲区占用 `(FS_FATFS_MAX_LFN + 1) * 2` 字节；启用 exFAT 后还额外占用 `608` 字节。若要完整支持长文件名（LFN）操作，应设为 `255`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FS_FATFS_LFN && CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
255
```

**取值范围（Ranges）**

```text
[12, 255]
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings） → 长文件名（Long filenames，LFN）

**配置项引用（Symbol References）**：[`CONFIG_FS_FATFS_LFN`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_LFN)、[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_FATFS_MAX_ROOT_ENTRIES"></a>

## 344.45 `CONFIG_FS_FATFS_MAX_ROOT_ENTRIES`

**提示（Prompt）**：FAT 文件系统根目录条目数量上限

**说明（Help）**

在设备上格式化新的 FAT 文件系统时，设置要分配的根目录条目（root directory entries）数量。注意，它应是 `FS_FATFS_MAX_SS / 32` 的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FS_FATFS_MKFS && CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
512
```

**取值范围（Ranges）**

```text
[1, 32768]
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FS_FATFS_MKFS`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_MKFS)、[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_FATFS_MAX_SS"></a>

## 344.46 `CONFIG_FS_FATFS_MAX_SS`

**提示（Prompt）**：支持的最大扇区大小（Maximum supported sector size）

**说明（Help）**

此值用作支持读写的最大扇区大小（sector size），最小为 `512`。它影响读写粒度，并增大 FAT 驱动所用缓冲区，因此影响与 FAT 挂载点关联的每个 `FATFS` 对象所需的 RAM：其大小为此值加上一个与本设置无关的固定量。

如果挂载点定义为静态／全局生命周期的变量，本项影响编译期 RAM 分配；若定义在栈上，则影响栈占用。值为 `512` 时，所有挂载点都使用 512 字节扇区；取其他值时，FAT 驱动会在挂载时查询设备的扇区大小。此选项影响 ELM FAT 模块内部 `ffconf.h` 中的 `FF_MAX_SS`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
512
```

**取值范围（Ranges）**

```text
[512, 4096]
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_FATFS_MIN_SS"></a>

## 344.47 `CONFIG_FS_FATFS_MIN_SS`

**提示（Prompt）**：预期的最小扇区大小（Minimum expected sector size）

**说明（Help）**

指定 FAT 文件系统驱动预期支持的最小扇区大小。只有一个 FAT 设备，或所有已连接设备使用相同扇区大小时，原文建议将其设为 `FS_FATFS_MAX_FS`，以略微减小 FAT 驱动代码，因为此时不必逐个查询设备的扇区大小。此项影响 ELM FAT 模块内部 `ffconf.h` 中的 `FF_MIN_SS`。

译注：原文此处写作 `FS_FATFS_MAX_FS`；同组“最大扇区大小”选项名称为 `FS_FATFS_MAX_SS`。这里保留原文标识符并标明差异，配置时应核对实际源码中的符号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
512
```

**取值范围（Ranges）**

```text
[512, CONFIG_FS_FATFS_MAX_SS]
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:223`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L223)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)、[`CONFIG_FS_FATFS_MAX_SS`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_MAX_SS)。

<a id="CONFIG_FS_FATFS_MKFS"></a>

## 344.48 `CONFIG_FS_FATFS_MKFS`

**提示（Prompt）**：FAT 文件系统的 mkfs 格式化支持

**说明（Help）**

加入创建 FAT 文件系统磁盘的代码。此项影响 ELM FAT 模块内部 `ffconf.h` 中定义的 `FF_USE_MKFS`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_FS_FATFS_READ_ONLY && CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
y if CONFIG_FILE_SYSTEM_MKFS
```

**被选择（Selected by）**

```text
CONFIG_FS_FATFS_MOUNT_MKFS
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FS_FATFS_READ_ONLY`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_READ_ONLY)、[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)、[`CONFIG_FILE_SYSTEM_MKFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_MKFS)、[`CONFIG_FS_FATFS_MOUNT_MKFS`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_MOUNT_MKFS)。

<a id="CONFIG_FS_FATFS_MOUNT_MKFS"></a>

## 344.49 `CONFIG_FS_FATFS_MOUNT_MKFS`

**提示（Prompt）**：允许在挂载失败时格式化卷（volume）

**说明（Help）**

加入相关代码，使 `fs_mount` 在找不到文件系统时尝试格式化卷（volume）。如果不需要格式化，禁用此项可略微减小应用体积。

注意：此选项会破坏数据，挂载尝试失败时将自动破坏磁盘上的数据。如果磁盘能够从设备上取下并通过其他系统恢复，可能更适合禁用本项。禁用后，必须在连接设备前将磁盘格式化为 FAT，否则无法挂载。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FS_FATFS_MKFS
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)、[`CONFIG_FS_FATFS_MKFS`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_MKFS)。

<a id="CONFIG_FS_FATFS_MULTI_PARTITION"></a>

## 344.50 `CONFIG_FS_FATFS_MULTI_PARTITION`

**提示（Prompt）**：支持物理驱动器上的多个卷（multiple volumes）

**说明（Help）**

启用后，每个逻辑驱动器编号（logical drive number）均可绑定到 FatFS 模块 `VolToPart[]` 中列出的任意物理驱动器和分区。`VolToPart[]` 应由 Zephyr 应用提供，此时挂载点必须编号。例如，在 Zephyr 编号为 `3` 的 SD 磁盘上有两个 FAT 分区：

| 物理驱动器、分区 | 挂载点（mount point） |
| --- | --- |
| `{3, 1}` | `/0:` |
| `{3, 2}` | `/1:` |

禁用时（默认），每个逻辑驱动器编号绑定到相同编号的物理驱动器，只挂载在该物理驱动器上找到的一个 FAT 卷。译注：`/0:`、`/1:` 为 Zephyr 的挂载点命名，不是主机仓库路径。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:265`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L265)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_FATFS_NUM_DIRS"></a>

## 344.51 `CONFIG_FS_FATFS_NUM_DIRS`

**提示（Prompt）**：已打开目录数量上限（Maximum number of opened directories）

**说明（Help）**

决定 FAT 驱动可同时使用的目录对象数量。每个对象大小为 `sizeof(DIR)`，其中 `DIR` 定义在 ELM FAT 驱动的 `ff.h` 中；对象在编译时预分配。此项影响对已挂载 FAT 文件系统使用 `fs_opendir` 的能力。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_FATFS_NUM_FILES"></a>

## 344.52 `CONFIG_FS_FATFS_NUM_FILES`

**提示（Prompt）**：已打开文件数量上限（Maximum number of opened files）

**说明（Help）**

决定 FAT 驱动可同时使用的文件对象数量。每个对象大小为 `sizeof(FIL)`，其中 `FIL` 定义在 ELM FAT 驱动的 `ff.h` 中；对象在编译时预分配。此项影响对已挂载 FAT 文件系统使用 `fs_open` 的能力。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_FATFS_READ_ONLY"></a>

## 344.53 `CONFIG_FS_FATFS_READ_ONLY`

**提示（Prompt）**：所有卷的只读支持（Read-only support）

**说明（Help）**

从 ELM FAT 文件系统驱动中移除写入代码。仅以只读方式访问 FAT 时选择此项，可略微减小代码大小。此项影响 ELM FAT 模块内部 `ffconf.h` 中定义的 `FF_FS_READONLY`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_FATFS_REENTRANT"></a>

## 344.54 `CONFIG_FS_FATFS_REENTRANT`

**提示（Prompt）**：FatFs 可重入支持（reentrant）

**说明（Help）**

对每个卷的文件／目录访问启用 FatFs 可重入（re-entrancy，即线程安全）选项。将为每个 FatFs 卷创建一个 Zephyr 互斥锁（mutex）对象，并创建一个 FatFs 系统互斥锁。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_FS_FATFS_LFN_MODE_BSS && CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:250`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L250)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FS_FATFS_LFN_MODE_BSS`](P344_subsys_fs_配置项参考.md#CONFIG_FS_FATFS_LFN_MODE_BSS)、[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_FATFS_WINDOW_ALIGNMENT"></a>

## 344.55 `CONFIG_FS_FATFS_WINDOW_ALIGNMENT`

**提示（Prompt）**：FATFS 中 win 成员的内存对齐（memory alignment）

**说明（Help）**

指定 FAT 文件系统窗口缓冲区（window buffer）的字节对齐要求，该缓冲区用于设备读写。MMC 控制器可能要求读写缓冲区从特定对齐地址开始，例如 16 或 512 字节对齐，本项即设置这一对齐值。窗口缓冲区是 `FATFS` 结构体的内部成员，因此在最坏情况下，该设置可能使 `FATFS` 结构体大小达到所设值的两倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FAT_FILESYSTEM_ELM && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/fs/Kconfig.fatfs:237`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.fatfs#L237)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → ELM FAT 文件系统支持 → ELM FAT 文件系统设置（settings）

**配置项引用（Symbol References）**：[`CONFIG_FAT_FILESYSTEM_ELM`](P344_subsys_fs_配置项参考.md#CONFIG_FAT_FILESYSTEM_ELM)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_LITTLEFS_BLK_DEV"></a>

## 344.56 `CONFIG_FS_LITTLEFS_BLK_DEV`

**提示（Prompt）**：支持块设备（block devices）上的 littlefs

**说明（Help）**

启用对块设备（block devices，例如 SD 卡）上的 littlefs 的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LITTLEFS && CONFIG_FILE_SYSTEM_LIB_LINK
```

**定义位置（Location）**：[`subsys/fs/Kconfig.littlefs:114`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.littlefs#L114)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → LittleFS 支持

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LITTLEFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LITTLEFS)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_LITTLEFS_BLOCK_CYCLES"></a>

## 344.57 `CONFIG_FS_LITTLEFS_BLOCK_CYCLES`

**提示（Prompt）**：将数据移至另一块之前的擦除周期数（erase cycles）

**说明（Help）**

用于动态磨损均衡（dynamic wear leveling）：达到此擦除周期数后，将数据移至另一块。设置为非正值可禁用磨损均衡。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LITTLEFS && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`subsys/fs/Kconfig.littlefs:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.littlefs#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → LittleFS 支持 → LittleFS 设置（Settings）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LITTLEFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LITTLEFS)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_LITTLEFS_CACHE_SIZE"></a>

## 344.58 `CONFIG_FS_LITTLEFS_CACHE_SIZE`

**提示（Prompt）**：块缓存大小（字节，block caches）

**说明（Help）**

每个缓存都在 RAM 中缓冲块的一部分。littlefs 需要一个读缓存、一个编程缓存（program cache），以及每个文件一个附加缓存。较大的缓存可存储更多数据、减少磁盘访问次数，从而改善性能。缓存大小必须是底层闪存设备读大小和编程大小的整数倍，同时必须是块大小（block size）的约数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LITTLEFS && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`subsys/fs/Kconfig.littlefs:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.littlefs#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → LittleFS 支持 → LittleFS 设置（Settings）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LITTLEFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LITTLEFS)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_LITTLEFS_DISK_VERSION"></a>

## 344.59 `CONFIG_FS_LITTLEFS_DISK_VERSION`

**提示（Prompt）**：支持选择 littlefs 磁盘格式版本（disk version）

**说明（Help）**

允许选择 littlefs 磁盘格式版本，以保持对现有 littlefs 的向后兼容，前提是磁盘格式主版本号（major disk version）相同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LITTLEFS && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`subsys/fs/Kconfig.littlefs:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.littlefs#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → LittleFS 支持

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LITTLEFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LITTLEFS)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_LITTLEFS_DISK_VERSION_NUMBER"></a>

## 344.60 `CONFIG_FS_LITTLEFS_DISK_VERSION_NUMBER`

**提示（Prompt）**：默认 littlefs 磁盘格式版本（disk version）

**说明（Help）**

设为 `0` 时使用最新的 littlefs 磁盘格式版本 `LFS_DISK_VERSION`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_FS_LITTLEFS_DISK_VERSION && CONFIG_FILE_SYSTEM_LITTLEFS && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/fs/Kconfig.littlefs:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.littlefs#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → LittleFS 支持 → 支持选择 littlefs 磁盘格式版本（disk version）

**配置项引用（Symbol References）**：[`CONFIG_FS_LITTLEFS_DISK_VERSION`](P344_subsys_fs_配置项参考.md#CONFIG_FS_LITTLEFS_DISK_VERSION)、[`CONFIG_FILE_SYSTEM_LITTLEFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LITTLEFS)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_LITTLEFS_FC_HEAP_SIZE"></a>

## 344.61 `CONFIG_FS_LITTLEFS_FC_HEAP_SIZE`

**提示（Prompt）**：为 littlefs 启用灵活的文件缓存大小（flexible file cache sizes）

**说明（Help）**

littlefs 需要为每个文件提供缓冲区以缓存数据。应用自定义 littlefs 配置、为不同分区支持不同缓存大小时，固定预分配方式可能不适合：应用可能需要少量使用大缓存的文件，以及更多使用小缓存的文件。此时应为堆大小（heap size）指定正值。注意，每次分配都存在额外开销，影响堆中实际可用空间。

如果本选项为非正值，则自动将堆配置为最多支持 `FS_LITTLE_FS_NUM_FILES` 个块，每块 `FS_LITTLEFS_CACHE_SIZE` 字节。译注：原文此处使用 `FS_LITTLE_FS_NUM_FILES`；同组其他说明使用 `FS_LITTLEFS_NUM_FILES`。保留原文拼写，实际配置时须对照源码符号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LITTLEFS && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/fs/Kconfig.littlefs:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.littlefs#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → LittleFS 支持

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LITTLEFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LITTLEFS)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_LITTLEFS_FMP_DEV"></a>

## 344.62 `CONFIG_FS_LITTLEFS_FMP_DEV`

**提示（Prompt）**：支持闪存设备（flash devices）上的 littlefs

**说明（Help）**

通过闪存映射（flash_map）API，启用对闪存设备上的 littlefs 的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MAP && (CONFIG_FLASH_PAGE_LAYOUT || !CONFIG_FLASH_HAS_EXPLICIT_ERASE) && CONFIG_FILE_SYSTEM_LITTLEFS && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/fs/Kconfig.littlefs:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.littlefs#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → LittleFS 支持

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MAP)、[`CONFIG_FLASH_PAGE_LAYOUT`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_PAGE_LAYOUT)、[`CONFIG_FLASH_HAS_EXPLICIT_ERASE`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_HAS_EXPLICIT_ERASE)、[`CONFIG_FILE_SYSTEM_LITTLEFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LITTLEFS)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_LITTLEFS_FSTAB_AUTOMOUNT"></a>

## 344.63 `CONFIG_FS_LITTLEFS_FSTAB_AUTOMOUNT`

**提示（Prompt）**：支持 fstab 自动挂载（auto-mounting）

**说明（Help）**

启用 littlefs 对设备树（devicetree）fstab 自动挂载功能的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/fs/Kconfig.littlefs:135`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.littlefs#L135)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → LittleFS 支持

<a id="CONFIG_FS_LITTLEFS_HEAP_PER_ALLOC_OVERHEAD_SIZE"></a>

## 344.64 `CONFIG_FS_LITTLEFS_HEAP_PER_ALLOC_OVERHEAD_SIZE`

**提示（Prompt）**：littleFS 堆每次分配的额外开销（字节）

**说明（Help）**

自动计算 littleFS 堆总大小时，需要计入每个块分配产生的额外开销（per-allocation overhead）。因此，在计算堆大小时，为每个缓存块增加本项指定的字节数。

注意：如果应用无法打开 `FS_LITTLEFS_NUM_FILES` 预先规定的文件数量，请尝试增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FS_LITTLEFS_FC_HEAP_SIZE <= 0 && CONFIG_FILE_SYSTEM_LITTLEFS && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/fs/Kconfig.littlefs:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.littlefs#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → LittleFS 支持

**配置项引用（Symbol References）**：[`CONFIG_FS_LITTLEFS_FC_HEAP_SIZE`](P344_subsys_fs_配置项参考.md#CONFIG_FS_LITTLEFS_FC_HEAP_SIZE)、[`CONFIG_FILE_SYSTEM_LITTLEFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LITTLEFS)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_LITTLEFS_LOOKAHEAD_SIZE"></a>

## 344.65 `CONFIG_FS_LITTLEFS_LOOKAHEAD_SIZE`

**提示（Prompt）**：前瞻缓冲区大小（字节，lookahead buffer）

**说明（Help）**

较大的前瞻缓冲区（lookahead buffer）可增加一次分配扫描中找到的块数。此缓冲区以紧凑位图（bitmap）保存，因此每字节 RAM 可以跟踪 8 个块。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LITTLEFS && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/fs/Kconfig.littlefs:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.littlefs#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → LittleFS 支持 → LittleFS 设置（Settings）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LITTLEFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LITTLEFS)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_LITTLEFS_NUM_DIRS"></a>

## 344.66 `CONFIG_FS_LITTLEFS_NUM_DIRS`

**提示（Prompt）**：已打开目录数量上限（Maximum number of opened directories）

**说明（Help）**

此限制是所有已挂载 littlefs 文件系统共享的全局最大值（global maximum）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LITTLEFS && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/fs/Kconfig.littlefs:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.littlefs#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → LittleFS 支持 → LittleFS 设置（Settings）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LITTLEFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LITTLEFS)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_LITTLEFS_NUM_FILES"></a>

## 344.67 `CONFIG_FS_LITTLEFS_NUM_FILES`

**提示（Prompt）**：已打开文件数量上限（Maximum number of opened files）

**说明（Help）**

此限制是所有已挂载 littlefs 文件系统共享的全局最大值（global maximum）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LITTLEFS && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/fs/Kconfig.littlefs:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.littlefs#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → LittleFS 支持 → LittleFS 设置（Settings）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LITTLEFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LITTLEFS)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_LITTLEFS_PROG_SIZE"></a>

## 344.68 `CONFIG_FS_LITTLEFS_PROG_SIZE`

**提示（Prompt）**：块编程的最小大小（block program）

**说明（Help）**

所有编程操作（program operations）的大小都将是此值的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LITTLEFS && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/fs/Kconfig.littlefs:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.littlefs#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → LittleFS 支持 → LittleFS 设置（Settings）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LITTLEFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LITTLEFS)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FS_LITTLEFS_READ_SIZE"></a>

## 344.69 `CONFIG_FS_LITTLEFS_READ_SIZE`

**提示（Prompt）**：块读取的最小大小（block read）

**说明（Help）**

所有读操作（read operations）的大小都将是此值的整数倍。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LITTLEFS && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/fs/Kconfig.littlefs:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig.littlefs#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → LittleFS 支持 → LittleFS 设置（Settings）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LITTLEFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LITTLEFS)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FUSE_CLIENT"></a>

## 344.70 `CONFIG_FUSE_CLIENT`

**提示（Prompt）**：FUSE 客户端原语支持（client-side primitives）

**说明（Help）**

启用 FUSE 客户端原语（client-side primitives）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LIB_LINK
```

**被选择（Selected by）**

```text
CONFIG_FILE_SYSTEM_VIRTIOFS
```

**定义位置（Location）**：[`subsys/fs/fuse_client/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/fuse_client/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)、[`CONFIG_FILE_SYSTEM_VIRTIOFS`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_VIRTIOFS)。

<a id="CONFIG_FUSE_CLIENT_GID_VALUE"></a>

## 344.71 `CONFIG_FUSE_CLIENT_GID_VALUE`

**提示（Prompt）**：FUSE 组标识（group ID）

**说明（Help）**

每个 FUSE 请求都包含组标识（group ID）。此配置设置该值，其效果相当于由属于指定组 ID（GID）的用户访问文件或资源。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/fs/fuse_client/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/fuse_client/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FUSE_CLIENT_PID_VALUE"></a>

## 344.72 `CONFIG_FUSE_CLIENT_PID_VALUE`

**提示（Prompt）**：FUSE 进程标识（process ID）

**说明（Help）**

每个 FUSE 请求都包含进程标识（process ID）。此配置设置该值，其效果相当于由具有指定进程 ID（PID）的进程访问文件或资源。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/fs/fuse_client/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/fuse_client/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FUSE_CLIENT_UID_VALUE"></a>

## 344.73 `CONFIG_FUSE_CLIENT_UID_VALUE`

**提示（Prompt）**：FUSE 用户标识（user ID）

**说明（Help）**

每个 FUSE 请求都包含用户标识（user ID）。此配置设置该值，其效果相当于由具有指定用户 ID（UID）的用户访问文件或资源。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/fs/fuse_client/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/fuse_client/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_FUSE_FS_ACCESS"></a>

## 344.74 `CONFIG_FUSE_FS_ACCESS`

**提示（Prompt）**：通过 FUSE 访问文件系统分区（partitions）

**说明（Help）**

通过用户空间文件系统（FUSE）向主机系统暴露文件系统分区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_POSIX && CONFIG_FILE_SYSTEM
```

**主动选择（Selects）**

```text
CONFIG_NATIVE_USE_NSI_ERRNO
```

**定义位置（Location）**：[`subsys/fs/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统支持（File system support）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)、[`CONFIG_NATIVE_USE_NSI_ERRNO`](P033_arch_posix_配置项参考.md#CONFIG_NATIVE_USE_NSI_ERRNO)。

<a id="CONFIG_FUSE_LIBRARY_V2"></a>

## 344.75 `CONFIG_FUSE_LIBRARY_V2`

**提示（Prompt）**：使用 libfuse(2)

**说明（Help）**

使用主机 FUSE 库的第 2 版（v2）。较新的发行版可能不再提供此版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FUSE_LIBRARY_VERSION>
```

**定义位置（Location）**：[`subsys/fs/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统支持（File system support） → 通过 FUSE 访问文件系统分区（partitions） → 主机 FUSE 库版本（library version）

**配置项引用（Symbol References）**：[`CONFIG_FUSE_LIBRARY_VERSION`](P344_subsys_fs_配置项参考.md#CONFIG_FUSE_LIBRARY_VERSION)。

<a id="CONFIG_FUSE_LIBRARY_V3"></a>

## 344.76 `CONFIG_FUSE_LIBRARY_V3`

**提示（Prompt）**：使用 libfuse3

**说明（Help）**

使用主机 fuse3 库。较旧的发行版可能不提供此版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FUSE_LIBRARY_VERSION>
```

**定义位置（Location）**：[`subsys/fs/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统支持（File system support） → 通过 FUSE 访问文件系统分区（partitions） → 主机 FUSE 库版本（library version）

**配置项引用（Symbol References）**：[`CONFIG_FUSE_LIBRARY_VERSION`](P344_subsys_fs_配置项参考.md#CONFIG_FUSE_LIBRARY_VERSION)。

<a id="CONFIG_FUSE_LIBRARY_VERSION"></a>

## 344.77 `CONFIG_FUSE_LIBRARY_VERSION`

**提示（Prompt）**：主机 FUSE 库版本（library version）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FUSE_FS_ACCESS && CONFIG_FILE_SYSTEM
```

**默认值（Defaults）**

```text
CONFIG_FUSE_LIBRARY_V3
```

**可选项（Choices）**

```text
CONFIG_FUSE_LIBRARY_V2
CONFIG_FUSE_LIBRARY_V3
```

**定义位置（Location）**：[`subsys/fs/Kconfig:114`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/Kconfig#L114)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统支持（File system support） → 通过 FUSE 访问文件系统分区（partitions）

**配置项引用（Symbol References）**：[`CONFIG_FUSE_FS_ACCESS`](P344_subsys_fs_配置项参考.md#CONFIG_FUSE_FS_ACCESS)、[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)、[`CONFIG_FUSE_LIBRARY_V3`](P344_subsys_fs_配置项参考.md#CONFIG_FUSE_LIBRARY_V3)、[`CONFIG_FUSE_LIBRARY_V2`](P344_subsys_fs_配置项参考.md#CONFIG_FUSE_LIBRARY_V2)。

<a id="CONFIG_VIRTIOFS_CREATE_MODE_VALUE"></a>

## 344.78 `CONFIG_VIRTIOFS_CREATE_MODE_VALUE`

**提示（Prompt）**：创建文件／目录时使用的 Virtiofs 模式值（mode）

**说明（Help）**

创建文件或目录时必须设置模式（mode），此配置允许指定该值，以决定新建文件和目录的访问权限（access permissions）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
438
```

**定义位置（Location）**：[`subsys/fs/virtiofs/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/virtiofs/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_VIRTIOFS_DEBUG"></a>

## 344.79 `CONFIG_VIRTIOFS_DEBUG`

**提示（Prompt）**：打印 virtiofs 详细调试信息（verbose debug information）

**说明（Help）**

启用 virtiofs 详细调试信息打印。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LIB_LINK
```

**定义位置（Location）**：[`subsys/fs/virtiofs/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/virtiofs/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_VIRTIOFS_MAX_FILES"></a>

## 344.80 `CONFIG_VIRTIOFS_MAX_FILES`

**提示（Prompt）**：Virtiofs 最大打开文件数（max open files）

**说明（Help）**

Virtiofs 同时打开的文件数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/fs/virtiofs/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/virtiofs/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_VIRTIOFS_MAX_VQUEUE_SIZE"></a>

## 344.81 `CONFIG_VIRTIOFS_MAX_VQUEUE_SIZE`

**提示（Prompt）**：Virtiofs 虚拟队列最大大小（max virtqueue size）

**说明（Help）**

虚拟队列（virtqueue）的最大大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/fs/virtiofs/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/virtiofs/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_VIRTIOFS_NO_NOTIFICATION_QUEUE_SLOT"></a>

## 344.82 `CONFIG_VIRTIOFS_NO_NOTIFICATION_QUEUE_SLOT`

**提示（Prompt）**：省略通知队列（索引 1），将索引 1 视为首个请求队列

**说明（Help）**

按照 virtio 规范 v1.3 第 5.11.2 节，索引（idx）`1` 的队列是通知队列（notification queue），请求队列（request queues）从索引 `2` 开始；但原文指出，qemu+virtiofsd 的行为并非如此，索引 `1` 是第一个请求队列。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/fs/virtiofs/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/virtiofs/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<a id="CONFIG_VIRTIOFS_VIRTIOFSD_UNLINK_QUIRK"></a>

## 344.83 `CONFIG_VIRTIOFS_VIRTIOFSD_UNLINK_QUIRK`

**提示（Prompt）**：修复部分 virtiofsd 版本的 unlink() 行为

**说明（Help）**

某些 virtiofsd 版本，至少包括 Debian `1:7.2+dfsg-7+deb12u7`，如果之前未查找过（looked up）文件，执行 `unlink` 时就会以 `EIO` 失败。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/fs/virtiofs/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/virtiofs/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)。

<!-- kconfig-navigation -->

[上一章](P343_subsys_fb_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P345_subsys_gnss_配置项参考.md)
