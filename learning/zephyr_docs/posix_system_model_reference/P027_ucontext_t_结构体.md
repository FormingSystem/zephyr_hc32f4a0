---
id: learning.zephyr-docs.posix-system-model-reference.page-27
title: ucontext_t_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structucontext__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_ucontext\_t\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structucontext__t.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/posix_signal.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 27.1\_数据成员（Data Fields）

<a id="r_a7210eb8a464c276b9c68e749b3aa28f1"></a>

```c
struct ucontext * uc_link
```

相关声明：[uc_link](#a7210eb8a464c276b9c68e749b3aa28f1)。

<a id="r_aabde4c64c7bcf764e937361d8c341504"></a>

```c
sigset_t uc_sigmask
```

相关声明：[sigset_t](P020_sigset_t_结构体.md)、[uc_sigmask](#aabde4c64c7bcf764e937361d8c341504)。

<a id="r_a2dc143fa6b3f0fa8d0f27acbfaed0d9e"></a>

```c
stack_t uc_stack
```

相关声明：[stack_t](P021_stack_t_结构体.md)、[uc_stack](#a2dc143fa6b3f0fa8d0f27acbfaed0d9e)。

<a id="r_a7f8c7406758045ea8be9dd61831f16f2"></a>

```c
mcontext_t uc_mcontext
```

相关声明：[mcontext_t](https://docs.zephyrproject.org/latest/doxygen/html/structmcontext__t.html)、[uc_mcontext](#a7f8c7406758045ea8be9dd61831f16f2)。

## 27.2\_详细说明（Detailed Documentation）

<a id="a7210eb8a464c276b9c68e749b3aa28f1"></a>

### `uc_link`

```c
struct ucontext* ucontext_t::uc_link
```

<a id="a7f8c7406758045ea8be9dd61831f16f2"></a>

### `uc_mcontext`

```c
mcontext_t ucontext_t::uc_mcontext
```

<a id="aabde4c64c7bcf764e937361d8c341504"></a>

### `uc_sigmask`

```c
sigset_t ucontext_t::uc_sigmask
```

<a id="a2dc143fa6b3f0fa8d0f27acbfaed0d9e"></a>

### `uc_stack`

```c
stack_t ucontext_t::uc_stack
```

本数据类型文档由以下文件生成：

- `zephyr/posix/posix_signal.h`

## 27.3\_原页交叉引用（Cross References）

- [zephyr/posix/posix_signal.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h_source.html)
- [sigset_t](P020_sigset_t_结构体.md)
- [stack_t](P021_stack_t_结构体.md)
- [mcontext_t](https://docs.zephyrproject.org/latest/doxygen/html/structmcontext__t.html)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P026_tms_结构体.md) · [返回大纲](大纲.md) · [下一章](P028_utsname_结构体.md)
