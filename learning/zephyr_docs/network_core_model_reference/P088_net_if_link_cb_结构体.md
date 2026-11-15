---
id: learning.zephyr-docs.network-core-model-reference.page-88
title: net_if_link_cb_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__link__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第88章\_net\_if\_link\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__if__link__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

链路回调处理程序（Link Callback Handler）的结构。

```c
#include <zephyr/net/net_if.h>
```

<a id="details"></a>

链路回调处理结构（Link callback handler struct）。保存链路回调信息。调用者必须确保所指向的变量在整个注册有效期（Lifetime of registration）内均有效；通常意味着该变量不能在栈（Stack）上分配。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 88.1\_数据成员（Data Fields）

<a id="r_accae7945a802c5b7fc36948b12a365ef"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#accae7945a802c5b7fc36948b12a365ef)。

单向链表（Slist）的节点信息（Node information）。

<a id="r_a66092a22cba3dd69ac1a91c3522240bb"></a>

```c
net_if_link_callback_t cb
```

相关声明：[net_if_link_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0f87d5753fcd7cce40ecd161e6c91078)、[cb](#a66092a22cba3dd69ac1a91c3522240bb)。

链路回调（Link callback）。

## 88.2\_详细说明（Detailed Documentation）

<a id="a66092a22cba3dd69ac1a91c3522240bb"></a>

### `cb`

```c
net_if_link_callback_t net_if_link_cb::cb
```

链路回调（Link callback）。

<a id="accae7945a802c5b7fc36948b12a365ef"></a>

### `node`

```c
sys_snode_t net_if_link_cb::node
```

单向链表（Slist）的节点信息（Node information）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_if.h`

## 88.3\_原页交叉引用（Cross References）

- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [net_if_link_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga0f87d5753fcd7cce40ecd161e6c91078)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P087_net_if_ipv6_prefix_结构体.md) · [返回大纲](大纲.md) · [下一章](P089_net_if_mcast_addr_结构体.md)
