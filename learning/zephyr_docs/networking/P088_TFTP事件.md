---
id: learning.zephyr-docs.networking.api-88
title: TFTP事件
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtftp__evt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第88章\_TFTP事件

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtftp__evt.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 88.1\_阅读说明与来源

译注：先读[TFTP客户端库](P077_TFTP客户端库.md)和[客户端示例](P078_TFTP客户端示例.md)，再按接口查询本组参考。

本组：[完整API参考](P084_TFTP完整API参考.md) · [头文件参考](P085_TFTP头文件参考.md) · [头文件源码](P086_TFTP头文件源码.md)。

定义通知给应用的TFTP异步事件（Asynchronous Event）。

```c
#include <zephyr/net/tftp.h>
```

定义通知给应用的TFTP异步事件（Asynchronous Event）。

## 88.2\_数据成员（Data Fields）

<a id="r_a2d622d9eb3ee0547b47a1330ad9cc412"></a>

```c
enum tftp_evt_type type
```

标识事件（Event）。

相关声明：[tftp_evt_type](P084_TFTP完整API参考.md#ga1ee3d814c6fbaf5570eb5fd9605af7ea)。

<a id="r_a37154f19c66ae09a200f4d8d6c2941ca"></a>

```c
union tftp_evt_param param
```

包含随事件传递的参数（如有）。

相关声明：[tftp_evt_param](P089_TFTP事件参数联合体.md)。

## 88.3\_详细说明（Detailed Documentation）

<a id="a37154f19c66ae09a200f4d8d6c2941ca"></a>

### `param`

```c
union tftp_evt_param tftp_evt::param
```

包含随事件传递的参数（如有）。

<a id="a2d622d9eb3ee0547b47a1330ad9cc412"></a>

### `type`

```c
enum tftp_evt_type tftp_evt::type
```

标识事件（Event）。

## 88.4\_相关头文件与源码

此页声明来自`<zephyr/net/tftp.h>`。本仓库的[对应头文件](../../../include/zephyr/net/tftp.h)可用于源码跟踪；本仓库版本可能与官网`latest`不同。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P087_TFTP客户端上下文.md) · [返回大纲](大纲.md) · [下一章](P089_TFTP事件参数联合体.md)
