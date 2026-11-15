---
id: learning.zephyr-docs.intercore_reference.rpmsgref-127
title: IPC的RPMsg头文件参考
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ipc__rpmsg_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第127章\_IPC的RPMsg头文件参考

原文：[ipc__rpmsg_8h](https://docs.zephyrproject.org/latest/doxygen/html/ipc__rpmsg_8h.html)。读取日期：2026-10-13，`latest`。

本页是 IPC 处理器间通信（Inter-Processor Communication）服务的 RPMsg 头文件`zephyr/ipc/ipc_rpmsg.h`参考索引。RPMsg 指远程处理器消息传递（Remote Processor Messaging）。

`NUM_ENDPOINTS`是端点数量宏，取值来自 Kconfig 配置项`CONFIG_IPC_SERVICE_BACKEND_RPMSG_NUM_ENDPOINTS_PER_INSTANCE`。

## 127.1\_包含文件

```c
#include <zephyr/ipc/ipc_service.h>
#include <openamp/open_amp.h>
#include <metal/device.h>
```

## 127.2\_结构、宏与回调

原页列出[端点结构`ipc_rpmsg_ept`](P125_IPC的RPMsg端点结构.md)和[实例结构`ipc_rpmsg_instance`](P126_IPC的RPMsg实例结构.md)。

端点数量宏：

```c
#define NUM_ENDPOINTS   CONFIG_IPC_SERVICE_BACKEND_RPMSG_NUM_ENDPOINTS_PER_INSTANCE
```

绑定回调（Bound Callback）类型定义：

```c
typedef void (*rpmsg_ept_bound_cb)(struct ipc_rpmsg_ept *ept);
```

## 127.3\_函数声明

初始化 RPMsg 实例。

```c
int ipc_rpmsg_init(struct ipc_rpmsg_instance *instance,
                   unsigned int role,
                   unsigned int buffer_size,
                   struct metal_io_region *shm_io,
                   struct virtio_device *vdev,
                   void *shb, size_t size,
                   rpmsg_ns_bind_cb ns_bind_cb);
```

反初始化（Deinitialize）RPMsg 实例。

```c
int ipc_rpmsg_deinit(struct ipc_rpmsg_instance *instance,
                   unsigned int role);
```

注册端点。

```c
int ipc_rpmsg_register_ept(struct ipc_rpmsg_instance *instance, unsigned int role,
                           struct ipc_rpmsg_ept *ept);
```

详细参数和返回值见[RPMsg公共层接口](P124_IPC的RPMsg公共层接口.md)，完整可见代码见[头文件源码](P128_IPC的RPMsg完整头文件.md)。

---

[上一章：IPC的RPMsg实例结构](P126_IPC的RPMsg实例结构.md) · [下一章：IPC的RPMsg完整头文件](P128_IPC的RPMsg完整头文件.md) · [返回大纲](大纲.md)
