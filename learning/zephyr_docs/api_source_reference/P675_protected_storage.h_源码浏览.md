---
id: learning.zephyr-docs.api-source-reference.page-675
title: protected_storage.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第675章\_protected\_storage.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../storage/P025_PSA受保护存储接口.md)。

## 675.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00046"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00079"></a>
<a id="foldopen00081"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00108"></a>
<a id="foldopen00110"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00136"></a>
<a id="foldopen00138"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00170"></a>
<a id="foldopen00172"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00208"></a>
<a id="foldopen00210"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00227"></a>
<a id="foldopen00229"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="aits_8h_html"></a>
<a id="aits_8h_html_a066a5ad089ca154c484b75ad2ff7fd3d"></a>
<a id="aits_8h_html_a2bf3b72ece99582585a223e1f41bf5a9"></a>
<a id="aits_8h_html_a6708e5131b0a090d99041bff56dfc84f"></a>
<a id="aits_8h_html_a6d0c166caa4b40ce95f422d9e4ad5ab5"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aprotected__storage_8h_html_a147a92d8387de36c32a8ede10d6d9a02"></a>
<a id="aprotected__storage_8h_html_a1630b75fce6941c4d619256822d5de9a"></a>
<a id="aprotected__storage_8h_html_a2ad1b8347d8cf174c028f0c485a66db6"></a>
<a id="aprotected__storage_8h_html_a7e1725cb412be305bd21e3e1af8c2312"></a>
<a id="aprotected__storage_8h_html_aa2c4d67afd77676a95becad71e902508"></a>
<a id="aprotected__storage_8h_html_ac27f8fc33b69e0a9ed09b73195b42eab"></a>
<a id="aprotected__storage_8h_html_af716b24d0761837d1c7b70042bd4966f"></a>
<a id="aps_8h_html"></a>
<a id="aps_8h_html_a0387828802c41350b9572a1555ecdeac"></a>
<a id="aps_8h_html_ab0be3c9374c1db65b45c43fdc6c05825"></a>
<a id="aps_8h_html_ab1612b91d341295578e16eb64d7035c4"></a>
<a id="aps_8h_html_ae044a9d36445840539578b9ea3a1e4d0"></a>
<a id="aps_8h_html_aef4fa69c85d80640a909868ad1749e8c"></a>
<a id="aps_8h_html_af6c6741b58d91798e2a9c2b3644f0bf1"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astorage__common_8h_html"></a>
<a id="astorage__common_8h_html_a1f53bd4fd1ba72bd88e9d7d9eb7da211"></a>
<a id="astorage__common_8h_html_ad9f16fc478036752ffb2ce9e50b2a710"></a>
<a id="astorage__common_8h_html_af5302147015dd30a2342728c98945087"></a>
<a id="astructpsa__storage__info__t_html"></a>
<a id="asubsys_2secure__storage_2include_2psa_2error_8h_html_a05676e70ba5c6a7565aff3c36677c1f9"></a>
<a id="asubsys_2secure__storage_2include_2psa_2error_8h_html_a1dcc6d130633ed5db8942257581b55dd"></a>

```c
/* Copyright (c) 2024 Nordic Semiconductor
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef PSA_PROTECTED_STORAGE_H
#define PSA_PROTECTED_STORAGE_H


#ifdef CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_ITS
#include "../internal/zephyr/secure_storage/its.h"
#define ITS_CALLER_ID SECURE_STORAGE_ITS_CALLER_PSA_PS
#else
#include "../internal/zephyr/secure_storage/ps.h"
#endif

#include <psa/storage_common.h>

#define PSA_PS_API_VERSION_MAJOR 1
#define PSA_PS_API_VERSION_MINOR 0

static ALWAYS_INLINE
psa_status_t psa_ps_set(psa_storage_uid_t uid, size_t data_length,
                        const void *p_data, psa_storage_create_flags_t create_flags)
{
#ifdef CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_ITS
        return secure_storage_its_set(ITS_CALLER_ID, uid, data_length, p_data, create_flags);
#else
        return secure_storage_ps_set(uid, data_length, p_data, create_flags);
#endif
}

static ALWAYS_INLINE
psa_status_t psa_ps_get(psa_storage_uid_t uid, size_t data_offset,
                        size_t data_size, void *p_data, size_t *p_data_length)
{
#ifdef CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_ITS
        return secure_storage_its_get(ITS_CALLER_ID, uid, data_offset,
                                      data_size, p_data, p_data_length);
#else
        return secure_storage_ps_get(uid, data_offset, data_size, p_data, p_data_length);
#endif
}

static ALWAYS_INLINE
psa_status_t psa_ps_get_info(psa_storage_uid_t uid, struct psa_storage_info_t *p_info)
{
#ifdef CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_ITS
        return secure_storage_its_get_info(ITS_CALLER_ID, uid, p_info);
#else
        return secure_storage_ps_get_info(uid, p_info);
#endif
}

static ALWAYS_INLINE
psa_status_t psa_ps_remove(psa_storage_uid_t uid)
{
#ifdef CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_ITS
        return secure_storage_its_remove(ITS_CALLER_ID, uid);
#else
        return secure_storage_ps_remove(uid);
#endif
}

static ALWAYS_INLINE
psa_status_t psa_ps_create(psa_storage_uid_t uid, size_t capacity,
                           psa_storage_create_flags_t create_flags)
{
#ifdef CONFIG_SECURE_STORAGE_PS_SUPPORTS_SET_EXTENDED
        return secure_storage_ps_create(uid, capacity, create_flags);
#else
        return PSA_ERROR_NOT_SUPPORTED;
#endif
}

static ALWAYS_INLINE
psa_status_t psa_ps_set_extended(psa_storage_uid_t uid, size_t data_offset,
                                 size_t data_length, const void *p_data)
{
#ifdef CONFIG_SECURE_STORAGE_PS_SUPPORTS_SET_EXTENDED
        return secure_storage_ps_set_extended(uid, data_offset, data_length, p_data);
#else
        return PSA_ERROR_NOT_SUPPORTED;
#endif
}

static ALWAYS_INLINE
uint32_t psa_ps_get_support(void)
{
        uint32_t flags = 0;

#ifdef CONFIG_SECURE_STORAGE_PS_SUPPORTS_SET_EXTENDED
        flags |= PSA_STORAGE_SUPPORT_SET_EXTENDED;
#endif
        return flags;
}

#undef ITS_CALLER_ID

#endif
```

## 675.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 675.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../storage/P025_PSA受保护存储接口.md)
- [../internal/zephyr/secure_storage/its.h](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html)
- [../internal/zephyr/secure_storage/ps.h](https://docs.zephyrproject.org/latest/doxygen/html/ps_8h.html)
- [psa/storage_common.h](../storage/P026_PSA存储公共定义.md)
- [psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)
- [psa_ps_set](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#ac27f8fc33b69e0a9ed09b73195b42eab)
- [psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)
- [psa_storage_create_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a1f53bd4fd1ba72bd88e9d7d9eb7da211)
- [secure_storage_its_set](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html#a6d0c166caa4b40ce95f422d9e4ad5ab5)
- [secure_storage_ps_set](https://docs.zephyrproject.org/latest/doxygen/html/ps_8h.html#ab0be3c9374c1db65b45c43fdc6c05825)
- [psa_ps_get](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#a2ad1b8347d8cf174c028f0c485a66db6)
- [secure_storage_its_get](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html#a2bf3b72ece99582585a223e1f41bf5a9)
- [secure_storage_ps_get](https://docs.zephyrproject.org/latest/doxygen/html/ps_8h.html#a0387828802c41350b9572a1555ecdeac)
- [psa_ps_get_info](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#af716b24d0761837d1c7b70042bd4966f)
- [psa_storage_info_t](../storage/P027_PSA存储条目元数据.md)
- [secure_storage_its_get_info](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html#a6708e5131b0a090d99041bff56dfc84f)
- [secure_storage_ps_get_info](https://docs.zephyrproject.org/latest/doxygen/html/ps_8h.html#af6c6741b58d91798e2a9c2b3644f0bf1)
- [psa_ps_remove](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#a147a92d8387de36c32a8ede10d6d9a02)
- [secure_storage_its_remove](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html#a066a5ad089ca154c484b75ad2ff7fd3d)
- [secure_storage_ps_remove](https://docs.zephyrproject.org/latest/doxygen/html/ps_8h.html#aef4fa69c85d80640a909868ad1749e8c)
- [psa_ps_create](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#aa2c4d67afd77676a95becad71e902508)
- [secure_storage_ps_create](https://docs.zephyrproject.org/latest/doxygen/html/ps_8h.html#ae044a9d36445840539578b9ea3a1e4d0)
- [PSA_ERROR_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a1dcc6d130633ed5db8942257581b55dd)
- [psa_ps_set_extended](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#a1630b75fce6941c4d619256822d5de9a)
- [secure_storage_ps_set_extended](https://docs.zephyrproject.org/latest/doxygen/html/ps_8h.html#ab1612b91d341295578e16eb64d7035c4)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [psa_ps_get_support](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#a7e1725cb412be305bd21e3e1af8c2312)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [PSA_STORAGE_SUPPORT_SET_EXTENDED](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#ad9f16fc478036752ffb2ce9e50b2a710)
- [its.h](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html)
- [ps.h](https://docs.zephyrproject.org/latest/doxygen/html/ps_8h.html)
- [storage_common.h](../storage/P026_PSA存储公共定义.md)

---

[上一章](P674_promiscuous.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P676_proxy.h_源码浏览.md)
