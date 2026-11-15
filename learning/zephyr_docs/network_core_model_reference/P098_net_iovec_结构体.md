---
id: learning.zephyr-docs.network-core-model-reference.page-98
title: net_iovec_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__iovec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第98章\_net\_iovec\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__iovec.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

输入输出向量（IO Vector）的数组元素。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

输入输出向量（IO Vector）的数组元素。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 98.1\_数据成员（Data Fields）

<a id="r_a85bbdc499845cf65f24e485ffb4220b8"></a>

```c
void * iov_base
```

相关声明：[iov_base](#a85bbdc499845cf65f24e485ffb4220b8)。

数据指针。

<a id="r_a9d64976623638c5856ff0bb76e41fe73"></a>

```c
size_t iov_len
```

相关声明：[iov_len](#a9d64976623638c5856ff0bb76e41fe73)。

数据长度（Data Length）。

## 98.2\_详细说明（Detailed Documentation）

<a id="a85bbdc499845cf65f24e485ffb4220b8"></a>

### `iov_base`

```c
void* net_iovec::iov_base
```

数据指针。

<a id="a9d64976623638c5856ff0bb76e41fe73"></a>

### `iov_len`

```c
size_t net_iovec::iov_len
```

数据长度（Data Length）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 98.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P097_net_in_pktinfo_结构体.md) · [返回大纲](大纲.md) · [下一章](P099_net_ip_mreq_结构体.md)
