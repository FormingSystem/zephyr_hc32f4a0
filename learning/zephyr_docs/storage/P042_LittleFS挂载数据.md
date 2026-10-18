---
id: learning.zephyr-docs.storage.fstypes-1
title: LittleFS挂载数据
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第42章\_LittleFS挂载数据

原文：[structfs__littlefs](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html)。读取日期：2026-10-13，`latest`。

`struct fs_littlefs` 是 **LittleFS 文件系统（File System）挂载（Mount）**使用的信息结构。

```c
#include <zephyr/fs/littlefs.h>
```

## 42.1\_配置与缓冲区

| 字段 | 原文类型/声明 | 含义与约束 |
| --- | --- | --- |
| [`cfg`](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#ab9b4cd8ce0aedfd071ea184d92b1224a) | `struct lfs_config` | LittleFS 配置，驱动提供默认值，可在挂载前自定义 |
| [`read_buffer`](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#ac1b102a94e6db2dfb4ca0d0bee5a561e) | `uint8_t *` | **读取缓存缓冲区（Read Cache Buffer）**，尺寸必须为 `cfg.cache_size` |
| [`prog_buffer`](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#a239d1ac90cc0de3a9cca766d41180def) | `uint8_t *` | **编程缓存缓冲区（Program Cache Buffer）**，尺寸必须为 `cfg.cache_size` |
| [`lookahead_buffer`](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#a7cd0dcd14e83138ba2ed698f55377e49) | `uint32_t *lookahead_buffer[CONFIG_FS_LITTLEFS_LOOKAHEAD_SIZE/sizeof(uint32_t)]` | **前瞻缓冲区（Lookahead Buffer）**，必须包含 `cfg.lookahead_size/4` 个元素，且 `cfg.lookahead_size` 必须是 8 的整数倍 |

译注：上表按原页保留 `lookahead_buffer` 的完整声明，包括指针星号和数组长度；不要把它与[配置宏](P041_LittleFS挂载配置头文件.md)中生成的 [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) 缓冲区数组声明混写。

## 42.2\_运行状态与同步

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`lfs`](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#a3a1902a64f78b65743786d154b435439) | `struct lfs` | LittleFS 状态，挂载时自动填充 |
| [`backend`](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#a0ebbf427f161722fc269573d86e562c5) | `void *` | 存储后端（Storage Backend），挂载时自动填充 |
| [`mutex`](https://docs.zephyrproject.org/latest/doxygen/html/structfs__littlefs.html#a337c24352a8f39c1d1f55682126341b5) | `struct k_mutex` | 保护此实例的**互斥锁（Mutex）**，挂载时自动填充 |

本结构的参考文档由 `zephyr/fs/littlefs.h` 生成。

---

[上一章：LittleFS挂载配置头文件](P041_LittleFS挂载配置头文件.md) · [下一章：Ext2配置头文件](P043_Ext2配置头文件.md) · [返回大纲](大纲.md)
