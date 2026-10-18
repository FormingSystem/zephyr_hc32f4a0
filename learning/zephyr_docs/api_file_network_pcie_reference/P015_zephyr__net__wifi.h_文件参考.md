---
id: learning.zephyr-docs.api-file-network-pcie-reference.page-15
title: zephyr__net__wifi.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wifi_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_net\_\_wifi.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/wifi_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IEEE 802.11协议与通用Wi-Fi定义。

<a id="details"></a>

```c
#include <zephyr/sys/util.h>
```

查看此文件的源码。

IEEE 802.11协议与通用Wi-Fi定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.1\_数据结构（Data Structures）

<a id="r_wifi_5Fcipher_5Fdesc"></a>

```c
struct wifi_cipher_desc
```

相关声明：[wifi_cipher_desc](../network_core_model_reference/P165_wifi_cipher_desc_结构体.md)。

密码算法能力与名称说明（Cipher Capability and Name Description）。

<a id="r_wifi_5Feap_5Fcipher_5Fconfig"></a>

```c
struct wifi_eap_cipher_config
```

相关声明：[wifi_eap_cipher_config](../network_core_model_reference/P171_wifi_eap_cipher_config_结构体.md)。

可扩展认证协议（EAP）的密码算法配置。

<a id="r_wifi_5Feap_5Fconfig"></a>

```c
struct wifi_eap_config
```

相关声明：[wifi_eap_config](../network_core_model_reference/P172_wifi_eap_config_结构体.md)。

可扩展认证协议（EAP）的方法配置。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.2\_宏定义（Macros）

<a id="r_ga6766ef7bcb001f1fb526a4083b6cd8bc"></a>

```c
#define WIFI_COUNTRY_CODE_LEN 2
```

相关声明：[WIFI_COUNTRY_CODE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga6766ef7bcb001f1fb526a4083b6cd8bc)。

国家代码字符串长度（Country Code String Length）。

<a id="r_gad62c60666c9fdffe2e0e9c4388f87886"></a>

```c
#define WIFI_SSID_MAX_LEN 32
```

相关声明：[WIFI_SSID_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad62c60666c9fdffe2e0e9c4388f87886)。

最大服务集标识符长度（Maximum SSID Length）。

<a id="r_gaa8e19abf8c85f237ba5033740ceff553"></a>

```c
#define WIFI_PSK_MIN_LEN 8
```

相关声明：[WIFI_PSK_MIN_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa8e19abf8c85f237ba5033740ceff553)。

最小预共享密钥长度（Minimum PSK Length）。

<a id="r_gad7c3b99c974b342935180a28fdc5ddfc"></a>

```c
#define WIFI_PSK_MAX_LEN 64
```

相关声明：[WIFI_PSK_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad7c3b99c974b342935180a28fdc5ddfc)。

最大预共享密钥长度（Maximum PSK Length）。

<a id="r_gaf466d0b11462b3f190d579702cb9ee51"></a>

```c
#define WIFI_WEP_KEY_MAX_LEN 26
```

相关声明：[WIFI_WEP_KEY_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf466d0b11462b3f190d579702cb9ee51)。

最大 WEP 密钥长度（Maximum WEP Key Length）；WEP-104 为 26 个十六进制字符。

<a id="r_ga7d6424d6770b2357f0b8abb456ae53fc"></a>

```c
#define WIFI_PSK_PBKDF2_KEY_LEN 32
```

相关声明：[WIFI_PSK_PBKDF2_KEY_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7d6424d6770b2357f0b8abb456ae53fc)。

PBKDF2 密钥长度（Key Length）。

<a id="r_gab63fa744cc2e049cfd635ab0a187971f"></a>

```c
#define WIFI_SAE_PSWD_MAX_LEN 128
```

相关声明：[WIFI_SAE_PSWD_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gab63fa744cc2e049cfd635ab0a187971f)。

最大 SAW 密码长度（Max SAW Password Length，原文写作 SAW）。

<a id="r_ga29409ff83a53c6464decdde9bdd04de6"></a>

```c
#define WIFI_MAC_ADDR_LEN 6
```

相关声明：[WIFI_MAC_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga29409ff83a53c6464decdde9bdd04de6)。

MAC 地址长度（MAC address length）。

<a id="r_gac6904487661f157274b0b60833f6684a"></a>

```c
#define WIFI_ENT_IDENTITY_MAX_LEN 64
```

相关声明：[WIFI_ENT_IDENTITY_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac6904487661f157274b0b60833f6684a)。

最大企业身份长度（Maximum Enterprise Identity Length）。

<a id="r_gae2fd55924f4078187431f7a1184f217f"></a>

```c
#define WIFI_ENT_PSWD_MAX_LEN 128
```

相关声明：[WIFI_ENT_PSWD_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae2fd55924f4078187431f7a1184f217f)。

最大企业密码长度（Maximum Enterprise Password Length）。

<a id="r_ga260e473dac1e823fd298a2c982470e0b"></a>

```c
#define WIFI_CHANNEL_MIN 1
```

相关声明：[WIFI_CHANNEL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga260e473dac1e823fd298a2c982470e0b)。

最小信道编号（Minimum Channel Number）。

<a id="r_ga8ea9141108f93b419f6a6530bf67bd95"></a>

```c
#define WIFI_CHANNEL_MAX 233
```

相关声明：[WIFI_CHANNEL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga8ea9141108f93b419f6a6530bf67bd95)。

最大信道编号（Maximum Channel Number）。

<a id="r_ga3876cd718af9f8a7b3682546da854544"></a>

```c
#define WIFI_CHANNEL_ANY 255
```

相关声明：[WIFI_CHANNEL_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3876cd718af9f8a7b3682546da854544)。

任意信道编号（Any Channel Number）。

<a id="r_gaa1a74ef94af57a7ea966c691c065a46d"></a>

```c
#define WIFI_INTERFACE_INDEX_MIN 1
```

相关声明：[WIFI_INTERFACE_INDEX_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa1a74ef94af57a7ea966c691c065a46d)。

网络接口索引最小值（Network Interface Index Minimum）。

<a id="r_gaa6cbecd7d4197d453038d3da7ef6be7b"></a>

```c
#define WIFI_INTERFACE_INDEX_MAX 255
```

相关声明：[WIFI_INTERFACE_INDEX_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa6cbecd7d4197d453038d3da7ef6be7b)。

网络接口索引最大值（Network Interface Index Maximum）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 15.3\_枚举（Enumerations）

<a id="r_ga86a5741e54aeb3e290142b0de217b8a8"></a>

```c
enum wifi_conn_status { WIFI_STATUS_CONN_SUCCESS = 0 , WIFI_STATUS_CONN_FAIL , WIFI_STATUS_CONN_WRONG_PASSWORD , WIFI_STATUS_CONN_TIMEOUT , WIFI_STATUS_CONN_AP_NOT_FOUND , WIFI_STATUS_CONN_AUTH_REJECT , WIFI_STATUS_CONN_ASSOC_REJECT , WIFI_STATUS_CONN_LAST_STATUS , WIFI_STATUS_DISCONN_FIRST_STATUS = WIFI_STATUS_CONN_LAST_STATUS }
```

相关声明：[wifi_conn_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga86a5741e54aeb3e290142b0de217b8a8)、[WIFI_STATUS_CONN_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd)、[WIFI_STATUS_CONN_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44)、[WIFI_STATUS_CONN_WRONG_PASSWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8)、[WIFI_STATUS_CONN_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563)、[WIFI_STATUS_CONN_AP_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4)、[WIFI_STATUS_CONN_AUTH_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8a008abc5c55c4ea7409f5b16be4f68a91)、[WIFI_STATUS_CONN_ASSOC_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8aeaccd303a2c836347555886f746b54eb)、[WIFI_STATUS_CONN_LAST_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f)、[WIFI_STATUS_DISCONN_FIRST_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8abe1401e5d516c0d63291add15e558b18)。

Wi-Fi 连接结果代码（Connect Result Codes）。

<a id="r_gadde31a04fa25ed805115c6b31854cd9c"></a>

```c
enum wifi_security_type { WIFI_SECURITY_TYPE_NONE = 0 , WIFI_SECURITY_TYPE_PSK , WIFI_SECURITY_TYPE_PSK_SHA256 , WIFI_SECURITY_TYPE_SAE , WIFI_SECURITY_TYPE_SAE_HNP = WIFI_SECURITY_TYPE_SAE , WIFI_SECURITY_TYPE_SAE_H2E , WIFI_SECURITY_TYPE_SAE_AUTO , WIFI_SECURITY_TYPE_WAPI , WIFI_SECURITY_TYPE_EAP , WIFI_SECURITY_TYPE_EAP_TLS = WIFI_SECURITY_TYPE_EAP , WIFI_SECURITY_TYPE_WEP , WIFI_SECURITY_TYPE_WPA_PSK , WIFI_SECURITY_TYPE_WPA_AUTO_PERSONAL , WIFI_SECURITY_TYPE_DPP , WIFI_SECURITY_TYPE_EAP_PEAP_MSCHAPV2 , WIFI_SECURITY_TYPE_EAP_PEAP_GTC , WIFI_SECURITY_TYPE_EAP_TTLS_MSCHAPV2 , WIFI_SECURITY_TYPE_EAP_PEAP_TLS , WIFI_SECURITY_TYPE_FT_PSK , WIFI_SECURITY_TYPE_FT_SAE , WIFI_SECURITY_TYPE_FT_EAP , WIFI_SECURITY_TYPE_FT_EAP_SHA384 , WIFI_SECURITY_TYPE_SAE_EXT_KEY , WIFI_SECURITY_TYPE_WEP_OPEN , WIFI_SECURITY_TYPE_WEP_SHARED , WIFI_SECURITY_TYPE_OWE , WIFI_SECURITY_TYPE_PSK_SHA384 , WIFI_SECURITY_TYPE_FT_PSK_SHA384 }
```

相关声明：[wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)、[WIFI_SECURITY_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca3f0a729e3c906d9c398a9fba163a0a9e)、[WIFI_SECURITY_TYPE_PSK](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca1b9f70d6425eaa5a94211826a91c2368)、[WIFI_SECURITY_TYPE_PSK_SHA256](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca0554b0fd5a6233aba5e25b035488380e)、[WIFI_SECURITY_TYPE_SAE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca00d5a50935f70344f03c778055755c2f)、[WIFI_SECURITY_TYPE_SAE_HNP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9caab329c818e10cbe98aac1f9c30849c91)、[WIFI_SECURITY_TYPE_SAE_H2E](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca1e45d14be678d0693b3f03f73fc5b0df)、[WIFI_SECURITY_TYPE_SAE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca4beacdae98f8ca155609d2fd660c5ed0)、[WIFI_SECURITY_TYPE_WAPI](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca37ab810084b3e024731f440e708b363d)、[WIFI_SECURITY_TYPE_EAP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9cacce1e8fbfbf71fb4d669e9d0bfb04f80)、[WIFI_SECURITY_TYPE_EAP_TLS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca85bcce61e75c01eb95083523e8925a40)、[WIFI_SECURITY_TYPE_WEP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca39b793d7f7c49dee4e60a5c6e6831724)、[WIFI_SECURITY_TYPE_WPA_PSK](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca4fd23c30c3b666132903fef27fd0651a)、[WIFI_SECURITY_TYPE_WPA_AUTO_PERSONAL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca275483ee9bced209eb2d131825f599ff)、[WIFI_SECURITY_TYPE_DPP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca6cf0bd5db90deaa6b35f7afe122e8b5f)、[WIFI_SECURITY_TYPE_EAP_PEAP_MSCHAPV2](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9caaa1dbea0100af80ca48ad594cddb4212)、[WIFI_SECURITY_TYPE_EAP_PEAP_GTC](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca0c9db910757c5a715a5e88089362fab5)、[WIFI_SECURITY_TYPE_EAP_TTLS_MSCHAPV2](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca3a20bf15c1e51313629789e6abe0273d)、[WIFI_SECURITY_TYPE_EAP_PEAP_TLS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca6d2e5f72b8bf76f093ab79be2a4b9477)、[WIFI_SECURITY_TYPE_FT_PSK](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca42e49ccccfed285d32aa9f36bcfd5fc5)、[WIFI_SECURITY_TYPE_FT_SAE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9cab7bcc9437586d4940126a2ae1efdb092)、[WIFI_SECURITY_TYPE_FT_EAP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca00d759c3332700100ca7be612abeeda5)、[WIFI_SECURITY_TYPE_FT_EAP_SHA384](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca52aa23f908a4fae0864f2e187b89af93)、[WIFI_SECURITY_TYPE_SAE_EXT_KEY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca64221ce0052ce510e16537a32c67bb02)、[WIFI_SECURITY_TYPE_WEP_OPEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca798e97bb232dfa2bc75b5e6865d78bf7)、[WIFI_SECURITY_TYPE_WEP_SHARED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9cadb96b16c24d4975e88f674b08cab7122)、[WIFI_SECURITY_TYPE_OWE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca3a91d5c899e0789587a94ab5981d98ca)、[WIFI_SECURITY_TYPE_PSK_SHA384](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca1b6d3f896a853bd9c1f03409f0f32814)、[WIFI_SECURITY_TYPE_FT_PSK_SHA384](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9cace9ee870a64b87aa7f97a146bb61951f)。

IEEE 802.11 安全类型（Security Types）。

<a id="r_gafc901312b5988481b34d05a031d6c0db"></a>

```c
enum wifi_wep_key_type { WIFI_WEP_KEY_TYPE_UNKNOWN = 0 , WIFI_WEP_KEY_TYPE_64 , WIFI_WEP_KEY_TYPE_128 }
```

相关声明：[wifi_wep_key_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gafc901312b5988481b34d05a031d6c0db)、[WIFI_WEP_KEY_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggafc901312b5988481b34d05a031d6c0dba58f0ce2c50683011de9e36b55879e104)、[WIFI_WEP_KEY_TYPE_64](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggafc901312b5988481b34d05a031d6c0dba8f89728c41b4aac1b803a558474c1484)、[WIFI_WEP_KEY_TYPE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggafc901312b5988481b34d05a031d6c0dba0a0b1dd584525ee634069c81b91cb97f)。

WEP 密钥类型（Key Type），依据密钥长度（Key Length）确定。

<a id="r_ga92b6fa6755491c3bd61f895213d07331"></a>

```c
enum wifi_eap_type { WIFI_EAP_TYPE_NONE = 0 , WIFI_EAP_TYPE_GTC = 6 , WIFI_EAP_TYPE_TLS = 13 , WIFI_EAP_TYPE_TTLS = 21 , WIFI_EAP_TYPE_PEAP = 25 , WIFI_EAP_TYPE_MSCHAPV2 = 26 }
```

相关声明：[wifi_eap_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga92b6fa6755491c3bd61f895213d07331)、[WIFI_EAP_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga92b6fa6755491c3bd61f895213d07331a39edcc7a267ce608a1e818948b5d172b)、[WIFI_EAP_TYPE_GTC](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga92b6fa6755491c3bd61f895213d07331a64daad77662868322e638da6531a5c0f)、[WIFI_EAP_TYPE_TLS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga92b6fa6755491c3bd61f895213d07331a505b4b888231dd1fbc169d612d8f0c38)、[WIFI_EAP_TYPE_TTLS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga92b6fa6755491c3bd61f895213d07331a35fce37fccb3d27596c4e0a531109dac)、[WIFI_EAP_TYPE_PEAP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga92b6fa6755491c3bd61f895213d07331a8e619153aa3dad398c6ced36605f5e3f)、[WIFI_EAP_TYPE_MSCHAPV2](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga92b6fa6755491c3bd61f895213d07331a37f7681b1fb5d7165010ec941018882f)。

EPA 方法类型（EPA Method Types，原文写作 EPA）。

<a id="r_ga48fea1f0c7d2700cef47068f96c6b71a"></a>

```c
enum wifi_wpa3_enterprise_type { WIFI_WPA3_ENTERPRISE_NA = 0 , WIFI_WPA3_ENTERPRISE_SUITEB = 1 , WIFI_WPA3_ENTERPRISE_SUITEB_192 , WIFI_WPA3_ENTERPRISE_ONLY }
```

相关声明：[wifi_wpa3_enterprise_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga48fea1f0c7d2700cef47068f96c6b71a)、[WIFI_WPA3_ENTERPRISE_NA](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga48fea1f0c7d2700cef47068f96c6b71aa7c34eb5cf3e76c3c1b45c424436adbb1)、[WIFI_WPA3_ENTERPRISE_SUITEB](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga48fea1f0c7d2700cef47068f96c6b71aaec90b38cb8fb95ff3a679da473537589)、[WIFI_WPA3_ENTERPRISE_SUITEB_192](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga48fea1f0c7d2700cef47068f96c6b71aa577671035478f3a385b8e4fdf6abf5fa)、[WIFI_WPA3_ENTERPRISE_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga48fea1f0c7d2700cef47068f96c6b71aaf13490bee764dd77f770f07bf3dac3fa)。

WPA3 企业安全类型（WPA3 Enterprise Security Types）。

<a id="r_ga218525a9d9ee64524f983e52d5767562"></a>

```c
enum wifi_eap_tls_cipher_type { WIFI_EAP_TLS_NONE , WIFI_EAP_TLS_ECC_P384 , WIFI_EAP_TLS_RSA_3K }
```

相关声明：[wifi_eap_tls_cipher_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga218525a9d9ee64524f983e52d5767562)、[WIFI_EAP_TLS_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga218525a9d9ee64524f983e52d5767562a38f97de2297f9df6e4ac3cecfd0799df)、[WIFI_EAP_TLS_ECC_P384](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga218525a9d9ee64524f983e52d5767562ae44c04c2d1510385fe43827dbe6026f9)、[WIFI_EAP_TLS_RSA_3K](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga218525a9d9ee64524f983e52d5767562ac5436dc7d2bbeded043b1102ee592e17)。

EAP TLS 密码类型（Cipher Types）。

<a id="r_ga7f7b23ac019ca504a2006f0376735645"></a>

```c
enum wifi_cipher_type { WPA_CAPA_ENC_CCMP , WPA_CAPA_ENC_GCMP , WPA_CAPA_ENC_GCMP_256 }
```

相关声明：[wifi_cipher_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7f7b23ac019ca504a2006f0376735645)、[WPA_CAPA_ENC_CCMP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga7f7b23ac019ca504a2006f0376735645ac0af8c48884381d3be7e9a2b7f3b54e1)、[WPA_CAPA_ENC_GCMP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga7f7b23ac019ca504a2006f0376735645a88fe5cd8b7777b931d869cb76ae65b1d)、[WPA_CAPA_ENC_GCMP_256](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga7f7b23ac019ca504a2006f0376735645a60599a3fdfad99c6ec1471d4973556c4)。

组密码与成对密码类型（Group Cipher and Pairwise Cipher Types）。

<a id="r_gaf84d5e1a68393483fc6063c06b8f26e0"></a>

```c
enum wifi_group_mgmt_cipher_type { WPA_CAPA_ENC_BIP , WPA_CAPA_ENC_BIP_GMAC_128 , WPA_CAPA_ENC_BIP_GMAC_256 }
```

相关声明：[wifi_group_mgmt_cipher_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf84d5e1a68393483fc6063c06b8f26e0)、[WPA_CAPA_ENC_BIP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaf84d5e1a68393483fc6063c06b8f26e0a7d5bfccaca027a00e834a8db03f8b8f8)、[WPA_CAPA_ENC_BIP_GMAC_128](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaf84d5e1a68393483fc6063c06b8f26e0ab15e42ab1ba05c1296b19cbfff2ccf70)、[WPA_CAPA_ENC_BIP_GMAC_256](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaf84d5e1a68393483fc6063c06b8f26e0ae437a3b3abd043b184e545a4ec40c096)。

组管理密码类型（Group Management Cipher Types）。

<a id="r_ga1f252da47d9650023d7fff6d08e49c76"></a>

```c
enum wifi_mfp_options { WIFI_MFP_DISABLE = 0 , WIFI_MFP_OPTIONAL , WIFI_MFP_REQUIRED }
```

相关声明：[wifi_mfp_options](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1f252da47d9650023d7fff6d08e49c76)、[WIFI_MFP_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1f252da47d9650023d7fff6d08e49c76a260e7b4688790ed39f4f7dc70547e969)、[WIFI_MFP_OPTIONAL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1f252da47d9650023d7fff6d08e49c76a3ffdc747c7c70f7c1b70c96292f57fbf)、[WIFI_MFP_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1f252da47d9650023d7fff6d08e49c76af118a2f047c13db04d164235fa15f840)。

IEEE 802.11w 管理帧保护（Management Frame Protection，MFP）。

<a id="r_ga1e2f0439a322355fa7368ea880c9c15d"></a>

```c
enum wifi_frequency_bands { WIFI_FREQ_BAND_2_4_GHZ = 0 , WIFI_FREQ_BAND_5_GHZ , WIFI_FREQ_BAND_6_GHZ , WIFI_FREQ_BAND_SUB_1_GHZ , __WIFI_FREQ_BAND_AFTER_LAST , WIFI_FREQ_BAND_MAX = __WIFI_FREQ_BAND_AFTER_LAST - 1 , WIFI_FREQ_BAND_UNKNOWN }
```

相关声明：[wifi_frequency_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1e2f0439a322355fa7368ea880c9c15d)、[WIFI_FREQ_BAND_2_4_GHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11)、[WIFI_FREQ_BAND_5_GHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895)、[WIFI_FREQ_BAND_6_GHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15da4f82878368ada29ce8986dd173efdcc0)、[WIFI_FREQ_BAND_SUB_1_GHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15daeb2366af7a35fa929882f7842abb4211)、[WIFI_FREQ_BAND_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15daea3a12c499228420adc9f3aac21d67a5)、[WIFI_FREQ_BAND_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15da8091041d87f7df93223527a31e7e76a5)。

IEEE 802.11 工作频段（Operational Frequency Bands），并非穷举。

<a id="r_ga3b01cead3c2eb4581fe85e2aaaffbd49"></a>

```c
enum wifi_frequency_bandwidths { WIFI_FREQ_BANDWIDTH_20MHZ = 1 , WIFI_FREQ_BANDWIDTH_40MHZ , WIFI_FREQ_BANDWIDTH_80MHZ , WIFI_FREQ_BANDWIDTH_1MHZ , WIFI_FREQ_BANDWIDTH_2MHZ , WIFI_FREQ_BANDWIDTH_4MHZ , WIFI_FREQ_BANDWIDTH_8MHZ , __WIFI_FREQ_BANDWIDTH_AFTER_LAST , WIFI_FREQ_BANDWIDTH_MAX = __WIFI_FREQ_BANDWIDTH_AFTER_LAST - 1 , WIFI_FREQ_BANDWIDTH_UNKNOWN }
```

相关声明：[wifi_frequency_bandwidths](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3b01cead3c2eb4581fe85e2aaaffbd49)、[WIFI_FREQ_BANDWIDTH_20MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49ae5efe45d5211477322968e55014d22d5)、[WIFI_FREQ_BANDWIDTH_40MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49a9f984c246be1976cf1b799c4aed02ea1)、[WIFI_FREQ_BANDWIDTH_80MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49a2c445a7a6345a66a41248bde2f7bf8cb)、[WIFI_FREQ_BANDWIDTH_1MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49a94c8cbcef66fc09604cf5e1a033c4bdc)、[WIFI_FREQ_BANDWIDTH_2MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49aa9036134a2d668f8e86e617628c4b134)、[WIFI_FREQ_BANDWIDTH_4MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49a7f78a7780a1059bf6fcedda5d96b5510)、[WIFI_FREQ_BANDWIDTH_8MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49ada0acd85e6a825be12fe2295c960b93c)、[WIFI_FREQ_BANDWIDTH_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49af57b996c36f950143c9f23a25d402b90)、[WIFI_FREQ_BANDWIDTH_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49a4e45ec9ffe32912a5673f9bbffeeef2d)。

IEEE 802.11 工作频率带宽（Operational Frequency Bandwidths），并非穷举。

<a id="r_ga981961f747b919d61d3ccbd41e4508b4"></a>

```c
enum wifi_iface_state { WIFI_STATE_DISCONNECTED = 0 , WIFI_STATE_INTERFACE_DISABLED , WIFI_STATE_INACTIVE , WIFI_STATE_SCANNING , WIFI_STATE_AUTHENTICATING , WIFI_STATE_ASSOCIATING , WIFI_STATE_ASSOCIATED , WIFI_STATE_4WAY_HANDSHAKE , WIFI_STATE_GROUP_HANDSHAKE , WIFI_STATE_COMPLETED }
```

相关声明：[wifi_iface_state](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga981961f747b919d61d3ccbd41e4508b4)、[WIFI_STATE_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f)、[WIFI_STATE_INTERFACE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c)、[WIFI_STATE_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598)、[WIFI_STATE_SCANNING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b)、[WIFI_STATE_AUTHENTICATING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba)、[WIFI_STATE_ASSOCIATING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b)、[WIFI_STATE_ASSOCIATED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc)、[WIFI_STATE_4WAY_HANDSHAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969)、[WIFI_STATE_GROUP_HANDSHAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e)、[WIFI_STATE_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f)。

Wi-Fi 接口状态（Interface States）。

<a id="r_ga584f6239ac14e2bedc5e6bd72756423b"></a>

```c
enum wifi_iface_mode { WIFI_MODE_INFRA = 0 , WIFI_MODE_IBSS = 1 , WIFI_MODE_AP = 2 , WIFI_MODE_P2P_GO = 3 , WIFI_MODE_P2P_GROUP_FORMATION = 4 , WIFI_MODE_MESH = 5 }
```

相关声明：[wifi_iface_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga584f6239ac14e2bedc5e6bd72756423b)、[WIFI_MODE_INFRA](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga584f6239ac14e2bedc5e6bd72756423bae5da6b5ad0afa9d29172935e3409f813)、[WIFI_MODE_IBSS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga584f6239ac14e2bedc5e6bd72756423ba2ca83b19fb80412c2e6577164ebb393b)、[WIFI_MODE_AP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga584f6239ac14e2bedc5e6bd72756423ba0e26010a13582e90def7366d6d663fe8)、[WIFI_MODE_P2P_GO](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga584f6239ac14e2bedc5e6bd72756423ba777a0cbe012477f334d9b3fa7999d889)、[WIFI_MODE_P2P_GROUP_FORMATION](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga584f6239ac14e2bedc5e6bd72756423babaabed89e520fb03599ca941d6742521)、[WIFI_MODE_MESH](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga584f6239ac14e2bedc5e6bd72756423baf52eb7740bf223c253ec8754a6defa68)。

Wi-Fi 接口模式（Interface Modes）。

<a id="r_gabdb2a784d4727b71ab44cca04e422c62"></a>

```c
enum wifi_link_mode { WIFI_0 = 0 , WIFI_1 , WIFI_2 , WIFI_3 , WIFI_4 , WIFI_5 , WIFI_6 , WIFI_6E , WIFI_7 }
```

相关声明：[wifi_link_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gabdb2a784d4727b71ab44cca04e422c62)、[WIFI_0](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62a530e059ee3ee741248c212287d3798f8)、[WIFI_1](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62abe63329d11a9642d6d9dec3120d1f36c)、[WIFI_2](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62aaf818813d87ea19fbe8396aff3f0c1d9)、[WIFI_3](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62aeca0be00ba42d701b6f148036a18e362)、[WIFI_4](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62a8e92427770e1ae2a3fe36deff6e6eef2)、[WIFI_5](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62a4c94fcb62c5213c6e1cf46409ef6b824)、[WIFI_6](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62ab9d56217d0abd71f7f824930ea226ffe)、[WIFI_6E](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62a1bbbd42fc347212077fbac6f8be6f6a6)、[WIFI_7](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62a8a121ae16410908526a2ce8c0beb9934)。

Wi-Fi 链路工作模式（Link Operating Modes）。

<a id="r_gad30e29eda65ccafdbd7f11865937b8ea"></a>

```c
enum wifi_scan_type { WIFI_SCAN_TYPE_ACTIVE = 0 , WIFI_SCAN_TYPE_PASSIVE }
```

相关声明：[wifi_scan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad30e29eda65ccafdbd7f11865937b8ea)、[WIFI_SCAN_TYPE_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad30e29eda65ccafdbd7f11865937b8eaa7cb9f32d9cbed0c055394eb3ce0c67d9)、[WIFI_SCAN_TYPE_PASSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad30e29eda65ccafdbd7f11865937b8eaab286c65b4c0e4405b37db8fd7f72808f)。

Wi-Fi 扫描类型（Scanning Types）。

<a id="r_ga0fffeb57b68fb8cdef9d3d571368b8ca"></a>

```c
enum wifi_ps { WIFI_PS_DISABLED = 0 , WIFI_PS_ENABLED }
```

相关声明：[wifi_ps](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga0fffeb57b68fb8cdef9d3d571368b8ca)、[WIFI_PS_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0fffeb57b68fb8cdef9d3d571368b8caa9860ebd60aad1694c2c903e18bbc5e82)、[WIFI_PS_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0fffeb57b68fb8cdef9d3d571368b8caa3c1495662d43fb52261c4137096a4c47)。

Wi-Fi 省电状态（Power Save States）。

<a id="r_gaffae7d2a754be5eb952ad2b83edad54c"></a>

```c
enum wifi_ps_mode { WIFI_PS_MODE_LEGACY = 0 , WIFI_PS_MODE_WMM }
```

相关声明：[wifi_ps_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaffae7d2a754be5eb952ad2b83edad54c)、[WIFI_PS_MODE_LEGACY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaffae7d2a754be5eb952ad2b83edad54ca761cfe837bd3b531d1e58298b5b1c5fd)、[WIFI_PS_MODE_WMM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaffae7d2a754be5eb952ad2b83edad54ca528fb6047805bd00691b3ae14bd5eae5)。

Wi-Fi 省电模式（Power Save Modes）。

<a id="r_ga4a9243eeb974111d6047fd3d8d9cbf35"></a>

```c
enum wifi_operational_modes { WIFI_STA_MODE = BIT(0) , WIFI_MONITOR_MODE = BIT(1) , WIFI_TX_INJECTION_MODE = BIT(2) , WIFI_PROMISCUOUS_MODE = BIT(3) , WIFI_AP_MODE = BIT(4) , WIFI_SOFTAP_MODE = BIT(5) }
```

相关声明：[wifi_operational_modes](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4a9243eeb974111d6047fd3d8d9cbf35)、[WIFI_STA_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4a9243eeb974111d6047fd3d8d9cbf35a340a5486c7da955853acdb005c4781f7)、[WIFI_MONITOR_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4a9243eeb974111d6047fd3d8d9cbf35ad5bc242078274f20949d9afa8c67b696)、[WIFI_TX_INJECTION_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4a9243eeb974111d6047fd3d8d9cbf35a2106a5725118f9b9b2a0ce04453adb74)、[WIFI_PROMISCUOUS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4a9243eeb974111d6047fd3d8d9cbf35aeb9bbb00469b4038f16b8b7cd2c5bf56)、[WIFI_AP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4a9243eeb974111d6047fd3d8d9cbf35aa25a1cb94f2d78baed38752af5d195bd)、[WIFI_SOFTAP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4a9243eeb974111d6047fd3d8d9cbf35ab2463380f240d8a51ef5b02e648c5623)。

Wi-Fi 工作模式（Operational Mode）。

<a id="r_gaa60495242c66a3fac294886856121c1f"></a>

```c
enum wifi_filter { WIFI_PACKET_FILTER_ALL = BIT(0) , WIFI_PACKET_FILTER_MGMT = BIT(1) , WIFI_PACKET_FILTER_DATA = BIT(2) , WIFI_PACKET_FILTER_CTRL = BIT(3) }
```

相关声明：[wifi_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa60495242c66a3fac294886856121c1f)、[WIFI_PACKET_FILTER_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaa60495242c66a3fac294886856121c1fa4ef04395b41e0578bdeb77b5e7b8612b)、[WIFI_PACKET_FILTER_MGMT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaa60495242c66a3fac294886856121c1fa2829d4e8b62d23d9fa5feb7cd9b2b2fc)、[WIFI_PACKET_FILTER_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaa60495242c66a3fac294886856121c1faca13230b05c62ece57186d6f01e5e244)、[WIFI_PACKET_FILTER_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaa60495242c66a3fac294886856121c1fad55696b27a792f0a4aefbcf4ff0182de)。

模式过滤器设置（Mode Filter Settings）。

<a id="r_gad0e998aeb1b27c4f203ca76339d323a3"></a>

```c
enum wifi_twt_operation { WIFI_TWT_SETUP = 0 , WIFI_TWT_TEARDOWN }
```

相关声明：[wifi_twt_operation](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad0e998aeb1b27c4f203ca76339d323a3)、[WIFI_TWT_SETUP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad0e998aeb1b27c4f203ca76339d323a3a127b1ba136c0a8b226378ce6398c4c45)、[WIFI_TWT_TEARDOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad0e998aeb1b27c4f203ca76339d323a3a8b7aef65a36005a1fc29367b9455e41f)。

Wi-Fi 目标唤醒时间操作（Target Wake Time Operations，TWT）。

<a id="r_ga695123cd534e2499f516a07fdc5cafa8"></a>

```c
enum wifi_twt_negotiation_type { WIFI_TWT_INDIVIDUAL = 0 , WIFI_TWT_BROADCAST , WIFI_TWT_WAKE_TBTT }
```

相关声明：[wifi_twt_negotiation_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga695123cd534e2499f516a07fdc5cafa8)、[WIFI_TWT_INDIVIDUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga695123cd534e2499f516a07fdc5cafa8ad8205ed96091863156066d9df874bee0)、[WIFI_TWT_BROADCAST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga695123cd534e2499f516a07fdc5cafa8a66d66faf5c949fa414b163eacb3871fa)、[WIFI_TWT_WAKE_TBTT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga695123cd534e2499f516a07fdc5cafa8a8eef8349e12980c39e63fd11ce2ab978)。

Wi-Fi 目标唤醒时间协商类型（TWT Negotiation Types）。

<a id="r_ga31c78afc89bfdc4b54cee177843f8022"></a>

```c
enum wifi_twt_setup_cmd { WIFI_TWT_SETUP_CMD_REQUEST = 0 , WIFI_TWT_SETUP_CMD_SUGGEST , WIFI_TWT_SETUP_CMD_DEMAND , WIFI_TWT_SETUP_CMD_GROUPING , WIFI_TWT_SETUP_CMD_ACCEPT , WIFI_TWT_SETUP_CMD_ALTERNATE , WIFI_TWT_SETUP_CMD_DICTATE , WIFI_TWT_SETUP_CMD_REJECT }
```

相关声明：[wifi_twt_setup_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga31c78afc89bfdc4b54cee177843f8022)、[WIFI_TWT_SETUP_CMD_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022a7b6568e80a31a17a742c23ae0f6892bd)、[WIFI_TWT_SETUP_CMD_SUGGEST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022abdd60c33f3a61b21c9f72bd66897b648)、[WIFI_TWT_SETUP_CMD_DEMAND](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022a4a687e30a23f1705e5b359b7d7b6366e)、[WIFI_TWT_SETUP_CMD_GROUPING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022a846145fb934c5235a5afea275263c279)、[WIFI_TWT_SETUP_CMD_ACCEPT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022afb7fb9876e2774f45cc7688b0308b64a)、[WIFI_TWT_SETUP_CMD_ALTERNATE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022a8247cf7843a5d2a7ddf48da1c5be9ae1)、[WIFI_TWT_SETUP_CMD_DICTATE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022a9965a5ee6b30a64d6849690f60d859f3)、[WIFI_TWT_SETUP_CMD_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022aed1c84e6699331726aa75477e9a1f565)。

Wi-Fi 目标唤醒时间建立命令（TWT Setup Commands）。

<a id="r_ga4d03aedac13ee4512d7717ac624f319a"></a>

```c
enum wifi_twt_setup_resp_status { WIFI_TWT_RESP_RECEIVED = 0 , WIFI_TWT_RESP_NOT_RECEIVED }
```

相关声明：[wifi_twt_setup_resp_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4d03aedac13ee4512d7717ac624f319a)、[WIFI_TWT_RESP_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4d03aedac13ee4512d7717ac624f319aa0ec181caece9e9d5f12827c6c5390286)、[WIFI_TWT_RESP_NOT_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4d03aedac13ee4512d7717ac624f319aa757054d1ad2033ebc6b9a0fb1f3b2c72)。

Wi-Fi 目标唤醒时间协商状态（TWT Negotiation Status）。

<a id="r_ga97fa304f9a1db2294a93cccd4c93bcf6"></a>

```c
enum wifi_twt_fail_reason { WIFI_TWT_FAIL_UNSPECIFIED , WIFI_TWT_FAIL_CMD_EXEC_FAIL , WIFI_TWT_FAIL_OPERATION_NOT_SUPPORTED , WIFI_TWT_FAIL_UNABLE_TO_GET_IFACE_STATUS , WIFI_TWT_FAIL_DEVICE_NOT_CONNECTED , WIFI_TWT_FAIL_PEER_NOT_HE_CAPAB , WIFI_TWT_FAIL_PEER_NOT_TWT_CAPAB , WIFI_TWT_FAIL_OPERATION_IN_PROGRESS , WIFI_TWT_FAIL_INVALID_FLOW_ID , WIFI_TWT_FAIL_IP_NOT_ASSIGNED , WIFI_TWT_FAIL_FLOW_ALREADY_EXISTS }
```

相关声明：[wifi_twt_fail_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga97fa304f9a1db2294a93cccd4c93bcf6)、[WIFI_TWT_FAIL_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13)、[WIFI_TWT_FAIL_CMD_EXEC_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556)、[WIFI_TWT_FAIL_OPERATION_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d)、[WIFI_TWT_FAIL_UNABLE_TO_GET_IFACE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef)、[WIFI_TWT_FAIL_DEVICE_NOT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831)、[WIFI_TWT_FAIL_PEER_NOT_HE_CAPAB](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860)、[WIFI_TWT_FAIL_PEER_NOT_TWT_CAPAB](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce)、[WIFI_TWT_FAIL_OPERATION_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7)、[WIFI_TWT_FAIL_INVALID_FLOW_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6)、[WIFI_TWT_FAIL_IP_NOT_ASSIGNED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee)、[WIFI_TWT_FAIL_FLOW_ALREADY_EXISTS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c)。

目标唤醒时间错误码（TWT Error Codes）。

<a id="r_gad3709d07aaa3ed59b48f9dd7bd181989"></a>

```c
enum wifi_twt_teardown_status { WIFI_TWT_TEARDOWN_SUCCESS = 0 , WIFI_TWT_TEARDOWN_FAILED }
```

相关声明：[wifi_twt_teardown_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad3709d07aaa3ed59b48f9dd7bd181989)、[WIFI_TWT_TEARDOWN_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad3709d07aaa3ed59b48f9dd7bd181989a17a0d82cff424ff5bdf462b6db63f965)、[WIFI_TWT_TEARDOWN_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad3709d07aaa3ed59b48f9dd7bd181989a53b36533aa40cb076be68cd1c902582d)。

Wi-Fi 目标唤醒时间拆除状态（TWT Teardown Status）。

<a id="r_gabe45d132797047c098041331c8f6f912"></a>

```c
enum wifi_ps_param_type { WIFI_PS_PARAM_STATE , WIFI_PS_PARAM_LISTEN_INTERVAL , WIFI_PS_PARAM_WAKEUP_MODE , WIFI_PS_PARAM_MODE , WIFI_PS_PARAM_EXIT_STRATEGY , WIFI_PS_PARAM_TIMEOUT }
```

相关声明：[wifi_ps_param_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gabe45d132797047c098041331c8f6f912)、[WIFI_PS_PARAM_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabe45d132797047c098041331c8f6f912a4f676a7085b7b0a37e717980412a379d)、[WIFI_PS_PARAM_LISTEN_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabe45d132797047c098041331c8f6f912a1999ab313a62a9208d683fb1d3e01c90)、[WIFI_PS_PARAM_WAKEUP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabe45d132797047c098041331c8f6f912a93ce25e041d81fdaa6c3c77f526a8db8)、[WIFI_PS_PARAM_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabe45d132797047c098041331c8f6f912ac65551112d0fdc28ec3805d2f70ddaab)、[WIFI_PS_PARAM_EXIT_STRATEGY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabe45d132797047c098041331c8f6f912a8eb7bd5dbe14f9262980dfeb5bd85e03)、[WIFI_PS_PARAM_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabe45d132797047c098041331c8f6f912aefc0c3c93b09f30270f8e7914e9c9c29)。

Wi-Fi省电参数（Power Save Parameters）。

<a id="r_gac7f907644847e905d67c709fa4afae7f"></a>

```c
enum wifi_ps_wakeup_mode { WIFI_PS_WAKEUP_MODE_DTIM = 0 , WIFI_PS_WAKEUP_MODE_LISTEN_INTERVAL }
```

相关声明：[wifi_ps_wakeup_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac7f907644847e905d67c709fa4afae7f)、[WIFI_PS_WAKEUP_MODE_DTIM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac7f907644847e905d67c709fa4afae7fad7232d95f68a6ce41cdaedc58444bba6)、[WIFI_PS_WAKEUP_MODE_LISTEN_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac7f907644847e905d67c709fa4afae7facbd61628e83216011745cb225e0c8b30)。

Wi-Fi 省电模式（Power Save Modes）。

<a id="r_ga2d424d1711389fb784e916a87ff854b7"></a>

```c
enum wifi_ps_exit_strategy { WIFI_PS_EXIT_CUSTOM_ALGO = 0 , WIFI_PS_EXIT_EVERY_TIM }
```

相关声明：[wifi_ps_exit_strategy](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga2d424d1711389fb784e916a87ff854b7)、[WIFI_PS_EXIT_CUSTOM_ALGO](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga2d424d1711389fb784e916a87ff854b7aa8e9097d5c86dfc078fa230ca3b41ce5)、[WIFI_PS_EXIT_EVERY_TIM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga2d424d1711389fb784e916a87ff854b7a9aa2663512a5fd0dec84807c4f2db832)。

Wi‑Fi 省电退出策略（Power save exit strategy）。

<a id="r_gad98099584d2222ede93aba42b1fbaff0"></a>

```c
enum wifi_config_ps_param_fail_reason { WIFI_PS_PARAM_FAIL_UNSPECIFIED , WIFI_PS_PARAM_FAIL_CMD_EXEC_FAIL , WIFI_PS_PARAM_FAIL_OPERATION_NOT_SUPPORTED , WIFI_PS_PARAM_FAIL_UNABLE_TO_GET_IFACE_STATUS , WIFI_PS_PARAM_FAIL_DEVICE_NOT_CONNECTED , WIFI_PS_PARAM_FAIL_DEVICE_CONNECTED , WIFI_PS_PARAM_LISTEN_INTERVAL_RANGE_INVALID , WIFI_PS_PARAM_FAIL_INVALID_EXIT_STRATEGY }
```

相关声明：[wifi_config_ps_param_fail_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad98099584d2222ede93aba42b1fbaff0)、[WIFI_PS_PARAM_FAIL_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38)、[WIFI_PS_PARAM_FAIL_CMD_EXEC_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394)、[WIFI_PS_PARAM_FAIL_OPERATION_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093)、[WIFI_PS_PARAM_FAIL_UNABLE_TO_GET_IFACE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3)、[WIFI_PS_PARAM_FAIL_DEVICE_NOT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a)、[WIFI_PS_PARAM_FAIL_DEVICE_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486)、[WIFI_PS_PARAM_LISTEN_INTERVAL_RANGE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f)、[WIFI_PS_PARAM_FAIL_INVALID_EXIT_STRATEGY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0adda816053e0d9a00f243b93b5b7178ce)。

Wi-Fi 省电错误码（Power Save Error Codes）。

<a id="r_ga4fced9c3627d8f65d75e1651b11916b0"></a>

```c
enum wifi_btm_query_reason { WIFI_BTM_QUERY_REASON_UNSPECIFIED = 0 , WIFI_BTM_QUERY_REASON_LOW_RSSI = 16 , WIFI_BTM_QUERY_REASON_LEAVING_ESS = 20 }
```

相关声明：[wifi_btm_query_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4fced9c3627d8f65d75e1651b11916b0)、[WIFI_BTM_QUERY_REASON_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4fced9c3627d8f65d75e1651b11916b0a41376bed59184da60f7c6558d2524c58)、[WIFI_BTM_QUERY_REASON_LOW_RSSI](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4fced9c3627d8f65d75e1651b11916b0a718e2d9c2f18fafc70c389177a4a5257)、[WIFI_BTM_QUERY_REASON_LEAVING_ESS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4fced9c3627d8f65d75e1651b11916b0a5491f6eabeae1cd0faec69b5ced04f49)。

IEEE 802.11v 基本服务集转换管理查询原因（BTM Query Reasons，BSS Transition Management）。

<a id="r_ga83546cf946a9123c563609e8903d9642"></a>

```c
enum wifi_ap_config_param { WIFI_AP_CONFIG_PARAM_MAX_INACTIVITY = BIT(0) , WIFI_AP_CONFIG_PARAM_MAX_NUM_STA = BIT(1) , WIFI_AP_CONFIG_PARAM_BANDWIDTH = BIT(2) , WIFI_AP_CONFIG_PARAM_HT_CAPAB = BIT(3) , WIFI_AP_CONFIG_PARAM_VHT_CAPAB = BIT(4) }
```

相关声明：[wifi_ap_config_param](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga83546cf946a9123c563609e8903d9642)、[WIFI_AP_CONFIG_PARAM_MAX_INACTIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga83546cf946a9123c563609e8903d9642a2ab06f57b7e2b75b18e919e7777e6a7c)、[WIFI_AP_CONFIG_PARAM_MAX_NUM_STA](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga83546cf946a9123c563609e8903d9642abdcec2dcf5a23339b90d5da94fd19958)、[WIFI_AP_CONFIG_PARAM_BANDWIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga83546cf946a9123c563609e8903d9642a1c9f37033909236e6a2259465dda4ef7)、[WIFI_AP_CONFIG_PARAM_HT_CAPAB](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga83546cf946a9123c563609e8903d9642ac357562788ce489023e9e66296401199)、[WIFI_AP_CONFIG_PARAM_VHT_CAPAB](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga83546cf946a9123c563609e8903d9642ac22e71c91a433674f0a96ec853539902)。

Wi-Fi 接入点模式配置参数（AP Mode Configuration Parameter）。

<a id="r_ga7ef91a39c2cc6bb454d870a8a80f8439"></a>

```c
enum wifi_config_param { WIFI_CONFIG_PARAM_OKC = BIT(0) }
```

相关声明：[wifi_config_param](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7ef91a39c2cc6bb454d870a8a80f8439)、[WIFI_CONFIG_PARAM_OKC](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga7ef91a39c2cc6bb454d870a8a80f8439ab8ef08f95a3b287c0a8be2e5ab0480c3)。

Wi-Fi 站点模式配置参数（STA Mode Configuration Parameter）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.4\_函数（Functions）

<a id="r_ga9bb9f658d7806e42b3ee351fb3e7dfa0"></a>

```c
const char * wifi_security_txt (enum wifi_security_type security)
```

相关声明：[wifi_security_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga9bb9f658d7806e42b3ee351fb3e7dfa0)、[wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)。

获取易读安全类型名称（Security Type Name）的辅助函数。

<a id="r_gaf67f2900be88fdf3f282400d09f2ab88"></a>

```c
const char * wifi_wpa3_enterprise_txt (enum wifi_wpa3_enterprise_type wpa3_ent)
```

相关声明：[wifi_wpa3_enterprise_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf67f2900be88fdf3f282400d09f2ab88)、[wifi_wpa3_enterprise_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga48fea1f0c7d2700cef47068f96c6b71a)。

获取易读 WPA3 企业安全类型名称（WPA3 Enterprise Security Type Name）的辅助函数。

<a id="r_gaf957fd93d98988347e009038cb694c04"></a>

```c
const char * wifi_wep_key_type_txt (enum wifi_wep_key_type wep_key_type)
```

相关声明：[wifi_wep_key_type_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf957fd93d98988347e009038cb694c04)、[wifi_wep_key_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gafc901312b5988481b34d05a031d6c0db)。

获取易读 WEP 密钥类型名称（WEP Key Type Name）的辅助函数。

<a id="r_ga22354241197a9227fdba77e67d471f5c"></a>

```c
const char * wifi_mfp_txt (enum wifi_mfp_options mfp)
```

相关声明：[wifi_mfp_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga22354241197a9227fdba77e67d471f5c)、[wifi_mfp_options](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1f252da47d9650023d7fff6d08e49c76)。

获取易读管理帧保护名称（MFP Name）的辅助函数。

<a id="r_ga44f875bf0d931b66d582f5dca2d65ed5"></a>

```c
const char * wifi_band_txt (enum wifi_frequency_bands band)
```

相关声明：[wifi_band_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga44f875bf0d931b66d582f5dca2d65ed5)、[wifi_frequency_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1e2f0439a322355fa7368ea880c9c15d)。

获取易读频段名称（Frequency Band Name）的辅助函数。

<a id="r_ga7ff13294abf2dc27acbb3021afb2faee"></a>

```c
const char * wifi_bandwidth_txt (enum wifi_frequency_bandwidths bandwidth)
```

相关声明：[wifi_bandwidth_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7ff13294abf2dc27acbb3021afb2faee)、[wifi_frequency_bandwidths](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3b01cead3c2eb4581fe85e2aaaffbd49)。

获取易读频率带宽名称（Frequency Bandwidth Name）的辅助函数。

<a id="r_ga03d306912dc96178e21d3c82c104582f"></a>

```c
const char * wifi_state_txt (enum wifi_iface_state state)
```

相关声明：[wifi_state_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga03d306912dc96178e21d3c82c104582f)、[wifi_iface_state](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga981961f747b919d61d3ccbd41e4508b4)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

获取易读接口状态名称（Interface State Name）的辅助函数。

<a id="r_gad78536ce1f30accfa45f258b6bf8c73d"></a>

```c
const char * wifi_mode_txt (enum wifi_iface_mode mode)
```

相关声明：[wifi_mode_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad78536ce1f30accfa45f258b6bf8c73d)、[wifi_iface_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga584f6239ac14e2bedc5e6bd72756423b)。

获取易读接口模式名称（Interface Mode Name）的辅助函数。

<a id="r_ga0d9d6e2150fb187025300904357f7b4d"></a>

```c
const char * wifi_link_mode_txt (enum wifi_link_mode link_mode)
```

相关声明：[wifi_link_mode_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga0d9d6e2150fb187025300904357f7b4d)、[wifi_link_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gabdb2a784d4727b71ab44cca04e422c62)。

获取易读链路模式名称（Link Mode Name）的辅助函数。

<a id="r_gafbeb5f7fa97fd2ba0c691da0f8853ef2"></a>

```c
const char * wifi_ps_txt (enum wifi_ps ps_name)
```

相关声明：[wifi_ps_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gafbeb5f7fa97fd2ba0c691da0f8853ef2)、[wifi_ps](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga0fffeb57b68fb8cdef9d3d571368b8ca)。

获取易读省电名称（Power Save Name）的辅助函数。

<a id="r_gadb21d49f64e04fba59433e51d5b3481c"></a>

```c
const char * wifi_ps_mode_txt (enum wifi_ps_mode ps_mode)
```

相关声明：[wifi_ps_mode_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadb21d49f64e04fba59433e51d5b3481c)、[wifi_ps_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaffae7d2a754be5eb952ad2b83edad54c)。

获取易读省电模式名称（Power Save Mode Name）的辅助函数。

<a id="r_gadb125925e851bf7569424cd4295e7712"></a>

```c
const char * wifi_twt_operation_txt (enum wifi_twt_operation twt_operation)
```

相关声明：[wifi_twt_operation_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadb125925e851bf7569424cd4295e7712)、[wifi_twt_operation](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad0e998aeb1b27c4f203ca76339d323a3)。

获取易读目标唤醒时间操作名称（TWT Operation Name）的辅助函数。

<a id="r_ga6a74e999d63ee491df68447219ef2a0d"></a>

```c
const char * wifi_twt_negotiation_type_txt (enum wifi_twt_negotiation_type twt_negotiation)
```

相关声明：[wifi_twt_negotiation_type_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga6a74e999d63ee491df68447219ef2a0d)、[wifi_twt_negotiation_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga695123cd534e2499f516a07fdc5cafa8)。

获取易读目标唤醒时间协商类型名称（TWT Negotiation Type Name）的辅助函数。

<a id="r_gae3ca047cc6ef6b6a2e44ba6574d41a44"></a>

```c
const char * wifi_twt_setup_cmd_txt (enum wifi_twt_setup_cmd twt_setup)
```

相关声明：[wifi_twt_setup_cmd_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae3ca047cc6ef6b6a2e44ba6574d41a44)、[wifi_twt_setup_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga31c78afc89bfdc4b54cee177843f8022)。

获取易读目标唤醒时间建立命令名称（TWT Setup Command Name）的辅助函数。

<a id="r_gab2e6a6e1d8358a8f34d67bd632709b3d"></a>

```c
static const char * wifi_twt_get_err_code_str (int16_t err_no)
```

相关声明：[wifi_twt_get_err_code_str](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gab2e6a6e1d8358a8f34d67bd632709b3d)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

获取易读目标唤醒时间错误码名称（TWT Error Code Name）的辅助函数。

<a id="r_ga6fd645f891234136b3028574a0af9666"></a>

```c
const char * wifi_ps_wakeup_mode_txt (enum wifi_ps_wakeup_mode ps_wakeup_mode)
```

相关声明：[wifi_ps_wakeup_mode_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga6fd645f891234136b3028574a0af9666)、[wifi_ps_wakeup_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac7f907644847e905d67c709fa4afae7f)。

获取易读省电唤醒模式名称（Power Save Wakeup Mode Name）的辅助函数。

<a id="r_ga034bfcd7891caeb31820579b5ee22a7b"></a>

```c
const char * wifi_ps_exit_strategy_txt (enum wifi_ps_exit_strategy ps_exit_strategy)
```

相关声明：[wifi_ps_exit_strategy_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga034bfcd7891caeb31820579b5ee22a7b)、[wifi_ps_exit_strategy](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga2d424d1711389fb784e916a87ff854b7)。

获取易读省电退出策略名称（Power Save Exit Strategy Name）的辅助函数。

<a id="r_ga8b72e7989964963a25f42ed1dba240a0"></a>

```c
static const char * wifi_ps_get_config_err_code_str (int16_t err_no)
```

相关声明：[wifi_ps_get_config_err_code_str](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga8b72e7989964963a25f42ed1dba240a0)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

获取易读省电错误码名称（Power Save Error Code Name）的辅助函数。

<a id="r_gac18305e124523b7cc9eb6adb05d987a8"></a>

```c
const char * wifi_conn_status_txt (enum wifi_conn_status status)
```

相关声明：[wifi_conn_status_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac18305e124523b7cc9eb6adb05d987a8)、[wifi_conn_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga86a5741e54aeb3e290142b0de217b8a8)。

根据状态码（Status Code）获取易读状态名称（Status Name）的辅助函数。


## 15.5\_原页交叉引用（Cross References）

- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_runtime_reference/P067_wifi.h_源码浏览.md)
- [wifi_cipher_desc](../network_core_model_reference/P165_wifi_cipher_desc_结构体.md)
- [wifi_eap_cipher_config](../network_core_model_reference/P171_wifi_eap_cipher_config_结构体.md)
- [wifi_eap_config](../network_core_model_reference/P172_wifi_eap_config_结构体.md)
- [WIFI_COUNTRY_CODE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga6766ef7bcb001f1fb526a4083b6cd8bc)
- [WIFI_SSID_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad62c60666c9fdffe2e0e9c4388f87886)
- [WIFI_PSK_MIN_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa8e19abf8c85f237ba5033740ceff553)
- [WIFI_PSK_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad7c3b99c974b342935180a28fdc5ddfc)
- [WIFI_WEP_KEY_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf466d0b11462b3f190d579702cb9ee51)
- [WIFI_PSK_PBKDF2_KEY_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7d6424d6770b2357f0b8abb456ae53fc)
- [WIFI_SAE_PSWD_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gab63fa744cc2e049cfd635ab0a187971f)
- [WIFI_MAC_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga29409ff83a53c6464decdde9bdd04de6)
- [WIFI_ENT_IDENTITY_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac6904487661f157274b0b60833f6684a)
- [WIFI_ENT_PSWD_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae2fd55924f4078187431f7a1184f217f)
- [WIFI_CHANNEL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga260e473dac1e823fd298a2c982470e0b)
- [WIFI_CHANNEL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga8ea9141108f93b419f6a6530bf67bd95)
- [WIFI_CHANNEL_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3876cd718af9f8a7b3682546da854544)
- [WIFI_INTERFACE_INDEX_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa1a74ef94af57a7ea966c691c065a46d)
- [WIFI_INTERFACE_INDEX_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa6cbecd7d4197d453038d3da7ef6be7b)
- [wifi_conn_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga86a5741e54aeb3e290142b0de217b8a8)
- [WIFI_STATUS_CONN_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd)
- [WIFI_STATUS_CONN_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44)
- [WIFI_STATUS_CONN_WRONG_PASSWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8)
- [WIFI_STATUS_CONN_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563)
- [WIFI_STATUS_CONN_AP_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4)
- [WIFI_STATUS_CONN_AUTH_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8a008abc5c55c4ea7409f5b16be4f68a91)
- [WIFI_STATUS_CONN_ASSOC_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8aeaccd303a2c836347555886f746b54eb)
- [WIFI_STATUS_CONN_LAST_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f)
- [WIFI_STATUS_DISCONN_FIRST_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga86a5741e54aeb3e290142b0de217b8a8abe1401e5d516c0d63291add15e558b18)
- [wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)
- [WIFI_SECURITY_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca3f0a729e3c906d9c398a9fba163a0a9e)
- [WIFI_SECURITY_TYPE_PSK](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca1b9f70d6425eaa5a94211826a91c2368)
- [WIFI_SECURITY_TYPE_PSK_SHA256](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca0554b0fd5a6233aba5e25b035488380e)
- [WIFI_SECURITY_TYPE_SAE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca00d5a50935f70344f03c778055755c2f)
- [WIFI_SECURITY_TYPE_SAE_HNP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9caab329c818e10cbe98aac1f9c30849c91)
- [WIFI_SECURITY_TYPE_SAE_H2E](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca1e45d14be678d0693b3f03f73fc5b0df)
- [WIFI_SECURITY_TYPE_SAE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca4beacdae98f8ca155609d2fd660c5ed0)
- [WIFI_SECURITY_TYPE_WAPI](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca37ab810084b3e024731f440e708b363d)
- [WIFI_SECURITY_TYPE_EAP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9cacce1e8fbfbf71fb4d669e9d0bfb04f80)
- [WIFI_SECURITY_TYPE_EAP_TLS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca85bcce61e75c01eb95083523e8925a40)
- [WIFI_SECURITY_TYPE_WEP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca39b793d7f7c49dee4e60a5c6e6831724)
- [WIFI_SECURITY_TYPE_WPA_PSK](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca4fd23c30c3b666132903fef27fd0651a)
- [WIFI_SECURITY_TYPE_WPA_AUTO_PERSONAL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca275483ee9bced209eb2d131825f599ff)
- [WIFI_SECURITY_TYPE_DPP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca6cf0bd5db90deaa6b35f7afe122e8b5f)
- [WIFI_SECURITY_TYPE_EAP_PEAP_MSCHAPV2](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9caaa1dbea0100af80ca48ad594cddb4212)
- [WIFI_SECURITY_TYPE_EAP_PEAP_GTC](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca0c9db910757c5a715a5e88089362fab5)
- [WIFI_SECURITY_TYPE_EAP_TTLS_MSCHAPV2](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca3a20bf15c1e51313629789e6abe0273d)
- [WIFI_SECURITY_TYPE_EAP_PEAP_TLS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca6d2e5f72b8bf76f093ab79be2a4b9477)
- [WIFI_SECURITY_TYPE_FT_PSK](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca42e49ccccfed285d32aa9f36bcfd5fc5)
- [WIFI_SECURITY_TYPE_FT_SAE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9cab7bcc9437586d4940126a2ae1efdb092)
- [WIFI_SECURITY_TYPE_FT_EAP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca00d759c3332700100ca7be612abeeda5)
- [WIFI_SECURITY_TYPE_FT_EAP_SHA384](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca52aa23f908a4fae0864f2e187b89af93)
- [WIFI_SECURITY_TYPE_SAE_EXT_KEY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca64221ce0052ce510e16537a32c67bb02)
- [WIFI_SECURITY_TYPE_WEP_OPEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca798e97bb232dfa2bc75b5e6865d78bf7)
- [WIFI_SECURITY_TYPE_WEP_SHARED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9cadb96b16c24d4975e88f674b08cab7122)
- [WIFI_SECURITY_TYPE_OWE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca3a91d5c899e0789587a94ab5981d98ca)
- [WIFI_SECURITY_TYPE_PSK_SHA384](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9ca1b6d3f896a853bd9c1f03409f0f32814)
- [WIFI_SECURITY_TYPE_FT_PSK_SHA384](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggadde31a04fa25ed805115c6b31854cd9cace9ee870a64b87aa7f97a146bb61951f)
- [wifi_wep_key_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gafc901312b5988481b34d05a031d6c0db)
- [WIFI_WEP_KEY_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggafc901312b5988481b34d05a031d6c0dba58f0ce2c50683011de9e36b55879e104)
- [WIFI_WEP_KEY_TYPE_64](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggafc901312b5988481b34d05a031d6c0dba8f89728c41b4aac1b803a558474c1484)
- [WIFI_WEP_KEY_TYPE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggafc901312b5988481b34d05a031d6c0dba0a0b1dd584525ee634069c81b91cb97f)
- [wifi_eap_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga92b6fa6755491c3bd61f895213d07331)
- [WIFI_EAP_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga92b6fa6755491c3bd61f895213d07331a39edcc7a267ce608a1e818948b5d172b)
- [WIFI_EAP_TYPE_GTC](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga92b6fa6755491c3bd61f895213d07331a64daad77662868322e638da6531a5c0f)
- [WIFI_EAP_TYPE_TLS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga92b6fa6755491c3bd61f895213d07331a505b4b888231dd1fbc169d612d8f0c38)
- [WIFI_EAP_TYPE_TTLS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga92b6fa6755491c3bd61f895213d07331a35fce37fccb3d27596c4e0a531109dac)
- [WIFI_EAP_TYPE_PEAP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga92b6fa6755491c3bd61f895213d07331a8e619153aa3dad398c6ced36605f5e3f)
- [WIFI_EAP_TYPE_MSCHAPV2](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga92b6fa6755491c3bd61f895213d07331a37f7681b1fb5d7165010ec941018882f)
- [wifi_wpa3_enterprise_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga48fea1f0c7d2700cef47068f96c6b71a)
- [WIFI_WPA3_ENTERPRISE_NA](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga48fea1f0c7d2700cef47068f96c6b71aa7c34eb5cf3e76c3c1b45c424436adbb1)
- [WIFI_WPA3_ENTERPRISE_SUITEB](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga48fea1f0c7d2700cef47068f96c6b71aaec90b38cb8fb95ff3a679da473537589)
- [WIFI_WPA3_ENTERPRISE_SUITEB_192](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga48fea1f0c7d2700cef47068f96c6b71aa577671035478f3a385b8e4fdf6abf5fa)
- [WIFI_WPA3_ENTERPRISE_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga48fea1f0c7d2700cef47068f96c6b71aaf13490bee764dd77f770f07bf3dac3fa)
- [wifi_eap_tls_cipher_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga218525a9d9ee64524f983e52d5767562)
- [WIFI_EAP_TLS_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga218525a9d9ee64524f983e52d5767562a38f97de2297f9df6e4ac3cecfd0799df)
- [WIFI_EAP_TLS_ECC_P384](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga218525a9d9ee64524f983e52d5767562ae44c04c2d1510385fe43827dbe6026f9)
- [WIFI_EAP_TLS_RSA_3K](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga218525a9d9ee64524f983e52d5767562ac5436dc7d2bbeded043b1102ee592e17)
- [wifi_cipher_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7f7b23ac019ca504a2006f0376735645)
- [WPA_CAPA_ENC_CCMP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga7f7b23ac019ca504a2006f0376735645ac0af8c48884381d3be7e9a2b7f3b54e1)
- [WPA_CAPA_ENC_GCMP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga7f7b23ac019ca504a2006f0376735645a88fe5cd8b7777b931d869cb76ae65b1d)
- [WPA_CAPA_ENC_GCMP_256](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga7f7b23ac019ca504a2006f0376735645a60599a3fdfad99c6ec1471d4973556c4)
- [wifi_group_mgmt_cipher_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf84d5e1a68393483fc6063c06b8f26e0)
- [WPA_CAPA_ENC_BIP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaf84d5e1a68393483fc6063c06b8f26e0a7d5bfccaca027a00e834a8db03f8b8f8)
- [WPA_CAPA_ENC_BIP_GMAC_128](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaf84d5e1a68393483fc6063c06b8f26e0ab15e42ab1ba05c1296b19cbfff2ccf70)
- [WPA_CAPA_ENC_BIP_GMAC_256](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaf84d5e1a68393483fc6063c06b8f26e0ae437a3b3abd043b184e545a4ec40c096)
- [wifi_mfp_options](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1f252da47d9650023d7fff6d08e49c76)
- [WIFI_MFP_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1f252da47d9650023d7fff6d08e49c76a260e7b4688790ed39f4f7dc70547e969)
- [WIFI_MFP_OPTIONAL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1f252da47d9650023d7fff6d08e49c76a3ffdc747c7c70f7c1b70c96292f57fbf)
- [WIFI_MFP_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1f252da47d9650023d7fff6d08e49c76af118a2f047c13db04d164235fa15f840)
- [wifi_frequency_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1e2f0439a322355fa7368ea880c9c15d)
- [WIFI_FREQ_BAND_2_4_GHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11)
- [WIFI_FREQ_BAND_5_GHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895)
- [WIFI_FREQ_BAND_6_GHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15da4f82878368ada29ce8986dd173efdcc0)
- [WIFI_FREQ_BAND_SUB_1_GHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15daeb2366af7a35fa929882f7842abb4211)
- [WIFI_FREQ_BAND_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15daea3a12c499228420adc9f3aac21d67a5)
- [WIFI_FREQ_BAND_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga1e2f0439a322355fa7368ea880c9c15da8091041d87f7df93223527a31e7e76a5)
- [wifi_frequency_bandwidths](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga3b01cead3c2eb4581fe85e2aaaffbd49)
- [WIFI_FREQ_BANDWIDTH_20MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49ae5efe45d5211477322968e55014d22d5)
- [WIFI_FREQ_BANDWIDTH_40MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49a9f984c246be1976cf1b799c4aed02ea1)
- [WIFI_FREQ_BANDWIDTH_80MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49a2c445a7a6345a66a41248bde2f7bf8cb)
- [WIFI_FREQ_BANDWIDTH_1MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49a94c8cbcef66fc09604cf5e1a033c4bdc)
- [WIFI_FREQ_BANDWIDTH_2MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49aa9036134a2d668f8e86e617628c4b134)
- [WIFI_FREQ_BANDWIDTH_4MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49a7f78a7780a1059bf6fcedda5d96b5510)
- [WIFI_FREQ_BANDWIDTH_8MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49ada0acd85e6a825be12fe2295c960b93c)
- [WIFI_FREQ_BANDWIDTH_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49af57b996c36f950143c9f23a25d402b90)
- [WIFI_FREQ_BANDWIDTH_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga3b01cead3c2eb4581fe85e2aaaffbd49a4e45ec9ffe32912a5673f9bbffeeef2d)
- [wifi_iface_state](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga981961f747b919d61d3ccbd41e4508b4)
- [WIFI_STATE_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f)
- [WIFI_STATE_INTERFACE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c)
- [WIFI_STATE_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598)
- [WIFI_STATE_SCANNING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b)
- [WIFI_STATE_AUTHENTICATING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba)
- [WIFI_STATE_ASSOCIATING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b)
- [WIFI_STATE_ASSOCIATED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc)
- [WIFI_STATE_4WAY_HANDSHAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969)
- [WIFI_STATE_GROUP_HANDSHAKE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e)
- [WIFI_STATE_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f)
- [wifi_iface_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga584f6239ac14e2bedc5e6bd72756423b)
- [WIFI_MODE_INFRA](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga584f6239ac14e2bedc5e6bd72756423bae5da6b5ad0afa9d29172935e3409f813)
- [WIFI_MODE_IBSS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga584f6239ac14e2bedc5e6bd72756423ba2ca83b19fb80412c2e6577164ebb393b)
- [WIFI_MODE_AP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga584f6239ac14e2bedc5e6bd72756423ba0e26010a13582e90def7366d6d663fe8)
- [WIFI_MODE_P2P_GO](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga584f6239ac14e2bedc5e6bd72756423ba777a0cbe012477f334d9b3fa7999d889)
- [WIFI_MODE_P2P_GROUP_FORMATION](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga584f6239ac14e2bedc5e6bd72756423babaabed89e520fb03599ca941d6742521)
- [WIFI_MODE_MESH](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga584f6239ac14e2bedc5e6bd72756423baf52eb7740bf223c253ec8754a6defa68)
- [wifi_link_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gabdb2a784d4727b71ab44cca04e422c62)
- [WIFI_0](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62a530e059ee3ee741248c212287d3798f8)
- [WIFI_1](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62abe63329d11a9642d6d9dec3120d1f36c)
- [WIFI_2](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62aaf818813d87ea19fbe8396aff3f0c1d9)
- [WIFI_3](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62aeca0be00ba42d701b6f148036a18e362)
- [WIFI_4](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62a8e92427770e1ae2a3fe36deff6e6eef2)
- [WIFI_5](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62a4c94fcb62c5213c6e1cf46409ef6b824)
- [WIFI_6](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62ab9d56217d0abd71f7f824930ea226ffe)
- [WIFI_6E](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62a1bbbd42fc347212077fbac6f8be6f6a6)
- [WIFI_7](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabdb2a784d4727b71ab44cca04e422c62a8a121ae16410908526a2ce8c0beb9934)
- [wifi_scan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad30e29eda65ccafdbd7f11865937b8ea)
- [WIFI_SCAN_TYPE_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad30e29eda65ccafdbd7f11865937b8eaa7cb9f32d9cbed0c055394eb3ce0c67d9)
- [WIFI_SCAN_TYPE_PASSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad30e29eda65ccafdbd7f11865937b8eaab286c65b4c0e4405b37db8fd7f72808f)
- [wifi_ps](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga0fffeb57b68fb8cdef9d3d571368b8ca)
- [WIFI_PS_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0fffeb57b68fb8cdef9d3d571368b8caa9860ebd60aad1694c2c903e18bbc5e82)
- [WIFI_PS_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga0fffeb57b68fb8cdef9d3d571368b8caa3c1495662d43fb52261c4137096a4c47)
- [wifi_ps_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaffae7d2a754be5eb952ad2b83edad54c)
- [WIFI_PS_MODE_LEGACY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaffae7d2a754be5eb952ad2b83edad54ca761cfe837bd3b531d1e58298b5b1c5fd)
- [WIFI_PS_MODE_WMM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaffae7d2a754be5eb952ad2b83edad54ca528fb6047805bd00691b3ae14bd5eae5)
- [wifi_operational_modes](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4a9243eeb974111d6047fd3d8d9cbf35)
- [WIFI_STA_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4a9243eeb974111d6047fd3d8d9cbf35a340a5486c7da955853acdb005c4781f7)
- [WIFI_MONITOR_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4a9243eeb974111d6047fd3d8d9cbf35ad5bc242078274f20949d9afa8c67b696)
- [WIFI_TX_INJECTION_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4a9243eeb974111d6047fd3d8d9cbf35a2106a5725118f9b9b2a0ce04453adb74)
- [WIFI_PROMISCUOUS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4a9243eeb974111d6047fd3d8d9cbf35aeb9bbb00469b4038f16b8b7cd2c5bf56)
- [WIFI_AP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4a9243eeb974111d6047fd3d8d9cbf35aa25a1cb94f2d78baed38752af5d195bd)
- [WIFI_SOFTAP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4a9243eeb974111d6047fd3d8d9cbf35ab2463380f240d8a51ef5b02e648c5623)
- [wifi_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaa60495242c66a3fac294886856121c1f)
- [WIFI_PACKET_FILTER_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaa60495242c66a3fac294886856121c1fa4ef04395b41e0578bdeb77b5e7b8612b)
- [WIFI_PACKET_FILTER_MGMT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaa60495242c66a3fac294886856121c1fa2829d4e8b62d23d9fa5feb7cd9b2b2fc)
- [WIFI_PACKET_FILTER_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaa60495242c66a3fac294886856121c1faca13230b05c62ece57186d6f01e5e244)
- [WIFI_PACKET_FILTER_CTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggaa60495242c66a3fac294886856121c1fad55696b27a792f0a4aefbcf4ff0182de)
- [wifi_twt_operation](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad0e998aeb1b27c4f203ca76339d323a3)
- [WIFI_TWT_SETUP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad0e998aeb1b27c4f203ca76339d323a3a127b1ba136c0a8b226378ce6398c4c45)
- [WIFI_TWT_TEARDOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad0e998aeb1b27c4f203ca76339d323a3a8b7aef65a36005a1fc29367b9455e41f)
- [wifi_twt_negotiation_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga695123cd534e2499f516a07fdc5cafa8)
- [WIFI_TWT_INDIVIDUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga695123cd534e2499f516a07fdc5cafa8ad8205ed96091863156066d9df874bee0)
- [WIFI_TWT_BROADCAST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga695123cd534e2499f516a07fdc5cafa8a66d66faf5c949fa414b163eacb3871fa)
- [WIFI_TWT_WAKE_TBTT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga695123cd534e2499f516a07fdc5cafa8a8eef8349e12980c39e63fd11ce2ab978)
- [wifi_twt_setup_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga31c78afc89bfdc4b54cee177843f8022)
- [WIFI_TWT_SETUP_CMD_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022a7b6568e80a31a17a742c23ae0f6892bd)
- [WIFI_TWT_SETUP_CMD_SUGGEST](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022abdd60c33f3a61b21c9f72bd66897b648)
- [WIFI_TWT_SETUP_CMD_DEMAND](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022a4a687e30a23f1705e5b359b7d7b6366e)
- [WIFI_TWT_SETUP_CMD_GROUPING](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022a846145fb934c5235a5afea275263c279)
- [WIFI_TWT_SETUP_CMD_ACCEPT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022afb7fb9876e2774f45cc7688b0308b64a)
- [WIFI_TWT_SETUP_CMD_ALTERNATE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022a8247cf7843a5d2a7ddf48da1c5be9ae1)
- [WIFI_TWT_SETUP_CMD_DICTATE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022a9965a5ee6b30a64d6849690f60d859f3)
- [WIFI_TWT_SETUP_CMD_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga31c78afc89bfdc4b54cee177843f8022aed1c84e6699331726aa75477e9a1f565)
- [wifi_twt_setup_resp_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4d03aedac13ee4512d7717ac624f319a)
- [WIFI_TWT_RESP_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4d03aedac13ee4512d7717ac624f319aa0ec181caece9e9d5f12827c6c5390286)
- [WIFI_TWT_RESP_NOT_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4d03aedac13ee4512d7717ac624f319aa757054d1ad2033ebc6b9a0fb1f3b2c72)
- [wifi_twt_fail_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga97fa304f9a1db2294a93cccd4c93bcf6)
- [WIFI_TWT_FAIL_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13)
- [WIFI_TWT_FAIL_CMD_EXEC_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556)
- [WIFI_TWT_FAIL_OPERATION_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d)
- [WIFI_TWT_FAIL_UNABLE_TO_GET_IFACE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef)
- [WIFI_TWT_FAIL_DEVICE_NOT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831)
- [WIFI_TWT_FAIL_PEER_NOT_HE_CAPAB](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860)
- [WIFI_TWT_FAIL_PEER_NOT_TWT_CAPAB](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce)
- [WIFI_TWT_FAIL_OPERATION_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7)
- [WIFI_TWT_FAIL_INVALID_FLOW_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6)
- [WIFI_TWT_FAIL_IP_NOT_ASSIGNED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee)
- [WIFI_TWT_FAIL_FLOW_ALREADY_EXISTS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c)
- [wifi_twt_teardown_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad3709d07aaa3ed59b48f9dd7bd181989)
- [WIFI_TWT_TEARDOWN_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad3709d07aaa3ed59b48f9dd7bd181989a17a0d82cff424ff5bdf462b6db63f965)
- [WIFI_TWT_TEARDOWN_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad3709d07aaa3ed59b48f9dd7bd181989a53b36533aa40cb076be68cd1c902582d)
- [wifi_ps_param_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gabe45d132797047c098041331c8f6f912)
- [WIFI_PS_PARAM_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabe45d132797047c098041331c8f6f912a4f676a7085b7b0a37e717980412a379d)
- [WIFI_PS_PARAM_LISTEN_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabe45d132797047c098041331c8f6f912a1999ab313a62a9208d683fb1d3e01c90)
- [WIFI_PS_PARAM_WAKEUP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabe45d132797047c098041331c8f6f912a93ce25e041d81fdaa6c3c77f526a8db8)
- [WIFI_PS_PARAM_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabe45d132797047c098041331c8f6f912ac65551112d0fdc28ec3805d2f70ddaab)
- [WIFI_PS_PARAM_EXIT_STRATEGY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabe45d132797047c098041331c8f6f912a8eb7bd5dbe14f9262980dfeb5bd85e03)
- [WIFI_PS_PARAM_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggabe45d132797047c098041331c8f6f912aefc0c3c93b09f30270f8e7914e9c9c29)
- [wifi_ps_wakeup_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac7f907644847e905d67c709fa4afae7f)
- [WIFI_PS_WAKEUP_MODE_DTIM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac7f907644847e905d67c709fa4afae7fad7232d95f68a6ce41cdaedc58444bba6)
- [WIFI_PS_WAKEUP_MODE_LISTEN_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac7f907644847e905d67c709fa4afae7facbd61628e83216011745cb225e0c8b30)
- [wifi_ps_exit_strategy](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga2d424d1711389fb784e916a87ff854b7)
- [WIFI_PS_EXIT_CUSTOM_ALGO](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga2d424d1711389fb784e916a87ff854b7aa8e9097d5c86dfc078fa230ca3b41ce5)
- [WIFI_PS_EXIT_EVERY_TIM](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga2d424d1711389fb784e916a87ff854b7a9aa2663512a5fd0dec84807c4f2db832)
- [wifi_config_ps_param_fail_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad98099584d2222ede93aba42b1fbaff0)
- [WIFI_PS_PARAM_FAIL_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38)
- [WIFI_PS_PARAM_FAIL_CMD_EXEC_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394)
- [WIFI_PS_PARAM_FAIL_OPERATION_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093)
- [WIFI_PS_PARAM_FAIL_UNABLE_TO_GET_IFACE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3)
- [WIFI_PS_PARAM_FAIL_DEVICE_NOT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a)
- [WIFI_PS_PARAM_FAIL_DEVICE_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486)
- [WIFI_PS_PARAM_LISTEN_INTERVAL_RANGE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f)
- [WIFI_PS_PARAM_FAIL_INVALID_EXIT_STRATEGY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggad98099584d2222ede93aba42b1fbaff0adda816053e0d9a00f243b93b5b7178ce)
- [wifi_btm_query_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4fced9c3627d8f65d75e1651b11916b0)
- [WIFI_BTM_QUERY_REASON_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4fced9c3627d8f65d75e1651b11916b0a41376bed59184da60f7c6558d2524c58)
- [WIFI_BTM_QUERY_REASON_LOW_RSSI](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4fced9c3627d8f65d75e1651b11916b0a718e2d9c2f18fafc70c389177a4a5257)
- [WIFI_BTM_QUERY_REASON_LEAVING_ESS](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga4fced9c3627d8f65d75e1651b11916b0a5491f6eabeae1cd0faec69b5ced04f49)
- [wifi_ap_config_param](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga83546cf946a9123c563609e8903d9642)
- [WIFI_AP_CONFIG_PARAM_MAX_INACTIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga83546cf946a9123c563609e8903d9642a2ab06f57b7e2b75b18e919e7777e6a7c)
- [WIFI_AP_CONFIG_PARAM_MAX_NUM_STA](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga83546cf946a9123c563609e8903d9642abdcec2dcf5a23339b90d5da94fd19958)
- [WIFI_AP_CONFIG_PARAM_BANDWIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga83546cf946a9123c563609e8903d9642a1c9f37033909236e6a2259465dda4ef7)
- [WIFI_AP_CONFIG_PARAM_HT_CAPAB](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga83546cf946a9123c563609e8903d9642ac357562788ce489023e9e66296401199)
- [WIFI_AP_CONFIG_PARAM_VHT_CAPAB](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga83546cf946a9123c563609e8903d9642ac22e71c91a433674f0a96ec853539902)
- [wifi_config_param](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7ef91a39c2cc6bb454d870a8a80f8439)
- [WIFI_CONFIG_PARAM_OKC](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gga7ef91a39c2cc6bb454d870a8a80f8439ab8ef08f95a3b287c0a8be2e5ab0480c3)
- [wifi_security_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga9bb9f658d7806e42b3ee351fb3e7dfa0)
- [wifi_wpa3_enterprise_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf67f2900be88fdf3f282400d09f2ab88)
- [wifi_wep_key_type_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaf957fd93d98988347e009038cb694c04)
- [wifi_mfp_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga22354241197a9227fdba77e67d471f5c)
- [wifi_band_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga44f875bf0d931b66d582f5dca2d65ed5)
- [wifi_bandwidth_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga7ff13294abf2dc27acbb3021afb2faee)
- [wifi_state_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga03d306912dc96178e21d3c82c104582f)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [wifi_mode_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad78536ce1f30accfa45f258b6bf8c73d)
- [wifi_link_mode_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga0d9d6e2150fb187025300904357f7b4d)
- [wifi_ps_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gafbeb5f7fa97fd2ba0c691da0f8853ef2)
- [wifi_ps_mode_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadb21d49f64e04fba59433e51d5b3481c)
- [wifi_twt_operation_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadb125925e851bf7569424cd4295e7712)
- [wifi_twt_negotiation_type_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga6a74e999d63ee491df68447219ef2a0d)
- [wifi_twt_setup_cmd_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae3ca047cc6ef6b6a2e44ba6574d41a44)
- [wifi_twt_get_err_code_str](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gab2e6a6e1d8358a8f34d67bd632709b3d)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [wifi_ps_wakeup_mode_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga6fd645f891234136b3028574a0af9666)
- [wifi_ps_exit_strategy_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga034bfcd7891caeb31820579b5ee22a7b)
- [wifi_ps_get_config_err_code_str](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga8b72e7989964963a25f42ed1dba240a0)
- [wifi_conn_status_txt](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac18305e124523b7cc9eb6adb05d987a8)

<a id="header-details"></a>

---

[上一章](P014_zephyr__drivers__usb_c__usbc_tcpc.h_文件参考.md) · [返回大纲](大纲.md)
