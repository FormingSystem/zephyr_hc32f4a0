---
id: learning.zephyr-docs.networking.api-89
title: TFTP事件参数联合体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uniontftp__evt__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第89章\_TFTP事件参数联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/uniontftp__evt__param.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 89.1\_阅读说明与来源

译注：先读[TFTP客户端库](P077_TFTP客户端库.md)和[客户端示例](P078_TFTP客户端示例.md)，再按接口查询本组参考。

本组：[完整API参考](P084_TFTP完整API参考.md) · [头文件参考](P085_TFTP头文件参考.md) · [头文件源码](P086_TFTP头文件源码.md)。

定义伴随异步事件一起通知给应用的事件参数（Event Parameters）。

```c
#include <zephyr/net/tftp.h>
```

定义伴随异步事件一起通知给应用的事件参数（Event Parameters）。

## 89.2\_数据成员（Data Fields）

<a id="r_a7bec7cd5512f25699fe6b733458e9128"></a>

```c
struct tftp_data_param data
```

随`TFTP_EVT_DATA`事件传递的参数。

相关声明：[tftp_data_param](P090_TFTP数据参数.md)。

<a id="r_a489485b84fa3e559b3065258cabfb205"></a>

```c
struct tftp_error_param error
```

随`TFTP_EVT_ERROR`事件传递的参数。

相关声明：[tftp_error_param](P091_TFTP错误参数.md)。

## 89.3\_详细说明（Detailed Documentation）

<a id="a7bec7cd5512f25699fe6b733458e9128"></a>

### `data`

```c
struct tftp_data_param tftp_evt_param::data
```

随`TFTP_EVT_DATA`事件传递的参数。

<a id="a489485b84fa3e559b3065258cabfb205"></a>

### `error`

```c
struct tftp_error_param tftp_evt_param::error
```

随`TFTP_EVT_ERROR`事件传递的参数。

## 89.4\_相关头文件与源码

此页声明来自`<zephyr/net/tftp.h>`。本仓库的[对应头文件](../../../include/zephyr/net/tftp.h)可用于源码跟踪；本仓库版本可能与官网`latest`不同。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P088_TFTP事件.md) · [返回大纲](大纲.md) · [下一章](P090_TFTP数据参数.md)
