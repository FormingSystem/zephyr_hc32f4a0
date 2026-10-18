---
id: learning.zephyr-docs.modem-wireless-model-reference.page-41
title: modem_backend_tty_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__backend__tty.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_modem\_backend\_tty\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__backend__tty.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/backend/tty.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 41.1\_数据成员（Data Fields）

<a id="r_af6a76d369957f01f9d44c7f4bba67642"></a>

```c
const char * tty_path
```

相关声明：[tty_path](#af6a76d369957f01f9d44c7f4bba67642)。

<a id="r_abf93189b2640afa8bad440089bb1a863"></a>

```c
int tty_fd
```

相关声明：[tty_fd](#abf93189b2640afa8bad440089bb1a863)。

<a id="r_abe654bb7b24f23417e60bc8af7b73d36"></a>

```c
struct modem_pipe pipe
```

相关声明：[pipe](#abe654bb7b24f23417e60bc8af7b73d36)。

<a id="r_ad454321f08f334b028bb63cbb0d8e8f6"></a>

```c
struct k_thread thread
```

相关声明：[k_thread](../thread_core_reference/P004_线程对象结构.md)、[thread](#ad454321f08f334b028bb63cbb0d8e8f6)。

<a id="r_a23afe812c5951bfa41251610056aa3aa"></a>

```c
k_thread_stack_t * stack
```

相关声明：[k_thread_stack_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)、[stack](#a23afe812c5951bfa41251610056aa3aa)。

<a id="r_a2ea8d323973de8423f558a7a2e6b8984"></a>

```c
size_t stack_size
```

相关声明：[stack_size](#a2ea8d323973de8423f558a7a2e6b8984)。

<a id="r_a7f85f1f41fbcdf69ad1846a3af1b0b1e"></a>

```c
atomic_t state
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[state](#a7f85f1f41fbcdf69ad1846a3af1b0b1e)。

## 41.2\_详细说明（Detailed Documentation）

<a id="abe654bb7b24f23417e60bc8af7b73d36"></a>

### `pipe`

```c
struct modem_pipe modem_backend_tty::pipe
```

<a id="a23afe812c5951bfa41251610056aa3aa"></a>

### `stack`

```c
k_thread_stack_t* modem_backend_tty::stack
```

<a id="a2ea8d323973de8423f558a7a2e6b8984"></a>

### `stack_size`

```c
size_t modem_backend_tty::stack_size
```

<a id="a7f85f1f41fbcdf69ad1846a3af1b0b1e"></a>

### `state`

```c
atomic_t modem_backend_tty::state
```

<a id="ad454321f08f334b028bb63cbb0d8e8f6"></a>

### `thread`

```c
struct k_thread modem_backend_tty::thread
```

<a id="abf93189b2640afa8bad440089bb1a863"></a>

### `tty_fd`

```c
int modem_backend_tty::tty_fd
```

<a id="af6a76d369957f01f9d44c7f4bba67642"></a>

### `tty_path`

```c
const char* modem_backend_tty::tty_path
```

本数据类型文档由以下文件生成：

- `zephyr/modem/backend/tty.h`

## 41.3\_原页交叉引用（Cross References）

- [zephyr/modem/backend/tty.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2tty_8h_source.html)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [k_thread_stack_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P040_mdm_hl7800_site_survey_结构体.md) · [返回大纲](大纲.md) · [下一章](P042_modem_backend_tty_config_结构体.md)
