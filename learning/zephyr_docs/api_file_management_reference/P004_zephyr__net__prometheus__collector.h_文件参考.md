---
id: learning.zephyr-docs.api-file-management-reference.page-4
title: zephyr__net__prometheus__collector.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/collector_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_net\_\_prometheus\_\_collector.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/collector_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Prometheus采集器（Collector）的API。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/prometheus/metric.h>
#include <stddef.h>
```

查看此文件的源码。

Prometheus采集器（Collector）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_prometheus_5Fcollector"></a>

```c
struct prometheus_collector
```

相关声明：[prometheus_collector](../network_service_model_reference/P045_prometheus_collector_结构体.md)。

Prometheus采集器（Collector）的定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_gaab3a797c867c6492dedb2b51774a48e5"></a>

```c
#define PROMETHEUS_COLLECTOR_DEFINE(_name, ...)
```

相关声明：[PROMETHEUS_COLLECTOR_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gaab3a797c867c6492dedb2b51774a48e5)。

Prometheus 收集器（Collector）定义。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.3\_类型定义（Typedefs）

<a id="r_ga4e2541cb094915187157d44a29e2d6b5"></a>

```c
typedef int(* prometheus_scrape_cb_t) (struct prometheus_collector *collector, struct prometheus_metric *metric, void *user_data)
```

相关声明：[prometheus_scrape_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga4e2541cb094915187157d44a29e2d6b5)、[prometheus_collector](../network_service_model_reference/P045_prometheus_collector_结构体.md)、[prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)。

用于从收集器抓取特定指标（metric）的回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.4\_函数（Functions）

<a id="r_ga976b9e82d747570cde631b03ee805a26"></a>

```c
int prometheus_collector_register_metric (struct prometheus_collector *collector, struct prometheus_metric *metric)
```

相关声明：[prometheus_collector_register_metric](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga976b9e82d747570cde631b03ee805a26)、[prometheus_collector](../network_service_model_reference/P045_prometheus_collector_结构体.md)、[prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)。

向 Prometheus 收集器注册一个指标。

<a id="r_ga757252a9157538870b1360924b16d0e0"></a>

```c
const void * prometheus_collector_get_metric (struct prometheus_collector *collector, const char *name)
```

相关声明：[prometheus_collector_get_metric](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga757252a9157538870b1360924b16d0e0)、[prometheus_collector](../network_service_model_reference/P045_prometheus_collector_结构体.md)。

从 Prometheus 收集器获取一个指标。

<a id="r_ga1bbdd8d5447144b21d3cda1ddac38ff0"></a>

```c
int prometheus_collector_walk_metrics (struct prometheus_collector_walk_context *ctx, uint8_t *buffer, size_t buffer_size)
```

相关声明：[prometheus_collector_walk_metrics](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga1bbdd8d5447144b21d3cda1ddac38ff0)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

遍历 Prometheus 收集器的所有指标，并将其格式化到缓冲区。

<a id="r_ga1c70215409029bbe163bdfdb03bfba43"></a>

```c
static int prometheus_collector_walk_init (struct prometheus_collector_walk_context *ctx, struct prometheus_collector *collector)
```

相关声明：[prometheus_collector_walk_init](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga1c70215409029bbe163bdfdb03bfba43)、[prometheus_collector](../network_service_model_reference/P045_prometheus_collector_结构体.md)。

初始化遍历器上下文（walker context），用于遍历全部指标。


## 4.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/net/prometheus/metric.h](../api_source_supplement_reference/P112_metric.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P109_collector.h_源码浏览.md)
- [prometheus_collector](../network_service_model_reference/P045_prometheus_collector_结构体.md)
- [PROMETHEUS_COLLECTOR_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gaab3a797c867c6492dedb2b51774a48e5)
- [prometheus_scrape_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga4e2541cb094915187157d44a29e2d6b5)
- [prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)
- [prometheus_collector_register_metric](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga976b9e82d747570cde631b03ee805a26)
- [prometheus_collector_get_metric](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga757252a9157538870b1360924b16d0e0)
- [prometheus_collector_walk_metrics](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga1bbdd8d5447144b21d3cda1ddac38ff0)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [prometheus_collector_walk_init](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga1c70215409029bbe163bdfdb03bfba43)

<a id="header-details"></a>

---

[上一章](P003_zephyr__mgmt__mcumgr__mgmt__callbacks.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__drivers__display__color_dither.h_文件参考.md)
