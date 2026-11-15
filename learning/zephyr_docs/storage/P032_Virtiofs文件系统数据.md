---
id: learning.zephyr-docs.storage.virtiofsapi-1
title: Virtiofs文件系统数据
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvirtiofs__fs__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第32章\_Virtiofs文件系统数据

原文：[structvirtiofs__fs__data](https://docs.zephyrproject.org/latest/doxygen/html/structvirtiofs__fs__data.html)。读取日期：2026-10-13，`latest`。

`struct virtiofs_fs_data` 保存一次 **VirtioFS 文件系统（File System）挂载（Mount）**使用的数据。

```c
#include <zephyr/fs/virtiofs.h>
```

## 32.1\_写请求大小

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`max_write`](https://docs.zephyrproject.org/latest/doxygen/html/structvirtiofs__fs__data.html#aec6fef87ac7970052ae1b1d7471e14e5) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 单次**写请求（Write Request）**允许的最大大小，单位为字节（Byte） |

本结构的参考文档由 `zephyr/fs/virtiofs.h` 生成。

---

[上一章：Virtiofs头文件](P031_Virtiofs头文件.md) · [下一章：文件系统接口](P033_文件系统接口.md) · [返回大纲](大纲.md)
