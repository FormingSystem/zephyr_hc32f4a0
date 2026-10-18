---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-11
title: bt_br_discovery_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__br__discovery__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_bt\_br\_discovery\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__br__discovery__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/classic/classic.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_a3315f86bf3c9dbf339aa2254e0679182"></a>

```c
void(* recv )(const struct bt_br_discovery_result *result)
```

相关声明：[recv](#a3315f86bf3c9dbf339aa2254e0679182)、[bt_br_discovery_result](P013_bt_br_discovery_result_结构体.md)。

收到查询响应的回调（Inquiry response received callback）。

<a id="r_a09c9f7258ea1739bf9330cf5c5bd882d"></a>

```c
void(* timeout )(const struct bt_br_discovery_result *results, size_t count)
```

相关声明：[timeout](#a09c9f7258ea1739bf9330cf5c5bd882d)、[bt_br_discovery_result](P013_bt_br_discovery_result_结构体.md)。

设备发现超时（Discovery timeout）后，查询（Inquiry）已停止。

<a id="r_a6ea814cabf9747cc7720ece9be59c8b9"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a6ea814cabf9747cc7720ece9be59c8b9)。

## 11.2\_详细说明（Detailed Documentation）

<a id="a6ea814cabf9747cc7720ece9be59c8b9"></a>

### `node`

```c
sys_snode_t bt_br_discovery_cb::node
```

<a id="a3315f86bf3c9dbf339aa2254e0679182"></a>

### `recv`

```c
void(* bt_br_discovery_cb::recv) (const struct bt_br_discovery_result *result)
```

收到查询响应的回调（Inquiry response received callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `result` | 用于保存发现结果（Discovery results）的存储空间。 |

<a id="a09c9f7258ea1739bf9330cf5c5bd882d"></a>

### `timeout`

```c
void(* bt_br_discovery_cb::timeout) (const struct bt_br_discovery_result *results, size_t count)
```

设备发现超时（Discovery timeout）后，查询（Inquiry）已停止。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `results` | 用于保存发现结果（Discovery results）的存储空间。 |
| `count` | 有效发现结果的数量（Valid discovery results）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/classic.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/classic.h](https://docs.zephyrproject.org/latest/doxygen/html/classic_8h_source.html)
- [bt_br_discovery_result](P013_bt_br_discovery_result_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_bt_br_conn_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_bt_br_discovery_param_结构体.md)
