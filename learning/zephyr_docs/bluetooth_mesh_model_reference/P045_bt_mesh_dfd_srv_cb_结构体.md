---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-45
title: bt_mesh_dfd_srv_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfd__srv__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_bt\_mesh\_dfd\_srv\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfd__srv__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

固件分发服务器（Firmware Distribution Server）的回调：

```c
#include <zephyr/bluetooth/mesh/dfd_srv.h>
```

<a id="details"></a>

固件分发服务器（Firmware Distribution Server）的回调：

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 45.1\_数据成员（Data Fields）

<a id="r_a6d6d991b3a5bd5fe69b1648fea94ebe4"></a>

```c
int(* recv )(struct bt_mesh_dfd_srv *srv, const struct bt_mesh_dfu_slot *slot, const struct bt_mesh_blob_io **io)
```

相关声明：[recv](#a6d6d991b3a5bd5fe69b1648fea94ebe4)、[bt_mesh_dfd_srv](P044_bt_mesh_dfd_srv_结构体.md)、[bt_mesh_dfu_slot](P054_bt_mesh_dfu_slot_结构体.md)、[bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)。

槽位接收回调（Slot receive callback）。

<a id="r_a73f230a76ea32fb1faee15a5d4adb550"></a>

```c
void(* del )(struct bt_mesh_dfd_srv *srv, const struct bt_mesh_dfu_slot *slot)
```

相关声明：[del](#a73f230a76ea32fb1faee15a5d4adb550)、[bt_mesh_dfd_srv](P044_bt_mesh_dfd_srv_结构体.md)、[bt_mesh_dfu_slot](P054_bt_mesh_dfu_slot_结构体.md)。

槽位删除回调（Slot delete callback）。

<a id="r_a84e14ad78ebe520bad3ad6ee24fbb629"></a>

```c
int(* send )(struct bt_mesh_dfd_srv *srv, const struct bt_mesh_dfu_slot *slot, const struct bt_mesh_blob_io **io)
```

相关声明：[send](#a84e14ad78ebe520bad3ad6ee24fbb629)、[bt_mesh_dfd_srv](P044_bt_mesh_dfd_srv_结构体.md)、[bt_mesh_dfu_slot](P054_bt_mesh_dfu_slot_结构体.md)、[bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)。

槽位发送回调（Slot send callback）。

<a id="r_ae72a527cae827e0a234af3277384d07f"></a>

```c
void(* phase )(struct bt_mesh_dfd_srv *srv, enum bt_mesh_dfd_phase phase)
```

相关声明：[phase](#ae72a527cae827e0a234af3277384d07f)、[bt_mesh_dfd_srv](P044_bt_mesh_dfd_srv_结构体.md)、[bt_mesh_dfd_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#gab6562d62668ebcdb146be35b909c30c2)。

阶段变化回调（Phase change callback），可选。

## 45.2\_详细说明（Detailed Documentation）

<a id="a73f230a76ea32fb1faee15a5d4adb550"></a>

### `del`

```c
void(* bt_mesh_dfd_srv_cb::del) (struct bt_mesh_dfd_srv *srv, const struct bt_mesh_dfu_slot *slot)
```

槽位删除回调（Slot delete callback）。

固件分发服务器（Firmware Distribution Server）即将删除设备固件更新镜像槽位（DFU image slot）时调用。应删除与该固件槽位关联的全部已分配数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 固件更新服务器（Firmware Update Server）的实例。 |
| `slot` | 正在删除的设备固件更新镜像槽位（DFU image slot）。 |

<a id="ae72a527cae827e0a234af3277384d07f"></a>

### `phase`

```c
void(* bt_mesh_dfd_srv_cb::phase) (struct bt_mesh_dfd_srv *srv, enum bt_mesh_dfd_phase phase)
```

阶段变化回调（Phase change callback），可选。

固件分发服务器（Firmware Distribution Server）的阶段发生变化时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 固件分发服务器模型实例（Firmware Distribution Server model instance）。 |
| `phase` | 新的固件分发阶段（Firmware Distribution phase）。 |

<a id="a6d6d991b3a5bd5fe69b1648fea94ebe4"></a>

### `recv`

```c
int(* bt_mesh_dfd_srv_cb::recv) (struct bt_mesh_dfd_srv *srv, const struct bt_mesh_dfu_slot *slot, const struct bt_mesh_blob_io **io)
```

槽位接收回调（Slot receive callback）。

上传过程（Upload procedure）开始时调用。回调必须向 `io` 填入一个可写的二进制大对象流（BLOB stream）指针，供固件分发服务器（Firmware Distribution Server）写入固件镜像。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 固件分发服务器模型实例（Firmware Distribution Server model instance）。 |
| `slot` | 正在接收的设备固件更新镜像槽位（DFU image slot）。 |
| `io` | 二进制大对象流响应指针（BLOB stream response pointer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="a84e14ad78ebe520bad3ad6ee24fbb629"></a>

### `send`

```c
int(* bt_mesh_dfd_srv_cb::send) (struct bt_mesh_dfd_srv *srv, const struct bt_mesh_dfu_slot *slot, const struct bt_mesh_blob_io **io)
```

槽位发送回调（Slot send callback）。

分发过程（Distribution procedure）开始时调用。回调必须向 `io` 填入一个可读的二进制大对象流（BLOB stream）指针，供固件分发服务器（Firmware Distribution Server）读取固件镜像。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `srv` | 固件分发服务器模型实例（Firmware Distribution Server model instance）。 |
| `slot` | 正在发送的设备固件更新镜像槽位（DFU image slot）。 |
| `io` | 二进制大对象流响应指针（BLOB stream response pointer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/dfd_srv.h`

## 45.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/dfd_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/dfd__srv_8h_source.html)
- [bt_mesh_dfd_srv](P044_bt_mesh_dfd_srv_结构体.md)
- [bt_mesh_dfu_slot](P054_bt_mesh_dfu_slot_结构体.md)
- [bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)
- [bt_mesh_dfd_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#gab6562d62668ebcdb146be35b909c30c2)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P044_bt_mesh_dfd_srv_结构体.md) · [返回大纲](大纲.md) · [下一章](P046_bt_mesh_dfu_cli_结构体.md)
