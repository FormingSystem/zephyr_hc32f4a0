---
id: learning.zephyr-docs.network-core-model-reference.page-169
title: wifi_credentials_header_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__credentials__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第169章\_wifi\_credentials\_header\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__credentials__header.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi凭据条目头部（Credentials Entry Header）。

```c
#include <zephyr/net/wifi_credentials.h>
```

<a id="details"></a>

Wi‑Fi 凭据条目头部（Wi-Fi credentials entry header）。注意（Note）：每个设置条目均以此头部开始。根据 `type` 字段，可以将此头部强制转换为一个更大的类型。除了服务集标识符（SSID，通常为字符串）和基本服务集标识符（BSSID，即 MAC 地址）以外，还可使用标志字段（Flags）控制某些细节设置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 169.1\_数据成员（Data Fields）

<a id="r_a5b873555b2154e22367644c2805c0494"></a>

```c
enum wifi_security_type type
```

相关声明：[wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)、[type](#a5b873555b2154e22367644c2805c0494)。

Wi‑Fi 安全类型（Wi-Fi security type）。

<a id="r_a52cd2e481d3ebf141c671e9a67f5a224"></a>

```c
char ssid [WIFI_SSID_MAX_LEN]
```

相关声明：[ssid](#a52cd2e481d3ebf141c671e9a67f5a224)、[WIFI_SSID_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad62c60666c9fdffe2e0e9c4388f87886)。

服务集标识符（Service Set Identifier，SSID）。

<a id="r_ab5bfa4ac972a8ad1ba4b395fad48a923"></a>

```c
size_t ssid_len
```

相关声明：[ssid_len](#ab5bfa4ac972a8ad1ba4b395fad48a923)。

服务集标识符长度（SSID length）。

<a id="r_a59b8b99ad309c0cc2cb6c5438554fefe"></a>

```c
uint32_t flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](#a59b8b99ad309c0cc2cb6c5438554fefe)。

用于控制细节设置的标志（Flags）。

<a id="r_ab6b02e3c88ff13a323cbafdf9af9ba1f"></a>

```c
uint32_t timeout
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timeout](#ab6b02e3c88ff13a323cbafdf9af9ba1f)。

连接网络的超时值（Connection timeout）。

<a id="r_a28d311d5535c7569bda860dca7fd08f6"></a>

```c
uint8_t bssid [WIFI_MAC_ADDR_LEN]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bssid](#a28d311d5535c7569bda860dca7fd08f6)、[WIFI_MAC_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga29409ff83a53c6464decdde9bdd04de6)。

基本服务集标识符（Basic Service Set Identifier，BSSID）。

<a id="r_a9ab939e7cb212a85d2612d5582e2336d"></a>

```c
uint8_t channel
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel](#a9ab939e7cb212a85d2612d5582e2336d)。

网络运行的信道（Channel）。

<a id="r_acbbd421fda51f23d2243dd9573b05d71"></a>

```c
char anon_id [16]
```

相关声明：[anon_id](#acbbd421fda51f23d2243dd9573b05d71)。

匿名标识符（Anonymous identifier）；因设置子系统溢出（Settings subsystem overflow），限制为 16 字节。

<a id="r_a2c39cdc6f7023560de61fb353a178369"></a>

```c
uint8_t aid_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[aid_length](#a2c39cdc6f7023560de61fb353a178369)。

匿名标识符长度（Anonymous identifier length）。

<a id="r_a99ccc993d609632f42650aabe9fc861b"></a>

```c
char key_passwd [16]
```

相关声明：[key_passwd](#a99ccc993d609632f42650aabe9fc861b)。

密码／预共享密钥（Password/PSK）；因设置子系统溢出（Settings subsystem overflow），限制为 16 字节。

<a id="r_a605b62d473586f3d8312aa1c80731ee6"></a>

```c
uint8_t key_passwd_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key_passwd_length](#a605b62d473586f3d8312aa1c80731ee6)。

密码长度（Password length）。

## 169.2\_详细说明（Detailed Documentation）

<a id="a2c39cdc6f7023560de61fb353a178369"></a>

### `aid_length`

```c
uint8_t wifi_credentials_header::aid_length
```

匿名标识符长度（Anonymous identifier length）。

<a id="acbbd421fda51f23d2243dd9573b05d71"></a>

### `anon_id`

```c
char wifi_credentials_header::anon_id[16]
```

匿名标识符（Anonymous identifier）；因设置子系统溢出（Settings subsystem overflow），限制为 16 字节。

<a id="a28d311d5535c7569bda860dca7fd08f6"></a>

### `bssid`

```c
uint8_t wifi_credentials_header::bssid[WIFI_MAC_ADDR_LEN]
```

基本服务集标识符（Basic Service Set Identifier，BSSID）。

<a id="a9ab939e7cb212a85d2612d5582e2336d"></a>

### `channel`

```c
uint8_t wifi_credentials_header::channel
```

网络运行的信道（Channel）。

<a id="a59b8b99ad309c0cc2cb6c5438554fefe"></a>

### `flags`

```c
uint32_t wifi_credentials_header::flags
```

用于控制细节设置的标志（Flags）。

<a id="a99ccc993d609632f42650aabe9fc861b"></a>

### `key_passwd`

```c
char wifi_credentials_header::key_passwd[16]
```

密码／预共享密钥（Password/PSK）；因设置子系统溢出（Settings subsystem overflow），限制为 16 字节。

<a id="a605b62d473586f3d8312aa1c80731ee6"></a>

### `key_passwd_length`

```c
uint8_t wifi_credentials_header::key_passwd_length
```

密码长度（Password length）。

<a id="a52cd2e481d3ebf141c671e9a67f5a224"></a>

### `ssid`

```c
char wifi_credentials_header::ssid[WIFI_SSID_MAX_LEN]
```

服务集标识符（Service Set Identifier，SSID）。

<a id="ab5bfa4ac972a8ad1ba4b395fad48a923"></a>

### `ssid_len`

```c
size_t wifi_credentials_header::ssid_len
```

服务集标识符长度（SSID length）。

<a id="ab6b02e3c88ff13a323cbafdf9af9ba1f"></a>

### `timeout`

```c
uint32_t wifi_credentials_header::timeout
```

连接网络的超时值（Connection timeout）。

<a id="a5b873555b2154e22367644c2805c0494"></a>

### `type`

```c
enum wifi_security_type wifi_credentials_header::type
```

Wi‑Fi 安全类型（Wi-Fi security type）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_credentials.h`

## 169.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_credentials.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__credentials_8h_source.html)
- [wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)
- [WIFI_SSID_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad62c60666c9fdffe2e0e9c4388f87886)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [WIFI_MAC_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga29409ff83a53c6464decdde9bdd04de6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P168_wifi_credentials_enterprise_结构体.md) · [返回大纲](大纲.md) · [下一章](P170_wifi_credentials_personal_结构体.md)
