---
id: learning.zephyr-docs.api-topic-reference.page-9
title: 蓝牙 Mesh 按需私有 GATT 代理服务器（On-Demand Private GATT Proxy Server）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_蓝牙 Mesh 按需私有 GATT 代理服务器（On-Demand Private GATT Proxy Server）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__srv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 9.1\_文件（Files）

<a id="r_od_5Fpriv_5Fproxy_5Fsrv_2Eh"></a>

```c
file od_priv_proxy_srv.h
```

相关声明：[od_priv_proxy_srv.h](../api_file_supplement_reference/P080_zephyr__bluetooth__mesh__od_priv_proxy_srv.h_文件参考.md)。

蓝牙Mesh按需私有GATT代理服务器（On-Demand Private GATT Proxy Server）模型API的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="r_gaa3c6451144f696ef9e67494165283c41"></a>

```c
#define BT_MESH_MODEL_OD_PRIV_PROXY_SRV
```

相关声明：[BT_MESH_MODEL_OD_PRIV_PROXY_SRV](#gaa3c6451144f696ef9e67494165283c41)。

按需私有代理服务器模型（On-Demand Private Proxy Server Model）的组成数据条目（Composition Data Entry）。

## 9.3\_详细说明（Detailed Documentation）

<a id="gaa3c6451144f696ef9e67494165283c41"></a>

### `BT_MESH_MODEL_OD_PRIV_PROXY_SRV`

```c
#define BT_MESH_MODEL_OD_PRIV_PROXY_SRV
```

```c
#include <zephyr/bluetooth/mesh/od_priv_proxy_srv.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_SOL_PDU_RPL_SRV,                                           \
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_ON_DEMAND_PROXY_SRV,                   \
                 _bt_mesh_od_priv_proxy_srv_op, NULL, NULL,              \
                 &_bt_mesh_od_priv_proxy_srv_cb)
```

按需私有代理服务器模型（On-Demand Private Proxy Server Model）的组成数据条目（Composition Data Entry）。


## 9.4\_原页交叉引用（Cross References）

- [od_priv_proxy_srv.h](../api_file_supplement_reference/P080_zephyr__bluetooth__mesh__od_priv_proxy_srv.h_文件参考.md)
- [BT_MESH_MODEL_SOL_PDU_RPL_SRV](P014_蓝牙 Mesh 请求 PDU 重放保护列表服务器（Solicitation PDU RPL Server）.md#gab32d54a2d8e7020107063b292a70f7b6)
- [BT_MESH_MODEL_ID_ON_DEMAND_PROXY_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#gaddc0bd645180a57cb9cd36745b84f7a1)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_gaddc0bd645180a57cb9cd36745b84f7a1"></a>
<a id="agroup__bt__mesh__sol__pdu__rpl__srv_html_gab32d54a2d8e7020107063b292a70f7b6"></a>

---

[上一章](P008_大型组成数据服务器模型（Large Composition Data Server model）.md) · [返回大纲](大纲.md) · [下一章](P010_蓝牙 Mesh 私有信标服务器（Private Beacon Server）.md)
