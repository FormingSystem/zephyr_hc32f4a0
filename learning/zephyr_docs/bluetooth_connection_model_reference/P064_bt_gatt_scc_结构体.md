---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-64
title: bt_gatt_scc_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__scc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_bt\_gatt\_scc\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__scc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

服务器特征配置（Server Characteristic Configuration）属性值。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

服务器特征配置属性值（Server Characteristic Configuration Attribute Value）。用于发现标准特征描述符值。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 64.1\_数据成员（Data Fields）

<a id="r_aa7ddf1810f6d47e59c364b7489823d00"></a>

```c
uint16_t flags
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[flags](#aa7ddf1810f6d47e59c364b7489823d00)。

服务器特征配置标志（Server Characteristic Configuration flags），由 `BT_GATT_SCC_*` 宏组成的位图。

## 64.2\_详细说明（Detailed Documentation）

<a id="aa7ddf1810f6d47e59c364b7489823d00"></a>

### `flags`

```c
uint16_t bt_gatt_scc::flags
```

服务器特征配置标志（Server Characteristic Configuration flags），由 `BT_GATT_SCC_*` 宏组成的位图。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 64.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P063_bt_gatt_read_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P065_bt_gatt_service_结构体.md)
