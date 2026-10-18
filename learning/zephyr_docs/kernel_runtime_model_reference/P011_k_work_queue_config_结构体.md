---
id: learning.zephyr-docs.kernel-runtime-model-reference.page-11
title: k_work_queue_config_结构体
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structk__work__queue__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_k\_work\_queue\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structk__work__queue__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存工作队列（Work Queue）可选配置项的结构。

```c
#include <zephyr/kernel.h>
```

<a id="details"></a>

保存工作队列（Work Queue）可选配置项的结构。k_work_queue_start()不会保留此结构及其引用的值。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_a0929d83372efff6798bc69bb7ca1eaaa"></a>

```c
const char * name
```

相关声明：[name](#a0929d83372efff6798bc69bb7ca1eaaa)。

要赋予工作队列线程（Work Queue Thread）的名称。

<a id="r_afcf64d6e69d1ddfff8cbd749dafa4d13"></a>

```c
bool no_yield
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[no_yield](#afcf64d6e69d1ddfff8cbd749dafa4d13)。

控制工作队列线程是否应在工作项之间让出执行权（Yield）。

<a id="r_a5aa4a80d91ef36498443c163428b02c0"></a>

```c
bool essential
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[essential](#a5aa4a80d91ef36498443c163428b02c0)。

控制工作队列线程是否应标记为关键线程（Essential Thread）。

<a id="r_a517d9895f211d886de4b18f2f16d06c3"></a>

```c
uint32_t work_timeout_ms
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[work_timeout_ms](#a517d9895f211d886de4b18f2f16d06c3)。

控制工作队列是否监测工作项超时（Work Timeouts）。

## 11.2\_详细说明（Detailed Documentation）

<a id="a5aa4a80d91ef36498443c163428b02c0"></a>

### `essential`

```c
bool k_work_queue_config::essential
```

控制工作队列线程是否应标记为关键线程（Essential Thread）。

<a id="a0929d83372efff6798bc69bb7ca1eaaa"></a>

### `name`

```c
const char* k_work_queue_config::name
```

要赋予工作队列线程（Work Queue Thread）的名称。

保留为空时，线程没有名称。

<a id="afcf64d6e69d1ddfff8cbd749dafa4d13"></a>

### `no_yield`

```c
bool k_work_queue_config::no_yield
```

控制工作队列线程是否应在工作项之间让出执行权（Yield）。

在工作项之间让出执行权（Yield），有助于保证工作队列线程不会使其他线程饥饿，包括被工作项释放的协作式线程（Cooperative Threads）。这是默认行为。

设为true可阻止工作队列线程在工作项之间让出执行权（Yield）。需要连续完成一系列工作项而不让出控制权时，可采用此设置。

<a id="a517d9895f211d886de4b18f2f16d06c3"></a>

### `work_timeout_ms`

```c
uint32_t k_work_queue_config::work_timeout_ms
```

控制工作队列是否监测工作项超时（Work Timeouts）。

若此值非零且启用CONFIG_WORKQUEUE_WORK_TIMEOUT，工作队列将监测每个工作项的持续时间。如果工作项处理函数执行时间超过指定时间，工作队列线程将被中止；启用CONFIG_LOG时还会记录错误。

本数据类型文档由以下文件生成：

- `zephyr/kernel.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [k_work_queue_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gadfc56554f9bfe7b52309d79660188593)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_k_work_q_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_k_work_sync_结构体.md)
