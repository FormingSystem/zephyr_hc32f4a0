---
id: learning.zephyr-docs.network-service-model-reference.page-46
title: prometheus_counter_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structprometheus__counter.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_prometheus\_counter\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structprometheus__counter.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于表示Prometheus计数器指标（Counter Metric）的类型。

```c
#include <zephyr/net/prometheus/counter.h>
```

<a id="details"></a>

用于表示 Prometheus 计数器（counter）指标的类型。参考资料：https://prometheus.io/docs/concepts/metric_types/#counter 。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 46.1\_数据成员（Data Fields）

<a id="r_a33714d75e20f8a69a7068c5c57fe3a37"></a>

```c
struct prometheus_metric base
```

相关声明：[prometheus_metric](P051_prometheus_metric_结构体.md)、[base](#a33714d75e20f8a69a7068c5c57fe3a37)。

Prometheus 计数器（counter）指标的基础部分。

<a id="r_a048376a671e83df41034908b85e9e234"></a>

```c
uint64_t value
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[value](#a048376a671e83df41034908b85e9e234)。

Prometheus 计数器（counter）指标的值。

<a id="r_a28793edc31342bd6572493d7aa72eaca"></a>

```c
void * user_data
```

相关声明：[user_data](#a28793edc31342bd6572493d7aa72eaca)。

用户数据（User Data）。

## 46.2\_详细说明（Detailed Documentation）

<a id="a33714d75e20f8a69a7068c5c57fe3a37"></a>

### `base`

```c
struct prometheus_metric prometheus_counter::base
```

Prometheus 计数器（counter）指标的基础部分。

<a id="a28793edc31342bd6572493d7aa72eaca"></a>

### `user_data`

```c
void* prometheus_counter::user_data
```

用户数据（User Data）。

<a id="a048376a671e83df41034908b85e9e234"></a>

### `value`

```c
uint64_t prometheus_counter::value
```

Prometheus 计数器（counter）指标的值。

本数据类型文档由以下文件生成：

- `zephyr/net/prometheus/counter.h`

## 46.3\_原页交叉引用（Cross References）

- [zephyr/net/prometheus/counter.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2prometheus_2counter_8h_source.html)
- [prometheus_metric](P051_prometheus_metric_结构体.md)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [https://prometheus.io/docs/concepts/metric_types/#counter](https://prometheus.io/docs/concepts/metric_types/#counter)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P045_prometheus_collector_结构体.md) · [返回大纲](大纲.md) · [下一章](P047_prometheus_gauge_结构体.md)
