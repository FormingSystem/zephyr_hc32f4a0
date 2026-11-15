---
id: learning.zephyr-docs.network-core-model-reference.page-173
title: wifi_enterprise_creds_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__enterprise__creds__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第173章\_wifi\_enterprise\_creds\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__enterprise__creds__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi企业模式凭据（Enterprise Mode Credentials）。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi企业模式凭据（Enterprise Mode Credentials）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 173.1\_数据成员（Data Fields）

<a id="r_ae37381504a457b2f1d56dd5270c6711d"></a>

```c
uint8_t * ca_cert
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ca_cert](#ae37381504a457b2f1d56dd5270c6711d)。

证书颁发机构证书（CA certificate）。

<a id="r_a5f7060fcd2ca3db0b202faf15062564b"></a>

```c
uint32_t ca_cert_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[ca_cert_len](#a5f7060fcd2ca3db0b202faf15062564b)。

证书颁发机构证书长度（CA certificate length）。

<a id="r_a81d61179feba627be5c6456130b9f2af"></a>

```c
uint8_t * client_cert
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[client_cert](#a81d61179feba627be5c6456130b9f2af)。

客户端证书（Client certificate）。

<a id="r_a5f122d59b25b00af2db7eeac93d5482e"></a>

```c
uint32_t client_cert_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[client_cert_len](#a5f122d59b25b00af2db7eeac93d5482e)。

客户端证书长度（Client certificate length）。

<a id="r_a8d88f5a8a6ccc8a9a883078af49ae96b"></a>

```c
uint8_t * client_key
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[client_key](#a8d88f5a8a6ccc8a9a883078af49ae96b)。

客户端密钥（Client key）。

<a id="r_a09f5b34c81fe871e7513358499518d95"></a>

```c
uint32_t client_key_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[client_key_len](#a09f5b34c81fe871e7513358499518d95)。

客户端密钥长度（Client key length）。

<a id="r_ad9b867873709d7f2363fef49d7b6f2ca"></a>

```c
uint8_t * ca_cert2
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ca_cert2](#ad9b867873709d7f2363fef49d7b6f2ca)。

第二阶段的证书颁发机构证书（Phase 2 CA certificate）。

<a id="r_abf35045e71afb0cb9ea25c635c5ac141"></a>

```c
uint32_t ca_cert2_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[ca_cert2_len](#abf35045e71afb0cb9ea25c635c5ac141)。

第二阶段 CA 证书长度（Phase 2 CA certificate length）。

<a id="r_a133126e338d89563733268a03e2fa613"></a>

```c
uint8_t * client_cert2
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[client_cert2](#a133126e338d89563733268a03e2fa613)。

第二阶段的客户端证书（Phase 2 client certificate）。

<a id="r_adbe26c9b88f44eb6b875888f6a03e1bb"></a>

```c
uint32_t client_cert2_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[client_cert2_len](#adbe26c9b88f44eb6b875888f6a03e1bb)。

第二阶段客户端证书长度（Phase 2 client certificate length）。

<a id="r_abcda4d7820681d517d70d8f130b47050"></a>

```c
uint8_t * client_key2
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[client_key2](#abcda4d7820681d517d70d8f130b47050)。

第二阶段的客户端密钥（Phase 2 client key）。

<a id="r_a3da90b8a8dfa848f617579760ad4f971"></a>

```c
uint32_t client_key2_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[client_key2_len](#a3da90b8a8dfa848f617579760ad4f971)。

第二阶段客户端密钥长度（Phase 2 client key length）。

<a id="r_ad3621e92a1aa968c58a899ace72967db"></a>

```c
uint8_t * server_cert
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[server_cert](#ad3621e92a1aa968c58a899ace72967db)。

服务器证书（Server certificate）。

<a id="r_ad0bfb59d3691e5d21cb4b810c4d1279e"></a>

```c
uint32_t server_cert_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[server_cert_len](#ad0bfb59d3691e5d21cb4b810c4d1279e)。

服务器证书长度（Server certificate length）。

<a id="r_acb94a8885b5ab99d1a8fb33dffebc322"></a>

```c
uint8_t * server_key
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[server_key](#acb94a8885b5ab99d1a8fb33dffebc322)。

服务器密钥（Server key）。

<a id="r_a9500252974bd15037d4dbc41eba3a27d"></a>

```c
uint32_t server_key_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[server_key_len](#a9500252974bd15037d4dbc41eba3a27d)。

服务器密钥长度（Server key length）。

<a id="r_ab0fd7419d8a94d1d804e5554acfbf49a"></a>

```c
uint8_t * dh_param
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[dh_param](#ab0fd7419d8a94d1d804e5554acfbf49a)。

迪菲–赫尔曼参数（Diffie-Hellman parameter）。

<a id="r_ac548e0b006a9f7b858409cda7c3d34ba"></a>

```c
uint32_t dh_param_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dh_param_len](#ac548e0b006a9f7b858409cda7c3d34ba)。

迪菲–赫尔曼参数长度（Diffie-Hellman parameter length）。

## 173.2\_详细说明（Detailed Documentation）

<a id="ae37381504a457b2f1d56dd5270c6711d"></a>

### `ca_cert`

```c
uint8_t* wifi_enterprise_creds_params::ca_cert
```

证书颁发机构证书（CA certificate）。

<a id="ad9b867873709d7f2363fef49d7b6f2ca"></a>

### `ca_cert2`

```c
uint8_t* wifi_enterprise_creds_params::ca_cert2
```

第二阶段的证书颁发机构证书（Phase 2 CA certificate）。

<a id="abf35045e71afb0cb9ea25c635c5ac141"></a>

### `ca_cert2_len`

```c
uint32_t wifi_enterprise_creds_params::ca_cert2_len
```

第二阶段 CA 证书长度（Phase 2 CA certificate length）。

<a id="a5f7060fcd2ca3db0b202faf15062564b"></a>

### `ca_cert_len`

```c
uint32_t wifi_enterprise_creds_params::ca_cert_len
```

证书颁发机构证书长度（CA certificate length）。

<a id="a81d61179feba627be5c6456130b9f2af"></a>

### `client_cert`

```c
uint8_t* wifi_enterprise_creds_params::client_cert
```

客户端证书（Client certificate）。

<a id="a133126e338d89563733268a03e2fa613"></a>

### `client_cert2`

```c
uint8_t* wifi_enterprise_creds_params::client_cert2
```

第二阶段的客户端证书（Phase 2 client certificate）。

<a id="adbe26c9b88f44eb6b875888f6a03e1bb"></a>

### `client_cert2_len`

```c
uint32_t wifi_enterprise_creds_params::client_cert2_len
```

第二阶段客户端证书长度（Phase 2 client certificate length）。

<a id="a5f122d59b25b00af2db7eeac93d5482e"></a>

### `client_cert_len`

```c
uint32_t wifi_enterprise_creds_params::client_cert_len
```

客户端证书长度（Client certificate length）。

<a id="a8d88f5a8a6ccc8a9a883078af49ae96b"></a>

### `client_key`

```c
uint8_t* wifi_enterprise_creds_params::client_key
```

客户端密钥（Client key）。

<a id="abcda4d7820681d517d70d8f130b47050"></a>

### `client_key2`

```c
uint8_t* wifi_enterprise_creds_params::client_key2
```

第二阶段的客户端密钥（Phase 2 client key）。

<a id="a3da90b8a8dfa848f617579760ad4f971"></a>

### `client_key2_len`

```c
uint32_t wifi_enterprise_creds_params::client_key2_len
```

第二阶段客户端密钥长度（Phase 2 client key length）。

<a id="a09f5b34c81fe871e7513358499518d95"></a>

### `client_key_len`

```c
uint32_t wifi_enterprise_creds_params::client_key_len
```

客户端密钥长度（Client key length）。

<a id="ab0fd7419d8a94d1d804e5554acfbf49a"></a>

### `dh_param`

```c
uint8_t* wifi_enterprise_creds_params::dh_param
```

迪菲–赫尔曼参数（Diffie-Hellman parameter）。

<a id="ac548e0b006a9f7b858409cda7c3d34ba"></a>

### `dh_param_len`

```c
uint32_t wifi_enterprise_creds_params::dh_param_len
```

迪菲–赫尔曼参数长度（Diffie-Hellman parameter length）。

<a id="ad3621e92a1aa968c58a899ace72967db"></a>

### `server_cert`

```c
uint8_t* wifi_enterprise_creds_params::server_cert
```

服务器证书（Server certificate）。

<a id="ad0bfb59d3691e5d21cb4b810c4d1279e"></a>

### `server_cert_len`

```c
uint32_t wifi_enterprise_creds_params::server_cert_len
```

服务器证书长度（Server certificate length）。

<a id="acb94a8885b5ab99d1a8fb33dffebc322"></a>

### `server_key`

```c
uint8_t* wifi_enterprise_creds_params::server_key
```

服务器密钥（Server key）。

<a id="a9500252974bd15037d4dbc41eba3a27d"></a>

### `server_key_len`

```c
uint32_t wifi_enterprise_creds_params::server_key_len
```

服务器密钥长度（Server key length）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 173.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P172_wifi_eap_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P174_wifi_filter_info_结构体.md)
