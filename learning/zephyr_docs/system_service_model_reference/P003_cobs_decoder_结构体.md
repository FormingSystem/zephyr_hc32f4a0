---
id: learning.zephyr-docs.system-service-model-reference.page-3
title: cobs_decoder_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcobs__decoder.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_cobs\_decoder\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcobs__decoder.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

固定开销字节填充（COBS）的流式解码器状态。

```c
#include <zephyr/data/cobs.h>
```

<a id="details"></a>

一致开销字节填充（COBS）流式解码器状态。此结构体维护增量 COBS 解码的状态，使用前应通过 `cobs_decoder_init()` 初始化。

本数据类型文档由以下文件生成：

- `zephyr/data/cobs.h`

## 3.1\_原页交叉引用（Cross References）

- [zephyr/data/cobs.h](https://docs.zephyrproject.org/latest/doxygen/html/cobs_8h_source.html)
- [cobs_decoder_init()](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga49fa5a2c541ac72c2a0fe89971bec38d)

<a id="header-details"></a>

---

[上一章](P002_cbor_nb_writer_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_cobs_encoder_结构体.md)
