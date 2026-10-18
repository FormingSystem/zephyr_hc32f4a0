---
id: learning.zephyr-docs.api-topic-reference.page-6
title: 桥接配置服务器模型（Bridge Configuration Server Model）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_桥接配置服务器模型（Bridge Configuration Server Model）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__srv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙 Mesh 桥接配置服务器模型的 API。

<a id="details"></a>

蓝牙 Mesh 桥接配置服务器模型的 API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="r_ga54e0629a3ae842e7c57a69f2cdab98e3"></a>

```c
#define BT_MESH_MODEL_BRG_CFG_SRV
```

相关声明：[BT_MESH_MODEL_BRG_CFG_SRV](#ga54e0629a3ae842e7c57a69f2cdab98e3)。

桥接配置服务器模型（Bridge Configuration Server Model）的组成数据条目（Composition Data Entry）。

## 6.2\_详细说明（Detailed Documentation）

<a id="ga54e0629a3ae842e7c57a69f2cdab98e3"></a>

### `BT_MESH_MODEL_BRG_CFG_SRV`

```c
#define BT_MESH_MODEL_BRG_CFG_SRV
```

```c
#include <zephyr/bluetooth/mesh/brg_cfg_srv.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_BRG_CFG_SRV, _bt_mesh_brg_cfg_srv_op, NULL, NULL,        \
                 &_bt_mesh_brg_cfg_srv_cb)
```

桥接配置服务器模型（Bridge Configuration Server Model）的组成数据条目（Composition Data Entry）。


## 6.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/brg_cfg_srv.h](../api_file_supplement_reference/P012_zephyr__bluetooth__mesh__brg_cfg_srv.h_文件参考.md)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_ID_BRG_CFG_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#ga599d00e9d63ade6ed1a6803579c1e16e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_ga599d00e9d63ade6ed1a6803579c1e16e"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>

---

[上一章](P005_身份认证（Authentication）.md) · [返回大纲](大纲.md) · [下一章](P007_配置服务器模型（Configuration Server Model）.md)
