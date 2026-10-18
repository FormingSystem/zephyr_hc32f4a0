---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-146
title: bt_ots_obj_type_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__ots__obj__type.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第146章\_bt\_ots\_obj\_type\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__ots__obj__type.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对象传输服务（OTS）对象的类型。

```c
#include <zephyr/bluetooth/services/ots.h>
```

<a id="details"></a>

对象传输服务（OTS）对象的类型。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 146.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_ae511df9949499b325a08aa0f37efdfe7"></a>

```c
struct bt_uuid uuid
```

相关声明：[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[uuid](#a89a8dbe566579422df503dd577ea8d42)。

<a id="r_ac9a1aba22699b679300e68b64217747b"></a>

```c
struct bt_uuid_16 uuid_16
```

相关声明：[bt_uuid_16](../bluetooth_connection_model_reference/P133_bt_uuid_16_结构体.md)、[uuid_16](#ae39b7a368314d1a771cf3573d2077095)。

<a id="r_a7347fdc713cdf25670173f62c5501a8b"></a>

```c
struct bt_uuid_128 uuid_128
```

相关声明：[bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)、[uuid_128](#aedf0e5d45f6f4912a8eeae077eda17be)。

<a id="r_a64cec1015024fa9cb7ff605d955e4bd1"></a>

```c
};
```

## 146.2\_详细说明（Detailed Documentation）

<a id="a64cec1015024fa9cb7ff605d955e4bd1"></a>

### `[union]`

```c
union { ... } bt_ots_obj_type
```

<a id="a89a8dbe566579422df503dd577ea8d42"></a>

### `uuid`

```c
struct bt_uuid bt_ots_obj_type::uuid
```

<a id="aedf0e5d45f6f4912a8eeae077eda17be"></a>

### `uuid_128`

```c
struct bt_uuid_128 bt_ots_obj_type::uuid_128
```

<a id="ae39b7a368314d1a771cf3573d2077095"></a>

### `uuid_16`

```c
struct bt_uuid_16 bt_ots_obj_type::uuid_16
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/ots.h`

## 146.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/ots.h](https://docs.zephyrproject.org/latest/doxygen/html/ots_8h_source.html)
- [bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)
- [bt_uuid_16](../bluetooth_connection_model_reference/P133_bt_uuid_16_结构体.md)
- [bt_uuid_128](../bluetooth_connection_model_reference/P132_bt_uuid_128_结构体.md)
- [bt_ots_obj_type](P146_bt_ots_obj_type_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P145_bt_ots_obj_size_结构体.md) · [返回大纲](大纲.md) · [下一章](P147_bt_pacs_cap_结构体.md)
