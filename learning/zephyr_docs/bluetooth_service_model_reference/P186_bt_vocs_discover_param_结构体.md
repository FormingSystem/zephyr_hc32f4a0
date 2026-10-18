---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-186
title: bt_vocs_discover_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__vocs__discover__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第186章\_bt\_vocs\_discover\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__vocs__discover__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于发现音量偏移控制服务（Volume Offset Control Service）实例的结构。

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

<a id="details"></a>

用于发现音量偏移控制服务（Volume Offset Control Service）实例的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 186.1\_数据成员（Data Fields）

<a id="r_aca830a50436def0f422d05eba34273ed"></a>

```c
uint16_t start_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[start_handle](#aca830a50436def0f422d05eba34273ed)。

发现范围的起始句柄（Start Handle）。

<a id="r_a3811da3035bb1f0ff5d290eb60fb2fda"></a>

```c
uint16_t end_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[end_handle](#a3811da3035bb1f0ff5d290eb60fb2fda)。

发现范围的结束句柄（End Handle）。

## 186.2\_详细说明（Detailed Documentation）

<a id="a3811da3035bb1f0ff5d290eb60fb2fda"></a>

### `end_handle`

```c
uint16_t bt_vocs_discover_param::end_handle
```

发现范围的结束句柄（End Handle）。

通常是 `bt_gatt_include` 的 `end_handle`。

<a id="aca830a50436def0f422d05eba34273ed"></a>

### `start_handle`

```c
uint16_t bt_vocs_discover_param::start_handle
```

发现范围的起始句柄（Start Handle）。

通常是 `bt_gatt_include` 的 `start_handle`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/vocs.h`

## 186.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/vocs.h](https://docs.zephyrproject.org/latest/doxygen/html/vocs_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_gatt_include](../bluetooth_connection_model_reference/P060_bt_gatt_include_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P185_bt_vocs_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P187_bt_vocs_register_param_结构体.md)
