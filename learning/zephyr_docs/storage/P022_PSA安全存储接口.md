---
id: learning.zephyr-docs.storage.psastorage-0
title: PSA安全存储接口
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__psa__secure__storage.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第22章\_PSA安全存储接口

原文：[group__psa__secure__storage](https://docs.zephyrproject.org/latest/doxygen/html/group__psa__secure__storage.html)。读取日期：2026-10-13，`latest`。

**平台安全架构（Platform Security Architecture，PSA）安全存储应用程序编程接口（Secure Storage API）**的文档版本为 **1.0.4**。规范全文见 [PSA Certified Secure Storage API](https://arm-software.github.io/psa-api/storage/1.0/)。

## 22.1\_接口文件

| 头文件 | 内容 |
| --- | --- |
| [`error.h`](P023_PSA存储返回值.md) | PSA 安全存储 API 的返回值 |
| [`internal_trusted_storage.h`](P024_PSA内部可信存储接口.md) | **内部可信存储（Internal Trusted Storage，ITS）**API |
| [`protected_storage.h`](P025_PSA受保护存储接口.md) | **受保护存储（Protected Storage，PS）**API |
| [`storage_common.h`](P026_PSA存储公共定义.md) | PSA 安全存储 API 的公共定义 |

译注：Zephyr 实现的功能范围与规范差异见[安全存储服务](P021_安全存储服务.md)。接口存在不代表当前配置提供全部可选功能或全部安全保证。

---

[上一章：安全存储服务](P021_安全存储服务.md) · [下一章：PSA存储返回值](P023_PSA存储返回值.md) · [返回大纲](大纲.md)
