---
id: learning.zephyr-docs.posix-system-model-reference.page-9
title: passwd_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpasswd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_passwd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpasswd.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/pwd.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

<a id="r_a6de92e6d2e3dd348ee82472d2b219556"></a>

```c
char * pw_name
```

相关声明：[pw_name](#a6de92e6d2e3dd348ee82472d2b219556)。

<a id="r_aa6e0e62ee3cf5152f2697a0104f627c1"></a>

```c
uid_t pw_uid
```

相关声明：[uid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#afc544433253791fc5f87b8203c9b6e63)、[pw_uid](#aa6e0e62ee3cf5152f2697a0104f627c1)。

<a id="r_aefbacfb7dc7f7f47313d08707253e4c6"></a>

```c
gid_t pw_gid
```

相关声明：[gid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a3a7834be1a79bb0c5a65d3546c2e3bd8)、[pw_gid](#aefbacfb7dc7f7f47313d08707253e4c6)。

<a id="r_afa7bb51f592e9199dc776ccc763352a7"></a>

```c
char * pw_dir
```

相关声明：[pw_dir](#afa7bb51f592e9199dc776ccc763352a7)。

<a id="r_aa0584dc9fdf7920c25b6326b5fdb5416"></a>

```c
char * pw_shell
```

相关声明：[pw_shell](#aa0584dc9fdf7920c25b6326b5fdb5416)。

## 9.2\_详细说明（Detailed Documentation）

<a id="afa7bb51f592e9199dc776ccc763352a7"></a>

### `pw_dir`

```c
char* passwd::pw_dir
```

<a id="aefbacfb7dc7f7f47313d08707253e4c6"></a>

### `pw_gid`

```c
gid_t passwd::pw_gid
```

<a id="a6de92e6d2e3dd348ee82472d2b219556"></a>

### `pw_name`

```c
char* passwd::pw_name
```

<a id="aa0584dc9fdf7920c25b6326b5fdb5416"></a>

### `pw_shell`

```c
char* passwd::pw_shell
```

<a id="aa6e0e62ee3cf5152f2697a0104f627c1"></a>

### `pw_uid`

```c
uid_t passwd::pw_uid
```

本数据类型文档由以下文件生成：

- `zephyr/posix/pwd.h`

## 9.3\_原页交叉引用（Cross References）

- [zephyr/posix/pwd.h](https://docs.zephyrproject.org/latest/doxygen/html/pwd_8h_source.html)
- [uid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#afc544433253791fc5f87b8203c9b6e63)
- [gid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a3a7834be1a79bb0c5a65d3546c2e3bd8)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_netent_结构体.md) · [返回大纲](大纲.md) · [下一章](P010_protoent_结构体.md)
