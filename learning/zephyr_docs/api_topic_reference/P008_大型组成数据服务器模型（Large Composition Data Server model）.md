---
id: learning.zephyr-docs.api-topic-reference.page-8
title: 大型组成数据服务器模型（Large Composition Data Server model）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__large__comp__data__srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_大型组成数据服务器模型（Large Composition Data Server model）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__large__comp__data__srv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 8.1\_文件（Files）

<a id="r_large_5Fcomp_5Fdata_5Fsrv_2Eh"></a>

```c
file large_comp_data_srv.h
```

相关声明：[large_comp_data_srv.h](../api_file_supplement_reference/P056_zephyr__bluetooth__mesh__large_comp_data_srv.h_文件参考.md)。

蓝牙Mesh大型组成数据服务器（Large Composition Data Server）模型API的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.2\_宏定义（Macros）

<a id="r_gae4af1e8cdbc517443e1966ba681d157e"></a>

```c
#define BT_MESH_MODEL_LARGE_COMP_DATA_SRV
```

相关声明：[BT_MESH_MODEL_LARGE_COMP_DATA_SRV](#gae4af1e8cdbc517443e1966ba681d157e)。

大型组成数据服务器模型（Large Composition Data Server Model）的组成数据条目（Composition Data Entry）。

## 8.3\_详细说明（Detailed Documentation）

<a id="gae4af1e8cdbc517443e1966ba681d157e"></a>

### `BT_MESH_MODEL_LARGE_COMP_DATA_SRV`

```c
#define BT_MESH_MODEL_LARGE_COMP_DATA_SRV
```

```c
#include <zephyr/bluetooth/mesh/large_comp_data_srv.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_LARGE_COMP_DATA_SRV,                 \
                 _bt_mesh_large_comp_data_srv_op, NULL, NULL,          \
                 &_bt_mesh_large_comp_data_srv_cb)
```

大型组成数据服务器模型（Large Composition Data Server Model）的组成数据条目（Composition Data Entry）。


## 8.4\_原页交叉引用（Cross References）

- [large_comp_data_srv.h](../api_file_supplement_reference/P056_zephyr__bluetooth__mesh__large_comp_data_srv.h_文件参考.md)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_ID_LARGE_COMP_DATA_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#gaec3abd6a0bd7b07a71fe5ed6a7a6931a)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_gaec3abd6a0bd7b07a71fe5ed6a7a6931a"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>

---

[上一章](P007_配置服务器模型（Configuration Server Model）.md) · [返回大纲](大纲.md) · [下一章](P009_蓝牙 Mesh 按需私有 GATT 代理服务器（On-Demand Private GATT Proxy Server）.md)
