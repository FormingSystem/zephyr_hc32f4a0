---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-52
title: bt_gatt_ccc_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__ccc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_bt\_gatt\_ccc\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__ccc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

客户端特征配置（Client Characteristic Configuration，CCC）属性值。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

客户端特征配置属性值（Client Characteristic Configuration Attribute Value）。用于发现标准特征描述符值（Standard characteristic descriptor values）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 52.1\_数据成员（Data Fields）

<a id="r_ac8fa1028c5e87aa025832257b18fa7c3"></a>

```c
uint16_t flags
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[flags](#ac8fa1028c5e87aa025832257b18fa7c3)。

客户端特征配置标志（Client Characteristic Configuration flags），由 `BT_GATT_CCC_*` 宏组成的位图。

## 52.2\_详细说明（Detailed Documentation）

<a id="ac8fa1028c5e87aa025832257b18fa7c3"></a>

### `flags`

```c
uint16_t bt_gatt_ccc::flags
```

客户端特征配置标志（Client Characteristic Configuration flags），由 `BT_GATT_CCC_*` 宏组成的位图。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 52.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P051_bt_gatt_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P053_bt_gatt_ccc_cfg_结构体.md)
