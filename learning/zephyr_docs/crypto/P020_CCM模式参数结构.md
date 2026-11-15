---
id: learning.zephyr-docs.crypto.api-20
title: CCM模式参数结构
kind: reference
status: maintained
domains: [zephyr, crypto, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structccm__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_CCM模式参数结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structccm__params.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 20.1\_阅读说明与来源

译注：先读[密码学指南](P001_密码学服务概览.md)、[API 指南](P002_密码学接口指南.md)和[密码驱动示例](P004_密码驱动测试示例.md)。本组说明通用密码驱动、会话（Session）、密码模式（Cipher Mode）及数据包（Packet）；与 PSA Crypto 的密钥标识符接口区分使用。

本组：[密码驱动通用接口](P008_密码驱动通用接口.md) · [密码驱动后端接口](P009_密码驱动后端接口.md) · [密码驱动公共头文件](P010_密码驱动公共头文件.md) · [密码驱动公共头文件源码](P011_密码驱动公共头文件源码.md) · [密码算法会话接口](P012_密码算法会话接口.md) · [密码算法头文件](P013_密码算法头文件.md) · [密码算法头文件源码](P014_密码算法头文件源码.md) · [密码会话上下文结构](P015_密码会话上下文结构.md) · [密码操作函数结构](P016_密码操作函数结构.md) · [密码数据包结构](P017_密码数据包结构.md) · [认证加密数据包结构](P018_认证加密数据包结构.md) · [密码驱动API结构](P019_密码驱动API结构.md) · [CCM模式参数结构](P020_CCM模式参数结构.md) · [CTR模式参数结构](P021_CTR模式参数结构.md) · [GCM模式参数结构](P022_GCM模式参数结构.md)。

CCM 模式会话参数。

```c
#include <zephyr/crypto/cipher.h>
```

CCM 模式会话参数。

## 20.2\_数据成员（Data Fields）

<a id="r_a6a0d01056dcc05e2f7dccef25d4c5747"></a>

```c
uint16_t tag_len
```

认证标签长度，单位为字节。

<a id="r_adbc306823d339083ec439277a7e35e8a"></a>

```c
uint16_t nonce_len
```

一次性值（Nonce）长度，单位为字节。

## 20.3\_详细说明（Detailed Documentation）

<a id="adbc306823d339083ec439277a7e35e8a"></a>

### `nonce_len`

```c
uint16_t ccm_params::nonce_len
```

一次性值（Nonce）长度，单位为字节。

<a id="a6a0d01056dcc05e2f7dccef25d4c5747"></a>

### `tag_len`

```c
uint16_t ccm_params::tag_len
```

认证标签长度，单位为字节。

## 20.4\_相关源码与使用边界

本仓库的[公共头文件](../../../include/zephyr/crypto/crypto.h)与[密码结构头文件](../../../include/zephyr/crypto/cipher.h)可用于源码追踪，版本可能与官网 `latest` 不同。译注核对依据为保存的[官方公共头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/crypto/crypto.h)、[官方结构头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/crypto/cipher.h)和[Mbed TLS 适配驱动](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/crypto_mbedtls_shim.c)，摘要见[来源记录](../SOURCES.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P019_密码驱动API结构.md) · [返回大纲](大纲.md) · [下一章](P021_CTR模式参数结构.md)
