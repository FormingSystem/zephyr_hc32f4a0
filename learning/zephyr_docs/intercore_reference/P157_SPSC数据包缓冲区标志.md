---
id: learning.zephyr-docs.intercore_reference.lockfreeref-157
title: SPSC数据包缓冲区标志
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__SPSC__PBUF__FLAGS.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第157章\_SPSC数据包缓冲区标志

原文：[group__SPSC__PBUF__FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__SPSC__PBUF__FLAGS.html)。读取日期：2026-10-13，`latest`。

本页介绍单生产者、单消费者（Single Producer, Single Consumer，SPSC）数据包缓冲区（Packet Buffer）的标志（Flags）。头文件为`zephyr/sys/spsc_pbuf.h`，主接口见[数据包缓冲区接口](P150_SPSC数据包缓冲区接口.md)。

## 157.1\_缓存处理标志

```c
#define SPSC_PBUF_CACHE BIT(0)
```

`BIT(0)`是选中第0位的位掩码（Bit Mask）表达式。`SPSC_PBUF_CACHE`表示需要进行缓存（Cache）处理。

**该标志只能在数据包缓冲区由两个核共享时使用。单核上不应手动处理缓存，因为这会导致数据损坏（Data Corruption）。** 这是原页对该标志的使用限制，不能省略。

## 157.2\_最大使用量字段

```c
#define SPSC_PBUF_UTILIZATION_BITS 24
#define SPSC_PBUF_UTILIZATION_OFFSET 8
```

`SPSC_PBUF_UTILIZATION_BITS`是存储最大使用量（Maximum Utilization）字段的宽度，为24位。`SPSC_PBUF_UTILIZATION_OFFSET`是该字段的偏移，为8位。完整头文件见[原始源码](P156_SPSC数据包缓冲区完整头文件.md)。

---

[上一章：SPSC数据包缓冲区完整头文件](P156_SPSC数据包缓冲区完整头文件.md) · [下一章：MPSC无锁队列接口](P158_MPSC无锁队列接口.md) · [返回大纲](大纲.md)
