---
id: learning.zephyr-docs.serialization.page-9
title: JSON对象描述符
kind: reference
status: maintained
domains: [zephyr, serialization, development]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structjson__obj__descr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_JSON对象描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structjson__obj__descr.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 9.1\_概述

JSON 对象描述符（Object Descriptor）。原页提供声明与成员列表，没有额外文字解释；下方保留全部结构和位域宽度（Bit-field Width）。

```c
#include <zephyr/data/json.h>
```

## 9.2\_结构声明（Structure Declaration）

以下按同批官方[源码浏览页](P008_JSON头文件源码.md)保留嵌套关系。

```c
struct json_obj_descr {
        const char *field_name;

        /* Alignment can be 1, 2, 4, or 8.  The macros to create
         * a struct json_obj_descr will store the alignment's
         * power of 2 in order to keep this value in the 0-3 range
         * and thus use only 2 bits.
         */
        uint32_t align_shift : 2;

        /* 127 characters is more than enough for a field name. */
        uint32_t field_name_len : 7;

        /* Valid values here (enum json_tokens): JSON_TOK_STRING,
         * JSON_TOK_NUMBER, JSON_TOK_TRUE, JSON_TOK_FALSE,
         * JSON_TOK_OBJECT_START, JSON_TOK_ARRAY_START.  (All others
         * ignored.) Maximum value is '}' (125), so this has to be 7 bits
         * long.
         */
        uint32_t type : 7;

        /* 65535 bytes is more than enough for many JSON payloads. */
        uint32_t offset : 16;

        union {
                struct {
                        const struct json_obj_descr *sub_descr;
                        size_t sub_descr_len;
                } object;
                struct {
                        const struct json_obj_descr *element_descr;
                        size_t n_elements;
                } array;
                struct {
                        size_t size;
                } field;
        };
};
```

译注：匿名联合体（Anonymous Union）中的各分支共用存储；同名字段属于各自嵌套分支，不能把扁平成员列表理解成全部同时独立存在。

## 9.3\_[union]

<a id="ab3fcd26cb6bbca104db63560c310ea8c"></a>
<a id="r_ab3fcd26cb6bbca104db63560c310ea8c"></a>

```c
union { ... } json_obj_descr
```


原页未提供额外的成员说明。

## 9.4\_align\_shift

<a id="a475717ac4dd01296c01468450e50f75b"></a>
<a id="r_a475717ac4dd01296c01468450e50f75b"></a>

```c
uint32_t json_obj_descr::align_shift
```


原页未提供额外的成员说明。

## 9.5\_[struct]

<a id="ac12783b89f5507bef7fa3da2c56d1d61"></a>

```c
struct { ... } json_obj_descr::array
```


原页未提供额外的成员说明。

## 9.6\_element\_descr

<a id="a0a459bf5ad8a210395fe80c5edd72d93"></a>

```c
const struct json_obj_descr* json_obj_descr::element_descr
```


原页未提供额外的成员说明。

## 9.7\_[struct]

<a id="a0449d269cff7813f37066f0381b9e8f5"></a>

```c
struct { ... } json_obj_descr::field
```


原页未提供额外的成员说明。

## 9.8\_field\_name

<a id="a2120b7752253ece0beddcaf4c57d3ed8"></a>
<a id="r_a2120b7752253ece0beddcaf4c57d3ed8"></a>

```c
const char* json_obj_descr::field_name
```


原页未提供额外的成员说明。

## 9.9\_field\_name\_len

<a id="a602bf4d8bb5d47c8edb40963ea8ba42f"></a>
<a id="r_a602bf4d8bb5d47c8edb40963ea8ba42f"></a>

```c
uint32_t json_obj_descr::field_name_len
```


原页未提供额外的成员说明。

## 9.10\_n\_elements

<a id="ace6558c5156a76658d8835fd5e65ee52"></a>

```c
size_t json_obj_descr::n_elements
```


原页未提供额外的成员说明。

## 9.11\_[struct]

<a id="a5d5df7aab020feb3eeb59a7f6089b066"></a>

```c
struct { ... } json_obj_descr::object
```


原页未提供额外的成员说明。

## 9.12\_offset

<a id="a8c6f3eae5e678b8b8ef1957c46f488f1"></a>
<a id="r_a8c6f3eae5e678b8b8ef1957c46f488f1"></a>

```c
uint32_t json_obj_descr::offset
```


原页未提供额外的成员说明。

## 9.13\_size

<a id="aa01763bb5316fdce6acc64c7d7d21406"></a>

```c
size_t json_obj_descr::size
```


原页未提供额外的成员说明。

## 9.14\_sub\_descr

<a id="a4f5e97c654d0c5e21f1efb5a01966e56"></a>

```c
const struct json_obj_descr* json_obj_descr::sub_descr
```


原页未提供额外的成员说明。

## 9.15\_sub\_descr\_len

<a id="adea0b44d1552305df9dce70074044ba1"></a>

```c
size_t json_obj_descr::sub_descr_len
```


原页未提供额外的成员说明。

## 9.16\_type

<a id="a975e998d3ec36f234f09aa2d0d116c9c"></a>
<a id="r_a975e998d3ec36f234f09aa2d0d116c9c"></a>

```c
uint32_t json_obj_descr::type
```


原页未提供额外的成员说明。

## 9.17\_源码对照与相关阅读

译注：可从本仓库的[JSON头文件](../../../include/zephyr/data/json.h)与[JSON实现](../../../lib/utils/json.c)继续跟踪，位置按本文相对路径解析。本地源码不自动等同于网页 latest 的版本；上述纠错另核对了本次读取的[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/utils/json.c)，摘要见[来源记录](../SOURCES.md)。

[JSON入门](P002_JSON序列化.md) · [接口参考](P006_JSON接口参考.md) · [头文件](P007_JSON头文件.md) · [源码浏览](P008_JSON头文件源码.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="r_a7c7fbd4bfc136cf048822e5f03855b9c"></a>
<a id="r_a6ad34e2ea14bfb2bf8a9cff2cc45416f"></a>
<a id="r_a92f678d2595846142f9d8396e581445e"></a>
<a id="r_a4864a984d89e0a5c8d262435ff018b4b"></a>
<a id="r_adab8f6c4e550341e73cf5125c96b0ce2"></a>
<a id="r_a6197e7f08fc96a4c1e0a26f2eb1a2dba"></a>
<a id="r_a5ba7869122aa317c1feca9066457b8ed"></a>
<a id="r_a083ef4e4a5040a0ae3481d79d0b3ae12"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P008_JSON头文件源码.md) · [返回大纲](大纲.md) · [下一章](P010_JSON混合数组描述符.md)
