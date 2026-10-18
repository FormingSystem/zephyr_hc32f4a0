---
id: learning.zephyr-docs.api-file-reference.page-48
title: ____w__zephyr__zephyr__lib__libc__minimal__include__ctype.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_lib\_\_libc\_\_minimal\_\_include\_\_ctype.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ctype_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 48.1\_函数（Functions）

<a id="r_a05d9ca901946ee2f2078c351163dc015"></a>

```c
static int isupper (int a)
```

相关声明：[isupper](#a05d9ca901946ee2f2078c351163dc015)。

<a id="r_ab208778249f6c2cf8339e187e21e11bd"></a>

```c
static int isalpha (int c)
```

相关声明：[isalpha](#ab208778249f6c2cf8339e187e21e11bd)。

<a id="r_a9ad6bca8b20d91ab6ee00b58d8c46475"></a>

```c
static int isblank (int c)
```

相关声明：[isblank](#a9ad6bca8b20d91ab6ee00b58d8c46475)。

<a id="r_a9318513eb3136e55002d65bf602f74a7"></a>

```c
static int isspace (int c)
```

相关声明：[isspace](#a9318513eb3136e55002d65bf602f74a7)。

<a id="r_a825ff84641e11035f0b6aa8f86eacbfd"></a>

```c
static int isgraph (int c)
```

相关声明：[isgraph](#a825ff84641e11035f0b6aa8f86eacbfd)。

<a id="r_ab14b97a75cf7392a543f89b5530e0ad7"></a>

```c
static int isprint (int c)
```

相关声明：[isprint](#ab14b97a75cf7392a543f89b5530e0ad7)。

<a id="r_a7c84919af75ed5a47fab36e2fa13775f"></a>

```c
static int isdigit (int a)
```

相关声明：[isdigit](#a7c84919af75ed5a47fab36e2fa13775f)。

<a id="r_a20359f43d3eb2382afa4efdeb3f66dcf"></a>

```c
static int islower (int c)
```

相关声明：[islower](#a20359f43d3eb2382afa4efdeb3f66dcf)。

<a id="r_a0152b6658f63acfdd96a9409d0142719"></a>

```c
static int isxdigit (int a)
```

相关声明：[isxdigit](#a0152b6658f63acfdd96a9409d0142719)。

<a id="r_ab5088a2e14096e665c030d72508e2e9d"></a>

```c
static int tolower (int chr)
```

相关声明：[tolower](#ab5088a2e14096e665c030d72508e2e9d)。

<a id="r_abfe63aca83a67be16cf7b8636260b018"></a>

```c
static int toupper (int chr)
```

相关声明：[toupper](#abfe63aca83a67be16cf7b8636260b018)。

<a id="r_ac4c06d14f1ed4d340b63aaeea1a830af"></a>

```c
static int isalnum (int chr)
```

相关声明：[isalnum](#ac4c06d14f1ed4d340b63aaeea1a830af)。

<a id="r_aba67c74e5652a4544dbb92a46704cca3"></a>

```c
static int ispunct (int c)
```

相关声明：[ispunct](#aba67c74e5652a4544dbb92a46704cca3)。

<a id="r_a5d4143d99c571ef986ffc4a88df64097"></a>

```c
static int iscntrl (int c)
```

相关声明：[iscntrl](#a5d4143d99c571ef986ffc4a88df64097)。

## 48.2\_详细说明（Detailed Documentation）

<a id="ac4c06d14f1ed4d340b63aaeea1a830af"></a>

### `isalnum()`

```c
int isalnum ( int chr)
```

声明属性：`inline`、`static`。

<a id="ab208778249f6c2cf8339e187e21e11bd"></a>

### `isalpha()`

```c
int isalpha ( int c)
```

声明属性：`inline`、`static`。

<a id="a9ad6bca8b20d91ab6ee00b58d8c46475"></a>

### `isblank()`

```c
int isblank ( int c)
```

声明属性：`inline`、`static`。

<a id="a5d4143d99c571ef986ffc4a88df64097"></a>

### `iscntrl()`

```c
int iscntrl ( int c)
```

声明属性：`inline`、`static`。

<a id="a7c84919af75ed5a47fab36e2fa13775f"></a>

### `isdigit()`

```c
int isdigit ( int a)
```

声明属性：`inline`、`static`。

<a id="a825ff84641e11035f0b6aa8f86eacbfd"></a>

### `isgraph()`

```c
int isgraph ( int c)
```

声明属性：`inline`、`static`。

<a id="a20359f43d3eb2382afa4efdeb3f66dcf"></a>

### `islower()`

```c
int islower ( int c)
```

声明属性：`inline`、`static`。

<a id="ab14b97a75cf7392a543f89b5530e0ad7"></a>

### `isprint()`

```c
int isprint ( int c)
```

声明属性：`inline`、`static`。

<a id="aba67c74e5652a4544dbb92a46704cca3"></a>

### `ispunct()`

```c
int ispunct ( int c)
```

声明属性：`inline`、`static`。

<a id="a9318513eb3136e55002d65bf602f74a7"></a>

### `isspace()`

```c
int isspace ( int c)
```

声明属性：`inline`、`static`。

<a id="a05d9ca901946ee2f2078c351163dc015"></a>

### `isupper()`

```c
int isupper ( int a)
```

声明属性：`inline`、`static`。

<a id="a0152b6658f63acfdd96a9409d0142719"></a>

### `isxdigit()`

```c
int isxdigit ( int a)
```

声明属性：`inline`、`static`。

<a id="ab5088a2e14096e665c030d72508e2e9d"></a>

### `tolower()`

```c
int tolower ( int chr)
```

声明属性：`inline`、`static`。

<a id="abfe63aca83a67be16cf7b8636260b018"></a>

### `toupper()`

```c
int toupper ( int chr)
```

声明属性：`inline`、`static`。


## 48.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P015_ctype.h_源码浏览.md)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P047_zephyr__arch__tricore__cr.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P049_zephyr__posix__dirent.h_文件参考.md)
