---
id: learning.zephyr-docs.api-topic-reference.page-11
title: 远程配网服务器（Remote provisioning server）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_远程配网服务器（Remote provisioning server）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__srv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 11.1\_文件（Files）

<a id="r_rpr_5Fsrv_2Eh"></a>

```c
file rpr_srv.h
```

相关声明：[rpr_srv.h](../api_file_supplement_reference/P100_zephyr__bluetooth__mesh__rpr_srv.h_文件参考.md)。

蓝牙Mesh远程配网服务器（Remote Provisioning Server）模型API的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.2\_宏定义（Macros）

<a id="r_ga49c08c3e98b0c3863dd79b37aea25b34"></a>

```c
#define BT_MESH_MODEL_RPR_SRV
```

相关声明：[BT_MESH_MODEL_RPR_SRV](#ga49c08c3e98b0c3863dd79b37aea25b34)。

远程配置服务器模型（Remote Provisioning Server Model）的组成数据条目（Composition Data Entry）。

## 11.3\_详细说明（Detailed Documentation）

<a id="ga49c08c3e98b0c3863dd79b37aea25b34"></a>

### `BT_MESH_MODEL_RPR_SRV`

```c
#define BT_MESH_MODEL_RPR_SRV
```

```c
#include <zephyr/bluetooth/mesh/rpr_srv.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_REMOTE_PROV_SRV,                     \
                 _bt_mesh_rpr_srv_op, NULL, NULL,                      \
                 &_bt_mesh_rpr_srv_cb)
```

远程配置服务器模型（Remote Provisioning Server Model）的组成数据条目（Composition Data Entry）。


## 11.4\_原页交叉引用（Cross References）

- [rpr_srv.h](../api_file_supplement_reference/P100_zephyr__bluetooth__mesh__rpr_srv.h_文件参考.md)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_ID_REMOTE_PROV_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#ga9c7d1c5dfb87a5ce50c08747af47414f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_ga9c7d1c5dfb87a5ce50c08747af47414f"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>

---

[上一章](P010_蓝牙 Mesh 私有信标服务器（Private Beacon Server）.md) · [返回大纲](大纲.md) · [下一章](P012_分段与重组（SAR）配置公共头文件.md)
