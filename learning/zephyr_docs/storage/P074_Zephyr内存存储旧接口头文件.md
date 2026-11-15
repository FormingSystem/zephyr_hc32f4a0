---
id: learning.zephyr-docs.storage.storagehdr-3
title: Zephyr内存存储旧接口头文件
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fs_2zms_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第74章\_Zephyr内存存储旧接口头文件

原文：[fs_2zms_8h](https://docs.zephyrproject.org/latest/doxygen/html/fs_2zms_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/fs/zms.h` 是**Zephyr 内存存储（Zephyr Memory Storage，ZMS）应用编程接口（Application Programming Interface，API）**的旧接口头文件（Legacy Interface Header）。

## 74.1\_包含关系

官方头文件的包含项如下：

```c
#include <zephyr/kvss/zms.h>
```

[查看官方源文件页面](https://docs.zephyrproject.org/latest/doxygen/html/fs_2zms_8h_source.html)。

## 74.2\_弃用说明

该头文件已**弃用（Deprecated）**。请改用 `zephyr/kvss/zms.h`；原文件通过上面的包含指令转入新头文件。

---

[上一章：非易失性存储头文件](P073_非易失性存储头文件.md) · [下一章：Zephyr内存存储头文件](P075_Zephyr内存存储头文件.md) · [返回大纲](大纲.md)
