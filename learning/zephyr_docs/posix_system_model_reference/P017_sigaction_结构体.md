---
id: learning.zephyr-docs.posix-system-model-reference.page-17
title: sigaction_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsigaction.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_sigaction\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsigaction.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/posix_signal.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 17.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a2b88033fc8788f2e1d9f605c0ce6b89f"></a>

```c
void(* sa_handler )(int sig)
```

相关声明：[sa_handler](#ac794783ce745372a2cd61fd0ec93b4d7)。

<a id="r_af9c5ae637005509eaf07263b6fa1da8b"></a>

```c
void(* sa_sigaction )(int sig, siginfo_t *info, void *context)
```

相关声明：[sa_sigaction](#a1830265abeb7454d61dbf1104bdef231)、[siginfo_t](P019_siginfo_t_结构体.md)。

<a id="r_a7795d4c47ea06f73f579e42ba2768fdb"></a>

```c
};
```

<a id="r_a684e70081d03d46ce70af097ea5cfd49"></a>

```c
sigset_t sa_mask
```

相关声明：[sigset_t](P020_sigset_t_结构体.md)、[sa_mask](#a684e70081d03d46ce70af097ea5cfd49)。

<a id="r_aea0dabe7a03641c8b426521f4406b425"></a>

```c
int sa_flags
```

相关声明：[sa_flags](#aea0dabe7a03641c8b426521f4406b425)。

## 17.2\_详细说明（Detailed Documentation）

<a id="a7795d4c47ea06f73f579e42ba2768fdb"></a>

### `[union]`

```c
union { ... } sigaction
```

<a id="aea0dabe7a03641c8b426521f4406b425"></a>

### `sa_flags`

```c
int sigaction::sa_flags
```

<a id="ac794783ce745372a2cd61fd0ec93b4d7"></a>

### `sa_handler`

```c
void(* sigaction::sa_handler) (int sig)
```

<a id="a684e70081d03d46ce70af097ea5cfd49"></a>

### `sa_mask`

```c
sigset_t sigaction::sa_mask
```

<a id="a1830265abeb7454d61dbf1104bdef231"></a>

### `sa_sigaction`

```c
void(* sigaction::sa_sigaction) (int sig, siginfo_t *info, void *context)
```

本数据类型文档由以下文件生成：

- `zephyr/posix/posix_signal.h`

## 17.3\_原页交叉引用（Cross References）

- [zephyr/posix/posix_signal.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h_source.html)
- [siginfo_t](P019_siginfo_t_结构体.md)
- [sigset_t](P020_sigset_t_结构体.md)
- [sigaction](P017_sigaction_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P016_servent_结构体.md) · [返回大纲](大纲.md) · [下一章](P018_sigevent_结构体.md)
