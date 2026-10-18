---
id: learning.zephyr-docs.api-source-reference.page-268
title: formatter.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/formatter_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第268章\_formatter.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/formatter_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/formatter_8h.html)。

## 268.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="acollector_8h_html"></a>
<a id="agroup__prometheus_html_ga2240cf4f807fe7180f21c8fab3fbbd66"></a>
<a id="agroup__prometheus_html_ga7d219be7f2b3b49a2f936489bdf68fe8"></a>
<a id="astructprometheus__collector_html"></a>
<a id="astructprometheus__metric_html"></a>

```c
/*
 * Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_PROMETHEUS_FORMATTER_H_
#define ZEPHYR_INCLUDE_NET_PROMETHEUS_FORMATTER_H_


#include <zephyr/net/prometheus/collector.h>

int prometheus_format_exposition(struct prometheus_collector *collector, char *buffer,
                                 size_t buffer_size);

int prometheus_format_one_metric(struct prometheus_metric *metric, char *buffer,
                                 size_t buffer_size, int *written);


#endif /* ZEPHYR_INCLUDE_NET_PROMETHEUS_FORMATTER_H_ */
```

## 268.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Mustafa Abdullah Kus, Sparse Technology。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 56 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_PROMETHEUS_FORMATTER_H_`。

## 268.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/formatter_8h.html)
- [zephyr/net/prometheus/collector.h](https://docs.zephyrproject.org/latest/doxygen/html/collector_8h.html)
- [prometheus_format_exposition](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga7d219be7f2b3b49a2f936489bdf68fe8)
- [prometheus_collector](../network_service_model_reference/P045_prometheus_collector_结构体.md)
- [prometheus_format_one_metric](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga2240cf4f807fe7180f21c8fab3fbbd66)
- [prometheus_metric](../network_service_model_reference/P051_prometheus_metric_结构体.md)
- [collector.h](https://docs.zephyrproject.org/latest/doxygen/html/collector_8h.html)

---

[上一章](P267_focaltech_ft9001_reset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P269_fota_http.h_源码浏览.md)
