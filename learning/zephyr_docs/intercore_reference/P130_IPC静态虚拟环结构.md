---
id: learning.zephyr-docs.intercore_reference.rpmsgref-130
title: IPC静态虚拟环结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structipc__static__vrings.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第130章\_IPC静态虚拟环结构

原文：[structipc__static__vrings](https://docs.zephyrproject.org/latest/doxygen/html/structipc__static__vrings.html)。读取日期：2026-10-13，`latest`。

`ipc_static_vrings`用于表示和传递虚拟环静态分配（Static Allocation of VRINGs）的信息，来自`zephyr/ipc/ipc_static_vrings.h`。IPC 指处理器间通信（Inter-Processor Communication），VRING 指虚拟环，VQ 指虚拟队列（Virtqueue）。

SHM 是共享内存（Shared Memory），I/O 是输入输出（Input/Output）；TX 为发送（Transmit），RX 为接收（Receive）。VirtIO 保留原虚拟输入输出框架名称。

下方`VRING_COUNT`为虚拟环数量宏；`ipc_notify_cb`是通知回调类型，`notify_cb`为回调成员，`priv`为传给回调的私有数据。

```c
struct ipc_static_vrings {
        struct virtio_device vdev;

        metal_phys_addr_t shm_physmap[1];

        uintptr_t status_reg_addr;

        uintptr_t tx_addr;

        uintptr_t rx_addr;

        size_t vring_size;

        uintptr_t shm_addr;

        size_t shm_size;

        struct metal_io_region shm_io;

        struct virtio_vring_info rvrings[VRING_COUNT];

        struct virtqueue *vq[VRING_COUNT];

        void *priv;

        ipc_notify_cb notify_cb;
};
```

## 130.1\_结构成员

| 类型 | 成员 | 含义 |
| --- | --- | --- |
| `struct virtio_device` | `vdev` | VirtIO 设备 |
| `metal_phys_addr_t`数组 | `shm_physmap[1]` | 共享内存物理地址映射（SHM Physical Map） |
| `uintptr_t` | `status_reg_addr` | 原页说明为“共享内存与地址”（SHM and addresses）；字段名原样保留 |
| `uintptr_t` | `tx_addr` | 发送虚拟环地址 |
| `uintptr_t` | `rx_addr` | 接收虚拟环地址 |
| `size_t` | `vring_size` | 虚拟环大小 |
| `uintptr_t` | `shm_addr` | 共享内存区域地址 |
| `size_t` | `shm_size` | 共享内存区域大小 |
| `struct metal_io_region` | `shm_io` | 共享内存 I/O 区域 |
| `struct virtio_vring_info`数组 | `rvrings[VRING_COUNT]` | 虚拟环信息 |
| `struct virtqueue *`数组 | `vq[VRING_COUNT]` | 虚拟队列指针 |
| `void *` | `priv` | 传给通知回调的私有数据 |
| `ipc_notify_cb` | `notify_cb` | 通知回调（Notify Callback） |

`uintptr_t`是可容纳指针表示的无符号整数类型，`size_t`用于表示大小，`metal_phys_addr_t`是原物理地址类型。源码的`VRING_COUNT`值为`(2)`，所以原结构参考页把`rvrings`和`vq`的长度显示为`[(2)]`；本页同时保留源码宏名与展开值。原文对`status_reg_addr`未作更细解释，不从字段名推定寄存器位布局或访问规则。

初始化、反初始化与回调参数见[静态虚拟环接口](P129_IPC静态虚拟环接口.md)，完整可见源码见[头文件](P132_IPC静态虚拟环完整头文件.md)。

---

[上一章：IPC静态虚拟环接口](P129_IPC静态虚拟环接口.md) · [下一章：IPC静态虚拟环头文件参考](P131_IPC静态虚拟环头文件参考.md) · [返回大纲](大纲.md)
