---
id: learning.zephyr-docs.storage.psastorage-1
title: PSA存储返回值
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第23章\_PSA存储返回值

原文：[subsys_2secure__storage_2include_2psa_2error_8h](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html)。读取日期：2026-10-13，`latest`。

本页定义**平台安全架构（Platform Security Architecture，PSA）安全存储应用程序编程接口（Secure Storage API）**使用的状态类型和返回值。头文件为 `psa/error.h`，包含：

```c
#include <stdint.h>
```

## 23.1\_状态类型

```c
typedef int32_t psa_status_t;
```

[`psa_status_t`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9) 表示函数返回状态，取值为 [`PSA_SUCCESS`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a4cc859e2c66ca381c7418db3527a65e1) 或本页定义的某个 `PSA_ERROR_*`。

## 23.2\_返回值定义

| 宏 | 定义值 | 含义 |
| --- | --- | --- |
| [`PSA_SUCCESS`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a4cc859e2c66ca381c7418db3527a65e1) | `((psa_status_t)0)` | 操作成功完成 |
| [`PSA_ERROR_GENERIC_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a8bfafd6baac18ce5d3192d1de256238f) | `((psa_status_t)-132)` | 发生未具体说明的内部故障 |
| [`PSA_ERROR_NOT_PERMITTED`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a4d1b8dd8526177a15a210b7afc1accb1) | `((psa_status_t)-133)` | 给定 `uid` 对应的条目已存在，且创建时使用了 [`PSA_STORAGE_FLAG_WRITE_ONCE`](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a15dbec8d862073de6024924bf015dcdd) |
| [`PSA_ERROR_NOT_SUPPORTED`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a1dcc6d130633ed5db8942257581b55dd) | `((psa_status_t)-134)` | 不支持该函数，或者 `create_flags` 中至少一个标志不受支持或无效 |
| [`PSA_ERROR_INVALID_ARGUMENT`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a798df25a505ebf931f7bec1f80f1f85f) | `((psa_status_t)-135)` | 除 `create_flags` 以外的至少一个参数无效 |
| [`PSA_ERROR_ALREADY_EXISTS`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#af2b34cc87edc72f3ba90071a08210d20) | `((psa_status_t)-139)` | 给定 `uid` 对应的条目已存在 |
| [`PSA_ERROR_DOES_NOT_EXIST`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a18646babb2ae6cbde02ea3828bbd9141) | `((psa_status_t)-140)` | 在存储中找不到给定 `uid` |
| [`PSA_ERROR_INSUFFICIENT_STORAGE`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a897a45eb206a6f6b7be7ffbe36f0d766) | `((psa_status_t)-142)` | 存储介质没有足够空间 |
| [`PSA_ERROR_STORAGE_FAILURE`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#add169a1af2707862b95fb9df91dfc37d) | `((psa_status_t)-146)` | 物理存储发生故障，属于致命错误 |
| [`PSA_ERROR_INVALID_SIGNATURE`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a35927f755d232c4766de600f2c49e9f2) | `((psa_status_t)-149)` | `uid` 对应的数据未通过**认证（Authentication）** |
| [`PSA_ERROR_DATA_CORRUPT`](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a9febb81a44bdeb4c6c42bf4f697b13bf) | `((psa_status_t)-152)` | `uid` 对应的数据已损坏 |

**唯一标识符（Unique Identifier，UID）**用于标识存储条目；[`PSA_STORAGE_FLAG_WRITE_ONCE`](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a15dbec8d862073de6024924bf015dcdd) 表示**只写一次（Write Once）**，其定义见[公共标志](P026_PSA存储公共定义.md)。每个函数实际列出的错误集合和参数限制见对应函数参考页。

---

[上一章：PSA安全存储接口](P022_PSA安全存储接口.md) · [下一章：PSA内部可信存储接口](P024_PSA内部可信存储接口.md) · [返回大纲](大纲.md)
