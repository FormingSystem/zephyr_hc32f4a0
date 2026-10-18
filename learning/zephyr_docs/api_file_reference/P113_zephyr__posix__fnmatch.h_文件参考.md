---
id: learning.zephyr-docs.api-file-reference.page-113
title: zephyr__posix__fnmatch.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fnmatch_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第113章\_zephyr\_\_posix\_\_fnmatch.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fnmatch_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 113.1\_宏定义（Macros）

<a id="r_af2661230e0cfc9970d6cdbe01571e753"></a>

```c
#define FNM_NOMATCH 1 /* Match failed. */
```

相关声明：[FNM_NOMATCH](#af2661230e0cfc9970d6cdbe01571e753)。

<a id="r_abf296e95251824c90803dd3aa374190d"></a>

```c
#define FNM_NOSYS 2 /* Function not implemented. */
```

相关声明：[FNM_NOSYS](#abf296e95251824c90803dd3aa374190d)。

<a id="r_a944d56e32e8885bb5f89d654b383abf8"></a>

```c
#define FNM_NORES 3 /* Out of resources */
```

相关声明：[FNM_NORES](#a944d56e32e8885bb5f89d654b383abf8)。

<a id="r_a0c050a8a7551c2ca86560396de3d20d0"></a>

```c
#define FNM_NOESCAPE 0x01 /* Disable backslash escaping. */
```

相关声明：[FNM_NOESCAPE](#a0c050a8a7551c2ca86560396de3d20d0)。

<a id="r_aed9e649990b20ba86e1aa7cacdc1bafe"></a>

```c
#define FNM_PATHNAME 0x02 /* Slash must be matched by slash. */
```

相关声明：[FNM_PATHNAME](#aed9e649990b20ba86e1aa7cacdc1bafe)。

<a id="r_aab98fecc02c06d6379bfcf416d6d297e"></a>

```c
#define FNM_PERIOD 0x04 /* Period must be matched by period. */
```

相关声明：[FNM_PERIOD](#aab98fecc02c06d6379bfcf416d6d297e)。

<a id="r_ad41e3158a654dd4dfdab19d97745698a"></a>

```c
#define FNM_CASEFOLD 0x08 /* Pattern is matched case-insensitive */
```

相关声明：[FNM_CASEFOLD](#ad41e3158a654dd4dfdab19d97745698a)。

<a id="r_a94f8f78b6d024e35c971dd3ec057140c"></a>

```c
#define FNM_LEADING_DIR 0x10 /* Ignore /<tail> after Imatch. */
```

相关声明：[FNM_LEADING_DIR](#a94f8f78b6d024e35c971dd3ec057140c)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 113.2\_函数（Functions）

<a id="r_a088b414f40eb0ce3dad9e5243816f68f"></a>

```c
int fnmatch (const char *pattern, const char *string, int flags)
```

相关声明：[fnmatch](#a088b414f40eb0ce3dad9e5243816f68f)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

## 113.3\_详细说明（Detailed Documentation）

<a id="ad41e3158a654dd4dfdab19d97745698a"></a>

### `FNM_CASEFOLD`

```c
#define FNM_CASEFOLD 0x08 /* Pattern is matched case-insensitive */
```

<a id="a94f8f78b6d024e35c971dd3ec057140c"></a>

### `FNM_LEADING_DIR`

```c
#define FNM_LEADING_DIR 0x10 /* Ignore /<tail> after Imatch. */
```

<a id="a0c050a8a7551c2ca86560396de3d20d0"></a>

### `FNM_NOESCAPE`

```c
#define FNM_NOESCAPE 0x01 /* Disable backslash escaping. */
```

<a id="af2661230e0cfc9970d6cdbe01571e753"></a>

### `FNM_NOMATCH`

```c
#define FNM_NOMATCH 1 /* Match failed. */
```

<a id="a944d56e32e8885bb5f89d654b383abf8"></a>

### `FNM_NORES`

```c
#define FNM_NORES 3 /* Out of resources */
```

<a id="abf296e95251824c90803dd3aa374190d"></a>

### `FNM_NOSYS`

```c
#define FNM_NOSYS 2 /* Function not implemented. */
```

<a id="aed9e649990b20ba86e1aa7cacdc1bafe"></a>

### `FNM_PATHNAME`

```c
#define FNM_PATHNAME 0x02 /* Slash must be matched by slash. */
```

<a id="aab98fecc02c06d6379bfcf416d6d297e"></a>

### `FNM_PERIOD`

```c
#define FNM_PERIOD 0x04 /* Period must be matched by period. */
```

<a id="a088b414f40eb0ce3dad9e5243816f68f"></a>

### `fnmatch()`

```c
int fnmatch ( const char * pattern, const char * string, int flags )
```


## 113.4\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/fnmatch_8h_source.html)
- [flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P112_zephyr__posix__fcntl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P114_zephyr__dt-bindings__clock__focaltech_ft9001_clocks.h_文件参考.md)
