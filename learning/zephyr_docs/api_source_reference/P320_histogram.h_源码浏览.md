---
id: learning.zephyr-docs.api-source-reference.page-320
title: histogram.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/histogram_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第320章\_histogram.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/histogram_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/histogram_8h.html)。

## 320.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="foldopen00079"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="agroup__prometheus_html_gaf0f24e64833302b74397654001ca5026"></a>
<a id="ametric_8h_html"></a>
<a id="astructprometheus__histogram__bucket_html"></a>
<a id="astructprometheus__histogram__bucket_html_a93865334a397013506d39a28505586c4"></a>
<a id="astructprometheus__histogram__bucket_html_aa18e37384ee094972b6a330bb4323fa3"></a>
<a id="astructprometheus__histogram_html"></a>
<a id="astructprometheus__histogram_html_a01cfda4eab91d6776b7f7b11279d2785"></a>
<a id="astructprometheus__histogram_html_a1ef93a8a5d7a934cf207041d461ce8ec"></a>
<a id="astructprometheus__histogram_html_a2f37871231727963173b7336ea8cfafb"></a>
<a id="astructprometheus__histogram_html_a65616857524ef4eeb09a577e0432e787"></a>
<a id="astructprometheus__histogram_html_a6ae0aad29b927a729263324704917873"></a>
<a id="astructprometheus__histogram_html_adc3ad0fe48cad15282a907e977bbf16b"></a>
<a id="astructprometheus__metric_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology
 * Copyright (c) 2024 Nordic Semiconductor
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_PROMETHEUS_HISTOGRAM_H_
#define ZEPHYR_INCLUDE_NET_PROMETHEUS_HISTOGRAM_H_


#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/prometheus/metric.h>

#include <stddef.h>

struct prometheus_histogram_bucket {
        double upper_bound;
        unsigned long count;
};

struct prometheus_histogram {
        struct prometheus_metric base;
        struct prometheus_histogram_bucket *buckets;
        size_t num_buckets;
        double sum;
        unsigned long count;
        void *user_data;
};

#define PROMETHEUS_HISTOGRAM_DEFINE(_name, _desc, _label, _collector, ...) \
        STRUCT_SECTION_ITERABLE(prometheus_histogram, _name) = {        \
                .base.name = STRINGIFY(_name),                          \
                .base.type = PROMETHEUS_HISTOGRAM,                      \
                .base.description = _desc,                              \
                .base.labels[0] = __DEBRACKET _label,                   \
                .base.num_labels = 1,                                   \
                .base.collector = _collector,                           \
                .buckets = NULL,                                        \
                .num_buckets = 0,                                       \
                .sum = 0.0,                                             \
                .count = 0U,                                            \
                .user_data = COND_CODE_0(                               \
                        NUM_VA_ARGS_LESS_1(LIST_DROP_EMPTY(__VA_ARGS__, _)), \
                        (NULL),                                         \
                        (GET_ARG_N(1, __VA_ARGS__))),                   \
        }

int prometheus_histogram_observe(struct prometheus_histogram *histogram, double value);


#endif /* ZEPHYR_INCLUDE_NET_PROMETHEUS_HISTOGRAM_H_ */
```

## 320.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Mustafa Abdullah Kus, Sparse Technology。

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 112 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_PROMETHEUS_HISTOGRAM_H_`。

## 320.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/histogram_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/net/prometheus/metric.h](https://docs.zephyrproject.org/latest/doxygen/html/metric_8h.html)
- [prometheus_histogram_bucket](../network_service_model_reference/P049_prometheus_histogram_bucket_结构体.md)
- [upper_bound](../network_service_model_reference/P049_prometheus_histogram_bucket_结构体.md#aa18e37384ee094972b6a330bb4323fa3)
- [count](../network_service_model_reference/P049_prometheus_histogram_bucket_结构体.md#a93865334a397013506d39a28505586c4)
- [prometheus_histogram](../network_service_model_reference/P048_prometheus_histogram_结构体.md)
- [prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)
- [base](../network_service_model_reference/P048_prometheus_histogram_结构体.md#adc3ad0fe48cad15282a907e977bbf16b)
- [buckets](../network_service_model_reference/P048_prometheus_histogram_结构体.md#a2f37871231727963173b7336ea8cfafb)
- [num_buckets](../network_service_model_reference/P048_prometheus_histogram_结构体.md#a01cfda4eab91d6776b7f7b11279d2785)
- [sum](../network_service_model_reference/P048_prometheus_histogram_结构体.md#a65616857524ef4eeb09a577e0432e787)
- [count](../network_service_model_reference/P048_prometheus_histogram_结构体.md#a6ae0aad29b927a729263324704917873)
- [user_data](../network_service_model_reference/P048_prometheus_histogram_结构体.md#a1ef93a8a5d7a934cf207041d461ce8ec)
- [prometheus_histogram_observe](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gaf0f24e64833302b74397654001ca5026)
- [metric.h](https://docs.zephyrproject.org/latest/doxygen/html/metric_8h.html)
- [prometheus_histogram_bucket::count](../network_service_model_reference/P049_prometheus_histogram_bucket_结构体.md#a93865334a397013506d39a28505586c4)
- [prometheus_histogram_bucket::upper_bound](../network_service_model_reference/P049_prometheus_histogram_bucket_结构体.md#aa18e37384ee094972b6a330bb4323fa3)
- [prometheus_histogram::num_buckets](../network_service_model_reference/P048_prometheus_histogram_结构体.md#a01cfda4eab91d6776b7f7b11279d2785)
- [prometheus_histogram::user_data](../network_service_model_reference/P048_prometheus_histogram_结构体.md#a1ef93a8a5d7a934cf207041d461ce8ec)
- [prometheus_histogram::buckets](../network_service_model_reference/P048_prometheus_histogram_结构体.md#a2f37871231727963173b7336ea8cfafb)
- [prometheus_histogram::sum](../network_service_model_reference/P048_prometheus_histogram_结构体.md#a65616857524ef4eeb09a577e0432e787)
- [prometheus_histogram::count](../network_service_model_reference/P048_prometheus_histogram_结构体.md#a6ae0aad29b927a729263324704917873)
- [prometheus_histogram::base](../network_service_model_reference/P048_prometheus_histogram_结构体.md#adc3ad0fe48cad15282a907e977bbf16b)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P319_hid_host.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P321_hooks.h_源码浏览.md)
