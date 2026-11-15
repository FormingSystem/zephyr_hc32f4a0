---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-55
title: bt_mesh_dfu_srv_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_bt\_mesh\_dfu\_srv\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__srv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

固件更新服务器（Firmware Update Server）的实例。

```c
#include <zephyr/bluetooth/mesh/dfu_srv.h>
```

<a id="details"></a>

固件更新服务器实例（Firmware Update Server instance）。应使用 `BT_MESH_DFU_SRV_INIT` 初始化。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 55.1\_数据成员（Data Fields）

<a id="r_a75fa0d64310958904435f0b08ae9e5a4"></a>

```c
struct bt_mesh_blob_srv blob
```

相关声明：[bt_mesh_blob_srv](P009_bt_mesh_blob_srv_结构体.md)、[blob](#a75fa0d64310958904435f0b08ae9e5a4)。

底层二进制大对象传输服务器（BLOB Transfer Server）。

<a id="r_a23fad6646192b4bdaf80e5bfa3cdf928"></a>

```c
const struct bt_mesh_dfu_srv_cb * cb
```

相关声明：[bt_mesh_dfu_srv_cb](P056_bt_mesh_dfu_srv_cb_结构体.md)、[cb](#a23fad6646192b4bdaf80e5bfa3cdf928)。

回调结构体（Callback Structure）。

<a id="r_ab372c28be95c833146f10236d9e3ecfe"></a>

```c
const struct bt_mesh_dfu_img * imgs
```

相关声明：[bt_mesh_dfu_img](P050_bt_mesh_dfu_img_结构体.md)、[imgs](#ab372c28be95c833146f10236d9e3ecfe)。

可更新镜像列表（Updatable images list）。

<a id="r_ab3cdb7ca3928bccebfcf59fab7f76e51"></a>

```c
size_t img_count
```

相关声明：[img_count](#ab3cdb7ca3928bccebfcf59fab7f76e51)。

可更新镜像数量（Number of updatable images）。

## 55.2\_详细说明（Detailed Documentation）

<a id="a75fa0d64310958904435f0b08ae9e5a4"></a>

### `blob`

```c
struct bt_mesh_blob_srv bt_mesh_dfu_srv::blob
```

底层二进制大对象传输服务器（BLOB Transfer Server）。

<a id="a23fad6646192b4bdaf80e5bfa3cdf928"></a>

### `cb`

```c
const struct bt_mesh_dfu_srv_cb* bt_mesh_dfu_srv::cb
```

回调结构体（Callback Structure）。

<a id="ab3cdb7ca3928bccebfcf59fab7f76e51"></a>

### `img_count`

```c
size_t bt_mesh_dfu_srv::img_count
```

可更新镜像数量（Number of updatable images）。

<a id="ab372c28be95c833146f10236d9e3ecfe"></a>

### `imgs`

```c
const struct bt_mesh_dfu_img* bt_mesh_dfu_srv::imgs
```

可更新镜像列表（Updatable images list）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/dfu_srv.h`

## 55.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/dfu_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__srv_8h_source.html)
- [bt_mesh_blob_srv](P009_bt_mesh_blob_srv_结构体.md)
- [bt_mesh_dfu_srv_cb](P056_bt_mesh_dfu_srv_cb_结构体.md)
- [bt_mesh_dfu_img](P050_bt_mesh_dfu_img_结构体.md)
- [BT_MESH_DFU_SRV_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga8467cd5241dfdcd7add718bbaae6fa60)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P054_bt_mesh_dfu_slot_结构体.md) · [返回大纲](大纲.md) · [下一章](P056_bt_mesh_dfu_srv_cb_结构体.md)
