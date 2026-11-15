---
id: learning.zephyr-docs.system-service-model-reference.page-4
title: cobs_encoder_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcobs__encoder.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_cobs\_encoder\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcobs__encoder.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

固定开销字节填充（COBS）的流式编码器状态。

```c
#include <zephyr/data/cobs.h>
```

<a id="details"></a>

一致开销字节填充（COBS）流式编码器状态。此结构体维护增量 COBS 编码的状态，使用前应通过 `cobs_encoder_init()` 初始化。

本数据类型文档由以下文件生成：

- `zephyr/data/cobs.h`

## 4.1\_原页交叉引用（Cross References）

- [zephyr/data/cobs.h](https://docs.zephyrproject.org/latest/doxygen/html/cobs_8h_source.html)
- [cobs_encoder_init()](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gafebbd3ea1b058cf7834dd534048602fb)

<a id="header-details"></a>

---

[上一章](P003_cobs_decoder_结构体.md) · [返回大纲](大纲.md) · [下一章](P005_console_input_结构体.md)
