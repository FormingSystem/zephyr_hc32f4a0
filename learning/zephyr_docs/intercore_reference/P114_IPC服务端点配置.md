---
id: learning.zephyr-docs.intercore_reference.ipcsvc-114
title: IPC服务端点配置
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structipc__ept__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第114章\_IPC服务端点配置

原文：[structipc__ept__cfg](https://docs.zephyrproject.org/latest/doxygen/html/structipc__ept__cfg.html)。读取日期：2026-10-13，`latest`。

`ipc_ept_cfg`是 IPC 处理器间通信（Inter-Processor Communication）服务的端点配置（Endpoint Configuration）结构，来自`zephyr/ipc/ipc_service.h`。

```c
struct ipc_ept_cfg {

        const char *name;

        int prio;

        struct ipc_service_cb cb;

        void *priv;
};
```

## 114.1\_配置成员

| 类型 | 成员 | 含义 |
| --- | --- | --- |
| `const char *` | `name` | 端点名称（Endpoint Name） |
| `int` | `prio` | 端点优先级（Endpoint Priority），仅在后端支持优先级时适用 |
| `struct ipc_service_cb` | `cb` | [事件回调结构（Event Callback Structure）](P112_IPC服务回调结构.md) |
| `void *` | `priv` | 用户私有数据（Private User Data） |

本结构的原页没有规定优先级数值大小与调度顺序的关系；应结合具体后端使用。另见[注册端点接口](P111_IPC服务公共接口.md)对配置变量生命周期的要求，以及[完整头文件](P118_IPC服务完整头文件.md)。

---

[上一章：IPC服务端点结构](P113_IPC服务端点结构.md) · [下一章：IPC服务后端接口](P115_IPC服务后端接口.md) · [返回大纲](大纲.md)
