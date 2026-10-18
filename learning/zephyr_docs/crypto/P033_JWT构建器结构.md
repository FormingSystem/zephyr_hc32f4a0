---
id: learning.zephyr-docs.crypto.api-33
title: JWT构建器结构
kind: reference
status: maintained
domains: [zephyr, crypto, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structjwt__builder.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_JWT构建器结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structjwt__builder.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 33.1\_阅读说明与来源

译注：配合[JSON Web Token 指南](P029_JSONWebToken指南.md)阅读。这里的构建器（Builder）生成包含固定声明（Claims）并经过签名的 JWT，接口没有提供任意声明编辑、令牌解析或验证功能。

本组：[JWT构建与签名接口](P030_JWT构建与签名接口.md) · [JWT头文件](P031_JWT头文件.md) · [JWT头文件源码](P032_JWT头文件源码.md) · [JWT构建器结构](P033_JWT构建器结构.md)。

JWT 数据跟踪（Data Tracking）。

```c
#include <zephyr/data/jwt.h>
```

JWT 数据跟踪。JSON Web 令牌由若干部分组成，每部分都使用 Base64URL 编码。此结构跟踪令牌构建过程，包括可用空间大小的限制；应使用 `jwt_init_builder()` 初始化。

## 33.2\_数据成员（Data Fields）

<a id="r_a23a0aa512e5bc66722b6d7a8cf20aa95"></a>

```c
char * base
```

正在写入的缓冲区的起始位置。

<a id="r_a74a3d3e645f8b438bcdf12abdf0aabf7"></a>

```c
char * buf
```

此缓冲区中当前的写入位置。

<a id="r_a8fcc85d6704b63cd773397a5a4d9774d"></a>

```c
size_t len
```

`buf` 中剩余的可用空间。

<a id="r_af53cb40609f623b95ff68d3c66a387ce"></a>

```c
bool overflowed
```

尝试写入超出缓冲区末尾的位置时设置的标志。

<a id="r_a4bd0376eef7f162e9e9e1e1399388fed"></a>

```c
unsigned char wip [3]
```



<a id="r_a7e4880c8fc8136083bad0ef2559c67e4"></a>

```c
int pending
```



## 33.3\_详细说明（Detailed Documentation）

<a id="a23a0aa512e5bc66722b6d7a8cf20aa95"></a>

### `base`

```c
char* jwt_builder::base
```

正在写入的缓冲区的起始位置。

<a id="a74a3d3e645f8b438bcdf12abdf0aabf7"></a>

### `buf`

```c
char* jwt_builder::buf
```

此缓冲区中当前的写入位置。

> 译注（源码核对）：这是随构建推进的当前写入指针，完整令牌应从最初的缓冲区或 `base` 读取，不能把末尾写入指针当作令牌起点。

<a id="a8fcc85d6704b63cd773397a5a4d9774d"></a>

### `len`

```c
size_t jwt_builder::len
```

`buf` 中剩余的可用空间。

> 译注（源码核对）：这是剩余容量，不是已经生成的令牌长度。完整输出还需容纳末尾空字符。

<a id="af53cb40609f623b95ff68d3c66a387ce"></a>

### `overflowed`

```c
bool jwt_builder::overflowed
```

尝试写入超出缓冲区末尾的位置时设置的标志。

此标志一旦置位，令牌就无效。

> 译注（源码核对）：溢出标志置位后，当前编码器停止继续追加字符；缓冲区即使仍以空字符结尾，也可能只是截断内容，不能当作有效 JWT 使用。

<a id="a7e4880c8fc8136083bad0ef2559c67e4"></a>

### `pending`

```c
int jwt_builder::pending
```

<a id="a4bd0376eef7f162e9e9e1e1399388fed"></a>

### `wip`

```c
unsigned char jwt_builder::wip[3]
```

## 33.4\_相关源码与使用边界

本仓库的[JWT 头文件](../../../include/zephyr/data/jwt.h)与[构建实现](../../../subsys/jwt/jwt.c)可用于源码追踪，版本可能与官网 `latest` 不同。译注核对依据为保存的[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/data/jwt.h)、[官方构建实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/jwt/jwt.c)与[PSA 签名后端](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/jwt/jwt_psa.c)，摘要见[来源记录](../SOURCES.md)。

> 译注：`wip[3]` 和 `pending` 是当前头文件还包含的 Base64URL 编码状态字段，其普通注释未出现在本页成员说明中；可在[头文件源码](P032_JWT头文件源码.md)查看。应用应调用初始化函数并保留整个构建器状态，不自行改动这些内部编码字段。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P032_JWT头文件源码.md) · [返回大纲](大纲.md)
