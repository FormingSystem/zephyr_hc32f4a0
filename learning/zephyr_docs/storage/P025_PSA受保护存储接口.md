---
id: learning.zephyr-docs.storage.psastorage-3
title: PSA受保护存储接口
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第25章\_PSA受保护存储接口

原文：[protected__storage_8h](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html)。读取日期：2026-10-13，`latest`。

本页说明**平台安全架构（Platform Security Architecture，PSA）**的**受保护存储（Protected Storage，PS）应用程序编程接口（Application Programming Interface，API）**。更多背景见规范中的 [Protected Storage API](https://arm-software.github.io/psa-api/storage/1.0/overview/architecture.html#the-protected-storage-api)。

包含的公共头文件如下：

```c
#include <psa/storage_common.h>
```

参数中的 `uid` 是存储条目的**唯一标识符（Unique Identifier，UID）**；`create_flags` 为创建标志。状态类型及数值见[返回值参考](P023_PSA存储返回值.md)，标志与类型见[公共定义](P026_PSA存储公共定义.md)。其中 [`PSA_STORAGE_FLAG_WRITE_ONCE`](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a15dbec8d862073de6024924bf015dcdd) 表示**只写一次（Write Once）**。

## 25.1\_接口版本

```c
#define PSA_PS_API_VERSION_MAJOR 1
#define PSA_PS_API_VERSION_MINOR 0
```

主版本为 1，次版本为 0。

## 25.2\_创建或修改条目

```c
psa_status_t psa_ps_set(psa_storage_uid_t uid, size_t data_length,
                         const void *p_data, psa_storage_create_flags_t create_flags);
```

创建新条目或修改已有条目。

| 参数 | 含义 |
| --- | --- |
| `uid` | 数据标识符，必须非零 |
| `data_length` | `p_data` 中要保存的数据大小，单位为字节 |
| `p_data` | 包含待保存数据的缓冲区 |
| `create_flags` | 指定条目属性的标志 |

| 返回值 | 含义 |
| --- | --- |
| [`PSA_SUCCESS`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a4cc859e2c66ca381c7418db3527a65e1) | 操作成功完成。 |
| [`PSA_ERROR_GENERIC_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a8bfafd6baac18ce5d3192d1de256238f) | 发生未具体说明的内部故障。 |
| [`PSA_ERROR_NOT_PERMITTED`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a4d1b8dd8526177a15a210b7afc1accb1) | 给定 `uid` 对应的条目已存在，且创建时使用了 [`PSA_STORAGE_FLAG_WRITE_ONCE`](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a15dbec8d862073de6024924bf015dcdd)。 |
| [`PSA_ERROR_NOT_SUPPORTED`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a1dcc6d130633ed5db8942257581b55dd) | `create_flags` 中至少一个标志不受支持或无效。 |
| [`PSA_ERROR_INVALID_ARGUMENT`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a798df25a505ebf931f7bec1f80f1f85f) | 除 `create_flags` 以外的至少一个参数无效。 |
| [`PSA_ERROR_INSUFFICIENT_STORAGE`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a897a45eb206a6f6b7be7ffbe36f0d766) | 存储介质没有足够空间。 |
| [`PSA_ERROR_STORAGE_FAILURE`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#add169a1af2707862b95fb9df91dfc37d) | 物理存储发生故障，属于致命错误。 |

## 25.3\_读取数据

```c
psa_status_t psa_ps_get(psa_storage_uid_t uid, size_t data_offset,
                         size_t data_size, void *p_data, size_t *p_data_length);
```

读取给定 `uid` 对应的数据。

| 参数 | 方向 | 含义 |
| --- | --- | --- |
| `uid` | 输入 | 数据标识符 |
| `data_offset` | 输入 | 开始读取的位置偏移量，单位为字节 |
| `data_size` | 输入 | 要读取的字节数 |
| `p_data` | 输出 | 成功时接收数据的缓冲区，长度必须至少为 `data_size` 字节 |
| `p_data_length` | 输出 | 成功时写入 `p_data` 的字节数 |

| 返回值 | 含义 |
| --- | --- |
| [`PSA_SUCCESS`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a4cc859e2c66ca381c7418db3527a65e1) | 操作成功完成。 |
| [`PSA_ERROR_GENERIC_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a8bfafd6baac18ce5d3192d1de256238f) | 发生未具体说明的内部故障。 |
| [`PSA_ERROR_INVALID_ARGUMENT`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a798df25a505ebf931f7bec1f80f1f85f) | 至少一个参数无效；当 `data_offset` 大于 `uid` 对应的数据大小时，也可能返回此错误。 |
| [`PSA_ERROR_DOES_NOT_EXIST`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a18646babb2ae6cbde02ea3828bbd9141) | 在存储中找不到给定 `uid`。 |
| [`PSA_ERROR_STORAGE_FAILURE`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#add169a1af2707862b95fb9df91dfc37d) | 物理存储发生故障，属于致命错误。 |
| [`PSA_ERROR_INVALID_SIGNATURE`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a35927f755d232c4766de600f2c49e9f2) | `uid` 对应的数据未通过认证（Authentication）。 |
| [`PSA_ERROR_DATA_CORRUPT`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a9febb81a44bdeb4c6c42bf4f697b13bf) | `uid` 对应的数据已损坏。 |

## 25.4\_读取条目元数据

```c
psa_status_t psa_ps_get_info(psa_storage_uid_t uid, struct psa_storage_info_t *p_info);
```

读取指定条目的**元数据（Metadata）**。

| 参数 | 方向 | 含义 |
| --- | --- | --- |
| `uid` | 输入 | 条目标识符 |
| `p_info` | 输出 | 指向 [`psa_storage_info_t`](https://docs.zephyrproject.org/latest/doxygen/html/structpsa__storage__info__t.html) 结构的指针；成功时用元数据填充该结构 |

结构的容量、数据大小和标志字段见[条目元数据](P027_PSA存储条目元数据.md)。

| 返回值 | 含义 |
| --- | --- |
| [`PSA_SUCCESS`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a4cc859e2c66ca381c7418db3527a65e1) | 操作成功完成。 |
| [`PSA_ERROR_GENERIC_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a8bfafd6baac18ce5d3192d1de256238f) | 发生未具体说明的内部故障。 |
| [`PSA_ERROR_INVALID_ARGUMENT`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a798df25a505ebf931f7bec1f80f1f85f) | `uid` 无效。 |
| [`PSA_ERROR_DOES_NOT_EXIST`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a18646babb2ae6cbde02ea3828bbd9141) | 在存储中找不到给定 `uid`。 |
| [`PSA_ERROR_STORAGE_FAILURE`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#add169a1af2707862b95fb9df91dfc37d) | 物理存储发生故障，属于致命错误。 |
| [`PSA_ERROR_INVALID_SIGNATURE`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a35927f755d232c4766de600f2c49e9f2) | `uid` 对应的数据未通过认证（Authentication）。 |
| [`PSA_ERROR_DATA_CORRUPT`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a9febb81a44bdeb4c6c42bf4f697b13bf) | `uid` 对应的数据已损坏。 |

## 25.5\_删除条目

```c
psa_status_t psa_ps_remove(psa_storage_uid_t uid);
```

删除给定 `uid` 及其关联数据。删除先前保存的数据及其所有相关元数据，包括**回滚保护（Rollback Protection）**数据。返回状态表示操作成功或失败。

`uid` 是要删除的条目的标识符。

| 返回值 | 含义 |
| --- | --- |
| [`PSA_SUCCESS`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a4cc859e2c66ca381c7418db3527a65e1) | 操作成功完成。 |
| [`PSA_ERROR_GENERIC_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a8bfafd6baac18ce5d3192d1de256238f) | 发生未具体说明的内部故障。 |
| [`PSA_ERROR_NOT_PERMITTED`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a4d1b8dd8526177a15a210b7afc1accb1) | 条目创建时使用了 [`PSA_STORAGE_FLAG_WRITE_ONCE`](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a15dbec8d862073de6024924bf015dcdd)。 |
| [`PSA_ERROR_INVALID_ARGUMENT`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a798df25a505ebf931f7bec1f80f1f85f) | `uid` 无效。 |
| [`PSA_ERROR_DOES_NOT_EXIST`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a18646babb2ae6cbde02ea3828bbd9141) | 在存储中找不到给定 `uid`。 |
| [`PSA_ERROR_STORAGE_FAILURE`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#add169a1af2707862b95fb9df91dfc37d) | 物理存储发生故障，属于致命错误。 |

## 25.6\_预留条目容量

```c
psa_status_t psa_ps_create(psa_storage_uid_t uid, size_t capacity,
                           psa_storage_create_flags_t create_flags);
```

为指定 `uid` 预留存储。成功后，该条目的**容量（Capacity）**为 `capacity`，数据**大小（Size）**为 0。

只有后续使用 [`psa_ps_set_extended()`](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#a1630b75fce6941c4d619256822d5de9a) 写入数据时，才有必要调用此函数。如果只使用 [`psa_ps_set()`](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#ac27f8fc33b69e0a9ed09b73195b42eab)，则无需额外调用它。此函数不能替换已有条目，也不能调整已有条目的容量。

| 参数 | 含义 |
| --- | --- |
| `uid` | 要为其预留存储的条目标识符 |
| `capacity` | 要分配的容量，单位为字节 |
| `create_flags` | 指定条目属性的标志 |


| 返回值 | 含义 |
| --- | --- |
| [`PSA_SUCCESS`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a4cc859e2c66ca381c7418db3527a65e1) | 操作成功完成。 |
| [`PSA_ERROR_GENERIC_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a8bfafd6baac18ce5d3192d1de256238f) | 发生未具体说明的内部故障。 |
| [`PSA_ERROR_NOT_SUPPORTED`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a1dcc6d130633ed5db8942257581b55dd) | 实现不支持此函数，或者 `create_flags` 中至少一个标志不受支持或无效。 |
| [`PSA_ERROR_INVALID_ARGUMENT`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a798df25a505ebf931f7bec1f80f1f85f) | `uid` 无效。 |
| [`PSA_ERROR_ALREADY_EXISTS`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#af2b34cc87edc72f3ba90071a08210d20) | 给定 `uid` 对应的条目已存在。 |
| [`PSA_ERROR_INSUFFICIENT_STORAGE`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a897a45eb206a6f6b7be7ffbe36f0d766) | 存储介质没有足够空间。 |
| [`PSA_ERROR_STORAGE_FAILURE`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#add169a1af2707862b95fb9df91dfc37d) | 物理存储发生故障，属于致命错误。 |

## 25.7\_写入部分数据或扩展数据

```c
psa_status_t psa_ps_set_extended(psa_storage_uid_t uid, size_t data_offset,
                                 size_t data_length, const void *p_data);
```

写入指定 `uid` 对应数据的一部分。原文要求在调用前通过 [`psa_ps_create()`](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#aa2c4d67afd77676a95becad71e902508) 预留存储，同时也说明此函数可以覆盖由 [`psa_ps_set()`](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#ac27f8fc33b69e0a9ed09b73195b42eab) 写入的数据。

可以覆盖已有数据，也可以扩展数据，但最多扩展到 [`psa_ps_create()`](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#aa2c4d67afd77676a95becad71e902508) 指定的条目容量，不能在数据中留下空洞。

| 参数 | 含义 |
| --- | --- |
| `uid` | 要写入的条目标识符 |
| `data_offset` | 写入起始偏移量，单位为字节；不能大于当前数据大小 |
| `data_length` | `p_data` 中要写入的数据大小，单位为字节；`data_offset + data_length` 不能大于条目容量 |
| `p_data` | 包含待写入数据的缓冲区 |

译注：原网页将上述公式中的 `+` 错排为列表符号。这里依据[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/secure_storage/include/psa/protected_storage.h)中的注释恢复为加法表达式，避免把长度约束误读成仅约束 `data_length`。


| 返回值 | 含义 |
| --- | --- |
| [`PSA_SUCCESS`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a4cc859e2c66ca381c7418db3527a65e1) | 操作成功完成。 |
| [`PSA_ERROR_GENERIC_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a8bfafd6baac18ce5d3192d1de256238f) | 发生未具体说明的内部故障。 |
| [`PSA_ERROR_NOT_PERMITTED`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a4d1b8dd8526177a15a210b7afc1accb1) | 条目创建时使用了 `PSA_STORAGE_FLAG_WRITE_ONCE`。 |
| [`PSA_ERROR_NOT_SUPPORTED`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a1dcc6d130633ed5db8942257581b55dd) | 实现不支持此函数。 |
| [`PSA_ERROR_INVALID_ARGUMENT`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a798df25a505ebf931f7bec1f80f1f85f) | 至少一个参数无效。 |
| [`PSA_ERROR_DOES_NOT_EXIST`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a18646babb2ae6cbde02ea3828bbd9141) | 在存储中找不到给定 `uid`。 |
| [`PSA_ERROR_STORAGE_FAILURE`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#add169a1af2707862b95fb9df91dfc37d) | 物理存储发生故障，属于致命错误。 |
| [`PSA_ERROR_INVALID_SIGNATURE`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a35927f755d232c4766de600f2c49e9f2) | `uid` 对应的数据未通过认证（Authentication）。 |
| [`PSA_ERROR_DATA_CORRUPT`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a9febb81a44bdeb4c6c42bf4f697b13bf) | `uid` 对应的数据已损坏。 |

## 25.8\_查询可选功能

```c
uint32_t psa_ps_get_support(void);
```

返回一个**位掩码（Bitmask）**，其中置位的标志表示当前实现支持相应可选功能。原文当前只定义了 [`PSA_STORAGE_SUPPORT_SET_EXTENDED`](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#ad9f16fc478036752ffb2ce9e50b2a710)，用于表示支持 [`psa_ps_create()`](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#aa2c4d67afd77676a95becad71e902508) 与 [`psa_ps_set_extended()`](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#a1630b75fce6941c4d619256822d5de9a)。

译注：此函数返回功能位掩码，返回类型是 [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)，并非其他函数使用的 [`psa_status_t`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)。Zephyr 的默认 PS 实现及其限制见[安全存储服务](P021_安全存储服务.md)。

---

[上一章：PSA内部可信存储接口](P024_PSA内部可信存储接口.md) · [下一章：PSA存储公共定义](P026_PSA存储公共定义.md) · [返回大纲](大纲.md)
