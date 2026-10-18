---
id: learning.zephyr-docs.intercore_reference.ipcsvc-119
title: IPC服务后端头文件参考
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ipc__service__backend_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第119章\_IPC服务后端头文件参考

原文：[ipc__service__backend_8h](https://docs.zephyrproject.org/latest/doxygen/html/ipc__service__backend_8h.html)。读取日期：2026-10-13，`latest`。

本页是 IPC 处理器间通信（Inter-Processor Communication）服务后端头文件`zephyr/ipc/ipc_service_backend.h`的参考索引。

## 119.1\_包含文件

```c
#include <zephyr/ipc/ipc_service.h>
#include <zephyr/kernel.h>
#include <stdio.h>
```

## 119.2\_数据结构

原页列出[`ipc_service_backend`](P116_IPC服务后端操作结构.md)，即后端配置结构（Backend Configuration Structure）。它包含实例开关、端点注册／注销以及数据和缓冲区操作的函数指针。

原文件完整可见代码见[IPC服务后端完整头文件](P120_IPC服务后端完整头文件.md)，其分组入口见[IPC服务后端接口](P115_IPC服务后端接口.md)。

---

[上一章：IPC服务完整头文件](P118_IPC服务完整头文件.md) · [下一章：IPC服务后端完整头文件](P120_IPC服务后端完整头文件.md) · [返回大纲](大纲.md)
