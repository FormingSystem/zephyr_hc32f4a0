---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-133
title: bt_obex_tlv_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__obex__tlv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第133章\_bt\_obex\_tlv\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__obex__tlv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙对象交换协议（Bluetooth OBEX）的类型-长度-值（TLV）三元组。

```c
#include <zephyr/bluetooth/classic/obex.h>
```

<a id="details"></a>

蓝牙 OBEX 的类型—长度—值（TLV）三元组。描述可编码为 TLV 三元组的不同数据类型，用于组成传给 `bt_obex_add_header_app_param()`、`bt_obex_add_header_auth_challenge()` 和 `bt_obex_add_header_auth_rsp()` 函数的数组。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 133.1\_数据成员（Data Fields）

<a id="r_abb39dc76c06c3dd89a739f3111d143b5"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#abb39dc76c06c3dd89a739f3111d143b5)。

<a id="r_addcdfe5b297fe7cd9e1f30eee8ade4d7"></a>

```c
uint8_t data_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_len](#addcdfe5b297fe7cd9e1f30eee8ade4d7)。

<a id="r_a18d22dae9d1f069d2403398454fadd45"></a>

```c
const uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a18d22dae9d1f069d2403398454fadd45)。

## 133.2\_详细说明（Detailed Documentation）

<a id="a18d22dae9d1f069d2403398454fadd45"></a>

### `data`

```c
const uint8_t* bt_obex_tlv::data
```

<a id="addcdfe5b297fe7cd9e1f30eee8ade4d7"></a>

### `data_len`

```c
uint8_t bt_obex_tlv::data_len
```

<a id="abb39dc76c06c3dd89a739f3111d143b5"></a>

### `type`

```c
uint8_t bt_obex_tlv::type
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/obex.h`

## 133.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/obex.h](https://docs.zephyrproject.org/latest/doxygen/html/obex_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_obex_add_header_app_param()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gaeacfe7cb654bf33e7b387358a19fd3d3)
- [bt_obex_add_header_auth_challenge()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#gacfc897d66e8c14629fa4d94f3782c741)
- [bt_obex_add_header_auth_rsp()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga5433561f0e9bad6da2d94dccca1578de)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P132_bt_obex_server_ops_结构体.md) · [返回大纲](大纲.md) · [下一章](P134_bt_obex_transport_ops_结构体.md)
