---
id: learning.zephyr-docs.api-file-service-interface-reference.page-49
title: zephyr__sys__sys_getopt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_zephyr\_\_sys\_\_sys\_getopt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sys__getopt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/kernel.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 49.1\_数据结构（Data Structures）

<a id="r_sys_5Fgetopt_5Fstate"></a>

```c
struct sys_getopt_state
```

相关声明：[sys_getopt_state](../kernel_runtime_model_reference/P016_sys_getopt_state_结构体.md)。

<a id="r_sys_5Fgetopt_5Foption"></a>

```c
struct sys_getopt_option
```

相关声明：[sys_getopt_option](../kernel_runtime_model_reference/P015_sys_getopt_option_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 49.2\_宏定义（Macros）

<a id="r_afcb3049e8d35509f0631d7d932f997db"></a>

```c
#define sys_getopt_no_argument 0
```

相关声明：[sys_getopt_no_argument](#afcb3049e8d35509f0631d7d932f997db)。

<a id="r_a51e2c2b48a1f03ffab489975ec1cbe2c"></a>

```c
#define sys_getopt_required_argument 1
```

相关声明：[sys_getopt_required_argument](#a51e2c2b48a1f03ffab489975ec1cbe2c)。

<a id="r_abd69aabac0c16b413b9c9c38786608b0"></a>

```c
#define sys_getopt_optional_argument 2
```

相关声明：[sys_getopt_optional_argument](#abd69aabac0c16b413b9c9c38786608b0)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 49.3\_函数（Functions）

<a id="r_a8339f5cdb7f036bec15e4a4a3b2fff20"></a>

```c
void sys_getopt_init (void)
```

相关声明：[sys_getopt_init](#a8339f5cdb7f036bec15e4a4a3b2fff20)。

<a id="r_a84af076f38140c6f7bc6c4797c96c157"></a>

```c
struct sys_getopt_state * sys_getopt_state_get (void)
```

相关声明：[sys_getopt_state](../kernel_runtime_model_reference/P016_sys_getopt_state_结构体.md)、[sys_getopt_state_get](#a84af076f38140c6f7bc6c4797c96c157)。

<a id="r_a35ad483c9371f3e0fd71813c3f2f39d2"></a>

```c
int sys_getopt (int nargc, char *const nargv[], const char *ostr)
```

相关声明：[sys_getopt](#a35ad483c9371f3e0fd71813c3f2f39d2)。

解析命令行参数（Command-line Arguments）。

<a id="r_a585cba391f737a7db7247a55f964ec38"></a>

```c
int sys_getopt_long (int nargc, char *const *nargv, const char *options, const struct sys_getopt_option *long_options, int *idx)
```

相关声明：[sys_getopt_long](#a585cba391f737a7db7247a55f964ec38)、[sys_getopt_option](../kernel_runtime_model_reference/P015_sys_getopt_option_结构体.md)。

解析命令行参数（Command-line Arguments）。

<a id="r_a823ee9bebc991cbb0f58f805c2df768d"></a>

```c
int sys_getopt_long_only (int nargc, char *const *nargv, const char *options, const struct sys_getopt_option *long_options, int *idx)
```

相关声明：[sys_getopt_long_only](#a823ee9bebc991cbb0f58f805c2df768d)、[sys_getopt_option](../kernel_runtime_model_reference/P015_sys_getopt_option_结构体.md)。

解析命令行参数（Command-line Arguments）。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 49.4\_变量（Variables）

<a id="r_a46ac8783a520db9faf201bfee4179d58"></a>

```c
int sys_getopt_optreset
```

相关声明：[sys_getopt_optreset](#a46ac8783a520db9faf201bfee4179d58)。

<a id="r_a091f245c08065a360b765b06a4bb3ec8"></a>

```c
char * sys_getopt_optarg
```

相关声明：[sys_getopt_optarg](#a091f245c08065a360b765b06a4bb3ec8)。

<a id="r_a162f907a30748f8e5b7bfed601c5723b"></a>

```c
int sys_getopt_opterr
```

相关声明：[sys_getopt_opterr](#a162f907a30748f8e5b7bfed601c5723b)。

<a id="r_aa259f622c6daa9a421e2542bc63bc29d"></a>

```c
int sys_getopt_optind
```

相关声明：[sys_getopt_optind](#aa259f622c6daa9a421e2542bc63bc29d)。

<a id="r_ae363b8a3a593e215292522d3ffd9839d"></a>

```c
int sys_getopt_optopt
```

相关声明：[sys_getopt_optopt](#ae363b8a3a593e215292522d3ffd9839d)。

## 49.5\_详细说明（Detailed Documentation）

<a id="afcb3049e8d35509f0631d7d932f997db"></a>

### `sys_getopt_no_argument`

```c
#define sys_getopt_no_argument 0
```

<a id="abd69aabac0c16b413b9c9c38786608b0"></a>

### `sys_getopt_optional_argument`

```c
#define sys_getopt_optional_argument 2
```

<a id="a51e2c2b48a1f03ffab489975ec1cbe2c"></a>

### `sys_getopt_required_argument`

```c
#define sys_getopt_required_argument 1
```

<a id="a35ad483c9371f3e0fd71813c3f2f39d2"></a>

### `sys_getopt()`

```c
int sys_getopt ( int nargc, char *const nargv[], const char * ostr )
```

解析命令行参数（Command-line Arguments）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] nargc` | 参数数量（Argument Count）。 |
| `[in] nargv` | 参数（Arguments）。 |
| `[in] ostr` | 包含合法选项字符（Option Characters）的字符串。 |

**说明（Note）**：**注意（Note）：**本函数基于 FreeBSD 实现，但不支持环境变量 `POSIXLY_CORRECT`。

**返回（Returns）**：**返回值（Returns）：**成功找到选项时，返回该选项字符（Option Character）。

<a id="a8339f5cdb7f036bec15e4a4a3b2fff20"></a>

### `sys_getopt_init()`

```c
void sys_getopt_init ( void )
```

<a id="a585cba391f737a7db7247a55f964ec38"></a>

### `sys_getopt_long()`

```c
int sys_getopt_long ( int nargc, char *const * nargv, const char * options, const struct sys_getopt_option * long_options, int * idx )
```

解析命令行参数（Command-line Arguments）。

`sys_getopt_long()` 的工作方式与 `sys_getopt()` 相同，但还接受以两个连字符开头的长选项（Long Options）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] nargc` | 参数数量（Argument Count）。 |
| `[in] nargv` | 参数（Arguments）。 |
| `[in] options` | 包含合法选项字符（Option Characters）的字符串。 |
| `[in] long_options` | 指向 `struct sys_getopt_option` 数组首元素的指针。 |
| `[in] idx` | 若 `idx` 不为 `NULL`，则指向一个变量，该变量将被设为所匹配长选项相对于 `long_options` 的索引。 |

**说明（Note）**：**注意（Note）：**本函数基于 FreeBSD 实现，但不支持环境变量 `POSIXLY_CORRECT`。

**返回（Returns）**：**返回值（Returns）：**成功找到选项时，返回该选项字符（Option Character）。

<a id="a823ee9bebc991cbb0f58f805c2df768d"></a>

### `sys_getopt_long_only()`

```c
int sys_getopt_long_only ( int nargc, char *const * nargv, const char * options, const struct sys_getopt_option * long_options, int * idx )
```

解析命令行参数（Command-line Arguments）。

`sys_getopt_long_only()` 的工作方式与 `sys_getopt_long()` 相同，但 `-` 和 `--` 均可表示长选项（Long Option）。若以 `-` 而非 `--` 开头的选项不匹配长选项，却匹配短选项（Short Option），则将其解析为短选项。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] nargc` | 参数数量（Argument Count）。 |
| `[in] nargv` | 参数（Arguments）。 |
| `[in] options` | 包含合法选项字符（Option Characters）的字符串。 |
| `[in] long_options` | 指向 `struct sys_getopt_option` 数组首元素的指针。 |
| `[in] idx` | 若 `idx` 不为 `NULL`，则指向一个变量，该变量将被设为所匹配长选项相对于 `long_options` 的索引。 |

**说明（Note）**：**注意（Note）：**本函数基于 FreeBSD 实现，但不支持环境变量 `POSIXLY_CORRECT`。

**返回（Returns）**：**返回值（Returns）：**成功找到选项时，返回该选项字符（Option Character）。

<a id="a84af076f38140c6f7bc6c4797c96c157"></a>

### `sys_getopt_state_get()`

```c
struct sys_getopt_state * sys_getopt_state_get ( void )
```

<a id="a091f245c08065a360b765b06a4bb3ec8"></a>

### `sys_getopt_optarg`

```c
char* sys_getopt_optarg
```

声明属性：`extern`。

<a id="a162f907a30748f8e5b7bfed601c5723b"></a>

### `sys_getopt_opterr`

```c
int sys_getopt_opterr
```

声明属性：`extern`。

<a id="aa259f622c6daa9a421e2542bc63bc29d"></a>

### `sys_getopt_optind`

```c
int sys_getopt_optind
```

声明属性：`extern`。

<a id="ae363b8a3a593e215292522d3ffd9839d"></a>

### `sys_getopt_optopt`

```c
int sys_getopt_optopt
```

声明属性：`extern`。

<a id="a46ac8783a520db9faf201bfee4179d58"></a>

### `sys_getopt_optreset`

```c
int sys_getopt_optreset
```

声明属性：`extern`。


## 49.6\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](../api_source_timing_sensor_reference/P012_sys_getopt.h_源码浏览.md)
- [sys_getopt_state](../kernel_runtime_model_reference/P016_sys_getopt_state_结构体.md)
- [sys_getopt_option](../kernel_runtime_model_reference/P015_sys_getopt_option_结构体.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="doc-var-members"></a>
<a id="header-doc-var-members"></a>

---

[上一章](P048_zephyr__net__ssh__server.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P050_zephyr__drivers__mfd__tla2528.h_文件参考.md)
