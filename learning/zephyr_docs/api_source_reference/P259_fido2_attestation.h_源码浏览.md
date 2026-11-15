---
id: learning.zephyr-docs.api-source-reference.page-259
title: fido2_attestation.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fido2__attestation_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第259章\_fido2\_attestation.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fido2__attestation_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fido2__attestation_8h.html)。

## 259.1\_原始可见代码（Source Code）

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
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="agroup__fido2_html_gaf81f2aff090633c893740db7b60ed614"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructfido2__attestation__result_html"></a>
<a id="astructfido2__attestation__result_html_a2283601407953326d34afbc7795202c4"></a>
<a id="astructfido2__attestation__result_html_a4a387ed4358d5aa66c91adc3a15dd902"></a>
<a id="astructfido2__attestation__result_html_a54faed1a597ea39e5938fa521388fd6f"></a>
<a id="astructfido2__attestation__result_html_a64a5324c4cead032417560df0692004b"></a>
<a id="astructfido2__attestation__result_html_a7be57d42d8c552659f59f8d49349f58f"></a>
<a id="astructfido2__attestation__result_html_a9c90db221f5dbc7371f526b8381fa091"></a>

```c
/*
 * Copyright (c) 2026 Siratul Islam <email@sirat.me>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_ATTESTATION_H_
#define ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_ATTESTATION_H_

#include <stddef.h>
#include <stdint.h>


#ifdef __cplusplus
extern "C" {
#endif

#define FIDO2_ATTESTATION_FMT_PACKED  "packed"
#define FIDO2_ATTESTATION_FMT_NONE    "none"
#define FIDO2_ATTESTATION_FMT_MAX_LEN 32

struct fido2_attestation_result {
        const char *fmt;
        int32_t alg;
        const uint8_t *sig;
        size_t sig_len;
        const uint8_t *x5c;
        size_t x5c_len;
};

int fido2_attestation_sign(const uint8_t *auth_data, size_t auth_data_len,
                           const uint8_t *client_data_hash, uint32_t credential_key_id,
                           struct fido2_attestation_result *result);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_ATTESTATION_H_ */
```

## 259.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Siratul Islam <email@sirat.me>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 74 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_ATTESTATION_H_`。

## 259.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fido2__attestation_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [fido2_attestation_result](../platform_security_model_reference/P006_fido2_attestation_result_结构体.md)
- [fmt](../platform_security_model_reference/P006_fido2_attestation_result_结构体.md#a54faed1a597ea39e5938fa521388fd6f)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [alg](../platform_security_model_reference/P006_fido2_attestation_result_结构体.md#a2283601407953326d34afbc7795202c4)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sig](../platform_security_model_reference/P006_fido2_attestation_result_结构体.md#a64a5324c4cead032417560df0692004b)
- [sig_len](../platform_security_model_reference/P006_fido2_attestation_result_结构体.md#a4a387ed4358d5aa66c91adc3a15dd902)
- [x5c](../platform_security_model_reference/P006_fido2_attestation_result_结构体.md#a9c90db221f5dbc7371f526b8381fa091)
- [x5c_len](../platform_security_model_reference/P006_fido2_attestation_result_结构体.md#a7be57d42d8c552659f59f8d49349f58f)
- [fido2_attestation_sign](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaf81f2aff090633c893740db7b60ed614)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [fido2_attestation_result::alg](../platform_security_model_reference/P006_fido2_attestation_result_结构体.md#a2283601407953326d34afbc7795202c4)
- [fido2_attestation_result::sig_len](../platform_security_model_reference/P006_fido2_attestation_result_结构体.md#a4a387ed4358d5aa66c91adc3a15dd902)
- [fido2_attestation_result::fmt](../platform_security_model_reference/P006_fido2_attestation_result_结构体.md#a54faed1a597ea39e5938fa521388fd6f)
- [fido2_attestation_result::sig](../platform_security_model_reference/P006_fido2_attestation_result_结构体.md#a64a5324c4cead032417560df0692004b)
- [fido2_attestation_result::x5c_len](../platform_security_model_reference/P006_fido2_attestation_result_结构体.md#a7be57d42d8c552659f59f8d49349f58f)
- [fido2_attestation_result::x5c](../platform_security_model_reference/P006_fido2_attestation_result_结构体.md#a9c90db221f5dbc7371f526b8381fa091)

---

[上一章](P258_fido2.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P260_fido2_storage.h_源码浏览.md)
