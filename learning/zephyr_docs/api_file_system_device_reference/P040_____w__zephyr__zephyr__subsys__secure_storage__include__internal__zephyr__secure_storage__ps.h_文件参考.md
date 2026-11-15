---
id: learning.zephyr-docs.api-file-system-device-reference.page-40
title: ____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__ps.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ps_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_secure\_storage\_\_include\_\_internal\_\_zephyr\_\_secure\_storage\_\_ps.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ps_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

安全存储的受保护存储（PS）实现。

<a id="details"></a>

```c
#include <psa/storage_common.h>
```

查看此文件的源码。

安全存储（secure storage）的受保护存储（Protected Storage，PS）实现。启用安全存储子系统时，本头文件声明的函数实现 PSA PS API。不得直接调用这些函数；只有在提供自定义实现（`CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_CUSTOM`）时才可包含此头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 40.1\_函数（Functions）

<a id="r_ab0be3c9374c1db65b45c43fdc6c05825"></a>

```c
psa_status_t secure_storage_ps_set (const psa_storage_uid_t uid, size_t data_length, const void *p_data, psa_storage_create_flags_t create_flags)
```

相关声明：[psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)、[secure_storage_ps_set](#ab0be3c9374c1db65b45c43fdc6c05825)、[psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)、[psa_storage_create_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a1f53bd4fd1ba72bd88e9d7d9eb7da211)。

参见 `psa_ps_set()`；此函数与其类似。

<a id="r_a0387828802c41350b9572a1555ecdeac"></a>

```c
psa_status_t secure_storage_ps_get (const psa_storage_uid_t uid, size_t data_offset, size_t data_length, void *p_data, size_t *p_data_length)
```

相关声明：[psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)、[secure_storage_ps_get](#a0387828802c41350b9572a1555ecdeac)、[psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)。

参见 `psa_ps_get()`；此函数与其类似。

<a id="r_af6c6741b58d91798e2a9c2b3644f0bf1"></a>

```c
psa_status_t secure_storage_ps_get_info (const psa_storage_uid_t uid, struct psa_storage_info_t *p_info)
```

相关声明：[psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)、[secure_storage_ps_get_info](#af6c6741b58d91798e2a9c2b3644f0bf1)、[psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)、[psa_storage_info_t](../storage/P027_PSA存储条目元数据.md)。

参见 `psa_ps_get_info()`；此函数与其类似。

<a id="r_aef4fa69c85d80640a909868ad1749e8c"></a>

```c
psa_status_t secure_storage_ps_remove (const psa_storage_uid_t uid)
```

相关声明：[psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)、[secure_storage_ps_remove](#aef4fa69c85d80640a909868ad1749e8c)、[psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)。

参见 `psa_ps_remove()`；此函数与其类似。

<a id="r_ae044a9d36445840539578b9ea3a1e4d0"></a>

```c
psa_status_t secure_storage_ps_create (psa_storage_uid_t uid, size_t capacity, psa_storage_create_flags_t create_flags)
```

相关声明：[psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)、[secure_storage_ps_create](#ae044a9d36445840539578b9ea3a1e4d0)、[psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)、[psa_storage_create_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a1f53bd4fd1ba72bd88e9d7d9eb7da211)。

参见 `psa_ps_create()`；此函数与其类似。

<a id="r_ab1612b91d341295578e16eb64d7035c4"></a>

```c
psa_status_t secure_storage_ps_set_extended (psa_storage_uid_t uid, size_t data_offset, size_t data_length, const void *p_data)
```

相关声明：[psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)、[secure_storage_ps_set_extended](#ab1612b91d341295578e16eb64d7035c4)、[psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)。

参见 `psa_ps_set_extended()`；此函数与其类似。

## 40.2\_详细说明（Detailed Documentation）

<a id="ae044a9d36445840539578b9ea3a1e4d0"></a>

### `secure_storage_ps_create()`

```c
psa_status_t secure_storage_ps_create ( psa_storage_uid_t uid, size_t capacity, psa_storage_create_flags_t create_flags )
```

参见 `psa_ps_create()`；此函数与其类似。

<a id="a0387828802c41350b9572a1555ecdeac"></a>

### `secure_storage_ps_get()`

```c
psa_status_t secure_storage_ps_get ( const psa_storage_uid_t uid, size_t data_offset, size_t data_length, void * p_data, size_t * p_data_length )
```

参见 `psa_ps_get()`；此函数与其类似。

<a id="af6c6741b58d91798e2a9c2b3644f0bf1"></a>

### `secure_storage_ps_get_info()`

```c
psa_status_t secure_storage_ps_get_info ( const psa_storage_uid_t uid, struct psa_storage_info_t * p_info )
```

参见 `psa_ps_get_info()`；此函数与其类似。

<a id="aef4fa69c85d80640a909868ad1749e8c"></a>

### `secure_storage_ps_remove()`

```c
psa_status_t secure_storage_ps_remove ( const psa_storage_uid_t uid)
```

参见 `psa_ps_remove()`；此函数与其类似。

<a id="ab0be3c9374c1db65b45c43fdc6c05825"></a>

### `secure_storage_ps_set()`

```c
psa_status_t secure_storage_ps_set ( const psa_storage_uid_t uid, size_t data_length, const void * p_data, psa_storage_create_flags_t create_flags )
```

参见 `psa_ps_set()`；此函数与其类似。

<a id="ab1612b91d341295578e16eb64d7035c4"></a>

### `secure_storage_ps_set_extended()`

```c
psa_status_t secure_storage_ps_set_extended ( psa_storage_uid_t uid, size_t data_offset, size_t data_length, const void * p_data )
```

参见 `psa_ps_set_extended()`；此函数与其类似。


## 40.3\_原页交叉引用（Cross References）

- [psa/storage_common.h](../api_source_reference/P839_storage_common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P677_ps.h_源码浏览.md)
- [psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)
- [psa_storage_uid_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087)
- [psa_storage_create_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a1f53bd4fd1ba72bd88e9d7d9eb7da211)
- [psa_ps_set()](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#ac27f8fc33b69e0a9ed09b73195b42eab)
- [psa_ps_get()](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#a2ad1b8347d8cf174c028f0c485a66db6)
- [psa_storage_info_t](../storage/P027_PSA存储条目元数据.md)
- [psa_ps_get_info()](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#af716b24d0761837d1c7b70042bd4966f)
- [psa_ps_remove()](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#a147a92d8387de36c32a8ede10d6d9a02)
- [psa_ps_create()](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#aa2c4d67afd77676a95becad71e902508)
- [psa_ps_set_extended()](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#a1630b75fce6941c4d619256822d5de9a)
- [CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_CUSTOM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_CUSTOM)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P039_zephyr__bluetooth__mesh__priv_beacon_cli.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P041_zephyr__dt-bindings__sensor__qdec_nrf.h_文件参考.md)
