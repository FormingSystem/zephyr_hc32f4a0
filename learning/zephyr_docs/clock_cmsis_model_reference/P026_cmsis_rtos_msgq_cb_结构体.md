---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-26
title: cmsis_rtos_msgq_cb_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcmsis__rtos__msgq__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_cmsis\_rtos\_msgq\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcmsis__rtos__msgq__cb.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

CMSIS-RTOSv2 消息队列（Message Queue）的控制块。

```c
#include <zephyr/portability/cmsis_types.h>
```

<a id="details"></a>

CMSIS-RTOSv2 消息队列（Message Queue）的控制块。应用可以提供指向消息队列控制块的指针，以采用手动的用户自定义方式为 RTOS 对象分配存储。控制块在 `osMessageQueueNew()` 内初始化。

本结构体文档由以下文件生成：

- `zephyr/portability/cmsis_types.h`

## 26.1\_原页交叉引用（Cross References）

- [zephyr/portability/cmsis_types.h](https://docs.zephyrproject.org/latest/doxygen/html/cmsis__types_8h_source.html)

<a id="header-details"></a>

---

[上一章](P025_cmsis_rtos_mempool_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P027_cmsis_rtos_mutex_cb_结构体.md)
