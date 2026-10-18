---
id: learning.zephyr-docs.network-service-model-reference.page-53
title: prometheus_summary_quantile_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structprometheus__summary__quantile.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_prometheus\_summary\_quantile\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structprometheus__summary__quantile.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Prometheus摘要分位数（Summary Quantile）的定义。

```c
#include <zephyr/net/prometheus/summary.h>
```

<a id="details"></a>

Prometheus 摘要分位数（summary quantile）定义。此结构体定义一个 Prometheus 摘要分位数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 53.1\_数据成员（Data Fields）

<a id="r_a811db0cddd6fd444a899be83e4116b92"></a>

```c
double quantile
```

相关声明：[quantile](#a811db0cddd6fd444a899be83e4116b92)。

摘要的分位数（quantile）。

<a id="r_a53fb78e35a0748f568d7bb15b083b037"></a>

```c
double value
```

相关声明：[value](#a53fb78e35a0748f568d7bb15b083b037)。

此分位数对应的值。

<a id="r_a788d30204d7ce61940741cefd2c073f6"></a>

```c
void * user_data
```

相关声明：[user_data](#a788d30204d7ce61940741cefd2c073f6)。

用户数据（User Data）。

## 53.2\_详细说明（Detailed Documentation）

<a id="a811db0cddd6fd444a899be83e4116b92"></a>

### `quantile`

```c
double prometheus_summary_quantile::quantile
```

摘要的分位数（quantile）。

<a id="a788d30204d7ce61940741cefd2c073f6"></a>

### `user_data`

```c
void* prometheus_summary_quantile::user_data
```

用户数据（User Data）。

<a id="a53fb78e35a0748f568d7bb15b083b037"></a>

### `value`

```c
double prometheus_summary_quantile::value
```

此分位数对应的值。

本数据类型文档由以下文件生成：

- `zephyr/net/prometheus/summary.h`

## 53.3\_原页交叉引用（Cross References）

- [zephyr/net/prometheus/summary.h](https://docs.zephyrproject.org/latest/doxygen/html/summary_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P052_prometheus_summary_结构体.md) · [返回大纲](大纲.md) · [下一章](P054_ptp_clock_driver_api_结构体.md)
