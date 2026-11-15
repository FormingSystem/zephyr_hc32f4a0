---
id: learning.zephyr-docs.modem-wireless-model-reference.page-42
title: modem_backend_tty_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__backend__tty__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_modem\_backend\_tty\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__backend__tty__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/backend/tty.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 42.1\_数据成员（Data Fields）

<a id="r_a139e7e96f3b021f560fa5ef8aa4d9e9f"></a>

```c
const char * tty_path
```

相关声明：[tty_path](#a139e7e96f3b021f560fa5ef8aa4d9e9f)。

<a id="r_ae8dd6da28163e6f97549e13e750d939d"></a>

```c
k_thread_stack_t * stack
```

相关声明：[k_thread_stack_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)、[stack](#ae8dd6da28163e6f97549e13e750d939d)。

<a id="r_a74cb7ee08a116261b19d834000db5242"></a>

```c
size_t stack_size
```

相关声明：[stack_size](#a74cb7ee08a116261b19d834000db5242)。

## 42.2\_详细说明（Detailed Documentation）

<a id="ae8dd6da28163e6f97549e13e750d939d"></a>

### `stack`

```c
k_thread_stack_t* modem_backend_tty_config::stack
```

<a id="a74cb7ee08a116261b19d834000db5242"></a>

### `stack_size`

```c
size_t modem_backend_tty_config::stack_size
```

<a id="a139e7e96f3b021f560fa5ef8aa4d9e9f"></a>

### `tty_path`

```c
const char* modem_backend_tty_config::tty_path
```

本数据类型文档由以下文件生成：

- `zephyr/modem/backend/tty.h`

## 42.3\_原页交叉引用（Cross References）

- [zephyr/modem/backend/tty.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2tty_8h_source.html)
- [k_thread_stack_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P041_modem_backend_tty_结构体.md) · [返回大纲](大纲.md) · [下一章](P043_modem_backend_uart_结构体.md)
