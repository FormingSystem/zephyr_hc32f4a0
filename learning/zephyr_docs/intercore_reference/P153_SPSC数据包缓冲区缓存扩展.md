---
id: learning.zephyr-docs.intercore_reference.pbufref-153
title: SPSC数据包缓冲区缓存扩展
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structspsc__pbuf__ext__cache.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第153章\_SPSC数据包缓冲区缓存扩展

原文：[structspsc__pbuf__ext__cache](https://docs.zephyrproject.org/latest/doxygen/html/structspsc__pbuf__ext__cache.html)。读取日期：2026-10-13，`latest`。

`spsc_pbuf_ext_cache`是使用缓存（Cache）时，单生产者、单消费者（Single Producer, Single Consumer，SPSC）数据包缓冲区的剩余部分。

它包含仅由写者（Writer）修改的数据。加入间隔（Gap）是为了确保这部分数据与读者（Reader）修改的数据位于不同缓存行（Cache Line）。

## 153.1\_结构与成员

```c
struct spsc_pbuf_ext_cache {
        uint8_t reserved[Z_SPSC_PBUF_PADDING];
        uint32_t wr_idx;        /* Index of the first free byte in data[] */
        uint8_t data[];         /* Buffer data. */
};
```

| 参数 | 含义 |
| --- | --- |
| `reserved` | 用于隔开读者与写者数据的填充区（Padding），长度为`Z_SPSC_PBUF_PADDING` |
| `wr_idx` | `data[]`中第一个空闲字节的索引 |
| `data[]` | 缓冲区数据（Buffer Data） |

## 153.2\_原页展开的数组长度

原字段参考将`reserved`显示为以下类型：

```c
uint8_t reserved[MAX(0, MAX(0, 0) -(int) sizeof(struct spsc_pbuf_common))]
```

译注：这是文档生成配置下的宏展开。源码使用`Z_SPSC_PBUF_PADDING`，不能把展开式中的0当作所有目标平台的数据缓存行大小。该宏取`MAX(0, Z_SPSC_PBUF_DCACHE_LINE - (int)sizeof(struct spsc_pbuf_common))`，用于填满缓存行。完整条件定义见[SPSC数据包缓冲区完整头文件](P156_SPSC数据包缓冲区完整头文件.md)。头文件为`zephyr/sys/spsc_pbuf.h`。

---

[上一章：SPSC数据包缓冲区公共布局](P152_SPSC数据包缓冲区公共布局.md) · [下一章：SPSC数据包缓冲区无缓存扩展](P154_SPSC数据包缓冲区无缓存扩展.md) · [返回大纲](大纲.md)
