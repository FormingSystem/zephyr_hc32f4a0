---
id: learning.zephyr-docs.network-service-model-reference.page-48
title: prometheus_histogram_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structprometheus__histogram.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_prometheus\_histogram\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structprometheus__histogram.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于表示Prometheus直方图指标（Histogram Metric）的类型。

```c
#include <zephyr/net/prometheus/histogram.h>
```

<a id="details"></a>

用于表示 Prometheus 直方图（histogram）指标的类型。参考资料：https://prometheus.io/docs/concepts/metric_types/#histogram 。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 48.1\_数据成员（Data Fields）

<a id="r_adc3ad0fe48cad15282a907e977bbf16b"></a>

```c
struct prometheus_metric base
```

相关声明：[prometheus_metric](P051_prometheus_metric_结构体.md)、[base](#adc3ad0fe48cad15282a907e977bbf16b)。

Prometheus 直方图（histogram）指标的基础部分。

<a id="r_a2f37871231727963173b7336ea8cfafb"></a>

```c
struct prometheus_histogram_bucket * buckets
```

相关声明：[prometheus_histogram_bucket](P049_prometheus_histogram_bucket_结构体.md)、[buckets](#a2f37871231727963173b7336ea8cfafb)。

直方图中的桶（buckets）数组。

<a id="r_a01cfda4eab91d6776b7f7b11279d2785"></a>

```c
size_t num_buckets
```

相关声明：[num_buckets](#a01cfda4eab91d6776b7f7b11279d2785)。

直方图中的桶数量。

<a id="r_a65616857524ef4eeb09a577e0432e787"></a>

```c
double sum
```

相关声明：[sum](#a65616857524ef4eeb09a577e0432e787)。

直方图中所有观测值的总和。

<a id="r_a6ae0aad29b927a729263324704917873"></a>

```c
unsigned long count
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[count](#a6ae0aad29b927a729263324704917873)。

直方图中的观测总次数。

<a id="r_a1ef93a8a5d7a934cf207041d461ce8ec"></a>

```c
void * user_data
```

相关声明：[user_data](#a1ef93a8a5d7a934cf207041d461ce8ec)。

用户数据（User Data）。

## 48.2\_详细说明（Detailed Documentation）

<a id="adc3ad0fe48cad15282a907e977bbf16b"></a>

### `base`

```c
struct prometheus_metric prometheus_histogram::base
```

Prometheus 直方图（histogram）指标的基础部分。

<a id="a2f37871231727963173b7336ea8cfafb"></a>

### `buckets`

```c
struct prometheus_histogram_bucket* prometheus_histogram::buckets
```

直方图中的桶（buckets）数组。

<a id="a6ae0aad29b927a729263324704917873"></a>

### `count`

```c
unsigned long prometheus_histogram::count
```

直方图中的观测总次数。

<a id="a01cfda4eab91d6776b7f7b11279d2785"></a>

### `num_buckets`

```c
size_t prometheus_histogram::num_buckets
```

直方图中的桶数量。

<a id="a65616857524ef4eeb09a577e0432e787"></a>

### `sum`

```c
double prometheus_histogram::sum
```

直方图中所有观测值的总和。

<a id="a1ef93a8a5d7a934cf207041d461ce8ec"></a>

### `user_data`

```c
void* prometheus_histogram::user_data
```

用户数据（User Data）。

本数据类型文档由以下文件生成：

- `zephyr/net/prometheus/histogram.h`

## 48.3\_原页交叉引用（Cross References）

- [zephyr/net/prometheus/histogram.h](https://docs.zephyrproject.org/latest/doxygen/html/histogram_8h_source.html)
- [prometheus_metric](P051_prometheus_metric_结构体.md)
- [prometheus_histogram_bucket](P049_prometheus_histogram_bucket_结构体.md)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [https://prometheus.io/docs/concepts/metric_types/#histogram](https://prometheus.io/docs/concepts/metric_types/#histogram)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P047_prometheus_gauge_结构体.md) · [返回大纲](大纲.md) · [下一章](P049_prometheus_histogram_bucket_结构体.md)
