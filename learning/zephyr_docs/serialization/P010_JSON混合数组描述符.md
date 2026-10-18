---
id: learning.zephyr-docs.serialization.page-10
title: JSON混合数组描述符
kind: reference
status: maintained
domains: [zephyr, serialization, development]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structjson__mixed__arr__descr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_JSON混合数组描述符

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structjson__mixed__arr__descr.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 10.1\_概述

混合类型 JSON 数组描述符（Mixed-type JSON Array Descriptor）。本结构描述一个顶层 JSON 数组，其中各元素可以是不同类型：基本类型、对象、数组或嵌套混合数组。每个数组元素由描述符数组中的一个条目描述。

混合数组适用于元素类型不一致的 JSON 数组的解析与编码，例如：

```json
[ "string", 42, { "foo": 1 }, [1,2,3], true ]
```

**原文注意（Note）**：此结构体及其关联宏用于混合数组解析与编码 API，见 [`json_mixed_arr_parse()`](P006_JSON接口参考.md)。

```c
#include <zephyr/data/json.h>
```

## 10.2\_结构声明（Structure Declaration）

以下按同批官方[源码浏览页](P008_JSON头文件源码.md)保留嵌套关系。

```c
struct json_mixed_arr_descr {
        uint32_t type : 7;
        size_t count_offset;

        union {
                struct {
                        size_t offset;
                        size_t size;
                } primitive;

                struct {
                        const struct json_obj_descr *sub_descr;
                        size_t sub_descr_len;
                        size_t offset;
                } object;

                struct {
                        const struct json_obj_descr *element_descr;
                        size_t n_elements;
                        size_t offset;
                } array;

                struct {
                        const struct json_mixed_arr_descr *sub_descr;
                        size_t sub_descr_len;
                        size_t offset;
                } mixed_array;
        };
};
```

译注：匿名联合体（Anonymous Union）中的各分支共用存储；同名字段属于各自嵌套分支，不能把扁平成员列表理解成全部同时独立存在。

## 10.3\_[union]

<a id="a2ddd49bd7a734a1d9402addfe6ffa46e"></a>
<a id="r_a2ddd49bd7a734a1d9402addfe6ffa46e"></a>

```c
union { ... } json_mixed_arr_descr
```


原页未提供额外的成员说明。

## 10.4\_[struct]

<a id="a3fa2bb6fa60dda662c11d273f6c26504"></a>

```c
struct { ... } json_mixed_arr_descr::array
```


原页未提供额外的成员说明。

## 10.5\_count\_offset

<a id="a5e0c419152731f1de5525448d1348b67"></a>
<a id="r_a5e0c419152731f1de5525448d1348b67"></a>

```c
size_t json_mixed_arr_descr::count_offset
```


原页未提供额外的成员说明。

## 10.6\_element\_descr

<a id="adde1179c855ca7e658389e6dcd5923a1"></a>

```c
const struct json_obj_descr* json_mixed_arr_descr::element_descr
```


原页未提供额外的成员说明。

## 10.7\_[struct]

<a id="ac8407e2ae891402cc17811f5230a43bb"></a>

```c
struct { ... } json_mixed_arr_descr::mixed_array
```


原页未提供额外的成员说明。

## 10.8\_n\_elements

<a id="a98f997d9e3ef4c1b4869b3be4a140875"></a>

```c
size_t json_mixed_arr_descr::n_elements
```


原页未提供额外的成员说明。

## 10.9\_[struct]

<a id="a7f3ae3b8861e2ff2ad2c3d1e9b625f94"></a>

```c
struct { ... } json_mixed_arr_descr::object
```


原页未提供额外的成员说明。

## 10.10\_offset

<a id="a87454dd52ecb62d2751b3705436a9603"></a>

```c
size_t json_mixed_arr_descr::offset
```


原页未提供额外的成员说明。

## 10.11\_[struct]

<a id="a0565129088b2a039a370db2779f327a8"></a>

```c
struct { ... } json_mixed_arr_descr::primitive
```


原页未提供额外的成员说明。

## 10.12\_size

<a id="a7d758504ef6b87a60468b1bf8e0aca41"></a>

```c
size_t json_mixed_arr_descr::size
```


原页未提供额外的成员说明。

## 10.13\_sub\_descr [1/2]

<a id="aac23b82933b11c01886a995625ce17de"></a>

```c
const struct json_mixed_arr_descr* json_mixed_arr_descr::sub_descr
```


原页未提供额外的成员说明。

## 10.14\_sub\_descr [2/2]

<a id="a3756bc3113f91e5acece578d37ad5409"></a>

```c
const struct json_obj_descr* json_mixed_arr_descr::sub_descr
```


原页未提供额外的成员说明。

## 10.15\_sub\_descr\_len

<a id="addaf657a20864a1a5040390720a084d7"></a>

```c
size_t json_mixed_arr_descr::sub_descr_len
```


原页未提供额外的成员说明。

## 10.16\_type

<a id="af27f330563f6bdf30f7c0a50992a9112"></a>
<a id="r_af27f330563f6bdf30f7c0a50992a9112"></a>

```c
uint32_t json_mixed_arr_descr::type
```


原页未提供额外的成员说明。

## 10.17\_源码对照与相关阅读

译注：可从本仓库的[JSON头文件](../../../include/zephyr/data/json.h)与[JSON实现](../../../lib/utils/json.c)继续跟踪，位置按本文相对路径解析。本地源码不自动等同于网页 latest 的版本；上述纠错另核对了本次读取的[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/utils/json.c)，摘要见[来源记录](../SOURCES.md)。

[JSON入门](P002_JSON序列化.md) · [接口参考](P006_JSON接口参考.md) · [头文件](P007_JSON头文件.md) · [源码浏览](P008_JSON头文件源码.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="r_a36726ab7a420f15cd57de89957f553ee"></a>
<a id="r_ad97e2ea89130de71ab6adbb65e4364e0"></a>
<a id="r_a95dc7bfc61780ac7f3b80ea25afb99a0"></a>
<a id="r_a00792eeb490c33eaf45c4841ea9d9adc"></a>
<a id="r_a77ab673975796506b5c74e6f1f27f5eb"></a>
<a id="r_aa5f463c1517324d776055228e1c5d930"></a>
<a id="r_a54c80405c0a457e8fda81440370af203"></a>
<a id="r_a1b54734ef0135e23cdadb40b4ffac70c"></a>
<a id="r_ae4f1c6883c7282e45436872946cec58f"></a>
<a id="r_a0aee22ea827aaf99906873167948cece"></a>
<a id="r_a02d6fe167bceb99099a69406628b97cf"></a>
<a id="r_aea47e729ed1214b211567b60109aff14"></a>
<a id="r_a6e29695e146d71feb716a5a4b00aff13"></a>
<a id="r_aae65bc8bfee7b3fa9639b8fc4cb64f08"></a>
<a id="r_abb7707a6feda03f9cceaf275380b70e4"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P009_JSON对象描述符.md) · [返回大纲](大纲.md) · [下一章](P011_JSON词法分析器.md)
