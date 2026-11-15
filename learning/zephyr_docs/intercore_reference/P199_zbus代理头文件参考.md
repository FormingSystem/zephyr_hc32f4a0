---
id: learning.zephyr-docs.intercore_reference.zbusproxyref-199
title: zbus代理头文件参考
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/zbus__proxy__agent_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第199章\_zbus代理头文件参考

原文：[zbus__proxy__agent_8h](https://docs.zephyrproject.org/latest/doxygen/html/zbus__proxy__agent_8h.html)。读取日期：2026-10-13，`latest`。

本页是 zbus 多域应用程序编程接口（Multi-domain Application Programming Interface，API）的头文件参考（Header Reference），对应`zephyr/zbus/proxy_agent/zbus_proxy_agent.h`。

## 199.1\_依赖头文件

```c
#include <zephyr/kernel.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/zbus/zbus.h>
```

## 199.2\_数据结构

| 结构 | 说明 |
| --- | --- |
| [zbus影子通道结构](P198_zbus影子通道结构.md) | 影子通道（Shadow Channel）的元数据（Metadata），用于跟踪它所属的代理（Proxy Agent） |
| [zbus代理消息布局](P197_zbus代理消息布局.md) | 代理消息（Proxy Agent Message）的结构 |
| [zbus代理接收消息结构](P196_zbus代理接收消息结构.md) | 已验证接收消息的内部线程载荷（Internal Thread Payload） |
| [zbus代理结构](P194_zbus代理结构.md) | 代理（Proxy Agent）实例及其关联配置 |
| [zbus代理后端接口结构](P195_zbus代理后端接口结构.md) | 代理后端（Proxy Agent Backend）的应用程序编程接口（Application Programming Interface，API） |

## 199.3\_宏定义

| 宏 | 用途 |
| --- | --- |
| `ZBUS_PROXY_AGENT_DEFINE(_name, _type, _backend_dt_node)` | 定义代理（Proxy Agent） |
| `ZBUS_PROXY_ADD_CHAN(_agent, _chan)` | 添加需要代理转发的通道（Channel） |
| `ZBUS_SHADOW_CHAN_DEFINE(_name, _type, _proxy_name, _user_data, _observers, _init_val)` | 定义与代理关联的影子通道（Shadow Channel） |
| `ZBUS_SHADOW_CHAN_DEFINE_WITH_ID(_name, _id, _type, _proxy_name, _user_data, _observers, _init_val)` | 定义具有指定标识（ID）、并与代理关联的影子通道 |

## 199.4\_类型与枚举

```c
typedef int (*zbus_proxy_agent_recv_cb_t)(const struct zbus_proxy_agent *agent,
                                          const struct zbus_proxy_msg *msg);
```

`zbus_proxy_agent_recv_cb_t`是代理接收回调（Receive Callback）类型。

`enum zbus_proxy_agent_backend_type`表示支持的后端类型，原页仅列出`ZBUS_PROXY_AGENT_BACKEND_IPC`。

## 199.5\_函数接口

```c
void zbus_proxy_agent_listener_cb(const struct zbus_channel *chan,
                                  const struct zbus_proxy_agent *agent);
```

内部代理监听器回调（Listener Callback）。

```c
int zbus_init_proxy_agent(const struct zbus_proxy_agent *agent);
```

原简介为“内部代理接收回调”。译注：对应详细文档实际说明此函数初始化代理，简介与用途的差异见[zbus代理接口](P193_zbus代理接口.md)。

宏、参数、返回值与内部调用限制见[zbus代理接口](P193_zbus代理接口.md)；完整可见源码见[zbus代理完整头文件](P200_zbus代理完整头文件.md)。

---

[上一章：zbus影子通道结构](P198_zbus影子通道结构.md) · [下一章：zbus代理完整头文件](P200_zbus代理完整头文件.md) · [返回大纲](大纲.md)
