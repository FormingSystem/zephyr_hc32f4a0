---
id: learning.zephyr-docs.api-source-reference.page-846
title: summary.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/summary_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第846章\_summary.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/summary_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/summary_8h.html)。

## 846.1\_原始可见代码（Source Code）

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
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="foldopen00045"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00082"></a>
<a id="foldopen00083"></a>
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
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="agroup__prometheus_html_ga7683de05e8b135161120ad5d3f2edc2c"></a>
<a id="agroup__prometheus_html_ga98369eb2a7c8ce36f7570ed5b55410d8"></a>
<a id="ametric_8h_html"></a>
<a id="astructprometheus__metric_html"></a>
<a id="astructprometheus__summary__quantile_html"></a>
<a id="astructprometheus__summary__quantile_html_a53fb78e35a0748f568d7bb15b083b037"></a>
<a id="astructprometheus__summary__quantile_html_a788d30204d7ce61940741cefd2c073f6"></a>
<a id="astructprometheus__summary__quantile_html_a811db0cddd6fd444a899be83e4116b92"></a>
<a id="astructprometheus__summary_html"></a>
<a id="astructprometheus__summary_html_a2fa33910c03339df68c33b54d5f267d7"></a>
<a id="astructprometheus__summary_html_a6cd8daf6014b485ccbca0dd3194e5d87"></a>
<a id="astructprometheus__summary_html_a7e2604e9c9891137e7232ccaa9014c59"></a>
<a id="astructprometheus__summary_html_aaef55d38ed7a9a8477d6e5ffeb748cbe"></a>
<a id="astructprometheus__summary_html_ab9ba58c106f9dd73c425976b0680b785"></a>
<a id="astructprometheus__summary_html_aead1e2754a146d36564472f8a1867da7"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology
 * Copyright (c) 2024 Nordic Semiconductor
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_PROMETHEUS_SUMMARY_H_
#define ZEPHYR_INCLUDE_NET_PROMETHEUS_SUMMARY_H_


#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/prometheus/metric.h>

#include <stddef.h>

struct prometheus_summary_quantile {
        double quantile;
        double value;
        void *user_data;
};

struct prometheus_summary {
        struct prometheus_metric base;
        struct prometheus_summary_quantile *quantiles;
        size_t num_quantiles;
        double sum;
        unsigned long count;
        void *user_data;
};


#define PROMETHEUS_SUMMARY_DEFINE(_name, _desc, _label, _collector, ...) \
        STRUCT_SECTION_ITERABLE(prometheus_summary, _name) = {          \
                .base.name = STRINGIFY(_name),                          \
                .base.type = PROMETHEUS_SUMMARY,                        \
                .base.description = _desc,                              \
                .base.labels[0] = __DEBRACKET _label,                   \
                .base.num_labels = 1,                                   \
                .base.collector = _collector,                           \
                .quantiles = NULL,                                      \
                .num_quantiles = 0,                                     \
                .sum = 0.0,                                             \
                .count = 0U,                                            \
                .user_data = COND_CODE_0(                               \
                        NUM_VA_ARGS_LESS_1(LIST_DROP_EMPTY(__VA_ARGS__, _)), \
                        (NULL),                                         \
                        (GET_ARG_N(1, __VA_ARGS__))),                   \
        }

int prometheus_summary_observe(struct prometheus_summary *summary, double value);

int prometheus_summary_observe_set(struct prometheus_summary *summary,
                                   double value, unsigned long count);


#endif /* ZEPHYR_INCLUDE_NET_PROMETHEUS_SUMMARY_H_ */
```

## 846.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Mustafa Abdullah Kus, Sparse Technology。

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 130 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_PROMETHEUS_SUMMARY_H_`。

## 846.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/summary_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/net/prometheus/metric.h](https://docs.zephyrproject.org/latest/doxygen/html/metric_8h.html)
- [prometheus_summary_quantile](../network_service_model_reference/P053_prometheus_summary_quantile_结构体.md)
- [quantile](../network_service_model_reference/P053_prometheus_summary_quantile_结构体.md#a811db0cddd6fd444a899be83e4116b92)
- [value](../network_service_model_reference/P053_prometheus_summary_quantile_结构体.md#a53fb78e35a0748f568d7bb15b083b037)
- [user_data](../network_service_model_reference/P053_prometheus_summary_quantile_结构体.md#a788d30204d7ce61940741cefd2c073f6)
- [prometheus_summary](../network_service_model_reference/P052_prometheus_summary_结构体.md)
- [prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)
- [base](../network_service_model_reference/P052_prometheus_summary_结构体.md#aaef55d38ed7a9a8477d6e5ffeb748cbe)
- [quantiles](../network_service_model_reference/P052_prometheus_summary_结构体.md#a2fa33910c03339df68c33b54d5f267d7)
- [num_quantiles](../network_service_model_reference/P052_prometheus_summary_结构体.md#a7e2604e9c9891137e7232ccaa9014c59)
- [sum](../network_service_model_reference/P052_prometheus_summary_结构体.md#aead1e2754a146d36564472f8a1867da7)
- [count](../network_service_model_reference/P052_prometheus_summary_结构体.md#a6cd8daf6014b485ccbca0dd3194e5d87)
- [user_data](../network_service_model_reference/P052_prometheus_summary_结构体.md#ab9ba58c106f9dd73c425976b0680b785)
- [prometheus_summary_observe](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga7683de05e8b135161120ad5d3f2edc2c)
- [prometheus_summary_observe_set](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga98369eb2a7c8ce36f7570ed5b55410d8)
- [metric.h](https://docs.zephyrproject.org/latest/doxygen/html/metric_8h.html)
- [prometheus_summary_quantile::value](../network_service_model_reference/P053_prometheus_summary_quantile_结构体.md#a53fb78e35a0748f568d7bb15b083b037)
- [prometheus_summary_quantile::user_data](../network_service_model_reference/P053_prometheus_summary_quantile_结构体.md#a788d30204d7ce61940741cefd2c073f6)
- [prometheus_summary_quantile::quantile](../network_service_model_reference/P053_prometheus_summary_quantile_结构体.md#a811db0cddd6fd444a899be83e4116b92)
- [prometheus_summary::quantiles](../network_service_model_reference/P052_prometheus_summary_结构体.md#a2fa33910c03339df68c33b54d5f267d7)
- [prometheus_summary::count](../network_service_model_reference/P052_prometheus_summary_结构体.md#a6cd8daf6014b485ccbca0dd3194e5d87)
- [prometheus_summary::num_quantiles](../network_service_model_reference/P052_prometheus_summary_结构体.md#a7e2604e9c9891137e7232ccaa9014c59)
- [prometheus_summary::base](../network_service_model_reference/P052_prometheus_summary_结构体.md#aaef55d38ed7a9a8477d6e5ffeb748cbe)
- [prometheus_summary::user_data](../network_service_model_reference/P052_prometheus_summary_结构体.md#ab9ba58c106f9dd73c425976b0680b785)
- [prometheus_summary::sum](../network_service_model_reference/P052_prometheus_summary_结构体.md#aead1e2754a146d36564472f8a1867da7)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P845_error.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P847_sx126x.h_源码浏览.md)
