---
id: learning.zephyr-docs.intercore_reference.zbusproxyref-194
title: zbus代理结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzbus__proxy__agent.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第194章\_zbus代理结构

原文：[structzbus__proxy__agent](https://docs.zephyrproject.org/latest/doxygen/html/structzbus__proxy__agent.html)。读取日期：2026-10-13，`latest`。

`zbus_proxy_agent`表示代理（Proxy Agent）实例及其关联配置。来自头文件`zephyr/zbus/proxy_agent/zbus_proxy_agent.h`。

## 194.1\_结构声明

```c
struct zbus_proxy_agent {
        const char *name;
        const void *backend_config;
        const struct zbus_proxy_agent_backend_api *backend_api;
        struct k_thread *thread;
        struct k_msgq *msgq;
        k_thread_stack_t *stack;
        k_tid_t *const thread_id;
};
```

## 194.2\_成员说明

| 成员 | 类型 | 含义 |
| --- | --- | --- |
| `name` | `const char *` | 代理名称 |
| `backend_config` | `const void *` | 后端专用配置（Backend-specific Configuration） |
| `backend_api` | `const struct zbus_proxy_agent_backend_api *` | 编译期（Compile Time）按后端类型确定的应用程序编程接口（Application Programming Interface，API） |
| `thread` | `struct k_thread *` | 处理收到的代理消息的专用线程（Dedicated Thread） |
| `msgq` | `struct k_msgq *` | 收到的代理消息使用的消息队列（Message Queue） |
| `stack` | `k_thread_stack_t *` | 代理专用线程使用的栈（Stack） |
| `thread_id` | `k_tid_t *const` | 指向代理专用线程标识（Thread ID）的指针 |

后端函数表见[zbus代理后端接口结构](P195_zbus代理后端接口结构.md)，内部接收消息见[zbus代理接收消息结构](P196_zbus代理接收消息结构.md)。

完整原始头文件见[zbus代理完整头文件](P200_zbus代理完整头文件.md)。

---

[上一章：zbus代理接口](P193_zbus代理接口.md) · [下一章：zbus代理后端接口结构](P195_zbus代理后端接口结构.md) · [返回大纲](大纲.md)
