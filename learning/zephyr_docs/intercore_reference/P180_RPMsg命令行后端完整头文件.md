---
id: learning.zephyr-docs.intercore_reference.ipchostref-180
title: RPMsg命令行后端完整头文件
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__rpmsg_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第180章\_RPMsg命令行后端完整头文件

原文：[shell__rpmsg_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/shell__rpmsg_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留`zephyr/shell/shell_rpmsg.h`完整官方可见源码（Source Code），仅去除网页行号及行尾空白。RPMsg 是远程消息传递（Remote Processor Messaging），Shell 为命令行。版权为2024年的 Basalte bv，许可证为`Apache-2.0`，原声明完整保留。

`CONFIG_SHELL_RPMSG_MAX_RX`是 Kconfig 构建配置系统（Build Configuration System）提供的配置宏，决定接收项数组长度。RX 表示接收（Receive）。

## 180.1\_完整源码

```c
/*
 * Copyright (c) 2024 Basalte bv
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_SHELL_SHELL_RPMSG_H_
#define ZEPHYR_INCLUDE_SHELL_SHELL_RPMSG_H_

#include <zephyr/kernel.h>
#include <zephyr/shell/shell.h>
#include <openamp/rpmsg.h>

#ifdef __cplusplus
extern "C" {
#endif

extern const struct shell_transport_api shell_rpmsg_transport_api;

struct shell_rpmsg_rx {
        void *data;
        size_t len;
};

struct shell_rpmsg {
        shell_transport_handler_t shell_handler;

        void *shell_context;

        bool ready;

        bool blocking;

        struct rpmsg_endpoint ept;

        struct k_msgq rx_q;

        struct shell_rpmsg_rx rx_buf[CONFIG_SHELL_RPMSG_MAX_RX];

        struct shell_rpmsg_rx rx_cur;

        size_t rx_consumed;
};


#define SHELL_RPMSG_DEFINE(_name)                                       \
        static struct shell_rpmsg _name##_shell_rpmsg;                  \
        struct shell_transport _name = {                                \
                .api = &shell_rpmsg_transport_api,                      \
                .ctx = (struct shell_rpmsg *)&_name##_shell_rpmsg,      \
        }

int shell_backend_rpmsg_init_transport(struct rpmsg_device *rpmsg_dev);

const struct shell *shell_backend_rpmsg_get_ptr(void);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_SHELL_SHELL_RPMSG_H_ */
```

## 180.2\_可见结构阅读说明

网页可见源码的成员说明注释被折叠，以下根据名称与类型提供阅读定位，不冒充原文逐字段契约。

`shell_rpmsg_rx`包含`void *data`数据指针和`size_t len`长度成员。主上下文`shell_rpmsg`包含以下九个成员：

| 成员声明 | 阅读说明 |
| --- | --- |
| `shell_transport_handler_t shell_handler` | 命令行传输处理函数类型的成员 |
| `void *shell_context` | 命令行上下文（Context）指针 |
| `bool ready` | 就绪（Ready）状态成员 |
| `bool blocking` | 阻塞（Blocking）状态成员 |
| `struct rpmsg_endpoint ept` | RPMsg 端点（Endpoint） |
| `struct k_msgq rx_q` | 接收消息队列（Receive Message Queue） |
| `struct shell_rpmsg_rx rx_buf[CONFIG_SHELL_RPMSG_MAX_RX]` | 按配置确定长度的接收项数组 |
| `struct shell_rpmsg_rx rx_cur` | 当前接收项（Current Receive Item） |
| `size_t rx_consumed` | 与接收消费进度有关的成员；原可见源码没有给出单位 |

`shell_rpmsg_transport_api`是以`extern const struct shell_transport_api`声明的外部传输接口对象。`SHELL_RPMSG_DEFINE`用它初始化传输实例，其完整展开与两个函数说明见[RPMsg命令行后端接口](P178_RPMsg命令行后端接口.md)。

`__cplusplus`分支提供 C++ 的 C 语言链接约定，文件末尾注释标记头文件保护宏`ZEPHYR_INCLUDE_SHELL_SHELL_RPMSG_H_`结束。其余可见自然语言仅为版权与许可证声明，已经保留。

---

[上一章：RPMsg命令行后端头文件参考](P179_RPMsg命令行后端头文件参考.md) · [下一章：IPC接口总览](P181_IPC接口总览.md) · [返回大纲](大纲.md)
