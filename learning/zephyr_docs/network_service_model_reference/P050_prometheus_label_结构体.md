---
id: learning.zephyr-docs.network-service-model-reference.page-50
title: prometheus_label_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structprometheus__label.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_prometheus\_label\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structprometheus__label.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Prometheus标签（Label）的定义。

```c
#include <zephyr/net/prometheus/label.h>
```

<a id="details"></a>

Prometheus 标签（label）定义。此结构体定义一个 Prometheus 标签。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 50.1\_数据成员（Data Fields）

<a id="r_a484ae44cbfdea3d66b010c765829da88"></a>

```c
const char * key
```

相关声明：[key](#a484ae44cbfdea3d66b010c765829da88)。

Prometheus 指标标签的键（key）。

<a id="r_a0cf2605f8904b2cd7ad14273816681b6"></a>

```c
const char * value
```

相关声明：[value](#a0cf2605f8904b2cd7ad14273816681b6)。

Prometheus 指标标签的值（value）。

## 50.2\_详细说明（Detailed Documentation）

<a id="a484ae44cbfdea3d66b010c765829da88"></a>

### `key`

```c
const char* prometheus_label::key
```

Prometheus 指标标签的键（key）。

<a id="a0cf2605f8904b2cd7ad14273816681b6"></a>

### `value`

```c
const char* prometheus_label::value
```

Prometheus 指标标签的值（value）。

本数据类型文档由以下文件生成：

- `zephyr/net/prometheus/label.h`

## 50.3\_原页交叉引用（Cross References）

- [zephyr/net/prometheus/label.h](https://docs.zephyrproject.org/latest/doxygen/html/label_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P049_prometheus_histogram_bucket_结构体.md) · [返回大纲](大纲.md) · [下一章](P051_prometheus_metric_结构体.md)
