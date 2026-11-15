---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-63
title: bt_gatt_read_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__read__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_bt\_gatt\_read\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__read__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GATT 读取（Read）参数。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

GATT 读取（Read）参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 63.1\_数据成员（Data Fields）

<a id="r_a3ea107db0b7537c9dccb2aa6d8f916fb"></a>

```c
bt_gatt_read_func_t func
```

相关声明：[bt_gatt_read_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga1ca94b4f2b6c456b6134e05127993569)、[func](#a3ea107db0b7537c9dccb2aa6d8f916fb)。

属性读取回调（Read attribute callback）。

<a id="r_a0a36063ac0b110fbf57ef6a66f7bece8"></a>

```c
size_t handle_count
```

相关声明：[handle_count](#a0a36063ac0b110fbf57ef6a66f7bece8)。

等于 `1` 时，使用 `single.handle` 和 `single.offset`。

```c
union {
```

```c
struct {
```

<a id="r_ad7f53f7ea43bdb136046dc844688c764"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#af37beb6a69b3a6b90da0594b099bd64d)。

属性句柄（Attribute handle）。

<a id="r_a64d2d4384a9b69ca52b6d50f25cfe591"></a>

```c
uint16_t offset
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[offset](#a27f685a45c405bb2784fe369513724ad)。

属性数据偏移量（Attribute data offset）。

<a id="r_a3b3c10c7af0eec4ffd6db8b5d7280b28"></a>

```c
} single
```

相关声明：[single](#a4cf61907bb95a2be6513d214b7030723)。

```c
struct {
```

<a id="r_aea9ba3adf1f22276d72e21ac7d499134"></a>

```c
uint16_t * handles
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handles](#a2794b8806933d0e16cfc77f4087fdeda)。

通过读取多个特征值（Read Multiple Characteristic Values）操作读取的属性句柄（Attribute handles）。

<a id="r_a50309d38f966c346d927ca7a9405fd1d"></a>

```c
bool variable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[variable](#a77d05cbc54b125fc35d180cf91bf9cb9)。

为 `true` 时，使用读取多个可变长度特征值过程（Read Multiple Variable Length Characteristic Values）。

<a id="r_a0e122bddc8d172b1653bff1dca0c2d3c"></a>

```c
} multiple
```

相关声明：[multiple](#a521f5d1859dd9271fa2c595012dacd25)。

```c
struct {
```

<a id="r_a5fbaf6be995dd61c48300f1726b81bfc"></a>

```c
uint16_t start_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[start_handle](#ac11db1652cd5cee567d666d3697f3a4b)。

请求的起始属性句柄编号（Start attribute handle number）。

<a id="r_ae44c27048ca485b7ca9c15d81e7c9fda"></a>

```c
uint16_t end_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[end_handle](#a8b2a2b912efe557e24276a654087e75c)。

请求的结束属性句柄编号（End attribute handle number）。

<a id="r_ab446ee400cb60a96095b059028b99306"></a>

```c
const struct bt_uuid * uuid
```

相关声明：[bt_uuid](P131_bt_uuid_结构体.md)、[uuid](#ae2ba6ce4043769b86a050fd767248111)。

长度为 2 或 16 个八位组（Octets）的通用唯一标识符（UUID）。

<a id="r_a770f13e3d000de911dc9c2559f9da9f9"></a>

```c
} by_uuid
```

相关声明：[by_uuid](#a86b81f185490e63a07d2a62dd26a7f74)。

<a id="r_ab986ea5924de4d65e7ed138bfd056ab7"></a>

```c
};
```

<a id="r_a1335d1f9aefeff89a57efe78335cb41b"></a>

```c
enum bt_att_chan_opt chan_opt
```

相关声明：[bt_att_chan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac593a27ecf029f33f50f990b2947562c)、[chan_opt](#a1335d1f9aefeff89a57efe78335cb41b)。

属性协议通道选项（ATT channel options）。

## 63.2\_详细说明（Detailed Documentation）

<a id="ab986ea5924de4d65e7ed138bfd056ab7"></a>

### `[union]`

```c
union { ... } bt_gatt_read_params
```

<a id="a86b81f185490e63a07d2a62dd26a7f74"></a>

### `[struct]`

```c
struct { ... } bt_gatt_read_params::by_uuid
```

<a id="a1335d1f9aefeff89a57efe78335cb41b"></a>

### `chan_opt`

```c
enum bt_att_chan_opt bt_gatt_read_params::chan_opt
```

属性协议通道选项（ATT channel options）。

<a id="a8b2a2b912efe557e24276a654087e75c"></a>

### `end_handle`

```c
uint16_t bt_gatt_read_params::end_handle
```

请求的结束属性句柄编号（End attribute handle number）。

结束句柄（End handle）设定本次读取范围的终点。例如，可设为 `BT_ATT_LAST_ATTRIBUTE_HANDLE`，使范围终点位于 GATT 数据库末尾；也可设为发现所得的服务结束句柄，此时可从 `bt_gatt_service_val` 获取 `end_handle`。

<a id="a3ea107db0b7537c9dccb2aa6d8f916fb"></a>

### `func`

```c
bt_gatt_read_func_t bt_gatt_read_params::func
```

属性读取回调（Read attribute callback）。

<a id="af37beb6a69b3a6b90da0594b099bd64d"></a>

### `handle`

```c
uint16_t bt_gatt_read_params::handle
```

属性句柄（Attribute handle）。

<a id="a0a36063ac0b110fbf57ef6a66f7bece8"></a>

### `handle_count`

```c
size_t bt_gatt_read_params::handle_count
```

等于 `1` 时，使用 `single.handle` 和 `single.offset`。

大于 `1` 时使用 `multiple.handles`。等于 `0` 时使用 `by_uuid`，执行按特征 UUID 读取（Read Using Characteristic UUID）。

<a id="a2794b8806933d0e16cfc77f4087fdeda"></a>

### `handles`

```c
uint16_t* bt_gatt_read_params::handles
```

通过读取多个特征值（Read Multiple Characteristic Values）操作读取的属性句柄（Attribute handles）。

<a id="a521f5d1859dd9271fa2c595012dacd25"></a>

### `[struct]`

```c
struct { ... } bt_gatt_read_params::multiple
```

<a id="a27f685a45c405bb2784fe369513724ad"></a>

### `offset`

```c
uint16_t bt_gatt_read_params::offset
```

属性数据偏移量（Attribute data offset）。

<a id="a4cf61907bb95a2be6513d214b7030723"></a>

### `[struct]`

```c
struct { ... } bt_gatt_read_params::single
```

<a id="ac11db1652cd5cee567d666d3697f3a4b"></a>

### `start_handle`

```c
uint16_t bt_gatt_read_params::start_handle
```

请求的起始属性句柄编号（Start attribute handle number）。

起始句柄（Starting handle）设定本次读取范围的起点。例如，可设为 `BT_ATT_FIRST_ATTRIBUTE_HANDLE`，使范围起点位于 GATT 数据库开头；也可设为发现所得的服务起始句柄。

协议栈每处理完服务器返回的一个匹配句柄—值对（Handle-value pair）后，都会自动递增此值。

<a id="ae2ba6ce4043769b86a050fd767248111"></a>

### `uuid`

```c
const struct bt_uuid* bt_gatt_read_params::uuid
```

长度为 2 或 16 个八位组（Octets）的通用唯一标识符（UUID）。

<a id="a77d05cbc54b125fc35d180cf91bf9cb9"></a>

### `variable`

```c
bool bt_gatt_read_params::variable
```

为 `true` 时，使用读取多个可变长度特征值过程（Read Multiple Variable Length Characteristic Values）。

该组属性的值可以为可变长度或未知长度。若为 `false`，使用读取多个特征值过程（Read Multiple Characteristic Values）；此时该组属性的值必须为已知固定长度，只有最后一个值可以为可变长度。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 63.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [bt_gatt_read_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#ga1ca94b4f2b6c456b6134e05127993569)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_uuid](P131_bt_uuid_结构体.md)
- [bt_att_chan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac593a27ecf029f33f50f990b2947562c)
- [bt_gatt_read_params](P063_bt_gatt_read_params_结构体.md)
- [BT_ATT_LAST_ATTRIBUTE_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga1b3dc5fedec8d8632d3650405d1ff988)
- [bt_gatt_service_val](P067_bt_gatt_service_val_结构体.md)
- [BT_ATT_FIRST_ATTRIBUTE_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gad0aa088f621b8965013c3ced27480df7)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P062_bt_gatt_notify_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P064_bt_gatt_scc_结构体.md)
