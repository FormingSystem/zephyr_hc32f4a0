---
id: learning.zephyr-docs.intercore_reference.zbusproxyref-205
title: zbus代理IPC完整头文件
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/zbus__proxy__agent__ipc_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第205章\_zbus代理IPC完整头文件

原文：[zbus__proxy__agent__ipc_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/zbus__proxy__agent__ipc_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留`zephyr/zbus/proxy_agent/zbus_proxy_agent_ipc.h`完整官方可见源码（Source Code），仅去除网页行号和行尾空白。版权为2026年的 Nordic Semiconductor ASA；`Apache-2.0`许可证（License）标识及原始声明完整保留。

zbus 为消息总线（Message Bus），Proxy Agent 为代理，IPC 为处理器间通信（Inter-Processor Communication），Backend 为后端，API 为应用程序编程接口（Application Programming Interface），Endpoint 为端点。

`DEVICE_DT_GET`是从设备树（Devicetree）节点取得设备对象的宏。

## 205.1\_完整源码

```c
/*
 * Copyright (c) 2026 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_ZBUS_PROXY_AGENT_ZBUS_PROXY_AGENT_IPC_H_
#define ZEPHYR_INCLUDE_ZBUS_PROXY_AGENT_ZBUS_PROXY_AGENT_IPC_H_

#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/ipc/ipc_service.h>
#include <zephyr/zbus/proxy_agent/zbus_proxy_agent.h>
#include <zephyr/sys/util.h>

#ifdef __cplusplus
extern "C" {
#endif


struct zbus_proxy_agent_ipc_data {
        struct ipc_ept ipc_ept;
        struct ipc_ept_cfg ept_cfg;
        struct k_sem ept_bound_sem;
        zbus_proxy_agent_recv_cb_t recv_cb;
        const struct zbus_proxy_agent *recv_cb_config_ptr;
        uint8_t initialized;
};

struct zbus_proxy_agent_ipc_config {
        const struct device *dev;
        const char *ept_name;
        struct zbus_proxy_agent_ipc_data *data;
};


#define _ZBUS_PROXY_AGENT_BACKEND_CONFIG_DEFINE_ZBUS_PROXY_AGENT_BACKEND_IPC(_name,                \
                                                                             _backend_dt_node)     \
        static struct zbus_proxy_agent_ipc_data _name##_ipc_data = {                               \
                .ept_cfg = {                                                                       \
                        .name = #_name "_ipc_ept",                                                 \
                },                                                                                 \
        };                                                                                         \
        static const struct zbus_proxy_agent_ipc_config _name##_ipc_config = {                     \
                .dev = DEVICE_DT_GET(_backend_dt_node),                                            \
                .ept_name = #_name "_ipc_ept",                                                     \
                .data = &_name##_ipc_data,                                                         \
        };

#define _ZBUS_PROXY_AGENT_GET_BACKEND_CONFIG_ZBUS_PROXY_AGENT_BACKEND_IPC(_name)                   \
        (&_name##_ipc_config)

/* Forward declaration of the IPC backend API */
extern const struct zbus_proxy_agent_backend_api zbus_proxy_agent_ipc_backend_api;

#define _ZBUS_PROXY_AGENT_GET_BACKEND_API_ZBUS_PROXY_AGENT_BACKEND_IPC                             \
        (&zbus_proxy_agent_ipc_backend_api)



#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_ZBUS_PROXY_AGENT_ZBUS_PROXY_AGENT_IPC_H_ */
```

## 205.2\_可见注释与宏的阅读说明

`Forward declaration of the IPC backend API`表示 IPC 后端接口的前置声明；对应对象是`zbus_proxy_agent_ipc_backend_api`。

`_ZBUS_PROXY_AGENT_BACKEND_CONFIG_DEFINE_ZBUS_PROXY_AGENT_BACKEND_IPC`创建可变运行时数据和只读配置，端点名称由代理名字符串加上`_ipc_ept`组成，设备对象通过`DEVICE_DT_GET(_backend_dt_node)`取得。

`_ZBUS_PROXY_AGENT_GET_BACKEND_CONFIG_ZBUS_PROXY_AGENT_BACKEND_IPC`返回该代理的 IPC 配置地址；`_ZBUS_PROXY_AGENT_GET_BACKEND_API_ZBUS_PROXY_AGENT_BACKEND_IPC`返回 IPC 后端接口地址。`##`用于记号拼接（Token Pasting），`#`用于字符串化（Stringification）。

`__cplusplus`分支提供 C++ 的 C 语言链接约定；文件末尾注释标记头文件保护宏（Header Guard）结束。

## 205.3\_配套说明

运行时结构的六个成员见[zbus代理IPC运行时结构](P203_zbus代理IPC运行时结构.md)；配置结构的三个成员见[zbus代理IPC配置结构](P202_zbus代理IPC配置结构.md)。网页隐藏的 Doxygen 注释对应的后端契约已在[zbus代理IPC后端接口](P201_zbus代理IPC后端接口.md)译出。

---

[上一章：zbus代理IPC头文件参考](P204_zbus代理IPC头文件参考.md) · [下一章：zbus通道结构](P206_zbus通道结构.md) · [返回大纲](大纲.md)
