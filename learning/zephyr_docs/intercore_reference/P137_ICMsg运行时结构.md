---
id: learning.zephyr-docs.intercore_reference.icmsgref-137
title: ICMsg运行时结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structicmsg__data__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第137章\_ICMsg运行时结构

原文：[structicmsg__data__t](https://docs.zephyrproject.org/latest/doxygen/html/structicmsg__data__t.html)。读取日期：2026-10-13，`latest`。

`icmsg_data_t`是 ICMsg 核间消息传递（Inter-core Messaging）实例的运行时数据结构（Run-time Data Structure），来自`zephyr/ipc/icmsg.h`。原结构参考页列出八个成员，没有逐字段文字说明。下表提供依据类型、字段名与同一头文件注释的阅读说明。

TX 表示发送（Transmit），RX 表示接收（Receive），SID 表示会话标识（Session ID）；`pbuf`为[数据包缓冲区（Packet Buffer）](P145_核间数据包缓冲区结构.md)结构，`atomic_t`为原子类型（Atomic Type）。

下方`CONFIG_IPC_SERVICE_ICMSG_SHMEM_ACCESS_SYNC`和`CONFIG_MULTITHREADING`均为 Kconfig 配置项，控制条件成员是否出现；Kconfig 是 Zephyr 的配置系统。

```c
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
```

## 137.1\_原参考页的成员

| 类型 | 成员 | 阅读说明 |
| --- | --- | --- |
| `struct pbuf *` | `tx_pb` | 发送数据包缓冲区指针 |
| `struct pbuf *` | `rx_pb` | 接收数据包缓冲区指针 |
| `const struct ipc_service_cb *` | `cb` | 端点事件[回调结构](P112_IPC服务回调结构.md)指针 |
| `void *` | `ctx` | 回调上下文（Context） |
| `const struct icmsg_config_t *` | `cfg` | [配置结构](P136_ICMsg配置结构.md)指针 |
| `uint16_t` | `remote_sid` | 远端会话标识 |
| `uint16_t` | `local_sid` | 本地会话标识 |
| `atomic_t` | `state` | 实例状态 |

`uint16_t`为16位无符号整数类型。

## 137.2\_源码中的条件成员

完整源码还包含两个受条件编译（Conditional Compilation）控制的成员，原结构参考页没有列出；这里补充其声明以对照源码：

| 配置条件 | 类型 | 成员 | 阅读说明 |
| --- | --- | --- | --- |
| `CONFIG_IPC_SERVICE_ICMSG_SHMEM_ACCESS_SYNC` | `struct k_mutex` | `tx_lock` | 发送路径的互斥锁（Mutex） |
| `CONFIG_MULTITHREADING` | `struct k_work` | `mbox_work` | 邮箱相关工作项（Work Item） |

这两个`CONFIG_`符号是 Kconfig 配置项；Kconfig 是 Zephyr 的配置系统。原可见注释依次把成员归为发送／接收缓冲区、端点回调、通用数据三组。完整可见代码见[ICMsg完整头文件](P139_ICMsg完整头文件.md)，状态行为见[基础接口](P135_ICMsg基础接口.md)。

---

[上一章：ICMsg配置结构](P136_ICMsg配置结构.md) · [下一章：ICMsg头文件参考](P138_ICMsg头文件参考.md) · [返回大纲](大纲.md)
