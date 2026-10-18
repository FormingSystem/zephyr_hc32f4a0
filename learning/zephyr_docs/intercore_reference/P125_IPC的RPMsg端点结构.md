---
id: learning.zephyr-docs.intercore_reference.rpmsgref-125
title: IPC的RPMsg端点结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structipc__rpmsg__ept.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第125章\_IPC的RPMsg端点结构

原文：[structipc__rpmsg__ept](https://docs.zephyrproject.org/latest/doxygen/html/structipc__rpmsg__ept.html)。读取日期：2026-10-13，`latest`。

`ipc_rpmsg_ept`是 IPC 处理器间通信（Inter-Processor Communication）服务使用的 RPMsg 端点结构（Endpoint Structure）。RPMsg 指远程处理器消息传递（Remote Processor Messaging）。它定义一个封装在 RPMsg 实例（Instance）内的端点，来自`zephyr/ipc/ipc_rpmsg.h`。

下方`RPMSG_NAME_SIZE`是端点名称数组长度常量；结构中的每个成员在表中逐项解释。

```c
struct ipc_rpmsg_ept {
        struct rpmsg_endpoint ep;

        char name[RPMSG_NAME_SIZE];

        uint32_t dest;

        volatile bool bound;

        const struct ipc_service_cb *cb;

        void *priv;
};
```

## 125.1\_结构成员

| 类型 | 成员 | 含义 |
| --- | --- | --- |
| `struct rpmsg_endpoint` | `ep` | RPMsg 端点 |
| `char`数组 | `name[RPMSG_NAME_SIZE]` | 端点名称，数组长度由`RPMSG_NAME_SIZE`常量确定 |
| `uint32_t` | `dest` | 目标端点（Destination Endpoint） |
| `volatile bool` | `bound` | 绑定标志（Bound Flag） |
| `const struct ipc_service_cb *` | `cb` | [事件回调结构指针（Callback）](P112_IPC服务回调结构.md) |
| `void *` | `priv` | 传给端点回调的私有数据（Private Data） |

原字段类型中的`uint32_t`为32位无符号整数，`bool`为布尔类型，`volatile`限定符按源码保留。原页没有在此给出名称数组长度的数值，因此保留常量名称。

相关注册接口见[RPMsg公共层接口](P124_IPC的RPMsg公共层接口.md)，完整可见源码见[头文件](P128_IPC的RPMsg完整头文件.md)。

---

[上一章：IPC的RPMsg公共层接口](P124_IPC的RPMsg公共层接口.md) · [下一章：IPC的RPMsg实例结构](P126_IPC的RPMsg实例结构.md) · [返回大纲](大纲.md)
