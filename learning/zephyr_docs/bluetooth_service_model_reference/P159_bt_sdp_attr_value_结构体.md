---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-159
title: bt_sdp_attr_value_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__attr__value.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第159章\_bt\_sdp\_attr\_value\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__attr__value.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

服务发现协议（SDP）属性值的容器结构。

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="details"></a>

服务发现协议（SDP）属性值容器结构体。保存已解析的任意受支持类型的属性值。`type` 字段指示联合体中的哪个成员包含实际值。此结构体为处理解析后的不同类型 SDP 属性值提供统一方式。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 159.1\_数据成员（Data Fields）

<a id="r_a36fe39424a1f3ed59c2f7addf6a3eb8a"></a>

```c
enum bt_sdp_attr_value_type type
```

相关声明：[bt_sdp_attr_value_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga5e4a45b7b860d82a111480c9f25c2666)、[type](#a36fe39424a1f3ed59c2f7addf6a3eb8a)。

属性值类型。

```c
union {
```

<a id="r_a9dc9011e2dcc3749562976344bcc518f"></a>

```c
bool value
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[value](#af1582544193e9598183d8bf6ea722dbc)。

布尔值；当 `type` 为 `BT_SDP_ATTR_VALUE_TYPE_BOOL` 时使用。

<a id="r_a99be14310edd57ae7b85c94b43410cfd"></a>

```c
struct bt_sdp_attr_value_uint uint
```

相关声明：[bt_sdp_attr_value_uint](P163_bt_sdp_attr_value_uint_结构体.md)、[uint](#a7a1c4a780d8712fbf16df75f8ebae05f)。

有符号整数值；当 `type` 为 `BT_SDP_ATTR_VALUE_TYPE_SINT` 时使用。

<a id="r_a7f92f04f5978a489b7d7927fd25da79e"></a>

```c
struct bt_sdp_attr_value_int sint
```

相关声明：[bt_sdp_attr_value_int](P160_bt_sdp_attr_value_int_结构体.md)、[sint](#ae5b6d1e373b37e2627b34e6da549098f)。

文本字符串值；当 `type` 为 `BT_SDP_ATTR_VALUE_TYPE_TEXT` 时使用。

<a id="r_a1420ed95375de5d29256eedd6afffe88"></a>

```c
struct bt_sdp_attr_value_text text
```

相关声明：[bt_sdp_attr_value_text](P162_bt_sdp_attr_value_text_结构体.md)、[text](#a2fc1e977a5b82f16b160c898cca1cff7)。

URL 字符串值；当 `type` 为 `BT_SDP_ATTR_VALUE_TYPE_URL` 时使用。

<a id="r_a0574d90a27aff89ab245a6c9576607a8"></a>

```c
struct bt_sdp_attr_value_url url
```

相关声明：[bt_sdp_attr_value_url](P164_bt_sdp_attr_value_url_结构体.md)、[url](#af6e3f74c2c405153654fcade2608eca0)。

<a id="r_a2b0c7336f6b26bddbd614869282d655e"></a>

```c
};
```

根据 `type` 保存实际属性值的联合体（union）。

## 159.2\_详细说明（Detailed Documentation）

<a id="a2b0c7336f6b26bddbd614869282d655e"></a>

### `[union]`

```c
union { ... } bt_sdp_attr_value
```

根据 `type` 保存实际属性值的联合体（union）。

<a id="ae5b6d1e373b37e2627b34e6da549098f"></a>

### `sint`

```c
struct bt_sdp_attr_value_int bt_sdp_attr_value::sint
```

文本字符串值；当 `type` 为 `BT_SDP_ATTR_VALUE_TYPE_TEXT` 时使用。

<a id="a2fc1e977a5b82f16b160c898cca1cff7"></a>

### `text`

```c
struct bt_sdp_attr_value_text bt_sdp_attr_value::text
```

URL 字符串值；当 `type` 为 `BT_SDP_ATTR_VALUE_TYPE_URL` 时使用。

<a id="a36fe39424a1f3ed59c2f7addf6a3eb8a"></a>

### `type`

```c
enum bt_sdp_attr_value_type bt_sdp_attr_value::type
```

属性值类型。

<a id="a7a1c4a780d8712fbf16df75f8ebae05f"></a>

### `uint`

```c
struct bt_sdp_attr_value_uint bt_sdp_attr_value::uint
```

有符号整数值；当 `type` 为 `BT_SDP_ATTR_VALUE_TYPE_SINT` 时使用。

<a id="af6e3f74c2c405153654fcade2608eca0"></a>

### `url`

```c
struct bt_sdp_attr_value_url bt_sdp_attr_value::url
```

<a id="af1582544193e9598183d8bf6ea722dbc"></a>

### `value`

```c
bool bt_sdp_attr_value::value
```

布尔值；当 `type` 为 `BT_SDP_ATTR_VALUE_TYPE_BOOL` 时使用。

无符号整数值；当 `type` 为 `BT_SDP_ATTR_VALUE_TYPE_UINT` 时使用。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/sdp.h`

## 159.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/sdp.h](https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h_source.html)
- [bt_sdp_attr_value_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#ga5e4a45b7b860d82a111480c9f25c2666)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_sdp_attr_value_uint](P163_bt_sdp_attr_value_uint_结构体.md)
- [bt_sdp_attr_value_int](P160_bt_sdp_attr_value_int_结构体.md)
- [bt_sdp_attr_value_text](P162_bt_sdp_attr_value_text_结构体.md)
- [bt_sdp_attr_value_url](P164_bt_sdp_attr_value_url_结构体.md)
- [bt_sdp_attr_value](P159_bt_sdp_attr_value_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P158_bt_rfcomm_server_结构体.md) · [返回大纲](大纲.md) · [下一章](P160_bt_sdp_attr_value_int_结构体.md)
