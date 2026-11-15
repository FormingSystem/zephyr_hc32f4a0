---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-5
title: 健康服务器模型（Health Server Model）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_健康服务器模型（Health Server Model）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

健康服务器模型（Health Server Model）

<a id="details"></a>

健康服务器模型（Health Server Model）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

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

## 5.2\_宏定义（Macros）

<a id="r_ga35c500e915092ec365862b11e76f92ad"></a>

```c
#define BT_MESH_HEALTH_PUB_DEFINE(_name, _max_faults)
```

相关声明：[BT_MESH_HEALTH_PUB_DEFINE](#ga35c500e915092ec365862b11e76f92ad)。

用于定义健康状态发布上下文（health publication context）的辅助宏。

<a id="r_gafcab7a9c9264c52f42b5409ccad1c931"></a>

```c
#define BT_MESH_MODEL_HEALTH_SRV(srv, pub, ...)
```

相关声明：[BT_MESH_MODEL_HEALTH_SRV](#gafcab7a9c9264c52f42b5409ccad1c931)。

定义一个新的健康服务器模型（Health Server model）。

<a id="r_ga240e4632cdf7c425d4beec3c6a290306"></a>

```c
#define BT_MESH_HEALTH_TEST_INFO_METADATA_ID 0x0000
```

相关声明：[BT_MESH_HEALTH_TEST_INFO_METADATA_ID](#ga240e4632cdf7c425d4beec3c6a290306)。

健康测试信息（Health Test Information）的元数据 ID。

<a id="r_ga37a52318699187a92de82d45dccf325d"></a>

```c
#define BT_MESH_HEALTH_TEST_INFO_METADATA(tests)
```

相关声明：[BT_MESH_HEALTH_TEST_INFO_METADATA](#ga37a52318699187a92de82d45dccf325d)。

<a id="r_ga29ca643e811a2c4f03eca7fed8d1cf4d"></a>

```c
#define BT_MESH_HEALTH_TEST_INFO(cid, tests...)
```

相关声明：[BT_MESH_HEALTH_TEST_INFO](#ga29ca643e811a2c4f03eca7fed8d1cf4d)。

定义健康测试信息元数据（Health Test Info Metadata）数组。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.3\_函数（Functions）

<a id="r_gad04789eb167b61d5ff19827c560ceb6e"></a>

```c
int bt_mesh_health_srv_fault_update (const struct bt_mesh_elem *elem)
```

相关声明：[bt_mesh_health_srv_fault_update](#gad04789eb167b61d5ff19827c560ceb6e)、[bt_mesh_elem](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md)。

通知协议栈（stack）：指定元素（element）的故障数组（fault array）状态已发生变化。

## 5.4\_详细说明（Detailed Documentation）

<a id="ga35c500e915092ec365862b11e76f92ad"></a>

### `BT_MESH_HEALTH_PUB_DEFINE`

```c
#define BT_MESH_HEALTH_PUB_DEFINE ( _name, _max_faults )
```

```c
#include <zephyr/bluetooth/mesh/health_srv.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_PUB_DEFINE(_name, NULL, (1 + 3 + (_max_faults)))
```

用于定义健康状态发布上下文（health publication context）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 发布上下文变量（Publication Context Variable）的名称。 |
| `_max_faults` | 元素（Element）可具有的最大故障（Fault）数量。 |

<a id="ga29ca643e811a2c4f03eca7fed8d1cf4d"></a>

### `BT_MESH_HEALTH_TEST_INFO`

```c
#define BT_MESH_HEALTH_TEST_INFO ( cid, tests... )
```

```c
#include <zephyr/bluetooth/mesh/health_srv.h>
```

展开值（Value）：

```c
BT_BYTES_LIST_LE16(cid), sizeof((uint8_t[]){ tests }), tests
```

定义健康测试信息元数据（Health Test Info Metadata）数组。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cid` | 健康测试套件（Health Test Suite）的公司标识（Company ID）。 |
| `tests` | 以逗号分隔的测试列表。 |

**返回（Returns）**：**返回值（Returns）：**构成健康测试信息元数据（Health Test Info Metadata）的一组逗号分隔值。

<a id="ga37a52318699187a92de82d45dccf325d"></a>

### `BT_MESH_HEALTH_TEST_INFO_METADATA`

```c
#define BT_MESH_HEALTH_TEST_INFO_METADATA ( tests)
```

```c
#include <zephyr/bluetooth/mesh/health_srv.h>
```

展开值（Value）：

```c
{                                                                      \
        .len = ARRAY_SIZE(tests),                                      \
        .id = BT_MESH_HEALTH_TEST_INFO_METADATA_ID,                    \
        .data = tests,                                                 \
}
```

<a id="ga240e4632cdf7c425d4beec3c6a290306"></a>

### `BT_MESH_HEALTH_TEST_INFO_METADATA_ID`

```c
#define BT_MESH_HEALTH_TEST_INFO_METADATA_ID 0x0000
```

```c
#include <zephyr/bluetooth/mesh/health_srv.h>
```

健康测试信息（Health Test Information）的元数据 ID。

<a id="gafcab7a9c9264c52f42b5409ccad1c931"></a>

### `BT_MESH_MODEL_HEALTH_SRV`

```c
#define BT_MESH_MODEL_HEALTH_SRV ( srv, pub, ... )
```

```c
#include <zephyr/bluetooth/mesh/health_srv.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_METADATA_CB(BT_MESH_MODEL_ID_HEALTH_SRV,         \
                          bt_mesh_health_srv_op,               \
                          pub,                                 \
                          srv,                                 \
                          &bt_mesh_health_srv_cb, __VA_ARGS__)
```

定义一个新的健康服务器模型（Health Server model）。

应用程序希望在哪些元素上设置健康服务器模型（Health Server Model），就必须分别为每个元素调用一次此 API。每个实例还需要独立的 `bt_mesh_health_srv` 和 `bt_mesh_model_pub` 上下文。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 指向独立 `struct bt_mesh_health_srv` 的指针。 |
| `pub` | 指向独立 `struct bt_mesh_model_pub` 的指针。 |
| `...` | 若应用程序编译时支持大型组合数据服务器（Large Composition Data Server），则提供可选的健康服务器元数据（Health Server Metadata）；否则忽略此参数。 |

**返回（Returns）**：**返回值（Returns）：**新 Mesh 模型实例（Model Instance）。

<a id="gad04789eb167b61d5ff19827c560ceb6e"></a>

### `bt_mesh_health_srv_fault_update()`

```c
int bt_mesh_health_srv_fault_update ( const struct bt_mesh_elem * elem)
```

```c
#include <zephyr/bluetooth/mesh/health_srv.h>
```

通知协议栈（stack）：指定元素（element）的故障数组（fault array）状态已发生变化。

若禁用了周期性发布（Periodic Publishing），此操作提示该元素上的健康服务器发布当前故障数组（Fault Array）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `elem` | 要更新故障状态的元素（Element）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。


## 5.5\_原页交叉引用（Cross References）

- [bt_mesh_health_srv_cb](../bluetooth_mesh_model_reference/P067_bt_mesh_health_srv_cb_结构体.md)
- [bt_mesh_health_srv](../bluetooth_mesh_model_reference/P066_bt_mesh_health_srv_结构体.md)
- [bt_mesh_elem](../bluetooth_mesh_model_reference/P059_bt_mesh_elem_结构体.md)
- [zephyr/bluetooth/mesh/health_srv.h](../api_file_interface_reference/P020_zephyr__bluetooth__mesh__health_srv.h_文件参考.md)
- [BT_MESH_MODEL_PUB_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga8334ff2da1f0dc3ab2fc914059c33622)
- [BT_BYTES_LIST_LE16](../byteorder_reference/P003_蓝牙字节序辅助接口.md#ga83b5828023306b4bbf354ca3d6d6c6f2)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ARRAY_SIZE](../util_reference/P001_通用工具公共接口.md#ga70c57aae3eb654e205459b4362c8089a)
- [BT_MESH_MODEL_METADATA_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga40204b4ccaa819a487de168bcf66c98f)
- [BT_MESH_MODEL_ID_HEALTH_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#ga6416216348d7186f91175ca50bb8c903)
- [bt_mesh_model_pub](../bluetooth_mesh_model_reference/P079_bt_mesh_model_pub_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__mesh__access_html_ga8334ff2da1f0dc3ab2fc914059c33622"></a>
<a id="agroup__bt__byteorder_html_ga83b5828023306b4bbf354ca3d6d6c6f2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="agroup__bt__mesh__health__srv_html_ga240e4632cdf7c425d4beec3c6a290306"></a>
<a id="agroup__sys-util_html_ga70c57aae3eb654e205459b4362c8089a"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_ga6416216348d7186f91175ca50bb8c903"></a>
<a id="agroup__bt__mesh__access_html_ga40204b4ccaa819a487de168bcf66c98f"></a>
<a id="astructbt__mesh__health__srv__cb_html"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_蓝牙 Mesh 设备固件更新（Device Firmware Update，DFU）元数据.md) · [返回大纲](大纲.md) · [下一章](P006_瑞萨 RA BSP 时钟源常量（Clock Source Constants）.md)
