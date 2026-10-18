---
id: learning.zephyr-docs.api-connection-topic-reference.page-5
title: 蓝牙 Mesh 二进制大对象（BLOB）传输服务器模型 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_蓝牙 Mesh 二进制大对象（BLOB）传输服务器模型 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__srv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 5.1\_文件（Files）

<a id="r_blob_5Fsrv_2Eh"></a>

```c
file blob_srv.h
```

相关声明：[blob_srv.h](../api_file_management_reference/P002_zephyr__bluetooth__mesh__blob_srv.h_文件参考.md)。

蓝牙Mesh BLOB传输服务器（Transfer Server）模型API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.2\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.3\_宏定义（Macros）

<a id="r_gaae3dfbf15f33739bc0a42c924de99cba"></a>

```c
#define BT_MESH_BLOB_BLOCKS_MAX 1
```

相关声明：[BT_MESH_BLOB_BLOCKS_MAX](#gaae3dfbf15f33739bc0a42c924de99cba)。

单次传输的最大块数（blocks）。

<a id="r_gad9db3253c13d50cfb6c89dff881dbfe9"></a>

```c
#define BT_MESH_MODEL_BLOB_SRV(_srv)
```

相关声明：[BT_MESH_MODEL_BLOB_SRV](#gad9db3253c13d50cfb6c89dff881dbfe9)。

二进制大对象传输服务器（BLOB Transfer Server）模型的组成数据条目（composition data entry）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.4\_函数（Functions）

<a id="r_ga5d35f13eeb6f7a1fb252e8fb905e9cb3"></a>

```c
int bt_mesh_blob_srv_recv (struct bt_mesh_blob_srv *srv, uint64_t id, const struct bt_mesh_blob_io *io, uint8_t ttl, uint16_t timeout_base)
```

相关声明：[bt_mesh_blob_srv_recv](#ga5d35f13eeb6f7a1fb252e8fb905e9cb3)、[bt_mesh_blob_srv](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

准备 BLOB 传输服务器，以接收即将到来的传输。

<a id="r_gae8739e96f2157f588072e91b51891835"></a>

```c
int bt_mesh_blob_srv_cancel (struct bt_mesh_blob_srv *srv)
```

相关声明：[bt_mesh_blob_srv_cancel](#gae8739e96f2157f588072e91b51891835)、[bt_mesh_blob_srv](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md)。

取消当前 BLOB 传输。

<a id="r_gaa7a253c9a577eaa1307bc0e6b93a3d66"></a>

```c
bool bt_mesh_blob_srv_is_busy (const struct bt_mesh_blob_srv *srv)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_blob_srv_is_busy](#gaa7a253c9a577eaa1307bc0e6b93a3d66)、[bt_mesh_blob_srv](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md)。

获取 BLOB 传输服务器的当前状态。

<a id="r_ga674b59ff721575539818ef74e8d1b91c"></a>

```c
uint8_t bt_mesh_blob_srv_progress (const struct bt_mesh_blob_srv *srv)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_blob_srv_progress](#ga674b59ff721575539818ef74e8d1b91c)、[bt_mesh_blob_srv](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md)。

获取当前活动传输的进度，以百分比表示。

## 5.5\_详细说明（Detailed Documentation）

<a id="gaae3dfbf15f33739bc0a42c924de99cba"></a>

### `BT_MESH_BLOB_BLOCKS_MAX`

```c
#define BT_MESH_BLOB_BLOCKS_MAX 1
```

```c
#include <zephyr/bluetooth/mesh/blob_srv.h>
```

单次传输的最大块数（blocks）。

<a id="gad9db3253c13d50cfb6c89dff881dbfe9"></a>

### `BT_MESH_MODEL_BLOB_SRV`

```c
#define BT_MESH_MODEL_BLOB_SRV ( _srv)
```

```c
#include <zephyr/bluetooth/mesh/blob_srv.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_BLOB_SRV, _bt_mesh_blob_srv_op,      \
                 NULL, _srv, &_bt_mesh_blob_srv_cb)
```

二进制大对象传输服务器（BLOB Transfer Server）模型的组成数据条目（composition data entry）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_srv` | 指向蓝牙 Mesh 二进制大对象传输服务器（BLOB Transfer Server）模型 API 实例的指针。 |

<a id="gae8739e96f2157f588072e91b51891835"></a>

### `bt_mesh_blob_srv_cancel()`

```c
int bt_mesh_blob_srv_cancel ( struct bt_mesh_blob_srv * srv)
```

```c
#include <zephyr/bluetooth/mesh/blob_srv.h>
```

取消当前 BLOB 传输。

通知 BLOB 传输客户端，将本设备从当前传输的目标列表（Targets）中移除。注意，客户端可能继续向其他目标发送该传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 二进制大对象传输服务器实例（BLOB Transfer Server instance）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gaa7a253c9a577eaa1307bc0e6b93a3d66"></a>

### `bt_mesh_blob_srv_is_busy()`

```c
bool bt_mesh_blob_srv_is_busy ( const struct bt_mesh_blob_srv * srv)
```

```c
#include <zephyr/bluetooth/mesh/blob_srv.h>
```

获取 BLOB 传输服务器的当前状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 二进制大对象传输服务器实例（BLOB Transfer Server instance）。 |

**返回（Returns）**：返回值：BLOB 传输服务器当前正在参与传输时为 true，否则为 false。

<a id="ga674b59ff721575539818ef74e8d1b91c"></a>

### `bt_mesh_blob_srv_progress()`

```c
uint8_t bt_mesh_blob_srv_progress ( const struct bt_mesh_blob_srv * srv)
```

```c
#include <zephyr/bluetooth/mesh/blob_srv.h>
```

获取当前活动传输的进度，以百分比表示。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 二进制大对象传输服务器实例（BLOB Transfer Server instance）。 |

**返回（Returns）**：返回值：当前传输进度；没有活动传输时返回 0。

<a id="ga5d35f13eeb6f7a1fb252e8fb905e9cb3"></a>

### `bt_mesh_blob_srv_recv()`

```c
int bt_mesh_blob_srv_recv ( struct bt_mesh_blob_srv * srv, uint64_t id, const struct bt_mesh_blob_io * io, uint8_t ttl, uint16_t timeout_base )
```

```c
#include <zephyr/bluetooth/mesh/blob_srv.h>
```

准备 BLOB 传输服务器，以接收即将到来的传输。

BLOB 传输服务器接收传输之前，必须通过某种应用层机制准备该传输。服务器只接受 BLOB ID 匹配的传入传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 二进制大对象传输服务器实例（BLOB Transfer Server instance）。 |
| `id` | 要接受的 BLOB ID。 |
| `io` | 用于写入传入 BLOB 的 BLOB 流（stream）。 |
| `ttl` | 响应 BLOB 传输客户端时使用的生存时间（TTL）值。 |
| `timeout_base` | 在基本的 10 秒之外，为客户端响应额外提供的时间，以 10 秒递增。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。


## 5.6\_原页交叉引用（Cross References）

- [blob_srv.h](../api_file_management_reference/P002_zephyr__bluetooth__mesh__blob_srv.h_文件参考.md)
- [bt_mesh_blob_srv_cb](../bluetooth_mesh_model_reference/P011_bt_mesh_blob_srv_cb_结构体.md)
- [bt_mesh_blob_srv](../bluetooth_mesh_model_reference/P009_bt_mesh_blob_srv_结构体.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_ID_BLOB_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#gae85d4cf7aad4e94582c24f79d6f60904)
- [蓝牙 Mesh 二进制大对象（BLOB）传输服务器模型 API](P005_蓝牙 Mesh 二进制大对象（BLOB）传输服务器模型 API.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_gae85d4cf7aad4e94582c24f79d6f60904"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_心率服务（Heart Rate Service，HRS）.md) · [返回大纲](大纲.md) · [下一章](P006_博流智能（Bouffalo Lab）.md)
