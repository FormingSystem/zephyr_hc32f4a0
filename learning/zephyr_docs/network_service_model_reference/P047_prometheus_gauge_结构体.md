---
id: learning.zephyr-docs.network-service-model-reference.page-47
title: prometheus_gauge_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structprometheus__gauge.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_prometheus\_gauge\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structprometheus__gauge.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于表示Prometheus仪表指标（Gauge Metric）的类型。

```c
#include <zephyr/net/prometheus/gauge.h>
```

<a id="details"></a>

用于表示 Prometheus 仪表（gauge）指标的类型。参考资料：https://prometheus.io/docs/concepts/metric_types/#gauge 。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 47.1\_数据成员（Data Fields）

<a id="r_a6ad64e6b7806165cb4d78ac29ff3ae27"></a>

```c
struct prometheus_metric base
```

相关声明：[prometheus_metric](P051_prometheus_metric_结构体.md)、[base](#a6ad64e6b7806165cb4d78ac29ff3ae27)。

Prometheus 仪表（gauge）指标的基础部分。

<a id="r_aabf12d85b93d419e19d9c300cb6313a7"></a>

```c
double value
```

相关声明：[value](#aabf12d85b93d419e19d9c300cb6313a7)。

Prometheus 仪表（gauge）指标的值。

<a id="r_a3c935bf93e23c10961e3160cce45e741"></a>

```c
void * user_data
```

相关声明：[user_data](#a3c935bf93e23c10961e3160cce45e741)。

用户数据（User Data）。

## 47.2\_详细说明（Detailed Documentation）

<a id="a6ad64e6b7806165cb4d78ac29ff3ae27"></a>

### `base`

```c
struct prometheus_metric prometheus_gauge::base
```

Prometheus 仪表（gauge）指标的基础部分。

<a id="a3c935bf93e23c10961e3160cce45e741"></a>

### `user_data`

```c
void* prometheus_gauge::user_data
```

用户数据（User Data）。

<a id="aabf12d85b93d419e19d9c300cb6313a7"></a>

### `value`

```c
double prometheus_gauge::value
```

Prometheus 仪表（gauge）指标的值。

本数据类型文档由以下文件生成：

- `zephyr/net/prometheus/gauge.h`

## 47.3\_原页交叉引用（Cross References）

- [zephyr/net/prometheus/gauge.h](https://docs.zephyrproject.org/latest/doxygen/html/gauge_8h_source.html)
- [prometheus_metric](P051_prometheus_metric_结构体.md)
- [https://prometheus.io/docs/concepts/metric_types/#gauge](https://prometheus.io/docs/concepts/metric_types/#gauge)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P046_prometheus_counter_结构体.md) · [返回大纲](大纲.md) · [下一章](P048_prometheus_histogram_结构体.md)
