---
id: learning.zephyr-docs.api-source-reference.page-574
title: counter.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net_2prometheus_2counter_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第574章\_counter.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net_2prometheus_2counter_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/net_2prometheus_2counter_8h.html)。

## 574.1\_原始可见代码（Source Code）

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
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00060"></a>
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
<a id="l00074"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="foldopen00090"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="agroup__prometheus_html_ga8621228b7a66a6a42fb2cb838ec94dfe"></a>
<a id="agroup__prometheus_html_ga9b7461d625acc075c9511249c67741ab"></a>
<a id="agroup__prometheus_html_gad2220d089050bc5db1e5866429d515b3"></a>
<a id="ametric_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astructprometheus__counter_html"></a>
<a id="astructprometheus__counter_html_a048376a671e83df41034908b85e9e234"></a>
<a id="astructprometheus__counter_html_a28793edc31342bd6572493d7aa72eaca"></a>
<a id="astructprometheus__counter_html_a33714d75e20f8a69a7068c5c57fe3a37"></a>
<a id="astructprometheus__metric_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology
 * Copyright (c) 2024 Nordic Semiconductor
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_PROMETHEUS_COUNTER_H_
#define ZEPHYR_INCLUDE_NET_PROMETHEUS_COUNTER_H_


#include <stdint.h>

#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/prometheus/metric.h>

struct prometheus_counter {
        struct prometheus_metric base;
        uint64_t value;
        void *user_data;
};

#define PROMETHEUS_COUNTER_DEFINE(_name, _desc, _label, _collector, ...) \
        STRUCT_SECTION_ITERABLE(prometheus_counter, _name) = {          \
                .base.name = STRINGIFY(_name),                          \
                .base.type = PROMETHEUS_COUNTER,                        \
                .base.description = _desc,                              \
                .base.labels[0] = __DEBRACKET _label,                   \
                .base.num_labels = 1,                                   \
                .base.collector = _collector,                           \
                .value = 0ULL,                                          \
                .user_data = COND_CODE_0(                               \
                        NUM_VA_ARGS_LESS_1(LIST_DROP_EMPTY(__VA_ARGS__, _)), \
                        (NULL),                                         \
                        (GET_ARG_N(1, __VA_ARGS__))),                   \
        }

int prometheus_counter_add(struct prometheus_counter *counter, uint64_t value);

static inline int prometheus_counter_inc(struct prometheus_counter *counter)
{
        return prometheus_counter_add(counter, 1ULL);
}

int prometheus_counter_set(struct prometheus_counter *counter, uint64_t value);


#endif /* ZEPHYR_INCLUDE_NET_PROMETHEUS_COUNTER_H_ */
```

## 574.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Mustafa Abdullah Kus, Sparse Technology。

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 111 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_PROMETHEUS_COUNTER_H_`。

## 574.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/net_2prometheus_2counter_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/net/prometheus/metric.h](https://docs.zephyrproject.org/latest/doxygen/html/metric_8h.html)
- [prometheus_counter](../network_service_model_reference/P046_prometheus_counter_结构体.md)
- [prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)
- [base](../network_service_model_reference/P046_prometheus_counter_结构体.md#a33714d75e20f8a69a7068c5c57fe3a37)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [value](../network_service_model_reference/P046_prometheus_counter_结构体.md#a048376a671e83df41034908b85e9e234)
- [user_data](../network_service_model_reference/P046_prometheus_counter_结构体.md#a28793edc31342bd6572493d7aa72eaca)
- [prometheus_counter_add](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga9b7461d625acc075c9511249c67741ab)
- [prometheus_counter_inc](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gad2220d089050bc5db1e5866429d515b3)
- [prometheus_counter_set](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga8621228b7a66a6a42fb2cb838ec94dfe)
- [metric.h](https://docs.zephyrproject.org/latest/doxygen/html/metric_8h.html)
- [prometheus_counter::value](../network_service_model_reference/P046_prometheus_counter_结构体.md#a048376a671e83df41034908b85e9e234)
- [prometheus_counter::user_data](../network_service_model_reference/P046_prometheus_counter_结构体.md#a28793edc31342bd6572493d7aa72eaca)
- [prometheus_counter::base](../network_service_model_reference/P046_prometheus_counter_结构体.md#a33714d75e20f8a69a7068c5c57fe3a37)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P573_nct38xx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P575_net_l2.h_源码浏览.md)
