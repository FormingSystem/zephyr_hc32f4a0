---
id: learning.zephyr-docs.intercore_reference.mpscpbufref-173
title: MPSC数据包头部
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpsc__pbuf__hdr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第173章\_MPSC数据包头部

原文：[structmpsc__pbuf__hdr](https://docs.zephyrproject.org/latest/doxygen/html/structmpsc__pbuf__hdr.html)。读取日期：2026-10-13，`latest`。

`mpsc_pbuf_hdr`是多生产者、单消费者（Multiple Producer, Single Consumer，MPSC）缓冲区的通用数据包头部（Generic Packet Header）。定义在`zephyr/sys/mpsc_packet.h`。

## 173.1\_原始结构

```c
struct mpsc_pbuf_hdr {
        MPSC_PBUF_HDR;
        uint32_t data: 32 - MPSC_PBUF_HDR_BITS;
};
```

## 173.2\_展开后的位域

| 字段 | 基础类型 | 位宽 |
| --- | --- | --- |
| `valid` | `uint32_t` | 1 |
| `busy` | `uint32_t` | 1 |
| `data` | `uint32_t` | `32 - 2` |

原页将`MPSC_PBUF_HDR`展开成有效（Valid）与忙（Busy）两个1位字段，并将剩余位宽展开为`32 - 2`。源码保留符号表达式`32 - MPSC_PBUF_HDR_BITS`，即剩余30位。

阅读说明：`data`为其余数据位（Data Bits）。这些字段的访问限制见[MPSC数据包描述接口](P172_MPSC数据包描述接口.md)，不能因字段可见就擅自修改缓冲区控制位。

---

[上一章：MPSC数据包描述接口](P172_MPSC数据包描述接口.md) · [下一章：MPSC数据包跳过结构](P174_MPSC数据包跳过结构.md) · [返回大纲](大纲.md)
