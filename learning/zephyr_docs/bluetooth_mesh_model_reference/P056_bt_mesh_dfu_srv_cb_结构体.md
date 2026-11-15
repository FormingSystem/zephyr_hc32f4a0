---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-56
title: bt_mesh_dfu_srv_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__srv__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_bt\_mesh\_dfu\_srv\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__srv__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

固件更新服务器（Firmware Update Server）的事件回调。

```c
#include <zephyr/bluetooth/mesh/dfu_srv.h>
```

<a id="details"></a>

固件更新服务器（Firmware Update Server）的事件回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 56.1\_数据成员（Data Fields）

<a id="r_afbde918804e66160ffa176c206540027"></a>

```c
int(* check )(struct bt_mesh_dfu_srv *srv, const struct bt_mesh_dfu_img *img, struct net_buf_simple *metadata, enum bt_mesh_dfu_effect *effect)
```

相关声明：[check](#afbde918804e66160ffa176c206540027)、[bt_mesh_dfu_srv](P055_bt_mesh_dfu_srv_结构体.md)、[bt_mesh_dfu_img](P050_bt_mesh_dfu_img_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[bt_mesh_dfu_effect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8)。

传输检查回调（Transfer check callback）。

<a id="r_adaefef5067cf3ea273f1db95ca536254"></a>

```c
int(* start )(struct bt_mesh_dfu_srv *srv, const struct bt_mesh_dfu_img *img, struct net_buf_simple *metadata, const struct bt_mesh_blob_io **io)
```

相关声明：[start](#adaefef5067cf3ea273f1db95ca536254)、[bt_mesh_dfu_srv](P055_bt_mesh_dfu_srv_结构体.md)、[bt_mesh_dfu_img](P050_bt_mesh_dfu_img_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)。

传输开始回调（Transfer start callback）。

<a id="r_a822ed15f15286ad4c5ce69009349f6cf"></a>

```c
void(* end )(struct bt_mesh_dfu_srv *srv, const struct bt_mesh_dfu_img *img, bool success)
```

相关声明：[end](#a822ed15f15286ad4c5ce69009349f6cf)、[bt_mesh_dfu_srv](P055_bt_mesh_dfu_srv_结构体.md)、[bt_mesh_dfu_img](P050_bt_mesh_dfu_img_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

传输结束回调（Transfer end callback）。

<a id="r_a3fec449cebe43dd2d8e6ecf3c148234d"></a>

```c
int(* recover )(struct bt_mesh_dfu_srv *srv, const struct bt_mesh_dfu_img *img, const struct bt_mesh_blob_io **io)
```

相关声明：[recover](#a3fec449cebe43dd2d8e6ecf3c148234d)、[bt_mesh_dfu_srv](P055_bt_mesh_dfu_srv_结构体.md)、[bt_mesh_dfu_img](P050_bt_mesh_dfu_img_结构体.md)、[bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)。

传输恢复处理回调（Transfer recovery callback）。

<a id="r_afe4b6ca9f56938695addba6ecc18bb4b"></a>

```c
int(* apply )(struct bt_mesh_dfu_srv *srv, const struct bt_mesh_dfu_img *img)
```

相关声明：[apply](#afe4b6ca9f56938695addba6ecc18bb4b)、[bt_mesh_dfu_srv](P055_bt_mesh_dfu_srv_结构体.md)、[bt_mesh_dfu_img](P050_bt_mesh_dfu_img_结构体.md)。

传输应用回调（Transfer apply callback）。

## 56.2\_详细说明（Detailed Documentation）

<a id="afe4b6ca9f56938695addba6ecc18bb4b"></a>

### `apply`

```c
int(* bt_mesh_dfu_srv_cb::apply) (struct bt_mesh_dfu_srv *srv, const struct bt_mesh_dfu_img *img)
```

传输应用回调（Transfer apply callback）。

传输已完成验证，且更新方（Updater）向目标节点发送应用消息（Apply message）之后调用。

此处理函数（Handler）为可选。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 固件更新服务器（Firmware Update Server）的实例。 |
| `img` | 应应用的设备固件更新镜像（DFU image）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="afbde918804e66160ffa176c206540027"></a>

### `check`

```c
int(* bt_mesh_dfu_srv_cb::check) (struct bt_mesh_dfu_srv *srv, const struct bt_mesh_dfu_img *img, struct net_buf_simple *metadata, enum bt_mesh_dfu_effect *effect)
```

传输检查回调（Transfer check callback）。

传输检查（Transfer check）可用于在传输开始前验证传入的传输内容。元数据（Metadata）的内容由具体实现决定，应包含应用判断是否接受该镜像、以及传输会产生何种影响所需的全部信息。

如果应用该镜像会影响 Mesh 协议栈的配网状态（Provisioning state），可通过返回参数 `effect` 传达此影响。

元数据检查（Metadata check）既可以作为启动新传输的一部分执行，也可以作为独立过程执行。

此处理函数（Handler）为可选。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 固件更新服务器（Firmware Update Server）的实例。 |
| `img` | 要对其执行元数据检查（Metadata check）的设备固件更新镜像（DFU image）。 |
| `metadata` | 镜像元数据（Image metadata）。 |
| `effect` | 用于返回镜像对 Mesh 协议栈配网状态（Provisioning state）影响的参数。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="a822ed15f15286ad4c5ce69009349f6cf"></a>

### `end`

```c
void(* bt_mesh_dfu_srv_cb::end) (struct bt_mesh_dfu_srv *srv, const struct bt_mesh_dfu_img *img, bool success)
```

传输结束回调（Transfer end callback）。

此处理函数（Handler）为可选。

若传输成功，应用应验证固件镜像（Firmware image），并根据结果调用 `bt_mesh_dfu_srv_verified` 或 `bt_mesh_dfu_srv_rejected`。

若传输失败，此函数返回后，固件更新服务器（Firmware Update Server）将立即可以接受新传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 固件更新服务器（Firmware Update Server）的实例。 |
| `img` | 更新失败的设备固件更新镜像（DFU image）。 |
| `success` | 设备固件更新传输（DFU transfer）是否成功。 |

<a id="a3fec449cebe43dd2d8e6ecf3c148234d"></a>

### `recover`

```c
int(* bt_mesh_dfu_srv_cb::recover) (struct bt_mesh_dfu_srv *srv, const struct bt_mesh_dfu_img *img, const struct bt_mesh_blob_io **io)
```

传输恢复处理回调（Transfer recovery callback）。

若设备在传输中途重启，固件更新服务器（Firmware Update Server）会在蓝牙 Mesh 子系统（Bluetooth Mesh subsystem）启动时调用此函数。

此回调为可选，但没有它就无法在重启后恢复传输（Transfer recovery）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 固件更新服务器（Firmware Update Server）的实例。 |
| `img` | 正在更新的设备固件更新镜像（DFU image）。 |
| `io` | 用于返回二进制大对象流（BLOB stream）的参数。回调必须将其设置为有效的 BLOB 流。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`；返回负错误码表示放弃传输。

<a id="adaefef5067cf3ea273f1db95ca536254"></a>

### `start`

```c
int(* bt_mesh_dfu_srv_cb::start) (struct bt_mesh_dfu_srv *srv, const struct bt_mesh_dfu_img *img, struct net_buf_simple *metadata, const struct bt_mesh_blob_io **io)
```

传输开始回调（Transfer start callback）。

固件更新服务器（Firmware Update Server）准备开始新的设备固件更新传输（DFU transfer）时调用。应用必须提供一个已初始化的二进制大对象流（BLOB stream），供此次 DFU 传输使用。

下列错误码（Error codes）会被特殊处理，应使用它们传达相应问题：

- `-ENOMEM`：设备无法容纳此镜像（Image）。
- `-EBUSY`：应用暂时无法接受此传输（Transfer）。
- `-EALREADY`：设备已收到并验证此镜像（Image），无需再次传输。固件更新模型（Firmware Update model）将跳过传输阶段，并将镜像标记为已验证（Verified）。

此处理函数（Handler）为必需。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 固件更新服务器（Firmware Update Server）的实例。 |
| `img` | 正在更新的设备固件更新镜像（DFU image）。 |
| `metadata` | 镜像元数据（Image metadata）。 |
| `io` | 用于返回二进制大对象流（BLOB stream）的参数。回调必须将其设置为有效的 BLOB 流。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。返回码 `-ENOMEM`、`-EBUSY`、`-EALREADY` 会传给更新方（Updater）；其他错误码作为内部错误（Internal errors）报告。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/dfu_srv.h`

## 56.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/dfu_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__srv_8h_source.html)
- [bt_mesh_dfu_srv](P055_bt_mesh_dfu_srv_结构体.md)
- [bt_mesh_dfu_img](P050_bt_mesh_dfu_img_结构体.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_mesh_dfu_effect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8)
- [bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_mesh_dfu_srv_verified](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga64eeb5bfe9bac8c1120c5e0aa9ce02ac)
- [bt_mesh_dfu_srv_rejected](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga77142a1f3cfe2ff1d53332114f977b38)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P055_bt_mesh_dfu_srv_结构体.md) · [返回大纲](大纲.md) · [下一章](P057_bt_mesh_dfu_target_结构体.md)
