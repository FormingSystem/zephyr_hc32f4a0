---
id: learning.zephyr-docs.serialization.page-7
title: JSON头文件
kind: reference
status: maintained
domains: [zephyr, serialization, development]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/json_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_JSON头文件

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/json_8h.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 7.1\_概述

本页列出 JSON 头文件的公开声明、宏、词元类型与函数入口；参数和返回说明见[完整JSON接口](P006_JSON接口参考.md)。

```c
#include <zephyr/sys/util.h>
#include <stddef.h>
#include <zephyr/toolchain.h>
#include <zephyr/types.h>
#include <sys/types.h>
```

## 7.2\_关联声明与说明

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

## 7.3\_关联声明与说明

<a id="r_ga1ed917f5a247ca33f2778afe62ff1a88"></a>

```c
#define JSON_OBJ_DESCR_PRIM(struct_, field_name_, type_)
```

用于为受支持的基本类型值声明描述符的辅助宏。

[详细说明](P006_JSON接口参考.md#ga1ed917f5a247ca33f2778afe62ff1a88)。

<a id="r_ga4ee365f43cfa86a214973defe81f1e88"></a>

```c
#define JSON_OBJ_DESCR_OBJECT(struct_, field_name_, sub_descr_)
```

用于为对象值声明描述符的辅助宏。

[详细说明](P006_JSON接口参考.md#ga4ee365f43cfa86a214973defe81f1e88)。

<a id="r_ga0b510decbc755c82903b54fcbc4a3b64"></a>

```c
#define JSON_OBJ_DESCR_ARRAY(struct_, field_name_, max_len_, len_field_, elem_type_)
```

用于为基本类型数组声明描述符的辅助宏。

[详细说明](P006_JSON接口参考.md#ga0b510decbc755c82903b54fcbc4a3b64)。

<a id="r_gae012264df03546a1c01eec4216b52ffd"></a>

```c
#define JSON_OBJ_DESCR_OBJ_ARRAY(struct_, field_name_, max_len_, len_field_, elem_descr_, elem_descr_len_)
```

用于为对象数组（Array of Objects）声明描述符的辅助宏。

[详细说明](P006_JSON接口参考.md#gae012264df03546a1c01eec4216b52ffd)。

<a id="r_gaed8189235fd30d2bc041cafee9591ec9"></a>

```c
#define JSON_OBJ_DESCR_ARRAY_ARRAY(struct_, field_name_, max_len_, len_field_, elem_descr_, elem_descr_len_)
```

用于为数组组成的数组（Array of Arrays）声明描述符的辅助宏。

[详细说明](P006_JSON接口参考.md#gaed8189235fd30d2bc041cafee9591ec9)。

<a id="r_ga9fea9111ac1024c8feb066cd53a4045b"></a>

```c
#define JSON_OBJ_DESCR_ARRAY_ARRAY_NAMED(struct_, json_field_name_, struct_field_name_, max_len_, len_field_, elem_descr_, elem_descr_len_)
```

[`JSON_OBJ_DESCR_ARRAY_ARRAY`](P006_JSON接口参考.md#gaed8189235fd30d2bc041cafee9591ec9) 的变体，适用于结构体字段名与 JSON 字段名不同的情况。

[详细说明](P006_JSON接口参考.md#ga9fea9111ac1024c8feb066cd53a4045b)。

<a id="r_gaad081c4f8debcb41779bd5879ed8bbd4"></a>

```c
#define JSON_OBJ_DESCR_PRIM_NAMED(struct_, json_field_name_, struct_field_name_, type_)
```

[`JSON_OBJ_DESCR_PRIM`](P006_JSON接口参考.md#ga1ed917f5a247ca33f2778afe62ff1a88) 的变体，适用于结构体字段名与 JSON 字段名不同的情况。

[详细说明](P006_JSON接口参考.md#gaad081c4f8debcb41779bd5879ed8bbd4)。

<a id="r_ga8f8d03241e4f69d5f7147792db9a9fe9"></a>

```c
#define JSON_OBJ_DESCR_OBJECT_NAMED(struct_, json_field_name_, struct_field_name_, sub_descr_)
```

[`JSON_OBJ_DESCR_OBJECT`](P006_JSON接口参考.md#ga4ee365f43cfa86a214973defe81f1e88) 的变体，适用于结构体字段名与 JSON 字段名不同的情况。

[详细说明](P006_JSON接口参考.md#ga8f8d03241e4f69d5f7147792db9a9fe9)。

<a id="r_ga4a5bafd64de8abcbc2b5c039bd59ec84"></a>

```c
#define JSON_OBJ_DESCR_ARRAY_NAMED(struct_, json_field_name_, struct_field_name_, max_len_, len_field_, elem_type_)
```

[`JSON_OBJ_DESCR_ARRAY`](P006_JSON接口参考.md#ga0b510decbc755c82903b54fcbc4a3b64) 的变体，适用于结构体字段名与 JSON 字段名不同的情况。

[详细说明](P006_JSON接口参考.md#ga4a5bafd64de8abcbc2b5c039bd59ec84)。

<a id="r_gaa6602833e59c7e5205d69cc7c4ab2bba"></a>

```c
#define JSON_OBJ_DESCR_OBJ_ARRAY_NAMED(struct_, json_field_name_, struct_field_name_, max_len_, len_field_, elem_descr_, elem_descr_len_)
```

[`JSON_OBJ_DESCR_OBJ_ARRAY`](P006_JSON接口参考.md#gae012264df03546a1c01eec4216b52ffd) 的变体，适用于结构体字段名与 JSON 字段名不同的情况。

[详细说明](P006_JSON接口参考.md#gaa6602833e59c7e5205d69cc7c4ab2bba)。

<a id="r_ga6eecf3f2cda73f7fe4fac37859ce3f77"></a>

```c
#define JSON_MIXED_ARR_DESCR_PRIM(struct_, field_name_, type_, count_field_)
```

用于声明混合数组中基本类型元素描述符（Primitive Element Descriptor）的辅助宏。

[详细说明](P006_JSON接口参考.md#ga6eecf3f2cda73f7fe4fac37859ce3f77)。

<a id="r_ga705b4980a865683c3b4df4dc0f4d6e28"></a>

```c
#define JSON_MIXED_ARR_DESCR_OBJECT(struct_, field_name_, sub_descr_, count_field_)
```

用于声明混合数组中对象元素描述符（Object Element Descriptor）的辅助宏。

[详细说明](P006_JSON接口参考.md#ga705b4980a865683c3b4df4dc0f4d6e28)。

<a id="r_ga38f87b83b1c5ef7da5b18a3066938b58"></a>

```c
#define JSON_MIXED_ARR_DESCR_ARRAY(struct_, field_name_, max_len_, elem_descr_, count_field_)
```

用于声明混合数组中同类型数组元素描述符（Homogeneous Array Element Descriptor）的辅助宏。

[详细说明](P006_JSON接口参考.md#ga38f87b83b1c5ef7da5b18a3066938b58)。

<a id="r_ga2b9d36bc7ff682f8d7236183818ff005"></a>

```c
#define JSON_MIXED_ARR_DESCR_MIXED_ARRAY(struct_, field_name_, sub_descr_, count_field_)
```

用于声明嵌套混合数组元素描述符（Nested Mixed Array Element Descriptor）的辅助宏。

[详细说明](P006_JSON接口参考.md#ga2b9d36bc7ff682f8d7236183818ff005)。

## 7.4\_关联声明与说明

<a id="r_gacb409ebe9c59789a5d9aca02c6c94674"></a>

```c
typedef int(* json_append_bytes_t) (const char *bytes, size_t len, void *data)
```

编码 JSON 数据时用于向缓冲区追加字节的函数指针类型（Function Pointer Type）。

[详细说明](P006_JSON接口参考.md#gacb409ebe9c59789a5d9aca02c6c94674)。

## 7.5\_关联声明与说明

<a id="r_ga18a137ac5e2998d375540298670797c4"></a>

```c
enum json_tokens { JSON_TOK_NONE = '_' , JSON_TOK_OBJECT_START = '{' , JSON_TOK_OBJECT_END = '}' , JSON_TOK_ARRAY_START = '[' , JSON_TOK_ARRAY_END = ']' , JSON_TOK_STRING = '"' , JSON_TOK_STRING_BUF = 's' , JSON_TOK_COLON = ':' , JSON_TOK_COMMA = ',' , JSON_TOK_NUMBER = '0' , JSON_TOK_FLOAT = '1' , JSON_TOK_OPAQUE = '2' , JSON_TOK_OBJ_ARRAY = '3' , JSON_TOK_ENCODED_OBJ = '4' , JSON_TOK_INT64 = '5' , JSON_TOK_UINT64 = '6' , JSON_TOK_FLOAT_FP = '7' , JSON_TOK_DOUBLE_FP = '8' , JSON_TOK_INT = 'i' , JSON_TOK_UINT = 'u' , JSON_TOK_TRUE = 't' , JSON_TOK_FALSE = 'f' , JSON_TOK_MIXED_ARRAY = 'm' , JSON_TOK_NULL = 'n' , JSON_TOK_ERROR = '!' , JSON_TOK_EOF = '\0' }
```

[详细说明](P006_JSON接口参考.md#ga18a137ac5e2998d375540298670797c4)。

## 7.6\_关联声明与说明

<a id="r_ga73997fa2154fcbc80f37edd7bcf3477a"></a>

```c
int64_t json_obj_parse (char *json, size_t len, const struct json_obj_descr *descr, size_t descr_len, void *val)
```

按照 `descr` 所指向的描述符，解析 `json` 所指向、长度为 `len` 的 JSON 编码对象。

[详细说明](P006_JSON接口参考.md#ga73997fa2154fcbc80f37edd7bcf3477a)。

<a id="r_gab4e6ad4a040c271d74eaa313c580a739"></a>

```c
int json_arr_parse (char *json, size_t len, const struct json_obj_descr *descr, void *val)
```

按照 `descr` 所指向的描述符，解析 `json` 所指向、长度为 `len` 的 JSON 编码数组。

[详细说明](P006_JSON接口参考.md#gab4e6ad4a040c271d74eaa313c580a739)。

<a id="r_ga6196411958e2e9b3683af4c281214b92"></a>

```c
int json_arr_separate_object_parse_init (struct json_obj *json, char *payload, size_t len)
```

初始化按单个对象处理数组的解析过程。

[详细说明](P006_JSON接口参考.md#ga6196411958e2e9b3683af4c281214b92)。

<a id="r_ga64859a835e7cb88c2499360fb00ca344"></a>

```c
int json_arr_separate_parse_object (struct json_obj *json, const struct json_obj_descr *descr, size_t descr_len, void *val)
```

从数组中解析单个对象。

[详细说明](P006_JSON接口参考.md#ga64859a835e7cb88c2499360fb00ca344)。

<a id="r_gaeef63343b8b15edc3ee96028332bfb39"></a>

```c
int json_obj_separate_parse_init (struct json_obj *json, char *payload, size_t len)
```

初始化 JSON 对象成员的增量解析（Incremental Parsing）。

[详细说明](P006_JSON接口参考.md#gaeef63343b8b15edc3ee96028332bfb39)。

<a id="r_ga9e3a815cae48a9825ff9904b97618ecb"></a>

```c
int json_obj_next_key_value (struct json_obj *json, struct json_obj_key_value *kv)
```

返回 JSON 对象的下一个顶层成员（Top-level Member）。

[详细说明](P006_JSON接口参考.md#ga9e3a815cae48a9825ff9904b97618ecb)。

<a id="r_ga43ee6d1fbd3fa8fb2ae052844b465dda"></a>

```c
ssize_t json_escape (char *str, size_t *len, size_t buf_size)
```

转义字符串，使其可用于编码 JSON 对象。

[详细说明](P006_JSON接口参考.md#ga43ee6d1fbd3fa8fb2ae052844b465dda)。

<a id="r_ga5ef155a3a6444801592badd6a092734c"></a>

```c
size_t json_calc_escaped_len (const char *str, size_t len)
```

计算经 JSON 转义（Escaping）后的字符串长度。

[详细说明](P006_JSON接口参考.md#ga5ef155a3a6444801592badd6a092734c)。

<a id="r_ga41e6e90beef8bae12fca1de2584145bb"></a>

```c
ssize_t json_calc_encoded_len (const struct json_obj_descr *descr, size_t descr_len, const void *val)
```

计算完整编码对象所需的字符串长度。

[详细说明](P006_JSON接口参考.md#ga41e6e90beef8bae12fca1de2584145bb)。

<a id="r_gad612b8441a21dca34cfeec6257877509"></a>

```c
ssize_t json_calc_encoded_arr_len (const struct json_obj_descr *descr, const void *val)
```

计算完整编码数组所需的字符串长度。

[详细说明](P006_JSON接口参考.md#gad612b8441a21dca34cfeec6257877509)。

<a id="r_gab758ad32cfb6369f4967a6842ac63245"></a>

```c
int json_obj_encode_buf (const struct json_obj_descr *descr, size_t descr_len, const void *val, char *buffer, size_t buf_size)
```

在连续内存位置中编码对象。

[详细说明](P006_JSON接口参考.md#gab758ad32cfb6369f4967a6842ac63245)。

<a id="r_gafd27bbcb898dc902cf1dadd3369cf923"></a>

```c
int json_arr_encode_buf (const struct json_obj_descr *descr, const void *val, char *buffer, size_t buf_size)
```

在连续内存位置中编码数组。

[详细说明](P006_JSON接口参考.md#gafd27bbcb898dc902cf1dadd3369cf923)。

<a id="r_gafec772f687a0280f5211139bd019e582"></a>

```c
int json_obj_encode (const struct json_obj_descr *descr, size_t descr_len, const void *val, json_append_bytes_t append_bytes, void *data)
```

使用任意写出函数编码对象。

[详细说明](P006_JSON接口参考.md#gafec772f687a0280f5211139bd019e582)。

<a id="r_ga4ffccdc602ab98d489499bf6fa4fa6c5"></a>

```c
int json_arr_encode (const struct json_obj_descr *descr, const void *val, json_append_bytes_t append_bytes, void *data)
```

使用任意写出函数（Writer Function）编码数组。

[详细说明](P006_JSON接口参考.md#ga4ffccdc602ab98d489499bf6fa4fa6c5)。

<a id="r_ga4348a45b1a45a271e3d62a0c5a4d9c0d"></a>

```c
int json_mixed_arr_parse (char *json, size_t len, const struct json_mixed_arr_descr *descr, size_t descr_len, void *val)
```

将 JSON 混合数组解析到 C 结构体中。

[详细说明](P006_JSON接口参考.md#ga4348a45b1a45a271e3d62a0c5a4d9c0d)。

<a id="r_ga210433173e35241dea8976bd7f532570"></a>

```c
int json_mixed_arr_encode (const struct json_mixed_arr_descr *descr, size_t descr_len, void *val, json_append_bytes_t append_bytes, void *data)
```

将 C 结构体编码为 JSON 混合数组。

[详细说明](P006_JSON接口参考.md#ga210433173e35241dea8976bd7f532570)。

<a id="r_ga51565a7e00a520d1257a0b6a91058a3d"></a>

```c
int json_mixed_arr_encode_buf (const struct json_mixed_arr_descr *descr, size_t descr_len, void *val, char *buffer, size_t buf_size)
```

将 C 结构体编码为 JSON 混合数组并写入缓冲区。

[详细说明](P006_JSON接口参考.md#ga51565a7e00a520d1257a0b6a91058a3d)。

<a id="r_ga20efb9b01733fadd8086dcab8be2ca85"></a>

```c
ssize_t json_calc_mixed_arr_len (const struct json_mixed_arr_descr *descr, size_t descr_len, void *val)
```

计算编码后的 JSON 混合数组（Mixed Array）的长度。

[详细说明](P006_JSON接口参考.md#ga20efb9b01733fadd8086dcab8be2ca85)。

## 7.7\_源码对照与相关阅读

译注：可从本仓库的[JSON头文件](../../../include/zephyr/data/json.h)与[JSON实现](../../../lib/utils/json.c)继续跟踪，位置按本文相对路径解析。本地源码不自动等同于网页 latest 的版本；上述纠错另核对了本次读取的[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/utils/json.c)，摘要见[来源记录](../SOURCES.md)。

[JSON入门](P002_JSON序列化.md) · [接口参考](P006_JSON接口参考.md) · [头文件](P007_JSON头文件.md) · [源码浏览](P008_JSON头文件源码.md)。

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

[上一章](P006_JSON接口参考.md) · [返回大纲](大纲.md) · [下一章](P008_JSON头文件源码.md)
