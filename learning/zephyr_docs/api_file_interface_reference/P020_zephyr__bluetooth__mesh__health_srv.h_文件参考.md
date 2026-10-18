---
id: learning.zephyr-docs.api-file-interface-reference.page-20
title: zephyr__bluetooth__mesh__health_srv.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/health__srv_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_zephyr\_\_bluetooth\_\_mesh\_\_health\_srv.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/health__srv_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

健康服务器模型（Health Server Model）的API。

<a id="details"></a>

```c
#include <zephyr/bluetooth/mesh.h>
#include <zephyr/bluetooth/byteorder.h>
```

查看此文件的源码。

健康服务器模型（Health Server Model）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 20.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fhealth_5Fsrv_5Fcb"></a>

```c
struct bt_mesh_health_srv_cb
```

相关声明：[bt_mesh_health_srv_cb](../bluetooth_mesh_model_reference/P067_bt_mesh_health_srv_cb_结构体.md)。

健康服务器（Health Server）模型的回调函数。

<a id="r_bt_5Fmesh_5Fhealth_5Fsrv"></a>

```c
struct bt_mesh_health_srv
```

相关声明：[bt_mesh_health_srv](../bluetooth_mesh_model_reference/P066_bt_mesh_health_srv_结构体.md)。

Mesh健康服务器（Health Server）的模型上下文。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 20.2\_宏定义（Macros）

<a id="r_ga35c500e915092ec365862b11e76f92ad"></a>

```c
#define BT_MESH_HEALTH_PUB_DEFINE(_name, _max_faults)
```

相关声明：[BT_MESH_HEALTH_PUB_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html#ga35c500e915092ec365862b11e76f92ad)。

用于定义健康状态发布上下文（health publication context）的辅助宏。

<a id="r_gafcab7a9c9264c52f42b5409ccad1c931"></a>

```c
#define BT_MESH_MODEL_HEALTH_SRV(srv, pub, ...)
```

相关声明：[BT_MESH_MODEL_HEALTH_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html#gafcab7a9c9264c52f42b5409ccad1c931)。

定义一个新的健康服务器模型（Health Server model）。

<a id="r_ga240e4632cdf7c425d4beec3c6a290306"></a>

```c
#define BT_MESH_HEALTH_TEST_INFO_METADATA_ID 0x0000
```

相关声明：[BT_MESH_HEALTH_TEST_INFO_METADATA_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html#ga240e4632cdf7c425d4beec3c6a290306)。

健康测试信息（Health Test Information）的元数据 ID。

<a id="r_ga37a52318699187a92de82d45dccf325d"></a>

```c
#define BT_MESH_HEALTH_TEST_INFO_METADATA(tests)
```

相关声明：[BT_MESH_HEALTH_TEST_INFO_METADATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html#ga37a52318699187a92de82d45dccf325d)。

<a id="r_ga29ca643e811a2c4f03eca7fed8d1cf4d"></a>

```c
#define BT_MESH_HEALTH_TEST_INFO(cid, tests...)
```

相关声明：[BT_MESH_HEALTH_TEST_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html#ga29ca643e811a2c4f03eca7fed8d1cf4d)。

定义健康测试信息元数据（Health Test Info Metadata）数组。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 20.3\_函数（Functions）

<a id="r_gad04789eb167b61d5ff19827c560ceb6e"></a>

```c
int bt_mesh_health_srv_fault_update (const struct bt_mesh_elem *elem)
```

相关声明：[bt_mesh_health_srv_fault_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html#gad04789eb167b61d5ff19827c560ceb6e)、[bt_mesh_elem](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md)。

通知协议栈（stack）：指定元素（element）的故障数组（fault array）状态已发生变化。


## 20.4\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh.h](../api_source_reference/P514_mesh.h_源码浏览.md)
- [zephyr/bluetooth/byteorder.h](../byteorder_reference/P005_蓝牙字节序头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P316_health_srv.h_源码浏览.md)
- [bt_mesh_health_srv_cb](../bluetooth_mesh_model_reference/P067_bt_mesh_health_srv_cb_结构体.md)
- [bt_mesh_health_srv](../bluetooth_mesh_model_reference/P066_bt_mesh_health_srv_结构体.md)
- [BT_MESH_HEALTH_PUB_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html#ga35c500e915092ec365862b11e76f92ad)
- [BT_MESH_MODEL_HEALTH_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html#gafcab7a9c9264c52f42b5409ccad1c931)
- [BT_MESH_HEALTH_TEST_INFO_METADATA_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html#ga240e4632cdf7c425d4beec3c6a290306)
- [BT_MESH_HEALTH_TEST_INFO_METADATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html#ga37a52318699187a92de82d45dccf325d)
- [BT_MESH_HEALTH_TEST_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html#ga29ca643e811a2c4f03eca7fed8d1cf4d)
- [bt_mesh_health_srv_fault_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html#gad04789eb167b61d5ff19827c560ceb6e)
- [bt_mesh_elem](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md)

<a id="header-details"></a>

---

[上一章](P019_zephyr__drivers__bluetooth__hci_lockstep.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P021_zephyr__bluetooth__services__ias.h_文件参考.md)
