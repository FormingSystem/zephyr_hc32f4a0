---
id: learning.zephyr-docs.api-source-reference.page-843
title: common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第843章\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html)。

## 843.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="foldopen00017"></a>
<a id="l00017"></a>
<a id="l00019"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="astorage__common_8h_html"></a>
<a id="astorage__common_8h_html_af5302147015dd30a2342728c98945087"></a>
<a id="astructsecure__storage__its__uid__t_html"></a>
<a id="astructsecure__storage__its__uid__t_html_a444f3c47521ef82e086c0c43941e23ee"></a>
<a id="astructsecure__storage__its__uid__t_html_a8f581033ce88a130f3a6b04c9821294e"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h_html"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h_html_ac3c7c0ba918fe964b4c39ae0d8047bdd"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_html_a2369ff303bf323cb4e57f1b970093d2b"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_html_a2369ff303bf323cb4e57f1b970093d2ba5f757e2cf7ded49541f9af38ca6ef00e"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_html_a2369ff303bf323cb4e57f1b970093d2ba8ee890874c86e0717973bc03208499bd"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_html_a2369ff303bf323cb4e57f1b970093d2bab584518773eefcb3731ec57ae6f4f21f"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_html_a2369ff303bf323cb4e57f1b970093d2badb6049a90872ae6773af2817093cce5d"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_html_a2ee97ffbf1145cf2d52ec6f27113dd99"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_html_a964e029c0c87aea5239bfb97cc3f66f0"></a>
<a id="atoolchain_8h_html"></a>

```c
/* Copyright (c) 2024 Nordic Semiconductor
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef SECURE_STORAGE_ITS_COMMON_H
#define SECURE_STORAGE_ITS_COMMON_H

#include "../common.h"
#include <zephyr/toolchain.h>
#include <psa/storage_common.h>

typedef enum {
        SECURE_STORAGE_ITS_CALLER_PSA_ITS,
        SECURE_STORAGE_ITS_CALLER_PSA_PS,
        SECURE_STORAGE_ITS_CALLER_PSA_CRYPTO,
        SECURE_STORAGE_ITS_CALLER_COUNT
} secure_storage_its_caller_id_t;

#ifdef CONFIG_SECURE_STORAGE_64_BIT_UID

typedef struct {
        psa_storage_uid_t uid;
        secure_storage_its_caller_id_t caller_id;
} __packed secure_storage_its_uid_t;

#else

#define SECURE_STORAGE_ITS_UID_BIT_SIZE 30
#define SECURE_STORAGE_ITS_CALLER_ID_BIT_SIZE 2

typedef struct {
        psa_storage_uid_t uid : SECURE_STORAGE_ITS_UID_BIT_SIZE;
        secure_storage_its_caller_id_t caller_id : SECURE_STORAGE_ITS_CALLER_ID_BIT_SIZE;
} secure_storage_its_uid_t;

#endif /* CONFIG_SECURE_STORAGE_64_BIT_UID */

#ifdef CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE

enum { SECURE_STORAGE_ITS_TRANSFORM_MAX_STORED_DATA_SIZE
        = CONFIG_SECURE_STORAGE_ITS_MAX_DATA_SIZE
          + sizeof(secure_storage_packed_create_flags_t)
          + CONFIG_SECURE_STORAGE_ITS_TRANSFORM_OUTPUT_OVERHEAD };

#define SECURE_STORAGE_ITS_TRANSFORM_DATA_SIZE(transformed_data_size) \
        (transformed_data_size - (SECURE_STORAGE_ITS_TRANSFORM_MAX_STORED_DATA_SIZE \
                                  - CONFIG_SECURE_STORAGE_ITS_MAX_DATA_SIZE))

#endif /* CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE */

#endif
```

## 843.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 52 行

条件编译配置（Configuration）标记：`CONFIG_SECURE_STORAGE_64_BIT_UID`。

### 注释 3：原第 67 行

条件编译配置（Configuration）标记：`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_MODULE`。

## 843.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html)
- [../common.h](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [psa/storage_common.h](../storage/P026_PSA存储公共定义.md)
- [SECURE_STORAGE_ITS_CALLER_PSA_ITS](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html#a2369ff303bf323cb4e57f1b970093d2ba8ee890874c86e0717973bc03208499bd)
- [SECURE_STORAGE_ITS_CALLER_PSA_PS](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html#a2369ff303bf323cb4e57f1b970093d2badb6049a90872ae6773af2817093cce5d)
- [SECURE_STORAGE_ITS_CALLER_PSA_CRYPTO](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html#a2369ff303bf323cb4e57f1b970093d2ba5f757e2cf7ded49541f9af38ca6ef00e)
- [SECURE_STORAGE_ITS_CALLER_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html#a2369ff303bf323cb4e57f1b970093d2bab584518773eefcb3731ec57ae6f4f21f)
- [secure_storage_its_caller_id_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html#a2369ff303bf323cb4e57f1b970093d2b)
- [psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)
- [secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)
- [uid](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md#a444f3c47521ef82e086c0c43941e23ee)
- [SECURE_STORAGE_ITS_UID_BIT_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html#a2ee97ffbf1145cf2d52ec6f27113dd99)
- [caller_id](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md#a8f581033ce88a130f3a6b04c9821294e)
- [SECURE_STORAGE_ITS_CALLER_ID_BIT_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html#a964e029c0c87aea5239bfb97cc3f66f0)
- [secure_storage_packed_create_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.html#ac3c7c0ba918fe964b4c39ae0d8047bdd)
- [storage_common.h](../storage/P026_PSA存储公共定义.md)
- [secure_storage_its_uid_t::uid](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md#a444f3c47521ef82e086c0c43941e23ee)
- [secure_storage_its_uid_t::caller_id](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md#a8f581033ce88a130f3a6b04c9821294e)
- [common.h](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.html)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P842_stts22h.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P844_settings.h_源码浏览.md)
