---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-69
title: bt_gatt_write_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__write__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_bt\_gatt\_write\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__write__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GATT 写入（Write）参数。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

GATT 写入（Write）参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 69.1\_数据成员（Data Fields）

<a id="r_a3468e3b75f3f9eda12bc4963f48cf9aa"></a>

```c
bt_gatt_write_func_t func
```

相关声明：[bt_gatt_write_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga2bca8c4a45f41e0400a9e0147f4baf50)、[func](#a3468e3b75f3f9eda12bc4963f48cf9aa)。

响应回调（Response callback）。

<a id="r_a384c5c15f248df5b327423ca32637bad"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a384c5c15f248df5b327423ca32637bad)。

属性句柄（Attribute handle）。

<a id="r_add53cc08465d28f33bc48a1e8649ac1a"></a>

```c
uint16_t offset
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[offset](#add53cc08465d28f33bc48a1e8649ac1a)。

属性数据偏移量（Attribute data offset）。

<a id="r_ab6510ef242e73325adb074322746c27c"></a>

```c
const void * data
```

相关声明：[data](#ab6510ef242e73325adb074322746c27c)。

要写入的数据（Data to be written）。

<a id="r_aded956dac2d398b642faeec81fdb9ec3"></a>

```c
uint16_t length
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[length](#aded956dac2d398b642faeec81fdb9ec3)。

数据长度（Data Length）。

<a id="r_ad79905c16f7ba5289817de552ece1a48"></a>

```c
enum bt_att_chan_opt chan_opt
```

相关声明：[bt_att_chan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac593a27ecf029f33f50f990b2947562c)、[chan_opt](#ad79905c16f7ba5289817de552ece1a48)。

属性协议通道选项（ATT channel options）。

## 69.2\_详细说明（Detailed Documentation）

<a id="ad79905c16f7ba5289817de552ece1a48"></a>

### `chan_opt`

```c
enum bt_att_chan_opt bt_gatt_write_params::chan_opt
```

属性协议通道选项（ATT channel options）。

<a id="ab6510ef242e73325adb074322746c27c"></a>

### `data`

```c
const void* bt_gatt_write_params::data
```

要写入的数据（Data to be written）。

<a id="a3468e3b75f3f9eda12bc4963f48cf9aa"></a>

### `func`

```c
bt_gatt_write_func_t bt_gatt_write_params::func
```

响应回调（Response callback）。

<a id="a384c5c15f248df5b327423ca32637bad"></a>

### `handle`

```c
uint16_t bt_gatt_write_params::handle
```

属性句柄（Attribute handle）。

<a id="aded956dac2d398b642faeec81fdb9ec3"></a>

### `length`

```c
uint16_t bt_gatt_write_params::length
```

数据长度（Data Length）。

<a id="add53cc08465d28f33bc48a1e8649ac1a"></a>

### `offset`

```c
uint16_t bt_gatt_write_params::offset
```

属性数据偏移量（Attribute data offset）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 69.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [bt_gatt_write_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga2bca8c4a45f41e0400a9e0147f4baf50)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_att_chan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac593a27ecf029f33f50f990b2947562c)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P068_bt_gatt_subscribe_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P070_bt_iso_accept_info_结构体.md)
