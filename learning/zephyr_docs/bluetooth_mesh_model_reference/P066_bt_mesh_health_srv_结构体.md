---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-66
title: bt_mesh_health_srv_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__health__srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_bt\_mesh\_health\_srv\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__health__srv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Mesh健康服务器（Health Server）的模型上下文。

```c
#include <zephyr/bluetooth/mesh/health_srv.h>
```

<a id="details"></a>

Mesh健康服务器（Health Server）的模型上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 66.1\_数据成员（Data Fields）

<a id="r_aff95fc381ea8048d4d76668b92126dc6"></a>

```c
const struct bt_mesh_model * model
```

相关声明：[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[model](#aff95fc381ea8048d4d76668b92126dc6)。

组成数据模型条目指针（Composition data model entry pointer）。

<a id="r_a4d316010b2737eca7bad3aef6774d52b"></a>

```c
const struct bt_mesh_health_srv_cb * cb
```

相关声明：[bt_mesh_health_srv_cb](P067_bt_mesh_health_srv_cb_结构体.md)、[cb](#a4d316010b2737eca7bad3aef6774d52b)。

可选的回调结构（Optional callback struct）。

<a id="r_a8df7f6c7e434cb717b9b51a3167b5e86"></a>

```c
struct k_work_delayable attn_timer
```

相关声明：[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[attn_timer](#a8df7f6c7e434cb717b9b51a3167b5e86)。

关注定时器状态（Attention Timer state）。

## 66.2\_详细说明（Detailed Documentation）

<a id="a8df7f6c7e434cb717b9b51a3167b5e86"></a>

### `attn_timer`

```c
struct k_work_delayable bt_mesh_health_srv::attn_timer
```

关注定时器状态（Attention Timer state）。

<a id="a4d316010b2737eca7bad3aef6774d52b"></a>

### `cb`

```c
const struct bt_mesh_health_srv_cb* bt_mesh_health_srv::cb
```

可选的回调结构（Optional callback struct）。

<a id="aff95fc381ea8048d4d76668b92126dc6"></a>

### `model`

```c
const struct bt_mesh_model* bt_mesh_health_srv::model
```

组成数据模型条目指针（Composition data model entry pointer）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/health_srv.h`

## 66.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/health_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/health__srv_8h_source.html)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)
- [bt_mesh_health_srv_cb](P067_bt_mesh_health_srv_cb_结构体.md)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P065_bt_mesh_health_cli_结构体.md) · [返回大纲](大纲.md) · [下一章](P067_bt_mesh_health_srv_cb_结构体.md)
