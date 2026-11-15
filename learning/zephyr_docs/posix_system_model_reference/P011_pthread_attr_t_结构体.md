---
id: learning.zephyr-docs.posix-system-model-reference.page-11
title: pthread_attr_t_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpthread__attr__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_pthread\_attr\_t\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpthread__attr__t.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/posix_signal.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_a24c790e83123e988fc8fdeb7c7ad9325"></a>

```c
void * stack
```

相关声明：[stack](#a24c790e83123e988fc8fdeb7c7ad9325)。

<a id="r_a83d718349c0b2f1d93e103fa7cc1dac4"></a>

```c
unsigned int details [2]
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[details](#a83d718349c0b2f1d93e103fa7cc1dac4)。

## 11.2\_详细说明（Detailed Documentation）

<a id="a83d718349c0b2f1d93e103fa7cc1dac4"></a>

### `details`

```c
unsigned int pthread_attr_t::details
```

<a id="a24c790e83123e988fc8fdeb7c7ad9325"></a>

### `stack`

```c
void * pthread_attr_t::stack
```

本数据类型文档由以下文件生成：

- `zephyr/posix/posix_signal.h`
- `zephyr/posix/posix_types.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/posix/posix_signal.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h_source.html)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_protoent_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_pthread_barrierattr_结构体.md)
