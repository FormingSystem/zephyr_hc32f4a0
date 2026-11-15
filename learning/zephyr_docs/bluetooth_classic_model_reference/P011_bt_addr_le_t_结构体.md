---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-11
title: bt_addr_le_t_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__addr__le__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_bt\_addr\_le\_t\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__addr__le__t.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

蓝牙低功耗（Bluetooth LE）设备地址。

```c
#include <zephyr/bluetooth/addr.h>
```

<a id="details"></a>

蓝牙低功耗（Bluetooth LE）设备地址。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_aa4ede005c57893383a21983bc3e47958"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#aa4ede005c57893383a21983bc3e47958)。

<a id="r_aacada5fc5b04ff22a02518e6f59387ed"></a>

```c
bt_addr_t a
```

相关声明：[bt_addr_t](P012_bt_addr_t_结构体.md)、[a](#aacada5fc5b04ff22a02518e6f59387ed)。

## 11.2\_详细说明（Detailed Documentation）

<a id="aacada5fc5b04ff22a02518e6f59387ed"></a>

### `a`

```c
bt_addr_t bt_addr_le_t::a
```

<a id="aa4ede005c57893383a21983bc3e47958"></a>

### `type`

```c
uint8_t bt_addr_le_t::type
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/addr.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_t](P012_bt_addr_t_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_bt_a2dp_stream_ops_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_bt_addr_t_结构体.md)
