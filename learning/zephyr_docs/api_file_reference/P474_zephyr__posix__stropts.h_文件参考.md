---
id: learning.zephyr-docs.api-file-reference.page-474
title: zephyr__posix__stropts.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stropts_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第474章\_zephyr\_\_posix\_\_stropts.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stropts_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 474.1\_数据结构（Data Structures）

<a id="r_strbuf"></a>

```c
struct strbuf
```

相关声明：[strbuf](../posix_system_model_reference/P023_strbuf_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 474.2\_宏定义（Macros）

<a id="r_ab12b3c3c77f22b0999f6b2cec1812da9"></a>

```c
#define RS_HIPRI BIT(0)
```

相关声明：[RS_HIPRI](#ab12b3c3c77f22b0999f6b2cec1812da9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 474.3\_函数（Functions）

<a id="r_a2e8c9b125d5b2b9e9c0f119bb8489c5e"></a>

```c
int putmsg (int fildes, const struct strbuf *ctlptr, const struct strbuf *dataptr, int flags)
```

相关声明：[putmsg](#a2e8c9b125d5b2b9e9c0f119bb8489c5e)、[strbuf](../posix_system_model_reference/P023_strbuf_结构体.md)、[strbuf](../posix_system_model_reference/P023_strbuf_结构体.md)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

<a id="r_ace3f43f93319016fce6e1ce8bb135ee2"></a>

```c
int fdetach (const char *path)
```

相关声明：[fdetach](#ace3f43f93319016fce6e1ce8bb135ee2)。

<a id="r_aad1d52cad379cd124cbed912aa636ad1"></a>

```c
int fattach (int fildes, const char *path)
```

相关声明：[fattach](#aad1d52cad379cd124cbed912aa636ad1)。

<a id="r_a49857bef3fb1cecd099e67c8df35c8ef"></a>

```c
int getmsg (int fildes, struct strbuf *ctlptr, struct strbuf *dataptr, int *flagsp)
```

相关声明：[getmsg](#a49857bef3fb1cecd099e67c8df35c8ef)、[strbuf](../posix_system_model_reference/P023_strbuf_结构体.md)、[strbuf](../posix_system_model_reference/P023_strbuf_结构体.md)。

<a id="r_a55b37250892d8a0821df369a5f744099"></a>

```c
int getpmsg (int fildes, struct strbuf *ctlptr, struct strbuf *dataptr, int *bandp, int *flagsp)
```

相关声明：[getpmsg](#a55b37250892d8a0821df369a5f744099)、[strbuf](../posix_system_model_reference/P023_strbuf_结构体.md)、[strbuf](../posix_system_model_reference/P023_strbuf_结构体.md)。

<a id="r_add5237bf6844593ab11f8daa15d16070"></a>

```c
int isastream (int fildes)
```

相关声明：[isastream](#add5237bf6844593ab11f8daa15d16070)。

## 474.4\_详细说明（Detailed Documentation）

<a id="ab12b3c3c77f22b0999f6b2cec1812da9"></a>

### `RS_HIPRI`

```c
#define RS_HIPRI BIT(0)
```

<a id="aad1d52cad379cd124cbed912aa636ad1"></a>

### `fattach()`

```c
int fattach ( int fildes, const char * path )
```

<a id="ace3f43f93319016fce6e1ce8bb135ee2"></a>

### `fdetach()`

```c
int fdetach ( const char * path)
```

<a id="a49857bef3fb1cecd099e67c8df35c8ef"></a>

### `getmsg()`

```c
int getmsg ( int fildes, struct strbuf * ctlptr, struct strbuf * dataptr, int * flagsp )
```

<a id="a55b37250892d8a0821df369a5f744099"></a>

### `getpmsg()`

```c
int getpmsg ( int fildes, struct strbuf * ctlptr, struct strbuf * dataptr, int * bandp, int * flagsp )
```

<a id="add5237bf6844593ab11f8daa15d16070"></a>

### `isastream()`

```c
int isastream ( int fildes)
```

<a id="a2e8c9b125d5b2b9e9c0f119bb8489c5e"></a>

### `putmsg()`

```c
int putmsg ( int fildes, const struct strbuf * ctlptr, const struct strbuf * dataptr, int flags )
```


## 474.5\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P841_stropts.h_源码浏览.md)
- [strbuf](../posix_system_model_reference/P023_strbuf_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P473_____w__zephyr__zephyr__lib__libc__minimal__include__strings.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P475_zephyr__arch__structs.h_文件参考.md)
