---
id: learning.zephyr-docs.api-file-configuration-reference.page-31
title: zephyr__net__prometheus__gauge.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gauge_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_zephyr\_\_net\_\_prometheus\_\_gauge.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gauge_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Prometheus仪表（Gauge）的API。

<a id="details"></a>

```c
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/prometheus/metric.h>
```

查看此文件的源码。

Prometheus仪表（Gauge）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 31.1\_数据结构（Data Structures）

<a id="r_prometheus_5Fgauge"></a>

```c
struct prometheus_gauge
```

相关声明：[prometheus_gauge](../network_service_model_reference/P047_prometheus_gauge_结构体.md)。

用于表示Prometheus仪表指标（Gauge Metric）的类型。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 31.2\_宏定义（Macros）

<a id="r_ga362e708722846a3ca9299e8994becd13"></a>

```c
#define PROMETHEUS_GAUGE_DEFINE(_name, _desc, _label, _collector, ...)
```

相关声明：[PROMETHEUS_GAUGE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga362e708722846a3ca9299e8994becd13)。

Prometheus 仪表（Gauge）的定义。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 31.3\_函数（Functions）

<a id="r_ga3ddc5efbdb9639486862f3df4b845fce"></a>

```c
int prometheus_gauge_set (struct prometheus_gauge *gauge, double value)
```

相关声明：[prometheus_gauge_set](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga3ddc5efbdb9639486862f3df4b845fce)、[prometheus_gauge](../network_service_model_reference/P047_prometheus_gauge_结构体.md)。

设置 Prometheus 仪表指标（Gauge Metric）的值。


## 31.4\_原页交叉引用（Cross References）

- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/net/prometheus/metric.h](../api_source_supplement_reference/P112_metric.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P283_gauge.h_源码浏览.md)
- [prometheus_gauge](../network_service_model_reference/P047_prometheus_gauge_结构体.md)
- [PROMETHEUS_GAUGE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga362e708722846a3ca9299e8994becd13)
- [prometheus_gauge_set](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga3ddc5efbdb9639486862f3df4b845fce)

<a id="header-details"></a>

---

[上一章](P030_zephyr__mgmt__mcumgr__grp__fs_mgmt__fs_mgmt_callbacks.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P032_zephyr__drivers__sensor__generic_emul.h_文件参考.md)
