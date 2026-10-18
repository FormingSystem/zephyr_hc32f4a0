---
id: learning.zephyr-docs.api-file-interface-reference.page-30
title: ____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_secure\_storage\_\_include\_\_internal\_\_zephyr\_\_secure\_storage\_\_its.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/its_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

安全存储的内部可信存储（ITS）实现。

<a id="details"></a>

```c
#include "its/common.h"
```

查看此文件的源码。

安全存储（secure storage）的内部可信存储（ITS）实现。启用安全存储子系统时，本头文件声明的函数实现 PSA ITS API。不得直接调用这些函数；只有在提供自定义实现（`CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_CUSTOM`）时才可包含此头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 30.1\_函数（Functions）

<a id="r_a6d0c166caa4b40ce95f422d9e4ad5ab5"></a>

```c
psa_status_t secure_storage_its_set (secure_storage_its_caller_id_t caller_id, psa_storage_uid_t uid, size_t data_length, const void *p_data, psa_storage_create_flags_t create_flags)
```

相关声明：[psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)、[secure_storage_its_set](#a6d0c166caa4b40ce95f422d9e4ad5ab5)、[secure_storage_its_caller_id_t](P056_____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its__common.h_文件参考.md#a2369ff303bf323cb4e57f1b970093d2b)、[psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)、[psa_storage_create_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a1f53bd4fd1ba72bd88e9d7d9eb7da211)。

参见 `psa_its_set()`；此函数与其类似。

<a id="r_a2bf3b72ece99582585a223e1f41bf5a9"></a>

```c
psa_status_t secure_storage_its_get (secure_storage_its_caller_id_t caller_id, psa_storage_uid_t uid, size_t data_offset, size_t data_size, void *p_data, size_t *p_data_length)
```

相关声明：[psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)、[secure_storage_its_get](#a2bf3b72ece99582585a223e1f41bf5a9)、[secure_storage_its_caller_id_t](P056_____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its__common.h_文件参考.md#a2369ff303bf323cb4e57f1b970093d2b)、[psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)。

参见 `psa_its_get()`；此函数与其类似。

<a id="r_a6708e5131b0a090d99041bff56dfc84f"></a>

```c
psa_status_t secure_storage_its_get_info (secure_storage_its_caller_id_t caller_id, psa_storage_uid_t uid, struct psa_storage_info_t *p_info)
```

相关声明：[psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)、[secure_storage_its_get_info](#a6708e5131b0a090d99041bff56dfc84f)、[secure_storage_its_caller_id_t](P056_____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its__common.h_文件参考.md#a2369ff303bf323cb4e57f1b970093d2b)、[psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)、[psa_storage_info_t](../storage/P027_PSA存储条目元数据.md)。

参见 `psa_its_get_info()`；此函数与其类似。

<a id="r_a066a5ad089ca154c484b75ad2ff7fd3d"></a>

```c
psa_status_t secure_storage_its_remove (secure_storage_its_caller_id_t caller_id, psa_storage_uid_t uid)
```

相关声明：[psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)、[secure_storage_its_remove](#a066a5ad089ca154c484b75ad2ff7fd3d)、[secure_storage_its_caller_id_t](P056_____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its__common.h_文件参考.md#a2369ff303bf323cb4e57f1b970093d2b)、[psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)。

参见 `psa_its_remove()`；此函数与其类似。

## 30.2\_详细说明（Detailed Documentation）

<a id="a2bf3b72ece99582585a223e1f41bf5a9"></a>

### `secure_storage_its_get()`

```c
psa_status_t secure_storage_its_get ( secure_storage_its_caller_id_t caller_id, psa_storage_uid_t uid, size_t data_offset, size_t data_size, void * p_data, size_t * p_data_length )
```

参见 `psa_its_get()`；此函数与其类似。

<a id="a6708e5131b0a090d99041bff56dfc84f"></a>

### `secure_storage_its_get_info()`

```c
psa_status_t secure_storage_its_get_info ( secure_storage_its_caller_id_t caller_id, psa_storage_uid_t uid, struct psa_storage_info_t * p_info )
```

参见 `psa_its_get_info()`；此函数与其类似。

<a id="a066a5ad089ca154c484b75ad2ff7fd3d"></a>

### `secure_storage_its_remove()`

```c
psa_status_t secure_storage_its_remove ( secure_storage_its_caller_id_t caller_id, psa_storage_uid_t uid )
```

参见 `psa_its_remove()`；此函数与其类似。

<a id="a6d0c166caa4b40ce95f422d9e4ad5ab5"></a>

### `secure_storage_its_set()`

```c
psa_status_t secure_storage_its_set ( secure_storage_its_caller_id_t caller_id, psa_storage_uid_t uid, size_t data_length, const void * p_data, psa_storage_create_flags_t create_flags )
```

参见 `psa_its_set()`；此函数与其类似。


## 30.3\_原页交叉引用（Cross References）

- [its/common.h](../api_source_reference/P843_common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P424_its.h_源码浏览.md)
- [psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)
- [secure_storage_its_caller_id_t](P056_____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its__common.h_文件参考.md#a2369ff303bf323cb4e57f1b970093d2b)
- [psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)
- [psa_storage_create_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a1f53bd4fd1ba72bd88e9d7d9eb7da211)
- [psa_its_set()](https://docs.zephyrproject.org/latest/doxygen/html/internal__trusted__storage_8h.html#a01e5344273e6d776d1f456c4d54a2ed8)
- [psa_its_get()](https://docs.zephyrproject.org/latest/doxygen/html/internal__trusted__storage_8h.html#a387d450b2a21673fba6c56e66c74b5f7)
- [psa_storage_info_t](../storage/P027_PSA存储条目元数据.md)
- [psa_its_get_info()](https://docs.zephyrproject.org/latest/doxygen/html/internal__trusted__storage_8h.html#ae4efe6e7f9088fdf8ef4e126045a432b)
- [psa_its_remove()](https://docs.zephyrproject.org/latest/doxygen/html/internal__trusted__storage_8h.html#abd70b9f9bc063e3651f315408f4ae04c)
- [CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_CUSTOM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE_ITS_IMPLEMENTATION_CUSTOM)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P029_zephyr__dt-bindings__interrupt-controller__ite-it51xxx-intc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P031_zephyr__drivers__clock_control__mchp_clock_pic32cm_pl.h_文件参考.md)
