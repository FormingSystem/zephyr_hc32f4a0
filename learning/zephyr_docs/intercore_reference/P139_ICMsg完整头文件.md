---
id: learning.zephyr-docs.intercore_reference.icmsgref-139
title: ICMsg完整头文件
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/icmsg_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第139章\_ICMsg完整头文件

原文：[icmsg_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/icmsg_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方`zephyr/ipc/icmsg.h`源码浏览页的完整可见代码。ICMsg 是核间消息传递（Inter-core Messaging）库，IPC 指处理器间通信（Inter-Processor Communication）。展示行号已移除，原条件编译、注释、声明和许可证保留。

`CONFIG_IPC_SERVICE_ICMSG_SHMEM_ACCESS_SYNC`与`CONFIG_MULTITHREADING`是 Kconfig 配置项，分别控制下方发送互斥锁和邮箱工作项的条件成员；Kconfig 是 Zephyr 的配置系统。

## 139.1\_完整可见源码

```c
/*
 * Copyright (c) 2022 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_IPC_ICMSG_H_
#define ZEPHYR_INCLUDE_IPC_ICMSG_H_

#include <stddef.h>
#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/drivers/mbox.h>
#include <zephyr/ipc/ipc_service.h>
#include <zephyr/ipc/pbuf.h>
#include <zephyr/sys/atomic.h>

#ifdef __cplusplus
extern "C" {
#endif


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

enum icmsg_unbound_mode {
        ICMSG_UNBOUND_MODE_DISABLE = ICMSG_STATE_INITIALIZING_SID_DISABLED,
        ICMSG_UNBOUND_MODE_ENABLE = ICMSG_STATE_INITIALIZING_SID_ENABLED,
        ICMSG_UNBOUND_MODE_DETECT = ICMSG_STATE_INITIALIZING_SID_DETECT,
};

struct icmsg_config_t {
        struct mbox_dt_spec mbox_tx;
        struct mbox_dt_spec mbox_rx;
        enum icmsg_unbound_mode unbound_mode;
};

struct icmsg_data_t {
        /* Tx/Rx buffers. */
        struct pbuf *tx_pb;
        struct pbuf *rx_pb;
#ifdef CONFIG_IPC_SERVICE_ICMSG_SHMEM_ACCESS_SYNC
        struct k_mutex tx_lock;
#endif

        /* Callbacks for an endpoint. */
        const struct ipc_service_cb *cb;
        void *ctx;

        /* General */
        const struct icmsg_config_t *cfg;
#ifdef CONFIG_MULTITHREADING
        struct k_work mbox_work;
#endif
        uint16_t remote_sid;
        uint16_t local_sid;
        atomic_t state;
};

int icmsg_open(const struct icmsg_config_t *conf,
               struct icmsg_data_t *dev_data,
               const struct ipc_service_cb *cb, void *ctx);

int icmsg_close(const struct icmsg_config_t *conf,
                struct icmsg_data_t *dev_data);

int icmsg_send(const struct icmsg_config_t *conf,
               struct icmsg_data_t *dev_data,
               const void *msg, size_t len);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_IPC_ICMSG_H_ */
```

## 139.2\_可见注释与阅读说明

原文件版权为2022年 Nordic Semiconductor ASA，许可证为 Apache-2.0。头文件保护宏（Header Guard）为`ZEPHYR_INCLUDE_IPC_ICMSG_H_`；`__cplusplus`与`extern "C"`用于保持 C++ 环境下的 C 语言链接方式。

源码保留的英文注释含义如下：

- 已连接状态（Connected States）必须放在枚举末尾。
- 发送／接收缓冲区（TX/RX Buffers）一组包含缓冲区指针及有条件启用的发送锁。
- 端点回调（Callbacks for an Endpoint）一组包含回调结构和上下文。
- 通用数据（General）一组包含配置、条件工作项、会话标识和状态。
- 文件末尾注释标识头文件保护宏结束。

官方 Doxygen 提取到说明页的文档注释见[基础接口](P135_ICMsg基础接口.md)。结构和条件成员说明见[配置结构](P136_ICMsg配置结构.md)与[运行时结构](P137_ICMsg运行时结构.md)。

---

[上一章：ICMsg头文件参考](P138_ICMsg头文件参考.md) · [下一章：ICMsg多端点接口](P140_ICMsg多端点接口.md) · [返回大纲](大纲.md)
