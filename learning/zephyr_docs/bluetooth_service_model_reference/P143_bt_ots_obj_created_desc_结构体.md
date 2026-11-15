---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-143
title: bt_ots_obj_created_desc_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__ots__obj__created__desc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第143章\_bt\_ots\_obj\_created\_desc\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__ots__obj__created__desc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对象传输服务（OTS）已创建对象的描述符。

```c
#include <zephyr/bluetooth/services/ots.h>
```

<a id="details"></a>

OTS 已创建对象的描述符。描述由应用创建的对象传输服务（OTS）对象。此描述符由 `bt_ots_cb::obj_created` 回调返回；该回调的文档进一步说明了如何区分服务器创建对象与客户端创建对象。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 143.1\_数据成员（Data Fields）

<a id="r_af69db0a3c56c6d3085f20fbb405b436e"></a>

```c
char * name
```

相关声明：[name](#af69db0a3c56c6d3085f20fbb405b436e)。

对象名称（Object name）。

<a id="r_adb52cffa29c08ee1131415faeaf13cda"></a>

```c
struct bt_ots_obj_size size
```

相关声明：[bt_ots_obj_size](P145_bt_ots_obj_size_结构体.md)、[size](#adb52cffa29c08ee1131415faeaf13cda)。

对象大小（Object size）。

<a id="r_a50b2b2ae0b87690d1995187bae577e8c"></a>

```c
uint32_t props
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[props](#a50b2b2ae0b87690d1995187bae577e8c)。

对象属性（Object properties）。

## 143.2\_详细说明（Detailed Documentation）

<a id="af69db0a3c56c6d3085f20fbb405b436e"></a>

### `name`

```c
char* bt_ots_obj_created_desc::name
```

对象名称（Object name）。

以空字符结尾的字符串形式表示的对象名称。

服务器创建新对象时，名称长度必须大于 0 且不超过 `BT_OTS_OBJ_MAX_NAME_LEN`。客户端创建新对象时，名称必须为空字符串。

<a id="a50b2b2ae0b87690d1995187bae577e8c"></a>

### `props`

```c
uint32_t bt_ots_obj_created_desc::props
```

对象属性（Object properties）。

<a id="adb52cffa29c08ee1131415faeaf13cda"></a>

### `size`

```c
struct bt_ots_obj_size bt_ots_obj_created_desc::size
```

对象大小（Object size）。

`bt_ots_obj_size::alloc` 必须大于或等于 `bt_ots_obj_add_param::size`。

服务器创建新对象时，`bt_ots_obj_size::cur` 必须小于或等于 `bt_ots_obj_add_param::size`。客户端创建新对象时，`bt_ots_obj_size::cur` 必须为 0。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/ots.h`

## 143.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/ots.h](https://docs.zephyrproject.org/latest/doxygen/html/ots_8h_source.html)
- [bt_ots_obj_size](P145_bt_ots_obj_size_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_ots_cb::obj_created](P136_bt_ots_cb_结构体.md#a0c95b2bc382474be3c1ae849936a8206)
- [bt_ots_obj_size::alloc](P145_bt_ots_obj_size_结构体.md#a86a5675532eae69d40b3305436e81cfb)
- [bt_ots_obj_add_param::size](P142_bt_ots_obj_add_param_结构体.md#a721734439b43e40324c3a548b5a4eb34)
- [bt_ots_obj_size::cur](P145_bt_ots_obj_size_结构体.md#a217290f0fae68a54046eef50ac2a3773)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P142_bt_ots_obj_add_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P144_bt_ots_obj_metadata_结构体.md)
