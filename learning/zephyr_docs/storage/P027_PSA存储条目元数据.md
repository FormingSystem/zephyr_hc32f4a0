---
id: learning.zephyr-docs.storage.psastorage-5
title: PSA存储条目元数据
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpsa__storage__info__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第27章\_PSA存储条目元数据

原文：[structpsa__storage__info__t](https://docs.zephyrproject.org/latest/doxygen/html/structpsa__storage__info__t.html)。读取日期：2026-10-13，`latest`。

`struct psa_storage_info_t` 表示特定存储条目关联的**元数据（Metadata）**，由**平台安全架构（Platform Security Architecture，PSA）**存储接口使用。

```c
#include <psa/storage_common.h>
```

## 27.1\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`capacity`](https://docs.zephyrproject.org/latest/doxygen/html/structpsa__storage__info__t.html#a1b2d4b80f2989c0c182bf519442090ae) | `size_t` | 为该条目分配的存储**容量（Capacity）** |
| [`size`](https://docs.zephyrproject.org/latest/doxygen/html/structpsa__storage__info__t.html#a2a18bf8e7a44cc050e088fb34a453a1d) | `size_t` | 条目当前数据的**大小（Size）** |
| [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/structpsa__storage__info__t.html#a3dfb41a4b9bf931f3b3fe96f13c1d289) | [`psa_storage_create_flags_t`](https://docs.zephyrproject.org/latest/doxygen/html/storage__common_8h.html#a1f53bd4fd1ba72bd88e9d7d9eb7da211) | 创建条目时使用的标志 |

译注：容量与当前数据大小是两个不同字段。例如，[受保护存储](P025_PSA受保护存储接口.md)的 `psa_ps_create()` 成功后，容量为请求值，而数据大小为 0。创建标志见[公共定义](P026_PSA存储公共定义.md)。

## 27.2\_定义来源

此结构的参考文档由 Zephyr 源码中的 `subsys/secure_storage/include/psa/storage_common.h` 生成。

---

[上一章：PSA存储公共定义](P026_PSA存储公共定义.md) · [下一章：NVMe磁盘驱动](P028_NVMe磁盘驱动.md) · [返回大纲](大纲.md)
