---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-55
title: bt_gatt_cep_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__cep.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_bt\_gatt\_cep\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__cep.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

特征扩展属性（Characteristic Extended Properties）属性值。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

特征扩展属性的属性值（Characteristic Extended Properties Attribute Value）。用于发现标准特征描述符值。若特征属性（Characteristic properties）中设置了 `BT_GATT_CHRC_EXT_PROP` 位，则此项必须存在。可与 `BT_GATT_CEP` 宏配合使用，声明特征扩展属性描述符（CEP descriptor）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 55.1\_数据成员（Data Fields）

<a id="r_a317442dc204f7632b0c5da8a8a9a98b5"></a>

```c
uint16_t properties
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[properties](#a317442dc204f7632b0c5da8a8a9a98b5)。

特征扩展属性（Characteristic Extended properties），由 `BT_GATT_CEP_*` 宏组成的位图。

## 55.2\_详细说明（Detailed Documentation）

<a id="a317442dc204f7632b0c5da8a8a9a98b5"></a>

### `properties`

```c
uint16_t bt_gatt_cep::properties
```

特征扩展属性（Characteristic Extended properties），由 `BT_GATT_CEP_*` 宏组成的位图。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 55.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [BT_GATT_CHRC_EXT_PROP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#gac84d73a0ad50bfd149ad83181315de1a)
- [BT_GATT_CEP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga55a82cada1093c4ff75fe5504ac504b1)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P054_bt_gatt_ccc_managed_user_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P056_bt_gatt_chrc_结构体.md)
