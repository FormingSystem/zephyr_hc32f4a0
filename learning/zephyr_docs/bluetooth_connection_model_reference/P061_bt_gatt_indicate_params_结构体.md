---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-61
title: bt_gatt_indicate_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__indicate__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_bt\_gatt\_indicate\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__indicate__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GATT 值指示（Indicate Value）参数。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

GATT 值指示参数（GATT Indicate Value parameters）。另见使用此参数的 `bt_gatt_indicate`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 61.1\_数据成员（Data Fields）

<a id="r_afde06f47d7a817291e437593ea01bccd"></a>

```c
const struct bt_uuid * uuid
```

相关声明：[bt_uuid](P131_bt_uuid_结构体.md)、[uuid](#afde06f47d7a817291e437593ea01bccd)。

指示属性的通用唯一标识符类型（Indicate Attribute UUID type）。

<a id="r_acbbee3a71838492416b20bb5cff89801"></a>

```c
const struct bt_gatt_attr * attr
```

相关声明：[bt_gatt_attr](P049_bt_gatt_attr_结构体.md)、[attr](#acbbee3a71838492416b20bb5cff89801)。

指示属性对象（Indicate Attribute object）。

<a id="r_af9eb83c3fba49ee3cd6162d5a2791707"></a>

```c
bt_gatt_indicate_func_t func
```

相关声明：[bt_gatt_indicate_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga1294850e6bdcbe7a8f42f2956fd837a8)、[func](#af9eb83c3fba49ee3cd6162d5a2791707)。

值指示回调（Indicate Value callback）。

<a id="r_aeb346dc4c0e4a298c66f394d037a6514"></a>

```c
bt_gatt_indicate_params_destroy_t destroy
```

相关声明：[bt_gatt_indicate_params_destroy_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga5d47ed9eaea22c8f00db14329daee8fe)、[destroy](#aeb346dc4c0e4a298c66f394d037a6514)。

指示操作完成回调（Indicate operation complete callback）。

<a id="r_ae1d657512c99d5bba6fc99a450a6da32"></a>

```c
const void * data
```

相关声明：[data](#ae1d657512c99d5bba6fc99a450a6da32)。

指示值数据（Indicate Value data）。

<a id="r_a10ad44140371165951eeac18cb3d0e7f"></a>

```c
uint16_t len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[len](#a10ad44140371165951eeac18cb3d0e7f)。

指示值长度（Indicate Value length）。

<a id="r_a0e536938123ecb4f3ba6736c1de2a599"></a>

```c
enum bt_att_chan_opt chan_opt
```

相关声明：[bt_att_chan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac593a27ecf029f33f50f990b2947562c)、[chan_opt](#a0e536938123ecb4f3ba6736c1de2a599)。

属性协议通道选项（ATT channel options）。

## 61.2\_详细说明（Detailed Documentation）

<a id="acbbee3a71838492416b20bb5cff89801"></a>

### `attr`

```c
const struct bt_gatt_attr* bt_gatt_indicate_params::attr
```

指示属性对象（Indicate Attribute object）。

提供了 `uuid` 时，此项为可选；此时将以它作为搜索范围的起点，查找具有指定 UUID 的属性（Attribute）。

<a id="a0e536938123ecb4f3ba6736c1de2a599"></a>

### `chan_opt`

```c
enum bt_att_chan_opt bt_gatt_indicate_params::chan_opt
```

属性协议通道选项（ATT channel options）。

<a id="ae1d657512c99d5bba6fc99a450a6da32"></a>

### `data`

```c
const void* bt_gatt_indicate_params::data
```

指示值数据（Indicate Value data）。

<a id="aeb346dc4c0e4a298c66f394d037a6514"></a>

### `destroy`

```c
bt_gatt_indicate_params_destroy_t bt_gatt_indicate_params::destroy
```

指示操作完成回调（Indicate operation complete callback）。

<a id="af9eb83c3fba49ee3cd6162d5a2791707"></a>

### `func`

```c
bt_gatt_indicate_func_t bt_gatt_indicate_params::func
```

值指示回调（Indicate Value callback）。

<a id="a10ad44140371165951eeac18cb3d0e7f"></a>

### `len`

```c
uint16_t bt_gatt_indicate_params::len
```

指示值长度（Indicate Value length）。

<a id="afde06f47d7a817291e437593ea01bccd"></a>

### `uuid`

```c
const struct bt_uuid* bt_gatt_indicate_params::uuid
```

指示属性的通用唯一标识符类型（Indicate Attribute UUID type）。

可选；不知道属性对象指针（Attribute object pointer）时，用于搜索具有匹配 UUID 的属性。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 61.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [bt_uuid](P131_bt_uuid_结构体.md)
- [bt_gatt_attr](P049_bt_gatt_attr_结构体.md)
- [bt_gatt_indicate_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga1294850e6bdcbe7a8f42f2956fd837a8)
- [bt_gatt_indicate_params_destroy_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga5d47ed9eaea22c8f00db14329daee8fe)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_att_chan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac593a27ecf029f33f50f990b2947562c)
- [bt_gatt_indicate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga4f2272692cc0f1d44638828012296c80)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P060_bt_gatt_include_结构体.md) · [返回大纲](大纲.md) · [下一章](P062_bt_gatt_notify_params_结构体.md)
