---
id: learning.zephyr-docs.network-service-model-reference.page-36
title: npf_rule_list_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnpf__rule__list.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_npf\_rule\_list\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnpf__rule__list.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

给定测试位置（Test Location）的规则集。

```c
#include <zephyr/net/net_pkt_filter.h>
```

<a id="details"></a>

给定测试位置（Test Location）的规则集。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 36.1\_数据成员（Data Fields）

<a id="r_ab6aadf2d3479853c28e94972e7862931"></a>

```c
sys_slist_t rule_head
```

相关声明：[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)、[rule_head](#ab6aadf2d3479853c28e94972e7862931)。

链表头（List head）。

<a id="r_af4d539d930acb257b1496761219d26cd"></a>

```c
struct k_spinlock lock
```

相关声明：[k_spinlock](../kernel/P066_自旋锁结构参考.md)、[lock](#af4d539d930acb257b1496761219d26cd)。

保护列表访问的锁（lock）。

## 36.2\_详细说明（Detailed Documentation）

<a id="af4d539d930acb257b1496761219d26cd"></a>

### `lock`

```c
struct k_spinlock npf_rule_list::lock
```

保护列表访问的锁（lock）。

<a id="ab6aadf2d3479853c28e94972e7862931"></a>

### `rule_head`

```c
sys_slist_t npf_rule_list::rule_head
```

链表头（List head）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_pkt_filter.h`

## 36.3\_原页交叉引用（Cross References）

- [zephyr/net/net_pkt_filter.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt__filter_8h_source.html)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [k_spinlock](../kernel/P066_自旋锁结构参考.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P035_npf_rule_结构体.md) · [返回大纲](大纲.md) · [下一章](P037_npf_test_结构体.md)
