---
id: learning.zephyr-docs.api-extension-topic-reference.page-4
title: 固件分发服务器模型（Firmware Distribution Server model）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd__srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_固件分发服务器模型（Firmware Distribution Server model）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd__srv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

固件分发服务器模型的 API。

<a id="details"></a>

固件分发服务器模型的 API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fdfd_5Fsrv_5Fcb"></a>

```c
struct bt_mesh_dfd_srv_cb
```

相关声明：[bt_mesh_dfd_srv_cb](../bluetooth_mesh_model_reference/P045_bt_mesh_dfd_srv_cb_结构体.md)。

固件分发服务器（Firmware Distribution Server）的回调：

<a id="r_bt_5Fmesh_5Fdfd_5Fsrv"></a>

```c
struct bt_mesh_dfd_srv
```

相关声明：[bt_mesh_dfd_srv](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md)。

固件分发服务器（Firmware Distribution Server）的实例。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_ga126e2d4df8f58b7de36da46c14b2c804"></a>

```c
#define CONFIG_BT_MESH_DFD_SRV_TARGETS_MAX 0
```

相关声明：[CONFIG_BT_MESH_DFD_SRV_TARGETS_MAX](#ga126e2d4df8f58b7de36da46c14b2c804)。

<a id="r_gab26590917c9de6edaccf07540c88f7c1"></a>

```c
#define CONFIG_BT_MESH_DFD_SRV_SLOT_MAX_SIZE 0
```

相关声明：[CONFIG_BT_MESH_DFD_SRV_SLOT_MAX_SIZE](#gab26590917c9de6edaccf07540c88f7c1)。

<a id="r_ga394c367492c72f66231b5cf3e2789f5f"></a>

```c
#define CONFIG_BT_MESH_DFD_SRV_SLOT_SPACE 0
```

相关声明：[CONFIG_BT_MESH_DFD_SRV_SLOT_SPACE](#ga394c367492c72f66231b5cf3e2789f5f)。

<a id="r_ga20b1232269b2e859608c21e84305196c"></a>

```c
#define BT_MESH_DFD_SRV_INIT(_cb)
```

相关声明：[BT_MESH_DFD_SRV_INIT](#ga20b1232269b2e859608c21e84305196c)。

固件分发服务器模型（Firmware Distribution Server Model）的初始化参数（Initialization Parameters）。

<a id="r_ga27457d4d72119ab080828359d43ad6cf"></a>

```c
#define BT_MESH_MODEL_DFD_SRV(_srv)
```

相关声明：[BT_MESH_MODEL_DFD_SRV](#ga27457d4d72119ab080828359d43ad6cf)。

固件分发服务器模型（Firmware Distribution Server Model）的组成数据条目（Composition Data Entry）。

## 4.3\_详细说明（Detailed Documentation）

<a id="ga20b1232269b2e859608c21e84305196c"></a>

### `BT_MESH_DFD_SRV_INIT`

```c
#define BT_MESH_DFD_SRV_INIT ( _cb)
```

```c
#include <zephyr/bluetooth/mesh/dfd_srv.h>
```

展开值（Value）：

```c
{                                                                      \
        .cb = _cb,                                                     \
        .dfu = BT_MESH_DFU_CLI_INIT(&_bt_mesh_dfd_srv_dfu_cb),         \
        .upload = {                                                    \
                .blob = { .cb = &_bt_mesh_dfd_srv_blob_cb },           \
        },                                                             \
}
```

固件分发服务器模型（Firmware Distribution Server Model）的初始化参数（Initialization Parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] _cb` | 指向 `bt_mesh_dfd_srv_cb` 实例（Instance）的指针（Pointer）。 |

<a id="ga27457d4d72119ab080828359d43ad6cf"></a>

### `BT_MESH_MODEL_DFD_SRV`

```c
#define BT_MESH_MODEL_DFD_SRV ( _srv)
```

```c
#include <zephyr/bluetooth/mesh/dfd_srv.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_DFU_CLI(&(_srv)->dfu),                                   \
BT_MESH_MODEL_BLOB_SRV(&(_srv)->upload.blob),                          \
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_DFD_SRV, _bt_mesh_dfd_srv_op, NULL,  \
                 _srv, &_bt_mesh_dfd_srv_cb)
```

固件分发服务器模型（Firmware Distribution Server Model）的组成数据条目（Composition Data Entry）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_srv` | 指向固件分发服务器模型实例（Firmware Distribution Server Model Instance）的指针（Pointer）。 |

<a id="gab26590917c9de6edaccf07540c88f7c1"></a>

### `CONFIG_BT_MESH_DFD_SRV_SLOT_MAX_SIZE`

```c
#define CONFIG_BT_MESH_DFD_SRV_SLOT_MAX_SIZE 0
```

```c
#include <zephyr/bluetooth/mesh/dfd_srv.h>
```

<a id="ga394c367492c72f66231b5cf3e2789f5f"></a>

### `CONFIG_BT_MESH_DFD_SRV_SLOT_SPACE`

```c
#define CONFIG_BT_MESH_DFD_SRV_SLOT_SPACE 0
```

```c
#include <zephyr/bluetooth/mesh/dfd_srv.h>
```

<a id="ga126e2d4df8f58b7de36da46c14b2c804"></a>

### `CONFIG_BT_MESH_DFD_SRV_TARGETS_MAX`

```c
#define CONFIG_BT_MESH_DFD_SRV_TARGETS_MAX 0
```

```c
#include <zephyr/bluetooth/mesh/dfd_srv.h>
```


## 4.4\_原页交叉引用（Cross References）

- [bt_mesh_dfd_srv_cb](../bluetooth_mesh_model_reference/P045_bt_mesh_dfd_srv_cb_结构体.md)
- [bt_mesh_dfd_srv](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md)
- [固件分发服务器模型（Firmware Distribution Server model）](P004_固件分发服务器模型（Firmware Distribution Server model）.md)
- [zephyr/bluetooth/mesh/dfd_srv.h](../api_file_configuration_reference/P015_zephyr__bluetooth__mesh__dfd_srv.h_文件参考.md)
- [BT_MESH_DFU_CLI_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga0b10a95f9b7c806bfd8649280f535c96)
- [BT_MESH_MODEL_DFU_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#gadee3710bb46d907a51232ca42cca7c2d)
- [BT_MESH_MODEL_ID_DFD_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#gaf4309dea32d05274f8f3a6ea45faba38)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__mesh__dfu__cli_html_ga0b10a95f9b7c806bfd8649280f535c96"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_gaf4309dea32d05274f8f3a6ea45faba38"></a>
<a id="agroup__bt__mesh__dfu__cli_html_gadee3710bb46d907a51232ca42cca7c2d"></a>

---

[上一章](P003_桥接配置公共头文件（Bridge Configuration common header）.md) · [返回大纲](大纲.md) · [下一章](P005_瑞昱（Realtek）BEE.md)
