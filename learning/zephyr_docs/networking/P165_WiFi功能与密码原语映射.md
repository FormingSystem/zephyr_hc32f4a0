---
id: learning.zephyr-docs.networking.page-165
title: WiFi功能与密码原语映射
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/wifi_crypto.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第165章\_WiFi功能与密码原语映射

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/wifi_crypto.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 本页范围

本页将 Zephyr 通过基于 hostap 的 `wpa_supplicant` 支持的 Wi-Fi 功能，映射到下层 MbedTLS 密码原语（Cryptographic Primitives）。可以据此了解哪些功能需要大整数（Bignum）、椭圆曲线 Diffie–Hellman（Elliptic Curve Diffie–Hellman，ECDH）、传输层安全（Transport Layer Security，TLS）等，以及启用 [`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA) 后，哪些路径使用传统密码接口（Legacy Crypto，MbedTLS Legacy APIs），哪些使用平台安全架构密码接口（Platform Security Architecture，PSA Crypto APIs）。

实现位于 hostap 模块：`crypto_mbedtls_alt.c` 负责通用密码操作，`tls_mbedtls_alt.c` 负责 TLS／EAP。本页只讨论 MbedTLS 后端。

> 译注：本页是官方映射说明的完整翻译，表中的“传统”和“PSA”描述软件接口路径，不能直接推断硬件加速、密钥隔离、固件大小或特定开发板是否支持。本文中的“传统”也不等于算法已经不安全；WEP 的弃用说明则是原文明确指出的安全问题。

## 2. 功能集合：来自 hostap Kconfig

功能由 Kconfig 控制，相关选项包括：

- [`CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP)：有线等效保密（Wired Equivalent Privacy，WEP），属于旧式功能。
- [`CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_COMMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3_COMMON)：在 WPA3 实现选择项 `WIFI_NM_WPA_SUPPLICANT_WPA3_IMPLEMENTATION` 中选择内部（Internal）或外部（External）实现时，提供 WPA3-SAE；默认内部实现。[`CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPA3) 是无提示符（Promptless）配置项，选择内部实现后会打开使用大整数的内部 SAE 路径。在 `prj.conf` 中应设置实现选择项，而不是直接设置这个无提示符符号。
- [`CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_DPP)：Wi-Fi Easy Connect，使用设备配置协议（Device Provisioning Protocol，DPP）。
- [`CONFIG_WIFI_NM_WPA_SUPPLICANT_WPS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_WPS)：Wi-Fi 保护设置（Wi-Fi Protected Setup，WPS）。
- [`CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_P2P)：点对点（Peer-to-Peer，P2P）／Wi-Fi Direct，同时需要 WPS。
- [`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)：可扩展认证协议（Extensible Authentication Protocol，EAP），包括 EAP-TLS、EAP-TTLS-MSCHAPV2、EAP-PEAP-MSCHAPV2、EAP-PEAP-GTC、EAP-PEAP-TLS。
- 只要密码实现没有设置为 `CRYPTO_NONE`，就可使用 WPA2-PSK 和 WPA2-PSK-256。

其中 SAE 指对等实体同时认证（Simultaneous Authentication of Equals），PSK 指预共享密钥（Pre-Shared Key）。功能配置的当前定义可对照官方[modules/hostap/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/hostap/Kconfig)。

## 3. Wi-Fi 功能与 MbedTLS 密码原语的映射

下表保留原文的全部 10 个功能行及各列说明。EC 指椭圆曲线（Elliptic Curve），HMAC 指基于散列的消息认证码（Hash-Based Message Authentication Code），AES 指高级加密标准（Advanced Encryption Standard），PBKDF2 指基于口令的密钥派生函数 2（Password-Based Key Derivation Function 2）。

| 功能（Feature） | 密码原语（Crypto Primitives） | 传统密码接口（Legacy Crypto） | PSA 密码接口（PSA Crypto） |
| --- | --- | --- | --- |
| WPA3-SAE | 大整数（mpi）、取模、幂运算；EC 群；HMAC-SHA256；AES（CCMP）。SAE 使用 Dragonfly 的口令元素（Password Element，PWE），涉及大整数和取模。 | 大整数 `mbedtls_mpi`；EC；HMAC、AES（除非采用 PSA 构建）。 | 启用 PSA 时，散列、HMAC、AES 使用 PSA；大整数和 EC 仍使用传统接口。 |
| SAE-PK | 与 WPA3-SAE 相同，再加 ECDH 和 EC 密钥操作；原文将其描述为“基于证书的 SAE”（certificate-based SAE）。 | ECDH／EC 密钥操作使用传统 MbedTLS，或按配置使用 PSA ECDH。 | ECDH 可以使用 PSA；大整数和 SAE 核心仍使用传统接口。 |
| DPP（Easy Connect） | ECDH（P-256、P-384、P-521）；EC 密钥生成、签名、验签；散列和 AES。DPP2 加入 PKCS#7，DPP3 加入混合公钥加密（Hybrid Public Key Encryption，HPKE）。 | ECDH、EC、RSA（若使用）；TLS／密码层中的 X.509 和证书签名请求（Certificate Signing Request，CSR）。 | 散列、HMAC、AES 通过 PSA；ECDH／EC 可能使用 PSA；TLS／CSR／PKCS#7／HPKE 层仍使用传统接口。 |
| WPA2-PSK / WPA2-PSK-256 | PBKDF2-SHA1（原文称 `-256` 使用 SHA256）；HMAC；AES（CCMP）；OMAC1-AES（原文标注用于密钥封装）。 | 禁用 PSA 时，PBKDF2、HMAC、AES、CMAC 全部通过 MbedTLS。 | 启用 PSA 时，PBKDF2、HMAC、AES、OMAC1 通过 PSA 实现。 |
| WEP | RC4／ARC4 流密码（Stream Cipher）；部分封装可选用 AES。已弃用。 | 仅使用传统 MbedTLS，当前代码中没有 WEP 的 PSA 路径。 | 不适用，WEP 尚未迁移到 PSA。 |
| WPS | 有限域 Diffie–Hellman（DH）；大整数；散列、HMAC、AES、TLS 伪随机函数（TLS-PRF）。注册器（Registrar）使用 TLS。 | DH 使用 `mbedtls_dhm`，大整数使用 `mbedtls_mpi`；TLS 位于 `tls_mbedtls_alt`。 | 散列、HMAC、AES、PBKDF2 使用 PSA；DH、大整数和 TLS 仍使用传统接口。 |
| EAP-TLS / EAP-TTLS / EAP-PEAP | TLS 1.2，可选 TLS 1.3；RSA；X.509 解析与验证；密码套件（Cipher Suites）中的散列、HMAC 和 AES。 | 完整 TLS 栈（`mbedtls_ssl_*`、`mbedtls_x509_*`）；RSA；原表称 `tls_mbedtls_alt` 中没有 PSA。 | TLS 层仍使用传统接口；下层散列、HMAC、AES 可以在 `crypto_mbedtls_alt` 中使用 PSA。 |
| EAP-PWD | TLS-PRF；大整数；有限域 DH；可选 EC；散列和 HMAC。 | 大整数、DH、EC（若使用）通过传统 MbedTLS。 | 散列和 HMAC 通过 PSA；大整数、DH、EC 仍使用传统接口。 |
| EAP-IKEV2 | 密码算法（AES）、大整数、DH；TLS-PRF 风格操作。 | 传统密码算法、大整数和 DH 接口。 | AES、散列、HMAC 通过 PSA；大整数、DH 仍使用传统接口。 |
| Open（开放网络） | 不进行认证或加密。 | 不适用。 | 不适用。 |

> 原文提示：必须显式启用 [`CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP) 才能使用 WEP。它已弃用且不安全，只用于旧网络兼容。

## 4. 按密码操作汇总传统与 PSA 路径

启用 [`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA) 后，原文将 `crypto_mbedtls_alt.c` 及 `supp_psa_api.h`／`supp_psa_api.c` 中的操作划分如下：

| 操作（Operation） | API | 使用者／说明 |
| --- | --- | --- |
| 消息摘要（Message Digests）：MD5、SHA1、SHA256、SHA384、SHA512 | PSA | 原表未补充说明。 |
| HMAC：上述所有散列类型 | PSA | 原表未补充说明。 |
| PBKDF2-SHA1 | PSA | WPA2-PSK 密钥派生。 |
| AES：块操作、CBC、CTR、OMAC1-AES | PSA | 密钥封装、CCMP 等。 |
| 大整数：`crypto_bignum_*` | 传统接口 | SAE、EAP-PWD、EAP-EKE、EAP-IKEV2、WPS；hostap 中没有 PSA 大整数接口。 |
| ECDH／EC 密钥操作 | 传统接口 | DPP、SAE-PK、EAP-PWD（EC）。配置 `MBEDTLS_ECDH_C`／[`CONFIG_PSA_WANT_ALG_ECDH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_ECDH) 时可能由 PSA 支撑，封装层共用。 |
| TLS／SSL | 传统接口 | EAP-TLS、EAP-TTLS、EAP-PEAP；完整协议栈在 `tls_mbedtls_alt.c` 中。 |
| RSA | 传统接口 | TLS、X.509。 |
| X.509／CSR | 传统接口 | 解析和生成。 |
| WEP | 传统接口 | 没有 PSA 路径。 |

原文据此总结：WPA2-PSK 和 WPA2-PSK-256 的密码操作仅使用 PSA；WPA3-SAE、DPP、SAE-PK、WPS 和企业 EAP 仍依赖传统大整数、EC 或 TLS。各功能的影响见上一节映射表。

## 5. 译注：源码版本与表格边界

上述表格保留官方页面的分类，不能把它当作永久不变的接口实现清单。本次按 Zephyr 官方 `west.yml` 中固定的 hostap 修订 `33921a8a77c56bddfe196a11935009cededc3bb3` 核对以下入口，网页和模块源码的具体摘要均记录在[来源记录](../SOURCES.md)：

- [crypto_mbedtls_alt.c](https://github.com/zephyrproject-rtos/hostap/blob/33921a8a77c56bddfe196a11935009cededc3bb3/src/crypto/crypto_mbedtls_alt.c)：通用密码操作。
- [tls_mbedtls_alt.c](https://github.com/zephyrproject-rtos/hostap/blob/33921a8a77c56bddfe196a11935009cededc3bb3/src/crypto/tls_mbedtls_alt.c)：TLS 及证书验证。
- [supp_psa_api.c](https://github.com/zephyrproject-rtos/hostap/blob/33921a8a77c56bddfe196a11935009cededc3bb3/port/mbedtls/supp_psa_api.c)与[supp_psa_api.h](https://github.com/zephyrproject-rtos/hostap/blob/33921a8a77c56bddfe196a11935009cededc3bb3/port/mbedtls/supp_psa_api.h)：PSA 适配，位于 `port/mbedtls`。

当前 `crypto_mbedtls_alt.c` 已有更多针对 Mbed TLS 4／tf-psa-crypto 的 PSA 调用与条件分支，因此“关闭某一个 PSA 选项就全部回到传统接口”不可脱离实际模块和库版本使用。原表把 OMAC1-AES 与密钥封装并列，也不能理解为它们是同一个接口；源码分别实现消息认证与 `aes_wrap()` 等密钥封装操作。

原表“WPA2-PSK-256 使用 PBKDF2-SHA256”的说法还需与实际密钥派生调用链区分。核对到的 `pbkdf2_sha1()` 明确向 PSA 适配层传递 `MBEDTLS_MD_SHA1`；仅凭安全模式名称中的 `256`，不能推导口令到密钥的 PBKDF2 散列算法。本页没有把原表改造成经所有模式实测的结论，也没有运行握手、密码学测试或硬件加速验证。


<a id="wi-fi-feature-to-crypto-mapping"></a>
<a id="wifi-crypto-mapping"></a>
<a id="feature-set-from-hostap-kconfig"></a>
<a id="feature-crypto-primitives-mbedtls"></a>
<a id="id1"></a>
<a id="summary-legacy-vs-psa-mbedtls-backend"></a>
<a id="id2"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：WiFi凭据库](P164_WiFi凭据库.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：IEEE802154无线网络](P170_IEEE802154无线网络.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P164_WiFi凭据库.md) · [返回大纲](大纲.md) · [下一章](P166_WiFi示例目录.md)

</details>

<!-- reading-navigation:end -->
