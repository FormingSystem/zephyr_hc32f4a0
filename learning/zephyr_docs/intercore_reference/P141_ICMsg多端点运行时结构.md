---
id: learning.zephyr-docs.intercore_reference.icmsgref-141
title: ICMsg多端点运行时结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structicmsg__me__data__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第141章\_ICMsg多端点运行时结构

原文：[structicmsg__me__data__t](https://docs.zephyrproject.org/latest/doxygen/html/structicmsg__me__data__t.html)。读取日期：2026-10-13，`latest`。

`icmsg_me_data_t`是 ICMsg 核间消息传递（Inter-core Messaging）多端点扩展（Multi-endpoint Extension，ME）的运行时数据结构（Run-time Data Structure），来自`zephyr/ipc/icmsg_me.h`。

原结构参考页列出六个成员，没有逐字段文字说明。下方阅读说明依据成员名称、类型与完整源码。数组长度由 Kconfig 配置项`CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_NUM_EP`和`CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_SEND_BUF_SIZE`给出，Kconfig 是 Zephyr 的配置系统。

```c
struct icmsg_me_data_t {
        struct icmsg_data_t icmsg_data;
        struct ipc_ept_cfg ept_cfg;

        struct k_event event;

        struct k_mutex send_mutex;
        const struct ipc_ept_cfg *epts[CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_NUM_EP];

        uint8_t send_buffer[CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_SEND_BUF_SIZE] __aligned(4);
};
```

## 141.1\_结构成员

| 类型 | 成员 | 阅读说明 |
| --- | --- | --- |
| `struct icmsg_data_t` | `icmsg_data` | 底层[ICMsg运行时数据](P137_ICMsg运行时结构.md) |
| `struct ipc_ept_cfg` | `ept_cfg` | [端点配置结构](P114_IPC服务端点配置.md) |
| `struct k_event` | `event` | 内核事件对象（Event Object） |
| `struct k_mutex` | `send_mutex` | 发送互斥锁（Mutex） |
| `const struct ipc_ept_cfg *`数组 | `epts[CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_NUM_EP]` | 端点配置指针槽位数组 |
| `uint8_t`数组 | `send_buffer[CONFIG_IPC_SERVICE_BACKEND_ICMSG_ME_SEND_BUF_SIZE]` | 发送缓冲区 |

原源码的`send_buffer`还带有`__aligned(4)`对齐属性（Alignment Attribute），即4字节对齐；原结构参考页未显示该属性，上方完整声明已保留。`uint8_t`为8位无符号整数类型。

初始化函数要求此结构在调用时全部填零，并在实例活动期间持续保留其内容，详见[多端点接口](P140_ICMsg多端点接口.md)。完整可见定义见[多端点完整头文件](P143_ICMsg多端点完整头文件.md)。

---

[上一章：ICMsg多端点接口](P140_ICMsg多端点接口.md) · [下一章：ICMsg多端点头文件参考](P142_ICMsg多端点头文件参考.md) · [返回大纲](大纲.md)
