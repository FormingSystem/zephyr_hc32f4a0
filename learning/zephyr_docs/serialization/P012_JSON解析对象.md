---
id: learning.zephyr-docs.serialization.page-12
title: JSON解析对象
kind: reference
status: maintained
domains: [zephyr, serialization, development]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structjson__obj.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_JSON解析对象

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structjson__obj.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 12.1\_概述

JSON 解析对象（Parser Object）结构体。原页仅提供成员声明，没有额外的成员说明。

```c
#include <zephyr/data/json.h>
```

## 12.2\_结构声明（Structure Declaration）

以下按同批官方[源码浏览页](P008_JSON头文件源码.md)保留嵌套关系。

```c
struct json_obj {
        struct json_lexer lex;
};
```

## 12.3\_lex

<a id="a7a48a2dca53ee74e7c8eb4727af0e33a"></a>
<a id="r_a7a48a2dca53ee74e7c8eb4727af0e33a"></a>

```c
struct json_lexer json_obj::lex
```


原页未提供额外的成员说明。

## 12.4\_源码对照与相关阅读

译注：可从本仓库的[JSON头文件](../../../include/zephyr/data/json.h)与[JSON实现](../../../lib/utils/json.c)继续跟踪，位置按本文相对路径解析。本地源码不自动等同于网页 latest 的版本；上述纠错另核对了本次读取的[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/utils/json.c)，摘要见[来源记录](../SOURCES.md)。

[JSON入门](P002_JSON序列化.md) · [接口参考](P006_JSON接口参考.md) · [头文件](P007_JSON头文件.md) · [源码浏览](P008_JSON头文件源码.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P011_JSON词法分析器.md) · [返回大纲](大纲.md) · [下一章](P013_JSON键值对.md)
