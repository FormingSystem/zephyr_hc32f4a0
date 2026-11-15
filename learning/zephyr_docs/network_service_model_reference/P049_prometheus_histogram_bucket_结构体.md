---
id: learning.zephyr-docs.network-service-model-reference.page-49
title: prometheus_histogram_bucket_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structprometheus__histogram__bucket.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_prometheus\_histogram\_bucket\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structprometheus__histogram__bucket.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Prometheus直方图桶（Histogram Bucket）的定义。

```c
#include <zephyr/net/prometheus/histogram.h>
```

<a id="details"></a>

Prometheus 直方图桶（histogram bucket）定义。此结构体定义一个 Prometheus 直方图桶。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 49.1\_数据成员（Data Fields）

<a id="r_aa18e37384ee094972b6a330bb4323fa3"></a>

```c
double upper_bound
```

相关声明：[upper_bound](#aa18e37384ee094972b6a330bb4323fa3)。

桶的上界值（upper bound）。

<a id="r_a93865334a397013506d39a28505586c4"></a>

```c
unsigned long count
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[count](#a93865334a397013506d39a28505586c4)。

桶中观测次数的累计值。

## 49.2\_详细说明（Detailed Documentation）

<a id="a93865334a397013506d39a28505586c4"></a>

### `count`

```c
unsigned long prometheus_histogram_bucket::count
```

桶中观测次数的累计值。

<a id="aa18e37384ee094972b6a330bb4323fa3"></a>

### `upper_bound`

```c
double prometheus_histogram_bucket::upper_bound
```

桶的上界值（upper bound）。

本数据类型文档由以下文件生成：

- `zephyr/net/prometheus/histogram.h`

## 49.3\_原页交叉引用（Cross References）

- [zephyr/net/prometheus/histogram.h](https://docs.zephyrproject.org/latest/doxygen/html/histogram_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P048_prometheus_histogram_结构体.md) · [返回大纲](大纲.md) · [下一章](P050_prometheus_label_结构体.md)
