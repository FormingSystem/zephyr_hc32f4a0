---
id: learning.zephyr-docs.api-file-reference.page-476
title: ____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第476章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_secure\_storage\_\_include\_\_internal\_\_zephyr\_\_secure\_storage\_\_common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

安全存储子系统（Secure Storage Subsystem）的通用定义。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

安全存储子系统（Secure Storage Subsystem）的通用定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 476.1\_宏定义（Macros）

<a id="r_ae07ad04cdb4e399b0751f58415d5e514"></a>

```c
#define SECURE_STORAGE_ALL_CREATE_FLAGS
```

相关声明：[SECURE_STORAGE_ALL_CREATE_FLAGS](#ae07ad04cdb4e399b0751f58415d5e514)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 476.2\_类型定义（Typedefs）

<a id="r_ac3c7c0ba918fe964b4c39ae0d8047bdd"></a>

```c
typedef uint8_t secure_storage_packed_create_flags_t
```

相关声明：[uint8_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[secure_storage_packed_create_flags_t](#ac3c7c0ba918fe964b4c39ae0d8047bdd)。

## 476.3\_详细说明（Detailed Documentation）

<a id="ae07ad04cdb4e399b0751f58415d5e514"></a>

### `SECURE_STORAGE_ALL_CREATE_FLAGS`

```c
#define SECURE_STORAGE_ALL_CREATE_FLAGS
```

展开值（Value）：

```c
(PSA_STORAGE_FLAG_NONE | \
 PSA_STORAGE_FLAG_WRITE_ONCE | \
 PSA_STORAGE_FLAG_NO_CONFIDENTIALITY | \
 PSA_STORAGE_FLAG_NO_REPLAY_PROTECTION)
```

<a id="ac3c7c0ba918fe964b4c39ae0d8047bdd"></a>

### `secure_storage_packed_create_flags_t`

```c
typedef uint8_t secure_storage_packed_create_flags_t
```


## 476.4\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [查看此文件的源码。](../api_source_supplement_reference/P218_common.h_源码浏览.md)
- [uint8_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [PSA_STORAGE_FLAG_NONE](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a65299349e8643d466eeaeb5bb62cfb6e)
- [PSA_STORAGE_FLAG_WRITE_ONCE](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a15dbec8d862073de6024924bf015dcdd)
- [PSA_STORAGE_FLAG_NO_CONFIDENTIALITY](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#ab3688fcb77630ebdb3774516560b5226)
- [PSA_STORAGE_FLAG_NO_REPLAY_PROTECTION](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a5781482a6bea58c8f9acdb1da921efbe)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astorage__common_8h_html_a15dbec8d862073de6024924bf015dcdd"></a>
<a id="astorage__common_8h_html_a5781482a6bea58c8f9acdb1da921efbe"></a>
<a id="astorage__common_8h_html_a65299349e8643d466eeaeb5bb62cfb6e"></a>
<a id="astorage__common_8h_html_ab3688fcb77630ebdb3774516560b5226"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P475_zephyr__arch__structs.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P477_zephyr__dt-bindings__lora__sx126x.h_文件参考.md)
