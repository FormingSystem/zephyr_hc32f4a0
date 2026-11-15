---
id: learning.zephyr-docs.network-core-model-reference.page-167
title: wifi_connect_req_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__connect__req__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第167章\_wifi\_connect\_req\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__connect__req__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi连接请求（Connect Request）的参数。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi连接请求（Connect Request）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 167.1\_数据成员（Data Fields）

<a id="r_ac260c2cd17a3f36ea101edaf23d41083"></a>

```c
const uint8_t * ssid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ssid](#ac260c2cd17a3f36ea101edaf23d41083)。

服务集标识符（SSID）。

<a id="r_a547dddf6be5dd77eda74b1085a798400"></a>

```c
uint8_t ssid_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ssid_length](#a547dddf6be5dd77eda74b1085a798400)。

服务集标识符长度（SSID length）。

<a id="r_aa7743f0ecbc27a9595720ce13ce57c1d"></a>

```c
const uint8_t * psk
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[psk](#aa7743f0ecbc27a9595720ce13ce57c1d)。

预共享密钥（Pre-shared key，PSK）。

<a id="r_aaf7455a65590d19f047214b459a2dcb9"></a>

```c
uint8_t psk_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[psk_length](#aaf7455a65590d19f047214b459a2dcb9)。

预共享密钥长度（Pre-shared key length）。

<a id="r_a694a729632ab4e0c54fa739dd9bd9132"></a>

```c
bool psk_is_pbkdf2
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[psk_is_pbkdf2](#a694a729632ab4e0c54fa739dd9bd9132)。

预共享密钥（Pre-shared key）是预先计算的 PBKDF2 输出。

<a id="r_a469fac5758b78fc425911837930b2060"></a>

```c
const uint8_t * sae_password
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sae_password](#a469fac5758b78fc425911837930b2060)。

对等实体同时认证密码（SAE password），可选；与 PSK 密码相同，但没有长度限制。

<a id="r_a74f0819e7a546ffb8bfb0ec587eccf20"></a>

```c
uint8_t sae_password_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sae_password_length](#a74f0819e7a546ffb8bfb0ec587eccf20)。

SAE 密码长度（SAE password length）。

<a id="r_aa2fea1881a8ffdf5d7093ae295867f3e"></a>

```c
uint8_t band
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[band](#aa2fea1881a8ffdf5d7093ae295867f3e)。

频段（Frequency band）。

<a id="r_a52b6d0323c35d03ec239f40be35cae72"></a>

```c
uint8_t channel
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel](#a52b6d0323c35d03ec239f40be35cae72)。

信道（Channel）。

<a id="r_a18dce6bb021086877a30e7a04f5b24b9"></a>

```c
enum wifi_security_type security
```

相关声明：[wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)、[security](#a18dce6bb021086877a30e7a04f5b24b9)。

安全类型（Security type）。

<a id="r_a745b3416172672a7e5b12bcc5b55e88c"></a>

```c
enum wifi_mfp_options mfp
```

相关声明：[wifi_mfp_options](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1f252da47d9650023d7fff6d08e49c76)、[mfp](#a745b3416172672a7e5b12bcc5b55e88c)。

管理帧保护选项（MFP options）。

<a id="r_aa8081b9075ff9244cefd0ac1ef3f42cb"></a>

```c
uint8_t bssid [WIFI_MAC_ADDR_LEN]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bssid](#aa8081b9075ff9244cefd0ac1ef3f42cb)、[WIFI_MAC_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga29409ff83a53c6464decdde9bdd04de6)。

基本服务集标识符（BSSID）。

<a id="r_a56183ba7f4d8eaf5fc5b495856adecfd"></a>

```c
int timeout
```

相关声明：[timeout](#a56183ba7f4d8eaf5fc5b495856adecfd)。

连接超时（Connect timeout），单位为秒；`SYS_FOREVER_MS` 表示不设超时。

<a id="r_a781456e079357e2e1096218af3bd218c"></a>

```c
const uint8_t * anon_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[anon_id](#a781456e079357e2e1096218af3bd218c)。

Wi‑Fi 企业网络进行 EAP 认证第一阶段（Phase 1）时使用的匿名身份（Anonymous identity）。

<a id="r_a2892253024b70e5cb8eb2166b17ebe22"></a>

```c
uint8_t aid_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[aid_length](#a2892253024b70e5cb8eb2166b17ebe22)。

匿名身份长度（Anonymous identity length），最多 64 字节。

<a id="r_a4946647659a347667ee49bb6990bba66"></a>

```c
const uint8_t * key_passwd
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key_passwd](#a4946647659a347667ee49bb6990bba66)。

Wi‑Fi 企业认证使用的私钥密码（Private key password）。

<a id="r_a9f913fc0ccecafaba488e444d701fd68"></a>

```c
uint8_t key_passwd_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key_passwd_length](#a9f913fc0ccecafaba488e444d701fd68)。

私钥密码长度（Private key password length），最多 128 字节。

<a id="r_a020fc58d7e5350cc803cd5d6fa575e6a"></a>

```c
const uint8_t * key2_passwd
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key2_passwd](#a020fc58d7e5350cc803cd5d6fa575e6a)。

认证方法要求时，第二个私钥所用的密码（Secondary private key password）。

<a id="r_af7b163cc2bffc59f7fa31f47c5e52062"></a>

```c
uint8_t key2_passwd_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key2_passwd_length](#af7b163cc2bffc59f7fa31f47c5e52062)。

第二个私钥的密码长度（Secondary private key password length），最多 128 字节。

<a id="r_ae0b94d870ecbee0b203caee6a6e3d8b2"></a>

```c
enum wifi_wpa3_enterprise_type wpa3_ent_mode
```

相关声明：[wifi_wpa3_enterprise_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga48fea1f0c7d2700cef47068f96c6b71a)、[wpa3_ent_mode](#ae0b94d870ecbee0b203caee6a6e3d8b2)。

WPA3 企业模式类型（WPA3 Enterprise mode type）。

<a id="r_aa4577535a27b8d54d9b8c7543d359ade"></a>

```c
uint8_t TLS_cipher
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[TLS_cipher](#aa4577535a27b8d54d9b8c7543d359ade)。

EAP-TLS 认证所使用的 TLS 密码套件（TLS cipher suite）。

<a id="r_a8c8ecb1ef0fe3f2f4c04a7a8eeccbbdf"></a>

```c
int eap_ver
```

相关声明：[eap_ver](#a8c8ecb1ef0fe3f2f4c04a7a8eeccbbdf)。

要使用的可扩展认证协议版本（Extensible Authentication Protocol，EAP version）。

<a id="r_ab9c65599409387af65a3c2895c3116da"></a>

```c
const uint8_t * eap_identity
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[eap_identity](#ab9c65599409387af65a3c2895c3116da)。

EAP 认证第二阶段，即内部认证（Phase 2, inner authentication）所用的身份字符串（Identity string）。

<a id="r_a4da02ff112c09f55dc5bddcda27d16a3"></a>

```c
uint8_t eap_id_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[eap_id_length](#a4da02ff112c09f55dc5bddcda27d16a3)。

EAP 身份长度（EAP identity length），最多 64 字节。

<a id="r_afd046e702739c4a0d89322ee41b37acd"></a>

```c
const uint8_t * eap_password
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[eap_password](#afd046e702739c4a0d89322ee41b37acd)。

EAP 认证第二阶段，即内部认证（Phase 2, inner authentication）所用的密码字符串（Password string）。

<a id="r_aeab22e95a04a1831b87beda1772d3db7"></a>

```c
uint8_t eap_passwd_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[eap_passwd_length](#aeab22e95a04a1831b87beda1772d3db7)。

EAP 密码长度（EAP password length），最多 128 字节。

<a id="r_aa8f18ace96e471eb0bc8bff8d8146f6f"></a>

```c
bool verify_peer_cert
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[verify_peer_cert](#aa8f18ace96e471eb0bc8bff8d8146f6f)。

认证期间是否校验服务器的证书颁发机构（Certificate authority，CA）。

<a id="r_a047b11e703fb646d778785dfcb14257b"></a>

```c
bool ft_used
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[ft_used](#a047b11e703fb646d778785dfcb14257b)。

指示是否使用快速基本服务集转换（Fast BSS Transition，802.11r）。

<a id="r_a71770c2f2da378db2efedaa87b141627"></a>

```c
int nusers
```

相关声明：[nusers](#a71770c2f2da378db2efedaa87b141627)。

提供的 EAP 用户身份（User identities）数量。

<a id="r_aaf071a51c7281e4d42197f266c729c04"></a>

```c
uint8_t passwds
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[passwds](#aaf071a51c7281e4d42197f266c729c04)。

提供的 EAP 密码（Passwords）数量。

<a id="r_a265001d2309840d04bdca507896255d0"></a>

```c
const uint8_t * identities [WIFI_ENT_IDENTITY_MAX_USERS]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[identities](#a265001d2309840d04bdca507896255d0)。

由指向 EAP 认证用户身份字符串的指针组成的数组（Array of user identity string pointers）。

<a id="r_a2163b50b6d466663404e1cb21ce6ae5d"></a>

```c
const uint8_t * passwords [WIFI_ENT_IDENTITY_MAX_USERS]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[passwords](#a2163b50b6d466663404e1cb21ce6ae5d)。

由指向 EAP 认证用户密码字符串的指针组成的数组（Array of user password string pointers）。

<a id="r_afac70366e509301f9a27ca51be30b88d"></a>

```c
uint8_t ignore_broadcast_ssid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ignore_broadcast_ssid](#afac70366e509301f9a27ca51be30b88d)。

隐藏服务集标识符配置（Hidden SSID configuration）：`0` 禁用，默认值；`1` 在信标（Beacon）中发送空 SSID，即长度为 `0`，并忽略针对广播 SSID 的探测请求（Probe request）；`2` 清空 SSID 内容但保留原长度，并忽略针对广播 SSID 的探测请求。

<a id="r_a0d44c86d9b9528041bbe7534e0c7597a"></a>

```c
enum wifi_frequency_bandwidths bandwidth
```

相关声明：[wifi_frequency_bandwidths](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3b01cead3c2eb4581fe85e2aaaffbd49)、[bandwidth](#a0d44c86d9b9528041bbe7534e0c7597a)。

用于指定频段（Frequency band）的参数。

<a id="r_a3833aaaaa78e31d2061e690564af200d"></a>

```c
const uint8_t * server_cert_domain_exact
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[server_cert_domain_exact](#a3833aaaaa78e31d2061e690564af200d)。

要在服务器证书（Server certificate）中校验的完整域名（Full domain name）。

<a id="r_a040d2bda9e1a6528814d4cb87bef2924"></a>

```c
uint8_t server_cert_domain_exact_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[server_cert_domain_exact_len](#a040d2bda9e1a6528814d4cb87bef2924)。

`server_cert_domain_exact` 字符串长度，最多 128 字节。

<a id="r_ad82589b9613dd52b63c9ea5ae0fcebeb"></a>

```c
const uint8_t * server_cert_domain_suffix
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[server_cert_domain_suffix](#ad82589b9613dd52b63c9ea5ae0fcebeb)。

要在服务器证书（Server certificate）中校验的域名后缀（Domain name suffix）。

<a id="r_af94eefb87c15c53057e8f22b67a50494"></a>

```c
uint8_t server_cert_domain_suffix_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[server_cert_domain_suffix_len](#af94eefb87c15c53057e8f22b67a50494)。

`server_cert_domain_suffix` 字符串长度，最多 64 字节。

<a id="r_ac9675ace459d40d6e912d86b6b416305"></a>

```c
uint8_t ssid_protection
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ssid_protection](#ac9675ace459d40d6e912d86b6b416305)。

四次握手中的 SSID 保护（SSID protection in 4-way handshake），需要 RSNXE 支持：`0` 禁用，默认值；`1` 启用。

<a id="r_a562ce91f5eff43e85f84acf342d4e288"></a>

```c
uint8_t transition_disable
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[transition_disable](#a562ce91f5eff43e85f84acf342d4e288)。

WPA3 过渡禁用位图（Transition Disable bitmap），参见 WPA3 规范 v3.0 表 5。

## 167.2\_详细说明（Detailed Documentation）

<a id="a2892253024b70e5cb8eb2166b17ebe22"></a>

### `aid_length`

```c
uint8_t wifi_connect_req_params::aid_length
```

匿名身份长度（Anonymous identity length），最多 64 字节。

<a id="a781456e079357e2e1096218af3bd218c"></a>

### `anon_id`

```c
const uint8_t* wifi_connect_req_params::anon_id
```

Wi‑Fi 企业网络进行 EAP 认证第一阶段（Phase 1）时使用的匿名身份（Anonymous identity）。

在 PEAP、TTLS 等 EAP 方法中，匿名身份（Anonymous identity）在初始外部认证交换中发送，用于保护用户的真实身份 `eap_identity`。此值并非总是必需；若未设置，真实身份可能暴露。仅用于第一阶段，即外部认证（Phase 1, outer authentication）。

<a id="aa2fea1881a8ffdf5d7093ae295867f3e"></a>

### `band`

```c
uint8_t wifi_connect_req_params::band
```

频段（Frequency band）。

<a id="a0d44c86d9b9528041bbe7534e0c7597a"></a>

### `bandwidth`

```c
enum wifi_frequency_bandwidths wifi_connect_req_params::bandwidth
```

用于指定频段（Frequency band）的参数。

<a id="aa8081b9075ff9244cefd0ac1ef3f42cb"></a>

### `bssid`

```c
uint8_t wifi_connect_req_params::bssid[WIFI_MAC_ADDR_LEN]
```

基本服务集标识符（BSSID）。

<a id="a52b6d0323c35d03ec239f40be35cae72"></a>

### `channel`

```c
uint8_t wifi_connect_req_params::channel
```

信道（Channel）。

<a id="a4da02ff112c09f55dc5bddcda27d16a3"></a>

### `eap_id_length`

```c
uint8_t wifi_connect_req_params::eap_id_length
```

EAP 身份长度（EAP identity length），最多 64 字节。

<a id="ab9c65599409387af65a3c2895c3116da"></a>

### `eap_identity`

```c
const uint8_t* wifi_connect_req_params::eap_identity
```

EAP 认证第二阶段，即内部认证（Phase 2, inner authentication）所用的身份字符串（Identity string）。

这是建立安全隧道（Secure tunnel）之后提供给认证服务器的真实用户名或身份，例如在 PEAP 或 TTLS 隧道内部提供。大多数企业 Wi‑Fi 网络（如 WPA2／WPA3 Enterprise）都要求此项。适用于第二阶段，即内部认证（Phase 2, inner authentication）。

<a id="aeab22e95a04a1831b87beda1772d3db7"></a>

### `eap_passwd_length`

```c
uint8_t wifi_connect_req_params::eap_passwd_length
```

EAP 密码长度（EAP password length），最多 128 字节。

<a id="afd046e702739c4a0d89322ee41b37acd"></a>

### `eap_password`

```c
const uint8_t* wifi_connect_req_params::eap_password
```

EAP 认证第二阶段，即内部认证（Phase 2, inner authentication）所用的密码字符串（Password string）。

用于需要密码的 EAP 方法，例如 PEAP、TTLS、EAP-FAST。这是用户在企业 Wi‑Fi 网络中的密码。适用于第二阶段，即内部认证（Phase 2, inner authentication）。

<a id="a8c8ecb1ef0fe3f2f4c04a7a8eeccbbdf"></a>

### `eap_ver`

```c
int wifi_connect_req_params::eap_ver
```

要使用的可扩展认证协议版本（Extensible Authentication Protocol，EAP version）。

可扩展认证协议（EAP）是一种网络认证框架，常用于企业 Wi‑Fi。网络有要求时，此字段允许指定协议版本。适用于第一阶段，即外部认证（Phase 1, outer authentication）。值为 `-1` 时将进行版本协商（Version negotiation）。

<a id="a047b11e703fb646d778785dfcb14257b"></a>

### `ft_used`

```c
bool wifi_connect_req_params::ft_used
```

指示是否使用快速基本服务集转换（Fast BSS Transition，802.11r）。

快速基本服务集转换（Fast BSS Transition）支持在企业网络的接入点（Access points）之间无缝漫游。它适用于整个连接，不专属于某个 EAP 阶段。

<a id="a265001d2309840d04bdca507896255d0"></a>

### `identities`

```c
const uint8_t* wifi_connect_req_params::identities[WIFI_ENT_IDENTITY_MAX_USERS]
```

由指向 EAP 认证用户身份字符串的指针组成的数组（Array of user identity string pointers）。

用于需要多个用户身份（User identities）的企业 Wi‑Fi 网络。适用于第二阶段，即内部认证（Phase 2, inner authentication）。

<a id="afac70366e509301f9a27ca51be30b88d"></a>

### `ignore_broadcast_ssid`

```c
uint8_t wifi_connect_req_params::ignore_broadcast_ssid
```

隐藏服务集标识符配置（Hidden SSID configuration）：`0` 禁用，默认值；`1` 在信标（Beacon）中发送空 SSID，即长度为 `0`，并忽略针对广播 SSID 的探测请求（Probe request）；`2` 清空 SSID 内容但保留原长度，并忽略针对广播 SSID 的探测请求。

<a id="a020fc58d7e5350cc803cd5d6fa575e6a"></a>

### `key2_passwd`

```c
const uint8_t* wifi_connect_req_params::key2_passwd
```

认证方法要求时，第二个私钥所用的密码（Secondary private key password）。

很少使用，通常只在高级企业配置中需要。使用第二个私钥（Second private key）时，适用于第一阶段，即外部认证（Phase 1, outer authentication）。

<a id="af7b163cc2bffc59f7fa31f47c5e52062"></a>

### `key2_passwd_length`

```c
uint8_t wifi_connect_req_params::key2_passwd_length
```

第二个私钥的密码长度（Secondary private key password length），最多 128 字节。

<a id="a4946647659a347667ee49bb6990bba66"></a>

### `key_passwd`

```c
const uint8_t* wifi_connect_req_params::key_passwd
```

Wi‑Fi 企业认证使用的私钥密码（Private key password）。

在需要客户端证书（Client certificate）和私钥（Private key）时使用，例如 EAP-TLS。这是保护私钥文件的密码。使用客户端证书时，适用于第一阶段，即外部认证（Phase 1, outer authentication）。

<a id="a9f913fc0ccecafaba488e444d701fd68"></a>

### `key_passwd_length`

```c
uint8_t wifi_connect_req_params::key_passwd_length
```

私钥密码长度（Private key password length），最多 128 字节。

<a id="a745b3416172672a7e5b12bcc5b55e88c"></a>

### `mfp`

```c
enum wifi_mfp_options wifi_connect_req_params::mfp
```

管理帧保护选项（MFP options）。

<a id="a71770c2f2da378db2efedaa87b141627"></a>

### `nusers`

```c
int wifi_connect_req_params::nusers
```

提供的 EAP 用户身份（User identities）数量。

用于需要多个用户凭据（User credentials）的高级企业认证场景。适用于第二阶段，即内部认证（Phase 2, inner authentication）。

<a id="aaf071a51c7281e4d42197f266c729c04"></a>

### `passwds`

```c
uint8_t wifi_connect_req_params::passwds
```

提供的 EAP 密码（Passwords）数量。

在企业认证中与多个用户身份（User identities）配合使用。适用于第二阶段，即内部认证（Phase 2, inner authentication）。

<a id="a2163b50b6d466663404e1cb21ce6ae5d"></a>

### `passwords`

```c
const uint8_t* wifi_connect_req_params::passwords[WIFI_ENT_IDENTITY_MAX_USERS]
```

由指向 EAP 认证用户密码字符串的指针组成的数组（Array of user password string pointers）。

用于需要多个用户密码（User passwords）的企业 Wi‑Fi 网络。适用于第二阶段，即内部认证（Phase 2, inner authentication）。

<a id="aa7743f0ecbc27a9595720ce13ce57c1d"></a>

### `psk`

```c
const uint8_t* wifi_connect_req_params::psk
```

预共享密钥（Pre-shared key，PSK）。

<a id="a694a729632ab4e0c54fa739dd9bd9132"></a>

### `psk_is_pbkdf2`

```c
bool wifi_connect_req_params::psk_is_pbkdf2
```

预共享密钥（Pre-shared key）是预先计算的 PBKDF2 输出。

`psk_length` 必须（MUST）为 32 字节。仅适用于基于预共享密钥（PSK）的安全类型。

<a id="aaf7455a65590d19f047214b459a2dcb9"></a>

### `psk_length`

```c
uint8_t wifi_connect_req_params::psk_length
```

预共享密钥长度（Pre-shared key length）。

<a id="a469fac5758b78fc425911837930b2060"></a>

### `sae_password`

```c
const uint8_t* wifi_connect_req_params::sae_password
```

对等实体同时认证密码（SAE password），可选；与 PSK 密码相同，但没有长度限制。

<a id="a74f0819e7a546ffb8bfb0ec587eccf20"></a>

### `sae_password_length`

```c
uint8_t wifi_connect_req_params::sae_password_length
```

SAE 密码长度（SAE password length）。

<a id="a18dce6bb021086877a30e7a04f5b24b9"></a>

### `security`

```c
enum wifi_security_type wifi_connect_req_params::security
```

安全类型（Security type）。

<a id="a3833aaaaa78e31d2061e690564af200d"></a>

### `server_cert_domain_exact`

```c
const uint8_t* wifi_connect_req_params::server_cert_domain_exact
```

要在服务器证书（Server certificate）中校验的完整域名（Full domain name）。

<a id="a040d2bda9e1a6528814d4cb87bef2924"></a>

### `server_cert_domain_exact_len`

```c
uint8_t wifi_connect_req_params::server_cert_domain_exact_len
```

`server_cert_domain_exact` 字符串长度，最多 128 字节。

<a id="ad82589b9613dd52b63c9ea5ae0fcebeb"></a>

### `server_cert_domain_suffix`

```c
const uint8_t* wifi_connect_req_params::server_cert_domain_suffix
```

要在服务器证书（Server certificate）中校验的域名后缀（Domain name suffix）。

<a id="af94eefb87c15c53057e8f22b67a50494"></a>

### `server_cert_domain_suffix_len`

```c
uint8_t wifi_connect_req_params::server_cert_domain_suffix_len
```

`server_cert_domain_suffix` 字符串长度，最多 64 字节。

<a id="ac260c2cd17a3f36ea101edaf23d41083"></a>

### `ssid`

```c
const uint8_t* wifi_connect_req_params::ssid
```

服务集标识符（SSID）。

<a id="a547dddf6be5dd77eda74b1085a798400"></a>

### `ssid_length`

```c
uint8_t wifi_connect_req_params::ssid_length
```

服务集标识符长度（SSID length）。

<a id="ac9675ace459d40d6e912d86b6b416305"></a>

### `ssid_protection`

```c
uint8_t wifi_connect_req_params::ssid_protection
```

四次握手中的 SSID 保护（SSID protection in 4-way handshake），需要 RSNXE 支持：`0` 禁用，默认值；`1` 启用。

<a id="a56183ba7f4d8eaf5fc5b495856adecfd"></a>

### `timeout`

```c
int wifi_connect_req_params::timeout
```

连接超时（Connect timeout），单位为秒；`SYS_FOREVER_MS` 表示不设超时。

<a id="aa4577535a27b8d54d9b8c7543d359ade"></a>

### `TLS_cipher`

```c
uint8_t wifi_connect_req_params::TLS_cipher
```

EAP-TLS 认证所使用的 TLS 密码套件（TLS cipher suite）。

此项选择安全连接使用的密码算法（Cryptographic algorithms）。仅与采用 EAP-TLS 或类似方法的企业网络有关。适用于第一阶段，即外部认证（Phase 1, outer authentication）。

<a id="a562ce91f5eff43e85f84acf342d4e288"></a>

### `transition_disable`

```c
uint8_t wifi_connect_req_params::transition_disable
```

WPA3 过渡禁用位图（Transition Disable bitmap），参见 WPA3 规范 v3.0 表 5。

在局域网上可扩展认证协议（EAPOL）的第 3 条消息中，以过渡禁用密钥数据元素（Transition Disable KDE）形式发送。位 0：WPA3-Personal；位 1：WPA3-Personal SAE-PK；位 2：WPA3-Enterprise；位 3：机会式无线加密（OWE）。

<a id="aa8f18ace96e471eb0bc8bff8d8146f6f"></a>

### `verify_peer_cert`

```c
bool wifi_connect_req_params::verify_peer_cert
```

认证期间是否校验服务器的证书颁发机构（Certificate authority，CA）。

设为 `true` 时要求校验服务器证书（Server certificate），出于安全考虑建议使用此设置。设为 `false` 时跳过 CA 校验；不建议这样做，但有时用于测试。适用于第一阶段，即外部认证（Phase 1, outer authentication）。

<a id="ae0b94d870ecbee0b203caee6a6e3d8b2"></a>

### `wpa3_ent_mode`

```c
enum wifi_wpa3_enterprise_type wifi_connect_req_params::wpa3_ent_mode
```

WPA3 企业模式类型（WPA3 Enterprise mode type）。

选择要使用的 WPA3 企业认证变体（WPA3 Enterprise authentication variant）。WPA3 Enterprise 是常用于组织机构的 Wi‑Fi 网络安全协议，相比 WPA2 提供增强的安全性。此字段仅与企业网络有关。适用于第一阶段，即外部认证（Phase 1, outer authentication）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 167.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)
- [wifi_mfp_options](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1f252da47d9650023d7fff6d08e49c76)
- [WIFI_MAC_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga29409ff83a53c6464decdde9bdd04de6)
- [wifi_wpa3_enterprise_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga48fea1f0c7d2700cef47068f96c6b71a)
- [wifi_frequency_bandwidths](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3b01cead3c2eb4581fe85e2aaaffbd49)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P166_wifi_config_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P168_wifi_credentials_enterprise_结构体.md)
