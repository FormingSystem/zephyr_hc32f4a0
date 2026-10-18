---
id: learning.zephyr-docs.crypto.api-30
title: JWT构建与签名接口
kind: reference
status: maintained
domains: [zephyr, crypto, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__jwt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_JWT构建与签名接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__jwt.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 30.1\_阅读说明与来源

译注：配合[JSON Web Token 指南](P029_JSONWebToken指南.md)阅读。这里的构建器（Builder）生成包含固定声明（Claims）并经过签名的 JWT，接口没有提供任意声明编辑、令牌解析或验证功能。

本组：[JWT构建与签名接口](P030_JWT构建与签名接口.md) · [JWT头文件](P031_JWT头文件.md) · [JWT头文件源码](P032_JWT头文件源码.md) · [JWT构建器结构](P033_JWT构建器结构.md)。

JSON Web 令牌（JSON Web Token，JWT），定义见 RFC 7519。

JSON Web 令牌（JSON Web Token，JWT），定义见 RFC 7519。

## 30.2\_数据结构（Data Structures）

<a id="r_jwt_5Fbuilder"></a>

```c
struct jwt_builder
```

JWT 数据跟踪（Data Tracking）。

相关声明：[jwt_builder](P033_JWT构建器结构.md)。

## 30.3\_函数（Functions）

<a id="r_gab10ee40ee3c0b3eea98051c2acbb8a75"></a>

```c
int jwt_init_builder (struct jwt_builder *builder, char *buffer, size_t buffer_size)
```

初始化 JWT 构建器（Builder）。

相关声明：[jwt_builder](P033_JWT构建器结构.md)。

<a id="r_ga209dc2bdbaf72b4c9d11be02e0ffe479"></a>

```c
int jwt_add_payload (struct jwt_builder *builder, int32_t exp, int32_t iat, const char *aud)
```

添加 JWT 载荷（Payload）。

相关声明：[jwt_builder](P033_JWT构建器结构.md)。

<a id="r_gaa000189c83e9b9113f401cd7d523cefe"></a>

```c
int jwt_sign (struct jwt_builder *builder, const char *der_key, size_t der_key_len)
```

对 JWT 进行签名（Sign）。

相关声明：[jwt_builder](P033_JWT构建器结构.md)。

## 30.4\_详细说明（Detailed Documentation）

<a id="ga209dc2bdbaf72b4c9d11be02e0ffe479"></a>

### `jwt_add_payload()`

```c
int jwt_add_payload ( struct jwt_builder * builder, int32_t exp, int32_t iat, const char * aud )
```

```c
#include <zephyr/data/jwt.h>
```

添加 JWT 载荷（Payload）。

向先前初始化的构建器添加 JWT 载荷，包含以下字段：

这些字段的详细信息见 RFC 7519 第 4.1 节。

- 过期时间（Expiration Time）。
- 签发时间（Issued At）。
- 受众（Audience）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `builder` | 先前已经初始化的构建器。 |
| `exp` | 过期时间（Expiration Time），以纪元时间（Epoch）格式表示。 |
| `iat` | 签发时间（Issued At），以纪元时间格式表示。 |
| `aud` | 受众（Audience）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `<0` | 失败。 |

> 译注（源码核对）：当前函数返回 `json_obj_encode()` 的结果，编码回调会记录 `builder->overflowed`，但不直接把空间不足作为此函数的负返回值传播。因此这里返回 0 不能单独证明载荷完整；应按初始化、载荷、签名的顺序构建，并在最终签名成功后才使用令牌。`exp` 与 `iat` 当前为 `int32_t`，函数不检查系统时钟或令牌是否已经过期。

<a id="gab10ee40ee3c0b3eea98051c2acbb8a75"></a>

### `jwt_init_builder()`

```c
int jwt_init_builder ( struct jwt_builder * builder, char * buffer, size_t buffer_size )
```

```c
#include <zephyr/data/jwt.h>
```

初始化 JWT 构建器（Builder）。

初始化给定 JWT 构建器，以创建一个新令牌。缓冲区大小必须足以存放完整令牌。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `builder` | 待初始化的构建器。 |
| `buffer` | 用于写入令牌的缓冲区。 |
| `buffer_size` | 此缓冲区的大小。令牌以空字符（NULL Terminator）结束，因此该大小必须为末尾空字符预留空间。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOSPC` | 缓冲区不足以完成初始化。 |

> 译注（源码核对）：初始化会重置写入位置、剩余容量、溢出标志和待编码字节数，并写入所选算法的 JWT 头部。返回成功只说明初始化完成，不代表缓冲区一定足够容纳后续载荷与签名；不能据此跳过后续错误检查。

<a id="gaa000189c83e9b9113f401cd7d523cefe"></a>

### `jwt_sign()`

```c
int jwt_sign ( struct jwt_builder * builder, const char * der_key, size_t der_key_len )
```

```c
#include <zephyr/data/jwt.h>
```

对 JWT 进行签名（Sign）。

对先前已经初始化且已添加载荷的 JWT 进行签名。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `builder` | 先前已经初始化并添加载荷的构建器。 |
| `der_key` | 用于签名的 DER 格式私钥。 |
| `der_key_len` | 私钥的字节数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `<0` | 失败。 |

> 译注（源码核对）：当前 `jwt_sign_impl()` 把输入直接交给 PSA `psa_import_key()`，实际格式由密钥类型决定；请参阅[指南中的格式核对](P029_JSONWebToken指南.md)。源码将 RSA 签名缓冲区固定为 256 字节、ECDSA 固定为 64 字节，不能据函数的通用长度参数推定支持任意 RSA 密钥位数。PSA 导入或签名失败目前统一映射为 `-EINVAL`；最终检测到构建器溢出时返回 `-ENOMEM`。

## 30.5\_相关源码与使用边界

本仓库的[JWT 头文件](../../../include/zephyr/data/jwt.h)与[构建实现](../../../subsys/jwt/jwt.c)可用于源码追踪，版本可能与官网 `latest` 不同。译注核对依据为保存的[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/data/jwt.h)、[官方构建实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/jwt/jwt.c)与[PSA 签名后端](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/jwt/jwt_psa.c)，摘要见[来源记录](../SOURCES.md)。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P029_JSONWebToken指南.md) · [返回大纲](大纲.md) · [下一章](P031_JWT头文件.md)
