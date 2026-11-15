---
id: learning.zephyr-docs.intercore_reference.zbusproxyref-203
title: zbus代理IPC运行时结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzbus__proxy__agent__ipc__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第203章\_zbus代理IPC运行时结构

原文：[structzbus__proxy__agent__ipc__data](https://docs.zephyrproject.org/latest/doxygen/html/structzbus__proxy__agent__ipc__data.html)。读取日期：2026-10-13，`latest`。

结构体`zbus_proxy_agent_ipc_data`表示zbus 代理（Proxy Agent）的处理器间通信（Inter-Processor Communication，IPC）后端的可变运行时数据（Mutable Runtime Data）。来自头文件`zephyr/zbus/proxy_agent/zbus_proxy_agent_ipc.h`。

## 203.1\_结构声明

```c
struct zbus_proxy_agent_ipc_data {
        struct ipc_ept ipc_ept;
        struct ipc_ept_cfg ept_cfg;
        struct k_sem ept_bound_sem;
        zbus_proxy_agent_recv_cb_t recv_cb;
        const struct zbus_proxy_agent *recv_cb_config_ptr;
        uint8_t initialized;
};
```

## 203.2\_成员说明

| 成员 | 类型 | 含义 |
| --- | --- | --- |
| `ipc_ept` | `struct ipc_ept` | IPC 端点（Endpoint） |
| `ept_cfg` | `struct ipc_ept_cfg` | IPC 端点配置 |
| `ept_bound_sem` | `struct k_sem` | 在 IPC 端点已绑定（Bound）时发出信号的信号量（Semaphore） |
| `recv_cb` | `zbus_proxy_agent_recv_cb_t` | 接收数据使用的回调函数（Callback Function） |
| `recv_cb_config_ptr` | `const struct zbus_proxy_agent *` | 代理配置指针，作为接收回调的用户数据（User Data） |
| `initialized` | `uint8_t` | 后端初始化成功完成后为1，否则为0 |

配置结构见[zbus代理IPC配置结构](P202_zbus代理IPC配置结构.md)，接收回调类型见[zbus代理接口](P193_zbus代理接口.md)。

完整原始头文件见[zbus代理IPC完整头文件](P205_zbus代理IPC完整头文件.md)。

---

[上一章：zbus代理IPC配置结构](P202_zbus代理IPC配置结构.md) · [下一章：zbus代理IPC头文件参考](P204_zbus代理IPC头文件参考.md) · [返回大纲](大纲.md)
