---
id: learning.zephyr-docs.storage.virtiofsapi-0
title: Virtiofs头文件
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/virtiofs_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第31章\_Virtiofs头文件

原文：[virtiofs_8h](https://docs.zephyrproject.org/latest/doxygen/html/virtiofs_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/fs/virtiofs.h` 提供 **VirtioFS 文件系统（File System）**的数据结构定义。

```c
#include <stdint.h>
```

## 31.1\_文件系统数据结构

`struct virtiofs_fs_data` 表示一次 VirtioFS **挂载（Mount）**使用的文件系统数据。其成员见[Virtiofs文件系统数据](P032_Virtiofs文件系统数据.md)。

---

[上一章：Virtiofs文件系统示例](P030_Virtiofs文件系统示例.md) · [下一章：Virtiofs文件系统数据](P032_Virtiofs文件系统数据.md) · [返回大纲](大纲.md)
