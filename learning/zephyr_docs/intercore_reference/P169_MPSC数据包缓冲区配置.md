---
id: learning.zephyr-docs.intercore_reference.mpscpbufref-169
title: MPSC数据包缓冲区配置
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpsc__pbuf__buffer__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第169章\_MPSC数据包缓冲区配置

原文：[structmpsc__pbuf__buffer__config](https://docs.zephyrproject.org/latest/doxygen/html/structmpsc__pbuf__buffer__config.html)。读取日期：2026-10-13，`latest`。

`mpsc_pbuf_buffer_config`是多生产者、单消费者（Multiple Producer, Single Consumer，MPSC）数据包缓冲区的配置结构（Configuration Structure），定义在`zephyr/sys/mpsc_pbuf.h`。

## 169.1\_完整结构

```c
struct mpsc_pbuf_buffer_config {
        /* Pointer to a memory used for storing packets. */
        uint32_t *buf;

        /* Buffer size in 32 bit words. */
        uint32_t size;

        /* Callbacks. */
        mpsc_pbuf_notify_drop notify_drop;
        mpsc_pbuf_get_wlen get_wlen;

        /* Configuration flags. */
        uint32_t flags;
};
```

## 169.2\_配置字段

原参考页只列出类型；下表依据完整头文件中的可见注释，并结合原回调名称说明各字段。回调具体契约见[MPSC数据包缓冲区接口](P166_MPSC数据包缓冲区接口.md)。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="a2090b3da5dc85c68601fd7bdb54f6174"></a>`buf` | `uint32_t *` | 用于存放数据包的内存指针 |
| `size` | `uint32_t` | 缓冲区大小，单位为32位字（32-bit Word） |
| `notify_drop` | `mpsc_pbuf_notify_drop` | 回调（Callback）；数据包丢弃通知 |
| `get_wlen` | `mpsc_pbuf_get_wlen` | 回调；获取数据包字长 |
| `flags` | `uint32_t` | 配置标志（Configuration Flags） |

配置传入`mpsc_pbuf_init()`，可用标志见[MPSC数据包缓冲区标志](P167_MPSC数据包缓冲区标志.md)。

---

[上一章：MPSC数据包缓冲区运行时结构](P168_MPSC数据包缓冲区运行时结构.md) · [下一章：MPSC数据包缓冲区头文件参考](P170_MPSC数据包缓冲区头文件参考.md) · [返回大纲](大纲.md)
