---
id: learning.zephyr-docs.intercore_reference.rpmsgref-126
title: IPC的RPMsg实例结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structipc__rpmsg__instance.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第126章\_IPC的RPMsg实例结构

原文：[structipc__rpmsg__instance](https://docs.zephyrproject.org/latest/doxygen/html/structipc__rpmsg__instance.html)。读取日期：2026-10-13，`latest`。

`ipc_rpmsg_instance`用于以结构体表示 RPMsg 实例（Instance）。RPMsg 为远程处理器消息传递（Remote Processor Messaging），IPC 为处理器间通信（Inter-Processor Communication）；头文件为`zephyr/ipc/ipc_rpmsg.h`。

下方端点数量宏`NUM_ENDPOINTS`的值来自 Kconfig 配置项`CONFIG_IPC_SERVICE_BACKEND_RPMSG_NUM_ENDPOINTS_PER_INSTANCE`；Kconfig 是 Zephyr 的配置系统。

```c
struct ipc_rpmsg_instance {
        struct ipc_rpmsg_ept endpoint[NUM_ENDPOINTS];

        struct rpmsg_virtio_device rvdev;

        struct rpmsg_virtio_shm_pool shm_pool;

        rpmsg_ept_bound_cb bound_cb;

        rpmsg_ept_cb cb;

        struct k_mutex mtx;
};
```

## 126.1\_结构成员

| 类型 | 成员 | 含义 |
| --- | --- | --- |
| `struct ipc_rpmsg_ept`数组 | `endpoint[NUM_ENDPOINTS]` | 实例中的[端点（Endpoint）](P125_IPC的RPMsg端点结构.md) |
| `struct rpmsg_virtio_device` | `rvdev` | RPMsg 的 VirtIO 设备，VirtIO 保留原虚拟输入输出框架名称 |
| `struct rpmsg_virtio_shm_pool` | `shm_pool` | 共享内存池（Shared Memory Pool，SHM Pool） |
| `rpmsg_ept_bound_cb` | `bound_cb` | 端点／实例绑定回调（Endpoint Bound Callback） |
| `rpmsg_ept_cb` | `cb` | 端点／实例回调（Endpoint Callback） |
| `struct k_mutex` | `mtx` | 该实例的互斥锁（Mutex） |

原文将端点简写为 EPT（Endpoint）。源码使用`NUM_ENDPOINTS`作为数组长度，它展开为`CONFIG_IPC_SERVICE_BACKEND_RPMSG_NUM_ENDPOINTS_PER_INSTANCE`；原结构参考页显示的正是该展开结果。

`rpmsg_ept_bound_cb`在实例级定义，实例内端点完成绑定时调用，详见[RPMsg公共层接口](P124_IPC的RPMsg公共层接口.md)。完整可见源码见[头文件](P128_IPC的RPMsg完整头文件.md)。

---

[上一章：IPC的RPMsg端点结构](P125_IPC的RPMsg端点结构.md) · [下一章：IPC的RPMsg头文件参考](P127_IPC的RPMsg头文件参考.md) · [返回大纲](大纲.md)
