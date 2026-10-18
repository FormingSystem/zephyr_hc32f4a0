---
id: learning.zephyr-docs.api-file-supplement-reference.page-66
title: zephyr__net__prometheus__metric.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/metric_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_zephyr\_\_net\_\_prometheus\_\_metric.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/metric_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Prometheus指标（Metric）的接口。

<a id="details"></a>

```c
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/slist.h>
#include <zephyr/net/prometheus/label.h>
```

查看此文件的源码。

Prometheus指标（Metric）的接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 66.1\_数据结构（Data Structures）

<a id="r_prometheus_5Fmetric"></a>

```c
struct prometheus_metric
```

相关声明：[prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)。

用于表示Prometheus指标基类（Metric Base）的类型。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 66.2\_枚举（Enumerations）

<a id="r_ga3499408dda4e539634c332c797651932"></a>

```c
enum prometheus_metric_type { PROMETHEUS_COUNTER = 0 , PROMETHEUS_GAUGE , PROMETHEUS_SUMMARY , PROMETHEUS_HISTOGRAM }
```

相关声明：[prometheus_metric_type](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga3499408dda4e539634c332c797651932)、[PROMETHEUS_COUNTER](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b)、[PROMETHEUS_GAUGE](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd)、[PROMETHEUS_SUMMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074)、[PROMETHEUS_HISTOGRAM](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf)。

Prometheus 指标类型（Metric Types）。


## 66.3\_原页交叉引用（Cross References）

- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/net/prometheus/label.h](../api_source_reference/P434_label.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P112_metric.h_源码浏览.md)
- [prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)
- [prometheus_metric_type](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga3499408dda4e539634c332c797651932)
- [PROMETHEUS_COUNTER](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b)
- [PROMETHEUS_GAUGE](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd)
- [PROMETHEUS_SUMMARY](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074)
- [PROMETHEUS_HISTOGRAM](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf)

<a id="header-details"></a>

---

[上一章](P065_zephyr__net__http__method.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P067_zephyr__dt-bindings__mfd__mfd_it8801_altctrl.h_文件参考.md)
