---
id: learning.zephyr-docs.api-source-reference.page-407
title: internal_trusted_storage.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/internal__trusted__storage_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第407章\_internal\_trusted\_storage.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/internal__trusted__storage_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../storage/P024_PSA内部可信存储接口.md)。

## 407.1\_原始可见代码（Source Code）

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
<a id="l00048"></a>
<a id="foldopen00050"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00077"></a>
<a id="foldopen00079"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00102"></a>
<a id="foldopen00104"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00123"></a>
<a id="foldopen00125"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="ainternal__trusted__storage_8h_html_a01e5344273e6d776d1f456c4d54a2ed8"></a>
<a id="ainternal__trusted__storage_8h_html_a387d450b2a21673fba6c56e66c74b5f7"></a>
<a id="ainternal__trusted__storage_8h_html_abd70b9f9bc063e3651f315408f4ae04c"></a>
<a id="ainternal__trusted__storage_8h_html_ae4efe6e7f9088fdf8ef4e126045a432b"></a>
<a id="aits_8h_html"></a>
<a id="aits_8h_html_a066a5ad089ca154c484b75ad2ff7fd3d"></a>
<a id="aits_8h_html_a2bf3b72ece99582585a223e1f41bf5a9"></a>
<a id="aits_8h_html_a6708e5131b0a090d99041bff56dfc84f"></a>
<a id="aits_8h_html_a6d0c166caa4b40ce95f422d9e4ad5ab5"></a>
<a id="astorage__common_8h_html"></a>
<a id="astorage__common_8h_html_a1f53bd4fd1ba72bd88e9d7d9eb7da211"></a>
<a id="astorage__common_8h_html_af5302147015dd30a2342728c98945087"></a>
<a id="astructpsa__storage__info__t_html"></a>
<a id="asubsys_2secure__storage_2include_2psa_2error_8h_html_a05676e70ba5c6a7565aff3c36677c1f9"></a>

```c
/* Copyright (c) 2024 Nordic Semiconductor
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef PSA_INTERNAL_TRUSTED_STORAGE_H
#define PSA_INTERNAL_TRUSTED_STORAGE_H


#include "../internal/zephyr/secure_storage/its.h"
#ifdef BUILDING_PSA_CRYPTO
#define ITS_CALLER_ID SECURE_STORAGE_ITS_CALLER_PSA_CRYPTO
#else
#define ITS_CALLER_ID SECURE_STORAGE_ITS_CALLER_PSA_ITS
#endif

#include <psa/storage_common.h>

#define PSA_ITS_API_VERSION_MAJOR 1
#define PSA_ITS_API_VERSION_MINOR 0

static ALWAYS_INLINE
psa_status_t psa_its_set(psa_storage_uid_t uid, size_t data_length,
                         const void *p_data, psa_storage_create_flags_t create_flags)
{
        return secure_storage_its_set(ITS_CALLER_ID, uid, data_length, p_data, create_flags);
}

static ALWAYS_INLINE
psa_status_t psa_its_get(psa_storage_uid_t uid, size_t data_offset,
                         size_t data_size, void *p_data, size_t *p_data_length)
{
        return secure_storage_its_get(ITS_CALLER_ID, uid, data_offset,
                                      data_size, p_data, p_data_length);
}

static ALWAYS_INLINE
psa_status_t psa_its_get_info(psa_storage_uid_t uid, struct psa_storage_info_t *p_info)
{
        return secure_storage_its_get_info(ITS_CALLER_ID, uid, p_info);
}

static ALWAYS_INLINE
psa_status_t psa_its_remove(psa_storage_uid_t uid)
{
        return secure_storage_its_remove(ITS_CALLER_ID, uid);
}

#undef ITS_UID
#undef ITS_CALLER_ID

#endif
```

## 407.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 407.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../storage/P024_PSA内部可信存储接口.md)
- [../internal/zephyr/secure_storage/its.h](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html)
- [psa/storage_common.h](../storage/P026_PSA存储公共定义.md)
- [psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)
- [psa_its_set](https://docs.zephyrproject.org/latest/doxygen/html/internal__trusted__storage_8h.html#a01e5344273e6d776d1f456c4d54a2ed8)
- [psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)
- [psa_storage_create_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a1f53bd4fd1ba72bd88e9d7d9eb7da211)
- [secure_storage_its_set](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html#a6d0c166caa4b40ce95f422d9e4ad5ab5)
- [psa_its_get](https://docs.zephyrproject.org/latest/doxygen/html/internal__trusted__storage_8h.html#a387d450b2a21673fba6c56e66c74b5f7)
- [secure_storage_its_get](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html#a2bf3b72ece99582585a223e1f41bf5a9)
- [psa_its_get_info](https://docs.zephyrproject.org/latest/doxygen/html/internal__trusted__storage_8h.html#ae4efe6e7f9088fdf8ef4e126045a432b)
- [psa_storage_info_t](../storage/P027_PSA存储条目元数据.md)
- [secure_storage_its_get_info](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html#a6708e5131b0a090d99041bff56dfc84f)
- [psa_its_remove](https://docs.zephyrproject.org/latest/doxygen/html/internal__trusted__storage_8h.html#abd70b9f9bc063e3651f315408f4ae04c)
- [secure_storage_its_remove](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html#a066a5ad089ca154c484b75ad2ff7fd3d)
- [its.h](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html)
- [storage_common.h](../storage/P026_PSA存储公共定义.md)

---

[上一章](P406_intel_vtd.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P408_ioctl.h_源码浏览.md)
