---
id: learning.zephyr-docs.api-source-reference.page-429
title: key_ids.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/key__ids_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第429章\_key\_ids.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/key__ids_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/key__ids_8h.html)。

## 429.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="akey__ids_8h_html_a11e986351c65bd3dc3c0fe2cd9926e4b"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/* Copyright (c) 2025 Nordic Semiconductor
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_PSA_KEY_IDS_H_
#define ZEPHYR_INCLUDE_PSA_KEY_IDS_H_


#include <stdint.h>
typedef uint32_t psa_key_id_t;

#define ZEPHYR_PSA_OPENTHREAD_KEY_ID_RANGE_BEGIN (psa_key_id_t)0x20000
#define ZEPHYR_PSA_OPENTHREAD_KEY_ID_RANGE_SIZE  0x10000

#define ZEPHYR_PSA_MATTER_KEY_ID_RANGE_BEGIN (psa_key_id_t)0x30000
#define ZEPHYR_PSA_MATTER_KEY_ID_RANGE_SIZE  0x10000

#define ZEPHYR_PSA_BT_MESH_KEY_ID_RANGE_BEGIN (psa_key_id_t)0x20000000
#define ZEPHYR_PSA_BT_MESH_KEY_ID_RANGE_SIZE  0xC000

#define ZEPHYR_PSA_WIFI_CREDENTIALS_KEY_ID_RANGE_BEGIN (psa_key_id_t)0x20010000
#define ZEPHYR_PSA_WIFI_CREDENTIALS_KEY_ID_RANGE_SIZE  0x100

#define ZEPHYR_PSA_FIDO2_KEY_ID_RANGE_BEGIN (psa_key_id_t)0x20011000
#define ZEPHYR_PSA_FIDO2_KEY_ID_RANGE_SIZE  0x1000

#define ZEPHYR_PSA_APPLICATION_KEY_ID_RANGE_BEGIN (psa_key_id_t)0x30000000
#define ZEPHYR_PSA_APPLICATION_KEY_ID_RANGE_SIZE  0x100000

#endif /* ZEPHYR_INCLUDE_PSA_KEY_IDS_H_ */
```

## 429.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 55 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_PSA_KEY_IDS_H_`。

## 429.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/key__ids_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [psa_key_id_t](https://docs.zephyrproject.org/latest/doxygen/html/key__ids_8h.html#a11e986351c65bd3dc3c0fe2cd9926e4b)

---

[上一章](P428_kernel_includes.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P430_keygen.h_源码浏览.md)
