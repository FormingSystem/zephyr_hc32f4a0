---
id: learning.zephyr-docs.api-source-reference.page-283
title: gauge.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gauge_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第283章\_gauge.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gauge_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gauge_8h.html)。

## 283.1\_原始可见代码（Source Code）

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
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00059"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="agroup__prometheus_html_ga3ddc5efbdb9639486862f3df4b845fce"></a>
<a id="ametric_8h_html"></a>
<a id="astructprometheus__gauge_html"></a>
<a id="astructprometheus__gauge_html_a3c935bf93e23c10961e3160cce45e741"></a>
<a id="astructprometheus__gauge_html_a6ad64e6b7806165cb4d78ac29ff3ae27"></a>
<a id="astructprometheus__gauge_html_aabf12d85b93d419e19d9c300cb6313a7"></a>
<a id="astructprometheus__metric_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology
 * Copyright (c) 2024 Nordic Semiconductor
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_PROMETHEUS_GAUGE_H_
#define ZEPHYR_INCLUDE_NET_PROMETHEUS_GAUGE_H_


#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/prometheus/metric.h>

struct prometheus_gauge {
        struct prometheus_metric base;
        double value;
        void *user_data;
};

#define PROMETHEUS_GAUGE_DEFINE(_name, _desc, _label, _collector, ...)  \
        STRUCT_SECTION_ITERABLE(prometheus_gauge, _name) = {            \
                .base.name = STRINGIFY(_name),                          \
                .base.type = PROMETHEUS_GAUGE,                          \
                .base.description = _desc,                              \
                .base.labels[0] = __DEBRACKET _label,                   \
                .base.num_labels = 1,                                   \
                .base.collector = _collector,                           \
                .value = 0.0,                                           \
                .user_data = COND_CODE_0(                               \
                        NUM_VA_ARGS_LESS_1(LIST_DROP_EMPTY(__VA_ARGS__, _)), \
                        (NULL),                                         \
                        (GET_ARG_N(1, __VA_ARGS__))),                   \
        }

int prometheus_gauge_set(struct prometheus_gauge *gauge, double value);


#endif /* ZEPHYR_INCLUDE_NET_PROMETHEUS_GAUGE_H_ */
```

## 283.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Mustafa Abdullah Kus, Sparse Technology。

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 90 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_PROMETHEUS_GAUGE_H_`。

## 283.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gauge_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/net/prometheus/metric.h](https://docs.zephyrproject.org/latest/doxygen/html/metric_8h.html)
- [prometheus_gauge](../network_service_model_reference/P047_prometheus_gauge_结构体.md)
- [prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)
- [base](../network_service_model_reference/P047_prometheus_gauge_结构体.md#a6ad64e6b7806165cb4d78ac29ff3ae27)
- [value](../network_service_model_reference/P047_prometheus_gauge_结构体.md#aabf12d85b93d419e19d9c300cb6313a7)
- [user_data](../network_service_model_reference/P047_prometheus_gauge_结构体.md#a3c935bf93e23c10961e3160cce45e741)
- [prometheus_gauge_set](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga3ddc5efbdb9639486862f3df4b845fce)
- [metric.h](https://docs.zephyrproject.org/latest/doxygen/html/metric_8h.html)
- [prometheus_gauge::user_data](../network_service_model_reference/P047_prometheus_gauge_结构体.md#a3c935bf93e23c10961e3160cce45e741)
- [prometheus_gauge::base](../network_service_model_reference/P047_prometheus_gauge_结构体.md#a6ad64e6b7806165cb4d78ac29ff3ae27)
- [prometheus_gauge::value](../network_service_model_reference/P047_prometheus_gauge_结构体.md#aabf12d85b93d419e19d9c300cb6313a7)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P282_fwargs.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P284_gcov.h_源码浏览.md)
