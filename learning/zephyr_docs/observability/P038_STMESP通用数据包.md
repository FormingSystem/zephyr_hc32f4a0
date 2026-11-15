---
id: learning.zephyr-docs.observability.obstruct-5
title: STMESP通用数据包
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__packet__generic.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第38章\_STMESP通用数据包

原文：[structlog__frontend__stmesp__demux__packet__generic](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__packet__generic.html)。读取日期：2026-10-13，`latest`。

## 38.1\_类型与头文件

结构 [`log_frontend_stmesp_demux_packet_generic`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__packet__generic.html) 保存通用STP解复用数据包（Generic STP Demux Packet）。它用于STM扩展激励端口（STM Extended Stimulus Port，STMESP）的日志解复用。STP表示MIPI系统跟踪协议（MIPI System Trace Protocol）。

```c
#include <zephyr/logging/log_frontend_stmesp_demux.h>
```

## 38.2\_字段

位宽列为原文明确列出的位域（Bit-field）宽度；“—”表示本表未给位域宽度。

| 字段 | 类型 | 位宽 | 说明 |
| --- | --- | --- | --- |
| <a id="ac202cf6bc5bc8699a858e10de2c0c492"></a>[`MPSC_PBUF_HDR`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__packet__generic.html#ac202cf6bc5bc8699a858e10de2c0c492) | `宏展开` | — | 多生产者单消费者（Multiple Producer Single Consumer，MPSC）数据包处理所需的头部数据 |
| <a id="a7a86c5de5e5b33830d963add116c1feb"></a>[`type`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__packet__generic.html#a7a86c5de5e5b33830d963add116c1feb) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 2 | 数据包类型（Type） |
| <a id="a42d6b5192e0f9ba897a2986d645c6a6c"></a>[`content_invalid`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__packet__generic.html#a42d6b5192e0f9ba897a2986d645c6a6c) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 1 | 指示数据包有效性的标志（Validity Flag） |

`MPSC_PBUF_HDR` 是头部字段宏，在这里按原文保留，不将它当作具有独立C类型的普通成员。

本文档由 `zephyr/logging/log_frontend_stmesp_demux.h` 生成。

---

[上一章：STMESP消息头联合体](P037_STMESP消息头联合体.md) · [下一章：STMESP日志数据包](P039_STMESP日志数据包.md) · [返回大纲](大纲.md)
