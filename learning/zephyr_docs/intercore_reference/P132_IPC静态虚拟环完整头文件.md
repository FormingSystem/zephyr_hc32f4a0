---
id: learning.zephyr-docs.intercore_reference.rpmsgref-132
title: IPC静态虚拟环完整头文件
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ipc__static__vrings_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第132章\_IPC静态虚拟环完整头文件

原文：[ipc__static__vrings_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/ipc__static__vrings_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览页中`zephyr/ipc/ipc_static_vrings.h`的完整可见代码，用于IPC 静态虚拟环。RPMsg 为远程处理器消息传递（Remote Processor Messaging），IPC 为处理器间通信（Inter-Processor Communication）。展示行号已移除，声明、版权和许可证均保留。

阅读提示：`VRING_COUNT`是虚拟环数量宏；`MEM_ALIGNMENT`是内存对齐宏，取值来自 Kconfig 配置项`CONFIG_IPC_SERVICE_STATIC_VRINGS_MEM_ALIGNMENT`。Kconfig 是 Zephyr 的配置系统。

## 132.1\_完整可见源码

```c
/*
 * Copyright (c) 2021 Carlo Caione <ccaione@baylibre.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_IPC_IPC_STATIC_VRINGS_H_
#define ZEPHYR_INCLUDE_IPC_IPC_STATIC_VRINGS_H_

#include <zephyr/ipc/ipc_service.h>
#include <openamp/open_amp.h>

#ifdef __cplusplus
extern "C" {
#endif


#define VRING_COUNT     (2)

#define MEM_ALIGNMENT   CONFIG_IPC_SERVICE_STATIC_VRINGS_MEM_ALIGNMENT

typedef void (*ipc_notify_cb)(struct virtqueue *vq, void *priv);

struct ipc_static_vrings {
        struct virtio_device vdev;

        metal_phys_addr_t shm_physmap[1];

        uintptr_t status_reg_addr;

        uintptr_t tx_addr;

        uintptr_t rx_addr;

        size_t vring_size;

        uintptr_t shm_addr;

        size_t shm_size;

        struct metal_io_region shm_io;

        struct virtio_vring_info rvrings[VRING_COUNT];

        struct virtqueue *vq[VRING_COUNT];

        void *priv;

        ipc_notify_cb notify_cb;
};

int ipc_static_vrings_init(struct ipc_static_vrings *vr, unsigned int role);

int ipc_static_vrings_deinit(struct ipc_static_vrings *vr, unsigned int role);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_IPC_IPC_STATIC_VRINGS_H_ */
```

## 132.2\_源码说明与对应译文

原文件版权为2021年 Carlo Caione，许可证为 Apache-2.0。头文件保护宏（Header Guard）为`ZEPHYR_INCLUDE_IPC_IPC_STATIC_VRINGS_H_`；文件末尾注释标识该保护宏的结束。
`__cplusplus`条件分支和`extern "C"`用于保持 C++ 环境下的 C 语言链接方式。官方 Doxygen 源码浏览页把文档注释提取到说明页，相关中文译文见[静态虚拟环接口](P129_IPC静态虚拟环接口.md)和[结构](P130_IPC静态虚拟环结构.md)。

---

[上一章：IPC静态虚拟环头文件参考](P131_IPC静态虚拟环头文件参考.md) · [下一章：静态虚拟环常量头文件参考](P133_静态虚拟环常量头文件参考.md) · [返回大纲](大纲.md)
