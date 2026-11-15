---
id: learning.zephyr-docs.api-topic-reference.page-7
title: 配置服务器模型（Configuration Server Model）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_配置服务器模型（Configuration Server Model）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__srv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

配置服务器模型（Configuration Server Model）

<a id="details"></a>

配置服务器模型（Configuration Server Model）

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="r_gafc6b9dea9f72d5754c1a4b42bfafd656"></a>

```c
#define BT_MESH_MODEL_CFG_SRV
```

相关声明：[BT_MESH_MODEL_CFG_SRV](#gafc6b9dea9f72d5754c1a4b42bfafd656)。

通用配置服务器模型（Generic Configuration Server Model）的组成数据条目（Composition Data Entry）。

## 7.2\_详细说明（Detailed Documentation）

<a id="gafc6b9dea9f72d5754c1a4b42bfafd656"></a>

### `BT_MESH_MODEL_CFG_SRV`

```c
#define BT_MESH_MODEL_CFG_SRV
```

```c
#include <zephyr/bluetooth/mesh/cfg_srv.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CNT_CB(BT_MESH_MODEL_ID_CFG_SRV,  \
                     bt_mesh_cfg_srv_op, NULL,  \
                     NULL, 1, 0, &bt_mesh_cfg_srv_cb)
```

通用配置服务器模型（Generic Configuration Server Model）的组成数据条目（Composition Data Entry）。


## 7.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/cfg_srv.h](../api_file_supplement_reference/P013_zephyr__bluetooth__mesh__cfg_srv.h_文件参考.md)
- [BT_MESH_MODEL_CNT_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga925da443eb15a4c1980d48a69388dc2c)
- [BT_MESH_MODEL_ID_CFG_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#ga004d8d1be55b2aec56abbeeca1d118d8)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_ga004d8d1be55b2aec56abbeeca1d118d8"></a>
<a id="agroup__bt__mesh__access_html_ga925da443eb15a4c1980d48a69388dc2c"></a>

---

[上一章](P006_桥接配置服务器模型（Bridge Configuration Server Model）.md) · [返回大纲](大纲.md) · [下一章](P008_大型组成数据服务器模型（Large Composition Data Server model）.md)
