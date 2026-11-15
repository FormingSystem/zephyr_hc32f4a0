---
id: learning.zephyr-docs.api-source-reference.page-424
title: its.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/its_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第424章\_its.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/its_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html)。

## 424.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="aits_8h_html_a066a5ad089ca154c484b75ad2ff7fd3d"></a>
<a id="aits_8h_html_a2bf3b72ece99582585a223e1f41bf5a9"></a>
<a id="aits_8h_html_a6708e5131b0a090d99041bff56dfc84f"></a>
<a id="aits_8h_html_a6d0c166caa4b40ce95f422d9e4ad5ab5"></a>
<a id="astorage__common_8h_html_a1f53bd4fd1ba72bd88e9d7d9eb7da211"></a>
<a id="astorage__common_8h_html_af5302147015dd30a2342728c98945087"></a>
<a id="astructpsa__storage__info__t_html"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_html"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_html_a2369ff303bf323cb4e57f1b970093d2b"></a>
<a id="asubsys_2secure__storage_2include_2psa_2error_8h_html_a05676e70ba5c6a7565aff3c36677c1f9"></a>

```c
/* Copyright (c) 2024 Nordic Semiconductor
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef SECURE_STORAGE_ITS_H
#define SECURE_STORAGE_ITS_H

#include "its/common.h"

psa_status_t secure_storage_its_set(secure_storage_its_caller_id_t caller_id, psa_storage_uid_t uid,
                                    size_t data_length, const void *p_data,
                                    psa_storage_create_flags_t create_flags);

psa_status_t secure_storage_its_get(secure_storage_its_caller_id_t caller_id, psa_storage_uid_t uid,
                                    size_t data_offset, size_t data_size,
                                    void *p_data, size_t *p_data_length);

psa_status_t secure_storage_its_get_info(secure_storage_its_caller_id_t caller_id,
                                         psa_storage_uid_t uid, struct psa_storage_info_t *p_info);

psa_status_t secure_storage_its_remove(secure_storage_its_caller_id_t caller_id,
                                       psa_storage_uid_t uid);

#endif
```

## 424.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 424.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html)
- [its/common.h](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html)
- [psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)
- [secure_storage_its_set](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html#a6d0c166caa4b40ce95f422d9e4ad5ab5)
- [secure_storage_its_caller_id_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html#a2369ff303bf323cb4e57f1b970093d2b)
- [psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)
- [psa_storage_create_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a1f53bd4fd1ba72bd88e9d7d9eb7da211)
- [secure_storage_its_get](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html#a2bf3b72ece99582585a223e1f41bf5a9)
- [secure_storage_its_get_info](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html#a6708e5131b0a090d99041bff56dfc84f)
- [psa_storage_info_t](../storage/P027_PSA存储条目元数据.md)
- [secure_storage_its_remove](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html#a066a5ad089ca154c484b75ad2ff7fd3d)
- [common.h](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html)

---

[上一章](P423_ite-it8xxx2-gpio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P425_its_ids.h_源码浏览.md)
