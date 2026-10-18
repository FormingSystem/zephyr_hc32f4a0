---
id: learning.zephyr-docs.posix-system-model-reference.page-28
title: utsname_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structutsname.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_utsname\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structutsname.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/sys/utsname.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 28.1\_数据成员（Data Fields）

<a id="r_a8bfca811eed8101b2310200a96e9757e"></a>

```c
char sysname [sizeof("Zephyr")]
```

相关声明：[sysname](#a8bfca811eed8101b2310200a96e9757e)。

<a id="r_afc4ee8a38fc0d85ac4f8fe1b669c3f74"></a>

```c
char nodename [COND_CODE_1(CONFIG_POSIX_SINGLE_PROCESS,(CONFIG_POSIX_UNAME_VERSION_LEN),(0))+1]
```

相关声明：[nodename](#afc4ee8a38fc0d85ac4f8fe1b669c3f74)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)。

<a id="r_afcc31cc768b481d10c887dcf56d64a1c"></a>

```c
char release [sizeof("99.99.99-rc1")]
```

相关声明：[release](#afcc31cc768b481d10c887dcf56d64a1c)。

<a id="r_abe146e9be86c55a25881e6c58ba3ddf0"></a>

```c
char version [COND_CODE_1(CONFIG_POSIX_SINGLE_PROCESS,(CONFIG_POSIX_UNAME_VERSION_LEN),(0))+1]
```

相关声明：[version](#abe146e9be86c55a25881e6c58ba3ddf0)、[COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)。

<a id="r_a708b512fcd536a51fa7266899eec3964"></a>

```c
char machine [sizeof(CONFIG_ARCH)]
```

相关声明：[machine](#a708b512fcd536a51fa7266899eec3964)。

## 28.2\_详细说明（Detailed Documentation）

<a id="a708b512fcd536a51fa7266899eec3964"></a>

### `machine`

```c
char utsname::machine[sizeof(CONFIG_ARCH)]
```

<a id="afc4ee8a38fc0d85ac4f8fe1b669c3f74"></a>

### `nodename`

```c
char utsname::nodename[COND_CODE_1(CONFIG_POSIX_SINGLE_PROCESS,(CONFIG_POSIX_UNAME_VERSION_LEN),(0))+1]
```

<a id="afcc31cc768b481d10c887dcf56d64a1c"></a>

### `release`

```c
char utsname::release[sizeof("99.99.99-rc1")]
```

<a id="a8bfca811eed8101b2310200a96e9757e"></a>

### `sysname`

```c
char utsname::sysname[sizeof("Zephyr")]
```

<a id="abe146e9be86c55a25881e6c58ba3ddf0"></a>

### `version`

```c
char utsname::version[COND_CODE_1(CONFIG_POSIX_SINGLE_PROCESS,(CONFIG_POSIX_UNAME_VERSION_LEN),(0))+1]
```

本数据类型文档由以下文件生成：

- `zephyr/posix/sys/utsname.h`

## 28.3\_原页交叉引用（Cross References）

- [zephyr/posix/sys/utsname.h](https://docs.zephyrproject.org/latest/doxygen/html/utsname_8h_source.html)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P027_ucontext_t_结构体.md) · [返回大纲](大纲.md) · [下一章](P029_zsock_addrinfo_结构体.md)
