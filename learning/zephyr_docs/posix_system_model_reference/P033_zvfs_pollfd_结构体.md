---
id: learning.zephyr-docs.posix-system-model-reference.page-33
title: zvfs_pollfd_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzvfs__pollfd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_zvfs\_pollfd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structzvfs__pollfd.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/sys/fdtable.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 33.1\_数据成员（Data Fields）

<a id="r_af249cde934b4e7f620d0724c89ac7000"></a>

```c
int fd
```

相关声明：[fd](#af249cde934b4e7f620d0724c89ac7000)。

<a id="r_a1e2a42fca725be5059d51817b2caaeb9"></a>

```c
short events
```

相关声明：[events](#a1e2a42fca725be5059d51817b2caaeb9)。

<a id="r_ab13e3da1e537937e487c99aa385c3265"></a>

```c
short revents
```

相关声明：[revents](#ab13e3da1e537937e487c99aa385c3265)。

## 33.2\_详细说明（Detailed Documentation）

<a id="a1e2a42fca725be5059d51817b2caaeb9"></a>

### `events`

```c
short zvfs_pollfd::events
```

<a id="af249cde934b4e7f620d0724c89ac7000"></a>

### `fd`

```c
int zvfs_pollfd::fd
```

<a id="ab13e3da1e537937e487c99aa385c3265"></a>

### `revents`

```c
short zvfs_pollfd::revents
```

本数据类型文档由以下文件生成：

- `zephyr/sys/fdtable.h`

## 33.3\_原页交叉引用（Cross References）

- [zephyr/sys/fdtable.h](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h_source.html)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P032_zvfs_fd_set_结构体.md) · [返回大纲](大纲.md) · [下一章](P034_zvfs_stat_结构体.md)
