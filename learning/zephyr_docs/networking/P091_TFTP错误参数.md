---
id: learning.zephyr-docs.networking.api-91
title: TFTP错误参数
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtftp__error__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第91章\_TFTP错误参数

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtftp__error__param.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 91.1\_阅读说明与来源

译注：先读[TFTP客户端库](P077_TFTP客户端库.md)和[客户端示例](P078_TFTP客户端示例.md)，再按接口查询本组参考。

本组：[完整API参考](P084_TFTP完整API参考.md) · [头文件参考](P085_TFTP头文件参考.md) · [头文件源码](P086_TFTP头文件源码.md)。

错误事件参数（Error Event Parameters）。

```c
#include <zephyr/net/tftp.h>
```

错误事件参数（Error Event Parameters）。

## 91.2\_数据成员（Data Fields）

<a id="r_a725f1d2b8b8848febacf4888a0b55611"></a>

```c
char * msg
```

错误消息（Error Message）。

<a id="r_aa8766ec6c9e92c9383b0dbbafe8a0f43"></a>

```c
int code
```

错误码（Error Code）。

## 91.3\_详细说明（Detailed Documentation）

<a id="aa8766ec6c9e92c9383b0dbbafe8a0f43"></a>

### `code`

```c
int tftp_error_param::code
```

错误码（Error Code）。

<a id="a725f1d2b8b8848febacf4888a0b55611"></a>

### `msg`

```c
char* tftp_error_param::msg
```

错误消息（Error Message）。

字符串在`tftp_buf`内以空字符（NUL）终止，最多包含`TFTP_BLOCK_SIZE - 1`个字符。

## 91.4\_相关头文件与源码

此页声明来自`<zephyr/net/tftp.h>`。本仓库的[对应头文件](../../../include/zephyr/net/tftp.h)可用于源码跟踪；本仓库版本可能与官网`latest`不同。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P090_TFTP数据参数.md) · [返回大纲](大纲.md) · [下一章](P092_网络Shell.md)
