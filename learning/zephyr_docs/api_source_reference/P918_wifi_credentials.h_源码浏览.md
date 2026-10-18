---
id: learning.zephyr-docs.api-source-reference.page-918
title: wifi_credentials.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wifi__credentials_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第918章\_wifi\_credentials.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/wifi__credentials_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/wifi__credentials_8h.html)。

## 918.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="foldopen00065"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="foldopen00108"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="foldopen00123"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="agroup__wifi__credentials_html_ga1b5525c7a6a7ca312236a2c674d94055"></a>
<a id="agroup__wifi__credentials_html_ga28b13d11cca692921252e98788552957"></a>
<a id="agroup__wifi__credentials_html_ga30c9333f10e8e8d03f268fb5c9a69562"></a>
<a id="agroup__wifi__credentials_html_ga3a5b20d07afc52cc452a9c55998ebcf7"></a>
<a id="agroup__wifi__credentials_html_ga3d83001e713206ec07f94996137537d5"></a>
<a id="agroup__wifi__credentials_html_ga467ef5e15a637c33cb1926a3548ffb9e"></a>
<a id="agroup__wifi__credentials_html_ga548522fbc6b5fdcff4585c34f3565c82"></a>
<a id="agroup__wifi__credentials_html_ga644d29db8091512a977f8e27b245975e"></a>
<a id="agroup__wifi__credentials_html_gade76c60899e42fc2af5f7e93143c21ad"></a>
<a id="agroup__wifi__credentials_html_gaf9d3ffe6c9120a7fbc248c3ee66f42fa"></a>
<a id="agroup__wifi__mgmt_html_ga29409ff83a53c6464decdde9bdd04de6"></a>
<a id="agroup__wifi__mgmt_html_gad62c60666c9fdffe2e0e9c4388f87886"></a>
<a id="agroup__wifi__mgmt_html_gadde31a04fa25ed805115c6b31854cd9c"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructwifi__credentials__enterprise_html"></a>
<a id="astructwifi__credentials__enterprise_html_a33525f5af6db7813b8f19554fd5c04f0"></a>
<a id="astructwifi__credentials__enterprise_html_a58ba430cb51a80009639263ebe412895"></a>
<a id="astructwifi__credentials__enterprise_html_a74d046dbfdc2f1208848c564c8d98843"></a>
<a id="astructwifi__credentials__enterprise_html_a757f7cfbaf1874be1300f68bf42ebc9d"></a>
<a id="astructwifi__credentials__enterprise_html_a8871721054c824b056fcbb9492bf96aa"></a>
<a id="astructwifi__credentials__enterprise_html_aadd1fe1f5d3f3983a5cd82d5d33a4ff4"></a>
<a id="astructwifi__credentials__enterprise_html_ab532c721b2e10c44bf660d67ca63f994"></a>
<a id="astructwifi__credentials__enterprise_html_aeb480da7b9b4c7e0f4ab3b86977032f9"></a>
<a id="astructwifi__credentials__header_html"></a>
<a id="astructwifi__credentials__header_html_a28d311d5535c7569bda860dca7fd08f6"></a>
<a id="astructwifi__credentials__header_html_a2c39cdc6f7023560de61fb353a178369"></a>
<a id="astructwifi__credentials__header_html_a52cd2e481d3ebf141c671e9a67f5a224"></a>
<a id="astructwifi__credentials__header_html_a59b8b99ad309c0cc2cb6c5438554fefe"></a>
<a id="astructwifi__credentials__header_html_a5b873555b2154e22367644c2805c0494"></a>
<a id="astructwifi__credentials__header_html_a605b62d473586f3d8312aa1c80731ee6"></a>
<a id="astructwifi__credentials__header_html_a99ccc993d609632f42650aabe9fc861b"></a>
<a id="astructwifi__credentials__header_html_a9ab939e7cb212a85d2612d5582e2336d"></a>
<a id="astructwifi__credentials__header_html_ab5bfa4ac972a8ad1ba4b395fad48a923"></a>
<a id="astructwifi__credentials__header_html_ab6b02e3c88ff13a323cbafdf9af9ba1f"></a>
<a id="astructwifi__credentials__header_html_acbbd421fda51f23d2243dd9573b05d71"></a>
<a id="astructwifi__credentials__personal_html"></a>
<a id="astructwifi__credentials__personal_html_a40f13f70ee0dd797d31b643cc754440c"></a>
<a id="astructwifi__credentials__personal_html_a4a8201ecec087203b69ade5d7547538c"></a>
<a id="astructwifi__credentials__personal_html_a627104585a2f6d58e2f899563c2993ad"></a>
<a id="awifi_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_WIFI_CREDENTIALS_H_
#define ZEPHYR_INCLUDE_NET_WIFI_CREDENTIALS_H_

#include <zephyr/types.h>
#include <zephyr/net/wifi.h>
#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif



#define WIFI_CREDENTIALS_FLAG_BSSID        BIT(0)
#define WIFI_CREDENTIALS_FLAG_FAVORITE     BIT(1)
#define WIFI_CREDENTIALS_FLAG_2_4GHz       BIT(2)
#define WIFI_CREDENTIALS_FLAG_5GHz         BIT(3)
#define WIFI_CREDENTIALS_FLAG_6GHz         BIT(4)
#define WIFI_CREDENTIALS_FLAG_MFP_REQUIRED BIT(5)
#define WIFI_CREDENTIALS_FLAG_MFP_DISABLED BIT(6)
#define WIFI_CREDENTIALS_FLAG_ANONYMOUS_IDENTITY  BIT(7)
#define WIFI_CREDENTIALS_FLAG_KEY_PASSWORD  BIT(8)

#define WIFI_CREDENTIALS_MAX_PASSWORD_LEN                                                          \
        MAX(WIFI_PSK_MAX_LEN, CONFIG_WIFI_CREDENTIALS_SAE_PASSWORD_LENGTH)

struct wifi_credentials_header {
        enum wifi_security_type type;

        char ssid[WIFI_SSID_MAX_LEN];

        size_t ssid_len;

        uint32_t flags;

        uint32_t timeout;

        uint8_t bssid[WIFI_MAC_ADDR_LEN];

        uint8_t channel;

        char anon_id[16];

        uint8_t aid_length;

        char key_passwd[16];

        uint8_t key_passwd_length;
};

struct wifi_credentials_personal {
        struct wifi_credentials_header header;

        char password[WIFI_CREDENTIALS_MAX_PASSWORD_LEN];

        size_t password_len;
};

struct wifi_credentials_enterprise {
        struct wifi_credentials_header header;

        size_t identity_len;

        size_t anonymous_identity_len;

        size_t password_len;

        size_t ca_cert_len;

        size_t client_cert_len;

        size_t private_key_len;

        size_t private_key_pw_len;
};

int wifi_credentials_get_by_ssid_personal(const char *ssid, size_t ssid_len,
                                          enum wifi_security_type *type, uint8_t *bssid_buf,
                                          size_t bssid_buf_len, char *password_buf,
                                          size_t password_buf_len, size_t *password_len,
                                          uint32_t *flags, uint8_t *channel, uint32_t *timeout);

int wifi_credentials_set_personal(const char *ssid, size_t ssid_len, enum wifi_security_type type,
                                  const uint8_t *bssid, size_t bssid_len, const char *password,
                                  size_t password_len, uint32_t flags, uint8_t channel,
                                  uint32_t timeout);

int wifi_credentials_get_by_ssid_personal_struct(const char *ssid, size_t ssid_len,
                                                 struct wifi_credentials_personal *buf);

int wifi_credentials_set_personal_struct(const struct wifi_credentials_personal *creds);

int wifi_credentials_delete_by_ssid(const char *ssid, size_t ssid_len);

bool wifi_credentials_is_empty(void);

int wifi_credentials_delete_all(void);

typedef void (*wifi_credentials_ssid_cb)(void *cb_arg, const char *ssid, size_t ssid_len);

void wifi_credentials_for_each_ssid(wifi_credentials_ssid_cb cb, void *cb_arg);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_WIFI_CREDENTIALS_H_ */
```

## 918.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 284 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_WIFI_CREDENTIALS_H_`。

## 918.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/wifi__credentials_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/net/wifi.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [wifi_credentials_header](../network_core_model_reference/P169_wifi_credentials_header_结构体.md)
- [wifi_security_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c)
- [type](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#a5b873555b2154e22367644c2805c0494)
- [ssid](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#a52cd2e481d3ebf141c671e9a67f5a224)
- [WIFI_SSID_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad62c60666c9fdffe2e0e9c4388f87886)
- [ssid_len](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#ab5bfa4ac972a8ad1ba4b395fad48a923)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flags](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#a59b8b99ad309c0cc2cb6c5438554fefe)
- [timeout](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#ab6b02e3c88ff13a323cbafdf9af9ba1f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bssid](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#a28d311d5535c7569bda860dca7fd08f6)
- [WIFI_MAC_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga29409ff83a53c6464decdde9bdd04de6)
- [channel](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#a9ab939e7cb212a85d2612d5582e2336d)
- [anon_id](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#acbbd421fda51f23d2243dd9573b05d71)
- [aid_length](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#a2c39cdc6f7023560de61fb353a178369)
- [key_passwd](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#a99ccc993d609632f42650aabe9fc861b)
- [key_passwd_length](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#a605b62d473586f3d8312aa1c80731ee6)
- [wifi_credentials_personal](../network_core_model_reference/P170_wifi_credentials_personal_结构体.md)
- [header](../network_core_model_reference/P170_wifi_credentials_personal_结构体.md#a40f13f70ee0dd797d31b643cc754440c)
- [password](../network_core_model_reference/P170_wifi_credentials_personal_结构体.md#a4a8201ecec087203b69ade5d7547538c)
- [WIFI_CREDENTIALS_MAX_PASSWORD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#gaf9d3ffe6c9120a7fbc248c3ee66f42fa)
- [password_len](../network_core_model_reference/P170_wifi_credentials_personal_结构体.md#a627104585a2f6d58e2f899563c2993ad)
- [wifi_credentials_enterprise](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md)
- [header](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md#a58ba430cb51a80009639263ebe412895)
- [identity_len](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md#aadd1fe1f5d3f3983a5cd82d5d33a4ff4)
- [anonymous_identity_len](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md#a8871721054c824b056fcbb9492bf96aa)
- [password_len](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md#aeb480da7b9b4c7e0f4ab3b86977032f9)
- [ca_cert_len](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md#a74d046dbfdc2f1208848c564c8d98843)
- [client_cert_len](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md#a33525f5af6db7813b8f19554fd5c04f0)
- [private_key_len](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md#a757f7cfbaf1874be1300f68bf42ebc9d)
- [private_key_pw_len](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md#ab532c721b2e10c44bf660d67ca63f994)
- [wifi_credentials_get_by_ssid_personal](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga548522fbc6b5fdcff4585c34f3565c82)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [wifi_credentials_set_personal](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga28b13d11cca692921252e98788552957)
- [wifi_credentials_get_by_ssid_personal_struct](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga3d83001e713206ec07f94996137537d5)
- [wifi_credentials_set_personal_struct](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga1b5525c7a6a7ca312236a2c674d94055)
- [wifi_credentials_delete_by_ssid](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga644d29db8091512a977f8e27b245975e)
- [wifi_credentials_is_empty](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga467ef5e15a637c33cb1926a3548ffb9e)
- [wifi_credentials_delete_all](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#gade76c60899e42fc2af5f7e93143c21ad)
- [wifi_credentials_ssid_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga30c9333f10e8e8d03f268fb5c9a69562)
- [wifi_credentials_for_each_ssid](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html#ga3a5b20d07afc52cc452a9c55998ebcf7)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [wifi_credentials_enterprise::client_cert_len](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md#a33525f5af6db7813b8f19554fd5c04f0)
- [wifi_credentials_enterprise::header](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md#a58ba430cb51a80009639263ebe412895)
- [wifi_credentials_enterprise::ca_cert_len](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md#a74d046dbfdc2f1208848c564c8d98843)
- [wifi_credentials_enterprise::private_key_len](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md#a757f7cfbaf1874be1300f68bf42ebc9d)
- [wifi_credentials_enterprise::anonymous_identity_len](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md#a8871721054c824b056fcbb9492bf96aa)
- [wifi_credentials_enterprise::identity_len](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md#aadd1fe1f5d3f3983a5cd82d5d33a4ff4)
- [wifi_credentials_enterprise::private_key_pw_len](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md#ab532c721b2e10c44bf660d67ca63f994)
- [wifi_credentials_enterprise::password_len](../network_core_model_reference/P168_wifi_credentials_enterprise_结构体.md#aeb480da7b9b4c7e0f4ab3b86977032f9)
- [wifi_credentials_header::bssid](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#a28d311d5535c7569bda860dca7fd08f6)
- [wifi_credentials_header::aid_length](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#a2c39cdc6f7023560de61fb353a178369)
- [wifi_credentials_header::ssid](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#a52cd2e481d3ebf141c671e9a67f5a224)
- [wifi_credentials_header::flags](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#a59b8b99ad309c0cc2cb6c5438554fefe)
- [wifi_credentials_header::type](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#a5b873555b2154e22367644c2805c0494)
- [wifi_credentials_header::key_passwd_length](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#a605b62d473586f3d8312aa1c80731ee6)
- [wifi_credentials_header::key_passwd](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#a99ccc993d609632f42650aabe9fc861b)
- [wifi_credentials_header::channel](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#a9ab939e7cb212a85d2612d5582e2336d)
- [wifi_credentials_header::ssid_len](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#ab5bfa4ac972a8ad1ba4b395fad48a923)
- [wifi_credentials_header::timeout](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#ab6b02e3c88ff13a323cbafdf9af9ba1f)
- [wifi_credentials_header::anon_id](../network_core_model_reference/P169_wifi_credentials_header_结构体.md#acbbd421fda51f23d2243dd9573b05d71)
- [wifi_credentials_personal::header](../network_core_model_reference/P170_wifi_credentials_personal_结构体.md#a40f13f70ee0dd797d31b643cc754440c)
- [wifi_credentials_personal::password](../network_core_model_reference/P170_wifi_credentials_personal_结构体.md#a4a8201ecec087203b69ade5d7547538c)
- [wifi_credentials_personal::password_len](../network_core_model_reference/P170_wifi_credentials_personal_结构体.md#a627104585a2f6d58e2f899563c2993ad)
- [wifi.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi_8h.html)

---

[上一章](P917_wifi_certs.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P919_wifi_nm.h_源码浏览.md)
