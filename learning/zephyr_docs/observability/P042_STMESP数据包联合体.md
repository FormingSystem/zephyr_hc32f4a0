---
id: learning.zephyr-docs.observability.obstruct-9
title: STMESP数据包联合体
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionlog__frontend__stmesp__demux__packet.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第42章\_STMESP数据包联合体

原文：[unionlog__frontend__stmesp__demux__packet](https://docs.zephyrproject.org/latest/doxygen/html/unionlog__frontend__stmesp__demux__packet.html)。读取日期：2026-10-13，`latest`。

## 42.1\_类型与头文件

联合体 [`log_frontend_stmesp_demux_packet`](https://docs.zephyrproject.org/latest/doxygen/html/unionlog__frontend__stmesp__demux__packet.html) 保存汇集所有数据包类型指针的联合体（Union）。它用于STM扩展激励端口（STM Extended Stimulus Port，STMESP）的日志解复用。

```c
#include <zephyr/logging/log_frontend_stmesp_demux.h>
```

## 42.2\_字段

位宽列为原文明确列出的位域（Bit-field）宽度；“—”表示本表未给位域宽度。

| 字段 | 类型 | 位宽 | 说明 |
| --- | --- | --- | --- |
| <a id="ac712f4dc2ca645e2ba6f6c638b41bf10"></a>[`rgeneric`](https://docs.zephyrproject.org/latest/doxygen/html/unionlog__frontend__stmesp__demux__packet.html#ac712f4dc2ca645e2ba6f6c638b41bf10) | `const union mpsc_pbuf_generic *` | — | 指向通用多生产者单消费者（Multiple Producer Single Consumer，MPSC）只读数据包 |
| [`generic`](https://docs.zephyrproject.org/latest/doxygen/html/unionlog__frontend__stmesp__demux__packet.html#a71d8ecb5afa1ac2cd64aaf21916119c5) | `union mpsc_pbuf_generic *` | — | 指向通用MPSC数据包 |
| <a id="ac75deeb2f665aeb5dcfd94090aa1a1cf"></a>[`log`](https://docs.zephyrproject.org/latest/doxygen/html/unionlog__frontend__stmesp__demux__packet.html#ac75deeb2f665aeb5dcfd94090aa1a1cf) | `struct log_frontend_stmesp_demux_log *` | — | 指向[日志消息数据包](P039_STMESP日志数据包.md) |
| <a id="aa68b1022f97c8806ee430a541190fc82"></a>[`trace_point`](https://docs.zephyrproject.org/latest/doxygen/html/unionlog__frontend__stmesp__demux__packet.html#aa68b1022f97c8806ee430a541190fc82) | `struct log_frontend_stmesp_demux_trace_point *` | — | 指向[跟踪点数据包](P040_STMESP跟踪点数据包.md) |
| <a id="ae764f7a3b04e66af22c52aa1d52a441e"></a>[`hw_event`](https://docs.zephyrproject.org/latest/doxygen/html/unionlog__frontend__stmesp__demux__packet.html#ae764f7a3b04e66af22c52aa1d52a441e) | `struct log_frontend_stmesp_demux_hw_event *` | — | 指向[硬件事件数据包](P041_STMESP硬件事件数据包.md) |
| <a id="a30d3cfc6071bebc1614f2f67c8a950c7"></a>[`generic_packet`](https://docs.zephyrproject.org/latest/doxygen/html/unionlog__frontend__stmesp__demux__packet.html#a30d3cfc6071bebc1614f2f67c8a950c7) | `struct log_frontend_stmesp_demux_packet_generic *` | — | 指向[通用STMESP解复用数据包](P038_STMESP通用数据包.md) |

本文档由 `zephyr/logging/log_frontend_stmesp_demux.h` 生成。

---

[上一章：STMESP硬件事件数据包](P041_STMESP硬件事件数据包.md) · [下一章：STMESP解复用配置](P043_STMESP解复用配置.md) · [返回大纲](大纲.md)
