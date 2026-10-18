---
id: learning.zephyr-docs.api-source-reference.page-875
title: transform.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/transform_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第875章\_transform.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/transform_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/transform_8h.html)。

## 875.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astorage__common_8h_html_a1f53bd4fd1ba72bd88e9d7d9eb7da211"></a>
<a id="astructsecure__storage__its__uid__t_html"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h_html_ac3c7c0ba918fe964b4c39ae0d8047bdd"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_html"></a>
<a id="asubsys_2secure__storage_2include_2psa_2error_8h_html_a05676e70ba5c6a7565aff3c36677c1f9"></a>
<a id="atransform_8h_html_a25353d53a0bce5dea8fc4d42bba8988e"></a>
<a id="atransform_8h_html_ac976a23f8049c4e2e5b95bf867b9ea24"></a>

```c
/* Copyright (c) 2024 Nordic Semiconductor
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef SECURE_STORAGE_ITS_TRANSFORM_H
#define SECURE_STORAGE_ITS_TRANSFORM_H

#include <zephyr/secure_storage/its/common.h>

psa_status_t secure_storage_its_transform_to_store(
                secure_storage_its_uid_t uid, size_t data_len, const void *data,
                secure_storage_packed_create_flags_t create_flags,
                uint8_t stored_data[static SECURE_STORAGE_ITS_TRANSFORM_MAX_STORED_DATA_SIZE],
                size_t *stored_data_len);

psa_status_t secure_storage_its_transform_from_store(
                secure_storage_its_uid_t uid, size_t stored_data_len,
                const uint8_t stored_data[static SECURE_STORAGE_ITS_TRANSFORM_MAX_STORED_DATA_SIZE],
                size_t data_size, void *data, size_t *data_len,
                psa_storage_create_flags_t *create_flags);

#endif
```

## 875.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 875.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/transform_8h.html)
- [zephyr/secure_storage/its/common.h](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html)
- [psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)
- [secure_storage_its_transform_to_store](https://docs.zephyrproject.org/latest/doxygen/html/transform_8h.html#ac976a23f8049c4e2e5b95bf867b9ea24)
- [secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)
- [secure_storage_packed_create_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.html#ac3c7c0ba918fe964b4c39ae0d8047bdd)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [secure_storage_its_transform_from_store](https://docs.zephyrproject.org/latest/doxygen/html/transform_8h.html#a25353d53a0bce5dea8fc4d42bba8988e)
- [psa_storage_create_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a1f53bd4fd1ba72bd88e9d7d9eb7da211)
- [common.h](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html)

---

[上一章](P874_tmp451.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P876_transport.h_源码浏览.md)
