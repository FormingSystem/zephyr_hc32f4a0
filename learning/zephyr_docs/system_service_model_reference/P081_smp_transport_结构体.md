---
id: learning.zephyr-docs.system-service-model-reference.page-81
title: smp_transport_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsmp__transport.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第81章\_smp\_transport\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsmp__transport.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于发送简单管理协议（SMP）响应的传输对象。

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

<a id="details"></a>

用于发送简单管理协议（SMP）响应的传输对象。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 81.1\_数据成员（Data Fields）

<a id="r_a2bb0436ae57a1c1d084f3fed1aa16652"></a>

```c
struct k_work work
```

相关声明：[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)、[work](#a2bb0436ae57a1c1d084f3fed1aa16652)。

<a id="r_a929ff7e97273dd18920ddc8426c6646f"></a>

```c
struct k_fifo fifo
```

相关声明：[k_fifo](../queue_reference/P004_内核FIFO结构.md)、[fifo](#a929ff7e97273dd18920ddc8426c6646f)。

<a id="r_ab732e7d9574b78635a90ff559306daaa"></a>

```c
struct smp_transport_api_t functions
```

相关声明：[smp_transport_api_t](P082_smp_transport_api_t_结构体.md)、[functions](#ab732e7d9574b78635a90ff559306daaa)。

## 81.2\_详细说明（Detailed Documentation）

<a id="a929ff7e97273dd18920ddc8426c6646f"></a>

### `fifo`

```c
struct k_fifo smp_transport::fifo
```

<a id="ab732e7d9574b78635a90ff559306daaa"></a>

### `functions`

```c
struct smp_transport_api_t smp_transport::functions
```

<a id="a2bb0436ae57a1c1d084f3fed1aa16652"></a>

### `work`

```c
struct k_work smp_transport::work
```

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/transport/smp.h`

## 81.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/transport/smp.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2transport_2smp_8h_source.html)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [smp_transport_api_t](P082_smp_transport_api_t_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P080_smp_streamer_结构体.md) · [返回大纲](大纲.md) · [下一章](P082_smp_transport_api_t_结构体.md)
