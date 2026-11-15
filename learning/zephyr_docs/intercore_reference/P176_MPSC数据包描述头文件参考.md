---
id: learning.zephyr-docs.intercore_reference.mpscpbufref-176
title: MPSC数据包描述头文件参考
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpsc__packet_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第176章\_MPSC数据包描述头文件参考

原文：[mpsc__packet_8h](https://docs.zephyrproject.org/latest/doxygen/html/mpsc__packet_8h.html)。读取日期：2026-10-13，`latest`。

本页对应多生产者、单消费者（Multiple Producer, Single Consumer，MPSC）数据包头部的`zephyr/sys/mpsc_packet.h`文件参考（File Reference）。

## 176.1\_依赖头文件

```c
#include <string.h>
#include <stdint.h>
#include <stdbool.h>
```

## 176.2\_数据结构

| 类型 | 含义 |
| --- | --- |
| `struct mpsc_pbuf_hdr` | 通用数据包头部（Generic Packet Header） |
| `struct mpsc_pbuf_skip` | 数据包缓冲区内部使用的跳过数据包（Skip Packet） |
| `union mpsc_pbuf_generic` | 通用数据包头部联合体（Union） |

字段细节分别见[MPSC数据包头部](P173_MPSC数据包头部.md)、[MPSC数据包跳过结构](P174_MPSC数据包跳过结构.md)和[MPSC数据包通用联合体](P175_MPSC数据包通用联合体.md)。

## 176.3\_宏定义

`MPSC_PBUF_HDR_BITS`取2，表示第一个字（Word）中由缓冲区使用的位数。`MPSC_PBUF_HDR`是必须加入每个数据包第一个字中的头部字段宏。完整定义与使用限制见[MPSC数据包描述接口](P172_MPSC数据包描述接口.md)，完整可见源码见[MPSC数据包描述完整头文件](P177_MPSC数据包描述完整头文件.md)。

---

[上一章：MPSC数据包通用联合体](P175_MPSC数据包通用联合体.md) · [下一章：MPSC数据包描述完整头文件](P177_MPSC数据包描述完整头文件.md) · [返回大纲](大纲.md)
