---
id: learning.zephyr-docs.network-service-model-reference.page-37
title: npf_test_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnpf__test.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_npf\_test\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnpf__test.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于嵌入更大结构中的通用过滤器测试结构（Filter Test Structure）。

```c
#include <zephyr/net/net_pkt_filter.h>
```

<a id="details"></a>

用于嵌入更大结构中的通用过滤器测试结构（Filter Test Structure）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 37.1\_数据成员（Data Fields）

<a id="r_ac49921514690a71986ca4d07245cfe7d"></a>

```c
npf_test_fn_t * fn
```

相关声明：[fn](#ac49921514690a71986ca4d07245cfe7d)。

数据包条件测试函数（packet condition test function）。

## 37.2\_详细说明（Detailed Documentation）

<a id="ac49921514690a71986ca4d07245cfe7d"></a>

### `fn`

```c
npf_test_fn_t* npf_test::fn
```

数据包条件测试函数（packet condition test function）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_pkt_filter.h`

## 37.3\_原页交叉引用（Cross References）

- [zephyr/net/net_pkt_filter.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt__filter_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P036_npf_rule_list_结构体.md) · [返回大纲](大纲.md) · [下一章](P038_offloaded_if_api_结构体.md)
