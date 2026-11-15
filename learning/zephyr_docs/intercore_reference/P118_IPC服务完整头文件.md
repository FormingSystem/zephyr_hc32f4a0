---
id: learning.zephyr-docs.intercore_reference.ipcsvc-118
title: IPC服务完整头文件
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ipc__service_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第118章\_IPC服务完整头文件

原文：[ipc__service_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/ipc__service_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览页中`zephyr/ipc/ipc_service.h`的完整可见代码。IPC 为处理器间通信（Inter-Processor Communication）。展示行号已移除，声明、条件编译、版权和许可证均保留。

## 118.1\_完整可见源码

```c
/*
 * Copyright (c) 2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_IPC_IPC_SERVICE_H_
#define ZEPHYR_INCLUDE_IPC_IPC_SERVICE_H_

#include <stdio.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif






struct ipc_service_cb {
        void (*bound)(void *priv);

        void (*unbound)(void *priv);

        void (*received)(const void *data, size_t len, void *priv);

        void (*error)(const char *message, void *priv);
};

struct ipc_ept {

        const struct device *instance;

        void *token;
};

struct ipc_ept_cfg {

        const char *name;

        int prio;

        struct ipc_service_cb cb;

        void *priv;
};

int ipc_service_open_instance(const struct device *instance);

int ipc_service_close_instance(const struct device *instance);

int ipc_service_register_endpoint(const struct device *instance,
                                  struct ipc_ept *ept,
                                  const struct ipc_ept_cfg *cfg);

int ipc_service_deregister_endpoint(struct ipc_ept *ept);

int ipc_service_send(struct ipc_ept *ept, const void *data, size_t len);

int ipc_service_send_critical(struct ipc_ept *ept, const void *data, size_t len);

int ipc_service_get_tx_buffer_size(struct ipc_ept *ept);

int ipc_service_get_tx_buffer(struct ipc_ept *ept, void **data, uint32_t *size, k_timeout_t wait);

int ipc_service_drop_tx_buffer(struct ipc_ept *ept, const void *data);

int ipc_service_send_nocopy(struct ipc_ept *ept, const void *data, size_t len);

int ipc_service_hold_rx_buffer(struct ipc_ept *ept, void *data);

int ipc_service_release_rx_buffer(struct ipc_ept *ept, void *data);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_IPC_IPC_SERVICE_H_ */
```

## 118.2\_源码说明与对应译文

原文件版权为2021年 Nordic Semiconductor ASA，许可证为 Apache-2.0。头文件保护宏（Header Guard）为`ZEPHYR_INCLUDE_IPC_IPC_SERVICE_H_`；`__cplusplus`条件分支和`extern "C"`用于保持 C++ 环境下的 C 语言链接方式。

官方 Doxygen 源码浏览页把文档注释提取到接口说明中，因此上方保留其可见代码；对应中文说明见[公共接口](P111_IPC服务公共接口.md)、[回调结构](P112_IPC服务回调结构.md)、[端点结构](P113_IPC服务端点结构.md)和[端点配置](P114_IPC服务端点配置.md)。文件末尾注释标识头文件保护宏的结束。

---

[上一章：IPC服务头文件参考](P117_IPC服务头文件参考.md) · [下一章：IPC服务后端头文件参考](P119_IPC服务后端头文件参考.md) · [返回大纲](大纲.md)
