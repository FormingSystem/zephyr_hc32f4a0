---
id: learning.zephyr-docs.network-service-model-reference.page-13
title: ethernet_txtime_param_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structethernet__txtime__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_ethernet\_txtime\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structethernet__txtime__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网发送时间（TXTIME）的专用参数。

```c
#include <zephyr/net/ethernet.h>
```

<a id="details"></a>

以太网发送时间（TXTIME）的专用参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_ab4a709e6907e76f9cf23c085f5be5d99"></a>

```c
enum ethernet_txtime_param_type type
```

相关声明：[type](#ab4a709e6907e76f9cf23c085f5be5d99)。

发送时间（TXTIME）参数类型。

<a id="r_aa4a46b7153b2a69ca0134f4e10bc7165"></a>

```c
int queue_id
```

相关声明：[queue_id](#aa4a46b7153b2a69ca0134f4e10bc7165)。

要配置 TXTIME 的队列编号。

<a id="r_a74b1e05cf0fac8aa435ba966e110ae27"></a>

```c
bool enable_txtime
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enable_txtime](#a74b1e05cf0fac8aa435ba966e110ae27)。

按队列启用或禁用 TXTIME。

## 13.2\_详细说明（Detailed Documentation）

<a id="a74b1e05cf0fac8aa435ba966e110ae27"></a>

### `enable_txtime`

```c
bool ethernet_txtime_param::enable_txtime
```

按队列启用或禁用 TXTIME。

<a id="aa4a46b7153b2a69ca0134f4e10bc7165"></a>

### `queue_id`

```c
int ethernet_txtime_param::queue_id
```

要配置 TXTIME 的队列编号。

<a id="ab4a709e6907e76f9cf23c085f5be5d99"></a>

### `type`

```c
enum ethernet_txtime_param_type ethernet_txtime_param::type
```

发送时间（TXTIME）参数类型。

本数据类型文档由以下文件生成：

- `zephyr/net/ethernet.h`

## 13.3\_原页交叉引用（Cross References）

- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_ethernet_qbv_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P014_ethphy_driver_api_结构体.md)
