---
id: learning.zephyr-docs.api-audio-metrics-topic-reference.page-6
title: Prometheus API API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_Prometheus API API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

自（Since）4.0 起提供，版本（Version）0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_prometheus_5Fcollector"></a>

```c
struct prometheus_collector
```

相关声明：[prometheus_collector](../network_service_model_reference/P045_prometheus_collector_结构体.md)。

Prometheus采集器（Collector）的定义。

<a id="r_prometheus_5Fcounter"></a>

```c
struct prometheus_counter
```

相关声明：[prometheus_counter](../network_service_model_reference/P046_prometheus_counter_结构体.md)。

用于表示Prometheus计数器指标（Counter Metric）的类型。

<a id="r_prometheus_5Fgauge"></a>

```c
struct prometheus_gauge
```

相关声明：[prometheus_gauge](../network_service_model_reference/P047_prometheus_gauge_结构体.md)。

用于表示Prometheus仪表指标（Gauge Metric）的类型。

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

<a id="r_prometheus_5Flabel"></a>

```c
struct prometheus_label
```

相关声明：[prometheus_label](../network_service_model_reference/P050_prometheus_label_结构体.md)。

Prometheus标签（Label）的定义。

<a id="r_prometheus_5Fmetric"></a>

```c
struct prometheus_metric
```

相关声明：[prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)。

用于表示Prometheus指标基类（Metric Base）的类型。

<a id="r_prometheus_5Fsummary_5Fquantile"></a>

```c
struct prometheus_summary_quantile
```

相关声明：[prometheus_summary_quantile](../network_service_model_reference/P053_prometheus_summary_quantile_结构体.md)。

Prometheus摘要分位数（Summary Quantile）的定义。

<a id="r_prometheus_5Fsummary"></a>

```c
struct prometheus_summary
```

相关声明：[prometheus_summary](../network_service_model_reference/P052_prometheus_summary_结构体.md)。

用于表示Prometheus摘要指标（Summary Metric）的类型。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_gaab3a797c867c6492dedb2b51774a48e5"></a>

```c
#define PROMETHEUS_COLLECTOR_DEFINE(_name, ...)
```

相关声明：[PROMETHEUS_COLLECTOR_DEFINE](#gaab3a797c867c6492dedb2b51774a48e5)。

Prometheus 收集器（Collector）定义。

<a id="r_gadbfcfc7904d6388d2c9dc81d4803264c"></a>

```c
#define PROMETHEUS_COUNTER_DEFINE(_name, _desc, _label, _collector, ...)
```

相关声明：[PROMETHEUS_COUNTER_DEFINE](#gadbfcfc7904d6388d2c9dc81d4803264c)。

Prometheus 计数器（Counter）的定义。

<a id="r_ga362e708722846a3ca9299e8994becd13"></a>

```c
#define PROMETHEUS_GAUGE_DEFINE(_name, _desc, _label, _collector, ...)
```

相关声明：[PROMETHEUS_GAUGE_DEFINE](#ga362e708722846a3ca9299e8994becd13)。

Prometheus 仪表（Gauge）的定义。

<a id="r_gaf2ddb4e016104faaf543d9a028756a0c"></a>

```c
#define PROMETHEUS_HISTOGRAM_DEFINE(_name, _desc, _label, _collector, ...)
```

相关声明：[PROMETHEUS_HISTOGRAM_DEFINE](#gaf2ddb4e016104faaf543d9a028756a0c)。

Prometheus 直方图（Histogram）的定义。

<a id="r_ga5fd572e5351cda0855cb587e88c3a247"></a>

```c
#define MAX_PROMETHEUS_LABELS_PER_METRIC 1
```

相关声明：[MAX_PROMETHEUS_LABELS_PER_METRIC](#ga5fd572e5351cda0855cb587e88c3a247)。

<a id="r_gaa3c043be86118ff9e8122136edc89cc4"></a>

```c
#define PROMETHEUS_SUMMARY_DEFINE(_name, _desc, _label, _collector, ...)
```

相关声明：[PROMETHEUS_SUMMARY_DEFINE](#gaa3c043be86118ff9e8122136edc89cc4)。

Prometheus 摘要指标（Summary）的定义。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.3\_类型定义（Typedefs）

<a id="r_ga4e2541cb094915187157d44a29e2d6b5"></a>

```c
typedef int(* prometheus_scrape_cb_t) (struct prometheus_collector *collector, struct prometheus_metric *metric, void *user_data)
```

相关声明：[prometheus_scrape_cb_t](#ga4e2541cb094915187157d44a29e2d6b5)、[prometheus_collector](../network_service_model_reference/P045_prometheus_collector_结构体.md)、[prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)。

用于从收集器抓取特定指标（metric）的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.4\_枚举（Enumerations）

<a id="r_ga3499408dda4e539634c332c797651932"></a>

```c
enum prometheus_metric_type { PROMETHEUS_COUNTER = 0 , PROMETHEUS_GAUGE , PROMETHEUS_SUMMARY , PROMETHEUS_HISTOGRAM }
```

相关声明：[prometheus_metric_type](#ga3499408dda4e539634c332c797651932)、[PROMETHEUS_COUNTER](#gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b)、[PROMETHEUS_GAUGE](#gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd)、[PROMETHEUS_SUMMARY](#gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074)、[PROMETHEUS_HISTOGRAM](#gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf)。

Prometheus 指标类型（Metric Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.5\_函数（Functions）

<a id="r_ga976b9e82d747570cde631b03ee805a26"></a>

```c
int prometheus_collector_register_metric (struct prometheus_collector *collector, struct prometheus_metric *metric)
```

相关声明：[prometheus_collector_register_metric](#ga976b9e82d747570cde631b03ee805a26)、[prometheus_collector](../network_service_model_reference/P045_prometheus_collector_结构体.md)、[prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)。

向 Prometheus 收集器注册一个指标。

<a id="r_ga757252a9157538870b1360924b16d0e0"></a>

```c
const void * prometheus_collector_get_metric (struct prometheus_collector *collector, const char *name)
```

相关声明：[prometheus_collector_get_metric](#ga757252a9157538870b1360924b16d0e0)、[prometheus_collector](../network_service_model_reference/P045_prometheus_collector_结构体.md)。

从 Prometheus 收集器获取一个指标。

<a id="r_ga1bbdd8d5447144b21d3cda1ddac38ff0"></a>

```c
int prometheus_collector_walk_metrics (struct prometheus_collector_walk_context *ctx, uint8_t *buffer, size_t buffer_size)
```

相关声明：[prometheus_collector_walk_metrics](#ga1bbdd8d5447144b21d3cda1ddac38ff0)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

遍历 Prometheus 收集器的所有指标，并将其格式化到缓冲区。

<a id="r_ga1c70215409029bbe163bdfdb03bfba43"></a>

```c
static int prometheus_collector_walk_init (struct prometheus_collector_walk_context *ctx, struct prometheus_collector *collector)
```

相关声明：[prometheus_collector_walk_init](#ga1c70215409029bbe163bdfdb03bfba43)、[prometheus_collector](../network_service_model_reference/P045_prometheus_collector_结构体.md)。

初始化遍历器上下文（walker context），用于遍历全部指标。

<a id="r_ga9b7461d625acc075c9511249c67741ab"></a>

```c
int prometheus_counter_add (struct prometheus_counter *counter, uint64_t value)
```

相关声明：[prometheus_counter_add](#ga9b7461d625acc075c9511249c67741ab)、[prometheus_counter](../network_service_model_reference/P046_prometheus_counter_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

增加 Prometheus 计数器指标（Counter Metric）的值：将指定计数器增加任意给定数量。

<a id="r_gad2220d089050bc5db1e5866429d515b3"></a>

```c
static int prometheus_counter_inc (struct prometheus_counter *counter)
```

相关声明：[prometheus_counter_inc](#gad2220d089050bc5db1e5866429d515b3)、[prometheus_counter](../network_service_model_reference/P046_prometheus_counter_结构体.md)。

增加 Prometheus 计数器指标（Counter Metric）的值：将指定计数器增加 1。

<a id="r_ga8621228b7a66a6a42fb2cb838ec94dfe"></a>

```c
int prometheus_counter_set (struct prometheus_counter *counter, uint64_t value)
```

相关声明：[prometheus_counter_set](#ga8621228b7a66a6a42fb2cb838ec94dfe)、[prometheus_counter](../network_service_model_reference/P046_prometheus_counter_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

将计数器值（Counter Value）设置为指定值。

<a id="r_ga7d219be7f2b3b49a2f936489bdf68fe8"></a>

```c
int prometheus_format_exposition (struct prometheus_collector *collector, char *buffer, size_t buffer_size)
```

相关声明：[prometheus_format_exposition](#ga7d219be7f2b3b49a2f936489bdf68fe8)、[prometheus_collector](../network_service_model_reference/P045_prometheus_collector_结构体.md)。

格式化 Prometheus 暴露数据（Exposition Data）。

<a id="r_ga2240cf4f807fe7180f21c8fab3fbbd66"></a>

```c
int prometheus_format_one_metric (struct prometheus_metric *metric, char *buffer, size_t buffer_size, int *written)
```

相关声明：[prometheus_format_one_metric](#ga2240cf4f807fe7180f21c8fab3fbbd66)、[prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)。

格式化单个 Prometheus 指标（Metric）的暴露数据（Exposition Data）。

<a id="r_ga3ddc5efbdb9639486862f3df4b845fce"></a>

```c
int prometheus_gauge_set (struct prometheus_gauge *gauge, double value)
```

相关声明：[prometheus_gauge_set](#ga3ddc5efbdb9639486862f3df4b845fce)、[prometheus_gauge](../network_service_model_reference/P047_prometheus_gauge_结构体.md)。

设置 Prometheus 仪表指标（Gauge Metric）的值。

<a id="r_gaf0f24e64833302b74397654001ca5026"></a>

```c
int prometheus_histogram_observe (struct prometheus_histogram *histogram, double value)
```

相关声明：[prometheus_histogram_observe](#gaf0f24e64833302b74397654001ca5026)、[prometheus_histogram](../network_service_model_reference/P048_prometheus_histogram_结构体.md)。

在 Prometheus 直方图指标（Histogram Metric）中记录一个观测值（Observe a Value）。

<a id="r_ga7683de05e8b135161120ad5d3f2edc2c"></a>

```c
int prometheus_summary_observe (struct prometheus_summary *summary, double value)
```

相关声明：[prometheus_summary_observe](#ga7683de05e8b135161120ad5d3f2edc2c)、[prometheus_summary](../network_service_model_reference/P052_prometheus_summary_结构体.md)。

在 Prometheus 摘要指标（Summary Metric）中记录一个观测值（Observe a Value）。

<a id="r_ga98369eb2a7c8ce36f7570ed5b55410d8"></a>

```c
int prometheus_summary_observe_set (struct prometheus_summary *summary, double value, unsigned long count)
```

相关声明：[prometheus_summary_observe_set](#ga98369eb2a7c8ce36f7570ed5b55410d8)、[prometheus_summary](../network_service_model_reference/P052_prometheus_summary_结构体.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

将摘要值（Summary Value）设置为指定值。

## 6.6\_详细说明（Detailed Documentation）

<a id="ga5fd572e5351cda0855cb587e88c3a247"></a>

### `MAX_PROMETHEUS_LABELS_PER_METRIC`

```c
#define MAX_PROMETHEUS_LABELS_PER_METRIC 1
```

```c
#include <zephyr/net/prometheus/label.h>
```

<a id="gaab3a797c867c6492dedb2b51774a48e5"></a>

### `PROMETHEUS_COLLECTOR_DEFINE`

```c
#define PROMETHEUS_COLLECTOR_DEFINE ( _name, ... )
```

```c
#include <zephyr/net/prometheus/collector.h>
```

展开值（Value）：

```c
STRUCT_SECTION_ITERABLE(prometheus_collector, _name) = {        \
        .name = STRINGIFY(_name),                               \
        .metrics = SYS_SLIST_STATIC_INIT(&_name.metrics),       \
        .lock = Z_MUTEX_INITIALIZER(_name.lock),                \
        .user_cb = COND_CODE_0(                                 \
                NUM_VA_ARGS_LESS_1(                             \
                        LIST_DROP_EMPTY(__VA_ARGS__, _)),       \
                (NULL),                                         \
                (GET_ARG_N(1, __VA_ARGS__))),                   \
        .user_data = COND_CODE_0(                               \
                NUM_VA_ARGS_LESS_1(__VA_ARGS__), (NULL),        \
                (GET_ARG_N(1,                                   \
                           GET_ARGS_LESS_N(1, __VA_ARGS__)))),  \
}
```

Prometheus 收集器（Collector）定义。

此宏定义一个采集器（Collector）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 采集器名称（Collector Name）。 |
| `...` | 可选的用户回调函数（User Callback）。设置后，在抓取（Scrape）采集器时调用。函数类型应为 `prometheus_scrape_cb_t`。还可提供传给用户回调函数的可选用户数据。 |

<a id="gadbfcfc7904d6388d2c9dc81d4803264c"></a>

### `PROMETHEUS_COUNTER_DEFINE`

```c
#define PROMETHEUS_COUNTER_DEFINE ( _name, _desc, _label, _collector, ... )
```

```c
#include <zephyr/net/prometheus/counter.h>
```

展开值（Value）：

```c
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
```

Prometheus 计数器（Counter）的定义。

此宏定义一个计数器指标（Counter Metric）。若要将计数器设为静态对象，请在 `PROMETHEUS_COUNTER_DEFINE` 前添加 `static` 关键字。

使用示例：

原始示例（Example）：

```c
PROMETHEUS_COUNTER_DEFINE(http_request_counter, "HTTP request counter",
                          ({ .key = "http_request", .value = "request_count" }),
                          NULL);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 计数器指标名称（Counter Metric Name）。 |
| `_desc` | 计数器说明（Counter Description）。 |
| `_label` | 指标标签（Metric Label）。可在运行时添加其他标签。 |
| `_collector` | 此指标归属的采集器（Collector）。尚未确定时可设为 `NULL`。 |
| `...` | 此指标实例特有的可选用户数据（User Data）。 |

<a id="ga362e708722846a3ca9299e8994becd13"></a>

### `PROMETHEUS_GAUGE_DEFINE`

```c
#define PROMETHEUS_GAUGE_DEFINE ( _name, _desc, _label, _collector, ... )
```

```c
#include <zephyr/net/prometheus/gauge.h>
```

展开值（Value）：

```c
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
```

Prometheus 仪表（Gauge）的定义。

此宏定义一个仪表指标（Gauge Metric）。若要将仪表设为静态对象，请在 `PROMETHEUS_GAUGE_DEFINE` 前添加 `static` 关键字。

使用示例：

原始示例（Example）：

```c
PROMETHEUS_GAUGE_DEFINE(http_request_gauge, "HTTP request gauge",
                        ({ .key = "http_request", .value = "request_count" }),
                        NULL);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 仪表指标名称（Gauge Metric Name）。 |
| `_desc` | 仪表说明（Gauge Description）。 |
| `_label` | 指标标签（Metric Label）。可在运行时添加其他标签。 |
| `_collector` | 此指标归属的采集器（Collector）。尚未确定时可设为 `NULL`。 |
| `...` | 此指标实例特有的可选用户数据（User Data）。 |

<a id="gaf2ddb4e016104faaf543d9a028756a0c"></a>

### `PROMETHEUS_HISTOGRAM_DEFINE`

```c
#define PROMETHEUS_HISTOGRAM_DEFINE ( _name, _desc, _label, _collector, ... )
```

```c
#include <zephyr/net/prometheus/histogram.h>
```

展开值（Value）：

```c
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
```

Prometheus 直方图（Histogram）的定义。

此宏定义一个直方图指标（Histogram Metric）。若要将直方图设为静态对象，请在 `PROMETHEUS_HISTOGRAM_DEFINE` 前添加 `static` 关键字。

使用示例：

原始示例（Example）：

```c
PROMETHEUS_HISTOGRAM_DEFINE(http_request_histogram, "HTTP request histogram",
                        ({ .key = "request_latency", .value = "request_latency_seconds" }),
                        NULL);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 直方图指标名称（Histogram Metric Name）。 |
| `_desc` | 直方图说明（Histogram Description）。 |
| `_label` | 指标标签（Metric Label）。可在运行时添加其他标签。 |
| `_collector` | 此指标归属的采集器（Collector）。尚未确定时可设为 `NULL`。 |
| `...` | 此指标实例特有的可选用户数据（User Data）。 |

<a id="gaa3c043be86118ff9e8122136edc89cc4"></a>

### `PROMETHEUS_SUMMARY_DEFINE`

```c
#define PROMETHEUS_SUMMARY_DEFINE ( _name, _desc, _label, _collector, ... )
```

```c
#include <zephyr/net/prometheus/summary.h>
```

展开值（Value）：

```c
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
```

Prometheus 摘要指标（Summary）的定义。

此宏定义一个摘要指标（Summary Metric）。若要将摘要设为静态对象，请在 `PROMETHEUS_SUMMARY_DEFINE` 前添加 `static` 关键字。

使用示例：

原始示例（Example）：

```c
PROMETHEUS_SUMMARY_DEFINE(http_request_summary, "HTTP request summary",
                          ({ .key = "request_latency",
                             .value = "request_latency_seconds" }), NULL);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 摘要指标名称（Summary Metric Name）。 |
| `_desc` | 摘要说明（Summary Description）。 |
| `_label` | 指标标签（Metric Label）。可在运行时添加其他标签。 |
| `_collector` | 此指标归属的采集器（Collector）。尚未确定时可设为 `NULL`。 |
| `...` | 此指标实例特有的可选用户数据（User Data）。 |

<a id="ga4e2541cb094915187157d44a29e2d6b5"></a>

### `prometheus_scrape_cb_t`

```c
typedef int(* prometheus_scrape_cb_t) (struct prometheus_collector *collector, struct prometheus_metric *metric, void *user_data)
```

```c
#include <zephyr/net/prometheus/collector.h>
```

用于从收集器抓取特定指标（metric）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `collector` | 指向要抓取（Scrape）的采集器（Collector）的有效指针。 |
| `metric` | 指向要抓取（Scrape）的指标（Metric）的有效指针。 |
| `user_data` | 指向用户数据（User Data）的有效指针，或 `NULL`。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，否则为负错误码。

<a id="ga3499408dda4e539634c332c797651932"></a>

### `prometheus_metric_type`

```c
enum prometheus_metric_type
```

```c
#include <zephyr/net/prometheus/metric.h>
```

Prometheus 指标类型（Metric Types）。

- 参考资料（References）。
- 参见 https://prometheus.io/docs/concepts/metric_types 。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `PROMETHEUS_COUNTER` | Prometheus 计数器（Counter）。 |
| `PROMETHEUS_GAUGE` | Prometheus 仪表（Gauge）。 |
| `PROMETHEUS_SUMMARY` | Prometheus 摘要（Summary）。 |
| `PROMETHEUS_HISTOGRAM` | Prometheus 直方图（Histogram）。 |

<a id="ga757252a9157538870b1360924b16d0e0"></a>

### `prometheus_collector_get_metric()`

```c
const void * prometheus_collector_get_metric ( struct prometheus_collector * collector, const char * name )
```

```c
#include <zephyr/net/prometheus/collector.h>
```

从 Prometheus 收集器获取一个指标。

从给定采集器（Collector）中检索指定名称的指标（Metric）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `collector` | 指向要从中检索指标的采集器（Collector）的指针。 |
| `name` | 要检索的指标名称（Metric Name）。 |

**返回（Returns）**：返回值（Returns）：指向检索到的指标的指针；未找到时为 `NULL`。

<a id="ga976b9e82d747570cde631b03ee805a26"></a>

### `prometheus_collector_register_metric()`

```c
int prometheus_collector_register_metric ( struct prometheus_collector * collector, struct prometheus_metric * metric )
```

```c
#include <zephyr/net/prometheus/collector.h>
```

向 Prometheus 收集器注册一个指标。

将指定指标（Metric）注册到给定采集器（Collector）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `collector` | 指向要向其注册指标的采集器（Collector）的指针。 |
| `metric` | 指向要注册的指标（Metric）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数无效（Invalid Arguments）。 |
| `-ENOMEM` | 内存不足，无法注册该指标（Metric）。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，否则为负错误码。

<a id="ga1c70215409029bbe163bdfdb03bfba43"></a>

### `prometheus_collector_walk_init()`

```c
int prometheus_collector_walk_init ( struct prometheus_collector_walk_context * ctx, struct prometheus_collector * collector )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/prometheus/collector.h>
```

初始化遍历器上下文（walker context），用于遍历全部指标。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 指向遍历器上下文（Walker Context）的指针。 |
| `collector` | 指向要遍历的采集器（Collector）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，否则为负错误码。

<a id="ga1bbdd8d5447144b21d3cda1ddac38ff0"></a>

### `prometheus_collector_walk_metrics()`

```c
int prometheus_collector_walk_metrics ( struct prometheus_collector_walk_context * ctx, uint8_t * buffer, size_t buffer_size )
```

```c
#include <zephyr/net/prometheus/collector.h>
```

遍历 Prometheus 收集器的所有指标，并将其格式化到缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 指向遍历器上下文（Walker Context）的指针。 |
| `buffer` | 指向用于存储格式化指标（Formatted Metrics）的缓冲区的指针。 |
| `buffer_size` | 缓冲区大小。 |

**返回（Returns）**：返回值（Returns）：成功且遍历完所有指标时为 0；需要再次调用此函数时为 `-EAGAIN`；其他负错误码表示发生错误。

<a id="ga9b7461d625acc075c9511249c67741ab"></a>

### `prometheus_counter_add()`

```c
int prometheus_counter_add ( struct prometheus_counter * counter, uint64_t value )
```

```c
#include <zephyr/net/prometheus/counter.h>
```

增加 Prometheus 计数器指标（Counter Metric）的值：将指定计数器增加任意给定数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `counter` | 指向要递增的计数器指标（Counter Metric）的指针。 |
| `value` | 计数器要增加的数值。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，出错时为负 `errno`。

<a id="gad2220d089050bc5db1e5866429d515b3"></a>

### `prometheus_counter_inc()`

```c
int prometheus_counter_inc ( struct prometheus_counter * counter)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/prometheus/counter.h>
```

增加 Prometheus 计数器指标（Counter Metric）的值：将指定计数器增加 1。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `counter` | 指向要递增的计数器指标（Counter Metric）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，出错时为负 `errno`。

<a id="ga8621228b7a66a6a42fb2cb838ec94dfe"></a>

### `prometheus_counter_set()`

```c
int prometheus_counter_set ( struct prometheus_counter * counter, uint64_t value )
```

```c
#include <zephyr/net/prometheus/counter.h>
```

将计数器值（Counter Value）设置为指定值。

新值必须大于当前值。如果不能逐次向计数器添加增量，而需要定期更新计数器值，可使用此函数。它将新值与旧值之间的差值加到计数器中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `counter` | 指向要递增的计数器指标（Counter Metric）的指针。 |
| `value` | 计数器（Counter）的新值。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，出错时为负 `errno`。

<a id="ga7d219be7f2b3b49a2f936489bdf68fe8"></a>

### `prometheus_format_exposition()`

```c
int prometheus_format_exposition ( struct prometheus_collector * collector, char * buffer, size_t buffer_size )
```

```c
#include <zephyr/net/prometheus/formatter.h>
```

格式化 Prometheus 暴露数据（Exposition Data）。

将指定采集器（Collector）收集的公开数据（Exposition Data）格式化到提供的缓冲区中。函数按 Prometheus 文本格式（Text-Based Format）格式化指标数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `collector` | 指向包含待格式化数据的采集器（Collector）的指针。 |
| `buffer` | 指向用于存储格式化公开数据（Exposition Data）的缓冲区的指针。 |
| `buffer_size` | 缓冲区大小。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，出错时为负 `errno`。

<a id="ga2240cf4f807fe7180f21c8fab3fbbd66"></a>

### `prometheus_format_one_metric()`

```c
int prometheus_format_one_metric ( struct prometheus_metric * metric, char * buffer, size_t buffer_size, int * written )
```

```c
#include <zephyr/net/prometheus/formatter.h>
```

格式化单个 Prometheus 指标（Metric）的暴露数据（Exposition Data）。

将某个指定指标（Metric）的公开数据（Exposition Data）格式化到提供的缓冲区中。函数按 Prometheus 文本格式（Text-Based Format）格式化指标数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `metric` | 指向包含待格式化数据的指标（Metric）的指针。 |
| `buffer` | 指向用于存储格式化公开数据（Exposition Data）的缓冲区的指针。 |
| `buffer_size` | 缓冲区大小。 |
| `written` | 已写入缓冲区的字节数。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，出错时为负 `errno`。

<a id="ga3ddc5efbdb9639486862f3df4b845fce"></a>

### `prometheus_gauge_set()`

```c
int prometheus_gauge_set ( struct prometheus_gauge * gauge, double value )
```

```c
#include <zephyr/net/prometheus/gauge.h>
```

设置 Prometheus 仪表指标（Gauge Metric）的值。

将指定仪表指标（Gauge Metric）的值设为给定值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `gauge` | 指向要设置的仪表指标（Gauge Metric）的指针。 |
| `value` | 要给仪表指标（Gauge Metric）设置的值。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，数值为负时为 `-EINVAL`。

<a id="gaf0f24e64833302b74397654001ca5026"></a>

### `prometheus_histogram_observe()`

```c
int prometheus_histogram_observe ( struct prometheus_histogram * histogram, double value )
```

```c
#include <zephyr/net/prometheus/histogram.h>
```

在 Prometheus 直方图指标（Histogram Metric）中记录一个观测值（Observe a Value）。

在给定直方图指标（Histogram Metric）中记录指定的观测值（Observation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `histogram` | 指向要记录观测值的直方图指标（Histogram Metric）的指针。 |
| `value` | 要在直方图指标（Histogram Metric）中记录的观测值。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，数值为负时为 `-EINVAL`。

<a id="ga7683de05e8b135161120ad5d3f2edc2c"></a>

### `prometheus_summary_observe()`

```c
int prometheus_summary_observe ( struct prometheus_summary * summary, double value )
```

```c
#include <zephyr/net/prometheus/summary.h>
```

在 Prometheus 摘要指标（Summary Metric）中记录一个观测值（Observe a Value）。

在给定摘要指标（Summary Metric）中记录指定的观测值（Observation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `summary` | 指向要记录观测值的摘要指标（Summary Metric）的指针。 |
| `value` | 要在摘要指标（Summary Metric）中记录的观测值。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，数值为负时为 `-EINVAL`。

<a id="ga98369eb2a7c8ce36f7570ed5b55410d8"></a>

### `prometheus_summary_observe_set()`

```c
int prometheus_summary_observe_set ( struct prometheus_summary * summary, double value, unsigned long count )
```

```c
#include <zephyr/net/prometheus/summary.h>
```

将摘要值（Summary Value）设置为指定值。

新值必须大于当前值。如果不能逐次向摘要（Summary）添加增量，而需要定期更新计数器值，可使用此函数。它将新值与旧值之间的差值加到摘要字段中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `summary` | 指向要递增的摘要指标（Summary Metric）的指针。 |
| `value` | 摘要（Summary）的新值。 |
| `count` | 摘要（Summary）的新计数器值。 |

**返回（Returns）**：返回值（Returns）：成功时为 0，出错时为负 `errno`。


## 6.7\_原页交叉引用（Cross References）

- [prometheus_collector](../network_service_model_reference/P045_prometheus_collector_结构体.md)
- [prometheus_counter](../network_service_model_reference/P046_prometheus_counter_结构体.md)
- [prometheus_gauge](../network_service_model_reference/P047_prometheus_gauge_结构体.md)
- [prometheus_histogram_bucket](../network_service_model_reference/P049_prometheus_histogram_bucket_结构体.md)
- [prometheus_histogram](../network_service_model_reference/P048_prometheus_histogram_结构体.md)
- [prometheus_label](../network_service_model_reference/P050_prometheus_label_结构体.md)
- [prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)
- [prometheus_summary_quantile](../network_service_model_reference/P053_prometheus_summary_quantile_结构体.md)
- [prometheus_summary](../network_service_model_reference/P052_prometheus_summary_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [zephyr/net/prometheus/label.h](../api_file_reference/P185_zephyr__net__prometheus__label.h_文件参考.md)
- [zephyr/net/prometheus/collector.h](../api_file_management_reference/P004_zephyr__net__prometheus__collector.h_文件参考.md)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)
- [SYS_SLIST_STATIC_INIT](../slist_reference/P001_单向链表公共接口.md#ga7f4710125f45643b7acdaa58dbfff225)
- [COND_CODE_0](../util_reference/P001_通用工具公共接口.md#ga5483ea38af79bc6c4509936288705377)
- [NUM_VA_ARGS_LESS_1](../util_reference/P001_通用工具公共接口.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)
- [LIST_DROP_EMPTY](../util_reference/P001_通用工具公共接口.md#gab9762d5128988f7f4f5d51213ea52025)
- [GET_ARG_N](../util_reference/P001_通用工具公共接口.md#gabbe04a4d59a495b2b86196304b937ec6)
- [GET_ARGS_LESS_N](../util_reference/P001_通用工具公共接口.md#ga01e1dc9b92e5be6895528d1da5f0c88b)
- [zephyr/net/prometheus/counter.h](../api_file_service_reference/P028_zephyr__net__prometheus__counter.h_文件参考.md)
- [zephyr/net/prometheus/gauge.h](../api_file_configuration_reference/P031_zephyr__net__prometheus__gauge.h_文件参考.md)
- [zephyr/net/prometheus/histogram.h](../api_file_configuration_reference/P037_zephyr__net__prometheus__histogram.h_文件参考.md)
- [zephyr/net/prometheus/summary.h](../api_file_runtime_reference/P068_zephyr__net__prometheus__summary.h_文件参考.md)
- [zephyr/net/prometheus/metric.h](../api_file_supplement_reference/P066_zephyr__net__prometheus__metric.h_文件参考.md)
- [https://prometheus.io/docs/concepts/metric_types](https://prometheus.io/docs/concepts/metric_types)
- [zephyr/net/prometheus/formatter.h](../api_file_configuration_reference/P029_zephyr__net__prometheus__formatter.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="agroup__single-linked-list__apis_html_ga7f4710125f45643b7acdaa58dbfff225"></a>
<a id="agroup__sys-util_html_ga01e1dc9b92e5be6895528d1da5f0c88b"></a>
<a id="agroup__sys-util_html_ga5483ea38af79bc6c4509936288705377"></a>
<a id="agroup__sys-util_html_ga8a0e9835e0a8f864ffc2359b9c419cc2"></a>
<a id="agroup__sys-util_html_gab9762d5128988f7f4f5d51213ea52025"></a>
<a id="agroup__sys-util_html_gabbe04a4d59a495b2b86196304b937ec6"></a>
<a id="astructprometheus__collector_html"></a>
<a id="agroup__prometheus_html_gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b"></a>
<a id="astructprometheus__counter_html"></a>
<a id="agroup__prometheus_html_gadbfcfc7904d6388d2c9dc81d4803264c"></a>
<a id="agroup__prometheus_html_gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd"></a>
<a id="astructprometheus__gauge_html"></a>
<a id="agroup__prometheus_html_ga362e708722846a3ca9299e8994becd13"></a>
<a id="agroup__prometheus_html_gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf"></a>
<a id="astructprometheus__histogram_html"></a>
<a id="agroup__prometheus_html_gaf2ddb4e016104faaf543d9a028756a0c"></a>
<a id="agroup__prometheus_html_gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074"></a>
<a id="astructprometheus__summary_html"></a>
<a id="agroup__prometheus_html_gaa3c043be86118ff9e8122136edc89cc4"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b"></a>
<a id="gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd"></a>
<a id="gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074"></a>
<a id="gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_网络管理（Network Management）.md) · [返回大纲](大纲.md)
