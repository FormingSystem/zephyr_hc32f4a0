---
id: learning.zephyr-docs.serialization.page-15
title: JSON词元
kind: reference
status: maintained
domains: [zephyr, serialization, development]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structjson__token.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_JSON词元

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structjson__token.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 15.1\_概述

JSON 词元（Token）结构体。原页仅提供成员声明，没有额外的成员说明。

```c
#include <zephyr/data/json.h>
```

## 15.2\_结构声明（Structure Declaration）

以下按同批官方[源码浏览页](P008_JSON头文件源码.md)保留嵌套关系。

```c
struct json_token {
        enum json_tokens type;
        char *start;
        char *end;
};
```

## 15.3\_end

<a id="abb55042d9343358e85311ea52cacb963"></a>
<a id="r_abb55042d9343358e85311ea52cacb963"></a>

```c
char* json_token::end
```


原页未提供额外的成员说明。

## 15.4\_start

<a id="a606e33f699c3ec5a66f450cc1777b3c2"></a>
<a id="r_a606e33f699c3ec5a66f450cc1777b3c2"></a>

```c
char* json_token::start
```


原页未提供额外的成员说明。

## 15.5\_type

<a id="ab163615cc3a39191d5a48e900c579e94"></a>
<a id="r_ab163615cc3a39191d5a48e900c579e94"></a>

```c
enum json_tokens json_token::type
```


原页未提供额外的成员说明。

## 15.6\_源码对照与相关阅读

译注：可从本仓库的[JSON头文件](../../../include/zephyr/data/json.h)与[JSON实现](../../../lib/utils/json.c)继续跟踪，位置按本文相对路径解析。本地源码不自动等同于网页 latest 的版本；上述纠错另核对了本次读取的[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/utils/json.c)，摘要见[来源记录](../SOURCES.md)。

[JSON入门](P002_JSON序列化.md) · [接口参考](P006_JSON接口参考.md) · [头文件](P007_JSON头文件.md) · [源码浏览](P008_JSON头文件源码.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P014_JSON对象词元.md) · [返回大纲](大纲.md)
