---
id: learning.zephyr-docs.posix-system-model-reference.page-21
title: stack_t_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structstack__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_stack\_t\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structstack__t.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/posix_signal.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 21.1\_数据成员（Data Fields）

<a id="r_a4e768ba748dc571d736f38cbb138f8e6"></a>

```c
void * ss_sp
```

相关声明：[ss_sp](#a4e768ba748dc571d736f38cbb138f8e6)。

<a id="r_ae3df42e1671d5e8861bca62318fb063f"></a>

```c
size_t ss_size
```

相关声明：[ss_size](#ae3df42e1671d5e8861bca62318fb063f)。

<a id="r_a72825bf6898b7e0bc0b916b220440d9e"></a>

```c
int ss_flags
```

相关声明：[ss_flags](#a72825bf6898b7e0bc0b916b220440d9e)。

## 21.2\_详细说明（Detailed Documentation）

<a id="a72825bf6898b7e0bc0b916b220440d9e"></a>

### `ss_flags`

```c
int stack_t::ss_flags
```

<a id="ae3df42e1671d5e8861bca62318fb063f"></a>

### `ss_size`

```c
size_t stack_t::ss_size
```

<a id="a4e768ba748dc571d736f38cbb138f8e6"></a>

### `ss_sp`

```c
void* stack_t::ss_sp
```

本数据类型文档由以下文件生成：

- `zephyr/posix/posix_signal.h`

## 21.3\_原页交叉引用（Cross References）

- [zephyr/posix/posix_signal.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h_source.html)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P020_sigset_t_结构体.md) · [返回大纲](大纲.md) · [下一章](P022_stat_结构体.md)
