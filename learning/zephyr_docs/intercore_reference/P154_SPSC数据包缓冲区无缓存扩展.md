---
id: learning.zephyr-docs.intercore_reference.pbufref-154
title: SPSC数据包缓冲区无缓存扩展
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structspsc__pbuf__ext__nocache.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第154章\_SPSC数据包缓冲区无缓存扩展

原文：[structspsc__pbuf__ext__nocache](https://docs.zephyrproject.org/latest/doxygen/html/structspsc__pbuf__ext__nocache.html)。读取日期：2026-10-13，`latest`。

`spsc_pbuf_ext_nocache`是不使用缓存（Cache）时，单生产者、单消费者（Single Producer, Single Consumer，SPSC）数据包缓冲区的剩余部分，定义在`zephyr/sys/spsc_pbuf.h`。

## 154.1\_结构与成员

```c
struct spsc_pbuf_ext_nocache {
        uint32_t wr_idx;        /* Index of the first free byte in data[] */
        uint8_t data[];         /* Buffer data. */
};
```

| 参数 | 含义 |
| --- | --- |
| `wr_idx` | `data[]`中第一个空闲字节的索引 |
| `data[]` | 缓冲区数据（Buffer Data） |

以上成员说明依据头文件可见注释译出。本结构没有缓存扩展中的填充数组，相关结构见[SPSC数据包缓冲区缓存扩展](P153_SPSC数据包缓冲区缓存扩展.md)。

---

[上一章：SPSC数据包缓冲区缓存扩展](P153_SPSC数据包缓冲区缓存扩展.md) · [下一章：SPSC数据包缓冲区头文件参考](P155_SPSC数据包缓冲区头文件参考.md) · [返回大纲](大纲.md)
