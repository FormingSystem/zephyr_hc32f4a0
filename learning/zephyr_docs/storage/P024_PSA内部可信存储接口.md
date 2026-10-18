---
id: learning.zephyr-docs.storage.psastorage-2
title: PSA内部可信存储接口
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/internal__trusted__storage_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第24章\_PSA内部可信存储接口

原文：[internal__trusted__storage_8h](https://docs.zephyrproject.org/latest/doxygen/html/internal__trusted__storage_8h.html)。读取日期：2026-10-13，`latest`。

本页说明**平台安全架构（Platform Security Architecture，PSA）**的**内部可信存储（Internal Trusted Storage，ITS）应用程序编程接口（Application Programming Interface，API）**。更多背景见规范中的 [Internal Trusted Storage API](https://arm-software.github.io/psa-api/storage/1.0/overview/architecture.html#the-internal-trusted-storage-api)。

包含的公共头文件如下：

```c
#include <psa/storage_common.h>
```

参数中的 `uid` 是存储条目的**唯一标识符（Unique Identifier，UID）**；`create_flags` 为创建标志。状态类型及数值见[返回值参考](P023_PSA存储返回值.md)，标志与类型见[公共定义](P026_PSA存储公共定义.md)。其中 [`PSA_STORAGE_FLAG_WRITE_ONCE`](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a15dbec8d862073de6024924bf015dcdd) 表示**只写一次（Write Once）**。

## 24.1\_接口版本

```c
#define PSA_ITS_API_VERSION_MAJOR 1
#define PSA_ITS_API_VERSION_MINOR 0
```

主版本为 1，次版本为 0。

## 24.2\_创建或修改条目

```c
psa_status_t psa_its_set(psa_storage_uid_t uid, size_t data_length,
                         const void *p_data, psa_storage_create_flags_t create_flags);
```

创建新条目或修改已有条目。数据保存在内部存储中。

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

## 24.3\_读取数据

```c
psa_status_t psa_its_get(psa_storage_uid_t uid, size_t data_offset,
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

## 24.4\_读取条目元数据

```c
psa_status_t psa_its_get_info(psa_storage_uid_t uid, struct psa_storage_info_t *p_info);
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

## 24.5\_删除条目

```c
psa_status_t psa_its_remove(psa_storage_uid_t uid);
```

删除给定 `uid` 及其关联数据。从内部存储中删除该条目的所有数据。

`uid` 是要删除的条目的标识符。

| 返回值 | 含义 |
| --- | --- |
| [`PSA_SUCCESS`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a4cc859e2c66ca381c7418db3527a65e1) | 操作成功完成。 |
| [`PSA_ERROR_NOT_PERMITTED`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a4d1b8dd8526177a15a210b7afc1accb1) | 条目创建时使用了 `PSA_STORAGE_FLAG_WRITE_ONCE`。 |
| [`PSA_ERROR_INVALID_ARGUMENT`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a798df25a505ebf931f7bec1f80f1f85f) | `uid` 无效。 |
| [`PSA_ERROR_DOES_NOT_EXIST`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a18646babb2ae6cbde02ea3828bbd9141) | 在存储中找不到给定 `uid`。 |
| [`PSA_ERROR_STORAGE_FAILURE`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#add169a1af2707862b95fb9df91dfc37d) | 物理存储发生故障，属于致命错误。 |

---

[上一章：PSA存储返回值](P023_PSA存储返回值.md) · [下一章：PSA受保护存储接口](P025_PSA受保护存储接口.md) · [返回大纲](大纲.md)
