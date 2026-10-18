---
id: learning.zephyr-docs.intercore_reference.rpmsgref-121
title: RPMsg服务公共接口
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__rpmsg__service__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第121章\_RPMsg服务公共接口

原文：[group__rpmsg__service__api](https://docs.zephyrproject.org/latest/doxygen/html/group__rpmsg__service__api.html)。读取日期：2026-10-13，`latest`。

本页介绍远程处理器消息传递（Remote Processor Messaging，RPMsg）服务的应用程序编程接口（Application Programming Interface，API）。通过注册端点（Endpoint）与远端通信，头文件为`zephyr/ipc/rpmsg_service.h`；IPC 指处理器间通信（Inter-Processor Communication）。

原文使用主端（Master）和从端（Slave）角色名称。主从两端均使用同一个注册函数，但名称必须一致，且从端注册时才创建端点。配套运行示例见 [RPMsg 服务示例](P090_RPMsg服务示例.md)。

## 121.1\_注册端点

```c
int rpmsg_service_register_endpoint(const char *name, rpmsg_ept_cb cb);
```

注册 IPC 端点，使其能够与远端设备通信。端点在从端设备注册它时创建；主端与从端均使用此函数。

| 参数 | 含义 |
| --- | --- |
| `name` | 包含端点名称的字符串；**主端与从端必须一致** |
| `cb` | 给定端点有数据可用时执行的回调（Callback），类型为`rpmsg_ept_cb` |

| 返回值 | 含义 |
| --- | --- |
| `>=0` | 成功时返回已注册端点的标识（ID） |
| `-EINPROGRESS` | 端点创建流程已经开始后，又请求注册端点 |
| `-ENOMEM` | 可用于注册端点的槽位（Slot）不足 |
| `<0` | RPMsg 报告的其他负错误码（errno） |

## 121.2\_发送数据

```c
int rpmsg_service_send(int endpoint_id, const void *data, size_t len);
```

使用给定 IPC 端点发送数据。

| 参数 | 含义 |
| --- | --- |
| `endpoint_id` | 通过`rpmsg_service_register_endpoint()`取得的已注册端点标识 |
| `data` | 要通过 RPMsg 服务发送的缓冲区指针 |
| `len` | 待发送字节数 |

| 返回值 | 含义 |
| --- | --- |
| `>=0` | 已发送字节数 |
| `<0` | RPMsg 报告的错误码 |

## 121.3\_检查绑定状态

```c
bool rpmsg_service_endpoint_is_bound(int endpoint_id);
```

检查远端端点是否已经创建，以及主端是否已经把自己的端点绑定到它。返回类型`bool`为布尔类型（Boolean）。

| 参数 | 含义 |
| --- | --- |
| `endpoint_id` | 通过`rpmsg_service_register_endpoint()`取得的已注册端点标识 |

| 返回值 | 含义 |
| --- | --- |
| `true` | 端点已经绑定（Bound） |
| `false` | 端点尚未绑定 |

完整可见声明见[RPMsg服务完整头文件](P123_RPMsg服务完整头文件.md)。

---

[上一章：IPC服务后端完整头文件](P120_IPC服务后端完整头文件.md) · [下一章：RPMsg服务头文件参考](P122_RPMsg服务头文件参考.md) · [返回大纲](大纲.md)
