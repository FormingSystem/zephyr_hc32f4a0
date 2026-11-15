---
id: learning.zephyr-docs.observability.obstruct-4
title: STMESP消息头联合体
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionlog__frontend__stmesp__demux__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第37章\_STMESP消息头联合体

原文：[unionlog__frontend__stmesp__demux__header](https://docs.zephyrproject.org/latest/doxygen/html/unionlog__frontend__stmesp__demux__header.html)。读取日期：2026-10-13，`latest`。

## 37.1\_类型与头文件

联合体 [`log_frontend_stmesp_demux_header`](https://docs.zephyrproject.org/latest/doxygen/html/unionlog__frontend__stmesp__demux__header.html) 保存用于向日志消息头写入原始数据的联合体（Union）。它用于STM扩展激励端口（STM Extended Stimulus Port，STMESP）的日志解复用。

```c
#include <zephyr/logging/log_frontend_stmesp_demux.h>
```

## 37.2\_字段

位宽列为原文明确列出的位域（Bit-field）宽度；“—”表示本表未给位域宽度。

| 字段 | 类型 | 位宽 | 说明 |
| --- | --- | --- | --- |
| <a id="ae94bab609a4f5c51eef7886db712420d"></a>[`log`](https://docs.zephyrproject.org/latest/doxygen/html/unionlog__frontend__stmesp__demux__header.html#ae94bab609a4f5c51eef7886db712420d) | `struct log_frontend_stmesp_demux_log_header` | — | 日志头结构，见[日志消息头](P036_STMESP日志消息头.md) |
| <a id="ae868e8f2e8b0623781d3f9377490c72a"></a>[`raw`](https://docs.zephyrproject.org/latest/doxygen/html/unionlog__frontend__stmesp__demux__header.html#ae868e8f2e8b0623781d3f9377490c72a) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | — | 原始数据字（Raw Word） |

本文档由 `zephyr/logging/log_frontend_stmesp_demux.h` 生成。

---

[上一章：STMESP日志消息头](P036_STMESP日志消息头.md) · [下一章：STMESP通用数据包](P038_STMESP通用数据包.md) · [返回大纲](大纲.md)
