---
id: learning.zephyr-docs.posix-system-model-reference.page-35
title: sigval_联合体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionsigval.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_sigval\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionsigval.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/posix_signal.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 35.1\_数据成员（Data Fields）

<a id="r_a560393252ee7edc37df44bf1c11bdbdd"></a>

```c
int sival_int
```

相关声明：[sival_int](#a560393252ee7edc37df44bf1c11bdbdd)。

<a id="r_a4668f1bd7463de7b70bd0022207e26ac"></a>

```c
void * sival_ptr
```

相关声明：[sival_ptr](#a4668f1bd7463de7b70bd0022207e26ac)。

## 35.2\_详细说明（Detailed Documentation）

<a id="a560393252ee7edc37df44bf1c11bdbdd"></a>

### `sival_int`

```c
int sigval::sival_int
```

<a id="a4668f1bd7463de7b70bd0022207e26ac"></a>

### `sival_ptr`

```c
void* sigval::sival_ptr
```

本数据类型文档由以下文件生成：

- `zephyr/posix/posix_signal.h`

## 35.3\_原页交叉引用（Cross References）

- [zephyr/posix/posix_signal.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h_source.html)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P034_zvfs_stat_结构体.md) · [返回大纲](大纲.md)
