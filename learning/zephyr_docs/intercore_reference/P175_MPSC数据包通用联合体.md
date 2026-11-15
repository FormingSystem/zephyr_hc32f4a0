---
id: learning.zephyr-docs.intercore_reference.mpscpbufref-175
title: MPSC数据包通用联合体
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionmpsc__pbuf__generic.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第175章\_MPSC数据包通用联合体

原文：[unionmpsc__pbuf__generic](https://docs.zephyrproject.org/latest/doxygen/html/unionmpsc__pbuf__generic.html)。读取日期：2026-10-13，`latest`。

`mpsc_pbuf_generic`是多生产者、单消费者（Multiple Producer, Single Consumer，MPSC）缓冲区的通用数据包头部联合体（Union），定义在`zephyr/sys/mpsc_packet.h`。

## 175.1\_完整联合体

```c
union mpsc_pbuf_generic {
        struct mpsc_pbuf_hdr hdr;
        struct mpsc_pbuf_skip skip;
        uint32_t raw;
};
```

## 175.2\_成员类型

| 成员 | 类型 |
| --- | --- |
| `hdr` | `struct mpsc_pbuf_hdr` |
| `skip` | `struct mpsc_pbuf_skip` |
| `raw` | `uint32_t` |

原参考页没有逐字段解释。阅读说明：`hdr`提供[MPSC数据包头部](P173_MPSC数据包头部.md)视图，`skip`提供[MPSC数据包跳过结构](P174_MPSC数据包跳过结构.md)视图，`raw`提供原始32位无符号整数（Raw 32-bit Unsigned Integer）视图；它们共享联合体存储。

---

[上一章：MPSC数据包跳过结构](P174_MPSC数据包跳过结构.md) · [下一章：MPSC数据包描述头文件参考](P176_MPSC数据包描述头文件参考.md) · [返回大纲](大纲.md)
