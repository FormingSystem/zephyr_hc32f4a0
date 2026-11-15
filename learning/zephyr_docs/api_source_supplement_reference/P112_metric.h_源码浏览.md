---
id: learning.zephyr-docs.api-source-supplement-reference.page-112
title: metric.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/metric_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第112章\_metric.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/metric_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/metric_8h.html)。

## 112.1\_原始可见代码（Source Code）

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
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="agroup__prometheus_html_ga3499408dda4e539634c332c797651932"></a>
<a id="agroup__prometheus_html_ga5fd572e5351cda0855cb587e88c3a247"></a>
<a id="agroup__prometheus_html_gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf"></a>
<a id="agroup__prometheus_html_gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd"></a>
<a id="agroup__prometheus_html_gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074"></a>
<a id="agroup__prometheus_html_gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="alabel_8h_html"></a>
<a id="aslist_8h_html"></a>
<a id="astructprometheus__collector_html"></a>
<a id="astructprometheus__label_html"></a>
<a id="astructprometheus__metric_html"></a>
<a id="astructprometheus__metric_html_a05e19d7781f4724dfe7776e62cd69ca2"></a>
<a id="astructprometheus__metric_html_a1138f189a5bdd44639dace426ef8f55a"></a>
<a id="astructprometheus__metric_html_a198f0ddcf143d8728d914ee34eb8cb78"></a>
<a id="astructprometheus__metric_html_a5266bf5bd528cdd4c34ea56d7a96129d"></a>
<a id="astructprometheus__metric_html_a67e8d38a696f2b20a076b8da6b1250e3"></a>
<a id="astructprometheus__metric_html_a68b4a71af679bef383d635f1b0018dba"></a>
<a id="astructprometheus__metric_html_a9ceba3f813e1bcf36c333af975c7ac76"></a>
<a id="astructprometheus__metric_html_ae2db853cae2c49634fda25eb23b825da"></a>
<a id="astructprometheus__metric_html_af3ae0862633b2ce475f7c6851d13c3d1"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology
 * Copyright (c) 2024 Nordic Semiconductor
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_PROMETHEUS_METRIC_H_
#define ZEPHYR_INCLUDE_NET_PROMETHEUS_METRIC_H_


#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/slist.h>
#include <zephyr/net/prometheus/label.h>

enum prometheus_metric_type {
        PROMETHEUS_COUNTER = 0,
        PROMETHEUS_GAUGE,
        PROMETHEUS_SUMMARY,
        PROMETHEUS_HISTOGRAM,
};

struct prometheus_metric {
        sys_snode_t node;
        struct prometheus_collector *collector;
        void *metric;
        enum prometheus_metric_type type;
        const char *name;
        const char *description;
        struct prometheus_label labels[MAX_PROMETHEUS_LABELS_PER_METRIC];
        int num_labels;
        void *user_data;
        /* Add any other necessary fields */
};


#endif /* ZEPHYR_INCLUDE_NET_PROMETHEUS_METRIC_H_ */
```

## 112.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Mustafa Abdullah Kus, Sparse Technology。

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 69 行

添加其他必要字段。

### 注释 3：原第 76 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_PROMETHEUS_METRIC_H_`。

## 112.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/metric_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/net/prometheus/label.h](https://docs.zephyrproject.org/latest/doxygen/html/label_8h.html)
- [prometheus_metric_type](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga3499408dda4e539634c332c797651932)
- [PROMETHEUS_COUNTER](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b)
- [PROMETHEUS_GAUGE](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd)
- [PROMETHEUS_SUMMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074)
- [PROMETHEUS_HISTOGRAM](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf)
- [prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../network_service_model_reference/P051_prometheus_metric_结构体.md#a68b4a71af679bef383d635f1b0018dba)
- [prometheus_collector](../network_service_model_reference/P045_prometheus_collector_结构体.md)
- [collector](../network_service_model_reference/P051_prometheus_metric_结构体.md#a1138f189a5bdd44639dace426ef8f55a)
- [metric](../network_service_model_reference/P051_prometheus_metric_结构体.md#a67e8d38a696f2b20a076b8da6b1250e3)
- [type](../network_service_model_reference/P051_prometheus_metric_结构体.md#a05e19d7781f4724dfe7776e62cd69ca2)
- [name](../network_service_model_reference/P051_prometheus_metric_结构体.md#a5266bf5bd528cdd4c34ea56d7a96129d)
- [description](../network_service_model_reference/P051_prometheus_metric_结构体.md#a9ceba3f813e1bcf36c333af975c7ac76)
- [prometheus_label](../network_service_model_reference/P050_prometheus_label_结构体.md)
- [labels](../network_service_model_reference/P051_prometheus_metric_结构体.md#af3ae0862633b2ce475f7c6851d13c3d1)
- [MAX_PROMETHEUS_LABELS_PER_METRIC](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga5fd572e5351cda0855cb587e88c3a247)
- [num_labels](../network_service_model_reference/P051_prometheus_metric_结构体.md#a198f0ddcf143d8728d914ee34eb8cb78)
- [user_data](../network_service_model_reference/P051_prometheus_metric_结构体.md#ae2db853cae2c49634fda25eb23b825da)
- [label.h](https://docs.zephyrproject.org/latest/doxygen/html/label_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [prometheus_metric::type](../network_service_model_reference/P051_prometheus_metric_结构体.md#a05e19d7781f4724dfe7776e62cd69ca2)
- [prometheus_metric::collector](../network_service_model_reference/P051_prometheus_metric_结构体.md#a1138f189a5bdd44639dace426ef8f55a)
- [prometheus_metric::num_labels](../network_service_model_reference/P051_prometheus_metric_结构体.md#a198f0ddcf143d8728d914ee34eb8cb78)
- [prometheus_metric::name](../network_service_model_reference/P051_prometheus_metric_结构体.md#a5266bf5bd528cdd4c34ea56d7a96129d)
- [prometheus_metric::metric](../network_service_model_reference/P051_prometheus_metric_结构体.md#a67e8d38a696f2b20a076b8da6b1250e3)
- [prometheus_metric::node](../network_service_model_reference/P051_prometheus_metric_结构体.md#a68b4a71af679bef383d635f1b0018dba)
- [prometheus_metric::description](../network_service_model_reference/P051_prometheus_metric_结构体.md#a9ceba3f813e1bcf36c333af975c7ac76)
- [prometheus_metric::user_data](../network_service_model_reference/P051_prometheus_metric_结构体.md#ae2db853cae2c49634fda25eb23b825da)
- [prometheus_metric::labels](../network_service_model_reference/P051_prometheus_metric_结构体.md#af3ae0862633b2ce475f7c6851d13c3d1)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P111_method.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P113_smp.h_源码浏览.md)
