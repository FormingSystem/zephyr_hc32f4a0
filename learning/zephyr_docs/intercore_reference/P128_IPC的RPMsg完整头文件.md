---
id: learning.zephyr-docs.intercore_reference.rpmsgref-128
title: IPC的RPMsg完整头文件
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ipc__rpmsg_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第128章\_IPC的RPMsg完整头文件

原文：[ipc__rpmsg_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/ipc__rpmsg_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览页中`zephyr/ipc/ipc_rpmsg.h`的完整可见代码，用于IPC 的 RPMsg 公共层。RPMsg 为远程处理器消息传递（Remote Processor Messaging），IPC 为处理器间通信（Inter-Processor Communication）。展示行号已移除，声明、版权和许可证均保留。

阅读提示：`NUM_ENDPOINTS`为端点数量宏，取值来自 Kconfig 配置项`CONFIG_IPC_SERVICE_BACKEND_RPMSG_NUM_ENDPOINTS_PER_INSTANCE`；`RPMSG_NAME_SIZE`是端点名称数组长度常量。Kconfig 是 Zephyr 的配置系统。

## 128.1\_完整可见源码

```c
/*
 * Copyright (c) 2021 Carlo Caione <ccaione@baylibre.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_IPC_IPC_RPMSG_H_
#define ZEPHYR_INCLUDE_IPC_IPC_RPMSG_H_

#include <zephyr/ipc/ipc_service.h>
#include <openamp/open_amp.h>
#include <metal/device.h>

#ifdef __cplusplus
extern "C" {
#endif


#define NUM_ENDPOINTS   CONFIG_IPC_SERVICE_BACKEND_RPMSG_NUM_ENDPOINTS_PER_INSTANCE

struct ipc_rpmsg_ept;

typedef void (*rpmsg_ept_bound_cb)(struct ipc_rpmsg_ept *ept);

struct ipc_rpmsg_ept {
        struct rpmsg_endpoint ep;

        char name[RPMSG_NAME_SIZE];

        uint32_t dest;

        volatile bool bound;

        const struct ipc_service_cb *cb;

        void *priv;
};

struct ipc_rpmsg_instance {
        struct ipc_rpmsg_ept endpoint[NUM_ENDPOINTS];

        struct rpmsg_virtio_device rvdev;

        struct rpmsg_virtio_shm_pool shm_pool;

        rpmsg_ept_bound_cb bound_cb;

        rpmsg_ept_cb cb;

        struct k_mutex mtx;
};

int ipc_rpmsg_init(struct ipc_rpmsg_instance *instance,
                   unsigned int role,
                   unsigned int buffer_size,
                   struct metal_io_region *shm_io,
                   struct virtio_device *vdev,
                   void *shb, size_t size,
                   rpmsg_ns_bind_cb ns_bind_cb);


int ipc_rpmsg_deinit(struct ipc_rpmsg_instance *instance,
                   unsigned int role);

int ipc_rpmsg_register_ept(struct ipc_rpmsg_instance *instance, unsigned int role,
                           struct ipc_rpmsg_ept *ept);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_IPC_IPC_RPMSG_H_ */
```

## 128.2\_源码说明与对应译文

原文件版权为2021年 Carlo Caione，许可证为 Apache-2.0。头文件保护宏（Header Guard）为`ZEPHYR_INCLUDE_IPC_IPC_RPMSG_H_`；文件末尾注释标识该保护宏的结束。
`__cplusplus`条件分支和`extern "C"`用于保持 C++ 环境下的 C 语言链接方式。官方 Doxygen 源码浏览页把文档注释提取到说明页，相关中文译文见[公共层接口](P124_IPC的RPMsg公共层接口.md)、[端点结构](P125_IPC的RPMsg端点结构.md)和[实例结构](P126_IPC的RPMsg实例结构.md)。

---

[上一章：IPC的RPMsg头文件参考](P127_IPC的RPMsg头文件参考.md) · [下一章：IPC静态虚拟环接口](P129_IPC静态虚拟环接口.md) · [返回大纲](大纲.md)
