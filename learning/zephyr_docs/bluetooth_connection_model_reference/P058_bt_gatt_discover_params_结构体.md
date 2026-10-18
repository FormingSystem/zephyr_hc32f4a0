---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-58
title: bt_gatt_discover_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__discover__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_bt\_gatt\_discover\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__discover__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GATT 属性发现（Discover Attributes）参数。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

GATT 属性发现（Discover Attributes）参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 58.1\_数据成员（Data Fields）

<a id="r_a77d6665c01902e4e23cf8de8a9436262"></a>

```c
const struct bt_uuid * uuid
```

相关声明：[bt_uuid](P131_bt_uuid_结构体.md)、[uuid](#a77d6665c01902e4e23cf8de8a9436262)。

要发现的通用唯一标识符类型（UUID type）。

<a id="r_a337d7366c12451938f12eec4dc60903e"></a>

```c
bt_gatt_discover_func_t func
```

相关声明：[bt_gatt_discover_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gabd3bcd3c1560956726574faed332fb13)、[func](#a337d7366c12451938f12eec4dc60903e)。

发现属性回调（Discover attribute callback）。

```c
union {
```

<a id="r_a2d944d87d1ee34186f6400419406a474"></a>

```c
uint16_t start_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[start_handle](#a0d2604e7c3ee8969cb5096cbf5793fdb)。

开始发现的起始属性句柄（Starting attribute handle）。

<a id="r_a5f582368e0d43cda157a66f3755837fe"></a>

```c
};
```

<a id="r_ab0f056c90954e1246d897019abd1e7fc"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#ab0f056c90954e1246d897019abd1e7fc)。

发现类型（Discover type）。

<a id="r_a87b130c520ce50f835d0589fd22a844c"></a>

```c
struct bt_gatt_subscribe_params * sub_params
```

相关声明：[bt_gatt_subscribe_params](P068_bt_gatt_subscribe_params_结构体.md)、[sub_params](#a87b130c520ce50f835d0589fd22a844c)。

仅供协议栈内部使用，用于自动发现（Automatic discovery）。

<a id="r_aba7585e3d0eefb323fcde9bcc88e287d"></a>

```c
enum bt_att_chan_opt chan_opt
```

相关声明：[bt_att_chan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac593a27ecf029f33f50f990b2947562c)、[chan_opt](#aba7585e3d0eefb323fcde9bcc88e287d)。

属性协议通道选项（ATT channel options）。

## 58.2\_详细说明（Detailed Documentation）

<a id="a5f582368e0d43cda157a66f3755837fe"></a>

### `[union]`

```c
union { ... } bt_gatt_discover_params
```

<a id="a65ca3c9aad7c02d48fd35c4d6f69dc70"></a>

### `attr_handle`

```c
uint16_t bt_gatt_discover_params::attr_handle
```

包含服务属性的声明句柄（Include service attribute declaration handle）。

<a id="aba7585e3d0eefb323fcde9bcc88e287d"></a>

### `chan_opt`

```c
enum bt_att_chan_opt bt_gatt_discover_params::chan_opt
```

属性协议通道选项（ATT channel options）。

<a id="a225868498c34411cc3fc2be8e678e85e"></a>

### `end_handle`

```c
uint16_t bt_gatt_discover_params::end_handle
```

被包含服务的结束属性句柄（Ending attribute handle）。

停止发现的结束属性句柄（Ending attribute handle）。

**说明（Note）**：注意（Note）：开始发现时，可将此值设为 `BT_ATT_LAST_ATTRIBUTE_HANDLE`，以发现服务中的所有属性。

<a id="a337d7366c12451938f12eec4dc60903e"></a>

### `func`

```c
bt_gatt_discover_func_t bt_gatt_discover_params::func
```

发现属性回调（Discover attribute callback）。

<a id="a0d2604e7c3ee8969cb5096cbf5793fdb"></a>

### `start_handle`

```c
uint16_t bt_gatt_discover_params::start_handle
```

被包含服务的起始属性句柄（Starting attribute handle）。

开始发现的起始属性句柄（Starting attribute handle）。

<a id="a87b130c520ce50f835d0589fd22a844c"></a>

### `sub_params`

```c
struct bt_gatt_subscribe_params* bt_gatt_discover_params::sub_params
```

仅供协议栈内部使用，用于自动发现（Automatic discovery）。

<a id="ab0f056c90954e1246d897019abd1e7fc"></a>

### `type`

```c
uint8_t bt_gatt_discover_params::type
```

发现类型（Discover type）。

<a id="a77d6665c01902e4e23cf8de8a9436262"></a>

### `uuid`

```c
const struct bt_uuid* bt_gatt_discover_params::uuid
```

要发现的通用唯一标识符类型（UUID type）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 58.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [bt_uuid](P131_bt_uuid_结构体.md)
- [bt_gatt_discover_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gabd3bcd3c1560956726574faed332fb13)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_gatt_subscribe_params](P068_bt_gatt_subscribe_params_结构体.md)
- [bt_att_chan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac593a27ecf029f33f50f990b2947562c)
- [bt_gatt_discover_params](P058_bt_gatt_discover_params_结构体.md)
- [BT_ATT_LAST_ATTRIBUTE_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga1b3dc5fedec8d8632d3650405d1ff988)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P057_bt_gatt_cpf_结构体.md) · [返回大纲](大纲.md) · [下一章](P059_bt_gatt_exchange_params_结构体.md)
