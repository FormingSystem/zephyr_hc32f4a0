---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-49
title: bt_gatt_attr_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__attr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_bt\_gatt\_attr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__gatt__attr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用属性配置文件（GATT）属性（Attribute）。

```c
#include <zephyr/bluetooth/gatt.h>
```

<a id="details"></a>

通用属性规范属性（GATT Attribute）。此类型主要表示属性协议属性（ATT Attribute），可作为本地 ATT 数据库中的一项。此类型的对象必须属于构成 GATT 服务（GATT service）的数组。在所构成的服务已向本地 GATT 服务器注册期间，通常可以将此类型的指针传给 GATT 服务器 API，例如 `bt_gatt_notify()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 49.1\_数据成员（Data Fields）

<a id="r_a6958f507f9ff172018be458ebc86106f"></a>

```c
const struct bt_uuid * uuid
```

相关声明：[bt_uuid](P131_bt_uuid_结构体.md)、[uuid](#a6958f507f9ff172018be458ebc86106f)。

属性类型（Attribute Type）。

<a id="r_a074abc719494ca35997a452f526e7ecc"></a>

```c
bt_gatt_attr_read_func_t read
```

相关声明：[bt_gatt_attr_read_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga57e36bf94652531964fd4237c203fe7b)、[read](#a074abc719494ca35997a452f526e7ecc)。

属性值读取方法（Attribute Value read method）。

<a id="r_a1ecd78536067f4bded506e0daccefd35"></a>

```c
bt_gatt_attr_write_func_t write
```

相关声明：[bt_gatt_attr_write_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga3fd8527a0f3e8f3699dc0d3b0339eba1)、[write](#a1ecd78536067f4bded506e0daccefd35)。

属性值写入方法（Attribute Value write method）。

<a id="r_adeb063fb101fab45dd789c7212c43357"></a>

```c
void * user_data
```

相关声明：[user_data](#adeb063fb101fab45dd789c7212c43357)。

供 `read()` 和 `write()` 实现使用的私有数据（Private data）。

<a id="r_aeee42a3d3ca15e40cf11cc0c3fde106b"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#aeee42a3d3ca15e40cf11cc0c3fde106b)。

属性句柄（Attribute Handle）。

<a id="r_a0849a40254622080d05e8559c4fdb9e2"></a>

```c
uint16_t perm: 15
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[perm](#a0849a40254622080d05e8559c4fdb9e2)。

属性权限（Attribute Permissions）。

## 49.2\_详细说明（Detailed Documentation）

<a id="aeee42a3d3ca15e40cf11cc0c3fde106b"></a>

### `handle`

```c
uint16_t bt_gatt_attr::handle
```

属性句柄（Attribute Handle）。

属性句柄（Attribute Handle）是对应 ATT 数据库中某个特定属性（Attribute）的索引。

**说明（Note）**：注意（Note）：对于本地 ATT 数据库中的属性，使用 `bt_gatt_attr_get_handle()`。

<a id="a0849a40254622080d05e8559c4fdb9e2"></a>

### `perm`

```c
uint16_t bt_gatt_attr::perm
```

属性权限（Attribute Permissions）。

由 `bt_gatt_perm` 构成的位域（Bit field）。

这些权限（Permissions）规定调用 `read()` 或 `write()` 之前必须满足的安全要求（Security requirements）。

<a id="a074abc719494ca35997a452f526e7ecc"></a>

### `read`

```c
bt_gatt_attr_read_func_t bt_gatt_attr::read
```

属性值读取方法（Attribute Value read method）。

可读属性（Readable Attributes）必须实现此方法。

属性不可读（Not readable）时必须为 `NULL`。

此方法的行为由属性类型（Attribute Type）决定。

参见 `bt_gatt_attr_read_func_t`。

<a id="adeb063fb101fab45dd789c7212c43357"></a>

### `user_data`

```c
void* bt_gatt_attr::user_data
```

供 `read()` 和 `write()` 实现使用的私有数据（Private data）。

此字段的含义因情况而异，此处不作规定。

**说明（Note）**：注意（Note）：属性（Attributes）可以具有相同的属性类型（Attribute Type），但采用不同实现，且用户数据（User data）彼此不兼容。不得仅依据属性类型推断用户数据的类型。

**参阅（See Also）**：有关此字段，另见（See also）`bt_gatt_discover_func_t`。

<a id="a6958f507f9ff172018be458ebc86106f"></a>

### `uuid`

```c
const struct bt_uuid* bt_gatt_attr::uuid
```

属性类型（Attribute Type）。

属性类型（Attribute Type）是一个通用唯一标识符（UUID），它决定 `read()`、`write()` 方法应提供的接口及可能的权限配置。

例如，类型为 `BT_UUID_GATT_CPF` 的属性将充当 GATT 特征表示格式描述符（Characteristic Presentation Format descriptor），其行为由核心规范（Core Specification）3.G.3.3.3.5 规定。

可通过生成新的通用唯一标识符（UUID），为应用专用场景定义新的属性类型（Attribute Type）。

<a id="a1ecd78536067f4bded506e0daccefd35"></a>

### `write`

```c
bt_gatt_attr_write_func_t bt_gatt_attr::write
```

属性值写入方法（Attribute Value write method）。

可写属性（Writeable Attributes）必须实现此方法。

属性不可写（Not writable）时必须为 `NULL`。

此方法的行为由属性类型（Attribute Type）决定。

参见 `bt_gatt_attr_write_func_t`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/gatt.h`

## 49.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h_source.html)
- [bt_uuid](P131_bt_uuid_结构体.md)
- [bt_gatt_attr_read_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga57e36bf94652531964fd4237c203fe7b)
- [bt_gatt_attr_write_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga3fd8527a0f3e8f3699dc0d3b0339eba1)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_gatt_notify()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga74ee552864c563aa5bc939f37395c14a)
- [bt_gatt_attr_get_handle()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__server.html#ga2d51136ea1bd6cdb50900639506fd9f7)
- [bt_gatt_perm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html#ga96e57500d2340a45badb23701cc43833)
- [bt_gatt_discover_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt__client.html#gabd3bcd3c1560956726574faed332fb13)
- [BT_UUID_GATT_CPF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga331a61702ffe9b15bac0de3d60414022)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P048_bt_df_per_adv_sync_iq_samples_report_结构体.md) · [返回大纲](大纲.md) · [下一章](P050_bt_gatt_authorization_cb_结构体.md)
