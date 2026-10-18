---
id: learning.zephyr-docs.intercore_reference.pbufref-152
title: SPSC数据包缓冲区公共布局
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structspsc__pbuf__common.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第152章\_SPSC数据包缓冲区公共布局

原文：[structspsc__pbuf__common](https://docs.zephyrproject.org/latest/doxygen/html/structspsc__pbuf__common.html)。读取日期：2026-10-13，`latest`。

`spsc_pbuf_common`是单生产者、单消费者（Single Producer, Single Consumer，SPSC）数据包缓冲区控制块（Control Block）的第一部分。

它仅包含初始化时设置的数据和读者（Reader）会访问的数据。若数据包在两个核之间共享，读者修改的数据应与写者（Writer）修改的数据位于不同的缓存行（Cache Line）。

## 152.1\_结构与成员

```c
struct spsc_pbuf_common {
        uint32_t len;           /* Length of data[] in bytes. */
        uint32_t flags;         /* Flags. See @ref SPSC_PBUF_FLAGS */
        uint32_t rd_idx;        /* Index of the first valid byte in data[] */
};
```

| 参数 | 含义 |
| --- | --- |
| `len` | `data[]`长度，单位为字节 |
| `flags` | 标志（Flags），参见 SPSC 数据包缓冲区标志 |
| `rd_idx` | `data[]`中第一个有效字节的索引 |

成员含义依据`zephyr/sys/spsc_pbuf.h`可见注释译出，完整文件见[SPSC数据包缓冲区完整头文件](P156_SPSC数据包缓冲区完整头文件.md)。

---

[上一章：SPSC数据包缓冲区结构](P151_SPSC数据包缓冲区结构.md) · [下一章：SPSC数据包缓冲区缓存扩展](P153_SPSC数据包缓冲区缓存扩展.md) · [返回大纲](大纲.md)
