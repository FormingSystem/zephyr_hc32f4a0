---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-62
title: bt_gatt_notify_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__notify__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_bt\_gatt\_notify\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__notify__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GATT 通知（Notification）参数。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

GATT 通知参数（GATT notification parameters）。另见使用此参数的 `bt_gatt_notify_cb` 和 `bt_gatt_notify_multiple`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 62.1\_数据成员（Data Fields）

<a id="r_a2994cbe737fad725c60427000c21c373"></a>

```c
const struct bt_uuid * uuid
```

相关声明：[bt_uuid](P131_bt_uuid_结构体.md)、[uuid](#a2994cbe737fad725c60427000c21c373)。

通知属性的通用唯一标识符类型（Notification Attribute UUID type）。

<a id="r_a6187d0457763a15a623129e3e9e98e13"></a>

```c
const struct bt_gatt_attr * attr
```

相关声明：[bt_gatt_attr](P049_bt_gatt_attr_结构体.md)、[attr](#a6187d0457763a15a623129e3e9e98e13)。

通知属性对象（Notification Attribute object）。

<a id="r_afaa276cff9cbf204c433ca776904ef32"></a>

```c
const void * data
```

相关声明：[data](#afaa276cff9cbf204c433ca776904ef32)。

通知值数据（Notification Value data）。

<a id="r_a4a511da0b099ca88d895594caf7aaa6a"></a>

```c
uint16_t len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[len](#a4a511da0b099ca88d895594caf7aaa6a)。

通知值长度（Notification Value length）。

<a id="r_ace3c6b5f5ed78b9f64c25b868d3bfbe2"></a>

```c
bt_gatt_complete_func_t func
```

相关声明：[bt_gatt_complete_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gac55832607b95f394d26a64ed1cfe5bba)、[func](#ace3c6b5f5ed78b9f64c25b868d3bfbe2)。

通知值回调（Notification Value callback）。

<a id="r_adec9a6f6ea0604e82b90dd47bb9951fa"></a>

```c
void * user_data
```

相关声明：[user_data](#adec9a6f6ea0604e82b90dd47bb9951fa)。

通知值回调用户数据（Notification Value callback user data）。

<a id="r_a978d7a42c39a098cedf751936f280fac"></a>

```c
enum bt_att_chan_opt chan_opt
```

相关声明：[bt_att_chan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac593a27ecf029f33f50f990b2947562c)、[chan_opt](#a978d7a42c39a098cedf751936f280fac)。

属性协议通道选项（ATT channel options）。

## 62.2\_详细说明（Detailed Documentation）

<a id="a6187d0457763a15a623129e3e9e98e13"></a>

### `attr`

```c
const struct bt_gatt_attr* bt_gatt_notify_params::attr
```

通知属性对象（Notification Attribute object）。

提供了 `uuid` 时，此项为可选；此时将以它作为搜索范围的起点，查找具有指定 UUID 的属性（Attribute）。

<a id="a978d7a42c39a098cedf751936f280fac"></a>

### `chan_opt`

```c
enum bt_att_chan_opt bt_gatt_notify_params::chan_opt
```

属性协议通道选项（ATT channel options）。

<a id="afaa276cff9cbf204c433ca776904ef32"></a>

### `data`

```c
const void* bt_gatt_notify_params::data
```

通知值数据（Notification Value data）。

<a id="ace3c6b5f5ed78b9f64c25b868d3bfbe2"></a>

### `func`

```c
bt_gatt_complete_func_t bt_gatt_notify_params::func
```

通知值回调（Notification Value callback）。

<a id="a4a511da0b099ca88d895594caf7aaa6a"></a>

### `len`

```c
uint16_t bt_gatt_notify_params::len
```

通知值长度（Notification Value length）。

<a id="adec9a6f6ea0604e82b90dd47bb9951fa"></a>

### `user_data`

```c
void* bt_gatt_notify_params::user_data
```

通知值回调用户数据（Notification Value callback user data）。

<a id="a2994cbe737fad725c60427000c21c373"></a>

### `uuid`

```c
const struct bt_uuid* bt_gatt_notify_params::uuid
```

通知属性的通用唯一标识符类型（Notification Attribute UUID type）。

可选；不知道属性对象指针（Attribute object pointer）时，用于搜索具有匹配 UUID 的属性。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 62.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [bt_uuid](P131_bt_uuid_结构体.md)
- [bt_gatt_attr](P049_bt_gatt_attr_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_gatt_complete_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#gac55832607b95f394d26a64ed1cfe5bba)
- [bt_att_chan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac593a27ecf029f33f50f990b2947562c)
- [bt_gatt_notify_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga55e3ef7cb43b8acb0a27643c78390146)
- [bt_gatt_notify_multiple](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga8071d6063f85c0a78155f6b2ac2da635)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P061_bt_gatt_indicate_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P063_bt_gatt_read_params_结构体.md)
