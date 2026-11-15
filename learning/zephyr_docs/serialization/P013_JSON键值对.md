---
id: learning.zephyr-docs.serialization.page-13
title: JSON键值对
kind: reference
status: maintained
domains: [zephyr, serialization, development]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structjson__obj__key__value.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_JSON键值对

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structjson__obj__key__value.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 13.1\_概述

JSON 对象中的一个顶层“`key`: `value`”成员。由 [`json_obj_next_key_value`](P006_JSON接口参考.md#ga9e3a815cae48a9825ff9904b97618ecb) 返回。键和值都是指向被解析载荷（Payload）内部的原始片段；值原样返回，不进行解码，其类型由 `value`.`type` 给出。

```c
#include <zephyr/data/json.h>
```

## 13.2\_结构声明（Structure Declaration）

以下按同批官方[源码浏览页](P008_JSON头文件源码.md)保留嵌套关系。

```c
struct json_obj_key_value {
        const char *key;
        size_t key_len;
        struct json_token value;
};
```

## 13.3\_key

<a id="aa902a4609788956586cdb29969c4d490"></a>
<a id="r_aa902a4609788956586cdb29969c4d490"></a>

```c
const char* json_obj_key_value::key
```

成员键文本，不以 `NUL` 终止；到达对象末尾时为 `NULL`。


## 13.4\_key\_len

<a id="a30594e48462592aa03b967b38bce0097"></a>
<a id="r_a30594e48462592aa03b967b38bce0097"></a>

```c
size_t json_obj_key_value::key_len
```

键文本的字节长度。


## 13.5\_value

<a id="a2f6ebba58df4fbeef182257031362179"></a>
<a id="r_a2f6ebba58df4fbeef182257031362179"></a>

```c
struct json_token json_obj_key_value::value
```

成员值，以原始词元片段（Raw Token Span）返回。


## 13.6\_源码对照与相关阅读

译注：可从本仓库的[JSON头文件](../../../include/zephyr/data/json.h)与[JSON实现](../../../lib/utils/json.c)继续跟踪，位置按本文相对路径解析。本地源码不自动等同于网页 latest 的版本；上述纠错另核对了本次读取的[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/utils/json.c)，摘要见[来源记录](../SOURCES.md)。

[JSON入门](P002_JSON序列化.md) · [接口参考](P006_JSON接口参考.md) · [头文件](P007_JSON头文件.md) · [源码浏览](P008_JSON头文件源码.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P012_JSON解析对象.md) · [返回大纲](大纲.md) · [下一章](P014_JSON对象词元.md)
