---
id: learning.zephyr-docs.network-service-model-reference.page-45
title: prometheus_collector_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structprometheus__collector.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_prometheus\_collector\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structprometheus__collector.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Prometheus采集器（Collector）的定义。

```c
#include <zephyr/net/prometheus/collector.h>
```

<a id="details"></a>

Prometheus 收集器（collector）定义。此结构体定义一个 Prometheus 收集器。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 45.1\_数据成员（Data Fields）

<a id="r_a050b6094f92369225dce734ef9f50476"></a>

```c
const char * name
```

相关声明：[name](#a050b6094f92369225dce734ef9f50476)。

收集器名称。

<a id="r_a389528dad4e2ada62ca85650b6be5972"></a>

```c
sys_slist_t metrics
```

相关声明：[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)、[metrics](#a389528dad4e2ada62ca85650b6be5972)。

与收集器关联的指标（metrics）数组。

<a id="r_a43e08aa447c0388d80771c33f59992b7"></a>

```c
struct k_mutex lock
```

相关声明：[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)、[lock](#a43e08aa447c0388d80771c33f59992b7)。

用于保护指标列表操作的互斥锁（mutex）。

<a id="r_ae131dcdd35fbacd30a210b547718c6be"></a>

```c
prometheus_scrape_cb_t user_cb
```

相关声明：[prometheus_scrape_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga4e2541cb094915187157d44a29e2d6b5)、[user_cb](#ae131dcdd35fbacd30a210b547718c6be)。

用户回调函数。

<a id="r_acd2c684c0c920f75e86d2560b4bb29e2"></a>

```c
void * user_data
```

相关声明：[user_data](#acd2c684c0c920f75e86d2560b4bb29e2)。

用户数据（User Data）。

## 45.2\_详细说明（Detailed Documentation）

<a id="a43e08aa447c0388d80771c33f59992b7"></a>

### `lock`

```c
struct k_mutex prometheus_collector::lock
```

用于保护指标列表操作的互斥锁（mutex）。

<a id="a389528dad4e2ada62ca85650b6be5972"></a>

### `metrics`

```c
sys_slist_t prometheus_collector::metrics
```

与收集器关联的指标（metrics）数组。

<a id="a050b6094f92369225dce734ef9f50476"></a>

### `name`

```c
const char* prometheus_collector::name
```

收集器名称。

<a id="ae131dcdd35fbacd30a210b547718c6be"></a>

### `user_cb`

```c
prometheus_scrape_cb_t prometheus_collector::user_cb
```

用户回调函数。

如果设置，则通过此函数回调获取指标数据。

<a id="acd2c684c0c920f75e86d2560b4bb29e2"></a>

### `user_data`

```c
void* prometheus_collector::user_data
```

用户数据（User Data）。

本数据类型文档由以下文件生成：

- `zephyr/net/prometheus/collector.h`

## 45.3\_原页交叉引用（Cross References）

- [zephyr/net/prometheus/collector.h](https://docs.zephyrproject.org/latest/doxygen/html/collector_8h_source.html)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [prometheus_scrape_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html#ga4e2541cb094915187157d44a29e2d6b5)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P044_ppp_fsm_结构体.md) · [返回大纲](大纲.md) · [下一章](P046_prometheus_counter_结构体.md)
