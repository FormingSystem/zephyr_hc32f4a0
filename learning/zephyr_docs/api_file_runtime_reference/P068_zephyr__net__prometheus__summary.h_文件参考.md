---
id: learning.zephyr-docs.api-file-runtime-reference.page-68
title: zephyr__net__prometheus__summary.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/summary_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_zephyr\_\_net\_\_prometheus\_\_summary.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/summary_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Prometheus摘要（Summary）的API。

<a id="details"></a>

```c
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/prometheus/metric.h>
#include <stddef.h>
```

查看此文件的源码。

Prometheus摘要（Summary）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 68.1\_数据结构（Data Structures）

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

## 68.2\_宏定义（Macros）

<a id="r_gaa3c043be86118ff9e8122136edc89cc4"></a>

```c
#define PROMETHEUS_SUMMARY_DEFINE(_name, _desc, _label, _collector, ...)
```

相关声明：[PROMETHEUS_SUMMARY_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gaa3c043be86118ff9e8122136edc89cc4)。

Prometheus 摘要指标（Summary）的定义。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 68.3\_函数（Functions）

<a id="r_ga7683de05e8b135161120ad5d3f2edc2c"></a>

```c
int prometheus_summary_observe (struct prometheus_summary *summary, double value)
```

相关声明：[prometheus_summary_observe](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga7683de05e8b135161120ad5d3f2edc2c)、[prometheus_summary](../network_service_model_reference/P052_prometheus_summary_结构体.md)。

在 Prometheus 摘要指标（Summary Metric）中记录一个观测值（Observe a Value）。

<a id="r_ga98369eb2a7c8ce36f7570ed5b55410d8"></a>

```c
int prometheus_summary_observe_set (struct prometheus_summary *summary, double value, unsigned long count)
```

相关声明：[prometheus_summary_observe_set](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga98369eb2a7c8ce36f7570ed5b55410d8)、[prometheus_summary](../network_service_model_reference/P052_prometheus_summary_结构体.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

将摘要值（Summary Value）设置为指定值。


## 68.4\_原页交叉引用（Cross References）

- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/net/prometheus/metric.h](../api_source_supplement_reference/P112_metric.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P846_summary.h_源码浏览.md)
- [prometheus_summary_quantile](../network_service_model_reference/P053_prometheus_summary_quantile_结构体.md)
- [prometheus_summary](../network_service_model_reference/P052_prometheus_summary_结构体.md)
- [PROMETHEUS_SUMMARY_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gaa3c043be86118ff9e8122136edc89cc4)
- [prometheus_summary_observe](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga7683de05e8b135161120ad5d3f2edc2c)
- [prometheus_summary_observe_set](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga98369eb2a7c8ce36f7570ed5b55410d8)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)

<a id="header-details"></a>

---

[上一章](P067_zephyr__dt-bindings__power__stm32h5_iocell.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P069_zephyr__dt-bindings__pinctrl__ti-cc32xx-pinctrl.h_文件参考.md)
