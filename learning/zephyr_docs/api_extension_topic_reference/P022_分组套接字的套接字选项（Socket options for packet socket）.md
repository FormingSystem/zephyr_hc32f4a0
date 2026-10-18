---
id: learning.zephyr-docs.api-extension-topic-reference.page-22
title: 分组套接字的套接字选项（Socket options for packet socket）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__packet__socket__options.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_分组套接字的套接字选项（Socket options for packet socket）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__packet__socket__options.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-member-group"></a>
<a id="member-group"></a>

## 22.1\_套接字级选项（Socket Level Options，ZSOCK_SOL_PACKET）

<a id="r_ga64d5f1636f942f9ff1f02d9918482931"></a>

```c
#define ZSOCK_SOL_PACKET 263
```

相关声明：[ZSOCK_SOL_PACKET](#ga64d5f1636f942f9ff1f02d9918482931)。

数据包套接字级选项（Packet Socket-Level Option）。

<a id="r_ga9674edba4b48e4cc2d1e01a101cead9b"></a>

```c
#define ZSOCK_PACKET_ADD_MEMBERSHIP 1
```

相关声明：[ZSOCK_PACKET_ADD_MEMBERSHIP](#ga9674edba4b48e4cc2d1e01a101cead9b)。

向数据包套接字（Packet Socket）添加多播组成员资格（Multicast Group Membership）。

<a id="r_ga59b254e51063accfb18916b17373d2f6"></a>

```c
#define ZSOCK_PACKET_DROP_MEMBERSHIP 2
```

相关声明：[ZSOCK_PACKET_DROP_MEMBERSHIP](#ga59b254e51063accfb18916b17373d2f6)。

从数据包套接字（Packet Socket）移除多播组成员资格（Multicast Group Membership）。

## 22.2\_详细说明（Detailed Documentation）

<a id="ga9674edba4b48e4cc2d1e01a101cead9b"></a>

### `ZSOCK_PACKET_ADD_MEMBERSHIP`

```c
#define ZSOCK_PACKET_ADD_MEMBERSHIP 1
```

```c
#include <zephyr/net/socket.h>
```

向数据包套接字（Packet Socket）添加多播组成员资格（Multicast Group Membership）。

<a id="ga59b254e51063accfb18916b17373d2f6"></a>

### `ZSOCK_PACKET_DROP_MEMBERSHIP`

```c
#define ZSOCK_PACKET_DROP_MEMBERSHIP 2
```

```c
#include <zephyr/net/socket.h>
```

从数据包套接字（Packet Socket）移除多播组成员资格（Multicast Group Membership）。

<a id="ga64d5f1636f942f9ff1f02d9918482931"></a>

### `ZSOCK_SOL_PACKET`

```c
#define ZSOCK_SOL_PACKET 263
```

```c
#include <zephyr/net/socket.h>
```

数据包套接字级选项（Packet Socket-Level Option）。


## 22.3\_原页交叉引用（Cross References）

- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P021_nPM10xx OTP 接口.md) · [返回大纲](大纲.md) · [下一章](P023_PAT912x API主题.md)
