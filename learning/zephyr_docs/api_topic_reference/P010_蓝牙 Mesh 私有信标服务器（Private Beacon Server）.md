---
id: learning.zephyr-docs.api-topic-reference.page-10
title: 蓝牙 Mesh 私有信标服务器（Private Beacon Server）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_蓝牙 Mesh 私有信标服务器（Private Beacon Server）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__priv__beacon__srv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 10.1\_文件（Files）

<a id="r_priv_5Fbeacon_5Fsrv_2Eh"></a>

```c
file priv_beacon_srv.h
```

相关声明：[priv_beacon_srv.h](../api_file_supplement_reference/P092_zephyr__bluetooth__mesh__priv_beacon_srv.h_文件参考.md)。

蓝牙Mesh私有信标服务器（Private Beacon Server）模型API的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.2\_宏定义（Macros）

<a id="r_gac2e5a8847c2abf94feddfc78d0589dc2"></a>

```c
#define BT_MESH_MODEL_PRIV_BEACON_SRV
```

相关声明：[BT_MESH_MODEL_PRIV_BEACON_SRV](#gac2e5a8847c2abf94feddfc78d0589dc2)。

私有信标服务器模型（Private Beacon Server Model）的组成数据条目（Composition Data Entry）。

## 10.3\_详细说明（Detailed Documentation）

<a id="gac2e5a8847c2abf94feddfc78d0589dc2"></a>

### `BT_MESH_MODEL_PRIV_BEACON_SRV`

```c
#define BT_MESH_MODEL_PRIV_BEACON_SRV
```

```c
#include <zephyr/bluetooth/mesh/priv_beacon_srv.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_PRIV_BEACON_SRV,                     \
                 bt_mesh_priv_beacon_srv_op, NULL, NULL,               \
                 &bt_mesh_priv_beacon_srv_cb)
```

私有信标服务器模型（Private Beacon Server Model）的组成数据条目（Composition Data Entry）。


## 10.4\_原页交叉引用（Cross References）

- [priv_beacon_srv.h](../api_file_supplement_reference/P092_zephyr__bluetooth__mesh__priv_beacon_srv.h_文件参考.md)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_ID_PRIV_BEACON_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#gacca0e355982935cfbde46a06b09a7bec)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_gacca0e355982935cfbde46a06b09a7bec"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>

---

[上一章](P009_蓝牙 Mesh 按需私有 GATT 代理服务器（On-Demand Private GATT Proxy Server）.md) · [返回大纲](大纲.md) · [下一章](P011_远程配网服务器（Remote provisioning server）.md)
