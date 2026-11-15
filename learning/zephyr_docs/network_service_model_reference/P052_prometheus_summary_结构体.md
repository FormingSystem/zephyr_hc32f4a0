---
id: learning.zephyr-docs.network-service-model-reference.page-52
title: prometheus_summary_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structprometheus__summary.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_prometheus\_summary\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structprometheus__summary.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于表示Prometheus摘要指标（Summary Metric）的类型。

```c
#include <zephyr/net/prometheus/summary.h>
```

<a id="details"></a>

用于表示 Prometheus 摘要（summary）指标的类型。参考资料：https://prometheus.io/docs/concepts/metric_types/#summary 。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 52.1\_数据成员（Data Fields）

<a id="r_aaef55d38ed7a9a8477d6e5ffeb748cbe"></a>

```c
struct prometheus_metric base
```

相关声明：[prometheus_metric](P051_prometheus_metric_结构体.md)、[base](#aaef55d38ed7a9a8477d6e5ffeb748cbe)。

Prometheus 摘要（summary）指标的基础部分。

<a id="r_a2fa33910c03339df68c33b54d5f267d7"></a>

```c
struct prometheus_summary_quantile * quantiles
```

相关声明：[prometheus_summary_quantile](P053_prometheus_summary_quantile_结构体.md)、[quantiles](#a2fa33910c03339df68c33b54d5f267d7)。

与 Prometheus 摘要指标关联的分位数（quantiles）数组。

<a id="r_a7e2604e9c9891137e7232ccaa9014c59"></a>

```c
size_t num_quantiles
```

相关声明：[num_quantiles](#a7e2604e9c9891137e7232ccaa9014c59)。

与 Prometheus 摘要指标关联的分位数数量。

<a id="r_aead1e2754a146d36564472f8a1867da7"></a>

```c
double sum
```

相关声明：[sum](#aead1e2754a146d36564472f8a1867da7)。

摘要指标中所有观测值的总和。

<a id="r_a6cd8daf6014b485ccbca0dd3194e5d87"></a>

```c
unsigned long count
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[count](#a6cd8daf6014b485ccbca0dd3194e5d87)。

摘要指标中的观测总次数。

<a id="r_ab9ba58c106f9dd73c425976b0680b785"></a>

```c
void * user_data
```

相关声明：[user_data](#ab9ba58c106f9dd73c425976b0680b785)。

用户数据（User Data）。

## 52.2\_详细说明（Detailed Documentation）

<a id="aaef55d38ed7a9a8477d6e5ffeb748cbe"></a>

### `base`

```c
struct prometheus_metric prometheus_summary::base
```

Prometheus 摘要（summary）指标的基础部分。

<a id="a6cd8daf6014b485ccbca0dd3194e5d87"></a>

### `count`

```c
unsigned long prometheus_summary::count
```

摘要指标中的观测总次数。

<a id="a7e2604e9c9891137e7232ccaa9014c59"></a>

### `num_quantiles`

```c
size_t prometheus_summary::num_quantiles
```

与 Prometheus 摘要指标关联的分位数数量。

<a id="a2fa33910c03339df68c33b54d5f267d7"></a>

### `quantiles`

```c
struct prometheus_summary_quantile* prometheus_summary::quantiles
```

与 Prometheus 摘要指标关联的分位数（quantiles）数组。

<a id="aead1e2754a146d36564472f8a1867da7"></a>

### `sum`

```c
double prometheus_summary::sum
```

摘要指标中所有观测值的总和。

<a id="ab9ba58c106f9dd73c425976b0680b785"></a>

### `user_data`

```c
void* prometheus_summary::user_data
```

用户数据（User Data）。

本数据类型文档由以下文件生成：

- `zephyr/net/prometheus/summary.h`

## 52.3\_原页交叉引用（Cross References）

- [zephyr/net/prometheus/summary.h](https://docs.zephyrproject.org/latest/doxygen/html/summary_8h_source.html)
- [prometheus_metric](P051_prometheus_metric_结构体.md)
- [prometheus_summary_quantile](P053_prometheus_summary_quantile_结构体.md)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [https://prometheus.io/docs/concepts/metric_types/#summary](https://prometheus.io/docs/concepts/metric_types/#summary)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P051_prometheus_metric_结构体.md) · [返回大纲](大纲.md) · [下一章](P053_prometheus_summary_quantile_结构体.md)
