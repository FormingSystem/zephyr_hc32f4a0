---
id: learning.zephyr-docs.posix-system-model-reference.page-30
title: zsock_pollfd_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzsock__pollfd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_zsock\_pollfd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structzsock__pollfd.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

被监测套接字/文件描述符（Socket / File Descriptor）的定义。

```c
#include <zephyr/net/socket_poll.h>
```

<a id="details"></a>

受监视的套接字或文件描述符的定义。由这些描述符组成的数组作为参数传给 `poll()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 30.1\_数据成员（Data Fields）

<a id="r_a58fcd3f9af542bb15a936319aaf9c32e"></a>

```c
int fd
```

相关声明：[fd](#a58fcd3f9af542bb15a936319aaf9c32e)。

套接字描述符（Socket Descriptor）。

<a id="r_a31929c24c64b58c6f7e443645352f67d"></a>

```c
short events
```

相关声明：[events](#a31929c24c64b58c6f7e443645352f67d)。

请求监视的事件。

<a id="r_a98838f19b29e759a4b53db9b15349917"></a>

```c
short revents
```

相关声明：[revents](#a98838f19b29e759a4b53db9b15349917)。

返回的事件。

## 30.2\_详细说明（Detailed Documentation）

<a id="a31929c24c64b58c6f7e443645352f67d"></a>

### `events`

```c
short zsock_pollfd::events
```

请求监视的事件。

<a id="a58fcd3f9af542bb15a936319aaf9c32e"></a>

### `fd`

```c
int zsock_pollfd::fd
```

套接字描述符（Socket Descriptor）。

<a id="a98838f19b29e759a4b53db9b15349917"></a>

### `revents`

```c
short zsock_pollfd::revents
```

返回的事件。

本数据类型文档由以下文件生成：

- `zephyr/net/socket_poll.h`

## 30.3\_原页交叉引用（Cross References）

- [zephyr/net/socket_poll.h](https://docs.zephyrproject.org/latest/doxygen/html/socket__poll_8h_source.html)
- [poll()](https://docs.zephyrproject.org/latest/doxygen/html/poll_8h.html#afa7e83ddea0ab5b08fcf614b89ac48ba)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P029_zsock_addrinfo_结构体.md) · [返回大纲](大纲.md) · [下一章](P031_zsock_tls_cert_verify_cb_结构体.md)
