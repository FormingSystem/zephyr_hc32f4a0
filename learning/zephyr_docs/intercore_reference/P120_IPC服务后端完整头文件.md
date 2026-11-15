---
id: learning.zephyr-docs.intercore_reference.ipcsvc-120
title: IPC服务后端完整头文件
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ipc__service__backend_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第120章\_IPC服务后端完整头文件

原文：[ipc__service__backend_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/ipc__service__backend_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览页中`zephyr/ipc/ipc_service_backend.h`的完整可见代码。IPC 为处理器间通信（Inter-Processor Communication），后端（Backend）通过函数指针提供操作实现。展示行号已移除，原声明、版权和许可证保留。

## 120.1\_完整可见源码

```c
/*
 * Copyright (c) 2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_IPC_IPC_SERVICE_BACKEND_H_
#define ZEPHYR_INCLUDE_IPC_IPC_SERVICE_BACKEND_H_

#include <zephyr/ipc/ipc_service.h>
#include <zephyr/kernel.h>
#include <stdio.h>

#ifdef __cplusplus
extern "C" {
#endif


struct ipc_service_backend {
        int (*open_instance)(const struct device *instance);

        int (*close_instance)(const struct device *instance);

        int (*send)(const struct device *instance, void *token,
                    const void *data, size_t len);

        int (*send_critical)(const struct device *instance, void *token,
                             const void *data, size_t len);

        int (*register_endpoint)(const struct device *instance,
                                 void **token,
                                 const struct ipc_ept_cfg *cfg);

        int (*deregister_endpoint)(const struct device *instance, void *token);

        int (*get_tx_buffer_size)(const struct device *instance, void *token);

        int (*get_tx_buffer)(const struct device *instance, void *token,
                             void **data, uint32_t *len, k_timeout_t wait);

        int (*drop_tx_buffer)(const struct device *instance, void *token,
                              const void *data);

        int (*send_nocopy)(const struct device *instance, void *token,
                           const void *data, size_t len);

        int (*hold_rx_buffer)(const struct device *instance, void *token,
                              void *data);

        int (*release_rx_buffer)(const struct device *instance, void *token,
                                 void *data);
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_IPC_IPC_SERVICE_BACKEND_H_ */
```

## 120.2\_源码说明与对应译文

原文件版权为2021年 Nordic Semiconductor ASA，许可证为 Apache-2.0。头文件保护宏（Header Guard）为`ZEPHYR_INCLUDE_IPC_IPC_SERVICE_BACKEND_H_`；`__cplusplus`条件分支和`extern "C"`用于保持 C++ 环境下的 C 语言链接方式。

官方 Doxygen 源码浏览页将文档注释提取到结构说明中；对应的12个成员、参数方向与返回值译文见[后端操作结构](P116_IPC服务后端操作结构.md)。其中注册回调输出后端令牌（Backend-specific Token），后续操作通过该令牌标识端点。文件末尾注释标识头文件保护宏的结束。

---

[上一章：IPC服务后端头文件参考](P119_IPC服务后端头文件参考.md) · [下一章：RPMsg服务公共接口](P121_RPMsg服务公共接口.md) · [返回大纲](大纲.md)
