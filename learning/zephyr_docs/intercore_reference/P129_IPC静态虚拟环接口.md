---
id: learning.zephyr-docs.intercore_reference.rpmsgref-129
title: IPC静态虚拟环接口
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ipc__service__static__vrings__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第129章\_IPC静态虚拟环接口

原文：[group__ipc__service__static__vrings__api](https://docs.zephyrproject.org/latest/doxygen/html/group__ipc__service__static__vrings__api.html)。读取日期：2026-10-13，`latest`。

本页是 IPC 服务静态虚拟环（Static VRINGs）的应用程序编程接口（Application Programming Interface，API）。IPC 为处理器间通信（Inter-Processor Communication），虚拟环承载虚拟队列（Virtqueue，VQ）的环形描述符结构。头文件为`zephyr/ipc/ipc_static_vrings.h`。

相关结构为[`ipc_static_vrings`](P130_IPC静态虚拟环结构.md)，用于表示静态分配的虚拟环信息。OpenAMP 为开放式非对称多处理（Open Asymmetric Multi Processing）框架，RPMsg 为远程处理器消息传递（Remote Processor Messaging）。

下方`VRING_COUNT`是虚拟环数量宏，`MEM_ALIGNMENT`是内存对齐宏，后者取值来自 Kconfig 配置项`CONFIG_IPC_SERVICE_STATIC_VRINGS_MEM_ALIGNMENT`。Kconfig 是 Zephyr 的配置系统。

## 129.1\_虚拟环数量与内存对齐

```c
#define VRING_COUNT     (2)
#define MEM_ALIGNMENT   CONFIG_IPC_SERVICE_STATIC_VRINGS_MEM_ALIGNMENT
```

`VRING_COUNT`是所用虚拟环缓冲区的数量，值为`(2)`。`MEM_ALIGNMENT`是内存对齐（Memory Alignment）要求，由`CONFIG_IPC_SERVICE_STATIC_VRINGS_MEM_ALIGNMENT`配置项给出。

**启用缓存时，对齐应考虑缓存行（Cache Line）；没有启用缓存时，应按机器字长（Machine Word Size）自然对齐。**

## 129.2\_通知回调

```c
typedef void (*ipc_notify_cb)(struct virtqueue *vq, void *priv);
```

`ipc_notify_cb`定义实例级通知回调（Notify Callback），在虚拟队列发出通知时调用。

| 参数 | 含义 |
| --- | --- |
| `vq` | 虚拟队列 |
| `priv` | 私有数据（Private Data） |

## 129.3\_初始化静态虚拟环

```c
int ipc_static_vrings_init(struct ipc_static_vrings *vr, unsigned int role);
```

初始化 OpenAMP／RPMsg 实例的虚拟环和虚拟队列。

| 参数 | 含义 |
| --- | --- |
| `vr` | 虚拟环实例结构指针 |
| `role` | 主机（Host）／远端（Remote）角色 |

| 返回值 | 含义 |
| --- | --- |
| `-EINVAL` | 缺少某个参数 |
| `-ENOMEM` | 内存不足，无法分配虚拟队列（VQs） |
| `0` | 成功 |
| `Other` | 其他错误码（errno），由 OpenAMP 实现决定 |

## 129.4\_反初始化静态虚拟环

```c
int ipc_static_vrings_deinit(struct ipc_static_vrings *vr, unsigned int role);
```

反初始化（Deinitialize）OpenAMP／RPMsg 实例的虚拟环和虚拟队列。

| 参数 | 含义 |
| --- | --- |
| `vr` | 虚拟环实例结构指针 |
| `role` | 主机（Host）／远端（Remote）角色 |

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `Other` | 其他错误码（errno），由 OpenAMP 实现决定 |

完整可见声明见[IPC静态虚拟环完整头文件](P132_IPC静态虚拟环完整头文件.md)。

---

[上一章：IPC的RPMsg完整头文件](P128_IPC的RPMsg完整头文件.md) · [下一章：IPC静态虚拟环结构](P130_IPC静态虚拟环结构.md) · [返回大纲](大纲.md)
