---
id: learning.zephyr-docs.intercore_reference.zbusproxyref-202
title: zbus代理IPC配置结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzbus__proxy__agent__ipc__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第202章\_zbus代理IPC配置结构

原文：[structzbus__proxy__agent__ipc__config](https://docs.zephyrproject.org/latest/doxygen/html/structzbus__proxy__agent__ipc__config.html)。读取日期：2026-10-13，`latest`。

`zbus_proxy_agent_ipc_config`表示zbus 代理（Proxy Agent）的处理器间通信（Inter-Processor Communication，IPC）后端配置。来自头文件`zephyr/zbus/proxy_agent/zbus_proxy_agent_ipc.h`。

## 202.1\_结构声明

```c
struct zbus_proxy_agent_ipc_config {
        const struct device *dev;
        const char *ept_name;
        struct zbus_proxy_agent_ipc_data *data;
};
```

## 202.2\_成员说明

| 成员 | 类型 | 含义 |
| --- | --- | --- |
| `dev` | `const struct device *` | IPC 设备（Device） |
| `ept_name` | `const char *` | IPC 端点（Endpoint）名称 |
| `data` | `struct zbus_proxy_agent_ipc_data *` | 指向可变 IPC 后端运行时数据（Mutable Runtime Data）的指针 |

可变数据的六个成员见[zbus代理IPC运行时结构](P203_zbus代理IPC运行时结构.md)。

完整原始头文件见[zbus代理IPC完整头文件](P205_zbus代理IPC完整头文件.md)。

---

[上一章：zbus代理IPC后端接口](P201_zbus代理IPC后端接口.md) · [下一章：zbus代理IPC运行时结构](P203_zbus代理IPC运行时结构.md) · [返回大纲](大纲.md)
