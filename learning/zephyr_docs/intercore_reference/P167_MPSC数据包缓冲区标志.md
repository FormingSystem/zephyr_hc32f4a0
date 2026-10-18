---
id: learning.zephyr-docs.intercore_reference.mpscpbufref-167
title: MPSC数据包缓冲区标志
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__MPSC__PBUF__FLAGS.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第167章\_MPSC数据包缓冲区标志

原文：[group__MPSC__PBUF__FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__MPSC__PBUF__FLAGS.html)。读取日期：2026-10-13，`latest`。

本页列出多生产者、单消费者（Multiple Producer, Single Consumer，MPSC）数据包缓冲区（Packet Buffer）的标志（Flags），定义在`zephyr/sys/mpsc_pbuf.h`。

`BIT(n)`是选中第 n 位的位掩码（Bit Mask）宏。下表保留原来的四个定义；`MPSC_PBUF_FULL`描述当前状态，不能仅因它出现在标志表中，就把它解释为要求用户启用的工作模式。

## 167.1\_标志定义与含义

| 宏 | 值 | 含义 |
| --- | --- | --- |
| `MPSC_PBUF_SIZE_POW2` | `BIT(0)` | 表示缓冲区大小是2的幂；大小为2的幂时会应用相应优化 |
| <a id="ga983332f7aff31ed7b7e62cacf7960497"></a>`MPSC_PBUF_MODE_OVERWRITE` | `BIT(1)` | 表示缓冲区满时的处理策略：置位时从已满缓冲区分配会丢弃最旧的数据包；未置位时分配返回空指针 |
| `MPSC_PBUF_MAX_UTILIZATION` | `BIT(2)` | 表示跟踪缓冲区的最大使用量（Maximum Buffer Usage） |
| `MPSC_PBUF_FULL` | `BIT(3)` | 表示缓冲区当前已满（Full） |

## 167.2\_覆盖模式与等待

覆盖模式（Overwrite Mode）的原规则是：缓冲区满时丢弃最旧的数据包，使新的分配能够继续；未启用时，无法分配就返回`NULL`。在线程上下文（Thread Context）中，分配接口还规定先等待给定超时，再选择丢弃或返回空指针，详见[MPSC数据包缓冲区接口](P166_MPSC数据包缓冲区接口.md)。

---

[上一章：MPSC数据包缓冲区接口](P166_MPSC数据包缓冲区接口.md) · [下一章：MPSC数据包缓冲区运行时结构](P168_MPSC数据包缓冲区运行时结构.md) · [返回大纲](大纲.md)
