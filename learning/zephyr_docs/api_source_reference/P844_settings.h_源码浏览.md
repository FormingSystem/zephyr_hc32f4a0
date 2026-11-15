---
id: learning.zephyr-docs.api-source-reference.page-844
title: settings.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2store_2settings_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第844章\_settings.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2store_2settings_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2store_2settings_8h.html)。

## 844.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="foldopen00018"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="astructsecure__storage__its__uid__t_html"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_html"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2store_2settings_8h_html_ab034dcdbc69cad67f1f6eddb561fb099"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2store_2settings_8h_html_aeb04a9d9f92c3dfae97bf2049729517b"></a>

```c
/* Copyright (c) 2024 Nordic Semiconductor
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef SECURE_STORAGE_ITS_STORE_SETTINGS_H
#define SECURE_STORAGE_ITS_STORE_SETTINGS_H

#include <zephyr/secure_storage/its/common.h>

#define SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_BUF_SIZE                    \
                (CONFIG_SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_MAX_LEN + 1)

void secure_storage_its_store_settings_get_name(
        secure_storage_its_uid_t uid,
        char name[static SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_BUF_SIZE]);

#endif
```

## 844.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 844.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2store_2settings_8h.html)
- [zephyr/secure_storage/its/common.h](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html)
- [secure_storage_its_store_settings_get_name](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2store_2settings_8h.html#ab034dcdbc69cad67f1f6eddb561fb099)
- [secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)
- [SECURE_STORAGE_ITS_STORE_SETTINGS_NAME_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2store_2settings_8h.html#aeb04a9d9f92c3dfae97bf2049729517b)
- [common.h](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html)

---

[上一章](P843_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P845_error.h_源码浏览.md)
