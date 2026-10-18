---
id: learning.zephyr-docs.posix-system-model-reference.page-14
title: pthread_mutexattr_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpthread__mutexattr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_pthread\_mutexattr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpthread__mutexattr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/posix_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_a2d6345d486a409d7e9942f102e7f0b59"></a>

```c
unsigned char type: 2
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[type](#a2d6345d486a409d7e9942f102e7f0b59)。

<a id="r_afa55f47ff86cf3931d7bbb65de6697c6"></a>

```c
bool initialized: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[initialized](#afa55f47ff86cf3931d7bbb65de6697c6)。

## 14.2\_详细说明（Detailed Documentation）

<a id="afa55f47ff86cf3931d7bbb65de6697c6"></a>

### `initialized`

```c
bool pthread_mutexattr::initialized
```

<a id="a2d6345d486a409d7e9942f102e7f0b59"></a>

### `type`

```c
unsigned char pthread_mutexattr::type
```

本数据类型文档由以下文件生成：

- `zephyr/posix/posix_types.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/posix/posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_pthread_condattr_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_pthread_once_结构体.md)
