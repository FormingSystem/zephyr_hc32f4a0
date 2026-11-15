---
id: learning.zephyr-docs.api-file-reference.page-391
title: ____w__zephyr__zephyr__lib__libc__minimal__include__signal.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/signal_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第391章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_lib\_\_libc\_\_minimal\_\_include\_\_signal.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/signal_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/posix_signal.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 391.1\_宏定义（Macros）

<a id="r_aa86c630133e5b5174ac970227b273446"></a>

```c
#define SIGABRT 6
```

相关声明：[SIGABRT](#aa86c630133e5b5174ac970227b273446)。

<a id="r_a7fbba29aec3e4a8daae12935299df92d"></a>

```c
#define SIGFPE 8
```

相关声明：[SIGFPE](#a7fbba29aec3e4a8daae12935299df92d)。

<a id="r_a4c9c5284f8c8d146bd7a93d25017fc62"></a>

```c
#define SIGILL 4
```

相关声明：[SIGILL](#a4c9c5284f8c8d146bd7a93d25017fc62)。

<a id="r_a487309e3e9e0527535644115204a639a"></a>

```c
#define SIGINT 2
```

相关声明：[SIGINT](#a487309e3e9e0527535644115204a639a)。

<a id="r_ae20b4f7171a09516ea73c9d2745bd596"></a>

```c
#define SIGSEGV 11
```

相关声明：[SIGSEGV](#ae20b4f7171a09516ea73c9d2745bd596)。

<a id="r_a682182a5e5f38fd61f4311501e9dac5d"></a>

```c
#define SIGTERM 15
```

相关声明：[SIGTERM](#a682182a5e5f38fd61f4311501e9dac5d)。

<a id="r_a27d5dc561093d6243542e6a2465bc0f8"></a>

```c
#define SIG_DFL ((sighandler_t)0)
```

相关声明：[SIG_DFL](#a27d5dc561093d6243542e6a2465bc0f8)、[sighandler_t](#a87cd503247b3afbb79788256ac093ad5)。

<a id="r_acf0e499b0ac946b366b4f47a3b3e8b9e"></a>

```c
#define SIG_IGN ((sighandler_t)1)
```

相关声明：[SIG_IGN](#acf0e499b0ac946b366b4f47a3b3e8b9e)、[sighandler_t](#a87cd503247b3afbb79788256ac093ad5)。

<a id="r_a3c330fbddd84bf34e65af370b11998d6"></a>

```c
#define SIG_ERR ((sighandler_t)(-1))
```

相关声明：[SIG_ERR](#a3c330fbddd84bf34e65af370b11998d6)、[sighandler_t](#a87cd503247b3afbb79788256ac093ad5)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 391.2\_类型定义（Typedefs）

<a id="r_af93df1c6eefeb62980b2a73387e24156"></a>

```c
typedef long sig_atomic_t
```

相关声明：[sig_atomic_t](#af93df1c6eefeb62980b2a73387e24156)。

<a id="r_a87cd503247b3afbb79788256ac093ad5"></a>

```c
typedef void(* sighandler_t) (int sig)
```

相关声明：[sighandler_t](#a87cd503247b3afbb79788256ac093ad5)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 391.3\_函数（Functions）

<a id="r_a5d326f119f87d0facaa662520f8c322a"></a>

```c
sighandler_t signal (int sig, sighandler_t handler)
```

相关声明：[sighandler_t](#a87cd503247b3afbb79788256ac093ad5)、[signal](#a5d326f119f87d0facaa662520f8c322a)、[sighandler_t](#a87cd503247b3afbb79788256ac093ad5)。

<a id="r_a08ba0dd26a850108a1746412faba2b21"></a>

```c
int raise (int sig)
```

相关声明：[raise](#a08ba0dd26a850108a1746412faba2b21)。

## 391.4\_详细说明（Detailed Documentation）

<a id="a27d5dc561093d6243542e6a2465bc0f8"></a>

### `SIG_DFL`

```c
#define SIG_DFL ((sighandler_t)0)
```

<a id="a3c330fbddd84bf34e65af370b11998d6"></a>

### `SIG_ERR`

```c
#define SIG_ERR ((sighandler_t)(-1))
```

<a id="acf0e499b0ac946b366b4f47a3b3e8b9e"></a>

### `SIG_IGN`

```c
#define SIG_IGN ((sighandler_t)1)
```

<a id="aa86c630133e5b5174ac970227b273446"></a>

### `SIGABRT`

```c
#define SIGABRT 6
```

<a id="a7fbba29aec3e4a8daae12935299df92d"></a>

### `SIGFPE`

```c
#define SIGFPE 8
```

<a id="a4c9c5284f8c8d146bd7a93d25017fc62"></a>

### `SIGILL`

```c
#define SIGILL 4
```

<a id="a487309e3e9e0527535644115204a639a"></a>

### `SIGINT`

```c
#define SIGINT 2
```

<a id="ae20b4f7171a09516ea73c9d2745bd596"></a>

### `SIGSEGV`

```c
#define SIGSEGV 11
```

<a id="a682182a5e5f38fd61f4311501e9dac5d"></a>

### `SIGTERM`

```c
#define SIGTERM 15
```

<a id="af93df1c6eefeb62980b2a73387e24156"></a>

### `sig_atomic_t`

```c
typedef long sig_atomic_t
```

<a id="a87cd503247b3afbb79788256ac093ad5"></a>

### `sighandler_t`

```c
typedef void(* sighandler_t) (int sig)
```

<a id="a08ba0dd26a850108a1746412faba2b21"></a>

### `raise()`

```c
int raise ( int sig)
```

<a id="a5d326f119f87d0facaa662520f8c322a"></a>

### `signal()`

```c
sighandler_t signal ( int sig, sighandler_t handler )
```


## 391.5\_原页交叉引用（Cross References）

- [zephyr/posix/posix_signal.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P784_signal.h_源码浏览.md)
- [sighandler_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a87cd503247b3afbb79788256ac093ad5)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P390_zephyr__dt-bindings__pinctrl__sifive-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P392_zephyr__dt-bindings__comparator__silabs-acmp.h_文件参考.md)
