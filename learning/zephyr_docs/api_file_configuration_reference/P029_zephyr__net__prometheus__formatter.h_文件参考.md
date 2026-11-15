---
id: learning.zephyr-docs.api-file-configuration-reference.page-29
title: zephyr__net__prometheus__formatter.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/formatter_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_zephyr\_\_net\_\_prometheus\_\_formatter.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/formatter_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Prometheus格式化器（Formatter）的API。

<a id="details"></a>

```c
#include <zephyr/net/prometheus/collector.h>
```

查看此文件的源码。

Prometheus格式化器（Formatter）的API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 29.1\_函数（Functions）

<a id="r_ga7d219be7f2b3b49a2f936489bdf68fe8"></a>

```c
int prometheus_format_exposition (struct prometheus_collector *collector, char *buffer, size_t buffer_size)
```

相关声明：[prometheus_format_exposition](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga7d219be7f2b3b49a2f936489bdf68fe8)、[prometheus_collector](../network_service_model_reference/P045_prometheus_collector_结构体.md)。

格式化 Prometheus 暴露数据（Exposition Data）。

<a id="r_ga2240cf4f807fe7180f21c8fab3fbbd66"></a>

```c
int prometheus_format_one_metric (struct prometheus_metric *metric, char *buffer, size_t buffer_size, int *written)
```

相关声明：[prometheus_format_one_metric](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga2240cf4f807fe7180f21c8fab3fbbd66)、[prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)。

格式化单个 Prometheus 指标（Metric）的暴露数据（Exposition Data）。


## 29.2\_原页交叉引用（Cross References）

- [zephyr/net/prometheus/collector.h](../api_source_reference/P109_collector.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P268_formatter.h_源码浏览.md)
- [prometheus_format_exposition](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga7d219be7f2b3b49a2f936489bdf68fe8)
- [prometheus_collector](../network_service_model_reference/P045_prometheus_collector_结构体.md)
- [prometheus_format_one_metric](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga2240cf4f807fe7180f21c8fab3fbbd66)
- [prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)

<a id="header-details"></a>

---

[上一章](P028_zephyr__xen__flask.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P030_zephyr__mgmt__mcumgr__grp__fs_mgmt__fs_mgmt_callbacks.h_文件参考.md)
