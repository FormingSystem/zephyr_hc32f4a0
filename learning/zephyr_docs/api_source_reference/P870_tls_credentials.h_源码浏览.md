---
id: learning.zephyr-docs.api-source-reference.page-870
title: tls_credentials.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tls__credentials_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第870章\_tls\_credentials.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/tls__credentials_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/tls__credentials_8h.html)。

## 870.1\_原始可见代码（Source Code）

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
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="a__timespec_8h_html_aa17c461cd5eca7fc12a66daa803c7fd7"></a>
<a id="agroup__tls__credentials_html_ga3a754894d0162634b59d60e319f37cd5"></a>
<a id="agroup__tls__credentials_html_ga640ff6dd3eb4d5017feaab6fab2bb2f7"></a>
<a id="agroup__tls__credentials_html_ga7508492d623044d33406de5abdf29216"></a>
<a id="agroup__tls__credentials_html_ga9d8b47a7a2675fb3b3c6ee346e925aca"></a>
<a id="agroup__tls__credentials_html_gaadfe9694309e473f7be74ed98dfb36d3"></a>
<a id="agroup__tls__credentials_html_gac3ac4ca887faf6c1f2ae60c6a08f8795"></a>
<a id="agroup__tls__credentials_html_gga3a754894d0162634b59d60e319f37cd5a1edcd43ba510558e4b1315e1bb86560d"></a>
<a id="agroup__tls__credentials_html_gga3a754894d0162634b59d60e319f37cd5a406e8bb1f992af5a72921f47b140840e"></a>
<a id="agroup__tls__credentials_html_gga3a754894d0162634b59d60e319f37cd5a7009a9f266011529e64ec4e4c6692315"></a>
<a id="agroup__tls__credentials_html_gga3a754894d0162634b59d60e319f37cd5accc6ad916ee6c6badafcc4c23e2a47df"></a>
<a id="agroup__tls__credentials_html_gga3a754894d0162634b59d60e319f37cd5acd8b96102765f7f2a83582eab80df3d8"></a>
<a id="agroup__tls__credentials_html_gga3a754894d0162634b59d60e319f37cd5adcf949c1422f4d3b38795ae40d2321d5"></a>
<a id="agroup__tls__credentials_html_gga3a754894d0162634b59d60e319f37cd5ae7f4b9f4ed9865678d7cbdb741ca19e1"></a>

```c
/*
 * Copyright (c) 2018 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_TLS_CREDENTIALS_H_
#define ZEPHYR_INCLUDE_NET_TLS_CREDENTIALS_H_

#include <stddef.h>


#ifdef __cplusplus
extern "C" {
#endif

#include <time.h>

enum tls_credential_type {
        TLS_CREDENTIAL_NONE,

        TLS_CREDENTIAL_CA_CERTIFICATE,

        TLS_CREDENTIAL_PUBLIC_CERTIFICATE,

        TLS_CREDENTIAL_PRIVATE_KEY,

        TLS_CREDENTIAL_PSK,

        TLS_CREDENTIAL_PSK_ID,

        TLS_CREDENTIAL_PRIVATE_KEY_PSA
};

typedef int sec_tag_t;

#define SEC_TAG_TLS_INVALID (-1)

int tls_credential_add(sec_tag_t tag, enum tls_credential_type type,
                       const void *cred, size_t credlen);

int tls_credential_get(sec_tag_t tag, enum tls_credential_type type,
                       void *cred, size_t *credlen);

int tls_credential_delete(sec_tag_t tag, enum tls_credential_type type);

int tls_credential_expiry(sec_tag_t tag, enum tls_credential_type type, time_t *expiry);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_TLS_CREDENTIALS_H_ */
```

## 870.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 170 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_TLS_CREDENTIALS_H_`。

## 870.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/tls__credentials_8h.html)
- [tls_credential_type](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga3a754894d0162634b59d60e319f37cd5)
- [TLS_CREDENTIAL_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5a7009a9f266011529e64ec4e4c6692315)
- [TLS_CREDENTIAL_CA_CERTIFICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5adcf949c1422f4d3b38795ae40d2321d5)
- [TLS_CREDENTIAL_PUBLIC_CERTIFICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5acd8b96102765f7f2a83582eab80df3d8)
- [TLS_CREDENTIAL_PRIVATE_KEY](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5a406e8bb1f992af5a72921f47b140840e)
- [TLS_CREDENTIAL_PSK](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5accc6ad916ee6c6badafcc4c23e2a47df)
- [TLS_CREDENTIAL_PSK_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5a1edcd43ba510558e4b1315e1bb86560d)
- [TLS_CREDENTIAL_PRIVATE_KEY_PSA](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gga3a754894d0162634b59d60e319f37cd5ae7f4b9f4ed9865678d7cbdb741ca19e1)
- [sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)
- [tls_credential_add](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga640ff6dd3eb4d5017feaab6fab2bb2f7)
- [tls_credential_get](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gac3ac4ca887faf6c1f2ae60c6a08f8795)
- [tls_credential_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga9d8b47a7a2675fb3b3c6ee346e925aca)
- [tls_credential_expiry](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#ga7508492d623044d33406de5abdf29216)
- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)

---

[上一章](P869_tlc5971.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P871_tmap.h_源码浏览.md)
