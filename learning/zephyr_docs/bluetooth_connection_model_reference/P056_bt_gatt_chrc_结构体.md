---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-56
title: bt_gatt_chrc_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__chrc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_bt\_gatt\_chrc\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__chrc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

特征声明（Characteristic Declaration）的属性值。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

特征声明的属性值（Attribute Value of a Characteristic Declaration）。这是与该特征关联的数据；根据特征属性（Characteristic properties），GATT 客户端可以读取或写入它。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 56.1\_数据成员（Data Fields）

<a id="r_af3b4c22ae37b912c8edf58294cc50702"></a>

```c
const struct bt_uuid * uuid
```

相关声明：[bt_uuid](P131_bt_uuid_结构体.md)、[uuid](#af3b4c22ae37b912c8edf58294cc50702)。

特征通用唯一标识符（Characteristic UUID）。

<a id="r_a2ca6aec1a621fdfd12142a1188d37bd3"></a>

```c
uint16_t value_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[value_handle](#a2ca6aec1a621fdfd12142a1188d37bd3)。

特征值句柄（Characteristic Value handle）。

<a id="r_a81bb8257052d7c8d03b51acaa51e5011"></a>

```c
uint8_t properties
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[properties](#a81bb8257052d7c8d03b51acaa51e5011)。

特征属性（Characteristic properties），由 `BT_GATT_CHRC_*` 宏组成的位图。

## 56.2\_详细说明（Detailed Documentation）

<a id="a81bb8257052d7c8d03b51acaa51e5011"></a>

### `properties`

```c
uint8_t bt_gatt_chrc::properties
```

特征属性（Characteristic properties），由 `BT_GATT_CHRC_*` 宏组成的位图。

<a id="af3b4c22ae37b912c8edf58294cc50702"></a>

### `uuid`

```c
const struct bt_uuid* bt_gatt_chrc::uuid
```

特征通用唯一标识符（Characteristic UUID）。

<a id="a2ca6aec1a621fdfd12142a1188d37bd3"></a>

### `value_handle`

```c
uint16_t bt_gatt_chrc::value_handle
```

特征值句柄（Characteristic Value handle）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 56.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [bt_uuid](P131_bt_uuid_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P055_bt_gatt_cep_结构体.md) · [返回大纲](大纲.md) · [下一章](P057_bt_gatt_cpf_结构体.md)
