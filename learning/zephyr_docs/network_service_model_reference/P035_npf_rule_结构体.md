---
id: learning.zephyr-docs.network-service-model-reference.page-35
title: npf_rule_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnpf__rule.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_npf\_rule\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnpf__rule.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

过滤规则（Filter Rule）结构。

```c
#include <zephyr/net/net_pkt_filter.h>
```

<a id="details"></a>

过滤规则（Filter Rule）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 35.1\_数据成员（Data Fields）

<a id="r_ad5ae58fbcee5112e2defde1d7f4320dc"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#ad5ae58fbcee5112e2defde1d7f4320dc)。

单向链表（Slist）中的规则列表节点。

<a id="r_a872daf53310dd8e20477eafd6808481f"></a>

```c
enum net_verdict result
```

相关声明：[net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)、[result](#a872daf53310dd8e20477eafd6808481f)。

所有测试均通过时的结果。

<a id="r_a3691e7be04a2948f0c979305f48fbb2c"></a>

```c
enum net_priority priority
```

相关声明：[net_priority](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gae87ef466e77ded673ed7e593d3eddffd)、[priority](#a3691e7be04a2948f0c979305f48fbb2c)。

结果为 `NET_CONTINUE` 时使用的优先级。

<a id="r_a06045c693cf06e6ebfc5a74b8c3f5ef7"></a>

```c
uint32_t nb_tests
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[nb_tests](#a06045c693cf06e6ebfc5a74b8c3f5ef7)。

此规则包含的测试数量。

<a id="r_a72c032c55535c82f365b2cd1229cb1e0"></a>

```c
struct npf_test * tests []
```

相关声明：[npf_test](P037_npf_test_结构体.md)、[tests](#a72c032c55535c82f365b2cd1229cb1e0)。

指向 `npf_test` 实例的指针。

## 35.2\_详细说明（Detailed Documentation）

<a id="a06045c693cf06e6ebfc5a74b8c3f5ef7"></a>

### `nb_tests`

```c
uint32_t npf_rule::nb_tests
```

此规则包含的测试数量。

<a id="ad5ae58fbcee5112e2defde1d7f4320dc"></a>

### `node`

```c
sys_snode_t npf_rule::node
```

单向链表（Slist）中的规则列表节点。

<a id="a3691e7be04a2948f0c979305f48fbb2c"></a>

### `priority`

```c
enum net_priority npf_rule::priority
```

结果为 `NET_CONTINUE` 时使用的优先级。

<a id="a872daf53310dd8e20477eafd6808481f"></a>

### `result`

```c
enum net_verdict npf_rule::result
```

所有测试均通过时的结果。

<a id="a72c032c55535c82f365b2cd1229cb1e0"></a>

### `tests`

```c
struct npf_test* npf_rule::tests[]
```

指向 `npf_test` 实例的指针。

本数据类型文档由以下文件生成：

- `zephyr/net/net_pkt_filter.h`

## 35.3\_原页交叉引用（Cross References）

- [zephyr/net/net_pkt_filter.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt__filter_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)
- [net_priority](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gae87ef466e77ded673ed7e593d3eddffd)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [npf_test](P037_npf_test_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P034_netmidi2_userlist_结构体.md) · [返回大纲](大纲.md) · [下一章](P036_npf_rule_list_结构体.md)
