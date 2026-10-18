---
id: learning.zephyr-docs.api-file-management-reference.page-2
title: zephyr__bluetooth__mesh__blob_srv.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/blob__srv_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_bluetooth\_\_mesh\_\_blob\_srv.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/blob__srv_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh BLOB传输服务器（Transfer Server）模型API的头文件。

<a id="details"></a>

```c
#include <zephyr/bluetooth/mesh/access.h>
#include <zephyr/bluetooth/mesh/blob.h>
```

查看此文件的源码。

蓝牙Mesh BLOB传输服务器（Transfer Server）模型API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fblob_5Fsrv_5Fcb"></a>

```c
struct bt_mesh_blob_srv_cb
```

相关声明：[bt_mesh_blob_srv_cb](../bluetooth_mesh_model_reference/P011_bt_mesh_blob_srv_cb_结构体.md)。

BLOB传输服务器（BLOB Transfer Server）模型的事件处理程序。

<a id="r_bt_5Fmesh_5Fblob_5Fsrv"></a>

```c
struct bt_mesh_blob_srv
```

相关声明：[bt_mesh_blob_srv](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md)。

BLOB传输服务器（BLOB Transfer Server）的模型实例。

<a id="r_bt_5Fmesh_5Fblob_5Fsrv_3A_3Abt_5Fmesh_5Fblob_5Fsrv_5Fstate"></a>

```c
struct bt_mesh_blob_srv::bt_mesh_blob_srv_state
```

相关声明：[bt_mesh_blob_srv::bt_mesh_blob_srv_state](../bluetooth_mesh_model_reference/P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_gaae3dfbf15f33739bc0a42c924de99cba"></a>

```c
#define BT_MESH_BLOB_BLOCKS_MAX 1
```

相关声明：[BT_MESH_BLOB_BLOCKS_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html#gaae3dfbf15f33739bc0a42c924de99cba)。

单次传输的最大块数（blocks）。

<a id="r_gad9db3253c13d50cfb6c89dff881dbfe9"></a>

```c
#define BT_MESH_MODEL_BLOB_SRV(_srv)
```

相关声明：[BT_MESH_MODEL_BLOB_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html#gad9db3253c13d50cfb6c89dff881dbfe9)。

二进制大对象传输服务器（BLOB Transfer Server）模型的组成数据条目（composition data entry）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.3\_函数（Functions）

<a id="r_ga5d35f13eeb6f7a1fb252e8fb905e9cb3"></a>

```c
int bt_mesh_blob_srv_recv (struct bt_mesh_blob_srv *srv, uint64_t id, const struct bt_mesh_blob_io *io, uint8_t ttl, uint16_t timeout_base)
```

相关声明：[bt_mesh_blob_srv_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html#ga5d35f13eeb6f7a1fb252e8fb905e9cb3)、[bt_mesh_blob_srv](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

准备 BLOB 传输服务器，以接收即将到来的传输。

<a id="r_gae8739e96f2157f588072e91b51891835"></a>

```c
int bt_mesh_blob_srv_cancel (struct bt_mesh_blob_srv *srv)
```

相关声明：[bt_mesh_blob_srv_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html#gae8739e96f2157f588072e91b51891835)、[bt_mesh_blob_srv](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md)。

取消当前 BLOB 传输。

<a id="r_gaa7a253c9a577eaa1307bc0e6b93a3d66"></a>

```c
bool bt_mesh_blob_srv_is_busy (const struct bt_mesh_blob_srv *srv)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_blob_srv_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html#gaa7a253c9a577eaa1307bc0e6b93a3d66)、[bt_mesh_blob_srv](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md)。

获取 BLOB 传输服务器的当前状态。

<a id="r_ga674b59ff721575539818ef74e8d1b91c"></a>

```c
uint8_t bt_mesh_blob_srv_progress (const struct bt_mesh_blob_srv *srv)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_blob_srv_progress](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html#ga674b59ff721575539818ef74e8d1b91c)、[bt_mesh_blob_srv](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md)。

获取当前活动传输的进度，以百分比表示。


## 2.4\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/access.h](../api_source_compiler_device_reference/P001_access.h_源码浏览.md)
- [zephyr/bluetooth/mesh/blob.h](../api_source_reference/P068_blob.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P002_blob_srv.h_源码浏览.md)
- [bt_mesh_blob_srv_cb](../bluetooth_mesh_model_reference/P011_bt_mesh_blob_srv_cb_结构体.md)
- [bt_mesh_blob_srv](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md)
- [bt_mesh_blob_srv::bt_mesh_blob_srv_state](../bluetooth_mesh_model_reference/P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md)
- [BT_MESH_BLOB_BLOCKS_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html#gaae3dfbf15f33739bc0a42c924de99cba)
- [BT_MESH_MODEL_BLOB_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html#gad9db3253c13d50cfb6c89dff881dbfe9)
- [bt_mesh_blob_srv_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html#ga5d35f13eeb6f7a1fb252e8fb905e9cb3)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_blob_srv_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html#gae8739e96f2157f588072e91b51891835)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_mesh_blob_srv_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html#gaa7a253c9a577eaa1307bc0e6b93a3d66)
- [bt_mesh_blob_srv_progress](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html#ga674b59ff721575539818ef74e8d1b91c)

<a id="header-details"></a>

---

[上一章](P001_zephyr__bluetooth__audio__ascs.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__mgmt__mcumgr__mgmt__callbacks.h_文件参考.md)
