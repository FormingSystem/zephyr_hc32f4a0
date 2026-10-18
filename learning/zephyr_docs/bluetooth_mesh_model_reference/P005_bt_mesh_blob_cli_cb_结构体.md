---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-5
title: bt_mesh_blob_cli_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__cli__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_bt\_mesh\_blob\_cli\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__cli__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BLOB传输客户端（BLOB Transfer Client）模型的事件处理回调。

```c
#include <zephyr/bluetooth/mesh/blob_cli.h>
```

<a id="details"></a>

二进制大对象传输客户端模型（BLOB Transfer Client model）的事件处理回调。所有处理函数均为可选。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_a58e749cadeb464299495ee74456c592c"></a>

```c
void(* caps )(struct bt_mesh_blob_cli *cli, const struct bt_mesh_blob_cli_caps *caps)
```

相关声明：[caps](#a58e749cadeb464299495ee74456c592c)、[bt_mesh_blob_cli](P003_bt_mesh_blob_cli_结构体.md)、[bt_mesh_blob_cli_caps](P004_bt_mesh_blob_cli_caps_结构体.md)。

能力获取完成回调（Capabilities retrieval completion callback）。

<a id="r_a26a5ebe87db105900b150f71d770234d"></a>

```c
void(* lost_target )(struct bt_mesh_blob_cli *cli, struct bt_mesh_blob_target *target, enum bt_mesh_blob_status reason)
```

相关声明：[lost_target](#a26a5ebe87db105900b150f71d770234d)、[bt_mesh_blob_cli](P003_bt_mesh_blob_cli_结构体.md)、[bt_mesh_blob_target](P012_bt_mesh_blob_target_结构体.md)、[bt_mesh_blob_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga7b5e2895a6577103a8a680a94ee7776d)。

目标节点丢失回调（Target node loss callback）。

<a id="r_a154a3308167eda4cd93ac28e379c52bc"></a>

```c
void(* suspended )(struct bt_mesh_blob_cli *cli)
```

相关声明：[suspended](#a154a3308167eda4cd93ac28e379c52bc)、[bt_mesh_blob_cli](P003_bt_mesh_blob_cli_结构体.md)。

传输已挂起（Transfer is suspended）。

<a id="r_a60bc49eab376b055a8c21099f86fdde7"></a>

```c
void(* end )(struct bt_mesh_blob_cli *cli, const struct bt_mesh_blob_xfer *xfer, bool success)
```

相关声明：[end](#a60bc49eab376b055a8c21099f86fdde7)、[bt_mesh_blob_cli](P003_bt_mesh_blob_cli_结构体.md)、[bt_mesh_blob_xfer](P014_bt_mesh_blob_xfer_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

传输结束回调（Transfer end callback）。

<a id="r_a4b01ef0ab0a367739a75751b57149546"></a>

```c
void(* xfer_progress )(struct bt_mesh_blob_cli *cli, struct bt_mesh_blob_target *target, const struct bt_mesh_blob_xfer_info *info)
```

相关声明：[xfer_progress](#a4b01ef0ab0a367739a75751b57149546)、[bt_mesh_blob_cli](P003_bt_mesh_blob_cli_结构体.md)、[bt_mesh_blob_target](P012_bt_mesh_blob_target_结构体.md)、[bt_mesh_blob_xfer_info](P015_bt_mesh_blob_xfer_info_结构体.md)。

传输进度回调（Transfer progress callback）。

<a id="r_abb4a4d4d24bef076aad7ae56b08d23ed"></a>

```c
void(* xfer_progress_complete )(struct bt_mesh_blob_cli *cli)
```

相关声明：[xfer_progress_complete](#abb4a4d4d24bef076aad7ae56b08d23ed)、[bt_mesh_blob_cli](P003_bt_mesh_blob_cli_结构体.md)。

获取传输进度过程结束（End of Get Transfer Progress procedure）。

## 5.2\_详细说明（Detailed Documentation）

<a id="a58e749cadeb464299495ee74456c592c"></a>

### `caps`

```c
void(* bt_mesh_blob_cli_cb::caps) (struct bt_mesh_blob_cli *cli, const struct bt_mesh_blob_cli_caps *caps)
```

能力获取完成回调（Capabilities retrieval completion callback）。

能力获取过程（Capabilities retrieval procedure）完成时调用，表示已为给定的目标节点（Target nodes）列表确定一组共同可接受的传输参数。所有兼容的目标节点的状态码均为 `BT_MESH_BLOB_SUCCESS`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 二进制大对象传输客户端实例（BLOB Transfer Client instance）。 |
| `caps` | 若至少一个目标节点的传输能力满足客户端要求，则为可安全使用的传输能力（Safe transfer capabilities）；否则为 `NULL`。 |

<a id="a60bc49eab376b055a8c21099f86fdde7"></a>

### `end`

```c
void(* bt_mesh_blob_cli_cb::end) (struct bt_mesh_blob_cli *cli, const struct bt_mesh_blob_xfer *xfer, bool success)
```

传输结束回调（Transfer end callback）。

传输结束（Transfer ends）时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 二进制大对象传输客户端实例（BLOB Transfer Client instance）。 |
| `xfer` | 已完成的传输（Completed transfer）。 |
| `success` | 传输状态（Transfer status）。至少有一个目标节点接收了全部传输内容时为 `true`。 |

<a id="a26a5ebe87db105900b150f71d770234d"></a>

### `lost_target`

```c
void(* bt_mesh_blob_cli_cb::lost_target) (struct bt_mesh_blob_cli *cli, struct bt_mesh_blob_target *target, enum bt_mesh_blob_status reason)
```

目标节点丢失回调（Target node loss callback）。

因传输错误而丢失目标节点（Target node）时调用。对于客户端（Client），只要尚未丢失所有目标节点，丢失某个目标节点就不视为致命错误（Fatal error）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 二进制大对象传输客户端实例（BLOB Transfer Client instance）。 |
| `target` | 丢失的目标节点（Lost Target node）。 |
| `reason` | 目标节点丢失原因（Reason for Target node loss）。 |

<a id="a154a3308167eda4cd93ac28e379c52bc"></a>

### `suspended`

```c
void(* bt_mesh_blob_cli_cb::suspended) (struct bt_mesh_blob_cli *cli)
```

传输已挂起（Transfer is suspended）。

因所有目标节点（Target nodes）响应超时而挂起传输时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 二进制大对象传输客户端实例（BLOB Transfer Client instance）。 |

<a id="a4b01ef0ab0a367739a75751b57149546"></a>

### `xfer_progress`

```c
void(* bt_mesh_blob_cli_cb::xfer_progress) (struct bt_mesh_blob_cli *cli, struct bt_mesh_blob_target *target, const struct bt_mesh_blob_xfer_info *info)
```

传输进度回调（Transfer progress callback）。

退出回调后，`info` 的内容将失效；如果以后仍要使用，必须复制它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 二进制大对象传输客户端实例（BLOB Transfer Client instance）。 |
| `target` | 响应请求的目标节点（Target node）。 |
| `info` | 二进制大对象传输（BLOB Transfer）的信息。 |

<a id="abb4a4d4d24bef076aad7ae56b08d23ed"></a>

### `xfer_progress_complete`

```c
void(* bt_mesh_blob_cli_cb::xfer_progress_complete) (struct bt_mesh_blob_cli *cli)
```

获取传输进度过程结束（End of Get Transfer Progress procedure）。

所有目标节点（Target nodes）均已响应或过程超时后调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 二进制大对象传输客户端实例（BLOB Transfer Client instance）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/blob_cli.h`

## 5.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/blob_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h_source.html)
- [bt_mesh_blob_cli](P003_bt_mesh_blob_cli_结构体.md)
- [bt_mesh_blob_cli_caps](P004_bt_mesh_blob_cli_caps_结构体.md)
- [bt_mesh_blob_target](P012_bt_mesh_blob_target_结构体.md)
- [bt_mesh_blob_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga7b5e2895a6577103a8a680a94ee7776d)
- [bt_mesh_blob_xfer](P014_bt_mesh_blob_xfer_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_mesh_blob_xfer_info](P015_bt_mesh_blob_xfer_info_结构体.md)
- [BT_MESH_BLOB_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776daac639c3c82cf48a394c13e3b057c9c0d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_bt_mesh_blob_cli_caps_结构体.md) · [返回大纲](大纲.md) · [下一章](P006_bt_mesh_blob_cli_inputs_结构体.md)
