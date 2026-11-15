---
id: learning.zephyr-docs.serialization.page-6
title: JSON接口参考
kind: reference
status: maintained
domains: [zephyr, serialization, development]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__json.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_JSON接口参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__json.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 6.1\_概述

JSON（JavaScript Object Notation，JavaScript对象表示法）应用程序编程接口（Application Programming Interface，API）。原文标注：自 1.10 版本起提供（Since），接口版本（Version）为 1.0.0。

```c
#include <zephyr/data/json.h>
```

## 6.2\_关联声明与说明

<a id="r_json_5Ftoken"></a>

```c
struct json_token
```

[详细说明](P015_JSON词元.md)。

<a id="r_json_5Flexer"></a>

```c
struct json_lexer
```

[详细说明](P011_JSON词法分析器.md)。

<a id="r_json_5Fobj"></a>

```c
struct json_obj
```

[详细说明](P012_JSON解析对象.md)。

<a id="r_json_5Fobj_5Fkey_5Fvalue"></a>

```c
struct json_obj_key_value
```

JSON 对象中的单个顶层“`key`: `value`”成员。

[详细说明](P013_JSON键值对.md)。

<a id="r_json_5Fobj_5Ftoken"></a>

```c
struct json_obj_token
```

[详细说明](P014_JSON对象词元.md)。

<a id="r_json_5Fobj_5Fdescr"></a>

```c
struct json_obj_descr
```

[详细说明](P009_JSON对象描述符.md)。

<a id="r_json_5Fmixed_5Farr_5Fdescr"></a>

```c
struct json_mixed_arr_descr
```

混合类型 JSON 数组的描述符（Mixed-`type` JSON Array Descriptor）。

[详细说明](P010_JSON混合数组描述符.md)。

## 6.3\_JSON\_MIXED\_ARR\_DESCR\_ARRAY

<a id="ga38f87b83b1c5ef7da5b18a3066938b58"></a>
<a id="r_ga38f87b83b1c5ef7da5b18a3066938b58"></a>

```c
#define JSON_MIXED_ARR_DESCR_ARRAY( struct_, field_name_, max_len_, elem_descr_, count_field_ )
```

```c
#include <zephyr/data/json.h>
```

用于声明混合数组中同类型数组元素描述符（Homogeneous Array Element Descriptor）的辅助宏。

原文示例（Example）：

```c
struct foo { int arr[4]; size_t arr_count; }; const struct json_obj_descr arr_elem_descr[] = { JSON_OBJ_DESCR_ARRAY(struct foo, arr, 4, arr_count, JSON_TOK_NUMBER), }; const struct json_mixed_arr_descr foo_descr[] = { JSON_MIXED_ARR_DESCR_ARRAY(struct foo, arr, 4, arr_elem_descr, arr_count), };
```

宏展开（Value）：

```c
{ \
        .type = JSON_TOK_ARRAY_START, \
        .count_offset = offsetof(struct_, count_field_), \
        .array = { \
                .element_descr = elem_descr_, \
                .n_elements = (max_len_), \
                .offset = offsetof(struct_, field_name_) \
        } \
}
```


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `struct_` | 包含数组的结构体。 |
| `field_name_` | 结构体中的字段名。 |
| `max_len_` | 数组的最大元素数量。 |
| `elem_descr_` | 元素描述符，指向 [`json_obj_descr`](P009_JSON对象描述符.md) 数组。 |
| `count_field_` | 结构体中保存元素数量的字段名。 |

## 6.4\_JSON\_MIXED\_ARR\_DESCR\_MIXED\_ARRAY

<a id="ga2b9d36bc7ff682f8d7236183818ff005"></a>
<a id="r_ga2b9d36bc7ff682f8d7236183818ff005"></a>

```c
#define JSON_MIXED_ARR_DESCR_MIXED_ARRAY( struct_, field_name_, sub_descr_, count_field_ )
```

```c
#include <zephyr/data/json.h>
```

用于声明嵌套混合数组元素描述符（Nested Mixed Array Element Descriptor）的辅助宏。

原文示例（Example）：

```c
struct foo { ...; size_t nested_count; }; const struct json_mixed_arr_descr nested_descr[] = { ... }; const struct json_mixed_arr_descr foo_descr[] = { JSON_MIXED_ARR_DESCR_MIXED_ARRAY(struct foo, nested, nested_descr, nested_count), };
```

宏展开（Value）：

```c
{ \
        .type = JSON_TOK_MIXED_ARRAY, \
        .count_offset = offsetof(struct_, count_field_), \
        .mixed_array = { \
                .sub_descr = sub_descr_, \
                .sub_descr_len = ARRAY_SIZE(sub_descr_), \
                .offset = offsetof(struct_, field_name_) \
        } \
}
```


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `struct_` | 包含嵌套混合数组的结构体。 |
| `field_name_` | 结构体中的字段名。 |
| `sub_descr_` | 描述嵌套数组的混合数组描述符。 |
| `count_field_` | 结构体中保存元素数量的字段名。 |

> 译注：原示例中的省略号表示需要补齐的结构体字段或描述符内容，不是可直接编译的 C 语法。

## 6.5\_JSON\_MIXED\_ARR\_DESCR\_OBJECT

<a id="ga705b4980a865683c3b4df4dc0f4d6e28"></a>
<a id="r_ga705b4980a865683c3b4df4dc0f4d6e28"></a>

```c
#define JSON_MIXED_ARR_DESCR_OBJECT( struct_, field_name_, sub_descr_, count_field_ )
```

```c
#include <zephyr/data/json.h>
```

用于声明混合数组中对象元素描述符（Object Element Descriptor）的辅助宏。

原文示例（Example）：

```c
struct bar { int y; }; struct foo { struct bar b; size_t b_count; }; const struct json_obj_descr bar_descr[] = { ... }; const struct json_mixed_arr_descr foo_descr[] = { JSON_MIXED_ARR_DESCR_OBJECT(struct foo, b, bar_descr, b_count), };
```

宏展开（Value）：

```c
{ \
        .type = JSON_TOK_OBJECT_START, \
        .count_offset = offsetof(struct_, count_field_), \
        .object = { \
                .sub_descr = sub_descr_, \
                .sub_descr_len = ARRAY_SIZE(sub_descr_), \
                .offset = offsetof(struct_, field_name_) \
        } \
}
```


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `struct_` | 包含对象的结构体。 |
| `field_name_` | 结构体中的字段名。 |
| `sub_descr_` | 描述对象字段的 [`json_obj_descr`](P009_JSON对象描述符.md) 数组。 |
| `count_field_` | 结构体中保存元素数量的字段名。 |

> 译注：原示例中的省略号是对象描述符的占位内容，需要在实际程序中补齐。

## 6.6\_JSON\_MIXED\_ARR\_DESCR\_PRIM

<a id="ga6eecf3f2cda73f7fe4fac37859ce3f77"></a>
<a id="r_ga6eecf3f2cda73f7fe4fac37859ce3f77"></a>

```c
#define JSON_MIXED_ARR_DESCR_PRIM( struct_, field_name_, type_, count_field_ )
```

```c
#include <zephyr/data/json.h>
```

用于声明混合数组中基本类型元素描述符（Primitive Element Descriptor）的辅助宏。

原文示例（Example）：

```c
struct foo { int x; size_t x_count; }; const struct json_mixed_arr_descr foo_descr[] = { JSON_MIXED_ARR_DESCR_PRIM(struct foo, x, JSON_TOK_NUMBER, x_count), };
```

宏展开（Value）：

```c
{ \
        .type = type_, \
        .count_offset = offsetof(struct_, count_field_), \
        .primitive = { \
            .offset = offsetof(struct_, field_name_), \
            .size = SIZEOF_FIELD(struct_, field_name_) \
        } \
}
```


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `struct_` | 包含该值的结构体。 |
| `field_name_` | 结构体中的字段名。 |
| `type_` | JSON 值的词元类型（Token Type），见 enum [`json_tokens`](#ga18a137ac5e2998d375540298670797c4)。 |
| `count_field_` | 结构体中保存元素数量的字段名。 |

## 6.7\_JSON\_OBJ\_DESCR\_ARRAY

<a id="ga0b510decbc755c82903b54fcbc4a3b64"></a>
<a id="r_ga0b510decbc755c82903b54fcbc4a3b64"></a>

```c
#define JSON_OBJ_DESCR_ARRAY( struct_, field_name_, max_len_, len_field_, elem_type_ )
```

```c
#include <zephyr/data/json.h>
```

用于为基本类型数组声明描述符的辅助宏。

用法示例如下：

宏展开（Value）：

```c
{ \
        .field_name = (#field_name_), \
        .align_shift = Z_ALIGN_SHIFT(struct_), \
        .field_name_len = sizeof(#field_name_) - 1, \
        .type = JSON_TOK_ARRAY_START, \
        .offset = offsetof(struct_, field_name_), \
        .array = { \
                .element_descr = Z_JSON_ELEMENT_DESCR(struct_, len_field_, \
                        elem_type_, \
                        Z_JSON_DESCR_FIELD(struct_, field_name_[0])), \
                .n_elements = (max_len_), \
        }, \
}
```

原文示例（Example）：

```c
 struct example {
     int32_t foo[10];
     size_t foo_len;
 };

 struct json_obj_descr array[] = {
      JSON_OBJ_DESCR_ARRAY(struct example, foo, 10, foo_len,
                           JSON_TOK_NUMBER)
 };
```


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `struct_` | 保存各值的结构体。 |
| `field_name_` | 结构体中的字段名。 |
| `max_len_` | 数组的最大元素数量。 |
| `len_field_` | 结构体中保存数组元素数量的字段名。 |
| `elem_type_` | 元素类型，必须是基本类型（Primitive Type）。 |

## 6.8\_JSON\_OBJ\_DESCR\_ARRAY\_ARRAY

<a id="gaed8189235fd30d2bc041cafee9591ec9"></a>
<a id="r_gaed8189235fd30d2bc041cafee9591ec9"></a>

```c
#define JSON_OBJ_DESCR_ARRAY_ARRAY( struct_, field_name_, max_len_, len_field_, elem_descr_, elem_descr_len_ )
```

```c
#include <zephyr/data/json.h>
```

用于为数组组成的数组（Array of Arrays）声明描述符的辅助宏。

用法示例如下：

宏展开（Value）：

```c
{ \
        .field_name = (#field_name_), \
        .align_shift = Z_ALIGN_SHIFT(struct_), \
        .field_name_len = sizeof(#field_name_) - 1, \
        .type = JSON_TOK_ARRAY_START, \
        .offset = offsetof(struct_, field_name_), \
        .array = { \
                .element_descr = Z_JSON_ELEMENT_DESCR( \
                        struct_, len_field_, JSON_TOK_ARRAY_START, \
                        Z_JSON_DESCR_ARRAY( \
                                elem_descr_, \
                                1 + ZERO_OR_COMPILE_ERROR(elem_descr_len_ == 1))), \
                .n_elements = (max_len_), \
        }, \
}
```

原文示例（Example）：

```c
 struct person_height {
     const char *name;
     int32_t height;
 };

 struct person_heights_array {
     struct person_height heights;
 }

 struct people_heights {
     struct person_height_array heights[10];
     size_t heights_len;
 };

 struct json_obj_descr person_height_descr[] = {
     JSON_OBJ_DESCR_PRIM(struct person_height, name, JSON_TOK_STRING),
     JSON_OBJ_DESCR_PRIM(struct person_height, height, JSON_TOK_NUMBER),
 };

 struct json_obj_descr person_height_array_descr[] = {
     JSON_OBJ_DESCR_OBJECT(struct person_heights_array,
                           heights, person_height_descr),
 };

 struct json_obj_descr array_array[] = {
      JSON_OBJ_DESCR_ARRAY_ARRAY(struct people_heights, heights, 10,
                                 heights_len, person_height_array_descr,
                                 ARRAY_SIZE(person_height_array_descr)),
 };
```


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `struct_` | 保存各值的结构体。 |
| `field_name_` | 结构体中保存数组的字段名。 |
| `max_len_` | 数组的最大元素数量。 |
| `len_field_` | 结构体中保存数组元素数量的字段名。 |
| `elem_descr_` | 元素描述符，指向描述符数组。 |
| `elem_descr_len_` | `elem_descr_` 的元素数量。 |

> 译注：原示例在 person_heights_array 的定义后缺少分号，后续又写成 person_height_array，类型名不一致。示例按原页保留；实际使用时须统一类型名称并补齐分号，不能视为已经编译通过的完整程序。

## 6.9\_JSON\_OBJ\_DESCR\_ARRAY\_ARRAY\_NAMED

<a id="ga9fea9111ac1024c8feb066cd53a4045b"></a>
<a id="r_ga9fea9111ac1024c8feb066cd53a4045b"></a>

```c
#define JSON_OBJ_DESCR_ARRAY_ARRAY_NAMED( struct_, json_field_name_, struct_field_name_, max_len_, len_field_, elem_descr_, elem_descr_len_ )
```

```c
#include <zephyr/data/json.h>
```

[`JSON_OBJ_DESCR_ARRAY_ARRAY`](#gaed8189235fd30d2bc041cafee9591ec9) 的变体，适用于结构体字段名与 JSON 字段名不同的情况。

当 JSON 字段名不是有效的 C 标识符（C Identifier）时，这种写法很有用。

宏展开（Value）：

```c
{ \
        .field_name = (#json_field_name_), \
        .align_shift = Z_ALIGN_SHIFT(struct_), \
        .field_name_len = sizeof(#json_field_name_) - 1, \
        .type = JSON_TOK_ARRAY_START, \
        .offset = offsetof(struct_, struct_field_name_), \
        .array = { \
                .element_descr = Z_JSON_ELEMENT_DESCR( \
                        struct_, len_field_, JSON_TOK_ARRAY_START, \
                        Z_JSON_DESCR_ARRAY( \
                                elem_descr_, \
                                1 + ZERO_OR_COMPILE_ERROR(elem_descr_len_ == 1))), \
                .n_elements = (max_len_), \
        }, \
}
```


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `struct_` | 保存各值的结构体。 |
| `json_field_name_` | 字符串，表示 JSON 字符串中的字段名。 |
| `struct_field_name_` | 结构体中保存数组的字段名。 |
| `max_len_` | 数组的最大元素数量。 |
| `len_field_` | 结构体中保存数组元素数量的字段名。 |
| `elem_descr_` | 元素描述符，指向描述符数组。 |
| `elem_descr_len_` | `elem_descr_` 的元素数量。 |

**参见（See Also）**：另见 [`JSON_OBJ_DESCR_ARRAY_ARRAY`](#gaed8189235fd30d2bc041cafee9591ec9)。

## 6.10\_JSON\_OBJ\_DESCR\_ARRAY\_NAMED

<a id="ga4a5bafd64de8abcbc2b5c039bd59ec84"></a>
<a id="r_ga4a5bafd64de8abcbc2b5c039bd59ec84"></a>

```c
#define JSON_OBJ_DESCR_ARRAY_NAMED( struct_, json_field_name_, struct_field_name_, max_len_, len_field_, elem_type_ )
```

```c
#include <zephyr/data/json.h>
```

[`JSON_OBJ_DESCR_ARRAY`](#ga0b510decbc755c82903b54fcbc4a3b64) 的变体，适用于结构体字段名与 JSON 字段名不同的情况。

当 JSON 字段名不是有效的 C 标识符（C Identifier）时，这种写法很有用。

宏展开（Value）：

```c
{ \
        .field_name = (json_field_name_), \
        .align_shift = Z_ALIGN_SHIFT(struct_), \
        .field_name_len = sizeof(json_field_name_) - 1, \
        .type = JSON_TOK_ARRAY_START, \
        .offset = offsetof(struct_, struct_field_name_), \
        .array = { \
                .element_descr = Z_JSON_ELEMENT_DESCR(struct_, len_field_, \
                        elem_type_, \
                        Z_JSON_DESCR_FIELD(struct_, struct_field_name_[0])), \
                .n_elements = (max_len_), \
        }, \
}
```


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `struct_` | 保存各值的结构体。 |
| `json_field_name_` | 字符串，表示 JSON 字符串中的字段名。 |
| `struct_field_name_` | 结构体中的字段名。 |
| `max_len_` | 数组的最大元素数量。 |
| `len_field_` | 结构体中保存数组元素数量的字段名。 |
| `elem_type_` | 元素类型，必须是基本类型（Primitive Type）。 |

**参见（See Also）**：另见 [`JSON_OBJ_DESCR_ARRAY`](#ga0b510decbc755c82903b54fcbc4a3b64)。

## 6.11\_JSON\_OBJ\_DESCR\_OBJ\_ARRAY

<a id="gae012264df03546a1c01eec4216b52ffd"></a>
<a id="r_gae012264df03546a1c01eec4216b52ffd"></a>

```c
#define JSON_OBJ_DESCR_OBJ_ARRAY( struct_, field_name_, max_len_, len_field_, elem_descr_, elem_descr_len_ )
```

```c
#include <zephyr/data/json.h>
```

用于为对象数组（Array of Objects）声明描述符的辅助宏。

用法示例如下：

宏展开（Value）：

```c
{ \
        .field_name = (#field_name_), \
        .align_shift = Z_ALIGN_SHIFT(struct_), \
        .field_name_len = sizeof(#field_name_) - 1, \
        .type = JSON_TOK_ARRAY_START, \
        .offset = offsetof(struct_, field_name_), \
        .array = { \
                .element_descr = Z_JSON_ELEMENT_DESCR(struct_, len_field_, \
                        JSON_TOK_OBJECT_START, \
                        Z_JSON_DESCR_OBJ(elem_descr_, elem_descr_len_)), \
                .n_elements = (max_len_), \
        }, \
}
```

原文示例（Example）：

```c
 struct person_height {
     const char *name;
     int32_t height;
 };

 struct people_heights {
     struct person_height heights[10];
     size_t heights_len;
 };

 struct json_obj_descr person_height_descr[] = {
      JSON_OBJ_DESCR_PRIM(struct person_height, name, JSON_TOK_STRING),
      JSON_OBJ_DESCR_PRIM(struct person_height, height, JSON_TOK_NUMBER),
 };

 struct json_obj_descr array[] = {
      JSON_OBJ_DESCR_OBJ_ARRAY(struct people_heights, heights, 10,
                               heights_len, person_height_descr,
                               ARRAY_SIZE(person_height_descr)),
 };
```


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `struct_` | 保存各值的结构体。 |
| `field_name_` | 结构体中保存数组的字段名。 |
| `max_len_` | 数组的最大元素数量。 |
| `len_field_` | 结构体中保存数组元素数量的字段名。 |
| `elem_descr_` | 元素描述符，指向描述符数组。 |
| `elem_descr_len_` | `elem_descr_` 的元素数量。 |

## 6.12\_JSON\_OBJ\_DESCR\_OBJ\_ARRAY\_NAMED

<a id="gaa6602833e59c7e5205d69cc7c4ab2bba"></a>
<a id="r_gaa6602833e59c7e5205d69cc7c4ab2bba"></a>

```c
#define JSON_OBJ_DESCR_OBJ_ARRAY_NAMED( struct_, json_field_name_, struct_field_name_, max_len_, len_field_, elem_descr_, elem_descr_len_ )
```

```c
#include <zephyr/data/json.h>
```

[`JSON_OBJ_DESCR_OBJ_ARRAY`](#gae012264df03546a1c01eec4216b52ffd) 的变体，适用于结构体字段名与 JSON 字段名不同的情况。

当 JSON 字段名不是有效的 C 标识符（C Identifier）时，这种写法很有用。

用法示例如下：

宏展开（Value）：

```c
{ \
        .field_name = json_field_name_, \
        .align_shift = Z_ALIGN_SHIFT(struct_), \
        .field_name_len = sizeof(json_field_name_) - 1, \
        .type = JSON_TOK_ARRAY_START, \
        .offset = offsetof(struct_, struct_field_name_), \
        .array = { \
                .element_descr = Z_JSON_ELEMENT_DESCR(struct_, len_field_, \
                        JSON_TOK_OBJECT_START, \
                        Z_JSON_DESCR_OBJ(elem_descr_, elem_descr_len_)), \
                .n_elements = (max_len_), \
        }, \
}
```

原文示例（Example）：

```c
 struct person_height {
     const char *name;
     int32_t height;
 };

 struct people_heights {
     struct person_height heights[10];
     size_t heights_len;
 };

 struct json_obj_descr person_height_descr[] = {
      JSON_OBJ_DESCR_PRIM(struct person_height, name, JSON_TOK_STRING),
      JSON_OBJ_DESCR_PRIM(struct person_height, height, JSON_TOK_NUMBER),
 };

 struct json_obj_descr array[] = {
      JSON_OBJ_DESCR_OBJ_ARRAY_NAMED(struct people_heights,
                                     "people-heights", heights,
                                     10, heights_len,
                                     person_height_descr,
                                     ARRAY_SIZE(person_height_descr)),
 };
```


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `struct_` | 保存各值的结构体。 |
| `json_field_name_` | 字符串，表示 JSON 字符串中数组的字段名。 |
| `struct_field_name_` | 结构体中保存数组的字段名。 |
| `max_len_` | 数组的最大元素数量。 |
| `len_field_` | 结构体中保存数组元素数量的字段名。 |
| `elem_descr_` | 元素描述符，指向描述符数组。 |
| `elem_descr_len_` | `elem_descr_` 的元素数量。 |

## 6.13\_JSON\_OBJ\_DESCR\_OBJECT

<a id="ga4ee365f43cfa86a214973defe81f1e88"></a>
<a id="r_ga4ee365f43cfa86a214973defe81f1e88"></a>

```c
#define JSON_OBJ_DESCR_OBJECT( struct_, field_name_, sub_descr_ )
```

```c
#include <zephyr/data/json.h>
```

用于为对象值声明描述符的辅助宏。

用法示例如下：

宏展开（Value）：

```c
{ \
        .field_name = (#field_name_), \
        .align_shift = Z_ALIGN_SHIFT(struct_), \
        .field_name_len = (sizeof(#field_name_) - 1), \
        .type = JSON_TOK_OBJECT_START, \
        .offset = offsetof(struct_, field_name_), \
        .object = { \
                .sub_descr = sub_descr_, \
                .sub_descr_len = ARRAY_SIZE(sub_descr_), \
        }, \
}
```

原文示例（Example）：

```c
 struct nested {
     int32_t foo;
     struct {
        int32_t baz;
     } bar;
 };

 struct json_obj_descr nested_bar[] = {
     { ... declare bar.baz descriptor ... },
 };
 struct json_obj_descr nested[] = {
     { ... declare foo descriptor ... },
     JSON_OBJ_DESCR_OBJECT(struct nested, bar, nested_bar),
 };
```


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `struct_` | 保存各值的结构体。 |
| `field_name_` | 结构体中的字段名。 |
| `sub_descr_` | 描述子对象（Subobject）的 [`json_obj_descr`](P009_JSON对象描述符.md) 数组。 |

> 译注：原例中的“declare bar.baz descriptor”和“declare foo descriptor”分别表示“在这里声明 bar.baz 的描述符”和“在这里声明 foo 的描述符”。省略号是占位文字，需要以真实描述符替换。

## 6.14\_JSON\_OBJ\_DESCR\_OBJECT\_NAMED

<a id="ga8f8d03241e4f69d5f7147792db9a9fe9"></a>
<a id="r_ga8f8d03241e4f69d5f7147792db9a9fe9"></a>

```c
#define JSON_OBJ_DESCR_OBJECT_NAMED( struct_, json_field_name_, struct_field_name_, sub_descr_ )
```

```c
#include <zephyr/data/json.h>
```

[`JSON_OBJ_DESCR_OBJECT`](#ga4ee365f43cfa86a214973defe81f1e88) 的变体，适用于结构体字段名与 JSON 字段名不同的情况。

当 JSON 字段名不是有效的 C 标识符（C Identifier）时，这种写法很有用。

宏展开（Value）：

```c
{ \
        .field_name = (json_field_name_), \
        .align_shift = Z_ALIGN_SHIFT(struct_), \
        .field_name_len = (sizeof(json_field_name_) - 1), \
        .type = JSON_TOK_OBJECT_START, \
        .offset = offsetof(struct_, struct_field_name_), \
        .object = { \
                .sub_descr = sub_descr_, \
                .sub_descr_len = ARRAY_SIZE(sub_descr_), \
        }, \
}
```


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `struct_` | 保存各值的结构体。 |
| `json_field_name_` | 字符串，表示 JSON 字符串中的字段名。 |
| `struct_field_name_` | 结构体中的字段名。 |
| `sub_descr_` | 描述子对象（Subobject）的 [`json_obj_descr`](P009_JSON对象描述符.md) 数组。 |

**参见（See Also）**：另见 [`JSON_OBJ_DESCR_OBJECT`](#ga4ee365f43cfa86a214973defe81f1e88)。

## 6.15\_JSON\_OBJ\_DESCR\_PRIM

<a id="ga1ed917f5a247ca33f2778afe62ff1a88"></a>
<a id="r_ga1ed917f5a247ca33f2778afe62ff1a88"></a>

```c
#define JSON_OBJ_DESCR_PRIM( struct_, field_name_, type_ )
```

```c
#include <zephyr/data/json.h>
```

用于为受支持的基本类型值声明描述符的辅助宏。

用法示例如下：

宏展开（Value）：

```c
{ \
        .field_name = (#field_name_), \
        .align_shift = Z_ALIGN_SHIFT(struct_), \
        .field_name_len = sizeof(#field_name_) - 1, \
        .type = type_, \
        .offset = offsetof(struct_, field_name_), \
        .field = { \
                .size = SIZEOF_FIELD(struct_, field_name_) \
        }, \
}
```

原文示例（Example）：

```c
struct foo {
    int32_t some_int;
};

struct json_obj_descr foo[] = {
    JSON_OBJ_DESCR_PRIM(struct foo, some_int, JSON_TOK_NUMBER),
};
```


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `struct_` | 保存各值的结构体。 |
| `field_name_` | 结构体中的字段名。 |
| `type_` | 基本类型 JSON 值对应的词元类型。必须是以下之一：字符串用 [`JSON_TOK_STRING`](#gga18a137ac5e2998d375540298670797c4ab145f07a93c4fdcf60c9052fbd9a7afc)，数字用 [`JSON_TOK_NUMBER`](#gga18a137ac5e2998d375540298670797c4ae25f16ae591eb17d4074e6dcc2f1e62c)，布尔值用 [`JSON_TOK_TRUE`](#gga18a137ac5e2998d375540298670797c4a87ffb12e4d174bb4427d9a72eabca7e3)（或 [`JSON_TOK_FALSE`](#gga18a137ac5e2998d375540298670797c4a8df1b1d0061d7e289f94bae1df35baa7)）。 |

## 6.16\_JSON\_OBJ\_DESCR\_PRIM\_NAMED

<a id="gaad081c4f8debcb41779bd5879ed8bbd4"></a>
<a id="r_gaad081c4f8debcb41779bd5879ed8bbd4"></a>

```c
#define JSON_OBJ_DESCR_PRIM_NAMED( struct_, json_field_name_, struct_field_name_, type_ )
```

```c
#include <zephyr/data/json.h>
```

[`JSON_OBJ_DESCR_PRIM`](#ga1ed917f5a247ca33f2778afe62ff1a88) 的变体，适用于结构体字段名与 JSON 字段名不同的情况。

当 JSON 字段名不是有效的 C 标识符（C Identifier）时，这种写法很有用。

宏展开（Value）：

```c
{ \
        .field_name = (json_field_name_), \
        .align_shift = Z_ALIGN_SHIFT(struct_), \
        .field_name_len = sizeof(json_field_name_) - 1, \
        .type = type_, \
        .offset = offsetof(struct_, struct_field_name_), \
        .field = { \
                .size = SIZEOF_FIELD(struct_, struct_field_name_) \
        }, \
}
```


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `struct_` | 保存各值的结构体。 |
| `json_field_name_` | 字符串，表示 JSON 字符串中的字段名。 |
| `struct_field_name_` | 结构体中的字段名。 |
| `type_` | 基本类型 JSON 值对应的词元类型。 |

**参见（See Also）**：另见 [`JSON_OBJ_DESCR_PRIM`](#ga1ed917f5a247ca33f2778afe62ff1a88)。

## 6.17\_json\_append\_bytes\_t

<a id="gacb409ebe9c59789a5d9aca02c6c94674"></a>
<a id="r_gacb409ebe9c59789a5d9aca02c6c94674"></a>

```c
typedef int(* json_append_bytes_t) (const char *bytes, size_t len, void *data)
```

```c
#include <zephyr/data/json.h>
```

编码 JSON 数据时用于向缓冲区追加字节的函数指针类型（Function Pointer Type）。


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `bytes` | 要写入输出的内容。 |
| `len` | 向输出追加的字节数。 |
| `data` | 使用者提供的指针。 |

**返回（Returns）**：此回调应在发生错误时返回负数，该值会传播到 [`json_obj_encode`](#gafec772f687a0280f5211139bd019e582)() 的返回值；成功时返回 0。

## 6.18\_json\_tokens

<a id="ga18a137ac5e2998d375540298670797c4"></a>
<a id="r_ga18a137ac5e2998d375540298670797c4"></a>

```c
enum json_tokens {
        /* Before changing this enum, ensure that its maximum
         * value is still within 7 bits. See comment next to the
         * declaration of `type` in struct json_obj_descr.
         */

        JSON_TOK_NONE = '_',
        JSON_TOK_OBJECT_START = '{',
        JSON_TOK_OBJECT_END = '}',
        JSON_TOK_ARRAY_START = '[',
        JSON_TOK_ARRAY_END = ']',
        JSON_TOK_STRING = '"',
        JSON_TOK_STRING_BUF = 's',
        JSON_TOK_COLON = ':',
        JSON_TOK_COMMA = ',',
        JSON_TOK_NUMBER = '0',
        JSON_TOK_FLOAT = '1',
        JSON_TOK_OPAQUE = '2',
        JSON_TOK_OBJ_ARRAY = '3',
        JSON_TOK_ENCODED_OBJ = '4',
        JSON_TOK_INT64 = '5',
        JSON_TOK_UINT64 = '6',
        JSON_TOK_FLOAT_FP = '7',
        JSON_TOK_DOUBLE_FP = '8',
        JSON_TOK_INT = 'i',
        JSON_TOK_UINT = 'u',
        JSON_TOK_TRUE = 't',
        JSON_TOK_FALSE = 'f',
        JSON_TOK_MIXED_ARRAY = 'm',
        JSON_TOK_NULL = 'n',
        JSON_TOK_ERROR = '!',
        JSON_TOK_EOF = '\0',
};
```

```c
#include <zephyr/data/json.h>
```


**枚举值（Enumerators）**

| 名称 | 说明 |
| --- | --- |
| `JSON_TOK_NONE` | 原页未提供文字说明。 |
| `JSON_TOK_OBJECT_START` | 原页未提供文字说明。 |
| `JSON_TOK_OBJECT_END` | 原页未提供文字说明。 |
| `JSON_TOK_ARRAY_START` | 原页未提供文字说明。 |
| `JSON_TOK_ARRAY_END` | 原页未提供文字说明。 |
| `JSON_TOK_STRING` | 原页未提供文字说明。 |
| `JSON_TOK_STRING_BUF` | 原页未提供文字说明。 |
| `JSON_TOK_COLON` | 原页未提供文字说明。 |
| `JSON_TOK_COMMA` | 原页未提供文字说明。 |
| `JSON_TOK_NUMBER` | 原页未提供文字说明。 |
| `JSON_TOK_FLOAT` | 原页未提供文字说明。 |
| `JSON_TOK_OPAQUE` | 原页未提供文字说明。 |
| `JSON_TOK_OBJ_ARRAY` | 原页未提供文字说明。 |
| `JSON_TOK_ENCODED_OBJ` | 原页未提供文字说明。 |
| `JSON_TOK_INT64` | 原页未提供文字说明。 |
| `JSON_TOK_UINT64` | 原页未提供文字说明。 |
| `JSON_TOK_FLOAT_FP` | 原页未提供文字说明。 |
| `JSON_TOK_DOUBLE_FP` | 原页未提供文字说明。 |
| `JSON_TOK_INT` | 原页未提供文字说明。 |
| `JSON_TOK_UINT` | 原页未提供文字说明。 |
| `JSON_TOK_TRUE` | 原页未提供文字说明。 |
| `JSON_TOK_FALSE` | 原页未提供文字说明。 |
| `JSON_TOK_MIXED_ARRAY` | 原页未提供文字说明。 |
| `JSON_TOK_NULL` | 原页未提供文字说明。 |
| `JSON_TOK_ERROR` | 原页未提供文字说明。 |
| `JSON_TOK_EOF` | 原页未提供文字说明。 |

## 6.19\_json\_arr\_encode()

<a id="ga4ffccdc602ab98d489499bf6fa4fa6c5"></a>
<a id="r_ga4ffccdc602ab98d489499bf6fa4fa6c5"></a>

```c
int json_arr_encode ( const struct json_obj_descr * descr, const void * val, json_append_bytes_t append_bytes, void * data )
```

```c
#include <zephyr/data/json.h>
```

使用任意写出函数（Writer Function）编码数组。


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `descr` | 描述符数组的指针。 |
| `val` | 保存各值的结构体。 |
| `append_bytes` | 向输出追加字节的函数。 |
| `data` | 传给 `append_bytes` 回调函数的数据指针。 |

**返回（Returns）**：对象编码成功返回 0；负值表示错误。

> 译注：返回说明沿用原文的“object（对象）”措辞；本函数实际编码数组。

## 6.20\_json\_arr\_encode\_buf()

<a id="gafd27bbcb898dc902cf1dadd3369cf923"></a>
<a id="r_gafd27bbcb898dc902cf1dadd3369cf923"></a>

```c
int json_arr_encode_buf ( const struct json_obj_descr * descr, const void * val, char * buffer, size_t buf_size )
```

```c
#include <zephyr/data/json.h>
```

在连续内存位置中编码数组。


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `descr` | 描述符数组的指针。 |
| `val` | 保存各值的结构体。 |
| `buffer` | 用于保存 JSON 数据的缓冲区。 |
| `buf_size` | 缓冲区大小，单位为字节，必须包含终止 `NUL` 字符所需的空间。 |

**返回（Returns）**：对象编码成功返回 0；负值表示 errno.h 中定义的错误。

> 译注：返回说明沿用原文的“object（对象）”措辞；本函数实际编码数组。

## 6.21\_json\_arr\_parse()

<a id="gab4e6ad4a040c271d74eaa313c580a739"></a>
<a id="r_gab4e6ad4a040c271d74eaa313c580a739"></a>

```c
int json_arr_parse ( char * json, size_t len, const struct json_obj_descr * descr, void * val )
```

```c
#include <zephyr/data/json.h>
```

按照 `descr` 所指向的描述符，解析 `json` 所指向、长度为 `len` 的 JSON 编码数组。

值保存到 `val` 所指向的结构体中。按下面方式设置描述符：

```c
struct s { int32_t foo; char *bar; } struct json_obj_descr descr[] = { JSON_OBJ_DESCR_PRIM(struct s, foo, JSON_TOK_NUMBER), JSON_OBJ_DESCR_PRIM(struct s, bar, JSON_TOK_STRING), }; struct a { struct s baz[10]; size_t count; } struct json_obj_descr array[] = { JSON_OBJ_DESCR_OBJ_ARRAY(struct a, baz, 10, count, descr, ARRAY_SIZE(descr)), };
```

本解析器面向机器间通信（Machine-to-machine Communication），为简化设计采用了几项取舍：（1）不对字符串进行反转义（Unescape），但只接受有效转义序列；（2）不验证 UTF-8 编码；（3）只支持整数，因为最小 C 库（Minimal libc）没有 `strtod`()。


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `json（原页显示 JSON）` | 待解析的 JSON 编码数组的指针。 |
| `len` | JSON 编码数组的长度。 |
| `descr` | 描述符数组的指针。 |
| `val` | 用于保存解码值的结构体指针。 |

**返回（Returns）**：数组解析成功返回 0；负值表示 errno.h 中定义的错误。

> 译注：原文内联示例的 struct s 和 struct a 定义后缺少分号，且片段没有展示完整调用。代码按原页保留，不能直接当作完整可编译程序。原文“只支持整数”的概括也已落后于本次读取的官方实现：它含 [`JSON_TOK_FLOAT_FP`](#gga18a137ac5e2998d375540298670797c4aa5cf82525a71c8a9ca8c69c1adb0ff62) 和 [`JSON_TOK_DOUBLE_FP`](#gga18a137ac5e2998d375540298670797c4a6e273425323ac63abad33f757572219b) 的解码分支；实际可用类型与 C 库、配置和版本有关，不能据旧句子排除所有浮点支持。

## 6.22\_json\_arr\_separate\_object\_parse\_init()

<a id="ga6196411958e2e9b3683af4c281214b92"></a>
<a id="r_ga6196411958e2e9b3683af4c281214b92"></a>

```c
int json_arr_separate_object_parse_init ( struct json_obj * json, char * payload, size_t len )
```

```c
#include <zephyr/data/json.h>
```

初始化按单个对象处理数组的解析过程。

JSON 编码数组每次解析一个对象。数据由 `payload` 提供，大小为 `len` 字节。

函数验证已检测到 JSON 数组起点，并初始化 `json` 对象，以便逐个解析 JSON 对象。


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `json（原页显示 JSON）` | 提供解析器状态（Parser State）的存储空间，在解析数组时使用。 |
| `payload` | 待解析的 JSON 编码数组的指针。 |
| `len` | JSON 编码数组的长度。 |

**返回（Returns）**：检测到数组起点并成功初始化时返回 0；失败返回负错误码。

## 6.23\_json\_arr\_separate\_parse\_object()

<a id="ga64859a835e7cb88c2499360fb00ca344"></a>
<a id="r_ga64859a835e7cb88c2499360fb00ca344"></a>

```c
int json_arr_separate_parse_object ( struct json_obj * json, const struct json_obj_descr * descr, size_t descr_len, void * val )
```

```c
#include <zephyr/data/json.h>
```

从数组中解析单个对象。

按照 `descr` 所指向的描述符，解析 `json` 对象数组所指向的 JSON 编码对象；原文将其大小记为 `len`。


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `json（原页显示 JSON）` | JSON 对象消息状态的指针。 |
| `descr` | 描述符数组的指针。 |
| `descr_len` | 描述符数组的元素数量，必须小于 31。 |
| `val` | 用于保存解码值的结构体指针。 |

**返回（Returns）**：错误时返回小于 0 的值；消息结束返回 0；成功时返回已解码字段的位图（Bitmap）：描述符中的第一个字段正确解码时置位 bit 0，依此类推。

> 译注：原文正文提到 `len`，但本函数声明没有 `len` 参数；长度在 [`json_arr_separate_object_parse_init`](#ga6196411958e2e9b3683af4c281214b92) 初始化时提供。这里保留原文表述并明确两步调用的边界。

## 6.24\_json\_calc\_encoded\_arr\_len()

<a id="gad612b8441a21dca34cfeec6257877509"></a>
<a id="r_gad612b8441a21dca34cfeec6257877509"></a>

```c
ssize_t json_calc_encoded_arr_len ( const struct json_obj_descr * descr, const void * val )
```

```c
#include <zephyr/data/json.h>
```

计算完整编码数组所需的字符串长度。


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `descr` | 描述符数组的指针。 |
| `val` | 保存各值的结构体。 |

**返回（Returns）**：原文返回说明：大于 0 时为编码这些值所需的字节数，随后写有“返回错误码”；该句的错误条件表述不完整，见下方译注。

> 译注：原文返回说明的条件不完整。本次读取的官方实现先检查编码返回值 ret < 0，失败返回该错误码，否则返回统计的总长度；不包含字符串末尾 `NUL`，分配缓冲区时另留终止字符空间。

## 6.25\_json\_calc\_encoded\_len()

<a id="ga41e6e90beef8bae12fca1de2584145bb"></a>
<a id="r_ga41e6e90beef8bae12fca1de2584145bb"></a>

```c
ssize_t json_calc_encoded_len ( const struct json_obj_descr * descr, size_t descr_len, const void * val )
```

```c
#include <zephyr/data/json.h>
```

计算完整编码对象所需的字符串长度。


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `descr` | 描述符数组的指针。 |
| `descr_len` | 描述符数组的元素数量。 |
| `val` | 保存各值的结构体。 |

**返回（Returns）**：原文返回说明：大于 0 时为编码这些值所需的字节数，随后写有“返回错误码”；该句的错误条件表述不完整，见下方译注。

> 译注：原文返回说明的条件不完整。本次读取的官方 lib/utils/json.c 实现先检查编码返回值 ret < 0，失败返回该错误码，否则返回统计的总长度；总长度不包含字符串末尾 `NUL`。用于分配字符串缓冲区时还需计入终止字符。

## 6.26\_json\_calc\_escaped\_len()

<a id="ga5ef155a3a6444801592badd6a092734c"></a>
<a id="r_ga5ef155a3a6444801592badd6a092734c"></a>

```c
size_t json_calc_escaped_len ( const char * str, size_t len )
```

```c
#include <zephyr/data/json.h>
```

计算经 JSON 转义（Escaping）后的字符串长度。


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `str` | 要分析的字符串。 |
| `len` | 字符串大小。 |

**返回（Returns）**：返回 `str` 经转义后应有的长度。

## 6.27\_json\_calc\_mixed\_arr\_len()

<a id="ga20efb9b01733fadd8086dcab8be2ca85"></a>
<a id="r_ga20efb9b01733fadd8086dcab8be2ca85"></a>

```c
ssize_t json_calc_mixed_arr_len ( const struct json_mixed_arr_descr * descr, size_t descr_len, void * val )
```

```c
#include <zephyr/data/json.h>
```

计算编码后的 JSON 混合数组（Mixed Array）的长度。

按照提供的描述符，计算将给定结构体编码为 JSON 混合数组所需的字节数。


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `descr` | 描述混合数组结构的描述符数组。 |
| `descr_len` | 描述符数组的元素数量。 |
| `val` | 要编码的结构体指针。 |

**返回（Returns）**：返回编码所需的字节数，或负错误码。

## 6.28\_json\_escape()

<a id="ga43ee6d1fbd3fa8fb2ae052844b465dda"></a>
<a id="r_ga43ee6d1fbd3fa8fb2ae052844b465dda"></a>

```c
ssize_t json_escape ( char * str, size_t * len, size_t buf_size )
```

```c
#include <zephyr/data/json.h>
```

转义字符串，使其可用于编码 JSON 对象。


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `str` | 要转义的字符串；转义结果存放于此参数所指向的缓冲区。 |
| `len` | 指向一个 `size_t`，转义前保存原大小，转义后保存处理后的大小。 |
| `buf_size` | `str` 所指向缓冲区的大小。 |

**返回（Returns）**：字符串正确转义返回 0；缓冲区空间不足以容纳转义结果时返回 -ENOMEM。

## 6.29\_json\_mixed\_arr\_encode()

<a id="ga210433173e35241dea8976bd7f532570"></a>
<a id="r_ga210433173e35241dea8976bd7f532570"></a>

```c
int json_mixed_arr_encode ( const struct json_mixed_arr_descr * descr, size_t descr_len, void * val, json_append_bytes_t append_bytes, void * data )
```

```c
#include <zephyr/data/json.h>
```

将 C 结构体编码为 JSON 混合数组。

把混合数组描述符所描述的 C 结构体编码为 JSON 数组。


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `descr` | 描述混合数组结构的描述符数组。 |
| `descr_len` | 描述符数组的元素数量。 |
| `val` | 要编码的结构体指针。 |
| `append_bytes` | 向输出追加字节的函数。 |
| `data` | 传给 `append_bytes` 回调函数的数据指针。 |

**返回（Returns）**：混合数组编码成功返回 0；失败返回负错误码。

## 6.30\_json\_mixed\_arr\_encode\_buf()

<a id="ga51565a7e00a520d1257a0b6a91058a3d"></a>
<a id="r_ga51565a7e00a520d1257a0b6a91058a3d"></a>

```c
int json_mixed_arr_encode_buf ( const struct json_mixed_arr_descr * descr, size_t descr_len, void * val, char * buffer, size_t buf_size )
```

```c
#include <zephyr/data/json.h>
```

将 C 结构体编码为 JSON 混合数组并写入缓冲区。

把混合数组描述符所描述的 C 结构体编码为 JSON 数组，并将结果写入提供的缓冲区。


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `descr` | 描述混合数组结构的描述符数组。 |
| `descr_len` | 描述符数组的元素数量。 |
| `val` | 要编码的结构体指针。 |
| `buffer` | 用于写入 JSON 字符串的输出缓冲区。 |
| `buf_size` | 输出缓冲区大小。 |

**返回（Returns）**：混合数组编码成功返回 0；失败返回负错误码。

## 6.31\_json\_mixed\_arr\_parse()

<a id="ga4348a45b1a45a271e3d62a0c5a4d9c0d"></a>
<a id="r_ga4348a45b1a45a271e3d62a0c5a4d9c0d"></a>

```c
int json_mixed_arr_parse ( char * json, size_t len, const struct json_mixed_arr_descr * descr, size_t descr_len, void * val )
```

```c
#include <zephyr/data/json.h>
```

将 JSON 混合数组解析到 C 结构体中。

按照提供的混合数组描述符解析 JSON 数组，并把结果保存到使用者提供的结构体中；该数组的各元素可以具有不同类型。


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `json（原页显示 JSON）` | 输入 JSON 字符串的指针。 |
| `len` | 输入 JSON 字符串的长度。 |
| `descr` | 描述混合数组结构的描述符数组。 |
| `descr_len` | 描述符数组的元素数量。 |
| `val` | 要填入解析结果的结构体指针。 |

**返回（Returns）**：错误时返回小于 0 的值；成功时返回已解析的元素数量。

## 6.32\_json\_obj\_encode()

<a id="gafec772f687a0280f5211139bd019e582"></a>
<a id="r_gafec772f687a0280f5211139bd019e582"></a>

```c
int json_obj_encode ( const struct json_obj_descr * descr, size_t descr_len, const void * val, json_append_bytes_t append_bytes, void * data )
```

```c
#include <zephyr/data/json.h>
```

使用任意写出函数编码对象。


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `descr` | 描述符数组的指针。 |
| `descr_len` | 描述符数组的元素数量。 |
| `val` | 保存各值的结构体。 |
| `append_bytes` | 向输出追加字节的函数。 |
| `data` | 传给 `append_bytes` 回调函数的数据指针。 |

**返回（Returns）**：对象编码成功返回 0；负值表示错误。

## 6.33\_json\_obj\_encode\_buf()

<a id="gab758ad32cfb6369f4967a6842ac63245"></a>
<a id="r_gab758ad32cfb6369f4967a6842ac63245"></a>

```c
int json_obj_encode_buf ( const struct json_obj_descr * descr, size_t descr_len, const void * val, char * buffer, size_t buf_size )
```

```c
#include <zephyr/data/json.h>
```

在连续内存位置中编码对象。


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `descr` | 描述符数组的指针。 |
| `descr_len` | 描述符数组的元素数量。 |
| `val` | 保存各值的结构体。 |
| `buffer` | 用于保存 JSON 数据的缓冲区。 |
| `buf_size` | 缓冲区大小，单位为字节，必须包含终止 `NUL` 字符所需的空间。 |

**返回（Returns）**：对象编码成功返回 0；负值表示 errno.h 中定义的错误。

## 6.34\_json\_obj\_next\_key\_value()

<a id="ga9e3a815cae48a9825ff9904b97618ecb"></a>
<a id="r_ga9e3a815cae48a9825ff9904b97618ecb"></a>

```c
int json_obj_next_key_value ( struct json_obj * json, struct json_obj_key_value * kv )
```

```c
#include <zephyr/data/json.h>
```

返回 JSON 对象的下一个顶层成员（Top-level Member）。

遍历由 [`json_obj_separate_parse_init`](#gaeef63343b8b15edc3ee96028332bfb39) 初始化的对象中的一个“`key`: `value`”成员。值作为原始、未解码的片段（Raw Span）保存在 `kv`->`value` 中，由调用者根据键分派处理。标量片段覆盖其值文本；对象或数组片段覆盖括号完整配对的整个 {...} 或 [...]，类型分别为 [`JSON_TOK_OBJECT_START`](#gga18a137ac5e2998d375540298670797c4a81e303d23da0b3d8504cc4a7ee7d52e8) 或 [`JSON_TOK_ARRAY_START`](#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd)。因此，可以依据 `kv`->`value`.`type` 将值片段直接交给 [`json_obj_parse`](#ga73997fa2154fcbc80f37edd7bcf3477a)() 或 [`json_arr_parse`](#gab4e6ad4a040c271d74eaa313c580a739)() 等解码器。


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `json（原页显示 JSON）` | JSON 对象解析器状态的指针。 |
| `kv` | 用于保存返回的键和值的存储空间指针。 |

**原文注意（Note）**：`kv`->`key` 和 `kv`->`value` 都指向传给 [`json_obj_separate_parse_init`](#gaeef63343b8b15edc3ee96028332bfb39) 的 `payload` 缓冲区内部；它们是借用的引用（Borrowed Reference），有效期不超过该缓冲区。如需稳定或可修改的副本，例如要原地解析之前，应先复制这些片段。

**返回（Returns）**：成功返回 0，此时 `kv`->`key` 指向成员键，`kv`->`value` 保存原始值片段；到达对象末尾也返回 0，但 `kv`->`key` 被设为 `NULL`。输入格式错误或容器嵌套超过 64 层时返回负错误码。

## 6.35\_json\_obj\_parse()

<a id="ga73997fa2154fcbc80f37edd7bcf3477a"></a>
<a id="r_ga73997fa2154fcbc80f37edd7bcf3477a"></a>

```c
int64_t json_obj_parse ( char * json, size_t len, const struct json_obj_descr * descr, size_t descr_len, void * val )
```

```c
#include <zephyr/data/json.h>
```

按照 `descr` 所指向的描述符，解析 `json` 所指向、长度为 `len` 的 JSON 编码对象。

值保存到 `val` 所指向的结构体中。按下面方式设置描述符：

```c
struct s { int32_t foo; char *bar; } struct json_obj_descr descr[] = { JSON_OBJ_DESCR_PRIM(struct s, foo, JSON_TOK_NUMBER), JSON_OBJ_DESCR_PRIM(struct s, bar, JSON_TOK_STRING), };
```

本解析器面向机器间通信（Machine-to-machine Communication），为简化设计采用了几项取舍：（1）不对字符串进行反转义（Unescape），但只接受有效转义序列；（2）不验证 UTF-8 编码；（3）只支持整数，因为最小 C 库（Minimal libc）没有 `strtod`()。

某个描述符解码失败时，行为取决于实际的 JSON 词元类型：

- 标量词元（Scalar Token：字符串、数字、布尔值）：解析器继续尝试其他候选描述符，因为没有发生解析，词法分析器（Lexer）状态仍然有效。
- 复杂词元（Complex Token：对象、数组）：解析器立即返回错误，因为部分解析可能已经破坏词法分析器状态，继续尝试其他描述符不安全。

**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `json（原页显示 JSON）` | 待解析的 JSON 编码值的指针。 |
| `len` | JSON 编码值的长度。 |
| `descr` | 描述符数组的指针。 |
| `descr_len` | 描述符数组的元素数量。受实现细节限制必须小于 63；如果需要更多字段，使用两份描述符。 |
| `val` | 用于保存解码值的结构体指针。 |

**原文注意（Note）**：多态解码（Polymorphic Decoding）：多个描述符可以使用相同字段名，处理可能包含不同 JSON 类型的字段。主要用于标量类型，例如 JSON-RPC 风格的 `id` 字段可以是字符串，也可以是数字。

**原文警告（Warning）**：只写入文档中实际出现的成员；遗漏成员保留调用前的值，因此必须预先初始化结构体。返回位图只覆盖顶层描述符，不覆盖子对象成员或已解码数量之外的数组元素；位索引取决于描述符位置，而非文档字段顺序。返回负值时，失败之前解码的成员可能已经被写入。

**返回（Returns）**：错误时返回小于 0 的值；成功返回已解码字段的位图：描述符中第一个字段正确解码时置位 bit 0，依此类推。

> 译注：原文内联示例的 struct s 定义后缺少分号，应在完整程序中补齐。原文“只支持整数”的概括已落后于本次读取的官方实现，其中存在 [`JSON_TOK_FLOAT_FP`](#gga18a137ac5e2998d375540298670797c4aa5cf82525a71c8a9ca8c69c1adb0ff62) 和 [`JSON_TOK_DOUBLE_FP`](#gga18a137ac5e2998d375540298670797c4a6e273425323ac63abad33f757572219b) 解码分支；实际能力以所用版本及配置为准。返回值是 `int64_t` 位图，只能据相应描述符位判断字段是否解码；必须先初始化目标结构体，并使用可写输入缓冲区。

## 6.36\_json\_obj\_separate\_parse\_init()

<a id="gaeef63343b8b15edc3ee96028332bfb39"></a>
<a id="r_gaeef63343b8b15edc3ee96028332bfb39"></a>

```c
int json_obj_separate_parse_init ( struct json_obj * json, char * payload, size_t len )
```

```c
#include <zephyr/data/json.h>
```

初始化 JSON 对象成员的增量解析（Incremental Parsing）。

JSON 编码对象每次遍历一个顶层成员。数据由 `payload` 提供，大小为 `len` 字节。

验证已检测到 JSON 对象起点，并初始化 `json`，供 [`json_obj_next_key_value`](#ga9e3a815cae48a9825ff9904b97618ecb) 逐成员解析。与 [`json_obj_parse`](#ga73997fa2154fcbc80f37edd7bcf3477a)() 不同，不需要预先提供描述符，适合在运行时选择处理器并向其分派各成员的调用者。


**参数（Parameters）**

| 名称 | 说明 |
| --- | --- |
| `json（原页显示 JSON）` | 提供解析器状态的存储空间，在遍历对象时使用。 |
| `payload` | 待解析的 JSON 编码对象的指针。 |
| `len` | JSON 编码对象的长度。 |

**返回（Returns）**：检测到对象起点并成功初始化时返回 0；失败返回负错误码。

## 6.37\_源码对照与相关阅读

译注：可从本仓库的[JSON头文件](../../../include/zephyr/data/json.h)与[JSON实现](../../../lib/utils/json.c)继续跟踪，位置按本文相对路径解析。本地源码不自动等同于网页 latest 的版本；上述纠错另核对了本次读取的[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/utils/json.c)，摘要见[来源记录](../SOURCES.md)。

[JSON入门](P002_JSON序列化.md) · [接口参考](P006_JSON接口参考.md) · [头文件](P007_JSON头文件.md) · [源码浏览](P008_JSON头文件源码.md)。

<a id="header-groups"></a>
<a id="groups"></a>
<a id="r_jwt"></a>
<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a651dd91f092a66f0e718a637e0178401"></a>
<a id="agroup__sys-util_html_ga70c57aae3eb654e205459b4362c8089a"></a>
<a id="agroup__json_html_gga18a137ac5e2998d375540298670797c4a81e303d23da0b3d8504cc4a7ee7d52e8"></a>
<a id="agroup__sys-util_html_ga78c188c333605984c4c83f80d15092a4"></a>
<a id="agroup__sys-util_html_ga831cb8468911b8ebdb9b42682778e53d"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga18a137ac5e2998d375540298670797c4a926d6b0a5458be2e707d51f0b25dbe77"></a>
<a id="gga18a137ac5e2998d375540298670797c4a81e303d23da0b3d8504cc4a7ee7d52e8"></a>
<a id="gga18a137ac5e2998d375540298670797c4a835bc516b25eb0619b3f1a52f1ebc911"></a>
<a id="gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd"></a>
<a id="gga18a137ac5e2998d375540298670797c4a2483f21d814abcd08b5253e55aef70c9"></a>
<a id="gga18a137ac5e2998d375540298670797c4ab145f07a93c4fdcf60c9052fbd9a7afc"></a>
<a id="gga18a137ac5e2998d375540298670797c4a1434ca9f19f4a411ea98e02d8a2cac7f"></a>
<a id="gga18a137ac5e2998d375540298670797c4a4873e5c0c6344323d5d6af158952ca36"></a>
<a id="gga18a137ac5e2998d375540298670797c4a736325745f9521f38a68962775e76a50"></a>
<a id="gga18a137ac5e2998d375540298670797c4ae25f16ae591eb17d4074e6dcc2f1e62c"></a>
<a id="gga18a137ac5e2998d375540298670797c4aa842c96d114ed77ab66446bcac1424b5"></a>
<a id="gga18a137ac5e2998d375540298670797c4a94ef68b273a74244acb3bdec99b6a024"></a>
<a id="gga18a137ac5e2998d375540298670797c4a14739d9c36212d3df0007427b7b99e25"></a>
<a id="gga18a137ac5e2998d375540298670797c4af1e451cb321c805cff8fcde3561d3e64"></a>
<a id="gga18a137ac5e2998d375540298670797c4a37f98b21d196182fd2b8cd4c71ed607e"></a>
<a id="gga18a137ac5e2998d375540298670797c4a6218cd0d5d8a34cf4b32797f361b5a41"></a>
<a id="gga18a137ac5e2998d375540298670797c4aa5cf82525a71c8a9ca8c69c1adb0ff62"></a>
<a id="gga18a137ac5e2998d375540298670797c4a6e273425323ac63abad33f757572219b"></a>
<a id="gga18a137ac5e2998d375540298670797c4a7f49f406c8204e6d53353e26213d5169"></a>
<a id="gga18a137ac5e2998d375540298670797c4a15a20a35f875a495a7514ae1a7027e75"></a>
<a id="gga18a137ac5e2998d375540298670797c4a87ffb12e4d174bb4427d9a72eabca7e3"></a>
<a id="gga18a137ac5e2998d375540298670797c4a8df1b1d0061d7e289f94bae1df35baa7"></a>
<a id="gga18a137ac5e2998d375540298670797c4a651dd91f092a66f0e718a637e0178401"></a>
<a id="gga18a137ac5e2998d375540298670797c4a93de1b7e780ac22744c97e922de3b35e"></a>
<a id="gga18a137ac5e2998d375540298670797c4afe9c51f453d7dd02504071330a030e9e"></a>
<a id="gga18a137ac5e2998d375540298670797c4ad970b7d8553296bf4ed03c831cb6f604"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P005_Nanopb示例.md) · [返回大纲](大纲.md) · [下一章](P007_JSON头文件.md)
