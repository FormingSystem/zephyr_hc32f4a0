---
id: learning.zephyr-docs.posix-system-model-reference.page-18
title: sigevent_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsigevent.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_sigevent\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsigevent.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/posix_signal.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

<a id="r_a5a687d2092b237d76eb08e2d46a5115f"></a>

```c
pthread_attr_t * sigev_notify_attributes
```

相关声明：[pthread_attr_t](P011_pthread_attr_t_结构体.md)、[sigev_notify_attributes](#a5a687d2092b237d76eb08e2d46a5115f)。

<a id="r_a0b3b43507546409ccc399a918942aba5"></a>

```c
void(* sigev_notify_function )(union sigval value)
```

相关声明：[sigev_notify_function](#a0b3b43507546409ccc399a918942aba5)、[sigval](P035_sigval_联合体.md)。

<a id="r_a757af1e34b87e3f66bbc08c514017a2c"></a>

```c
union sigval sigev_value
```

相关声明：[sigval](P035_sigval_联合体.md)、[sigev_value](#a757af1e34b87e3f66bbc08c514017a2c)。

<a id="r_aae9a19d879c38e0c4e8a9bf738c5081e"></a>

```c
int sigev_notify
```

相关声明：[sigev_notify](#aae9a19d879c38e0c4e8a9bf738c5081e)。

<a id="r_a5c645ec1d12bb46efc3f4097c52b665d"></a>

```c
int sigev_signo
```

相关声明：[sigev_signo](#a5c645ec1d12bb46efc3f4097c52b665d)。

## 18.2\_详细说明（Detailed Documentation）

<a id="aae9a19d879c38e0c4e8a9bf738c5081e"></a>

### `sigev_notify`

```c
int sigevent::sigev_notify
```

<a id="a5a687d2092b237d76eb08e2d46a5115f"></a>

### `sigev_notify_attributes`

```c
pthread_attr_t* sigevent::sigev_notify_attributes
```

<a id="a0b3b43507546409ccc399a918942aba5"></a>

### `sigev_notify_function`

```c
void(* sigevent::sigev_notify_function) (union sigval value)
```

<a id="a5c645ec1d12bb46efc3f4097c52b665d"></a>

### `sigev_signo`

```c
int sigevent::sigev_signo
```

<a id="a757af1e34b87e3f66bbc08c514017a2c"></a>

### `sigev_value`

```c
union sigval sigevent::sigev_value
```

本数据类型文档由以下文件生成：

- `zephyr/posix/posix_signal.h`

## 18.3\_原页交叉引用（Cross References）

- [zephyr/posix/posix_signal.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h_source.html)
- [pthread_attr_t](P011_pthread_attr_t_结构体.md)
- [sigval](P035_sigval_联合体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_sigaction_结构体.md) · [返回大纲](大纲.md) · [下一章](P019_siginfo_t_结构体.md)
