---
id: learning.zephyr-docs.intercore_reference.ipcsvc-113
title: IPC服务端点结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structipc__ept.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第113章\_IPC服务端点结构

原文：[structipc__ept](https://docs.zephyrproject.org/latest/doxygen/html/structipc__ept.html)。读取日期：2026-10-13，`latest`。

`ipc_ept`是 IPC 处理器间通信（Inter-Processor Communication）服务的端点实例（Endpoint Instance）结构，来自`zephyr/ipc/ipc_service.h`。

```c
struct ipc_ept {

        const struct device *instance;

        void *token;
};
```

## 113.1\_成员与后端令牌

| 类型 | 成员 | 含义 |
| --- | --- | --- |
| `const struct device *` | `instance` | 该端点所属的实例（Instance） |
| `void *` | `token` | 后端专用令牌（Backend-specific Token），用于在实例中标识端点 |

令牌由具体后端实现，API 用户无须关心其内部含义。这里 API 指应用程序编程接口（Application Programming Interface）。

注册、注销和发送等操作见[IPC服务公共接口](P111_IPC服务公共接口.md)；完整可见定义见[头文件源码](P118_IPC服务完整头文件.md)。

---

[上一章：IPC服务回调结构](P112_IPC服务回调结构.md) · [下一章：IPC服务端点配置](P114_IPC服务端点配置.md) · [返回大纲](大纲.md)
