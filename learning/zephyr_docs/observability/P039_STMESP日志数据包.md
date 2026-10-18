---
id: learning.zephyr-docs.observability.obstruct-6
title: STMESP日志数据包
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__log.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第39章\_STMESP日志数据包

原文：[structlog__frontend__stmesp__demux__log](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__log.html)。读取日期：2026-10-13，`latest`。

## 39.1\_类型与头文件

结构 [`log_frontend_stmesp_demux_log`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__log.html) 保存包含日志消息的数据包（Logging Message Packet）。它用于STM扩展激励端口（STM Extended Stimulus Port，STMESP）的日志解复用。

```c
#include <zephyr/logging/log_frontend_stmesp_demux.h>
```

## 39.2\_字段

位宽列为原文明确列出的位域（Bit-field）宽度；“—”表示本表未给位域宽度。

| 字段 | 类型 | 位宽 | 说明 |
| --- | --- | --- | --- |
| <a id="ad25f0378c2c3ba3d153a58a843704033"></a>[`MPSC_PBUF_HDR`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__log.html#ad25f0378c2c3ba3d153a58a843704033) | `宏展开` | — | 多生产者单消费者（Multiple Producer Single Consumer，MPSC）数据包处理所需的头部数据 |
| <a id="adb1b61bdca3a97df2c8ba2b34fc2ebff"></a>[`type`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__log.html#adb1b61bdca3a97df2c8ba2b34fc2ebff) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 2 | 数据包类型（Type） |
| <a id="a84cf9f64d96e87cfd2bb9d859fed3886"></a>[`content_invalid`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__log.html#a84cf9f64d96e87cfd2bb9d859fed3886) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 1 | 指示数据包有效性的标志（Validity Flag） |
| <a id="af2b9820efce6f58d655b08a306c8d8d1"></a>[`timestamp`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__log.html#af2b9820efce6f58d655b08a306c8d8d1) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 59 | 时间戳（Timestamp） |
| <a id="aa5b7175e05dbdcc41d75c5412ce30b15"></a>[`hdr`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__log.html#aa5b7175e05dbdcc41d75c5412ce30b15) | `struct log_frontend_stmesp_demux_log_header` | — | 日志头，见[日志消息头](P036_STMESP日志消息头.md) |
| <a id="ab063e3ed4d81cbdb4ec417508c55bd13"></a>[`padding`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__log.html#ab063e3ed4d81cbdb4ec417508c55bd13) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | — | 填充（Padding），使数据按8字节对齐 |
| <a id="ae8c62ffd8a11fbcebce29ed934f52597"></a>`data[]` | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | — | 内容（Content），使用不定长数组成员 |

`MPSC_PBUF_HDR` 是头部字段宏，在这里按原文保留，不将它当作具有独立C类型的普通成员。

本文档由 `zephyr/logging/log_frontend_stmesp_demux.h` 生成。

---

[上一章：STMESP通用数据包](P038_STMESP通用数据包.md) · [下一章：STMESP跟踪点数据包](P040_STMESP跟踪点数据包.md) · [返回大纲](大纲.md)
