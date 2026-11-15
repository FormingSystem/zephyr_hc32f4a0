---
id: learning.zephyr-docs.api-file-reference.page-141
title: zephyr__posix__net__if.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/if_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第141章\_zephyr\_\_posix\_\_net\_\_if.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/if_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 141.1\_数据结构（Data Structures）

<a id="r_if_5Fnameindex"></a>

```c
struct if_nameindex
```

相关声明：[if_nameindex](../posix_system_model_reference/P005_if_nameindex_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 141.2\_宏定义（Macros）

<a id="r_aedb93bcce9682d7644080b859849f59d"></a>

```c
#define IF_NAMESIZE 1
```

相关声明：[IF_NAMESIZE](#aedb93bcce9682d7644080b859849f59d)。

<a id="r_acd06da230a96d3b7e6f193c5b3142002"></a>

```c
#define IFNAMSIZ IF_NAMESIZE
```

相关声明：[IFNAMSIZ](#acd06da230a96d3b7e6f193c5b3142002)、[IF_NAMESIZE](#aedb93bcce9682d7644080b859849f59d)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 141.3\_函数（Functions）

<a id="r_a4da7243450c66298378e0f2d6434b997"></a>

```c
char * if_indextoname (unsigned int ifindex, char *ifname)
```

相关声明：[if_indextoname](#a4da7243450c66298378e0f2d6434b997)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

<a id="r_a4349b1231de2572765f6b3771e6023f1"></a>

```c
void if_freenameindex (struct if_nameindex *ptr)
```

相关声明：[if_freenameindex](#a4349b1231de2572765f6b3771e6023f1)、[if_nameindex](../posix_system_model_reference/P005_if_nameindex_结构体.md)。

<a id="r_aadc0427486b1b97fa250760e8ccd4f7f"></a>

```c
struct if_nameindex * if_nameindex (void)
```

相关声明：[if_nameindex](#aadc0427486b1b97fa250760e8ccd4f7f)。

<a id="r_aabacc3c49f072845092730128fbadd93"></a>

```c
unsigned int if_nametoindex (const char *ifname)
```

相关声明：[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[if_nametoindex](#aabacc3c49f072845092730128fbadd93)。

## 141.4\_详细说明（Detailed Documentation）

<a id="aedb93bcce9682d7644080b859849f59d"></a>

### `IF_NAMESIZE`

```c
#define IF_NAMESIZE 1
```

<a id="acd06da230a96d3b7e6f193c5b3142002"></a>

### `IFNAMSIZ`

```c
#define IFNAMSIZ IF_NAMESIZE
```

<a id="a4349b1231de2572765f6b3771e6023f1"></a>

### `if_freenameindex()`

```c
void if_freenameindex ( struct if_nameindex * ptr)
```

<a id="a4da7243450c66298378e0f2d6434b997"></a>

### `if_indextoname()`

```c
char * if_indextoname ( unsigned int ifindex, char * ifname )
```

<a id="aadc0427486b1b97fa250760e8ccd4f7f"></a>

### `if_nameindex()`

```c
struct if_nameindex * if_nameindex ( void )
```

<a id="aabacc3c49f072845092730128fbadd93"></a>

### `if_nametoindex()`

```c
unsigned int if_nametoindex ( const char * ifname)
```


## 141.5\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P341_if.h_源码浏览.md)
- [if_nameindex](../posix_system_model_reference/P005_if_nameindex_结构体.md)
- [unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P140_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__test_toolchain__iar.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P142_zephyr__posix__net__if_arp.h_文件参考.md)
