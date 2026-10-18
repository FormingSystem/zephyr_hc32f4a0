---
id: learning.zephyr-docs.api-file-storage-event-reference.page-22
title: ____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its__transform.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/transform_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_secure\_storage\_\_include\_\_internal\_\_zephyr\_\_secure\_storage\_\_its\_\_transform.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/transform_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

安全存储（Secure Storage）的ITS变换模块。

<a id="details"></a>

```c
#include <zephyr/secure_storage/its/common.h>
```

查看此文件的源码。

安全存储（Secure Storage）的 ITS 转换模块（Transform Module）。本头文件声明的函数实现 ITS 转换模块，只应由 ITS 实现调用。提供自定义转换模块实现（`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_CUSTOM`）时，可包含此头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 22.1\_函数（Functions）

<a id="r_ac976a23f8049c4e2e5b95bf867b9ea24"></a>

```c
psa_status_t secure_storage_its_transform_to_store (secure_storage_its_uid_t uid, size_t data_len, const void *data, secure_storage_packed_create_flags_t create_flags, uint8_t stored_data[static SECURE_STORAGE_ITS_TRANSFORM_MAX_STORED_DATA_SIZE], size_t *stored_data_len)
```

相关声明：[psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)、[secure_storage_its_transform_to_store](#ac976a23f8049c4e2e5b95bf867b9ea24)、[secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)、[secure_storage_packed_create_flags_t](../api_file_reference/P476_____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__common.h_文件参考.md#ac3c7c0ba918fe964b4c39ae0d8047bdd)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将 ITS 条目数据转换为用于存储的形式（Transform for Storage）。

<a id="r_a25353d53a0bce5dea8fc4d42bba8988e"></a>

```c
psa_status_t secure_storage_its_transform_from_store (secure_storage_its_uid_t uid, size_t stored_data_len, const uint8_t stored_data[static SECURE_STORAGE_ITS_TRANSFORM_MAX_STORED_DATA_SIZE], size_t data_size, void *data, size_t *data_len, psa_storage_create_flags_t *create_flags)
```

相关声明：[psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)、[secure_storage_its_transform_from_store](#a25353d53a0bce5dea8fc4d42bba8988e)、[secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[psa_storage_create_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a1f53bd4fd1ba72bd88e9d7d9eb7da211)。

转换并验证 ITS 条目的已存数据（Stored Data），以供使用。

## 22.2\_详细说明（Detailed Documentation）

<a id="a25353d53a0bce5dea8fc4d42bba8988e"></a>

### `secure_storage_its_transform_from_store()`

```c
psa_status_t secure_storage_its_transform_from_store ( secure_storage_its_uid_t uid, size_t stored_data_len, const uint8_t stored_data[static SECURE_STORAGE_ITS_TRANSFORM_MAX_STORED_DATA_SIZE], size_t data_size, void * data, size_t * data_len, psa_storage_create_flags_t * create_flags )
```

转换并验证 ITS 条目的已存数据（Stored Data），以供使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uid` | 条目的唯一标识符（UID）。 |
| `[in] stored_data_len` | `stored_data` 中的字节数（Number of Bytes）。 |
| `[in] stored_data` | 要转换为可用形式的已存数据（Stored Data）。 |
| `[in] data_size` | 数据大小（Data Size），单位为字节。 |
| `[out] data` | 用于写入转换后数据（Transformed Data）的缓冲区。 |
| `[out] data_len` | 成功时，写入 `stored_data` 的字节数。 |
| `[out] create_flags` | 成功时，返回条目的创建标志（Create Flags）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `PSA_SUCCESS`，其他值均表示失败。

<a id="ac976a23f8049c4e2e5b95bf867b9ea24"></a>

### `secure_storage_its_transform_to_store()`

```c
psa_status_t secure_storage_its_transform_to_store ( secure_storage_its_uid_t uid, size_t data_len, const void * data, secure_storage_packed_create_flags_t create_flags, uint8_t stored_data[static SECURE_STORAGE_ITS_TRANSFORM_MAX_STORED_DATA_SIZE], size_t * stored_data_len )
```

将 ITS 条目数据转换为用于存储的形式（Transform for Storage）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uid` | 条目的唯一标识符（UID）。 |
| `[in] data_len` | `data` 中的字节数（Number of Bytes）。 |
| `[in] data` | 要转换为存储形式的数据（Data）。 |
| `[in] create_flags` | 条目的创建标志（Create Flags）。只能包含有效的 `PSA_STORAGE_FLAG_*` 值，并作为 `stored_data` 的一部分存储。 |
| `[out] stored_data` | 用于写入转换后数据（Transformed Data）的缓冲区。 |
| `[out] stored_data_len` | 成功时，写入 `stored_data` 的字节数。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `PSA_SUCCESS`，其他值均表示失败。


## 22.3\_原页交叉引用（Cross References）

- [zephyr/secure_storage/its/common.h](../api_source_reference/P843_common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P875_transform.h_源码浏览.md)
- [psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)
- [secure_storage_its_uid_t](../platform_security_model_reference/P053_secure_storage_its_uid_t_结构体.md)
- [secure_storage_packed_create_flags_t](../api_file_reference/P476_____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__common.h_文件参考.md#ac3c7c0ba918fe964b4c39ae0d8047bdd)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [psa_storage_create_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a1f53bd4fd1ba72bd88e9d7d9eb7da211)
- [CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_CUSTOM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_CUSTOM)
- [PSA_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a4cc859e2c66ca381c7418db3527a65e1)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P021_zephyr__drivers__firmware__scmi__system.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P023_zephyr__drivers__uart_pipe.h_文件参考.md)
