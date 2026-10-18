---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-187
title: bt_vocs_register_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__vocs__register__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第187章\_bt\_vocs\_register\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__vocs__register__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于注册音量偏移控制服务（Volume Offset Control Service）实例的结构。

```c
#include <zephyr/bluetooth/audio/vocs.h>
```

<a id="details"></a>

用于注册音量偏移控制服务（Volume Offset Control Service）实例的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 187.1\_数据成员（Data Fields）

<a id="r_a0572c60319c8984e2437e596584c46f5"></a>

```c
uint32_t location
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[location](#a0572c60319c8984e2437e596584c46f5)。

音频位置（Audio Location）位掩码。

<a id="r_a6919f965abfa1fec39a3c8e0f29c04f3"></a>

```c
bool location_writable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[location_writable](#a6919f965abfa1fec39a3c8e0f29c04f3)。

布尔值，用于设置客户端是否可以写入位置。

<a id="r_ac1c2475cd390f5acf840f92ea45c6d31"></a>

```c
int16_t offset
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[offset](#ac1c2475cd390f5acf840f92ea45c6d31)。

初始音量偏移（volume offset），范围为 -255 至 255。

<a id="r_a1f6baed09dc35b974d06f1426b671e05"></a>

```c
char * output_desc
```

相关声明：[output_desc](#a1f6baed09dc35b974d06f1426b671e05)。

初始音频输出描述（audio output description）。

<a id="r_aace5987e890c8b4dbf3e01fa5c2a4432"></a>

```c
bool desc_writable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[desc_writable](#aace5987e890c8b4dbf3e01fa5c2a4432)。

布尔值，用于设置客户端是否可以写入描述。

<a id="r_a306ad3c712bb5a5109f3afb4912d590b"></a>

```c
struct bt_vocs_cb * cb
```

相关声明：[bt_vocs_cb](P185_bt_vocs_cb_结构体.md)、[cb](#a306ad3c712bb5a5109f3afb4912d590b)。

指向回调结构体（Callback Structure）的指针。

## 187.2\_详细说明（Detailed Documentation）

<a id="a306ad3c712bb5a5109f3afb4912d590b"></a>

### `cb`

```c
struct bt_vocs_cb* bt_vocs_register_param::cb
```

指向回调结构体（Callback Structure）的指针。

<a id="aace5987e890c8b4dbf3e01fa5c2a4432"></a>

### `desc_writable`

```c
bool bt_vocs_register_param::desc_writable
```

布尔值，用于设置客户端是否可以写入描述。

<a id="a0572c60319c8984e2437e596584c46f5"></a>

### `location`

```c
uint32_t bt_vocs_register_param::location
```

音频位置（Audio Location）位掩码。

<a id="a6919f965abfa1fec39a3c8e0f29c04f3"></a>

### `location_writable`

```c
bool bt_vocs_register_param::location_writable
```

布尔值，用于设置客户端是否可以写入位置。

<a id="ac1c2475cd390f5acf840f92ea45c6d31"></a>

### `offset`

```c
int16_t bt_vocs_register_param::offset
```

初始音量偏移（volume offset），范围为 -255 至 255。

<a id="a1f6baed09dc35b974d06f1426b671e05"></a>

### `output_desc`

```c
char* bt_vocs_register_param::output_desc
```

初始音频输出描述（audio output description）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/vocs.h`

## 187.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/vocs.h](https://docs.zephyrproject.org/latest/doxygen/html/vocs_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [bt_vocs_cb](P185_bt_vocs_cb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P186_bt_vocs_discover_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P188_bt_cap_set_member_联合体.md)
