---
id: learning.zephyr-docs.api-platform-topic-reference.page-5
title: 操作码聚合器服务器模型（Opcodes Aggregator Server model）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_操作码聚合器服务器模型（Opcodes Aggregator Server model）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__op__agg__srv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 5.1\_文件（Files）

<a id="r_op_5Fagg_5Fsrv_2Eh"></a>

```c
file op_agg_srv.h
```

相关声明：[op_agg_srv.h](../api_file_supplement_reference/P081_zephyr__bluetooth__mesh__op_agg_srv.h_文件参考.md)。

蓝牙Mesh操作码聚合器服务器（Opcodes Aggregator Server）模型API的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_ga9729e918d83a5b86e2fb1d443d23558a"></a>

```c
#define BT_MESH_MODEL_OP_AGG_SRV
```

相关声明：[BT_MESH_MODEL_OP_AGG_SRV](#ga9729e918d83a5b86e2fb1d443d23558a)。

操作码聚合器服务器模型（Opcodes Aggregator Server Model）的组成数据条目（Composition Data Entry）。

## 5.3\_详细说明（Detailed Documentation）

<a id="ga9729e918d83a5b86e2fb1d443d23558a"></a>

### `BT_MESH_MODEL_OP_AGG_SRV`

```c
#define BT_MESH_MODEL_OP_AGG_SRV
```

```c
#include <zephyr/bluetooth/mesh/op_agg_srv.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_OP_AGG_SRV, _bt_mesh_op_agg_srv_op,  \
                 NULL, NULL, &_bt_mesh_op_agg_srv_cb)
```

操作码聚合器服务器模型（Opcodes Aggregator Server Model）的组成数据条目（Composition Data Entry）。

**说明（Note）**：注意（Note）：操作码聚合器服务器（Opcodes Aggregator Server）处理聚合消息（Aggregated Messages），将其分派到相应模型（Models）及其消息处理器（Message Handlers）。当前实现假设响应（Responses）在接收消息的同一执行上下文（Execution Context）中发送，不允许延后发送响应，例如从工作队列（Workqueue）发送。


## 5.4\_原页交叉引用（Cross References）

- [op_agg_srv.h](../api_file_supplement_reference/P081_zephyr__bluetooth__mesh__op_agg_srv.h_文件参考.md)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_ID_OP_AGG_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#ga5cf2bb09e5eaa299cfc6b7fe4ed66e9a)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_ga5cf2bb09e5eaa299cfc6b7fe4ed66e9a"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>

---

[上一章](P004_呼叫控制配置文件（Call Control Profile，CCP）.md) · [返回大纲](大纲.md) · [下一章](P006_Silicon Labs Series 2 和 Series 3 设备树辅助功能（Devicetree helpers）.md)
