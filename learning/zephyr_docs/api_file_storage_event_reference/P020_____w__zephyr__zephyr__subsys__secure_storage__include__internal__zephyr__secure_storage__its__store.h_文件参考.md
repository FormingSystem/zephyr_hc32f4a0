---
id: learning.zephyr-docs.api-file-storage-event-reference.page-20
title: ____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its__store.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/store_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_secure\_storage\_\_include\_\_internal\_\_zephyr\_\_secure\_storage\_\_its\_\_store.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/store_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

安全存储（Secure Storage）的ITS存储模块。

<a id="details"></a>

```c
#include <zephyr/secure_storage/its/common.h>
```

查看此文件的源码。

安全存储（Secure Storage）的内部可信存储（ITS）存储模块（Store Module）。本头文件声明的函数实现 ITS 存储模块，只应由 ITS 实现调用。提供自定义 ITS 存储模块实现（`CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_CUSTOM`）时，可包含此头文件。ITS 实现会串行化修改存储介质（Storage Medium）的操作，但读取可能与其中一个修改操作并发。因此各操作相互之间必须保证原子性（Atomicity），使读取结果要么是条目的旧数据，要么是新数据，绝不能是两者的混合。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 20.1\_函数（Functions）

<a id="r_aed06855314e4dafb4e935d31b6fb21bb"></a>

```c
psa_status_t secure_storage_its_store_set (secure_storage_its_uid_t uid, size_t data_length, const void *data)
```

相关声明：[psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)、[secure_storage_its_store_set](#aed06855314e4dafb4e935d31b6fb21bb)、[secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)。

将 ITS 条目（Entry）的数据写入存储介质（Storage Medium）。

<a id="r_a22d16815fb645ff5cc014f2fe4e9e987"></a>

```c
psa_status_t secure_storage_its_store_get (secure_storage_its_uid_t uid, size_t data_size, void *data, size_t *data_length)
```

相关声明：[psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)、[secure_storage_its_store_get](#a22d16815fb645ff5cc014f2fe4e9e987)、[secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)。

从存储介质（Storage Medium）读取 ITS 条目（Entry）的数据。

<a id="r_a58eb126f3d92112b3ed19d1920d43fa0"></a>

```c
psa_status_t secure_storage_its_store_remove (secure_storage_its_uid_t uid)
```

相关声明：[psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)、[secure_storage_its_store_remove](#a58eb126f3d92112b3ed19d1920d43fa0)、[secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)。

从存储介质（Storage Medium）移除 ITS 条目（Entry）。

## 20.2\_详细说明（Detailed Documentation）

<a id="a22d16815fb645ff5cc014f2fe4e9e987"></a>

### `secure_storage_its_store_get()`

```c
psa_status_t secure_storage_its_store_get ( secure_storage_its_uid_t uid, size_t data_size, void * data, size_t * data_length )
```

从存储介质（Storage Medium）读取 ITS 条目（Entry）的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uid` | 条目的唯一标识符（UID）。 |
| `[in] data_size` | 数据大小（Data Size），单位为字节。 |
| `[out] data` | 用于接收条目所存数据（Stored Data）的缓冲区。 |
| `[out] data_length` | 成功时，写入 `data` 的字节数，可能小于 `data_size`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `PSA_SUCCESS` | 读取成功（Read Succeeded）。 |
| `PSA_ERROR_DOES_NOT_EXIST` | 在存储（Storage）中未找到该条目（Entry）。 |
| `PSA_ERROR_STORAGE_FAILURE` | 发生存储故障（Storage Failure）。 |

<a id="a58eb126f3d92112b3ed19d1920d43fa0"></a>

### `secure_storage_its_store_remove()`

```c
psa_status_t secure_storage_its_store_remove ( secure_storage_its_uid_t uid)
```

从存储介质（Storage Medium）移除 ITS 条目（Entry）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `uid` | 条目的唯一标识符（UID）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `PSA_SUCCESS`，其他值均表示失败。

<a id="aed06855314e4dafb4e935d31b6fb21bb"></a>

### `secure_storage_its_store_set()`

```c
psa_status_t secure_storage_its_store_set ( secure_storage_its_uid_t uid, size_t data_length, const void * data )
```

将 ITS 条目（Entry）的数据写入存储介质（Storage Medium）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `uid` | 条目的唯一标识符（UID）。 |
| `data_length` | `data` 中的字节数（Number of Bytes）。 |
| `data` | 要存储的数据（Data to Store）。 |

**返回（Returns）**：**返回值（Returns）：**`psa_its_set()` 的返回值之一。


## 20.3\_原页交叉引用（Cross References）

- [zephyr/secure_storage/its/common.h](../api_source_reference/P843_common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P840_store.h_源码浏览.md)
- [psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)
- [secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)
- [CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_CUSTOM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_CUSTOM)
- [PSA_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a4cc859e2c66ca381c7418db3527a65e1)
- [PSA_ERROR_DOES_NOT_EXIST](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a18646babb2ae6cbde02ea3828bbd9141)
- [PSA_ERROR_STORAGE_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#add169a1af2707862b95fb9df91dfc37d)
- [psa_its_set()](https://docs.zephyrproject.org/latest/doxygen/html/internal__trusted__storage_8h.html#a01e5344273e6d776d1f456c4d54a2ed8)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P019_zephyr__drivers__stepper__stepper.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P021_zephyr__drivers__firmware__scmi__system.h_文件参考.md)
