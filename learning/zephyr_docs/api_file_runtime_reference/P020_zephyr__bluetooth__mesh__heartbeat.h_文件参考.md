---
id: learning.zephyr-docs.api-file-runtime-reference.page-20
title: zephyr__bluetooth__mesh__heartbeat.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/heartbeat_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_zephyr\_\_bluetooth\_\_mesh\_\_heartbeat.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/heartbeat_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

心跳（Heartbeat）的API。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

心跳（Heartbeat）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 20.1\_数据结构（Data Structures）

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

## 20.2\_宏定义（Macros）

<a id="r_ga517f009151a7eeaa898a853fd0d7a93a"></a>

```c
#define BT_MESH_HB_CB_DEFINE(_name)
```

相关声明：[BT_MESH_HB_CB_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__heartbeat.html#ga517f009151a7eeaa898a853fd0d7a93a)。

注册用于心跳事件（Heartbeat Events）的回调结构体（Callback Structure）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 20.3\_函数（Functions）

<a id="r_ga2e95d8f9d75f1bea13a9584d201fd713"></a>

```c
void bt_mesh_hb_pub_get (struct bt_mesh_hb_pub *get)
```

相关声明：[bt_mesh_hb_pub_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__heartbeat.html#ga2e95d8f9d75f1bea13a9584d201fd713)、[bt_mesh_hb_pub](../bluetooth_mesh_model_reference/P063_bt_mesh_hb_pub_结构体.md)。

获取当前心跳发布参数（Heartbeat Publication Parameters）。

<a id="r_ga3013c3da6cc1a34b0c98c56fba7e7877"></a>

```c
void bt_mesh_hb_sub_get (struct bt_mesh_hb_sub *get)
```

相关声明：[bt_mesh_hb_sub_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__heartbeat.html#ga3013c3da6cc1a34b0c98c56fba7e7877)、[bt_mesh_hb_sub](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md)。

获取当前心跳订阅参数（Heartbeat Subscription Parameters）。


## 20.4\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P317_heartbeat.h_源码浏览.md)
- [bt_mesh_hb_pub](../bluetooth_mesh_model_reference/P063_bt_mesh_hb_pub_结构体.md)
- [bt_mesh_hb_sub](../bluetooth_mesh_model_reference/P064_bt_mesh_hb_sub_结构体.md)
- [bt_mesh_hb_cb](../bluetooth_mesh_model_reference/P062_bt_mesh_hb_cb_结构体.md)
- [BT_MESH_HB_CB_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__heartbeat.html#ga517f009151a7eeaa898a853fd0d7a93a)
- [bt_mesh_hb_pub_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__heartbeat.html#ga2e95d8f9d75f1bea13a9584d201fd713)
- [bt_mesh_hb_sub_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__heartbeat.html#ga3013c3da6cc1a34b0c98c56fba7e7877)

<a id="header-details"></a>

---

[上一章](P019_zephyr__drivers__i3c__hdr_ddr.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P021_zephyr__drivers__sensor__hx711.h_文件参考.md)
