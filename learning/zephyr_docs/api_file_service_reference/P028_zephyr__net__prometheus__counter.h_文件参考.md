---
id: learning.zephyr-docs.api-file-service-reference.page-28
title: zephyr__net__prometheus__counter.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net_2prometheus_2counter_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_zephyr\_\_net\_\_prometheus\_\_counter.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/net_2prometheus_2counter_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Prometheus计数器（Counter）的API。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/prometheus/metric.h>
```

查看此文件的源码。

Prometheus计数器（Counter）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 28.1\_数据结构（Data Structures）

<a id="r_prometheus_5Fcounter"></a>

```c
struct prometheus_counter
```

相关声明：[prometheus_counter](../network_service_model_reference/P046_prometheus_counter_结构体.md)。

用于表示Prometheus计数器指标（Counter Metric）的类型。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 28.2\_宏定义（Macros）

<a id="r_gadbfcfc7904d6388d2c9dc81d4803264c"></a>

```c
#define PROMETHEUS_COUNTER_DEFINE(_name, _desc, _label, _collector, ...)
```

相关声明：[PROMETHEUS_COUNTER_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gadbfcfc7904d6388d2c9dc81d4803264c)。

Prometheus 计数器（Counter）的定义。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 28.3\_函数（Functions）

<a id="r_ga9b7461d625acc075c9511249c67741ab"></a>

```c
int prometheus_counter_add (struct prometheus_counter *counter, uint64_t value)
```

相关声明：[prometheus_counter_add](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga9b7461d625acc075c9511249c67741ab)、[prometheus_counter](../network_service_model_reference/P046_prometheus_counter_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

增加 Prometheus 计数器指标（Counter Metric）的值：将指定计数器增加任意给定数量。

<a id="r_gad2220d089050bc5db1e5866429d515b3"></a>

```c
static int prometheus_counter_inc (struct prometheus_counter *counter)
```

相关声明：[prometheus_counter_inc](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gad2220d089050bc5db1e5866429d515b3)、[prometheus_counter](../network_service_model_reference/P046_prometheus_counter_结构体.md)。

增加 Prometheus 计数器指标（Counter Metric）的值：将指定计数器增加 1。

<a id="r_ga8621228b7a66a6a42fb2cb838ec94dfe"></a>

```c
int prometheus_counter_set (struct prometheus_counter *counter, uint64_t value)
```

相关声明：[prometheus_counter_set](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga8621228b7a66a6a42fb2cb838ec94dfe)、[prometheus_counter](../network_service_model_reference/P046_prometheus_counter_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

将计数器值（Counter Value）设置为指定值。


## 28.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/net/prometheus/metric.h](../api_source_supplement_reference/P112_metric.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P574_counter.h_源码浏览.md)
- [prometheus_counter](../network_service_model_reference/P046_prometheus_counter_结构体.md)
- [PROMETHEUS_COUNTER_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gadbfcfc7904d6388d2c9dc81d4803264c)
- [prometheus_counter_add](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga9b7461d625acc075c9511249c67741ab)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [prometheus_counter_inc](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#gad2220d089050bc5db1e5866429d515b3)
- [prometheus_counter_set](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga8621228b7a66a6a42fb2cb838ec94dfe)

<a id="header-details"></a>

---

[上一章](P027_zephyr__drivers__pcie__msi.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P029_zephyr__dt-bindings__gpio__nordic-npm10xx-gpio.h_文件参考.md)
