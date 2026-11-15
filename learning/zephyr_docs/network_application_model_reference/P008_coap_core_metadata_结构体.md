---
id: learning.zephyr-docs.network-application-model-reference.page-8
title: coap_core_metadata_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcoap__core__metadata.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_coap\_core\_metadata\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__core__metadata.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

如果需要为“well-known/core”虚拟资源包含的资源添加属性，应让metadata字段指向有效的coap_core_metadata结构。

```c
#include <zephyr/net/coap_link_format.h>
```

<a id="details"></a>

如果需要为“well-known/core”虚拟资源包含的资源添加属性，应让metadata字段指向有效的coap_core_metadata结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_aeb04ef8b47ecc144dd036007cccd2e59"></a>

```c
const char *const * attributes
```

相关声明：[attributes](#aeb04ef8b47ecc144dd036007cccd2e59)。

要添加的属性（Attributes）列表。

<a id="r_a74e8a533d7f8596498d5d0ce2afc102f"></a>

```c
void * user_data
```

相关声明：[user_data](#a74e8a533d7f8596498d5d0ce2afc102f)。

用户专用数据（User Specific Data）。

## 8.2\_详细说明（Detailed Documentation）

<a id="aeb04ef8b47ecc144dd036007cccd2e59"></a>

### `attributes`

```c
const char* const* coap_core_metadata::attributes
```

要添加的属性（Attributes）列表。

<a id="a74e8a533d7f8596498d5d0ce2afc102f"></a>

### `user_data`

```c
void* coap_core_metadata::user_data
```

用户专用数据（User Specific Data）。

本数据类型文档由以下文件生成：

- `zephyr/net/coap_link_format.h`

## 8.3\_原页交叉引用（Cross References）

- [coap_core_metadata](P008_coap_core_metadata_结构体.md)
- [zephyr/net/coap_link_format.h](https://docs.zephyrproject.org/latest/doxygen/html/coap__link__format_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_coap_client_tcp_request_结构体.md) · [返回大纲](大纲.md) · [下一章](P009_coap_observer_结构体.md)
