---
id: learning.zephyr-docs.intercore_reference.zbusproxyref-200
title: zbus代理完整头文件
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/zbus__proxy__agent_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第200章\_zbus代理完整头文件

原文：[zbus__proxy__agent_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/zbus__proxy__agent_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留`zephyr/zbus/proxy_agent/zbus_proxy_agent.h`完整官方可见源码（Source Code），仅去除网页行号和行尾空白。版权为2026年的 Nordic Semiconductor ASA；`Apache-2.0`许可证（License）标识及原始声明完整保留。

zbus 是消息总线（Message Bus）；Proxy Agent 为代理，Backend 为后端，Shadow Channel 为影子通道，IPC 为处理器间通信（Inter-Processor Communication），API 为应用程序编程接口（Application Programming Interface）。`CONFIG_`开头的宏来自 Kconfig 构建配置系统（Build Configuration System）。

`ZBUS_PROXY_AGENT_BACKEND_IPC`是 IPC 后端枚举项。`ZBUS_PROXY_AGENT_DEFINE`定义代理；`ZBUS_PROXY_ADD_CHAN`添加转发通道；`ZBUS_SHADOW_CHAN_DEFINE`和`ZBUS_SHADOW_CHAN_DEFINE_WITH_ID`定义影子通道，后者同时指定通道标识。

源码用到的基础宏包括：定义线程栈的`K_THREAD_STACK_DEFINE`、定义静态消息队列的`K_MSGQ_DEFINE_STATIC_TYPE`、定义监听器的`ZBUS_LISTENER_DEFINE`、添加通道观察者的`ZBUS_CHAN_ADD_OBS`、注册可迭代段对象的`STRUCT_SECTION_ITERABLE`，以及定义普通通道／带标识通道的`ZBUS_CHAN_DEFINE`和`ZBUS_CHAN_DEFINE_WITH_ID`。`SYS_INIT`是系统初始化注册宏，`APPLICATION`是其应用初始化级别。

五个 Kconfig 配置宏分别是：消息缓冲区容量`CONFIG_ZBUS_PROXY_AGENT_MAX_MESSAGE_SIZE`、通道名缓冲区容量`CONFIG_ZBUS_PROXY_AGENT_MAX_CHANNEL_NAME_SIZE`、专用线程栈大小`CONFIG_ZBUS_PROXY_AGENT_WORK_QUEUE_STACK_SIZE`、接收队列深度`CONFIG_ZBUS_PROXY_AGENT_RX_QUEUE_DEPTH`以及初始化优先级`CONFIG_ZBUS_PROXY_AGENT_INIT_PRIORITY`。

## 200.1\_完整源码

```c
/*
 * Copyright (c) 2026 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_ZBUS_PROXY_AGENT_ZBUS_PROXY_AGENT_H_
#define ZEPHYR_INCLUDE_ZBUS_PROXY_AGENT_ZBUS_PROXY_AGENT_H_

#include <zephyr/kernel.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/zbus/zbus.h>

#ifdef __cplusplus
extern "C" {
#endif


/* Forward declarations */
struct zbus_proxy_agent_backend_api;
struct zbus_proxy_agent;

enum zbus_proxy_agent_backend_type {
        ZBUS_PROXY_AGENT_BACKEND_IPC,
};

struct zbus_shadow_channel {
        const struct zbus_channel *chan;
        const struct zbus_proxy_agent *proxy_agent;
};

struct zbus_proxy_msg {
        uint32_t message_size;
        uint8_t message[CONFIG_ZBUS_PROXY_AGENT_MAX_MESSAGE_SIZE];
        uint32_t channel_name_len;
        char channel_name[CONFIG_ZBUS_PROXY_AGENT_MAX_CHANNEL_NAME_SIZE];
};

struct zbus_proxy_agent_rx_msg {
        const struct zbus_channel *chan;
        uint8_t message[CONFIG_ZBUS_PROXY_AGENT_MAX_MESSAGE_SIZE];
};

struct zbus_proxy_agent {
        const char *name;
        const void *backend_config;
        const struct zbus_proxy_agent_backend_api *backend_api;
        struct k_thread *thread;
        struct k_msgq *msgq;
        k_thread_stack_t *stack;
        k_tid_t *const thread_id;
};

typedef int (*zbus_proxy_agent_recv_cb_t)(const struct zbus_proxy_agent *agent,
                                          const struct zbus_proxy_msg *msg);

struct zbus_proxy_agent_backend_api {
        int (*backend_init)(const struct zbus_proxy_agent *agent);
        int (*backend_send)(const struct zbus_proxy_agent *agent, struct zbus_proxy_msg *msg);
        int (*backend_set_recv_cb)(const struct zbus_proxy_agent *agent,
                                   zbus_proxy_agent_recv_cb_t recv_cb);
};

void zbus_proxy_agent_listener_cb(const struct zbus_channel *chan,
                                  const struct zbus_proxy_agent *agent);

int zbus_init_proxy_agent(const struct zbus_proxy_agent *agent);

#define ZBUS_PROXY_AGENT_DEFINE(_name, _type, _backend_dt_node)                                    \
        _ZBUS_PROXY_AGENT_BACKEND_CONFIG_DEFINE(_name, _type, _backend_dt_node)                    \
        K_THREAD_STACK_DEFINE(_name##_thread_stack,                                                \
                              CONFIG_ZBUS_PROXY_AGENT_WORK_QUEUE_STACK_SIZE);                      \
        K_MSGQ_DEFINE_STATIC_TYPE(_name##_rx_msgq, struct zbus_proxy_agent_rx_msg,                 \
                                  CONFIG_ZBUS_PROXY_AGENT_RX_QUEUE_DEPTH);                         \
        static struct k_thread _name##_thread;                                                     \
        static k_tid_t _name##_thread_id;                                                          \
        const struct zbus_proxy_agent _name = {                                                    \
                .name = #_name,                                                                    \
                .backend_config = _ZBUS_PROXY_AGENT_GET_BACKEND_CONFIG(_name, _type),              \
                .backend_api = _ZBUS_PROXY_AGENT_GET_BACKEND_API(_type),                           \
                .thread = &_name##_thread,                                                         \
                .msgq = &_name##_rx_msgq,                                                          \
                .stack = _name##_thread_stack,                                                     \
                .thread_id = &_name##_thread_id,                                                   \
        };                                                                                         \
        static void _name##_zbus_listener_cb(const struct zbus_channel *chan)                      \
        {                                                                                          \
                zbus_proxy_agent_listener_cb(chan, &_name);                                        \
        }                                                                                          \
        ZBUS_LISTENER_DEFINE(_name##_listener, _name##_zbus_listener_cb);                          \
        _ZBUS_PROXY_AGENT_GENERATE_SHADOW_VALIDATOR(_name);                                        \
        static int _name##_init(void)                                                              \
        {                                                                                          \
                return zbus_init_proxy_agent(&_name);                                              \
        }                                                                                          \
        SYS_INIT(_name##_init, APPLICATION, CONFIG_ZBUS_PROXY_AGENT_INIT_PRIORITY)


#define _ZBUS_PROXY_AGENT_BACKEND_CONFIG_DEFINE(_name, _type, _backend_dt_node)                    \
        _ZBUS_PROXY_AGENT_BACKEND_CONFIG_DEFINE_##_type(_name, _backend_dt_node)

#define _ZBUS_PROXY_AGENT_GET_BACKEND_CONFIG(_name, _type)                                         \
        _ZBUS_PROXY_AGENT_GET_BACKEND_CONFIG_##_type(_name)

#define _ZBUS_PROXY_AGENT_GET_BACKEND_API(_type) _ZBUS_PROXY_AGENT_GET_BACKEND_API_##_type

void zbus_proxy_agent_log_shadow_pub_denied(const struct zbus_proxy_agent *agent);

#define _ZBUS_PROXY_AGENT_VALIDATOR(_proxy_name) _proxy_name##_shadow_validator

#define _ZBUS_PROXY_AGENT_GENERATE_SHADOW_VALIDATOR(_proxy_name)                                   \
        bool _proxy_name##_shadow_validator(const void *msg, size_t msg_size)                      \
        {                                                                                          \
                (void)msg;                                                                         \
                (void)msg_size;                                                                    \
                /* Only allow publishing from the proxy agent's dedicated thread */                \
                if (k_current_get() != *_proxy_name.thread_id) {                                   \
                        zbus_proxy_agent_log_shadow_pub_denied(&_proxy_name);                      \
                        return false;                                                              \
                }                                                                                  \
                return true;                                                                       \
        }


#define ZBUS_PROXY_ADD_CHAN(_agent, _chan)                                                         \
        ZBUS_CHAN_ADD_OBS(_chan, _agent##_listener, zz)


#define _ZBUS_SHADOW_CHAN_REGISTER(_name, _proxy_name)                                             \
        extern const struct zbus_proxy_agent _proxy_name;                                          \
        static const STRUCT_SECTION_ITERABLE(zbus_shadow_channel,                                  \
                                             _CONCAT(_zbus_shadow_chan_, _name)) = {               \
                .chan = &_name,                                                                    \
                .proxy_agent = &_proxy_name,                                                       \
        }


#define ZBUS_SHADOW_CHAN_DEFINE(_name, _type, _proxy_name, _user_data, _observers, _init_val)      \
        ZBUS_CHAN_DEFINE(_name, _type, _ZBUS_PROXY_AGENT_VALIDATOR(_proxy_name), _user_data,       \
                         _observers, _init_val);                                                   \
        _ZBUS_SHADOW_CHAN_REGISTER(_name, _proxy_name)

#define ZBUS_SHADOW_CHAN_DEFINE_WITH_ID(_name, _id, _type, _proxy_name, _user_data, _observers,    \
                                        _init_val)                                                 \
        ZBUS_CHAN_DEFINE_WITH_ID(_name, _id, _type, _ZBUS_PROXY_AGENT_VALIDATOR(_proxy_name),      \
                                 _user_data, _observers, _init_val);                               \
        _ZBUS_SHADOW_CHAN_REGISTER(_name, _proxy_name)


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_ZBUS_PROXY_AGENT_ZBUS_PROXY_AGENT_H_ */
```

## 200.2\_可见注释与宏的阅读说明

`Forward declarations`表示前置声明。

`Only allow publishing from the proxy agent's dedicated thread`表示：**只允许从代理的专用线程发布**。对应验证器（Validator）比较`k_current_get()`与代理保存的线程标识（Thread ID）；不一致时调用拒绝发布的日志函数并返回`false`，一致时返回`true`。

`ZBUS_PROXY_AGENT_DEFINE`定义后端配置、线程栈（Thread Stack）、接收消息队列（Receive Message Queue）、线程对象与代理配置，并生成监听器（Listener）、影子通道验证器和初始化函数。`SYS_INIT`在`APPLICATION`级别按`CONFIG_ZBUS_PROXY_AGENT_INIT_PRIORITY`注册初始化函数。栈大小使用`CONFIG_ZBUS_PROXY_AGENT_WORK_QUEUE_STACK_SIZE`，接收队列深度使用`CONFIG_ZBUS_PROXY_AGENT_RX_QUEUE_DEPTH`。

三个后端分派宏`_ZBUS_PROXY_AGENT_BACKEND_CONFIG_DEFINE``_ZBUS_PROXY_AGENT_GET_BACKEND_CONFIG``_ZBUS_PROXY_AGENT_GET_BACKEND_API`根据后端类型拼接对应实现；`##`表示记号拼接（Token Pasting），`#`用于字符串化（Stringification）。

`_ZBUS_SHADOW_CHAN_REGISTER`在可迭代段（Iterable Section）中保存通道及其所属代理的对应关系。两个影子通道定义宏均关联专用验证器。

`__cplusplus`分支提供 C++ 的 C 语言链接约定；文件末尾注释标明头文件保护宏（Header Guard）的结束。

## 200.3\_配套说明

网页隐藏的 Doxygen 文档注释没有补写进原代码；相应说明已经翻译到[zbus代理接口](P193_zbus代理接口.md)。五个结构的成员详见[zbus代理结构](P194_zbus代理结构.md)、[zbus代理后端接口结构](P195_zbus代理后端接口结构.md)、[zbus代理接收消息结构](P196_zbus代理接收消息结构.md)、[zbus代理消息布局](P197_zbus代理消息布局.md)、[zbus影子通道结构](P198_zbus影子通道结构.md)。IPC 后端源码见[zbus代理IPC完整头文件](P205_zbus代理IPC完整头文件.md)。

---

[上一章：zbus代理头文件参考](P199_zbus代理头文件参考.md) · [下一章：zbus代理IPC后端接口](P201_zbus代理IPC后端接口.md) · [返回大纲](大纲.md)
