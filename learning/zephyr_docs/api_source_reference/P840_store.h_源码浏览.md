---
id: learning.zephyr-docs.api-source-reference.page-840
title: store.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/store_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第840章\_store.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/store_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/store_8h.html)。

## 840.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="astore_8h_html_a22d16815fb645ff5cc014f2fe4e9e987"></a>
<a id="astore_8h_html_a58eb126f3d92112b3ed19d1920d43fa0"></a>
<a id="astore_8h_html_aed06855314e4dafb4e935d31b6fb21bb"></a>
<a id="astructsecure__storage__its__uid__t_html"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_html"></a>
<a id="asubsys_2secure__storage_2include_2psa_2error_8h_html_a05676e70ba5c6a7565aff3c36677c1f9"></a>

```c
/* Copyright (c) 2024 Nordic Semiconductor
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef SECURE_STORAGE_ITS_STORE_H
#define SECURE_STORAGE_ITS_STORE_H

#include <zephyr/secure_storage/its/common.h>

psa_status_t secure_storage_its_store_set(secure_storage_its_uid_t uid,
                                          size_t data_length, const void *data);

psa_status_t secure_storage_its_store_get(secure_storage_its_uid_t uid, size_t data_size,
                                          void *data, size_t *data_length);

psa_status_t secure_storage_its_store_remove(secure_storage_its_uid_t uid);

#endif
```

## 840.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 840.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/store_8h.html)
- [zephyr/secure_storage/its/common.h](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html)
- [psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)
- [secure_storage_its_store_set](https://docs.zephyrproject.org/latest/doxygen/html/store_8h.html#aed06855314e4dafb4e935d31b6fb21bb)
- [secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)
- [secure_storage_its_store_get](https://docs.zephyrproject.org/latest/doxygen/html/store_8h.html#a22d16815fb645ff5cc014f2fe4e9e987)
- [secure_storage_its_store_remove](https://docs.zephyrproject.org/latest/doxygen/html/store_8h.html#a58eb126f3d92112b3ed19d1920d43fa0)
- [common.h](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html)

---

[上一章](P839_storage_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P841_stropts.h_源码浏览.md)
