---
id: learning.zephyr-docs.api-topic-reference.page-13
title: 蓝牙 Mesh 分段与重组配置服务器模型（SAR Configuration Server Model）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_蓝牙 Mesh 分段与重组配置服务器模型（SAR Configuration Server Model）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__srv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙网状网络（Bluetooth Mesh）

<a id="details"></a>

蓝牙网状网络（Bluetooth Mesh）

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.1\_宏定义（Macros）

<a id="r_gaddb9214dd96ad476aac4f9a8947dfd45"></a>

```c
#define BT_MESH_MODEL_SAR_CFG_SRV
```

相关声明：[BT_MESH_MODEL_SAR_CFG_SRV](#gaddb9214dd96ad476aac4f9a8947dfd45)。

传输分段与重组配置服务器模型（Transport SAR Configuration Server Model）的组成数据条目（Composition Data Entry）。

## 13.2\_详细说明（Detailed Documentation）

<a id="gaddb9214dd96ad476aac4f9a8947dfd45"></a>

### `BT_MESH_MODEL_SAR_CFG_SRV`

```c
#define BT_MESH_MODEL_SAR_CFG_SRV
```

```c
#include <zephyr/bluetooth/mesh/sar_cfg_srv.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_SAR_CFG_SRV, bt_mesh_sar_cfg_srv_op, \
                 NULL, NULL, &bt_mesh_sar_cfg_srv_cb)
```

传输分段与重组配置服务器模型（Transport SAR Configuration Server Model）的组成数据条目（Composition Data Entry）。


## 13.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/sar_cfg_srv.h](../api_file_supplement_reference/P105_zephyr__bluetooth__mesh__sar_cfg_srv.h_文件参考.md)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_ID_SAR_CFG_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#ga1e9d8be1d2e65d2977aea0306b015258)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_ga1e9d8be1d2e65d2977aea0306b015258"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>

---

[上一章](P012_分段与重组（SAR）配置公共头文件.md) · [返回大纲](大纲.md) · [下一章](P014_蓝牙 Mesh 请求 PDU 重放保护列表服务器（Solicitation PDU RPL Server）.md)
