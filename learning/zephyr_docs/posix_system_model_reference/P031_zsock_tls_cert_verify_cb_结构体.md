---
id: learning.zephyr-docs.posix-system-model-reference.page-31
title: zsock_tls_cert_verify_cb_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzsock__tls__cert__verify__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_zsock\_tls\_cert\_verify\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structzsock__tls__cert__verify__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ZSOCK_TLS_CERT_VERIFY_CALLBACK套接字选项的数据结构。

```c
#include <zephyr/net/socket.h>
```

<a id="details"></a>

ZSOCK_TLS_CERT_VERIFY_CALLBACK套接字选项的数据结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 31.1\_数据成员（Data Fields）

<a id="r_a41240ca56bdbf02f6946b8b19df73463"></a>

```c
void * cb
```

相关声明：[cb](#a41240ca56bdbf02f6946b8b19df73463)。

指向证书验证（certificate verification）回调函数的指针。

<a id="r_acc073b829127224887c8da33bce19943"></a>

```c
void * ctx
```

相关声明：[ctx](#acc073b829127224887c8da33bce19943)。

指向传给回调的不透明上下文（opaque context）的指针。

## 31.2\_详细说明（Detailed Documentation）

<a id="a41240ca56bdbf02f6946b8b19df73463"></a>

### `cb`

```c
void* zsock_tls_cert_verify_cb::cb
```

指向证书验证（certificate verification）回调函数的指针。

实际回调函数类型由 Mbed TLS 定义，参见 `mbedtls_x509_crt_verify()` 函数文档。

<a id="acc073b829127224887c8da33bce19943"></a>

### `ctx`

```c
void* zsock_tls_cert_verify_cb::ctx
```

指向传给回调的不透明上下文（opaque context）的指针。

本数据类型文档由以下文件生成：

- `zephyr/net/socket.h`

## 31.3\_原页交叉引用（Cross References）

- [ZSOCK_TLS_CERT_VERIFY_CALLBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__secure__sockets__options.html#ga4425112197a30ca359c57de0e824f0d1)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P030_zsock_pollfd_结构体.md) · [返回大纲](大纲.md) · [下一章](P032_zvfs_fd_set_结构体.md)
