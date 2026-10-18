---
id: learning.zephyr-docs.intercore_reference.mpscpbufref-177
title: MPSC数据包描述完整头文件
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpsc__packet_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第177章\_MPSC数据包描述完整头文件

原文：[mpsc__packet_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/mpsc__packet_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留`zephyr/sys/mpsc_packet.h`完整官方可见源码（Source Code），仅去除网页行号和行尾空白。MPSC 指多生产者、单消费者（Multiple Producer, Single Consumer）。版权为2021年的 Nordic Semiconductor ASA，许可证`Apache-2.0`原样保留。

## 177.1\_完整源码

```c
/*
 * Copyright (c) 2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_SYS_MPSC_PACKET_H_
#define ZEPHYR_INCLUDE_SYS_MPSC_PACKET_H_

#include <string.h>
#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif


#define MPSC_PBUF_HDR_BITS 2

#define MPSC_PBUF_HDR \
        uint32_t valid: 1; \
        uint32_t busy: 1

struct mpsc_pbuf_hdr {
        MPSC_PBUF_HDR;
        uint32_t data: 32 - MPSC_PBUF_HDR_BITS;
};

struct mpsc_pbuf_skip {
        MPSC_PBUF_HDR;
        uint32_t len: 32 - MPSC_PBUF_HDR_BITS;
};

union mpsc_pbuf_generic {
        struct mpsc_pbuf_hdr hdr;
        struct mpsc_pbuf_skip skip;
        uint32_t raw;
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_SYS_MPSC_PACKET_H_ */
```

## 177.2\_代码阅读说明

`MPSC_PBUF_HDR_BITS`为头部使用的位数，取2。`MPSC_PBUF_HDR`声明有效（Valid）与忙（Busy）两个1位字段。两个结构分别把其余`32 - MPSC_PBUF_HDR_BITS`位用于`data`或`len`；通用联合体（Union）则提供头部、跳过数据包和原始整数三种视图。

本网页可见源码除了版权与头文件保护结束标记，没有其他自然语言注释。接口文档中的字段权限要求和结构用途另见[MPSC数据包描述接口](P172_MPSC数据包描述接口.md)，没有补造进源码。

`__cplusplus`分支提供 C++ 的 C 语言链接约定，末尾注释标记头文件保护宏`ZEPHYR_INCLUDE_SYS_MPSC_PACKET_H_`的结束。

---

[上一章：MPSC数据包描述头文件参考](P176_MPSC数据包描述头文件参考.md) · [下一章：RPMsg命令行后端接口](P178_RPMsg命令行后端接口.md) · [返回大纲](大纲.md)
