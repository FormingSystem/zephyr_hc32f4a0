---
id: learning.zephyr-docs.modem-wireless-model-reference.page-15
title: esp_wifi_mesh_status_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structesp__wifi__mesh__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_esp\_wifi\_mesh\_status\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structesp__wifi__mesh__status.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

当前Mesh状态快照（Status Snapshot）。

```c
#include <zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h>
```

<a id="details"></a>

当前Mesh状态快照（Status Snapshot）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_ad796be56b81338faa45d47fd60e0cac5"></a>

```c
int layer
```

相关声明：[layer](#ad796be56b81338faa45d47fd60e0cac5)。

当前 Mesh 层级，即树深度；尚未接入时为 -1。

<a id="r_a3c7f1798e50aab22882586a0b388b135"></a>

```c
bool is_root
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_root](#a3c7f1798e50aab22882586a0b388b135)。

此节点是 Mesh 根节点时为 `true`。

<a id="r_a9e7451c7e2ad2780279db9db50f319f1"></a>

```c
int routing_table_size
```

相关声明：[routing_table_size](#a9e7451c7e2ad2780279db9db50f319f1)。

路由表中的节点数量；对于根节点，表示整个子网络的节点数量。

<a id="r_ab4962e3da36ca5f7a883a16994058d5a"></a>

```c
bool tods_reachable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[tods_reachable](#ab4962e3da36ca5f7a883a16994058d5a)。

根节点已宣告外部网络可达后为 `true`。

## 15.2\_详细说明（Detailed Documentation）

<a id="a3c7f1798e50aab22882586a0b388b135"></a>

### `is_root`

```c
bool esp_wifi_mesh_status::is_root
```

此节点是 Mesh 根节点时为 `true`。

<a id="ad796be56b81338faa45d47fd60e0cac5"></a>

### `layer`

```c
int esp_wifi_mesh_status::layer
```

当前 Mesh 层级，即树深度；尚未接入时为 -1。

<a id="a9e7451c7e2ad2780279db9db50f319f1"></a>

### `routing_table_size`

```c
int esp_wifi_mesh_status::routing_table_size
```

路由表中的节点数量；对于根节点，表示整个子网络的节点数量。

<a id="ab4962e3da36ca5f7a883a16994058d5a"></a>

### `tods_reachable`

```c
bool esp_wifi_mesh_status::tods_reachable
```

根节点已宣告外部网络可达后为 `true`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/esp__wifi__mesh_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P014_esp_wifi_mesh_event_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P016_hl78xx_agnss_status_结构体.md)
