---
id: learning.zephyr-docs.observability.obstruct-8
title: STMESP硬件事件数据包
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__hw__event.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第41章\_STMESP硬件事件数据包

原文：[structlog__frontend__stmesp__demux__hw__event](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__hw__event.html)。读取日期：2026-10-13，`latest`。

## 41.1\_类型与头文件

结构 [`log_frontend_stmesp_demux_hw_event`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__hw__event.html) 保存包含硬件事件的数据包（Hardware Event Packet）。它用于STM扩展激励端口（STM Extended Stimulus Port，STMESP）的日志解复用。

```c
#include <zephyr/logging/log_frontend_stmesp_demux.h>
```

## 41.2\_字段

位宽列为原文明确列出的位域（Bit-field）宽度；“—”表示本表未给位域宽度。

| 字段 | 类型 | 位宽 | 说明 |
| --- | --- | --- | --- |
| <a id="a6a060e7fbda81c47eaa8088f3e45052a"></a>[`MPSC_PBUF_HDR`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__hw__event.html#a6a060e7fbda81c47eaa8088f3e45052a) | `宏展开` | — | 多生产者单消费者（Multiple Producer Single Consumer，MPSC）数据包处理所需的头部数据 |
| <a id="a5a781f1b681ef2499bf9ba2635261d4f"></a>[`type`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__hw__event.html#a5a781f1b681ef2499bf9ba2635261d4f) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 2 | 数据包类型（Type） |
| <a id="ae6872dcd7e11eeb431e3d990ccdad243"></a>[`content_invalid`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__hw__event.html#ae6872dcd7e11eeb431e3d990ccdad243) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 1 | 指示数据包有效性的标志（Validity Flag） |
| <a id="a0766f3aa6163ea1a197d674eac00305b"></a>[`timestamp`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__hw__event.html#a0766f3aa6163ea1a197d674eac00305b) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 59 | 时间戳（Timestamp） |
| <a id="a090039b38d646812a292510476d16644"></a>[`evt`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__hw__event.html#a090039b38d646812a292510476d16644) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | — | 硬件事件标识符（Hardware Event ID） |

`MPSC_PBUF_HDR` 是头部字段宏，在这里按原文保留，不将它当作具有独立C类型的普通成员。

本文档由 `zephyr/logging/log_frontend_stmesp_demux.h` 生成。

---

[上一章：STMESP跟踪点数据包](P040_STMESP跟踪点数据包.md) · [下一章：STMESP数据包联合体](P042_STMESP数据包联合体.md) · [返回大纲](大纲.md)
