---
id: learning.zephyr-docs.api-source-supplement-reference.page-4
title: aead.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/aead_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_aead.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/aead_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/aead_8h.html)。

## 4.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="foldopen00019"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="aaead_8h_html_a2a8cf814d206a63fd4c850da478b0077"></a>
<a id="aaead_8h_html_a2d29f8a15b7314e1b2211bbb93d5a1b2"></a>
<a id="aaead_8h_html_a59a656fec3b4347c2bd6ac4843877856"></a>
<a id="aaead_8h_html_abf498c228e9c8d6f32432d859b5d225e"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructsecure__storage__its__uid__t_html"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_html"></a>
<a id="asubsys_2secure__storage_2include_2psa_2error_8h_html_a05676e70ba5c6a7565aff3c36677c1f9"></a>

```c
/* Copyright (c) 2024 Nordic Semiconductor
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef SECURE_STORAGE_ITS_TRANSFORM_AEAD_H
#define SECURE_STORAGE_ITS_TRANSFORM_AEAD_H

#include <zephyr/secure_storage/its/common.h>
#include <psa/crypto_types.h>

#define SECURE_STORAGE_ITS_TRANSFORM_AEAD_TAG_SIZE                     \
                (CONFIG_SECURE_STORAGE_ITS_TRANSFORM_OUTPUT_OVERHEAD   \
                 - CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_SIZE)

psa_status_t secure_storage_its_transform_aead_crypt(
                psa_key_usage_t operation, secure_storage_its_uid_t uid,
                const uint8_t nonce[static CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_SIZE],
                size_t add_data_len, const uint8_t *add_data, size_t input_len,
                const uint8_t *input, size_t output_size, uint8_t *output, size_t *output_len);

#if defined(CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_IS_CONFIGURABLE) || defined(__DOXYGEN__)

void secure_storage_its_transform_aead_get_scheme(psa_key_type_t *key_type, psa_algorithm_t *alg);

#endif /* CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_IS_CONFIGURABLE */

#if !defined(CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_CRYPT_CUSTOM) || defined(__DOXYGEN__)

psa_status_t secure_storage_its_transform_aead_get_key(
                secure_storage_its_uid_t uid,
                uint8_t key[static CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_SIZE]);

#endif /* SECURE_STORAGE_ITS_TRANSFORM_AEAD_CRYPT_CUSTOM */

psa_status_t secure_storage_its_transform_aead_get_nonce(
                uint8_t nonce[static CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_NONCE_SIZE]);

#endif
```

## 4.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 57 行

条件编译配置（Configuration）标记：`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_SCHEME_IS_CONFIGURABLE`。

### 注释 3：原第 72 行

条件编译标记：`SECURE_STORAGE_ITS_TRANSFORM_AEAD_CRYPT_CUSTOM`。

## 4.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/aead_8h.html)
- [zephyr/secure_storage/its/common.h](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html)
- [psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)
- [secure_storage_its_transform_aead_crypt](https://docs.zephyrproject.org/latest/doxygen/html/aead_8h.html#a59a656fec3b4347c2bd6ac4843877856)
- [secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [secure_storage_its_transform_aead_get_scheme](https://docs.zephyrproject.org/latest/doxygen/html/aead_8h.html#abf498c228e9c8d6f32432d859b5d225e)
- [secure_storage_its_transform_aead_get_key](https://docs.zephyrproject.org/latest/doxygen/html/aead_8h.html#a2a8cf814d206a63fd4c850da478b0077)
- [secure_storage_its_transform_aead_get_nonce](https://docs.zephyrproject.org/latest/doxygen/html/aead_8h.html#a2d29f8a15b7314e1b2211bbb93d5a1b2)
- [common.h](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html)

---

[上一章](P003_addresses.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P005_aio.h_源码浏览.md)
