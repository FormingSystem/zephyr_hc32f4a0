---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-3
title: bt_aics_discover_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__aics__discover__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_bt\_aics\_discover\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__aics__discover__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

用于发现音频输入控制服务（AICS）实例的结构体。

```c
#include <zephyr/bluetooth/audio/aics.h>
```

<a id="details"></a>

用于发现音频输入控制服务（AICS）实例的结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_ab867f7d2ae219df0c479cce72d68842f"></a>

```c
uint16_t start_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[start_handle](#ab867f7d2ae219df0c479cce72d68842f)。

发现范围的起始句柄（Start Handle）。

<a id="r_ab2931e7c4a627e717d943b2907b264cb"></a>

```c
uint16_t end_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[end_handle](#ab2931e7c4a627e717d943b2907b264cb)。

发现范围的结束句柄（End Handle）。

## 3.2\_详细说明（Detailed Documentation）

<a id="ab2931e7c4a627e717d943b2907b264cb"></a>

### `end_handle`

```c
uint16_t bt_aics_discover_param::end_handle
```

发现范围的结束句柄（End Handle）。

通常是 `bt_gatt_include` 的 `end_handle`。

<a id="ab867f7d2ae219df0c479cce72d68842f"></a>

### `start_handle`

```c
uint16_t bt_aics_discover_param::start_handle
```

发现范围的起始句柄（Start Handle）。

通常是 `bt_gatt_include` 的 `start_handle`。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/aics.h`

## 3.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/aics.h](https://docs.zephyrproject.org/latest/doxygen/html/aics_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_gatt_include](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__include.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_bt_aics_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_bt_aics_register_param_结构体.md)
