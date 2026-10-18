---
id: learning.zephyr-docs.api-file-reference.page-472
title: ____w__zephyr__zephyr__lib__libc__minimal__include__string.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第472章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_lib\_\_libc\_\_minimal\_\_include\_\_string.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stddef.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 472.1\_函数（Functions）

<a id="r_a6d729a7b6396b8508060821c56f4adbc"></a>

```c
char * strcpy (char *ZRESTRICT d, const char *ZRESTRICT s)
```

相关声明：[strcpy](#a6d729a7b6396b8508060821c56f4adbc)。

<a id="r_a4bc5f273980fb0e81e0fc7a4dd3de87e"></a>

```c
char * strerror (int errnum)
```

相关声明：[strerror](#a4bc5f273980fb0e81e0fc7a4dd3de87e)。

<a id="r_a080c6052ea267026d0baa316f8610b46"></a>

```c
int strerror_r (int errnum, char *strerrbuf, size_t buflen)
```

相关声明：[strerror_r](#a080c6052ea267026d0baa316f8610b46)。

<a id="r_aa7003ae2e637e6eb92a4c5e7523848a5"></a>

```c
char * strncpy (char *ZRESTRICT d, const char *ZRESTRICT s, size_t n)
```

相关声明：[strncpy](#aa7003ae2e637e6eb92a4c5e7523848a5)。

<a id="r_ad7c16a2447154107d5ecd28434993443"></a>

```c
char * strchr (const char *s, int c)
```

相关声明：[strchr](#ad7c16a2447154107d5ecd28434993443)。

<a id="r_af87bb1cdc3d71abcd9aa0bd6d36e50a8"></a>

```c
char * strrchr (const char *s, int c)
```

相关声明：[strrchr](#af87bb1cdc3d71abcd9aa0bd6d36e50a8)。

<a id="r_aa383452fe445bfae989358c9d7d96f4f"></a>

```c
size_t strlen (const char *s)
```

相关声明：[strlen](#aa383452fe445bfae989358c9d7d96f4f)。

<a id="r_afc92d2231e45d19988c7894aa2a07f0c"></a>

```c
size_t strnlen (const char *s, size_t maxlen)
```

相关声明：[strnlen](#afc92d2231e45d19988c7894aa2a07f0c)。

<a id="r_a11bd144d7d44914099a3aeddf1c8567d"></a>

```c
int strcmp (const char *s1, const char *s2)
```

相关声明：[strcmp](#a11bd144d7d44914099a3aeddf1c8567d)。

<a id="r_a07f4a84c11c106e95c32b6ab509346ef"></a>

```c
int strncmp (const char *s1, const char *s2, size_t n)
```

相关声明：[strncmp](#a07f4a84c11c106e95c32b6ab509346ef)。

<a id="r_a22af6fcfed68749460181f2077c34813"></a>

```c
char * strtok_r (char *str, const char *sep, char **state)
```

相关声明：[strtok_r](#a22af6fcfed68749460181f2077c34813)、[state](P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

<a id="r_a85c0f130f91a3121ee06207f42554572"></a>

```c
char * strcat (char *ZRESTRICT dest, const char *ZRESTRICT src)
```

相关声明：[strcat](#a85c0f130f91a3121ee06207f42554572)。

<a id="r_a32dff100d3a0806b158b13bbe60710af"></a>

```c
char * strncat (char *ZRESTRICT dest, const char *ZRESTRICT src, size_t n)
```

相关声明：[strncat](#a32dff100d3a0806b158b13bbe60710af)。

<a id="r_adef2d6284e392701fd4149b344188ceb"></a>

```c
char * strstr (const char *s, const char *find)
```

相关声明：[strstr](#adef2d6284e392701fd4149b344188ceb)。

<a id="r_a900a0edfa51f601d479244f7451cedd1"></a>

```c
size_t strspn (const char *s, const char *accept)
```

相关声明：[strspn](#a900a0edfa51f601d479244f7451cedd1)、[accept](P307_zephyr__posix__sys__socket.h_文件参考.md#a66e3de379c18201b21c889035ec54864)。

<a id="r_aeb6c449e5d77477c057abf00eaaf88fe"></a>

```c
size_t strcspn (const char *s, const char *reject)
```

相关声明：[strcspn](#aeb6c449e5d77477c057abf00eaaf88fe)。

<a id="r_ad8bfbfa1e4ad284ded921dd775735521"></a>

```c
int memcmp (const void *m1, const void *m2, size_t n)
```

相关声明：[memcmp](#ad8bfbfa1e4ad284ded921dd775735521)。

<a id="r_a71a1afb093b0af8298df8a745b1b1f5c"></a>

```c
void * memmove (void *d, const void *s, size_t n)
```

相关声明：[memmove](#a71a1afb093b0af8298df8a745b1b1f5c)。

<a id="r_af0f01bffcd16daa9143f6014d10a25ad"></a>

```c
void * memcpy (void *ZRESTRICT d, const void *ZRESTRICT s, size_t n)
```

相关声明：[memcpy](#af0f01bffcd16daa9143f6014d10a25ad)。

<a id="r_a4137694174d4ca2fad886a1db355015c"></a>

```c
void * memset (void *buf, int c, size_t n)
```

相关声明：[memset](#a4137694174d4ca2fad886a1db355015c)。

<a id="r_a0a3e4af1b88f5d51a32fe7dcbf753b38"></a>

```c
void * memchr (const void *s, int c, size_t n)
```

相关声明：[memchr](#a0a3e4af1b88f5d51a32fe7dcbf753b38)。

## 472.2\_详细说明（Detailed Documentation）

<a id="a0a3e4af1b88f5d51a32fe7dcbf753b38"></a>

### `memchr()`

```c
void * memchr ( const void * s, int c, size_t n )
```

声明属性：`extern`。

<a id="ad8bfbfa1e4ad284ded921dd775735521"></a>

### `memcmp()`

```c
int memcmp ( const void * m1, const void * m2, size_t n )
```

声明属性：`extern`。

<a id="af0f01bffcd16daa9143f6014d10a25ad"></a>

### `memcpy()`

```c
void * memcpy ( void *ZRESTRICT d, const void *ZRESTRICT s, size_t n )
```

声明属性：`extern`。

<a id="a71a1afb093b0af8298df8a745b1b1f5c"></a>

### `memmove()`

```c
void * memmove ( void * d, const void * s, size_t n )
```

声明属性：`extern`。

<a id="a4137694174d4ca2fad886a1db355015c"></a>

### `memset()`

```c
void * memset ( void * buf, int c, size_t n )
```

声明属性：`extern`。

<a id="a85c0f130f91a3121ee06207f42554572"></a>

### `strcat()`

```c
char * strcat ( char *ZRESTRICT dest, const char *ZRESTRICT src )
```

声明属性：`extern`。

<a id="ad7c16a2447154107d5ecd28434993443"></a>

### `strchr()`

```c
char * strchr ( const char * s, int c )
```

声明属性：`extern`。

<a id="a11bd144d7d44914099a3aeddf1c8567d"></a>

### `strcmp()`

```c
int strcmp ( const char * s1, const char * s2 )
```

声明属性：`extern`。

<a id="a6d729a7b6396b8508060821c56f4adbc"></a>

### `strcpy()`

```c
char * strcpy ( char *ZRESTRICT d, const char *ZRESTRICT s )
```

声明属性：`extern`。

<a id="aeb6c449e5d77477c057abf00eaaf88fe"></a>

### `strcspn()`

```c
size_t strcspn ( const char * s, const char * reject )
```

声明属性：`extern`。

<a id="a4bc5f273980fb0e81e0fc7a4dd3de87e"></a>

### `strerror()`

```c
char * strerror ( int errnum)
```

声明属性：`extern`。

<a id="a080c6052ea267026d0baa316f8610b46"></a>

### `strerror_r()`

```c
int strerror_r ( int errnum, char * strerrbuf, size_t buflen )
```

声明属性：`extern`。

<a id="aa383452fe445bfae989358c9d7d96f4f"></a>

### `strlen()`

```c
size_t strlen ( const char * s)
```

声明属性：`extern`。

<a id="a32dff100d3a0806b158b13bbe60710af"></a>

### `strncat()`

```c
char * strncat ( char *ZRESTRICT dest, const char *ZRESTRICT src, size_t n )
```

声明属性：`extern`。

<a id="a07f4a84c11c106e95c32b6ab509346ef"></a>

### `strncmp()`

```c
int strncmp ( const char * s1, const char * s2, size_t n )
```

声明属性：`extern`。

<a id="aa7003ae2e637e6eb92a4c5e7523848a5"></a>

### `strncpy()`

```c
char * strncpy ( char *ZRESTRICT d, const char *ZRESTRICT s, size_t n )
```

声明属性：`extern`。

<a id="afc92d2231e45d19988c7894aa2a07f0c"></a>

### `strnlen()`

```c
size_t strnlen ( const char * s, size_t maxlen )
```

声明属性：`extern`。

<a id="af87bb1cdc3d71abcd9aa0bd6d36e50a8"></a>

### `strrchr()`

```c
char * strrchr ( const char * s, int c )
```

声明属性：`extern`。

<a id="a900a0edfa51f601d479244f7451cedd1"></a>

### `strspn()`

```c
size_t strspn ( const char * s, const char * accept )
```

声明属性：`extern`。

<a id="adef2d6284e392701fd4149b344188ceb"></a>

### `strstr()`

```c
char * strstr ( const char * s, const char * find )
```

声明属性：`extern`。

<a id="a22af6fcfed68749460181f2077c34813"></a>

### `strtok_r()`

```c
char * strtok_r ( char * str, const char * sep, char ** state )
```

声明属性：`extern`。


## 472.3\_原页交叉引用（Cross References）

- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [查看此文件的源码。](../api_source_supplement_reference/P216_string.h_源码浏览.md)
- [state](P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [accept](P307_zephyr__posix__sys__socket.h_文件参考.md#a66e3de379c18201b21c889035ec54864)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P471_zephyr__dt-bindings__clock__stm32wl_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P473_____w__zephyr__zephyr__lib__libc__minimal__include__strings.h_文件参考.md)
