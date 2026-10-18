---
id: learning.zephyr-docs.network-service-model-reference.page-51
title: prometheus_metric_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structprometheus__metric.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_prometheus\_metric\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structprometheus__metric.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于表示Prometheus指标基类（Metric Base）的类型。

```c
#include <zephyr/net/prometheus/metric.h>
```

<a id="details"></a>

用于表示 Prometheus 指标基础部分（metric base）的类型。每个指标都关联一个 `prometheus_metric` 结构体，用于控制指标的访问和使用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 51.1\_数据成员（Data Fields）

<a id="r_a68b4a71af679bef383d635f1b0018dba"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a68b4a71af679bef383d635f1b0018dba)。

单向链表（Slist）中的指标列表节点。

<a id="r_a1138f189a5bdd44639dace426ef8f55a"></a>

```c
struct prometheus_collector * collector
```

相关声明：[prometheus_collector](P045_prometheus_collector_结构体.md)、[collector](#a1138f189a5bdd44639dace426ef8f55a)。

反向指向此指标所属收集器的指针。

<a id="r_a67e8d38a696f2b20a076b8da6b1250e3"></a>

```c
void * metric
```

相关声明：[metric](#a67e8d38a696f2b20a076b8da6b1250e3)。

反向指向实际指标的指针，例如计数器（counter）或仪表（gauge）。

<a id="r_a05e19d7781f4724dfe7776e62cd69ca2"></a>

```c
enum prometheus_metric_type type
```

相关声明：[prometheus_metric_type](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga3499408dda4e539634c332c797651932)、[type](#a05e19d7781f4724dfe7776e62cd69ca2)。

Prometheus 指标类型。

<a id="r_a5266bf5bd528cdd4c34ea56d7a96129d"></a>

```c
const char * name
```

相关声明：[name](#a5266bf5bd528cdd4c34ea56d7a96129d)。

Prometheus 指标名称。

<a id="r_a9ceba3f813e1bcf36c333af975c7ac76"></a>

```c
const char * description
```

相关声明：[description](#a9ceba3f813e1bcf36c333af975c7ac76)。

Prometheus 指标描述。

<a id="r_af3ae0862633b2ce475f7c6851d13c3d1"></a>

```c
struct prometheus_label labels [MAX_PROMETHEUS_LABELS_PER_METRIC]
```

相关声明：[prometheus_label](P050_prometheus_label_结构体.md)、[labels](#af3ae0862633b2ce475f7c6851d13c3d1)、[MAX_PROMETHEUS_LABELS_PER_METRIC](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga5fd572e5351cda0855cb587e88c3a247)。

与 Prometheus 指标关联的标签。

<a id="r_a198f0ddcf143d8728d914ee34eb8cb78"></a>

```c
int num_labels
```

相关声明：[num_labels](#a198f0ddcf143d8728d914ee34eb8cb78)。

与 Prometheus 指标关联的标签数量。

<a id="r_ae2db853cae2c49634fda25eb23b825da"></a>

```c
void * user_data
```

相关声明：[user_data](#ae2db853cae2c49634fda25eb23b825da)。

用户定义的数据。

## 51.2\_详细说明（Detailed Documentation）

<a id="a1138f189a5bdd44639dace426ef8f55a"></a>

### `collector`

```c
struct prometheus_collector* prometheus_metric::collector
```

反向指向此指标所属收集器的指针。

<a id="a9ceba3f813e1bcf36c333af975c7ac76"></a>

### `description`

```c
const char* prometheus_metric::description
```

Prometheus 指标描述。

<a id="af3ae0862633b2ce475f7c6851d13c3d1"></a>

### `labels`

```c
struct prometheus_label prometheus_metric::labels[MAX_PROMETHEUS_LABELS_PER_METRIC]
```

与 Prometheus 指标关联的标签。

<a id="a67e8d38a696f2b20a076b8da6b1250e3"></a>

### `metric`

```c
void* prometheus_metric::metric
```

反向指向实际指标的指针，例如计数器（counter）或仪表（gauge）。

这只是临时方案，最终目标是将此通用指标结构体嵌入实际的指标结构体。

<a id="a5266bf5bd528cdd4c34ea56d7a96129d"></a>

### `name`

```c
const char* prometheus_metric::name
```

Prometheus 指标名称。

<a id="a68b4a71af679bef383d635f1b0018dba"></a>

### `node`

```c
sys_snode_t prometheus_metric::node
```

单向链表（Slist）中的指标列表节点。

<a id="a198f0ddcf143d8728d914ee34eb8cb78"></a>

### `num_labels`

```c
int prometheus_metric::num_labels
```

与 Prometheus 指标关联的标签数量。

<a id="a05e19d7781f4724dfe7776e62cd69ca2"></a>

### `type`

```c
enum prometheus_metric_type prometheus_metric::type
```

Prometheus 指标类型。

<a id="ae2db853cae2c49634fda25eb23b825da"></a>

### `user_data`

```c
void* prometheus_metric::user_data
```

用户定义的数据。

本数据类型文档由以下文件生成：

- `zephyr/net/prometheus/metric.h`

## 51.3\_原页交叉引用（Cross References）

- [zephyr/net/prometheus/metric.h](https://docs.zephyrproject.org/latest/doxygen/html/metric_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [prometheus_collector](P045_prometheus_collector_结构体.md)
- [prometheus_metric_type](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga3499408dda4e539634c332c797651932)
- [prometheus_label](P050_prometheus_label_结构体.md)
- [MAX_PROMETHEUS_LABELS_PER_METRIC](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga5fd572e5351cda0855cb587e88c3a247)
- [prometheus_metric](P051_prometheus_metric_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P050_prometheus_label_结构体.md) · [返回大纲](大纲.md) · [下一章](P052_prometheus_summary_结构体.md)
