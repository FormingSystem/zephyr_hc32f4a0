---
id: learning.zephyr-docs.serialization.page-11
title: JSON词法分析器
kind: reference
status: maintained
domains: [zephyr, serialization, development]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structjson__lexer.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_JSON词法分析器

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structjson__lexer.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 11.1\_概述

JSON 词法分析器（Lexer）结构体。原页仅提供成员声明，没有额外的成员说明。

```c
#include <zephyr/data/json.h>
```

## 11.2\_结构声明（Structure Declaration）

以下按同批官方[源码浏览页](P008_JSON头文件源码.md)保留嵌套关系。

```c
struct json_lexer {
        void *(*state)(struct json_lexer *lex);
        char *start;
        char *pos;
        char *end;
        struct json_token tok;
};
```

## 11.3\_end

<a id="aeaf5743a9285e0aef9df99f9b3b48320"></a>
<a id="r_aeaf5743a9285e0aef9df99f9b3b48320"></a>

```c
char* json_lexer::end
```


原页未提供额外的成员说明。

## 11.4\_pos

<a id="a9b403c5505e9a2cd9e475416b2e7f0ac"></a>
<a id="r_a9b403c5505e9a2cd9e475416b2e7f0ac"></a>

```c
char* json_lexer::pos
```


原页未提供额外的成员说明。

## 11.5\_start

<a id="aa4d4a29301fb840c691bbfa416474de4"></a>
<a id="r_aa4d4a29301fb840c691bbfa416474de4"></a>

```c
char* json_lexer::start
```


原页未提供额外的成员说明。

## 11.6\_state

<a id="ae74beb9d896daf102ec5ffff370830b3"></a>
<a id="r_ae74beb9d896daf102ec5ffff370830b3"></a>

```c
void *(* json_lexer::state) (struct json_lexer *lex)
```


原页未提供额外的成员说明。

## 11.7\_tok

<a id="ab285bc72bf12a4de31b45ac0fc992620"></a>
<a id="r_ab285bc72bf12a4de31b45ac0fc992620"></a>

```c
struct json_token json_lexer::tok
```


原页未提供额外的成员说明。

## 11.8\_源码对照与相关阅读

译注：可从本仓库的[JSON头文件](../../../include/zephyr/data/json.h)与[JSON实现](../../../lib/utils/json.c)继续跟踪，位置按本文相对路径解析。本地源码不自动等同于网页 latest 的版本；上述纠错另核对了本次读取的[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/utils/json.c)，摘要见[来源记录](../SOURCES.md)。

[JSON入门](P002_JSON序列化.md) · [接口参考](P006_JSON接口参考.md) · [头文件](P007_JSON头文件.md) · [源码浏览](P008_JSON头文件源码.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P010_JSON混合数组描述符.md) · [返回大纲](大纲.md) · [下一章](P012_JSON解析对象.md)
