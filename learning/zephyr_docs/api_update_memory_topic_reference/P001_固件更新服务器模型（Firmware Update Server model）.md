---
id: learning.zephyr-docs.api-update-memory-topic-reference.page-1
title: 固件更新服务器模型（Firmware Update Server model）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_固件更新服务器模型（Firmware Update Server model）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙 Mesh 固件更新服务器模型的 API。

<a id="details"></a>

蓝牙 Mesh 固件更新服务器模型的 API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fdfu_5Fsrv_5Fcb"></a>

```c
struct bt_mesh_dfu_srv_cb
```

相关声明：[bt_mesh_dfu_srv_cb](../bluetooth_mesh_model_reference/P056_bt_mesh_dfu_srv_cb_结构体.md)。

固件更新服务器（Firmware Update Server）的事件回调。

<a id="r_bt_5Fmesh_5Fdfu_5Fsrv"></a>

```c
struct bt_mesh_dfu_srv
```

相关声明：[bt_mesh_dfu_srv](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md)。

固件更新服务器（Firmware Update Server）的实例。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_ga8467cd5241dfdcd7add718bbaae6fa60"></a>

```c
#define BT_MESH_DFU_SRV_INIT(_handlers, _imgs, _img_count)
```

相关声明：[BT_MESH_DFU_SRV_INIT](#ga8467cd5241dfdcd7add718bbaae6fa60)。

固件更新服务器模型（Firmware Update Server Model）的初始化参数。

<a id="r_gafdf78cc0f99668d38df4f29138392632"></a>

```c
#define BT_MESH_MODEL_DFU_SRV(_srv)
```

相关声明：[BT_MESH_MODEL_DFU_SRV](#gafdf78cc0f99668d38df4f29138392632)。

固件更新服务器模型（Firmware Update Server Model）条目。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.3\_函数（Functions）

<a id="r_ga64eeb5bfe9bac8c1120c5e0aa9ce02ac"></a>

```c
void bt_mesh_dfu_srv_verified (struct bt_mesh_dfu_srv *srv)
```

相关声明：[bt_mesh_dfu_srv_verified](#ga64eeb5bfe9bac8c1120c5e0aa9ce02ac)、[bt_mesh_dfu_srv](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md)。

接受已接收的设备固件更新（DFU）传输。

<a id="r_ga77142a1f3cfe2ff1d53332114f977b38"></a>

```c
void bt_mesh_dfu_srv_rejected (struct bt_mesh_dfu_srv *srv)
```

相关声明：[bt_mesh_dfu_srv_rejected](#ga77142a1f3cfe2ff1d53332114f977b38)、[bt_mesh_dfu_srv](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md)。

拒绝已接收的设备固件更新（DFU）传输。

<a id="r_gaf5a00dd89faf52cd7797c54c572e1211"></a>

```c
void bt_mesh_dfu_srv_cancel (struct bt_mesh_dfu_srv *srv)
```

相关声明：[bt_mesh_dfu_srv_cancel](#gaf5a00dd89faf52cd7797c54c572e1211)、[bt_mesh_dfu_srv](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md)。

取消正在进行的设备固件更新（DFU）传输。

<a id="r_ga45aef92fe1de4c45ccb5369c1f5222ee"></a>

```c
void bt_mesh_dfu_srv_applied (struct bt_mesh_dfu_srv *srv)
```

相关声明：[bt_mesh_dfu_srv_applied](#ga45aef92fe1de4c45ccb5369c1f5222ee)、[bt_mesh_dfu_srv](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md)。

确认已应用收到的设备固件更新（DFU）传输内容。

<a id="r_ga94107fb1ca9207fc6918eae1fb1b3755"></a>

```c
bool bt_mesh_dfu_srv_is_busy (const struct bt_mesh_dfu_srv *srv)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_dfu_srv_is_busy](#ga94107fb1ca9207fc6918eae1fb1b3755)、[bt_mesh_dfu_srv](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md)。

检查固件更新服务器（Firmware Update Server）是否正忙于处理传输。

<a id="r_ga9f125ace97a40f060e0d8c59fd49f514"></a>

```c
uint8_t bt_mesh_dfu_srv_progress (const struct bt_mesh_dfu_srv *srv)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_dfu_srv_progress](#ga9f125ace97a40f060e0d8c59fd49f514)、[bt_mesh_dfu_srv](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md)。

获取当前设备固件更新（DFU）过程的进度，单位为百分比。

## 1.4\_详细说明（Detailed Documentation）

<a id="ga8467cd5241dfdcd7add718bbaae6fa60"></a>

### `BT_MESH_DFU_SRV_INIT`

```c
#define BT_MESH_DFU_SRV_INIT ( _handlers, _imgs, _img_count )
```

```c
#include <zephyr/bluetooth/mesh/dfu_srv.h>
```

展开值（Value）：

```c
{                                                                      \
        .blob = { .cb = &_bt_mesh_dfu_srv_blob_cb }, .cb = _handlers,  \
        .imgs = _imgs, .img_count = _img_count,                        \
}
```

固件更新服务器模型（Firmware Update Server Model）的初始化参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_handlers` | 设备固件更新（DFU）处理函数结构体。 |
| `_imgs` | 此服务器管理的 `bt_mesh_dfu_img` 列表。 |
| `_img_count` | 此服务器管理的设备固件更新（DFU）镜像数量。 |

<a id="gafdf78cc0f99668d38df4f29138392632"></a>

### `BT_MESH_MODEL_DFU_SRV`

```c
#define BT_MESH_MODEL_DFU_SRV ( _srv)
```

```c
#include <zephyr/bluetooth/mesh/dfu_srv.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_BLOB_SRV(&(_srv)->blob),                                  \
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_DFU_SRV, _bt_mesh_dfu_srv_op, NULL,  \
                 _srv, &_bt_mesh_dfu_srv_cb)
```

固件更新服务器模型（Firmware Update Server Model）条目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_srv` | 指向固件更新服务器模型（Firmware Update Server Model）实例的指针。 |

<a id="ga45aef92fe1de4c45ccb5369c1f5222ee"></a>

### `bt_mesh_dfu_srv_applied()`

```c
void bt_mesh_dfu_srv_applied ( struct bt_mesh_dfu_srv * srv)
```

```c
#include <zephyr/bluetooth/mesh/dfu_srv.h>
```

确认已应用收到的设备固件更新（DFU）传输内容。

应在处理 `bt_mesh_dfu_srv_cb::apply` 回调时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 固件更新服务器（Firmware Update Server）的实例。 |

<a id="gaf5a00dd89faf52cd7797c54c572e1211"></a>

### `bt_mesh_dfu_srv_cancel()`

```c
void bt_mesh_dfu_srv_cancel ( struct bt_mesh_dfu_srv * srv)
```

```c
#include <zephyr/bluetooth/mesh/dfu_srv.h>
```

取消正在进行的设备固件更新（DFU）传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 固件更新服务器（Firmware Update Server）的实例。 |

<a id="ga94107fb1ca9207fc6918eae1fb1b3755"></a>

### `bt_mesh_dfu_srv_is_busy()`

```c
bool bt_mesh_dfu_srv_is_busy ( const struct bt_mesh_dfu_srv * srv)
```

```c
#include <zephyr/bluetooth/mesh/dfu_srv.h>
```

检查固件更新服务器（Firmware Update Server）是否正忙于处理传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 固件更新服务器（Firmware Update Server）的实例。 |

**返回（Returns）**：**返回值（Returns）：**设备固件更新（DFU）过程正在进行时返回 `true`，否则返回 `false`。

<a id="ga9f125ace97a40f060e0d8c59fd49f514"></a>

### `bt_mesh_dfu_srv_progress()`

```c
uint8_t bt_mesh_dfu_srv_progress ( const struct bt_mesh_dfu_srv * srv)
```

```c
#include <zephyr/bluetooth/mesh/dfu_srv.h>
```

获取当前设备固件更新（DFU）过程的进度，单位为百分比。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 固件更新服务器（Firmware Update Server）的实例。 |

**返回（Returns）**：**返回值（Returns）：**当前传输进度，单位为百分比。

<a id="ga77142a1f3cfe2ff1d53332114f977b38"></a>

### `bt_mesh_dfu_srv_rejected()`

```c
void bt_mesh_dfu_srv_rejected ( struct bt_mesh_dfu_srv * srv)
```

```c
#include <zephyr/bluetooth/mesh/dfu_srv.h>
```

拒绝已接收的设备固件更新（DFU）传输。

应在设备固件更新（DFU）传输成功结束时调用。

若设备固件更新（DFU）传输成功完成，应用程序应验证镜像有效性，包括镜像认证（Authentication）和完整性检查（Integrity Checks）；若任一检查失败，应调用本函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 固件更新服务器（Firmware Update Server）的实例。 |

<a id="ga64eeb5bfe9bac8c1120c5e0aa9ce02ac"></a>

### `bt_mesh_dfu_srv_verified()`

```c
void bt_mesh_dfu_srv_verified ( struct bt_mesh_dfu_srv * srv)
```

```c
#include <zephyr/bluetooth/mesh/dfu_srv.h>
```

接受已接收的设备固件更新（DFU）传输。

应在设备固件更新（DFU）传输成功结束时调用。

若设备固件更新（DFU）传输成功完成，应用程序应验证镜像有效性，包括镜像认证（Authentication）和完整性检查（Integrity Checks）；若镜像已可应用，应调用本函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 固件更新服务器（Firmware Update Server）的实例。 |


## 1.5\_原页交叉引用（Cross References）

- [bt_mesh_dfu_srv_cb](../bluetooth_mesh_model_reference/P056_bt_mesh_dfu_srv_cb_结构体.md)
- [bt_mesh_dfu_srv](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md)
- [固件更新服务器模型（Firmware Update Server model）](P001_固件更新服务器模型（Firmware Update Server model）.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/bluetooth/mesh/dfu_srv.h](../api_file_service_interface_reference/P014_zephyr__bluetooth__mesh__dfu_srv.h_文件参考.md)
- [bt_mesh_dfu_img](../bluetooth_mesh_model_reference/P050_bt_mesh_dfu_img_结构体.md)
- [BT_MESH_MODEL_BLOB_SRV](../api_connection_topic_reference/P005_蓝牙 Mesh 二进制大对象（BLOB）传输服务器模型 API.md#gad9db3253c13d50cfb6c89dff881dbfe9)
- [BT_MESH_MODEL_ID_DFU_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#ga0215c2c8cd16ab6536ea243864f9604e)
- [bt_mesh_dfu_srv_cb::apply](../bluetooth_mesh_model_reference/P056_bt_mesh_dfu_srv_cb_结构体.md#afe4b6ca9f56938695addba6ecc18bb4b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_ga0215c2c8cd16ab6536ea243864f9604e"></a>
<a id="agroup__bt__mesh__blob__srv_html_gad9db3253c13d50cfb6c89dff881dbfe9"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_大型组成数据客户端模型（Large Composition Data Client model）.md)
