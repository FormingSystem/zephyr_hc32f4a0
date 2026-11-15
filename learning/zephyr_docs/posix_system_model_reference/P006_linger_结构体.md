---
id: learning.zephyr-docs.posix-system-model-reference.page-6
title: linger_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlinger.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_linger\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlinger.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/sys/socket.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_aa917aeadf061af6ed64aad87df3255fc"></a>

```c
int l_onoff
```

相关声明：[l_onoff](#aa917aeadf061af6ed64aad87df3255fc)。

<a id="r_a2b7d01c9a43f95d2ba6f6cf0ec68b412"></a>

```c
int l_linger
```

相关声明：[l_linger](#a2b7d01c9a43f95d2ba6f6cf0ec68b412)。

## 6.2\_详细说明（Detailed Documentation）

<a id="a2b7d01c9a43f95d2ba6f6cf0ec68b412"></a>

### `l_linger`

```c
int linger::l_linger
```

<a id="aa917aeadf061af6ed64aad87df3255fc"></a>

### `l_onoff`

```c
int linger::l_onoff
```

本数据类型文档由以下文件生成：

- `zephyr/posix/sys/socket.h`

## 6.3\_原页交叉引用（Cross References）

- [zephyr/posix/sys/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h_source.html)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_if_nameindex_结构体.md) · [返回大纲](大纲.md) · [下一章](P007_mq_attr_结构体.md)
