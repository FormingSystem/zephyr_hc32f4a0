---
id: learning.zephyr-docs.crypto.page-29
title: JSONWebToken指南
kind: reference
status: maintained
domains: [zephyr, crypto, security]
source_url: https://docs.zephyrproject.org/latest/services/jwt/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_JSONWebToken指南

原文：[官方页面](https://docs.zephyrproject.org/latest/services/jwt/index.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 29.1\_概述（Overview）

JSON Web 令牌（JSON Web Token，JWT）是一种在双方之间安全表示声明（Claims）的开放行业标准方法，定义见 [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519.html)。JWT 本身较为灵活，但此 API 仅用于创建原文所称 Google Core IoT 基础设施认证所需的简单令牌。

从高层看，JWT 是经过签名的 JSON 数据；客户端可以提交令牌，而不必每次都发送用户名／密码等凭据。

译注：上述 Google Core IoT 名称按原文保留，描述该接口的历史应用目标，不构成具体云服务当前可用性的承诺。当前接口只提供令牌生成，并不包含通用 JWT 解析与验证器；签名也不意味着载荷经过加密。

## 29.2\_用法（Usage）

使用 JWT API 时，包含以下头文件：

```c
#include <zephyr/data/jwt.h>
```

## 29.3\_生成 JWT（Generating a JWT）

JWT 子系统提供基于构建器（Builder）的轻量接口，用来构造 JSON Web 令牌。载荷（Payload，即声明）包含过期时间（Expiration Time）、签发时间（Issued At）和受众（Audience），然后使用提供的私钥签名。

```c
#include <zephyr/data/jwt.h>

struct jwt_builder builder;
char buffer[1024];
int ret;

/* Initialize the builder */
ret = jwt_init_builder(&builder, buffer, sizeof(buffer));
if (ret < 0) {
    /* Handle error */
}

/* Add payload: expiration, issued at, audience */
ret = jwt_add_payload(&builder, 1767221999, 1764605987, "project-id");
if (ret < 0) {
    /* Handle error */
}

/* Sign the token using a DER-encoded private key */
ret = jwt_sign(&builder, private_key_der, private_key_der_len);
if (ret < 0) {
    /* Handle error */
}

/*
 * buffer now contains the JWT; it can be passed to a third-party service that will be able
 * to validate it against the public key associated with `private_key_der`.
 */
```

代码注释译文：初始化构建器；遇到负返回值时处理错误；添加过期时间、签发时间和受众；用 DER 编码的私钥签名；成功后 `buffer` 包含 JWT，可传给能够使用对应公钥验证签名的第三方服务。

译注：`private_key_der` 与 `private_key_der_len` 需要由应用提供；两个时间数值和 `"project-id"` 是原示例值，应按实际时间与服务要求替换。示例的“处理错误”分支只是注释，实际代码应停止使用失败或不完整的令牌，不能直接继续下一步。`exp`、`iat` 的当前类型为 `int32_t`，应核对取值范围；API 不自行读取时钟或验证过期时间。

译注（源码核对）：按“初始化 → 添加载荷 → 签名”的顺序构建一次令牌。缓冲区溢出时，`jwt_add_payload()` 可能只设置 `builder.overflowed` 而仍返回 JSON 编码结果；最终 `jwt_sign()` 会检查该标志并返回失败。只有最终签名成功且未溢出，才可将缓冲区视作完整输出。

译注——私钥格式：原文与参数名都写 DER（Distinguished Encoding Rules），但当前实现直接把字节传给 PSA 的 `psa_import_key()`。应按所选密钥类型解释输入：RSA 的标准导入形式为未加密 PKCS #1 `RSAPrivateKey` DER；P-256 椭圆曲线私钥的标准形式是 32 字节大端标量，不是完整 ECPrivateKey DER 容器。实现可支持额外格式，不能仅凭参数名假定所有分支都接受同一 DER 文件。见 [PSA 密钥格式](https://arm-software.github.io/psa-api/crypto/1.2/api/keys/management.html#key-formats)。

## 29.4\_配置（Configuration）

相关配置选项：

- [`CONFIG_JWT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_JWT)。
- [`CONFIG_JWT_.*`](https://docs.zephyrproject.org/latest/kconfig.html#!CONFIG_JWT_.*)。

译注：当前 Kconfig 在基于 PSA Crypto 的 RSA 签名（RS256）与椭圆曲线数字签名（Elliptic Curve Digital Signature Algorithm，ECDSA；ES256）之间选择，默认 RSA。签名头部随构建配置决定，不能把不同算法的密钥随意互换。

## 29.5\_API 参考（API Reference）

[JWT 构建与签名接口](P030_JWT构建与签名接口.md)。


译注核对来源：[include/zephyr/data/jwt.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/data/jwt.h)、[subsys/jwt/jwt.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/jwt/jwt.c)、[subsys/jwt/jwt_psa.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/jwt/jwt_psa.c)、[subsys/jwt/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/jwt/Kconfig)。

本仓库的[对应源码](../../../include/zephyr/data/jwt.h)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、烧录、密钥生成或存储操作。

<a id="json-web-token-jwt"></a>
<a id="jwt-api"></a>
<a id="overview"></a>
<a id="index-0"></a>
<a id="usage"></a>
<a id="generating-a-jwt"></a>
<a id="configuration"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：PSA密码学](P003_PSA密码学.md) · [本模块主线目录](../reading/crypto.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P028_散列性能测试示例.md) · [返回大纲](大纲.md) · [下一章](P030_JWT构建与签名接口.md)

</details>

<!-- reading-navigation:end -->
