---
id: learning.zephyr-docs.api-source-reference.page-839
title: storage_common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第839章\_storage\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../storage/P026_PSA存储公共定义.md)。

## 839.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astorage__common_8h_html_a1f53bd4fd1ba72bd88e9d7d9eb7da211"></a>
<a id="astorage__common_8h_html_af5302147015dd30a2342728c98945087"></a>
<a id="astructpsa__storage__info__t_html"></a>
<a id="astructpsa__storage__info__t_html_a1b2d4b80f2989c0c182bf519442090ae"></a>
<a id="astructpsa__storage__info__t_html_a2a18bf8e7a44cc050e088fb34a453a1d"></a>
<a id="astructpsa__storage__info__t_html_a3dfb41a4b9bf931f3b3fe96f13c1d289"></a>
<a id="asubsys_2secure__storage_2include_2psa_2error_8h_html"></a>

```c
/* Copyright (c) 2024 Nordic Semiconductor
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef PSA_STORAGE_COMMON_H
#define PSA_STORAGE_COMMON_H
#include <psa/error.h>
#include <stddef.h>

#ifdef CONFIG_SECURE_STORAGE_64_BIT_UID
typedef uint64_t psa_storage_uid_t;
#else
typedef uint32_t psa_storage_uid_t;
#endif

typedef uint32_t psa_storage_create_flags_t;

#define PSA_STORAGE_FLAG_NONE                 0u
#define PSA_STORAGE_FLAG_WRITE_ONCE           (1u << 0)
#define PSA_STORAGE_FLAG_NO_CONFIDENTIALITY   (1u << 1)
#define PSA_STORAGE_FLAG_NO_REPLAY_PROTECTION (1u << 2)

struct psa_storage_info_t {
        size_t capacity;
        size_t size;
        psa_storage_create_flags_t flags;
};

#define PSA_STORAGE_SUPPORT_SET_EXTENDED (1u << 0)

#endif
```

## 839.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 839.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../storage/P026_PSA存储公共定义.md)
- [psa/error.h](../storage/P023_PSA存储返回值.md)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [psa_storage_create_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a1f53bd4fd1ba72bd88e9d7d9eb7da211)
- [psa_storage_info_t](../storage/P027_PSA存储条目元数据.md)
- [capacity](https://docs.zephyrproject.org/latest/doxygen/html/structpsa__storage__info__t.html#a1b2d4b80f2989c0c182bf519442090ae)
- [size](https://docs.zephyrproject.org/latest/doxygen/html/structpsa__storage__info__t.html#a2a18bf8e7a44cc050e088fb34a453a1d)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/structpsa__storage__info__t.html#a3dfb41a4b9bf931f3b3fe96f13c1d289)
- [psa_storage_info_t::capacity](https://docs.zephyrproject.org/latest/doxygen/html/structpsa__storage__info__t.html#a1b2d4b80f2989c0c182bf519442090ae)
- [psa_storage_info_t::size](https://docs.zephyrproject.org/latest/doxygen/html/structpsa__storage__info__t.html#a2a18bf8e7a44cc050e088fb34a453a1d)
- [psa_storage_info_t::flags](https://docs.zephyrproject.org/latest/doxygen/html/structpsa__storage__info__t.html#a3dfb41a4b9bf931f3b3fe96f13c1d289)
- [error.h](../storage/P023_PSA存储返回值.md)

---

[上一章](P838_stmod-plus-connector.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P840_store.h_源码浏览.md)
