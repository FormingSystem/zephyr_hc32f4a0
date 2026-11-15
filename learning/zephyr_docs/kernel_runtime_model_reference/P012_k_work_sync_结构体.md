---
id: learning.zephyr-docs.kernel-runtime-model-reference.page-12
title: k_work_sync_结构体
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structk__work__sync.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_k\_work\_sync\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structk__work__sync.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存工作项或队列上待完成同步操作（Synchronous Operation）内部状态的结构。

```c
#include <zephyr/kernel.h>
```

<a id="details"></a>

保存工作项或队列上待完成同步操作（Synchronous Operation）内部状态的结构。调用k_work_flush()、k_work_cancel_sync()及同类刷新与取消API时，由调用方提供此类型的实例。被引用对象必须持续存在到调用返回，并且调用方线程和工作队列线程都必须能够访问它。说明（Note）：启用CONFIG_KERNEL_COHERENCE时，对象必须分配在一致性内存（Coherent Memory）中，参见sys_cache_is_mem_coherent()；这些架构上的栈通常不具备一致性。违规行为会由运行时断言检测。所有成员均供内部使用，不应直接访问。

> 译注：原文在栈一致性说明之后还出现孤立短语“be stack-allocated”，句子不完整；这里不据此推断允许在栈上分配，仍保留其明确的一致性内存要求。

本数据类型文档由以下文件生成：

- `zephyr/kernel.h`

## 12.1\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [k_work_flush()](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gabd1cda459bab538fb2d6dfd84a73b253)
- [k_work_cancel_sync()](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gab2b05cfe3af08f7d32c3946fa1c808f9)
- [sys_cache_is_mem_coherent()](../cache_reference/P001_公共缓存接口.md#ga17071b17b61be7a8c00064a69d107b19)

<a id="header-details"></a>

---

[上一章](P011_k_work_queue_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P013_pmu_counter_config_结构体.md)
