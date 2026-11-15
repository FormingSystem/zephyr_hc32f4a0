---
id: learning.zephyr-docs.observability.obstruct-7
title: STMESP跟踪点数据包
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__trace__point.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第40章\_STMESP跟踪点数据包

原文：[structlog__frontend__stmesp__demux__trace__point](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__trace__point.html)。读取日期：2026-10-13，`latest`。

## 40.1\_类型与头文件

结构 [`log_frontend_stmesp_demux_trace_point`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__trace__point.html) 保存包含跟踪点的数据包（Trace Point Packet）。它用于STM扩展激励端口（STM Extended Stimulus Port，STMESP）的日志解复用。

```c
#include <zephyr/logging/log_frontend_stmesp_demux.h>
```

## 40.2\_字段

位宽列为原文明确列出的位域（Bit-field）宽度；“—”表示本表未给位域宽度。

| 字段 | 类型 | 位宽 | 说明 |
| --- | --- | --- | --- |
| <a id="ae3e776e4a470ccb3abd8f6a73ce7b21b"></a>[`MPSC_PBUF_HDR`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__trace__point.html#ae3e776e4a470ccb3abd8f6a73ce7b21b) | `宏展开` | — | 多生产者单消费者（Multiple Producer Single Consumer，MPSC）数据包处理所需的头部数据 |
| <a id="ab250b6782df720df3d1cdb37ab25a024"></a>[`type`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__trace__point.html#ab250b6782df720df3d1cdb37ab25a024) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 2 | 数据包类型（Type） |
| <a id="a300adc8bd0882810ae4a5759a76857ce"></a>[`content_invalid`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__trace__point.html#a300adc8bd0882810ae4a5759a76857ce) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 1 | 指示数据包有效性的标志（Validity Flag） |
| <a id="a0bdc2a3e1afb5748e08e68617f2ccbb6"></a>[`has_data`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__trace__point.html#a0bdc2a3e1afb5748e08e68617f2ccbb6) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 1 | 指示跟踪点是否携带数据的标志 |
| <a id="a6e1892f15fa3149f8161a1792420ba73"></a>[`timestamp`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__trace__point.html#a6e1892f15fa3149f8161a1792420ba73) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 54 | 时间戳（Timestamp）；在40 MHz计时频率下，54位可表示超过14年的时间 |
| <a id="acfa056769b9ba00b945e1ff7d1e4cdb9"></a>[`major`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__trace__point.html#acfa056769b9ba00b945e1ff7d1e4cdb9) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 4 | 主设备标识符（Major ID） |
| <a id="a0ca97d4ffd9bae1d640b8f99c8bd5ace"></a>[`source_id`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__trace__point.html#a0ca97d4ffd9bae1d640b8f99c8bd5ace) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | — | 源标识符（Source ID），用于压缩日志（Compressed Logging） |
| <a id="aeb86bfae01245a4778d08ac9c1ee138a"></a>[`id`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__trace__point.html#aeb86bfae01245a4778d08ac9c1ee138a) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | — | 标识符（Identifier，ID） |
| <a id="ada954ed2971c2fc720a1d1f2634c0e2a"></a>[`data`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__trace__point.html#ada954ed2971c2fc720a1d1f2634c0e2a) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | — | 内容（Content） |

`MPSC_PBUF_HDR` 是头部字段宏，在这里按原文保留，不将它当作具有独立C类型的普通成员。

本文档由 `zephyr/logging/log_frontend_stmesp_demux.h` 生成。

---

[上一章：STMESP日志数据包](P039_STMESP日志数据包.md) · [下一章：STMESP硬件事件数据包](P041_STMESP硬件事件数据包.md) · [返回大纲](大纲.md)
