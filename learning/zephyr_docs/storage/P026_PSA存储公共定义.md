---
id: learning.zephyr-docs.storage.psastorage-4
title: PSA存储公共定义
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第26章\_PSA存储公共定义

原文：[storage__common_8h](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html)。读取日期：2026-10-13，`latest`。

`psa/storage_common.h` 提供**平台安全架构（Platform Security Architecture，PSA）安全存储应用程序编程接口（Secure Storage API）**的公共定义，包含以下头文件：

```c
#include <psa/error.h>
#include <stddef.h>
```

## 26.1\_公共类型

```c
typedef uint32_t psa_storage_uid_t;
typedef uint32_t psa_storage_create_flags_t;
```

[`psa_storage_uid_t`](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#af5302147015dd30a2342728c98945087) 是用于标识条目的**唯一标识符（Unique Identifier，UID）**类型。[`psa_storage_create_flags_t`](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a1f53bd4fd1ba72bd88e9d7d9eb7da211) 表示创建条目时使用的标志。

译注：这里按此 Zephyr 参考页保留 [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)，不替换为其他 PSA 实现的类型；此实现的可用 UID 范围和规范差异见[安全存储服务](P021_安全存储服务.md)。

## 26.2\_创建标志

| 宏 | 定义值 | 含义 |
| --- | --- | --- |
| [`PSA_STORAGE_FLAG_NONE`](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a65299349e8643d466eeaeb5bb62cfb6e) | `0u` | 不传入任何标志 |
| [`PSA_STORAGE_FLAG_WRITE_ONCE`](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a15dbec8d862073de6024924bf015dcdd) | `(1u << 0)` | **只写一次（Write Once）**：此 UID 对应的数据不能再修改或删除 |
| [`PSA_STORAGE_FLAG_NO_CONFIDENTIALITY`](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#ab3688fcb77630ebdb3774516560b5226) | `(1u << 1)` | 此 UID 对应的数据是公开数据，只要求**完整性（Integrity）**，不要求**机密性（Confidentiality）** |
| [`PSA_STORAGE_FLAG_NO_REPLAY_PROTECTION`](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a5781482a6bea58c8f9acdb1da921efbe) | `(1u << 2)` | 此 UID 对应的数据不要求**重放保护（Replay Protection）** |

## 26.3\_可选功能支持标志

```c
#define PSA_STORAGE_SUPPORT_SET_EXTENDED (1u << 0)
```

此标志表示支持 [`psa_ps_create()`](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#aa2c4d67afd77676a95becad71e902508) 和 [`psa_ps_set_extended()`](https://docs.zephyrproject.org/latest/doxygen/html/protected__storage_8h.html#a1630b75fce6941c4d619256822d5de9a)。可通过[受保护存储接口](P025_PSA受保护存储接口.md)中的 `psa_ps_get_support()` 查询。

## 26.4\_元数据结构

`struct psa_storage_info_t` 表示特定条目关联的**元数据（Metadata）**。字段定义见[条目元数据](P027_PSA存储条目元数据.md)。

---

[上一章：PSA受保护存储接口](P025_PSA受保护存储接口.md) · [下一章：PSA存储条目元数据](P027_PSA存储条目元数据.md) · [返回大纲](大纲.md)
