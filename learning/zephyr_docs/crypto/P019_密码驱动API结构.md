---
id: learning.zephyr-docs.crypto.api-19
title: 密码驱动API结构
kind: reference
status: maintained
domains: [zephyr, crypto, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcrypto__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_密码驱动API结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcrypto__driver__api.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 19.1\_阅读说明与来源

译注：先读[密码学指南](P001_密码学服务概览.md)、[API 指南](P002_密码学接口指南.md)和[密码驱动示例](P004_密码驱动测试示例.md)。本组说明通用密码驱动、会话（Session）、密码模式（Cipher Mode）及数据包（Packet）；与 PSA Crypto 的密钥标识符接口区分使用。

本组：[密码驱动通用接口](P008_密码驱动通用接口.md) · [密码驱动后端接口](P009_密码驱动后端接口.md) · [密码驱动公共头文件](P010_密码驱动公共头文件.md) · [密码驱动公共头文件源码](P011_密码驱动公共头文件源码.md) · [密码算法会话接口](P012_密码算法会话接口.md) · [密码算法头文件](P013_密码算法头文件.md) · [密码算法头文件源码](P014_密码算法头文件源码.md) · [密码会话上下文结构](P015_密码会话上下文结构.md) · [密码操作函数结构](P016_密码操作函数结构.md) · [密码数据包结构](P017_密码数据包结构.md) · [认证加密数据包结构](P018_认证加密数据包结构.md) · [密码驱动API结构](P019_密码驱动API结构.md) · [CCM模式参数结构](P020_CCM模式参数结构.md) · [CTR模式参数结构](P021_CTR模式参数结构.md) · [GCM模式参数结构](P022_GCM模式参数结构.md)。

驱动操作（Driver Operations）：密码驱动操作。

```c
#include <zephyr/crypto/crypto.h>
```

驱动操作（Driver Operations）：密码驱动操作。这是所有密码驱动都需要定义的驱动 API 结构，包含已实现操作的函数指针以及其他驱动专用常量数据。标记为 REQ 的成员必须由驱动设置，标记为 OPT 的成员是可选的。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 与 `DEVICE_API()`。

## 19.2\_数据成员（Data Fields）

<a id="r_a8915e4a587406b1fb2a9952eb5689f04"></a>

```c
crypto_api_query_hw_caps query_hw_caps
```

必需（REQ）：查询密码硬件能力。

相关声明：[crypto_api_query_hw_caps](P009_密码驱动后端接口.md#gab793287abb88cd60beb2081e19d213b1)。

<a id="r_a508969d611dde99f4837666ffefe2095"></a>

```c
crypto_api_cipher_begin_session cipher_begin_session
```

必需（REQ）：建立密码算法会话。

相关声明：[crypto_api_cipher_begin_session](P009_密码驱动后端接口.md#ga5873378194774dac59ad97a4ab3e22ee)。

<a id="r_a71976e23a2f748677a621e7c37b9b4e3"></a>

```c
crypto_api_cipher_free_session cipher_free_session
```

必需（REQ）：清理密码算法会话。

相关声明：[crypto_api_cipher_free_session](P009_密码驱动后端接口.md#gab64f46720c197503bfaf2c7aba5d3c65)。

<a id="r_ae52b3f8e6242a2e6a5a439a2f2a68f5d"></a>

```c
crypto_api_cipher_async_callback_set cipher_async_callback_set
```

可选（OPT）：注册异步密码算法回调。

相关声明：[crypto_api_cipher_async_callback_set](P009_密码驱动后端接口.md#gad1fc74ac61bb5ae4016f3829959c1a89)。

<a id="r_ab0ab3196e64819bf2e7647d63a48e3dd"></a>

```c
crypto_api_hash_begin_session hash_begin_session
```

必需（REQ）：建立密码散列会话。

相关声明：[crypto_api_hash_begin_session](P009_密码驱动后端接口.md#gaf3e1105ac5b40da851957ad68ede0e9b)。

<a id="r_a5a52c54cb7242576fcb03f566f3d1bfc"></a>

```c
crypto_api_hash_free_session hash_free_session
```

必需（REQ）：清理密码散列会话。

相关声明：[crypto_api_hash_free_session](P009_密码驱动后端接口.md#ga625d8c213d610eeea54fb98772e1269b)。

<a id="r_a5b396e69dde8b30f2310b5357feb8631"></a>

```c
crypto_api_hash_async_callback_set hash_async_callback_set
```

可选（OPT）：注册异步密码散列回调。

相关声明：[crypto_api_hash_async_callback_set](P009_密码驱动后端接口.md#gaaf81d09943d108004cd7e979e8cbd2dd)。

## 19.3\_详细说明（Detailed Documentation）

<a id="ae52b3f8e6242a2e6a5a439a2f2a68f5d"></a>

### `cipher_async_callback_set`

```c
crypto_api_cipher_async_callback_set crypto_driver_api::cipher_async_callback_set
```

可选（OPT）：注册异步密码算法回调。

<a id="a508969d611dde99f4837666ffefe2095"></a>

### `cipher_begin_session`

```c
crypto_api_cipher_begin_session crypto_driver_api::cipher_begin_session
```

必需（REQ）：建立密码算法会话。

<a id="a71976e23a2f748677a621e7c37b9b4e3"></a>

### `cipher_free_session`

```c
crypto_api_cipher_free_session crypto_driver_api::cipher_free_session
```

必需（REQ）：清理密码算法会话。

<a id="a5b396e69dde8b30f2310b5357feb8631"></a>

### `hash_async_callback_set`

```c
crypto_api_hash_async_callback_set crypto_driver_api::hash_async_callback_set
```

可选（OPT）：注册异步密码散列回调。

<a id="ab0ab3196e64819bf2e7647d63a48e3dd"></a>

### `hash_begin_session`

```c
crypto_api_hash_begin_session crypto_driver_api::hash_begin_session
```

必需（REQ）：建立密码散列会话。

<a id="a5a52c54cb7242576fcb03f566f3d1bfc"></a>

### `hash_free_session`

```c
crypto_api_hash_free_session crypto_driver_api::hash_free_session
```

必需（REQ）：清理密码散列会话。

<a id="a8915e4a587406b1fb2a9952eb5689f04"></a>

### `query_hw_caps`

```c
crypto_api_query_hw_caps crypto_driver_api::query_hw_caps
```

必需（REQ）：查询密码硬件能力。

## 19.4\_相关源码与使用边界

本仓库的[公共头文件](../../../include/zephyr/crypto/crypto.h)与[密码结构头文件](../../../include/zephyr/crypto/cipher.h)可用于源码追踪，版本可能与官网 `latest` 不同。译注核对依据为保存的[官方公共头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/crypto/crypto.h)、[官方结构头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/crypto/cipher.h)和[Mbed TLS 适配驱动](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/crypto/crypto_mbedtls_shim.c)，摘要见[来源记录](../SOURCES.md)。

本批保留公共头文件中散列入口与驱动回调类型的全部声明；散列的详细参数与数据结构现已另译，见[Hash 会话参考](P023_密码散列会话接口.md)。随机函数的既有译文见[随机数接口](../data_utilities/P007_随机数接口.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P018_认证加密数据包结构.md) · [返回大纲](大纲.md) · [下一章](P020_CCM模式参数结构.md)
