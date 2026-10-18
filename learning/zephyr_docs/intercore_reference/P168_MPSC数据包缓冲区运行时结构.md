---
id: learning.zephyr-docs.intercore_reference.mpscpbufref-168
title: MPSC数据包缓冲区运行时结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpsc__pbuf__buffer.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第168章\_MPSC数据包缓冲区运行时结构

原文：[structmpsc__pbuf__buffer](https://docs.zephyrproject.org/latest/doxygen/html/structmpsc__pbuf__buffer.html)。读取日期：2026-10-13，`latest`。

`mpsc_pbuf_buffer`是多生产者、单消费者（Multiple Producer, Single Consumer，MPSC）数据包缓冲区结构，定义在`zephyr/sys/mpsc_pbuf.h`。

## 168.1\_完整结构

```c
struct mpsc_pbuf_buffer {
        uint32_t tmp_wr_idx;

        uint32_t wr_idx;

        uint32_t tmp_rd_idx;

        uint32_t rd_idx;

        uint32_t flags;

        struct k_spinlock lock;

        mpsc_pbuf_notify_drop notify_drop;

        mpsc_pbuf_get_wlen get_wlen;

        /* Buffer. */
        uint32_t *buf;

        /* Buffer size in 32 bit words. */
        uint32_t size;

        /* Store max buffer usage. */
        uint32_t max_usage;

        struct k_sem sem;
};
```

## 168.2\_全部成员

下表翻译原参考页字段说明，并将仅来自完整源码注释的补充单独标出。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `tmp_wr_idx` | `uint32_t` | 临时写索引（Temporary Write Index） |
| `wr_idx` | `uint32_t` | 写索引（Write Index） |
| `tmp_rd_idx` | `uint32_t` | 临时读索引（Temporary Read Index） |
| `rd_idx` | `uint32_t` | 读索引（Read Index） |
| `flags` | `uint32_t` | 标志（Flags） |
| `lock` | `struct k_spinlock` | 锁（Lock）；类型为内核自旋锁（Spinlock） |
| `notify_drop` | `mpsc_pbuf_notify_drop` | 每次丢弃数据包时调用的用户回调（User Callback）；不需要时可为`NULL` |
| `get_wlen` | `mpsc_pbuf_get_wlen` | 获取数据包长度的回调 |
| `buf` | `uint32_t *` | 缓冲区；此说明来自源码可见注释 |
| `size` | `uint32_t` | 缓冲区大小，单位为32位字（32-bit Word）；此说明来自源码可见注释 |
| `max_usage` | `uint32_t` | 保存最大缓冲区使用量；此说明来自源码可见注释，未在此处指定单位 |
| `sem` | `struct k_sem` | 原页没有成员描述；类型是内核信号量（Semaphore），此处不推导内部计数约定 |

回调原型见[MPSC数据包缓冲区接口](P166_MPSC数据包缓冲区接口.md)，标志见[MPSC数据包缓冲区标志](P167_MPSC数据包缓冲区标志.md)；完整源码见[MPSC数据包缓冲区完整头文件](P171_MPSC数据包缓冲区完整头文件.md)。

---

[上一章：MPSC数据包缓冲区标志](P167_MPSC数据包缓冲区标志.md) · [下一章：MPSC数据包缓冲区配置](P169_MPSC数据包缓冲区配置.md) · [返回大纲](大纲.md)
