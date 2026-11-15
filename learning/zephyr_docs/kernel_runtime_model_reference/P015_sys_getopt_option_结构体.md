---
id: learning.zephyr-docs.kernel-runtime-model-reference.page-15
title: sys_getopt_option_结构体
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsys__getopt__option.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_sys\_getopt\_option\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsys__getopt__option.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/sys/sys_getopt.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_a5001cbba7a4968a76a2015f3bc0c752a"></a>

```c
const char * name
```

相关声明：[name](#a5001cbba7a4968a76a2015f3bc0c752a)。

<a id="r_a38c70fec67104f8721366063600ae890"></a>

```c
int has_arg
```

相关声明：[has_arg](#a38c70fec67104f8721366063600ae890)。

<a id="r_a921375712892da06f943f1418bfca4ce"></a>

```c
int * flag
```

相关声明：[flag](#a921375712892da06f943f1418bfca4ce)。

<a id="r_ab7b799a1971273a5464eb9eca849606b"></a>

```c
int val
```

相关声明：[val](#ab7b799a1971273a5464eb9eca849606b)。

## 15.2\_详细说明（Detailed Documentation）

<a id="a921375712892da06f943f1418bfca4ce"></a>

### `flag`

```c
int* sys_getopt_option::flag
```

<a id="a38c70fec67104f8721366063600ae890"></a>

### `has_arg`

```c
int sys_getopt_option::has_arg
```

<a id="a5001cbba7a4968a76a2015f3bc0c752a"></a>

### `name`

```c
const char* sys_getopt_option::name
```

<a id="ab7b799a1971273a5464eb9eca849606b"></a>

### `val`

```c
int sys_getopt_option::val
```

本数据类型文档由以下文件生成：

- `zephyr/sys/sys_getopt.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/sys/sys_getopt.h](https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h_source.html)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P014_pmu_info_t_结构体.md) · [返回大纲](大纲.md) · [下一章](P016_sys_getopt_state_结构体.md)
