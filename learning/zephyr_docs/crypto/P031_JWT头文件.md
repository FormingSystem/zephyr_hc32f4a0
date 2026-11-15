---
id: learning.zephyr-docs.crypto.api-31
title: JWT头文件
kind: reference
status: maintained
domains: [zephyr, crypto, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/jwt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_JWT头文件

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/jwt_8h.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 31.1\_阅读说明与来源

译注：配合[JSON Web Token 指南](P029_JSONWebToken指南.md)阅读。这里的构建器（Builder）生成包含固定声明（Claims）并经过签名的 JWT，接口没有提供任意声明编辑、令牌解析或验证功能。

本组：[JWT构建与签名接口](P030_JWT构建与签名接口.md) · [JWT头文件](P031_JWT头文件.md) · [JWT头文件源码](P032_JWT头文件源码.md) · [JWT构建器结构](P033_JWT构建器结构.md)。

```c
#include <zephyr/types.h>
```

```c
#include <stdbool.h>
```

## 31.2\_数据结构（Data Structures）

<a id="r_jwt_5Fbuilder"></a>

```c
struct jwt_builder
```

JWT 数据跟踪（Data Tracking）。

相关声明：[jwt_builder](P033_JWT构建器结构.md)。

## 31.3\_函数（Functions）

<a id="r_gab10ee40ee3c0b3eea98051c2acbb8a75"></a>

```c
int jwt_init_builder (struct jwt_builder *builder, char *buffer, size_t buffer_size)
```

初始化 JWT 构建器（Builder）。

相关声明：[jwt_init_builder](P030_JWT构建与签名接口.md#gab10ee40ee3c0b3eea98051c2acbb8a75)、[jwt_builder](P033_JWT构建器结构.md)。

<a id="r_ga209dc2bdbaf72b4c9d11be02e0ffe479"></a>

```c
int jwt_add_payload (struct jwt_builder *builder, int32_t exp, int32_t iat, const char *aud)
```

添加 JWT 载荷（Payload）。

相关声明：[jwt_add_payload](P030_JWT构建与签名接口.md#ga209dc2bdbaf72b4c9d11be02e0ffe479)、[jwt_builder](P033_JWT构建器结构.md)。

<a id="r_gaa000189c83e9b9113f401cd7d523cefe"></a>

```c
int jwt_sign (struct jwt_builder *builder, const char *der_key, size_t der_key_len)
```

对 JWT 进行签名（Sign）。

相关声明：[jwt_sign](P030_JWT构建与签名接口.md#gaa000189c83e9b9113f401cd7d523cefe)、[jwt_builder](P033_JWT构建器结构.md)。

## 31.4\_相关源码与使用边界

本仓库的[JWT 头文件](../../../include/zephyr/data/jwt.h)与[构建实现](../../../subsys/jwt/jwt.c)可用于源码追踪，版本可能与官网 `latest` 不同。译注核对依据为保存的[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/data/jwt.h)、[官方构建实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/jwt/jwt.c)与[PSA 签名后端](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/jwt/jwt_psa.c)，摘要见[来源记录](../SOURCES.md)。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>

[上一章](P030_JWT构建与签名接口.md) · [返回大纲](大纲.md) · [下一章](P032_JWT头文件源码.md)
