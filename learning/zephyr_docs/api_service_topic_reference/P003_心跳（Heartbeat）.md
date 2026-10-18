---
id: learning.zephyr-docs.api-service-topic-reference.page-3
title: 心跳（Heartbeat）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__heartbeat.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_心跳（Heartbeat）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__heartbeat.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

心跳（Heartbeat）

<a id="details"></a>

心跳（Heartbeat）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fhb_5Fpub"></a>

```c
struct bt_mesh_hb_pub
```

相关声明：[bt_mesh_hb_pub](../bluetooth_mesh_model_reference/P063_bt_mesh_hb_pub_结构体.md)。

心跳发布（Heartbeat Publication）的参数。

<a id="r_bt_5Fmesh_5Fhb_5Fsub"></a>

```c
struct bt_mesh_hb_sub
```

相关声明：[bt_mesh_hb_sub](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md)。

心跳订阅（Heartbeat Subscription）的参数。

<a id="r_bt_5Fmesh_5Fhb_5Fcb"></a>

```c
struct bt_mesh_hb_cb
```

相关声明：[bt_mesh_hb_cb](../bluetooth_mesh_model_reference/P062_bt_mesh_hb_cb_结构体.md)。

心跳（Heartbeat）的回调结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_ga517f009151a7eeaa898a853fd0d7a93a"></a>

```c
#define BT_MESH_HB_CB_DEFINE(_name)
```

相关声明：[BT_MESH_HB_CB_DEFINE](#ga517f009151a7eeaa898a853fd0d7a93a)。

注册用于心跳事件（Heartbeat Events）的回调结构体（Callback Structure）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.3\_函数（Functions）

<a id="r_ga2e95d8f9d75f1bea13a9584d201fd713"></a>

```c
void bt_mesh_hb_pub_get (struct bt_mesh_hb_pub *get)
```

相关声明：[bt_mesh_hb_pub_get](#ga2e95d8f9d75f1bea13a9584d201fd713)、[bt_mesh_hb_pub](../bluetooth_mesh_model_reference/P063_bt_mesh_hb_pub_结构体.md)。

获取当前心跳发布参数（Heartbeat Publication Parameters）。

<a id="r_ga3013c3da6cc1a34b0c98c56fba7e7877"></a>

```c
void bt_mesh_hb_sub_get (struct bt_mesh_hb_sub *get)
```

相关声明：[bt_mesh_hb_sub_get](#ga3013c3da6cc1a34b0c98c56fba7e7877)、[bt_mesh_hb_sub](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md)。

获取当前心跳订阅参数（Heartbeat Subscription Parameters）。

## 3.4\_详细说明（Detailed Documentation）

<a id="ga517f009151a7eeaa898a853fd0d7a93a"></a>

### `BT_MESH_HB_CB_DEFINE`

```c
#define BT_MESH_HB_CB_DEFINE ( _name)
```

```c
#include <zephyr/bluetooth/mesh/heartbeat.h>
```

展开值（Value）：

```c
static const STRUCT_SECTION_ITERABLE(bt_mesh_hb_cb, _name)
```

注册用于心跳事件（Heartbeat Events）的回调结构体（Callback Structure）。

注册回调结构体（Callback Structure），每当发生心跳事件（Heartbeat Events）时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 回调结构体名称（Callback Structure Name）。 |

<a id="ga2e95d8f9d75f1bea13a9584d201fd713"></a>

### `bt_mesh_hb_pub_get()`

```c
void bt_mesh_hb_pub_get ( struct bt_mesh_hb_pub * get)
```

```c
#include <zephyr/bluetooth/mesh/heartbeat.h>
```

获取当前心跳发布参数（Heartbeat Publication Parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `get` | 用于返回心跳发布参数（Heartbeat Publication Parameters）的缓冲区（Buffer）。 |

<a id="ga3013c3da6cc1a34b0c98c56fba7e7877"></a>

### `bt_mesh_hb_sub_get()`

```c
void bt_mesh_hb_sub_get ( struct bt_mesh_hb_sub * get)
```

```c
#include <zephyr/bluetooth/mesh/heartbeat.h>
```

获取当前心跳订阅参数（Heartbeat Subscription Parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `get` | 用于返回心跳订阅参数（Heartbeat Subscription Parameters）的缓冲区（Buffer）。 |


## 3.5\_原页交叉引用（Cross References）

- [bt_mesh_hb_pub](../bluetooth_mesh_model_reference/P063_bt_mesh_hb_pub_结构体.md)
- [bt_mesh_hb_sub](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md)
- [bt_mesh_hb_cb](../bluetooth_mesh_model_reference/P062_bt_mesh_hb_cb_结构体.md)
- [zephyr/bluetooth/mesh/heartbeat.h](../api_file_runtime_reference/P020_zephyr__bluetooth__mesh__heartbeat.h_文件参考.md)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructbt__mesh__hb__cb_html"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_蓝牙 Mesh BLOB 闪存数据流（Flash stream）.md) · [返回大纲](大纲.md) · [下一章](P004_微芯（Microchip）SAM 电源管理控制器（PMC）.md)
