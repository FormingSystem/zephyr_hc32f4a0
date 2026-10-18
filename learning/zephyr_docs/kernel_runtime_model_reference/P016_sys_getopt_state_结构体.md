---
id: learning.zephyr-docs.kernel-runtime-model-reference.page-16
title: sys_getopt_state_结构体
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsys__getopt__state.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_sys\_getopt\_state\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsys__getopt__state.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/sys/sys_getopt.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 16.1\_数据成员（Data Fields）

<a id="r_a51925275080512a6dcac6b4e1a28d8cb"></a>

```c
int opterr
```

相关声明：[opterr](#a51925275080512a6dcac6b4e1a28d8cb)。

<a id="r_a9de2baf0642b3e50a05116b10706bbe8"></a>

```c
int optind
```

相关声明：[optind](#a9de2baf0642b3e50a05116b10706bbe8)。

<a id="r_ad41495ab8dd1cb55efc177fdb3e45316"></a>

```c
int optopt
```

相关声明：[optopt](#ad41495ab8dd1cb55efc177fdb3e45316)。

<a id="r_a8b05064215051a7ee82038bfb56a1cd1"></a>

```c
int optreset
```

相关声明：[optreset](#a8b05064215051a7ee82038bfb56a1cd1)。

<a id="r_a65eb337bc32085a402a9fb0c58a2bea8"></a>

```c
char * optarg
```

相关声明：[optarg](#a65eb337bc32085a402a9fb0c58a2bea8)。

<a id="r_a887b21d513bca0eee2a300b7ccd39364"></a>

```c
char * place
```

相关声明：[place](#a887b21d513bca0eee2a300b7ccd39364)。

## 16.2\_详细说明（Detailed Documentation）

<a id="a65eb337bc32085a402a9fb0c58a2bea8"></a>

### `optarg`

```c
char* sys_getopt_state::optarg
```

<a id="a51925275080512a6dcac6b4e1a28d8cb"></a>

### `opterr`

```c
int sys_getopt_state::opterr
```

<a id="a9de2baf0642b3e50a05116b10706bbe8"></a>

### `optind`

```c
int sys_getopt_state::optind
```

<a id="ad41495ab8dd1cb55efc177fdb3e45316"></a>

### `optopt`

```c
int sys_getopt_state::optopt
```

<a id="a8b05064215051a7ee82038bfb56a1cd1"></a>

### `optreset`

```c
int sys_getopt_state::optreset
```

<a id="a887b21d513bca0eee2a300b7ccd39364"></a>

### `place`

```c
char* sys_getopt_state::place
```

本数据类型文档由以下文件生成：

- `zephyr/sys/sys_getopt.h`

## 16.3\_原页交叉引用（Cross References）

- [zephyr/sys/sys_getopt.h](https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h_source.html)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P015_sys_getopt_option_结构体.md) · [返回大纲](大纲.md) · [下一章](P017_sys_mm_drv_bank_结构体.md)
