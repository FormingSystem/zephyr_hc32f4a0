---
id: learning.zephyr-docs.intercore_reference.icmsgref-138
title: ICMsg头文件参考
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/icmsg_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第138章\_ICMsg头文件参考

原文：[icmsg_8h](https://docs.zephyrproject.org/latest/doxygen/html/icmsg_8h.html)。读取日期：2026-10-13，`latest`。

本页是 ICMsg 核间消息传递（Inter-core Messaging）库头文件`zephyr/ipc/icmsg.h`的参考索引。

## 138.1\_包含文件


```c
#include <stddef.h>
#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/drivers/mbox.h>
#include <zephyr/ipc/ipc_service.h>
#include <zephyr/ipc/pbuf.h>
#include <zephyr/sys/atomic.h>
```

## 138.2\_结构与枚举

原页列出[配置结构`icmsg_config_t`](P136_ICMsg配置结构.md)和[运行时结构`icmsg_data_t`](P137_ICMsg运行时结构.md)。

实例状态枚举（State Enumeration）`icmsg_state`如下。SID 是会话标识（Session ID），原注释要求已连接状态放在末尾。

```c
enum icmsg_state {
        ICMSG_STATE_OFF,

        ICMSG_STATE_INITIALIZING_SID_DISABLED,

        ICMSG_STATE_INITIALIZING_SID_ENABLED,

        ICMSG_STATE_INITIALIZING_SID_DETECT,

        ICMSG_STATE_DISCONNECTED,

        /* Connected states must be at the end. */

        ICMSG_STATE_CONNECTED_SID_DISABLED,

        ICMSG_STATE_CONNECTED_SID_ENABLED,
};
```

模式名中的`DISABLE`、`ENABLE`、`DETECT`分别表示禁用（Disable）、启用（Enable）和检测（Detect）；它们的赋值对应初始化状态。

解绑模式枚举（Unbound Mode Enumeration）如下：

```c
enum icmsg_unbound_mode {
        ICMSG_UNBOUND_MODE_DISABLE = ICMSG_STATE_INITIALIZING_SID_DISABLED,
        ICMSG_UNBOUND_MODE_ENABLE = ICMSG_STATE_INITIALIZING_SID_ENABLED,
        ICMSG_UNBOUND_MODE_DETECT = ICMSG_STATE_INITIALIZING_SID_DETECT,
};
```

## 138.3\_函数声明

打开实例。

```c
int icmsg_open(const struct icmsg_config_t *conf,
               struct icmsg_data_t *dev_data,
               const struct ipc_service_cb *cb, void *ctx);
```

关闭实例。

```c
int icmsg_close(const struct icmsg_config_t *conf,
                struct icmsg_data_t *dev_data);
```

向远端实例发送消息。

```c
int icmsg_send(const struct icmsg_config_t *conf,
               struct icmsg_data_t *dev_data,
               const void *msg, size_t len);
```

状态含义、阻塞握手、参数与返回值详见[基础接口](P135_ICMsg基础接口.md)，完整可见代码见[头文件源码](P139_ICMsg完整头文件.md)。

---

[上一章：ICMsg运行时结构](P137_ICMsg运行时结构.md) · [下一章：ICMsg完整头文件](P139_ICMsg完整头文件.md) · [返回大纲](大纲.md)
