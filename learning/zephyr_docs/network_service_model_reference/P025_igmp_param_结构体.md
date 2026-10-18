---
id: learning.zephyr-docs.network-service-model-reference.page-25
title: igmp_param_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structigmp__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_igmp\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structigmp__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

互联网组管理协议（IGMP）的参数。

```c
#include <zephyr/net/igmp.h>
```

<a id="details"></a>

互联网组管理协议（IGMP）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 25.1\_数据成员（Data Fields）

<a id="r_a5c76562c4679766f5132036febf05a03"></a>

```c
struct net_in_addr * source_list
```

相关声明：[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[source_list](#a5c76562c4679766f5132036febf05a03)。

要包含或排除的源列表。

<a id="r_acb8f39f66f0c11733cf855f4303b0495"></a>

```c
size_t sources_len
```

相关声明：[sources_len](#acb8f39f66f0c11733cf855f4303b0495)。

源列表长度。

<a id="r_a2b60c5de6e21371dacc7f7f34ba6904b"></a>

```c
bool include
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[include](#a2b60c5de6e21371dacc7f7f34ba6904b)。

源列表过滤器类型。

## 25.2\_详细说明（Detailed Documentation）

<a id="a2b60c5de6e21371dacc7f7f34ba6904b"></a>

### `include`

```c
bool igmp_param::include
```

源列表过滤器类型。

<a id="a5c76562c4679766f5132036febf05a03"></a>

### `source_list`

```c
struct net_in_addr* igmp_param::source_list
```

要包含或排除的源列表。

<a id="acb8f39f66f0c11733cf855f4303b0495"></a>

### `sources_len`

```c
size_t igmp_param::sources_len
```

源列表长度。

本数据类型文档由以下文件生成：

- `zephyr/net/igmp.h`

## 25.3\_原页交叉引用（Cross References）

- [zephyr/net/igmp.h](https://docs.zephyrproject.org/latest/doxygen/html/igmp_8h_source.html)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P024_http2_settings_field_结构体.md) · [返回大纲](大纲.md) · [下一章](P026_ipcp_options_结构体.md)
