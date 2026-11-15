---
id: learning.zephyr-docs.serialization.page-14
title: JSON对象词元
kind: reference
status: maintained
domains: [zephyr, serialization, development]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structjson__obj__token.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_JSON对象词元

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structjson__obj__token.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 14.1\_概述

JSON 对象词元（Object Token）结构体。原页仅提供成员声明，没有额外的成员说明。

```c
#include <zephyr/data/json.h>
```

## 14.2\_结构声明（Structure Declaration）

以下按同批官方[源码浏览页](P008_JSON头文件源码.md)保留嵌套关系。

```c
struct json_obj_token {
        char *start;
        size_t length;
};
```

## 14.3\_length

<a id="ac996ab0b850803998a37025b57051144"></a>
<a id="r_ac996ab0b850803998a37025b57051144"></a>

```c
size_t json_obj_token::length
```


原页未提供额外的成员说明。

## 14.4\_start

<a id="aef14abe1f0cefda6bd89d058787550b1"></a>
<a id="r_aef14abe1f0cefda6bd89d058787550b1"></a>

```c
char* json_obj_token::start
```


原页未提供额外的成员说明。

## 14.5\_源码对照与相关阅读

译注：可从本仓库的[JSON头文件](../../../include/zephyr/data/json.h)与[JSON实现](../../../lib/utils/json.c)继续跟踪，位置按本文相对路径解析。本地源码不自动等同于网页 latest 的版本；上述纠错另核对了本次读取的[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/utils/json.c)，摘要见[来源记录](../SOURCES.md)。

[JSON入门](P002_JSON序列化.md) · [接口参考](P006_JSON接口参考.md) · [头文件](P007_JSON头文件.md) · [源码浏览](P008_JSON头文件源码.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P013_JSON键值对.md) · [返回大纲](大纲.md) · [下一章](P015_JSON词元.md)
