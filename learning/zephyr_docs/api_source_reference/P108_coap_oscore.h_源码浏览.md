---
id: learning.zephyr-docs.api-source-reference.page-108
title: coap_oscore.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/coap__oscore_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第108章\_coap\_oscore.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/coap__oscore_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/coap__oscore_8h.html)。

## 108.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
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
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00037"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00069"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="foldopen00163"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="acoap_8h_html"></a>
<a id="agroup__coap__oscore_html_ga2e53e54122bc7c00c8bf67918617714a"></a>
<a id="agroup__coap__oscore_html_ga41bc77478b88bf7ca0f04f1ed0a2a0d1"></a>
<a id="agroup__coap__oscore_html_ga7193e52c30307dcc319d9347fade7dbe"></a>
<a id="agroup__coap__oscore_html_gad189c86f6afad030884f96778ed98091"></a>
<a id="agroup__coap__oscore_html_gga41bc77478b88bf7ca0f04f1ed0a2a0d1abd3a2ccfa28e081e9d0672bd835949bd"></a>
<a id="agroup__coap__oscore_html_ggad189c86f6afad030884f96778ed98091a7e2d8a3abb742efbe6afaeee0dd80123"></a>
<a id="agroup__ip__4__6_html_ga361fe60d9b96001f74363788352858a0"></a>
<a id="anet__ip_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astructcoap__oscore__exchange_html"></a>
<a id="astructcoap__oscore__exchange_html_a17cb77ffec08aeb0c808986a5d213ef2"></a>
<a id="astructcoap__oscore__exchange_html_a4742ebc7d9858fa1b31f09eed3a266e1"></a>
<a id="astructcoap__oscore__exchange_html_a4bc063a4f3e275fb22880fd93a052c2f"></a>
<a id="astructcoap__oscore__exchange_html_a8115ef4326b8739e6f73a8e5dd70e748"></a>
<a id="astructcoap__oscore__exchange_html_a8a2114940e704221746fda5e4888df51"></a>
<a id="astructcoap__oscore__exchange_html_ab97aabcc192841eb9646e187ae3409c3"></a>
<a id="astructcoap__oscore__init__params_html"></a>
<a id="astructcoap__oscore__init__params_html_a0ad550ea2dc25001f78054a843ae2118"></a>
<a id="astructcoap__oscore__init__params_html_a1108ec5f1f6d01995149bbef0430278c"></a>
<a id="astructcoap__oscore__init__params_html_a149618d292ea959fed2eb1aa4b61e03f"></a>
<a id="astructcoap__oscore__init__params_html_a1e9ed9e0b5d27133519cc639629f5d66"></a>
<a id="astructcoap__oscore__init__params_html_a1eb4865020de525243b7a6e8cae2cf9f"></a>
<a id="astructcoap__oscore__init__params_html_a2c1c9a3175976ee35194ec54404eae4a"></a>
<a id="astructcoap__oscore__init__params_html_a3cab68148e70cf453545058fdb0e94e3"></a>
<a id="astructcoap__oscore__init__params_html_a5180b28768cc1396c27bb8f712919a7d"></a>
<a id="astructcoap__oscore__init__params_html_a5b6b967e34473ddc2a3d9f9f19656340"></a>
<a id="astructcoap__oscore__init__params_html_a6b4842301e3de5b5b6a27b3f5b7f2b16"></a>
<a id="astructcoap__oscore__init__params_html_a836d7cd5a6181fff740aa4958b3217ca"></a>
<a id="astructcoap__oscore__init__params_html_a923f137c01c062e6fa596589d14b1321"></a>
<a id="astructcoap__oscore__init__params_html_a9c5b4efd2f490c65c79b72317e7d703f"></a>

```c
/*
 * Copyright (c) 2026 Martin Schröder <info@swedishembedded.com>
 * Copyright (c) 2026 Siemens AG
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_COAP_OSCORE_H_
#define ZEPHYR_INCLUDE_NET_COAP_OSCORE_H_

#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>

#include <zephyr/net/net_ip.h>
#include <zephyr/net/coap.h>

#ifdef __cplusplus
extern "C" {
#endif


struct coap_oscore_context;

enum coap_oscore_aead_alg {
        COAP_OSCORE_AEAD_AES_CCM_16_64_128 = 0,
};

enum coap_oscore_hkdf {
        COAP_OSCORE_HKDF_SHA_256 = 0,
};

struct coap_oscore_init_params {
        const uint8_t *master_secret;
        size_t master_secret_len;

        const uint8_t *sender_id;
        size_t sender_id_len;

        const uint8_t *recipient_id;
        size_t recipient_id_len;

        const uint8_t *master_salt;
        size_t master_salt_len;

        const uint8_t *id_context;
        size_t id_context_len;

        enum coap_oscore_aead_alg aead_alg;
        enum coap_oscore_hkdf hkdf;

        bool fresh_master_secret_salt;
};

int coap_oscore_context_add(const struct coap_oscore_init_params *params,
                            struct coap_oscore_context **ctx);

int coap_oscore_context_remove(struct coap_oscore_context *ctx);

struct coap_oscore_exchange {
        struct net_sockaddr_storage addr;
        net_socklen_t addr_len;
        uint8_t token[COAP_TOKEN_MAX_LEN];
        uint8_t tkl;
        int64_t timestamp;
        struct coap_oscore_context *ctx;
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_COAP_OSCORE_H_ */
```

## 108.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Martin Schröder <info@swedishembedded.com>。

版权（Copyright）：© 2026 Siemens AG。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 178 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_COAP_OSCORE_H_`。

## 108.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/coap__oscore_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h.html)
- [coap_oscore_aead_alg](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#gad189c86f6afad030884f96778ed98091)
- [COAP_OSCORE_AEAD_AES_CCM_16_64_128](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#ggad189c86f6afad030884f96778ed98091a7e2d8a3abb742efbe6afaeee0dd80123)
- [coap_oscore_hkdf](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#ga41bc77478b88bf7ca0f04f1ed0a2a0d1)
- [COAP_OSCORE_HKDF_SHA_256](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#gga41bc77478b88bf7ca0f04f1ed0a2a0d1abd3a2ccfa28e081e9d0672bd835949bd)
- [coap_oscore_init_params](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [master_secret](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a6b4842301e3de5b5b6a27b3f5b7f2b16)
- [master_secret_len](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a836d7cd5a6181fff740aa4958b3217ca)
- [sender_id](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a9c5b4efd2f490c65c79b72317e7d703f)
- [sender_id_len](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a1eb4865020de525243b7a6e8cae2cf9f)
- [recipient_id](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a5180b28768cc1396c27bb8f712919a7d)
- [recipient_id_len](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a1108ec5f1f6d01995149bbef0430278c)
- [master_salt](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a149618d292ea959fed2eb1aa4b61e03f)
- [master_salt_len](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a5b6b967e34473ddc2a3d9f9f19656340)
- [id_context](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a0ad550ea2dc25001f78054a843ae2118)
- [id_context_len](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a1e9ed9e0b5d27133519cc639629f5d66)
- [aead_alg](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a923f137c01c062e6fa596589d14b1321)
- [hkdf](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a2c1c9a3175976ee35194ec54404eae4a)
- [fresh_master_secret_salt](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a3cab68148e70cf453545058fdb0e94e3)
- [coap_oscore_context_add](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#ga2e53e54122bc7c00c8bf67918617714a)
- [coap_oscore_context_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__oscore.html#ga7193e52c30307dcc319d9347fade7dbe)
- [coap_oscore_exchange](../network_application_model_reference/P011_coap_oscore_exchange_结构体.md)
- [addr](../network_application_model_reference/P011_coap_oscore_exchange_结构体.md#ab97aabcc192841eb9646e187ae3409c3)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [addr_len](../network_application_model_reference/P011_coap_oscore_exchange_结构体.md#a17cb77ffec08aeb0c808986a5d213ef2)
- [token](../network_application_model_reference/P011_coap_oscore_exchange_结构体.md#a8a2114940e704221746fda5e4888df51)
- [tkl](../network_application_model_reference/P011_coap_oscore_exchange_结构体.md#a4742ebc7d9858fa1b31f09eed3a266e1)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [timestamp](../network_application_model_reference/P011_coap_oscore_exchange_结构体.md#a8115ef4326b8739e6f73a8e5dd70e748)
- [ctx](../network_application_model_reference/P011_coap_oscore_exchange_结构体.md#a4bc063a4f3e275fb22880fd93a052c2f)
- [coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [coap_oscore_exchange::addr_len](../network_application_model_reference/P011_coap_oscore_exchange_结构体.md#a17cb77ffec08aeb0c808986a5d213ef2)
- [coap_oscore_exchange::tkl](../network_application_model_reference/P011_coap_oscore_exchange_结构体.md#a4742ebc7d9858fa1b31f09eed3a266e1)
- [coap_oscore_exchange::ctx](../network_application_model_reference/P011_coap_oscore_exchange_结构体.md#a4bc063a4f3e275fb22880fd93a052c2f)
- [coap_oscore_exchange::timestamp](../network_application_model_reference/P011_coap_oscore_exchange_结构体.md#a8115ef4326b8739e6f73a8e5dd70e748)
- [coap_oscore_exchange::token](../network_application_model_reference/P011_coap_oscore_exchange_结构体.md#a8a2114940e704221746fda5e4888df51)
- [coap_oscore_exchange::addr](../network_application_model_reference/P011_coap_oscore_exchange_结构体.md#ab97aabcc192841eb9646e187ae3409c3)
- [coap_oscore_init_params::id_context](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a0ad550ea2dc25001f78054a843ae2118)
- [coap_oscore_init_params::recipient_id_len](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a1108ec5f1f6d01995149bbef0430278c)
- [coap_oscore_init_params::master_salt](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a149618d292ea959fed2eb1aa4b61e03f)
- [coap_oscore_init_params::id_context_len](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a1e9ed9e0b5d27133519cc639629f5d66)
- [coap_oscore_init_params::sender_id_len](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a1eb4865020de525243b7a6e8cae2cf9f)
- [coap_oscore_init_params::hkdf](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a2c1c9a3175976ee35194ec54404eae4a)
- [coap_oscore_init_params::fresh_master_secret_salt](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a3cab68148e70cf453545058fdb0e94e3)
- [coap_oscore_init_params::recipient_id](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a5180b28768cc1396c27bb8f712919a7d)
- [coap_oscore_init_params::master_salt_len](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a5b6b967e34473ddc2a3d9f9f19656340)
- [coap_oscore_init_params::master_secret](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a6b4842301e3de5b5b6a27b3f5b7f2b16)
- [coap_oscore_init_params::master_secret_len](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a836d7cd5a6181fff740aa4958b3217ca)
- [coap_oscore_init_params::aead_alg](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a923f137c01c062e6fa596589d14b1321)
- [coap_oscore_init_params::sender_id](../network_application_model_reference/P012_coap_oscore_init_params_结构体.md#a9c5b4efd2f490c65c79b72317e7d703f)

---

[上一章](P107_coap_link_format.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P109_collector.h_源码浏览.md)
