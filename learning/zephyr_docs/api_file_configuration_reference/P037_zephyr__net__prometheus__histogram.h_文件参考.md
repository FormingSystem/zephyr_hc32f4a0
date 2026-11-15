---
id: learning.zephyr-docs.api-file-configuration-reference.page-37
title: zephyr__net__prometheus__histogram.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/histogram_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_zephyr\_\_net\_\_prometheus\_\_histogram.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/histogram_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Prometheus直方图（Histogram）的API。

<a id="details"></a>

```c
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/prometheus/metric.h>
#include <stddef.h>
```

查看此文件的源码。

Prometheus直方图（Histogram）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 37.1\_数据结构（Data Structures）

<a id="r_prometheus_5Fhistogram_5Fbucket"></a>

```c
struct prometheus_histogram_bucket
```

相关声明：[prometheus_histogram_bucket](../network_service_model_reference/P049_prometheus_histogram_bucket_结构体.md)。

Prometheus直方图桶（Histogram Bucket）的定义。

<a id="r_prometheus_5Fhistogram"></a>

```c
struct prometheus_histogram
```

相关声明：[prometheus_histogram](../network_service_model_reference/P048_prometheus_histogram_结构体.md)。

用于表示Prometheus直方图指标（Histogram Metric）的类型。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 37.2\_宏定义（Macros）

<a id="r_gaf2ddb4e016104faaf543d9a028756a0c"></a>

```c
#define PROMETHEUS_HISTOGRAM_DEFINE(_name, _desc, _label, _collector, ...)
```

相关声明：[PROMETHEUS_HISTOGRAM_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gaf2ddb4e016104faaf543d9a028756a0c)。

Prometheus 直方图（Histogram）的定义。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 37.3\_函数（Functions）

<a id="r_gaf0f24e64833302b74397654001ca5026"></a>

```c
int prometheus_histogram_observe (struct prometheus_histogram *histogram, double value)
```

相关声明：[prometheus_histogram_observe](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gaf0f24e64833302b74397654001ca5026)、[prometheus_histogram](../network_service_model_reference/P048_prometheus_histogram_结构体.md)。

在 Prometheus 直方图指标（Histogram Metric）中记录一个观测值（Observe a Value）。


## 37.4\_原页交叉引用（Cross References）

- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/net/prometheus/metric.h](../api_source_supplement_reference/P112_metric.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P320_histogram.h_源码浏览.md)
- [prometheus_histogram_bucket](../network_service_model_reference/P049_prometheus_histogram_bucket_结构体.md)
- [prometheus_histogram](../network_service_model_reference/P048_prometheus_histogram_结构体.md)
- [PROMETHEUS_HISTOGRAM_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gaf2ddb4e016104faaf543d9a028756a0c)
- [prometheus_histogram_observe](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gaf0f24e64833302b74397654001ca5026)

<a id="header-details"></a>

---

[上一章](P036_zephyr__bluetooth__hci_raw.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P038_zephyr__xen__hvm.h_文件参考.md)
