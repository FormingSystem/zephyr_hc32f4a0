---
id: learning.zephyr-docs.network-core-model-reference.page-168
title: wifi_credentials_enterprise_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__credentials__enterprise.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第168章\_wifi\_credentials\_enterprise\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__credentials__enterprise.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi企业模式凭据（Enterprise Credentials）的条目。

```c
#include <zephyr/net/wifi_credentials.h>
```

<a id="details"></a>

Wi‑Fi 企业凭据条目（Wi-Fi Enterprise credentials entry）。注意（Note）：此功能尚未实现。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 168.1\_数据成员（Data Fields）

<a id="r_a58ba430cb51a80009639263ebe412895"></a>

```c
struct wifi_credentials_header header
```

相关声明：[wifi_credentials_header](P169_wifi_credentials_header_结构体.md)、[header](#a58ba430cb51a80009639263ebe412895)。

头部（Header）。

<a id="r_aadd1fe1f5d3f3983a5cd82d5d33a4ff4"></a>

```c
size_t identity_len
```

相关声明：[identity_len](#aadd1fe1f5d3f3983a5cd82d5d33a4ff4)。

身份长度（Identity length）。

<a id="r_a8871721054c824b056fcbb9492bf96aa"></a>

```c
size_t anonymous_identity_len
```

相关声明：[anonymous_identity_len](#a8871721054c824b056fcbb9492bf96aa)。

匿名身份长度（Anonymous identity length）。

<a id="r_aeb480da7b9b4c7e0f4ab3b86977032f9"></a>

```c
size_t password_len
```

相关声明：[password_len](#aeb480da7b9b4c7e0f4ab3b86977032f9)。

密码长度（Password length）。

<a id="r_a74d046dbfdc2f1208848c564c8d98843"></a>

```c
size_t ca_cert_len
```

相关声明：[ca_cert_len](#a74d046dbfdc2f1208848c564c8d98843)。

证书颁发机构证书长度（CA certificate length）。

<a id="r_a33525f5af6db7813b8f19554fd5c04f0"></a>

```c
size_t client_cert_len
```

相关声明：[client_cert_len](#a33525f5af6db7813b8f19554fd5c04f0)。

客户端证书长度（Client certificate length）。

<a id="r_a757f7cfbaf1874be1300f68bf42ebc9d"></a>

```c
size_t private_key_len
```

相关声明：[private_key_len](#a757f7cfbaf1874be1300f68bf42ebc9d)。

私钥长度（Private key length）。

<a id="r_ab532c721b2e10c44bf660d67ca63f994"></a>

```c
size_t private_key_pw_len
```

相关声明：[private_key_pw_len](#ab532c721b2e10c44bf660d67ca63f994)。

私钥密码长度（Private key password length）。

## 168.2\_详细说明（Detailed Documentation）

<a id="a8871721054c824b056fcbb9492bf96aa"></a>

### `anonymous_identity_len`

```c
size_t wifi_credentials_enterprise::anonymous_identity_len
```

匿名身份长度（Anonymous identity length）。

<a id="a74d046dbfdc2f1208848c564c8d98843"></a>

### `ca_cert_len`

```c
size_t wifi_credentials_enterprise::ca_cert_len
```

证书颁发机构证书长度（CA certificate length）。

<a id="a33525f5af6db7813b8f19554fd5c04f0"></a>

### `client_cert_len`

```c
size_t wifi_credentials_enterprise::client_cert_len
```

客户端证书长度（Client certificate length）。

<a id="a58ba430cb51a80009639263ebe412895"></a>

### `header`

```c
struct wifi_credentials_header wifi_credentials_enterprise::header
```

头部（Header）。

<a id="aadd1fe1f5d3f3983a5cd82d5d33a4ff4"></a>

### `identity_len`

```c
size_t wifi_credentials_enterprise::identity_len
```

身份长度（Identity length）。

<a id="aeb480da7b9b4c7e0f4ab3b86977032f9"></a>

### `password_len`

```c
size_t wifi_credentials_enterprise::password_len
```

密码长度（Password length）。

<a id="a757f7cfbaf1874be1300f68bf42ebc9d"></a>

### `private_key_len`

```c
size_t wifi_credentials_enterprise::private_key_len
```

私钥长度（Private key length）。

<a id="ab532c721b2e10c44bf660d67ca63f994"></a>

### `private_key_pw_len`

```c
size_t wifi_credentials_enterprise::private_key_pw_len
```

私钥密码长度（Private key password length）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_credentials.h`

## 168.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_credentials.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__credentials_8h_source.html)
- [wifi_credentials_header](P169_wifi_credentials_header_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P167_wifi_connect_req_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P169_wifi_credentials_header_结构体.md)
