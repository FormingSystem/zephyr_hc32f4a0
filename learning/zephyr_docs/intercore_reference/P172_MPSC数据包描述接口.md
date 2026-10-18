---
id: learning.zephyr-docs.intercore_reference.mpscpbufref-172
title: MPSC数据包描述接口
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpsc__packet.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第172章\_MPSC数据包描述接口

原文：[group__mpsc__packet](https://docs.zephyrproject.org/latest/doxygen/html/group__mpsc__packet.html)。读取日期：2026-10-13，`latest`。

本页介绍多生产者、单消费者（Multiple Producer, Single Consumer，MPSC）数据包头部（Packet Header）。头文件为`zephyr/sys/mpsc_packet.h`。

通用头部、内部跳过数据包和通用联合体分别见[MPSC数据包头部](P173_MPSC数据包头部.md)、[MPSC数据包跳过结构](P174_MPSC数据包跳过结构.md)和[MPSC数据包通用联合体](P175_MPSC数据包通用联合体.md)。

## 172.1\_必须放在头部开头的字段

`MPSC_PBUF_HDR`必须加入每个数据包的第一个字（Word）中，展开为两个位域（Bit-field）：

```c
uint32_t valid: 1; \
uint32_t busy: 1
```

这些字段由数据包缓冲区控制，**除非接口明确另作规定，否则不得使用这些字段**。字段必须放在数据包头部结构的最开头。阅读说明：标识符`valid`表示有效（Valid），`busy`表示忙（Busy）；原页没有在此定义它们的完整状态转换规则。

## 172.2\_头部位数

```c
#define MPSC_PBUF_HDR_BITS 2
```

该宏给出第一个字中由缓冲区使用的位数，为2位。若接口明确要求有效位置位，例如写入单字或复制数据包的接口，应遵守该接口要求，见[MPSC数据包缓冲区接口](P166_MPSC数据包缓冲区接口.md)。

---

[上一章：MPSC数据包缓冲区完整头文件](P171_MPSC数据包缓冲区完整头文件.md) · [下一章：MPSC数据包头部](P173_MPSC数据包头部.md) · [返回大纲](大纲.md)
