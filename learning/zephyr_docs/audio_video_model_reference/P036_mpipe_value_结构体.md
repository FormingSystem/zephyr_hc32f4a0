---
id: learning.zephyr-docs.audio-video-model-reference.page-36
title: mpipe_value_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__value.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_mpipe\_value\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__value.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

值结构（Value Structure）。

```c
#include <zephyr/mpipe/mpipe_value.h>
```

<a id="details"></a>

值（Value）结构体。采用一个固定大小的带标签联合体（tagged union），使每个值占用相同空间，并能按值存储在拥有它的结构体内部。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 36.1\_数据成员（Data Fields）

<a id="r_a46023f18c7182424227b2499fe59673f"></a>

```c
enum mpipe_value_type type
```

相关声明：[mpipe_value_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga8b8b4952140ae9ef7e6e6f20aa99d8a2)、[type](#a46023f18c7182424227b2499fe59673f)。

值的类型，参见 `mpipe_value_type`。

```c
union {
```

<a id="r_ab87354111cec7745bfa92658442b02cd"></a>

```c
bool v_boolean
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[v_boolean](#a1988df0611b4ec27d349a7b3c000fa11)。

布尔类型：`MPIPE_TYPE_BOOLEAN`。

<a id="r_ac83b154d9faab94ddf99d301969145f1"></a>

```c
int32_t v_int
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[v_int](#af070b57c281efe0ca839848063ea6522)。

有符号整数类型：`MPIPE_TYPE_INT`。

<a id="r_a41bf0be5999a2da4fce47a22eb1b7736"></a>

```c
uint32_t v_uint
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[v_uint](#a4b04c1933350af6ce38f32c0300fff0d)。

无符号整数类型：`MPIPE_TYPE_UINT`。

```c
struct {
```

<a id="r_a7a6333f7f04d808339156674d328cc84"></a>

```c
union mpipe_value_bound min
```

相关声明：[mpipe_value_bound](P069_mpipe_value_bound_联合体.md)、[min](#a6e8be639c2273a55e3ae42f2eac0cc66)。

范围下界（Lower bound）。

<a id="r_a2853565a90c4b4ffb5c35862bf0b210f"></a>

```c
union mpipe_value_bound max
```

相关声明：[mpipe_value_bound](P069_mpipe_value_bound_联合体.md)、[max](#ac5a154705771d149e834aa881441e373)。

范围上界（Upper bound）。

<a id="r_a318773a003c17ff6e34aa5b0d161539f"></a>

```c
union mpipe_value_bound step
```

相关声明：[mpipe_value_bound](P069_mpipe_value_bound_联合体.md)、[step](#a5e52fd9659e057fe6bbcba626fe4b581)。

范围内两个相邻值之间的步长（step）。

<a id="r_a912ad817ac23b367e7b0185f9f4d29a6"></a>

```c
} range
```

相关声明：[range](#a7f43a41b3c31051462180182998e8b05)。

整数范围类型：`MPIPE_TYPE_INT_RANGE`、`MPIPE_TYPE_UINT_RANGE`。

<a id="r_ae0ed6ff46b8319d0ef4eba01878dd74f"></a>

```c
};
```

值的内容，通过其类型所选择的联合体成员读取。

## 36.2\_详细说明（Detailed Documentation）

<a id="ae0ed6ff46b8319d0ef4eba01878dd74f"></a>

### `[union]`

```c
union { ... } mpipe_value
```

值的内容，通过其类型所选择的联合体成员读取。

<a id="ac5a154705771d149e834aa881441e373"></a>

### `max`

```c
union mpipe_value_bound mpipe_value::max
```

范围上界（Upper bound）。

<a id="a6e8be639c2273a55e3ae42f2eac0cc66"></a>

### `min`

```c
union mpipe_value_bound mpipe_value::min
```

范围下界（Lower bound）。

<a id="a7f43a41b3c31051462180182998e8b05"></a>

### `[struct]`

```c
struct { ... } mpipe_value::range
```

整数范围类型：`MPIPE_TYPE_INT_RANGE`、`MPIPE_TYPE_UINT_RANGE`。

<a id="a5e52fd9659e057fe6bbcba626fe4b581"></a>

### `step`

```c
union mpipe_value_bound mpipe_value::step
```

范围内两个相邻值之间的步长（step）。

<a id="a46023f18c7182424227b2499fe59673f"></a>

### `type`

```c
enum mpipe_value_type mpipe_value::type
```

值的类型，参见 `mpipe_value_type`。

<a id="a1988df0611b4ec27d349a7b3c000fa11"></a>

### `v_boolean`

```c
bool mpipe_value::v_boolean
```

布尔类型：`MPIPE_TYPE_BOOLEAN`。

<a id="af070b57c281efe0ca839848063ea6522"></a>

### `v_int`

```c
int32_t mpipe_value::v_int
```

有符号整数类型：`MPIPE_TYPE_INT`。

<a id="a4b04c1933350af6ce38f32c0300fff0d"></a>

### `v_uint`

```c
uint32_t mpipe_value::v_uint
```

无符号整数类型：`MPIPE_TYPE_UINT`。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_value.h`

## 36.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_value.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__value_8h_source.html)
- [mpipe_value_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__value.html#ga8b8b4952140ae9ef7e6e6f20aa99d8a2)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mpipe_value_bound](P069_mpipe_value_bound_联合体.md)
- [mpipe_value](P036_mpipe_value_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P035_mpipe_transform_client_结构体.md) · [返回大纲](大纲.md) · [下一章](P037_mpl_cmd_结构体.md)
