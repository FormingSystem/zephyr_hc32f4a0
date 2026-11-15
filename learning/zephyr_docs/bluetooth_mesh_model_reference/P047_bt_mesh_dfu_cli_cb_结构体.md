---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-47
title: bt_mesh_dfu_cli_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__cli__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_bt\_mesh\_dfu\_cli\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__cli__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

固件更新客户端（Firmware Update Client）的事件回调。

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

<a id="details"></a>

固件更新客户端（Firmware Update Client）的事件回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 47.1\_数据成员（Data Fields）

<a id="r_ad2abfdf93f23cecd30e12241bb064a7f"></a>

```c
void(* suspended )(struct bt_mesh_dfu_cli *cli)
```

相关声明：[suspended](#ad2abfdf93f23cecd30e12241bb064a7f)、[bt_mesh_dfu_cli](P046_bt_mesh_dfu_cli_结构体.md)。

二进制大对象传输（BLOB transfer）已挂起。

<a id="r_aa3c8985490a6b2bd6fcd81dff0132060"></a>

```c
void(* ended )(struct bt_mesh_dfu_cli *cli, enum bt_mesh_dfu_status reason)
```

相关声明：[ended](#aa3c8985490a6b2bd6fcd81dff0132060)、[bt_mesh_dfu_cli](P046_bt_mesh_dfu_cli_结构体.md)、[bt_mesh_dfu_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga9e627a3c15de782faa11ef6c4ec5e05d)。

设备固件更新（DFU）已结束。

<a id="r_a6f580db9629d81f72c79d00a5aea2de4"></a>

```c
void(* applied )(struct bt_mesh_dfu_cli *cli)
```

相关声明：[applied](#a6f580db9629d81f72c79d00a5aea2de4)、[bt_mesh_dfu_cli](P046_bt_mesh_dfu_cli_结构体.md)。

设备固件更新传输（DFU transfer）已在所有活动目标节点上应用。

<a id="r_a32b20280b2196437bad6d85edc017c63"></a>

```c
void(* confirmed )(struct bt_mesh_dfu_cli *cli)
```

相关声明：[confirmed](#a32b20280b2196437bad6d85edc017c63)、[bt_mesh_dfu_cli](P046_bt_mesh_dfu_cli_结构体.md)。

设备固件更新传输（DFU transfer）已在所有活动目标节点上确认。

<a id="r_ab4d00147b1e525f392d09d5545de2465"></a>

```c
void(* lost_target )(struct bt_mesh_dfu_cli *cli, struct bt_mesh_dfu_target *target)
```

相关声明：[lost_target](#ab4d00147b1e525f392d09d5545de2465)、[bt_mesh_dfu_cli](P046_bt_mesh_dfu_cli_结构体.md)、[bt_mesh_dfu_target](P057_bt_mesh_dfu_target_结构体.md)。

设备固件更新目标节点（DFU Target node）丢失。

## 47.2\_详细说明（Detailed Documentation）

<a id="a6f580db9629d81f72c79d00a5aea2de4"></a>

### `applied`

```c
void(* bt_mesh_dfu_cli_cb::applied) (struct bt_mesh_dfu_cli *cli)
```

设备固件更新传输（DFU transfer）已在所有活动目标节点上应用。

由 `bt_mesh_dfu_cli_apply` 启动的应用过程（Apply procedure）结束时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 固件更新客户端（Firmware Update Client）的模型实例。 |

<a id="a32b20280b2196437bad6d85edc017c63"></a>

### `confirmed`

```c
void(* bt_mesh_dfu_cli_cb::confirmed) (struct bt_mesh_dfu_cli *cli)
```

设备固件更新传输（DFU transfer）已在所有活动目标节点上确认。

由 `bt_mesh_dfu_cli_confirm` 启动的应用过程（Apply procedure）结束时调用。译注：此处过程名称“apply”按原文保留，函数标识仍为 `bt_mesh_dfu_cli_confirm`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 固件更新客户端（Firmware Update Client）的模型实例。 |

<a id="aa3c8985490a6b2bd6fcd81dff0132060"></a>

### `ended`

```c
void(* bt_mesh_dfu_cli_cb::ended) (struct bt_mesh_dfu_cli *cli, enum bt_mesh_dfu_status reason)
```

设备固件更新（DFU）已结束。

设备固件更新传输（DFU transfer）结束时调用，无论结束原因为丢失所有目标节点，还是成功完成传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 固件更新客户端（Firmware Update Client）的模型实例。 |
| `reason` | 结束原因（Reason for ending）。 |

<a id="ab4d00147b1e525f392d09d5545de2465"></a>

### `lost_target`

```c
void(* bt_mesh_dfu_cli_cb::lost_target) (struct bt_mesh_dfu_cli *cli, struct bt_mesh_dfu_target *target)
```

设备固件更新目标节点（DFU Target node）丢失。

一个设备固件更新目标节点（DFU Target node）已从接收方列表中移除。该目标节点的状态被设置为反映失败原因的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 固件更新客户端（Firmware Update Client）的模型实例。 |
| `target` | 丢失的设备固件更新目标节点（DFU Target node）。 |

<a id="ad2abfdf93f23cecd30e12241bb064a7f"></a>

### `suspended`

```c
void(* bt_mesh_dfu_cli_cb::suspended) (struct bt_mesh_dfu_cli *cli)
```

二进制大对象传输（BLOB transfer）已挂起。

因所有目标节点响应超时而挂起二进制大对象传输（BLOB transfer）时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 固件更新客户端（Firmware Update Client）的模型实例。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/dfu_cli.h`

## 47.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/dfu_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__cli_8h_source.html)
- [bt_mesh_dfu_cli](P046_bt_mesh_dfu_cli_结构体.md)
- [bt_mesh_dfu_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga9e627a3c15de782faa11ef6c4ec5e05d)
- [bt_mesh_dfu_target](P057_bt_mesh_dfu_target_结构体.md)
- [bt_mesh_dfu_cli_apply](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga2904ba992a00ee9fba6704c1efc8f074)
- [bt_mesh_dfu_cli_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#gaf76f0cdb5c6b0df12ddb495c718c3c93)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P046_bt_mesh_dfu_cli_结构体.md) · [返回大纲](大纲.md) · [下一章](P048_bt_mesh_dfu_cli_xfer_结构体.md)
