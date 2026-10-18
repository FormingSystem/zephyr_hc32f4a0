---
id: learning.zephyr-docs.network-application-model-reference.page-51
title: lwm2m_time_series_elem_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlwm2m__time__series__elem.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_lwm2m\_time\_series\_elem\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlwm2m__time__series__elem.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

轻量级M2M（LwM2M）的时间序列数据结构。

```c
#include <zephyr/net/lwm2m.h>
```

<a id="details"></a>

轻量级M2M（LwM2M）的时间序列数据结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 51.1\_数据成员（Data Fields）

<a id="r_acd00227c551b6ee1960b3881819ef90b"></a>

```c
time_t t
```

相关声明：[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)、[t](#acd00227c551b6ee1960b3881819ef90b)。

缓存数据的Unix时间戳（Timestamp）。

```c
union {
```

<a id="r_a8c4c934ccd7d1d2d596522aeb21b934d"></a>

```c
};
```

元素值（Element Value）。

## 51.2\_详细说明（Detailed Documentation）

<a id="a8c4c934ccd7d1d2d596522aeb21b934d"></a>

### `[union]`

```c
union { ... } lwm2m_time_series_elem
```

元素值（Element Value）。

<a id="acd00227c551b6ee1960b3881819ef90b"></a>

### `t`

```c
time_t lwm2m_time_series_elem::t
```

缓存数据的Unix时间戳（Timestamp）。

本数据类型文档由以下文件生成：

- `zephyr/net/lwm2m.h`

## 51.3\_原页交叉引用（Cross References）

- [zephyr/net/lwm2m.h](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m_8h_source.html)
- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- [lwm2m_time_series_elem](P051_lwm2m_time_series_elem_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P050_lwm2m_res_item_结构体.md) · [返回大纲](大纲.md) · [下一章](P052_mqtt_auth_param_结构体.md)
