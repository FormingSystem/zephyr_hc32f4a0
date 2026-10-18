---
id: learning.zephyr-docs.modem-wireless-model-reference.page-14
title: esp_wifi_mesh_event_info_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structesp__wifi__mesh__event__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_esp\_wifi\_mesh\_event\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structesp__wifi__mesh__event__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

随Mesh事件提供的信息。

```c
#include <zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h>
```

<a id="details"></a>

随Mesh事件提供的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_a90676505f5e1d0df03bf245cbb16f2c0"></a>

```c
int layer
```

相关声明：[layer](#a90676505f5e1d0df03bf245cbb16f2c0)。

当前 Mesh 层级，即树深度；尚未接入时为 -1。

<a id="r_a69fa2fd2f6c244b1c730ecb880165728"></a>

```c
bool is_root
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_root](#a69fa2fd2f6c244b1c730ecb880165728)。

此节点是 Mesh 根节点时为 `true`。

<a id="r_af1702d5f2359103b31cc8d8ff7346f6e"></a>

```c
int routing_table_size
```

相关声明：[routing_table_size](#af1702d5f2359103b31cc8d8ff7346f6e)。

当前路由表大小，对路由表事件有效。

<a id="r_af5a036d50b7f2a8b878fdc262a91acd0"></a>

```c
int reason
```

相关声明：[reason](#af5a036d50b7f2a8b878fdc262a91acd0)。

断开原因，对断连事件有效。

## 14.2\_详细说明（Detailed Documentation）

<a id="a69fa2fd2f6c244b1c730ecb880165728"></a>

### `is_root`

```c
bool esp_wifi_mesh_event_info::is_root
```

此节点是 Mesh 根节点时为 `true`。

<a id="a90676505f5e1d0df03bf245cbb16f2c0"></a>

### `layer`

```c
int esp_wifi_mesh_event_info::layer
```

当前 Mesh 层级，即树深度；尚未接入时为 -1。

<a id="af5a036d50b7f2a8b878fdc262a91acd0"></a>

### `reason`

```c
int esp_wifi_mesh_event_info::reason
```

断开原因，对断连事件有效。

<a id="af1702d5f2359103b31cc8d8ff7346f6e"></a>

### `routing_table_size`

```c
int esp_wifi_mesh_event_info::routing_table_size
```

当前路由表大小，对路由表事件有效。

本数据类型文档由以下文件生成：

- `zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/esp__wifi__mesh_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_esp_wifi_mesh_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_esp_wifi_mesh_status_结构体.md)
