---
id: learning.zephyr-docs.api-file-configuration-reference.page-15
title: zephyr__bluetooth__mesh__dfd_srv.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dfd__srv_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_bluetooth\_\_mesh\_\_dfd\_srv.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dfd__srv_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/mesh/access.h>
#include <zephyr/bluetooth/mesh/dfd.h>
#include <zephyr/bluetooth/mesh/blob_srv.h>
#include <zephyr/bluetooth/mesh/blob_cli.h>
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.1\_数据结构（Data Structures）

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

## 15.2\_宏定义（Macros）

<a id="r_ga126e2d4df8f58b7de36da46c14b2c804"></a>

```c
#define CONFIG_BT_MESH_DFD_SRV_TARGETS_MAX 0
```

相关声明：[CONFIG_BT_MESH_DFD_SRV_TARGETS_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd__srv.html#ga126e2d4df8f58b7de36da46c14b2c804)。

<a id="r_gab26590917c9de6edaccf07540c88f7c1"></a>

```c
#define CONFIG_BT_MESH_DFD_SRV_SLOT_MAX_SIZE 0
```

相关声明：[CONFIG_BT_MESH_DFD_SRV_SLOT_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd__srv.html#gab26590917c9de6edaccf07540c88f7c1)。

<a id="r_ga394c367492c72f66231b5cf3e2789f5f"></a>

```c
#define CONFIG_BT_MESH_DFD_SRV_SLOT_SPACE 0
```

相关声明：[CONFIG_BT_MESH_DFD_SRV_SLOT_SPACE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd__srv.html#ga394c367492c72f66231b5cf3e2789f5f)。

<a id="r_ga20b1232269b2e859608c21e84305196c"></a>

```c
#define BT_MESH_DFD_SRV_INIT(_cb)
```

相关声明：[BT_MESH_DFD_SRV_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd__srv.html#ga20b1232269b2e859608c21e84305196c)。

固件分发服务器模型（Firmware Distribution Server Model）的初始化参数（Initialization Parameters）。

<a id="r_ga27457d4d72119ab080828359d43ad6cf"></a>

```c
#define BT_MESH_MODEL_DFD_SRV(_srv)
```

相关声明：[BT_MESH_MODEL_DFD_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd__srv.html#ga27457d4d72119ab080828359d43ad6cf)。

固件分发服务器模型（Firmware Distribution Server Model）的组成数据条目（Composition Data Entry）。


## 15.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h_source.html)
- [zephyr/bluetooth/mesh/dfd.h](../api_source_reference/P124_dfd.h_源码浏览.md)
- [zephyr/bluetooth/mesh/blob_srv.h](../api_source_runtime_reference/P002_blob_srv.h_源码浏览.md)
- [zephyr/bluetooth/mesh/blob_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h_source.html)
- [zephyr/bluetooth/mesh/dfu_cli.h](../api_source_supplement_reference/P039_dfu_cli.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P125_dfd_srv.h_源码浏览.md)
- [bt_mesh_dfd_srv_cb](../bluetooth_mesh_model_reference/P045_bt_mesh_dfd_srv_cb_结构体.md)
- [bt_mesh_dfd_srv](../bluetooth_mesh_model_reference/P044_bt_mesh_dfd_srv_结构体.md)
- [CONFIG_BT_MESH_DFD_SRV_TARGETS_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd__srv.html#ga126e2d4df8f58b7de36da46c14b2c804)
- [CONFIG_BT_MESH_DFD_SRV_SLOT_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd__srv.html#gab26590917c9de6edaccf07540c88f7c1)
- [CONFIG_BT_MESH_DFD_SRV_SLOT_SPACE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd__srv.html#ga394c367492c72f66231b5cf3e2789f5f)
- [BT_MESH_DFD_SRV_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd__srv.html#ga20b1232269b2e859608c21e84305196c)
- [固件分发服务器模型（Firmware Distribution Server model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd__srv.html)
- [BT_MESH_MODEL_DFD_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd__srv.html#ga27457d4d72119ab080828359d43ad6cf)

---

[上一章](P014_zephyr__input__cy8cmbr3xxx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__drivers__dma__dma_smartbond.h_文件参考.md)
