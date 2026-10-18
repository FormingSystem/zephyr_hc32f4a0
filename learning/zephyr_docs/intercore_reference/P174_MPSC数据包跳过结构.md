---
id: learning.zephyr-docs.intercore_reference.mpscpbufref-174
title: MPSC数据包跳过结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpsc__pbuf__skip.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第174章\_MPSC数据包跳过结构

原文：[structmpsc__pbuf__skip](https://docs.zephyrproject.org/latest/doxygen/html/structmpsc__pbuf__skip.html)。读取日期：2026-10-13，`latest`。

`mpsc_pbuf_skip`是多生产者、单消费者（Multiple Producer, Single Consumer，MPSC）缓冲区的跳过数据包（Skip Packet）。它供数据包缓冲区内部使用。定义在`zephyr/sys/mpsc_packet.h`。

## 174.1\_原始结构

```c
struct mpsc_pbuf_skip {
        MPSC_PBUF_HDR;
        uint32_t len: 32 - MPSC_PBUF_HDR_BITS;
};
```

## 174.2\_展开后的位域

| 字段 | 基础类型 | 位宽 |
| --- | --- | --- |
| `valid` | `uint32_t` | 1 |
| `busy` | `uint32_t` | 1 |
| `len` | `uint32_t` | `32 - 2` |

原页将`MPSC_PBUF_HDR`展开成有效（Valid）与忙（Busy）两个1位字段，并将剩余位宽展开为`32 - 2`。源码保留符号表达式`32 - MPSC_PBUF_HDR_BITS`，即剩余30位。

阅读说明：`len`是长度字段（Length Field）；原页未指定其单位或编码规则。这些字段的访问限制见[MPSC数据包描述接口](P172_MPSC数据包描述接口.md)，不能因字段可见就擅自修改缓冲区控制位。

---

[上一章：MPSC数据包头部](P173_MPSC数据包头部.md) · [下一章：MPSC数据包通用联合体](P175_MPSC数据包通用联合体.md) · [返回大纲](大纲.md)
