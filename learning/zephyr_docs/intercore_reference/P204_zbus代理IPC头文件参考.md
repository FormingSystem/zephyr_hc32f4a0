---
id: learning.zephyr-docs.intercore_reference.zbusproxyref-204
title: zbus代理IPC头文件参考
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/zbus__proxy__agent__ipc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第204章\_zbus代理IPC头文件参考

原文：[zbus__proxy__agent__ipc_8h](https://docs.zephyrproject.org/latest/doxygen/html/zbus__proxy__agent__ipc_8h.html)。读取日期：2026-10-13，`latest`。

本页是 zbus 多域应用程序编程接口（Multi-domain Application Programming Interface，API）的头文件参考（Header Reference），对应`zephyr/zbus/proxy_agent/zbus_proxy_agent_ipc.h`。IPC 表示处理器间通信（Inter-Processor Communication）。

## 204.1\_依赖头文件

```c
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/ipc/ipc_service.h>
#include <zephyr/zbus/proxy_agent/zbus_proxy_agent.h>
#include <zephyr/sys/util.h>
```

## 204.2\_数据结构

| 结构 | 说明 |
| --- | --- |
| [zbus代理IPC运行时结构](P203_zbus代理IPC运行时结构.md) | zbus 代理（Proxy Agent）IPC 后端的可变运行时数据（Mutable Runtime Data） |
| [zbus代理IPC配置结构](P202_zbus代理IPC配置结构.md) | zbus 代理 IPC 后端的配置结构 |

后端的固定帧传输限制见[zbus代理IPC后端接口](P201_zbus代理IPC后端接口.md)；完整可见源码见[zbus代理IPC完整头文件](P205_zbus代理IPC完整头文件.md)。

---

[上一章：zbus代理IPC运行时结构](P203_zbus代理IPC运行时结构.md) · [下一章：zbus代理IPC完整头文件](P205_zbus代理IPC完整头文件.md) · [返回大纲](大纲.md)
