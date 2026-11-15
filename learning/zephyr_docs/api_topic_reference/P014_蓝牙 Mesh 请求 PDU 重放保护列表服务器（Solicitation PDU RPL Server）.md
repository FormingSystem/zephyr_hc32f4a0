---
id: learning.zephyr-docs.api-topic-reference.page-14
title: 蓝牙 Mesh 请求 PDU 重放保护列表服务器（Solicitation PDU RPL Server）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_蓝牙 Mesh 请求 PDU 重放保护列表服务器（Solicitation PDU RPL Server）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sol__pdu__rpl__srv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 14.1\_文件（Files）

<a id="r_sol_5Fpdu_5Frpl_5Fsrv_2Eh"></a>

```c
file sol_pdu_rpl_srv.h
```

相关声明：[sol_pdu_rpl_srv.h](../api_file_supplement_reference/P116_zephyr__bluetooth__mesh__sol_pdu_rpl_srv.h_文件参考.md)。

蓝牙Mesh请求PDU重放保护列表配置服务器（Solicitation PDU RPL Configuration Server）模型API的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.2\_宏定义（Macros）

<a id="r_gab32d54a2d8e7020107063b292a70f7b6"></a>

```c
#define BT_MESH_MODEL_SOL_PDU_RPL_SRV
```

相关声明：[BT_MESH_MODEL_SOL_PDU_RPL_SRV](#gab32d54a2d8e7020107063b292a70f7b6)。

征询协议数据单元重放保护列表服务器模型（Solicitation PDU RPL Server Model）的组成数据条目（Composition Data Entry）。

## 14.3\_详细说明（Detailed Documentation）

<a id="gab32d54a2d8e7020107063b292a70f7b6"></a>

### `BT_MESH_MODEL_SOL_PDU_RPL_SRV`

```c
#define BT_MESH_MODEL_SOL_PDU_RPL_SRV
```

```c
#include <zephyr/bluetooth/mesh/sol_pdu_rpl_srv.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_SOL_PDU_RPL_SRV,                     \
                 _bt_mesh_sol_pdu_rpl_srv_op, NULL, NULL,              \
                 &_bt_mesh_sol_pdu_rpl_srv_cb)
```

征询协议数据单元重放保护列表服务器模型（Solicitation PDU RPL Server Model）的组成数据条目（Composition Data Entry）。


## 14.4\_原页交叉引用（Cross References）

- [sol_pdu_rpl_srv.h](../api_file_supplement_reference/P116_zephyr__bluetooth__mesh__sol_pdu_rpl_srv.h_文件参考.md)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_ID_SOL_PDU_RPL_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#ga165bc198dadaa0d534ec82eb8192ebc0)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_ga165bc198dadaa0d534ec82eb8192ebc0"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>

---

[上一章](P013_蓝牙 Mesh 分段与重组配置服务器模型（SAR Configuration Server Model）.md) · [返回大纲](大纲.md) · [下一章](P015_设备专用蜂窝通信 API 扩展（Device-specific Cellular API extensions）.md)
