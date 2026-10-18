---
id: learning.zephyr-docs.networking.api-196
title: OCPP的TLS凭据结构
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structocpp__tls__credentials.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第196章\_OCPP的TLS凭据结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structocpp__tls__credentials.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 196.1\_阅读说明与来源

译注：先读[OCPP 充电桩协议指南](P179_OCPP充电桩协议.md)和[充电桩示例](P182_OCPP充电桩示例.md)，理解充电桩（Charge Point，CP）、中央系统（Central System，CS）、连接器（Connector）、会话（Session）与交易（Transaction）的关系，再按符号查询。

本组：[OCPP完整API参考](P191_OCPP完整API参考.md) · [OCPP头文件参考](P192_OCPP头文件参考.md) · [OCPP头文件源码](P193_OCPP头文件源码.md) · [OCPP充电桩信息结构](P194_OCPP充电桩信息结构.md) · [OCPP中央系统信息结构](P195_OCPP中央系统信息结构.md) · [OCPP的TLS凭据结构](P196_OCPP的TLS凭据结构.md) · [OCPP回调输入输出联合体](P197_OCPP回调输入输出联合体.md)。

中央系统（Central System，CS）的传输层安全（Transport Layer Security，TLS）凭据信息。

```c
#include <zephyr/net/ocpp.h>
```

中央系统（Central System，CS）的传输层安全（Transport Layer Security，TLS）凭据信息。

## 196.2\_数据成员（Data Fields）

<a id="r_a38877cf5cdbfb9d86a0932a231ac4ac0"></a>

```c
const sec_tag_t * sec_tag_list
```

TLS 安全标签列表（Security Tag List）。

<a id="r_aa86c71d47996475aed2dc064f8278a2d"></a>

```c
char * tls_hostname
```

TLS 主机名（Hostname）。

<a id="r_a489357da079435f78a5fbcc96c7d4eb3"></a>

```c
size_t sec_tag_list_size
```

TLS 安全标签列表的大小。

<a id="r_a7a8e98e378561654968250b157ef2bf7"></a>

```c
size_t tls_hostname_size
```

TLS 主机名的大小。

## 196.3\_详细说明（Detailed Documentation）

<a id="a38877cf5cdbfb9d86a0932a231ac4ac0"></a>

### `sec_tag_list`

```c
const sec_tag_t* ocpp_tls_credentials::sec_tag_list
```

TLS 安全标签列表（Security Tag List）。

<a id="a489357da079435f78a5fbcc96c7d4eb3"></a>

### `sec_tag_list_size`

```c
size_t ocpp_tls_credentials::sec_tag_list_size
```

TLS 安全标签列表的大小。

<a id="aa86c71d47996475aed2dc064f8278a2d"></a>

### `tls_hostname`

```c
char* ocpp_tls_credentials::tls_hostname
```

TLS 主机名（Hostname）。

<a id="a7a8e98e378561654968250b157ef2bf7"></a>

### `tls_hostname_size`

```c
size_t ocpp_tls_credentials::tls_hostname_size
```

TLS 主机名的大小。

## 196.4\_相关源码与使用边界

声明来自 `<zephyr/net/ocpp.h>`。本仓库的[对应头文件](../../../include/zephyr/net/ocpp.h)可用于源码追踪，版本可能与官网 `latest` 不同。源码核对依据为本批保存的[官方协议实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/ocpp.c)、[官方请求实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/core.c)及[官方示例](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ocpp/src/main.c)，摘要见[来源记录](../SOURCES.md)。

> 译注——大小与生存期：当前实现把两个 `*_size` 直接传给 `zsock_setsockopt()` 的长度参数。官方示例使用 `sizeof(tags)` 填写 `sec_tag_list_size`，使用 `strlen(TLS_PEER_HOSTNAME)` 填写 `tls_hostname_size`；前者是数组字节数，不是标签个数，后者按示例不包含字符串末尾的空字符。初始化保存的是 `sec_tag_list` 和 `tls_hostname` 指针，没有复制其内容，应保证所指对象在后续连接使用期间有效。安全标签指向预先注册的 TLS 凭据，不是证书文件本身。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P195_OCPP中央系统信息结构.md) · [返回大纲](大纲.md) · [下一章](P197_OCPP回调输入输出联合体.md)
