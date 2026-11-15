---
id: learning.zephyr-docs.network-core-model-reference.page-171
title: wifi_eap_cipher_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__eap__cipher__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第171章\_wifi\_eap\_cipher\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__eap__cipher__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

可扩展认证协议（EAP）的密码算法配置。

```c
#include <zephyr/net/wifi.h>
```

<a id="details"></a>

可扩展认证协议（EAP）的密码算法配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 171.1\_数据成员（Data Fields）

<a id="r_a385d365bb70a70fa09d321c55988afcc"></a>

```c
char * key_mgmt
```

相关声明：[key_mgmt](#a385d365bb70a70fa09d321c55988afcc)。

密钥管理类型字符串（Key management type string）。

<a id="r_a14128465917447f38d3854444a9bf6e1"></a>

```c
char * openssl_ciphers
```

相关声明：[openssl_ciphers](#a14128465917447f38d3854444a9bf6e1)。

OpenSSL 密码算法字符串（OpenSSL cipher string）。

<a id="r_aa505ae934897742078aa46f1fdb5d0d1"></a>

```c
char * group_cipher
```

相关声明：[group_cipher](#aa505ae934897742078aa46f1fdb5d0d1)。

组密码算法字符串（Group cipher string）。

<a id="r_a3917f94dfafb22df260db9c4a129c3c4"></a>

```c
char * pairwise_cipher
```

相关声明：[pairwise_cipher](#a3917f94dfafb22df260db9c4a129c3c4)。

成对密码算法字符串（Pairwise_cipher cipher string）。

<a id="r_ab53f5b5419b2b8c8a869ba4f9d645a41"></a>

```c
char * group_mgmt_cipher
```

相关声明：[group_mgmt_cipher](#ab53f5b5419b2b8c8a869ba4f9d645a41)。

组管理密码算法字符串（Group management cipher string）。

<a id="r_ae9a4b8a0f0b47ac1065562ce287473a5"></a>

```c
char * tls_flags
```

相关声明：[tls_flags](#ae9a4b8a0f0b47ac1065562ce287473a5)。

用于配置传输层安全特性（TLS features）。

## 171.2\_详细说明（Detailed Documentation）

<a id="aa505ae934897742078aa46f1fdb5d0d1"></a>

### `group_cipher`

```c
char* wifi_eap_cipher_config::group_cipher
```

组密码算法字符串（Group cipher string）。

<a id="ab53f5b5419b2b8c8a869ba4f9d645a41"></a>

### `group_mgmt_cipher`

```c
char* wifi_eap_cipher_config::group_mgmt_cipher
```

组管理密码算法字符串（Group management cipher string）。

<a id="a385d365bb70a70fa09d321c55988afcc"></a>

### `key_mgmt`

```c
char* wifi_eap_cipher_config::key_mgmt
```

密钥管理类型字符串（Key management type string）。

<a id="a14128465917447f38d3854444a9bf6e1"></a>

### `openssl_ciphers`

```c
char* wifi_eap_cipher_config::openssl_ciphers
```

OpenSSL 密码算法字符串（OpenSSL cipher string）。

<a id="a3917f94dfafb22df260db9c4a129c3c4"></a>

### `pairwise_cipher`

```c
char* wifi_eap_cipher_config::pairwise_cipher
```

成对密码算法字符串（Pairwise_cipher cipher string）。

<a id="ae9a4b8a0f0b47ac1065562ce287473a5"></a>

### `tls_flags`

```c
char* wifi_eap_cipher_config::tls_flags
```

用于配置传输层安全特性（TLS features）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi.h`

## 171.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P170_wifi_credentials_personal_结构体.md) · [返回大纲](大纲.md) · [下一章](P172_wifi_eap_config_结构体.md)
