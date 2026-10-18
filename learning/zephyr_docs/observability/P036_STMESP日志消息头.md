---
id: learning.zephyr-docs.observability.obstruct-3
title: STMESP日志消息头
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__log__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第36章\_STMESP日志消息头

原文：[structlog__frontend__stmesp__demux__log__header](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__log__header.html)。读取日期：2026-10-13，`latest`。

## 36.1\_类型与头文件

结构 [`log_frontend_stmesp_demux_log_header`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__log__header.html) 保存日志消息头（Logging Message Header）。它用于STM扩展激励端口（STM Extended Stimulus Port，STMESP）的日志解复用。

```c
#include <zephyr/logging/log_frontend_stmesp_demux.h>
```

## 36.2\_字段

位宽列为原文明确列出的位域（Bit-field）宽度；“—”表示本表未给位域宽度。

| 字段 | 类型 | 位宽 | 说明 |
| --- | --- | --- | --- |
| <a id="acec1720948196deb1f09ab1ea443ecb9"></a>[`major`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__log__header.html#acec1720948196deb1f09ab1ea443ecb9) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 3 | 主设备索引（Major Index） |
| <a id="a3b1474632ab446d8c9d590fb4bd8e420"></a>[`level`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__log__header.html#a3b1474632ab446d8c9d590fb4bd8e420) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 3 | 严重性级别（Severity Level） |
| <a id="a138b653d76c50c0454210b7a1d7ec60b"></a>[`total_len`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__log__header.html#a138b653d76c50c0454210b7a1d7ec60b) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 15 | 不包含本消息头的总长度（Total Length） |
| <a id="a0a378b7740a3def454bf34fe54927aa1"></a>[`package_len`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__log__header.html#a0a378b7740a3def454bf34fe54927aa1) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 10 | 参数包数据长度（Package Data Length） |
| <a id="ae18c81e29011d48e548a7daec2a3f9ba"></a>[`has_data`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__log__header.html#ae18c81e29011d48e548a7daec2a3f9ba) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 1 | 是否存在十六进制转储数据（Hexdump Data） |

本文档由 `zephyr/logging/log_frontend_stmesp_demux.h` 生成。

---

[上一章：插桩事件记录](P035_插桩事件记录.md) · [下一章：STMESP消息头联合体](P037_STMESP消息头联合体.md) · [返回大纲](大纲.md)
