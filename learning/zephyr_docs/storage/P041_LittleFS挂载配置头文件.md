---
id: learning.zephyr-docs.storage.fstypes-0
title: LittleFS挂载配置头文件
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/littlefs_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第41章\_LittleFS挂载配置头文件

原文：[littlefs_8h](https://docs.zephyrproject.org/latest/doxygen/html/littlefs_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/fs/littlefs.h` 提供 **LittleFS 文件系统（File System）**的挂载结构与配置宏，包含：

```c
#include <zephyr/types.h>
#include <zephyr/kernel.h>
#include <zephyr/storage/flash_map.h>
#include <lfs.h>
```

`struct fs_littlefs` 是 LittleFS 的挂载信息结构，成员详见[LittleFS挂载数据](P042_LittleFS挂载数据.md)。

## 41.1\_自定义尺寸配置

`FS_LITTLEFS_DECLARE_CUSTOM_CONFIG(name, alignment, read_sz, prog_sz, cache_sz, lookahead_sz)` 定义采用自定义尺寸参数的 LittleFS 配置。

| 参数 | 含义 |
| --- | --- |
| `name` | 结构对象名称；所定义对象具有文件作用域（File Scope） |
| `alignment` | 具体设备对读取/编程缓冲区要求的**对齐（Alignment）** |
| `read_sz` | 读取尺寸，参见 [`CONFIG_FS_LITTLEFS_READ_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FS_LITTLEFS_READ_SIZE) |
| `prog_sz` | **编程（Program）**尺寸，参见 [`CONFIG_FS_LITTLEFS_PROG_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FS_LITTLEFS_PROG_SIZE) |
| `cache_sz` | **缓存（Cache）**尺寸，参见 [`CONFIG_FS_LITTLEFS_CACHE_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FS_LITTLEFS_CACHE_SIZE) |
| `lookahead_sz` | **前瞻缓冲区（Lookahead Buffer）**尺寸，参见 [`CONFIG_FS_LITTLEFS_LOOKAHEAD_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FS_LITTLEFS_LOOKAHEAD_SIZE) |

该宏定义缓存所需的静态数组，并使用传入值初始化配置结构，以替代全局 Kconfig 默认值。必须将所定义对象的指针放入挂载结构 [`fs_mount_t`](https://docs.zephyrproject.org/latest/doxygen/html/structfs__mount__t.html) 的 `fs_data` 字段。

宏体如下，`__aligned` 用于声明对齐要求，`##` 将对象名与缓冲区后缀连接成标识符：

```c
static uint8_t __aligned(alignment) name ## _read_buffer[cache_sz];               \
static uint8_t __aligned(alignment) name ## _prog_buffer[cache_sz];               \
static uint32_t name ## _lookahead_buffer[(lookahead_sz) / sizeof(uint32_t)];     \
static struct fs_littlefs name = {                                                \
        .cfg = {                                                                  \
                .read_size = (read_sz),                                           \
                .prog_size = (prog_sz),                                           \
                .cache_size = (cache_sz),                                         \
                .lookahead_size = (lookahead_sz),                                 \
                .read_buffer = name ## _read_buffer,                              \
                .prog_buffer = name ## _prog_buffer,                              \
                .lookahead_buffer = name ## _lookahead_buffer,                    \
        },                                                                        \
}
```

若要采用 Kconfig 默认值，使用下一节的 [`FS_LITTLEFS_DECLARE_DEFAULT_CONFIG`](https://docs.zephyrproject.org/latest/doxygen/html/littlefs_8h.html#a9f584969a034fb4058c28fed33164d7a)。若要完全控制配置，应用可以直接定义并初始化 `struct fs_littlefs` 对象，但必须自行确保配置值满足 LittleFS 要求。

**若缓存大小采用非默认配置，还必须选择 [`CONFIG_FS_LITTLEFS_FC_HEAP_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FS_LITTLEFS_FC_HEAP_SIZE)，以放宽每文件缓存分配的尺寸约束。**

## 41.2\_默认尺寸配置

`FS_LITTLEFS_DECLARE_DEFAULT_CONFIG(name)` 定义静态数组，并使用 Kconfig 提供的默认尺寸初始化 LittleFS 配置。参数 `name` 是结构对象名称，定义的对象具有文件作用域。

```c
FS_LITTLEFS_DECLARE_CUSTOM_CONFIG(name,                          \
                                  4,                             \
                                  CONFIG_FS_LITTLEFS_READ_SIZE,  \
                                  CONFIG_FS_LITTLEFS_PROG_SIZE,  \
                                  CONFIG_FS_LITTLEFS_CACHE_SIZE, \
                                  CONFIG_FS_LITTLEFS_LOOKAHEAD_SIZE)
```

## 41.3\_磁盘版本主次号

两个宏的 `disk_version` 都是 LittleFS 分区的磁盘版本。[`GENMASK`](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d) 生成位范围掩码，[`FIELD_GET`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-siwx91x_8h.html#aa49a456f06f7bdbedfcf3517e461947e) 提取相应字段；宏体分别取位 `31..16` 和 `15..0`。
`FS_LITTLEFS_DISK_VERSION_MAJOR_GET(disk_version)` 提取 LittleFS 分区磁盘版本的**主版本号（Major Version）**：

```c
FIELD_GET(GENMASK(31, 16), disk_version)
```

`FS_LITTLEFS_DISK_VERSION_MINOR_GET(disk_version)` 提取该版本的**次版本号（Minor Version）**：

```c
FIELD_GET(GENMASK(15, 0), disk_version)
```


---

[上一章：文件系统驱动操作结构](P040_文件系统驱动操作结构.md) · [下一章：LittleFS挂载数据](P042_LittleFS挂载数据.md) · [返回大纲](大纲.md)
