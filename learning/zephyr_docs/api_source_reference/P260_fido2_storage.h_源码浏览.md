---
id: learning.zephyr-docs.api-source-reference.page-260
title: fido2_storage.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fido2__storage_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第260章\_fido2\_storage.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fido2__storage_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fido2__storage_8h.html)。

## 260.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00089"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="afido2__types_8h_html"></a>
<a id="agroup__fido2_html_ga27aa8972d17b4ee6454204d0ab527ed0"></a>
<a id="agroup__fido2_html_gaa42cec8a02f80b77e8ddf3250d4b289b"></a>
<a id="agroup__fido2_html_gad0f22c2a4c49fdd7b47ed0913115c5b2"></a>
<a id="agroup__fido2_html_gaead02ba380ab3899742dfbf41edc4a98"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructfido2__credential_html"></a>
<a id="astructfido2__storage__api_html"></a>
<a id="astructfido2__storage__api_html_a11e569e7e42eb592e63de614bf3caea4"></a>
<a id="astructfido2__storage__api_html_a1c48cffc28698583435cb5fc5944b0a2"></a>
<a id="astructfido2__storage__api_html_a267cf93095b7d6c99f616cecbea71640"></a>
<a id="astructfido2__storage__api_html_a2aca20305a1b0919124231d5f62de79a"></a>
<a id="astructfido2__storage__api_html_a336bade2445fabab3f1583d2cced0932"></a>
<a id="astructfido2__storage__api_html_a493ad305f851d7e71f53d27f596b5cec"></a>
<a id="astructfido2__storage__api_html_a516702caaa10b783fbdbe6f6bf42ed96"></a>
<a id="astructfido2__storage__api_html_a51e0d7161f98222bb587ad69f399256e"></a>
<a id="astructfido2__storage__api_html_a5a0ff58bbd5769839d45fe5dd8f32663"></a>
<a id="astructfido2__storage__api_html_a6e73c6a26dc5601d8936ce977e9061b1"></a>
<a id="astructfido2__storage__api_html_a71cda9437a7abfc29644188addad3bec"></a>
<a id="astructfido2__storage__api_html_a72eac7fc7756ca6dbc53fe67d2161a93"></a>
<a id="astructfido2__storage__api_html_a7fdaf0829c6cacaba0e0e2966999c1fd"></a>
<a id="astructfido2__storage__api_html_aab707de64b5401fd8884f28c1d52b3af"></a>
<a id="astructfido2__storage__api_html_ab12cffb1e35e20105a118c3de6fca768"></a>
<a id="astructfido2__storage__api_html_ad5d135ae94fd0d4feef3c815b0cbe213"></a>

```c
/*
 * Copyright (c) 2026 Siratul Islam <email@sirat.me>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_STORAGE_H_
#define ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_STORAGE_H_

#include <zephyr/authentication/fido2/fido2_types.h>
#include <stddef.h>


#ifdef __cplusplus
extern "C" {
#endif

typedef int (*fido2_storage_iterate_cb_t)(const struct fido2_credential *cred, void *user_data);

struct fido2_storage_api {
        int (*init)(void);
        int (*store)(const struct fido2_credential *cred);
        int (*load)(const uint8_t *cred_id, size_t cred_id_len, struct fido2_credential *cred);
        int (*remove)(const uint8_t *cred_id, size_t cred_id_len, struct fido2_credential *cred);
        int (*find_by_rp)(const uint8_t rp_id_hash[FIDO2_SHA256_SIZE],
                          struct fido2_credential *creds, size_t max_creds, size_t *count);
        int (*enumerate_rps)(size_t offset, struct fido2_credential *creds, size_t max_creds,
                             size_t *count);
        int (*iterate)(fido2_storage_iterate_cb_t cb, void *user_data);
        int (*sign_count_increment)(const uint8_t *cred_id, size_t cred_id_len,
                                    uint32_t *new_count);
        int (*update_user_info)(const uint8_t *cred_id, size_t cred_id_len, const char *user_name,
                                const char *user_display_name);
        int (*credential_count)(size_t *count);
        int (*wipe_all)(void);
        int (*pin_set)(const uint8_t pin_hash[FIDO2_PIN_HASH_SIZE]);
        int (*pin_get)(uint8_t pin_hash[FIDO2_PIN_HASH_SIZE]);
        int (*pin_retries_get)(uint8_t *retries);
        int (*pin_retries_decrement)(void);
        int (*pin_retries_reset)(void);
};

extern const struct fido2_storage_api fido2_storage_backend;


int fido2_storage_init(void);

int fido2_storage_store(const struct fido2_credential *cred);

int fido2_storage_load(const uint8_t *cred_id, size_t cred_id_len, struct fido2_credential *cred);

int fido2_storage_remove(const uint8_t *cred_id, size_t cred_id_len);

int fido2_storage_find_by_rp(const uint8_t rp_id_hash[FIDO2_SHA256_SIZE],
                             struct fido2_credential *creds, size_t max_creds, size_t *count);

int fido2_storage_enumerate_rps(size_t offset, struct fido2_credential *creds, size_t max_creds,
                                size_t *count);

int fido2_storage_sign_count_increment(const uint8_t *cred_id, size_t cred_id_len,
                                       uint32_t *new_count);

int fido2_storage_pin_retries_get(uint8_t *retries);

int fido2_storage_pin_retries_decrement(void);

int fido2_storage_pin_retries_reset(void);

int fido2_storage_pin_set(uint8_t pin_hash[FIDO2_PIN_HASH_SIZE]);

int fido2_storage_pin_get(uint8_t pin_hash[FIDO2_PIN_HASH_SIZE]);


#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_STORAGE_H_ */
```

## 260.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Siratul Islam <email@sirat.me>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 201 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_STORAGE_H_`。

## 260.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fido2__storage_8h.html)
- [zephyr/authentication/fido2/fido2_types.h](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html)
- [fido2_storage_iterate_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gad0f22c2a4c49fdd7b47ed0913115c5b2)
- [fido2_credential](../platform_security_model_reference/P007_fido2_credential_结构体.md)
- [fido2_storage_api](../platform_security_model_reference/P009_fido2_storage_api_结构体.md)
- [init](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a5a0ff58bbd5769839d45fe5dd8f32663)
- [store](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a6e73c6a26dc5601d8936ce977e9061b1)
- [load](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a51e0d7161f98222bb587ad69f399256e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [remove](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a516702caaa10b783fbdbe6f6bf42ed96)
- [find_by_rp](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a493ad305f851d7e71f53d27f596b5cec)
- [FIDO2_SHA256_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaead02ba380ab3899742dfbf41edc4a98)
- [enumerate_rps](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a11e569e7e42eb592e63de614bf3caea4)
- [iterate](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a336bade2445fabab3f1583d2cced0932)
- [sign_count_increment](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a7fdaf0829c6cacaba0e0e2966999c1fd)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [update_user_info](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a1c48cffc28698583435cb5fc5944b0a2)
- [credential_count](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#ab12cffb1e35e20105a118c3de6fca768)
- [wipe_all](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a2aca20305a1b0919124231d5f62de79a)
- [pin_set](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#ad5d135ae94fd0d4feef3c815b0cbe213)
- [FIDO2_PIN_HASH_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaa42cec8a02f80b77e8ddf3250d4b289b)
- [pin_get](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a267cf93095b7d6c99f616cecbea71640)
- [pin_retries_get](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a71cda9437a7abfc29644188addad3bec)
- [pin_retries_decrement](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#aab707de64b5401fd8884f28c1d52b3af)
- [pin_retries_reset](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a72eac7fc7756ca6dbc53fe67d2161a93)
- [fido2_storage_backend](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga27aa8972d17b4ee6454204d0ab527ed0)
- [fido2_types.h](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html)
- [fido2_storage_api::enumerate_rps](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a11e569e7e42eb592e63de614bf3caea4)
- [fido2_storage_api::update_user_info](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a1c48cffc28698583435cb5fc5944b0a2)
- [fido2_storage_api::pin_get](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a267cf93095b7d6c99f616cecbea71640)
- [fido2_storage_api::wipe_all](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a2aca20305a1b0919124231d5f62de79a)
- [fido2_storage_api::iterate](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a336bade2445fabab3f1583d2cced0932)
- [fido2_storage_api::find_by_rp](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a493ad305f851d7e71f53d27f596b5cec)
- [fido2_storage_api::remove](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a516702caaa10b783fbdbe6f6bf42ed96)
- [fido2_storage_api::load](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a51e0d7161f98222bb587ad69f399256e)
- [fido2_storage_api::init](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a5a0ff58bbd5769839d45fe5dd8f32663)
- [fido2_storage_api::store](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a6e73c6a26dc5601d8936ce977e9061b1)
- [fido2_storage_api::pin_retries_get](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a71cda9437a7abfc29644188addad3bec)
- [fido2_storage_api::pin_retries_reset](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a72eac7fc7756ca6dbc53fe67d2161a93)
- [fido2_storage_api::sign_count_increment](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#a7fdaf0829c6cacaba0e0e2966999c1fd)
- [fido2_storage_api::pin_retries_decrement](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#aab707de64b5401fd8884f28c1d52b3af)
- [fido2_storage_api::credential_count](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#ab12cffb1e35e20105a118c3de6fca768)
- [fido2_storage_api::pin_set](../platform_security_model_reference/P009_fido2_storage_api_结构体.md#ad5d135ae94fd0d4feef3c815b0cbe213)

---

[上一章](P259_fido2_attestation.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P261_fido2_transport.h_源码浏览.md)
