---
id: learning.zephyr-docs.intercore_reference.rpmsgref-124
title: IPC的RPMsg公共层接口
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ipc__service__rpmsg__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第124章\_IPC的RPMsg公共层接口

原文：[group__ipc__service__rpmsg__api](https://docs.zephyrproject.org/latest/doxygen/html/group__ipc__service__rpmsg__api.html)。读取日期：2026-10-13，`latest`。

本页描述 IPC 服务的 RPMsg 公共层应用程序编程接口（Application Programming Interface，API）。IPC 是处理器间通信（Inter-Processor Communication），RPMsg 是远程处理器消息传递（Remote Processor Messaging）。

头文件为`zephyr/ipc/ipc_rpmsg.h`，数据结构包括[端点`ipc_rpmsg_ept`](P125_IPC的RPMsg端点结构.md)和[实例`ipc_rpmsg_instance`](P126_IPC的RPMsg实例结构.md)。主机（Host）与远端（Remote）角色通过`role`参数传入。OpenAMP 是开放式非对称多处理（Open Asymmetric Multi Processing）框架；VirtIO 保留原框架名称，用于虚拟输入输出设备。SHM 指共享内存（Shared Memory），I/O 指输入输出（Input/Output）。

下方`NUM_ENDPOINTS`是端点数量宏，其值来自 Kconfig 配置项`CONFIG_IPC_SERVICE_BACKEND_RPMSG_NUM_ENDPOINTS_PER_INSTANCE`；Kconfig 是 Zephyr 的配置系统。

## 124.1\_端点数量

```c
#define NUM_ENDPOINTS   CONFIG_IPC_SERVICE_BACKEND_RPMSG_NUM_ENDPOINTS_PER_INSTANCE
```

`NUM_ENDPOINTS`表示端点数量，由配置项`CONFIG_IPC_SERVICE_BACKEND_RPMSG_NUM_ENDPOINTS_PER_INSTANCE`提供。

## 124.2\_实例级绑定回调

```c
typedef void (*rpmsg_ept_bound_cb)(struct ipc_rpmsg_ept *ept);
```

`rpmsg_ept_bound_cb`定义绑定回调（Bound Callback）。它在实例级定义，当该实例的某个端点完成绑定时调用。`ept`参数是刚刚完成绑定的实例端点，返回类型为`void`。

## 124.3\_初始化实例

```c
int ipc_rpmsg_init(struct ipc_rpmsg_instance *instance,
                   unsigned int role,
                   unsigned int buffer_size,
                   struct metal_io_region *shm_io,
                   struct virtio_device *vdev,
                   void *shb, size_t size,
                   rpmsg_ns_bind_cb ns_bind_cb);
```

初始化 RPMsg 实例。

| 参数 | 含义 |
| --- | --- |
| `instance` | RPMsg 实例结构指针 |
| `role` | 主机／远端角色 |
| `buffer_size` | 主机与远端之间发送数据使用的缓冲区大小 |
| `shm_io` | 共享内存 I/O 区域指针，类型为`struct metal_io_region *` |
| `vdev` | VirtIO 设备指针 |
| `shb` | 共享内存区域指针 |
| `size` | 共享内存区域大小 |
| `ns_bind_cb` | 收到名称服务公告（Name Service Announcement），且没有本地端点等待绑定时使用的回调处理函数；**为`NULL`时回退到内部实现** |

| 返回值 | 含义 |
| --- | --- |
| `-EINVAL` | 缺少某个参数 |
| `0` | 成功 |
| `Other` | 其他错误码（errno），由 OpenAMP 实现决定 |

## 124.4\_反初始化实例

```c
int ipc_rpmsg_deinit(struct ipc_rpmsg_instance *instance,
                   unsigned int role);
```

反初始化（Deinitialize）RPMsg 实例。

| 参数 | 含义 |
| --- | --- |
| `instance` | RPMsg 实例结构指针 |
| `role` | 主机／远端角色 |

| 返回值 | 含义 |
| --- | --- |
| `-EINVAL` | 缺少某个参数 |
| `0` | 成功 |

## 124.5\_注册端点

```c
int ipc_rpmsg_register_ept(struct ipc_rpmsg_instance *instance, unsigned int role,
                           struct ipc_rpmsg_ept *ept);
```

向给定 RPMsg 实例注册端点。

| 参数 | 含义 |
| --- | --- |
| `instance` | RPMsg 实例结构指针 |
| `role` | 主机／远端角色 |
| `ept` | 要注册的端点 |

| 返回值 | 含义 |
| --- | --- |
| `-EINVAL` | 缺少某个参数 |
| `0` | 成功 |
| `Other` | 其他错误码（errno），由 OpenAMP 实现决定 |

完整可见代码见[IPC的RPMsg完整头文件](P128_IPC的RPMsg完整头文件.md)。

---

[上一章：RPMsg服务完整头文件](P123_RPMsg服务完整头文件.md) · [下一章：IPC的RPMsg端点结构](P125_IPC的RPMsg端点结构.md) · [返回大纲](大纲.md)
