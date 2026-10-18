---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-144
title: bt_ots_obj_metadata_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__ots__obj__metadata.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第144章\_bt\_ots\_obj\_metadata\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__ots__obj__metadata.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对象传输服务（OTS）对象的元数据。

```c
#include <zephyr/bluetooth/services/ots.h>
```

<a id="details"></a>

OTS 对象的元数据（Metadata）。服务器将其用作 OTS 对象初始化的描述符；客户端使用它向应用提供对象元数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 144.1\_数据成员（Data Fields）

<a id="r_a63b154d9a40a170acc8a632cbb00602f"></a>

```c
char * name
```

相关声明：[name](#a63b154d9a40a170acc8a632cbb00602f)。

对象名称（Object Name）。

<a id="r_aabaa62092e281f3278b69297eedcc7d6"></a>

```c
char name_c [CONFIG_BT_OTS_OBJ_MAX_NAME_LEN+1]
```

相关声明：[name_c](#aabaa62092e281f3278b69297eedcc7d6)。

对象名称（客户端）。

<a id="r_aee93aef1932e9c8b4cb0c8055e5cb055"></a>

```c
struct bt_ots_obj_type type
```

相关声明：[bt_ots_obj_type](P146_bt_ots_obj_type_结构体.md)、[type](#aee93aef1932e9c8b4cb0c8055e5cb055)。

对象类型（Object Type）。

<a id="r_afd451a3b531250db1d45eb6ddb4d9b0f"></a>

```c
struct bt_ots_obj_size size
```

相关声明：[bt_ots_obj_size](P145_bt_ots_obj_size_结构体.md)、[size](#afd451a3b531250db1d45eb6ddb4d9b0f)。

对象大小（Object Size）。

<a id="r_a6a564d53607261992bb4d3fc9035c23c"></a>

```c
struct bt_ots_date_time first_created
```

相关声明：[bt_ots_date_time](P139_bt_ots_date_time_结构体.md)、[first_created](#a6a564d53607261992bb4d3fc9035c23c)。

对象首次创建时间（first created time）。

<a id="r_a91f8183d1eac783b277fe6b040378b2f"></a>

```c
struct bt_ots_date_time modified
```

相关声明：[bt_ots_date_time](P139_bt_ots_date_time_结构体.md)、[modified](#a91f8183d1eac783b277fe6b040378b2f)。

对象最后修改时间（last modified time）。

<a id="r_aa51fd3166fedebbe0d6c66cfbe9ba649"></a>

```c
uint64_t id
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[id](#aa51fd3166fedebbe0d6c66cfbe9ba649)。

对象标识（Object ID）。

<a id="r_aa4ffe00ede40ff23ab5788c82ec2ac38"></a>

```c
uint32_t props
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[props](#aa4ffe00ede40ff23ab5788c82ec2ac38)。

对象属性（Object Properties）。

## 144.2\_详细说明（Detailed Documentation）

<a id="a6a564d53607261992bb4d3fc9035c23c"></a>

### `first_created`

```c
struct bt_ots_date_time bt_ots_obj_metadata::first_created
```

对象首次创建时间（first created time）。

<a id="aa51fd3166fedebbe0d6c66cfbe9ba649"></a>

### `id`

```c
uint64_t bt_ots_obj_metadata::id
```

对象标识（Object ID）。

<a id="a91f8183d1eac783b277fe6b040378b2f"></a>

### `modified`

```c
struct bt_ots_date_time bt_ots_obj_metadata::modified
```

对象最后修改时间（last modified time）。

<a id="a63b154d9a40a170acc8a632cbb00602f"></a>

### `name`

```c
char* bt_ots_obj_metadata::name
```

对象名称（Object Name）。

<a id="aabaa62092e281f3278b69297eedcc7d6"></a>

### `name_c`

```c
char bt_ots_obj_metadata::name_c[CONFIG_BT_OTS_OBJ_MAX_NAME_LEN+1]
```

对象名称（客户端）。

<a id="aa4ffe00ede40ff23ab5788c82ec2ac38"></a>

### `props`

```c
uint32_t bt_ots_obj_metadata::props
```

对象属性（Object Properties）。

<a id="afd451a3b531250db1d45eb6ddb4d9b0f"></a>

### `size`

```c
struct bt_ots_obj_size bt_ots_obj_metadata::size
```

对象大小（Object Size）。

<a id="aee93aef1932e9c8b4cb0c8055e5cb055"></a>

### `type`

```c
struct bt_ots_obj_type bt_ots_obj_metadata::type
```

对象类型（Object Type）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/ots.h`

## 144.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/ots.h](https://docs.zephyrproject.org/latest/doxygen/html/ots_8h_source.html)
- [bt_ots_obj_type](P146_bt_ots_obj_type_结构体.md)
- [bt_ots_obj_size](P145_bt_ots_obj_size_结构体.md)
- [bt_ots_date_time](P139_bt_ots_date_time_结构体.md)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P143_bt_ots_obj_created_desc_结构体.md) · [返回大纲](大纲.md) · [下一章](P145_bt_ots_obj_size_结构体.md)
