---
id: learning.zephyr-docs.api-file-interface-reference.page-56
title: ____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its__common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_secure\_storage\_\_include\_\_internal\_\_zephyr\_\_secure\_storage\_\_its\_\_common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

安全存储子系统（Secure Storage Subsystem）内部可信存储（ITS）API的通用定义。

<a id="details"></a>

```c
#include "../common.h"
#include <zephyr/toolchain.h>
#include <psa/storage_common.h>
```

查看此文件的源码。

安全存储子系统（Secure Storage Subsystem）内部可信存储（ITS）API的通用定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 56.1\_数据结构（Data Structures）

<a id="r_secure_5Fstorage_5Fits_5Fuid_5Ft"></a>

```c
struct secure_storage_its_uid_t
```

相关声明：[secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)。

内部可信存储（ITS）条目的UID，由调用方ID与条目ID组成。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 56.2\_宏定义（Macros）

<a id="r_a2ee97ffbf1145cf2d52ec6f27113dd99"></a>

```c
#define SECURE_STORAGE_ITS_UID_BIT_SIZE 30
```

相关声明：[SECURE_STORAGE_ITS_UID_BIT_SIZE](#a2ee97ffbf1145cf2d52ec6f27113dd99)。

<a id="r_a964e029c0c87aea5239bfb97cc3f66f0"></a>

```c
#define SECURE_STORAGE_ITS_CALLER_ID_BIT_SIZE 2
```

相关声明：[SECURE_STORAGE_ITS_CALLER_ID_BIT_SIZE](#a964e029c0c87aea5239bfb97cc3f66f0)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 56.3\_枚举（Enumerations）

<a id="r_a2369ff303bf323cb4e57f1b970093d2b"></a>

```c
enum secure_storage_its_caller_id_t { SECURE_STORAGE_ITS_CALLER_PSA_ITS , SECURE_STORAGE_ITS_CALLER_PSA_PS , SECURE_STORAGE_ITS_CALLER_PSA_CRYPTO , SECURE_STORAGE_ITS_CALLER_COUNT }
```

相关声明：[secure_storage_its_caller_id_t](#a2369ff303bf323cb4e57f1b970093d2b)、[SECURE_STORAGE_ITS_CALLER_PSA_ITS](#a2369ff303bf323cb4e57f1b970093d2ba8ee890874c86e0717973bc03208499bd)、[SECURE_STORAGE_ITS_CALLER_PSA_PS](#a2369ff303bf323cb4e57f1b970093d2badb6049a90872ae6773af2817093cce5d)、[SECURE_STORAGE_ITS_CALLER_PSA_CRYPTO](#a2369ff303bf323cb4e57f1b970093d2ba5f757e2cf7ded49541f9af38ca6ef00e)、[SECURE_STORAGE_ITS_CALLER_COUNT](#a2369ff303bf323cb4e57f1b970093d2bab584518773eefcb3731ec57ae6f4f21f)。

发起 ITS API 调用的调用方标识符（caller ID）。

## 56.4\_详细说明（Detailed Documentation）

<a id="a964e029c0c87aea5239bfb97cc3f66f0"></a>

### `SECURE_STORAGE_ITS_CALLER_ID_BIT_SIZE`

```c
#define SECURE_STORAGE_ITS_CALLER_ID_BIT_SIZE 2
```

<a id="a2ee97ffbf1145cf2d52ec6f27113dd99"></a>

### `SECURE_STORAGE_ITS_UID_BIT_SIZE`

```c
#define SECURE_STORAGE_ITS_UID_BIT_SIZE 30
```

<a id="a2369ff303bf323cb4e57f1b970093d2b"></a>

### `secure_storage_its_caller_id_t`

```c
enum secure_storage_its_caller_id_t
```

发起 ITS API 调用的调用方标识符（caller ID）。

用于为不同调用方划分命名空间（namespace），并可对它们采用不同的处理方式。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SECURE_STORAGE_ITS_CALLER_PSA_ITS` | 调用来自 `psa_its_*()` 函数时。 |
| `SECURE_STORAGE_ITS_CALLER_PSA_PS` | 调用来自 `psa_ps_*()` 函数时。 |
| `SECURE_STORAGE_ITS_CALLER_PSA_CRYPTO` | 调用来自 PSA Crypto 实现时。 |
| `SECURE_STORAGE_ITS_CALLER_COUNT` |  |


## 56.5\_原页交叉引用（Cross References）

- [../common.h](../api_source_supplement_reference/P218_common.h_源码浏览.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [psa/storage_common.h](../api_source_reference/P839_storage_common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P843_common.h_源码浏览.md)
- [secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a2369ff303bf323cb4e57f1b970093d2ba8ee890874c86e0717973bc03208499bd"></a>
<a id="a2369ff303bf323cb4e57f1b970093d2badb6049a90872ae6773af2817093cce5d"></a>
<a id="a2369ff303bf323cb4e57f1b970093d2ba5f757e2cf7ded49541f9af38ca6ef00e"></a>
<a id="a2369ff303bf323cb4e57f1b970093d2bab584518773eefcb3731ec57ae6f4f21f"></a>

---

[上一章](P055_zephyr__dt-bindings__gpio__stm32-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P057_____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its__store__settings.h_文件参考.md)
