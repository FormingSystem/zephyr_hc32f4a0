---
id: learning.zephyr-docs.posix-system-model-reference.page-19
title: siginfo_t_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsiginfo__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_siginfo\_t\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsiginfo__t.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/posix_signal.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 19.1\_数据成员（Data Fields）

<a id="r_ad1b72421321261362dfc00d180d8de69"></a>

```c
void * si_addr
```

相关声明：[si_addr](#ad1b72421321261362dfc00d180d8de69)。

<a id="r_a6ce15e0f745b97a19ccbd075e9a6ce7d"></a>

```c
long si_band
```

相关声明：[si_band](#a6ce15e0f745b97a19ccbd075e9a6ce7d)。

<a id="r_aea6512792c4af9f46ba221e454b6e0a7"></a>

```c
union sigval si_value
```

相关声明：[sigval](P035_sigval_联合体.md)、[si_value](#aea6512792c4af9f46ba221e454b6e0a7)。

<a id="r_a6053bfd6db1f12a9678cf53ebfeae45d"></a>

```c
pid_t si_pid
```

相关声明：[pid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a114f9c2461df851d2ad00aad8dcfa3f7)、[si_pid](#a6053bfd6db1f12a9678cf53ebfeae45d)。

<a id="r_a1574f7a20201b3f6bf64c5091fd14845"></a>

```c
uid_t si_uid
```

相关声明：[uid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#afc544433253791fc5f87b8203c9b6e63)、[si_uid](#a1574f7a20201b3f6bf64c5091fd14845)。

<a id="r_a238821f6eb15317d3d7b10efef80b9c7"></a>

```c
int si_signo
```

相关声明：[si_signo](#a238821f6eb15317d3d7b10efef80b9c7)。

<a id="r_a0dd36ae3e9df589f5755f88c93671c2d"></a>

```c
int si_code
```

相关声明：[si_code](#a0dd36ae3e9df589f5755f88c93671c2d)。

<a id="r_ae840a8f2824bab1693577f19f4d0432d"></a>

```c
int si_errno
```

相关声明：[si_errno](#ae840a8f2824bab1693577f19f4d0432d)。

<a id="r_accaf16ba75f1d4efd2e76f1991dc2b56"></a>

```c
int si_status
```

相关声明：[si_status](#accaf16ba75f1d4efd2e76f1991dc2b56)。

## 19.2\_详细说明（Detailed Documentation）

<a id="ad1b72421321261362dfc00d180d8de69"></a>

### `si_addr`

```c
void* siginfo_t::si_addr
```

<a id="a6ce15e0f745b97a19ccbd075e9a6ce7d"></a>

### `si_band`

```c
long siginfo_t::si_band
```

<a id="a0dd36ae3e9df589f5755f88c93671c2d"></a>

### `si_code`

```c
int siginfo_t::si_code
```

<a id="ae840a8f2824bab1693577f19f4d0432d"></a>

### `si_errno`

```c
int siginfo_t::si_errno
```

<a id="a6053bfd6db1f12a9678cf53ebfeae45d"></a>

### `si_pid`

```c
pid_t siginfo_t::si_pid
```

<a id="a238821f6eb15317d3d7b10efef80b9c7"></a>

### `si_signo`

```c
int siginfo_t::si_signo
```

<a id="accaf16ba75f1d4efd2e76f1991dc2b56"></a>

### `si_status`

```c
int siginfo_t::si_status
```

<a id="a1574f7a20201b3f6bf64c5091fd14845"></a>

### `si_uid`

```c
uid_t siginfo_t::si_uid
```

<a id="aea6512792c4af9f46ba221e454b6e0a7"></a>

### `si_value`

```c
union sigval siginfo_t::si_value
```

本数据类型文档由以下文件生成：

- `zephyr/posix/posix_signal.h`

## 19.3\_原页交叉引用（Cross References）

- [zephyr/posix/posix_signal.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h_source.html)
- [sigval](P035_sigval_联合体.md)
- [pid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a114f9c2461df851d2ad00aad8dcfa3f7)
- [uid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#afc544433253791fc5f87b8203c9b6e63)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P018_sigevent_结构体.md) · [返回大纲](大纲.md) · [下一章](P020_sigset_t_结构体.md)
