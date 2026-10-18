---
id: learning.zephyr-docs.api-file-display-management-reference.page-5
title: zephyr__bluetooth__data.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_bluetooth\_\_data.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/data_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙数据类型与辅助接口（Bluetooth Data Types and Helpers）。

<a id="details"></a>

```c
#include <stddef.h>
#include <stdint.h>
```

查看此文件的源码。

蓝牙数据类型与辅助接口（Bluetooth Data Types and Helpers）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_bt_5Fdata"></a>

```c
struct bt_data
```

相关声明：[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)。

蓝牙数据（Bluetooth Data）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_a7357d34bf295a16d8288df3bf75e7976"></a>

```c
#define BT_DATA_SERIALIZED_SIZE(data_len)
```

相关声明：[BT_DATA_SERIALIZED_SIZE](#a7357d34bf295a16d8288df3bf75e7976)。

根据数据长度，获取序列化后的 `bt_data` 大小（Serialized Size）。

<a id="r_a8481217e632522e1f322de87d745f8f0"></a>

```c
#define BT_DATA(_type, _data, _data_len)
```

相关声明：[BT_DATA](#a8481217e632522e1f322de87d745f8f0)。

用于声明 `bt_data` 数组元素的辅助宏。

<a id="r_a4c51f9b7a3a4e84abb4df3f1f714c6e2"></a>

```c
#define BT_DATA_BYTES(_type, _bytes...)
```

相关声明：[BT_DATA_BYTES](#a4c51f9b7a3a4e84abb4df3f1f714c6e2)。

用于声明 `bt_data` 数组元素的辅助宏。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.3\_函数（Functions）

<a id="r_a3d2c6adc42eb9510734630f38d921b9a"></a>

```c
size_t bt_data_get_len (const struct bt_data data[], size_t data_count)
```

相关声明：[bt_data_get_len](#a3d2c6adc42eb9510734630f38d921b9a)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)。

获取一组 `bt_data` 结构体的总大小，单位为字节（Octets）。

<a id="r_a3c067b16468ebd17973faeded0fc83c9"></a>

```c
size_t bt_data_serialize (const struct bt_data *input, uint8_t *output)
```

相关声明：[bt_data_serialize](#a3c067b16468ebd17973faeded0fc83c9)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将 `bt_data` 结构体序列化（Serialize）为广播结构（Advertising Structure），即平坦数组。

## 5.4\_详细说明（Detailed Documentation）

<a id="a8481217e632522e1f322de87d745f8f0"></a>

### `BT_DATA`

```c
#define BT_DATA ( _type, _data, _data_len )
```

展开值（Value）：

```c
{ \
        .type = (_type), \
        .data_len = (_data_len), \
        .data = (const uint8_t *)(_data), \
}
```

用于声明 `bt_data` 数组元素的辅助宏。

此宏主要用于创建由 `struct bt_data` 元素组成的数组，随后可将其传入 `bt_le_adv_start` 等函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_type` | 广播数据字段类型（Advertising Data Field Type）。 |
| `_data` | 指向数据字段有效载荷（Payload）的指针。 |
| `_data_len` | `_data` 指针之后的数据字节数（Octets）。 |

<a id="a4c51f9b7a3a4e84abb4df3f1f714c6e2"></a>

### `BT_DATA_BYTES`

```c
#define BT_DATA_BYTES ( _type, _bytes... )
```

展开值（Value）：

```c
BT_DATA(_type, ((uint8_t []) { _bytes }), \
        sizeof((uint8_t []) { _bytes }))
```

用于声明 `bt_data` 数组元素的辅助宏。

此宏主要用于创建由 `struct bt_data` 元素组成的数组，随后可将其传入 `bt_le_adv_start` 等函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_type` | 广播数据字段类型（Advertising Data Field Type）。 |
| `_bytes` | 数量可变的单字节参数（Single-byte Parameters）。 |

<a id="a7357d34bf295a16d8288df3bf75e7976"></a>

### `BT_DATA_SERIALIZED_SIZE`

```c
#define BT_DATA_SERIALIZED_SIZE ( data_len)
```

展开值（Value）：

```c
((data_len) + 2)
```

根据数据长度，获取序列化后的 `bt_data` 大小（Serialized Size）。

广播结构（AD Structure）的 `Length` 字段大小为 1；`Data` 中的 `AD Type` 字段大小为 1；`Data` 中的 `AD Data` 字段大小为 `data_len`。

参见蓝牙核心规范（Core Specification）5.4 版，第 3 卷 C 部分第 11 节图 11.1。

<a id="a3d2c6adc42eb9510734630f38d921b9a"></a>

### `bt_data_get_len()`

```c
size_t bt_data_get_len ( const struct bt_data data[], size_t data_count )
```

获取一组 `bt_data` 结构体的总大小，单位为字节（Octets）。

总大小包含每个元素的长度字段（Length，1 字节）、类型字段（Type，1 字节），以及各自的数据长度。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] data` | `bt_data` 结构体数组（Array）。 |
| `[in] data_count` | `data` 中 `bt_data` 结构体的数量。 |

**返回（Returns）**：返回值：由这组 `bt_data` 结构体构造的拼接数据大小（Concatenated Data Size）。

<a id="a3c067b16468ebd17973faeded0fc83c9"></a>

### `bt_data_serialize()`

```c
size_t bt_data_serialize ( const struct bt_data * input, uint8_t * output )
```

将 `bt_data` 结构体序列化（Serialize）为广播结构（Advertising Structure），即平坦数组。

数据按照蓝牙核心规范（Bluetooth Core Specification）5.4 版、第 3 卷 C 部分第 11 节的格式组织。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] input` | 用于读取的单个 `bt_data` 结构体。 |
| `[out] output` | 足以保存 `input` 所含广播结构（Advertising Structure）的缓冲区。其大小至少为 `input->data_len + 2`，额外两字节用于类型和长度。 |

**返回（Returns）**：返回值：写入 `output` 的字节数（Octets）。


## 5.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P121_data.h_源码浏览.md)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_le_adv_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad2e3caef88d52d720e8e4d21df767b02)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="adata_8h_html_a8481217e632522e1f322de87d745f8f0"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_zephyr__net__coap_client_tcp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__drivers__firmware__scmi__util.h_文件参考.md)
