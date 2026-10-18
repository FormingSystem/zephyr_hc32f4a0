---
id: learning.zephyr-docs.networking.api-90
title: TFTP数据参数
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtftp__data__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第90章\_TFTP数据参数

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtftp__data__param.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 90.1\_阅读说明与来源

译注：先读[TFTP客户端库](P077_TFTP客户端库.md)和[客户端示例](P078_TFTP客户端示例.md)，再按接口查询本组参考。

本组：[完整API参考](P084_TFTP完整API参考.md) · [头文件参考](P085_TFTP头文件参考.md) · [头文件源码](P086_TFTP头文件源码.md)。

数据事件参数（Data Event Parameters）。

```c
#include <zephyr/net/tftp.h>
```

数据事件参数（Data Event Parameters）。

## 90.2\_数据成员（Data Fields）

<a id="r_a93f666944e8f20bd3a0e1320452913db"></a>

```c
uint8_t * data_ptr
```

指向二进制数据（Binary Data）的指针。

<a id="r_a704c20ab3177a3d53df21fc9ef64d084"></a>

```c
uint32_t len
```

二进制数据的长度。

## 90.3\_详细说明（Detailed Documentation）

<a id="a93f666944e8f20bd3a0e1320452913db"></a>

### `data_ptr`

```c
uint8_t* tftp_data_param::data_ptr
```

指向二进制数据（Binary Data）的指针。

<a id="a704c20ab3177a3d53df21fc9ef64d084"></a>

### `len`

```c
uint32_t tftp_data_param::len
```

二进制数据的长度。

## 90.4\_相关头文件与源码

此页声明来自`<zephyr/net/tftp.h>`。本仓库的[对应头文件](../../../include/zephyr/net/tftp.h)可用于源码跟踪；本仓库版本可能与官网`latest`不同。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P089_TFTP事件参数联合体.md) · [返回大纲](大纲.md) · [下一章](P091_TFTP错误参数.md)
