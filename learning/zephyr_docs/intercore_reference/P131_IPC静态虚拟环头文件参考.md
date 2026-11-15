---
id: learning.zephyr-docs.intercore_reference.rpmsgref-131
title: IPC静态虚拟环头文件参考
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ipc__static__vrings_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第131章\_IPC静态虚拟环头文件参考

原文：[ipc__static__vrings_8h](https://docs.zephyrproject.org/latest/doxygen/html/ipc__static__vrings_8h.html)。读取日期：2026-10-13，`latest`。

本页是 IPC 处理器间通信（Inter-Processor Communication）服务的静态虚拟环（Static VRINGs）头文件`zephyr/ipc/ipc_static_vrings.h`参考索引。

`VRING_COUNT`是虚拟环数量宏，`MEM_ALIGNMENT`取值来自 Kconfig 配置项`CONFIG_IPC_SERVICE_STATIC_VRINGS_MEM_ALIGNMENT`，指定内存对齐。

## 131.1\_包含文件

```c
#include <zephyr/ipc/ipc_service.h>
#include <openamp/open_amp.h>
```

## 131.2\_结构、宏与回调

静态虚拟环信息通过[`ipc_static_vrings`结构](P130_IPC静态虚拟环结构.md)表示。

以下宏分别规定虚拟环缓冲区数量和内存对齐（Memory Alignment）：

```c
#define VRING_COUNT     (2)
#define MEM_ALIGNMENT   CONFIG_IPC_SERVICE_STATIC_VRINGS_MEM_ALIGNMENT
```

通知回调（Notify Callback）类型，`vq`为虚拟队列（Virtqueue）：

```c
typedef void (*ipc_notify_cb)(struct virtqueue *vq, void *priv);
```

## 131.3\_函数声明

初始化静态虚拟环：

```c
int ipc_static_vrings_init(struct ipc_static_vrings *vr, unsigned int role);
```

反初始化（Deinitialize）静态虚拟环：

```c
int ipc_static_vrings_deinit(struct ipc_static_vrings *vr, unsigned int role);
```

参数、返回值及缓存对齐要求见[静态虚拟环接口](P129_IPC静态虚拟环接口.md)，完整可见代码见[头文件源码](P132_IPC静态虚拟环完整头文件.md)。

---

[上一章：IPC静态虚拟环结构](P130_IPC静态虚拟环结构.md) · [下一章：IPC静态虚拟环完整头文件](P132_IPC静态虚拟环完整头文件.md) · [返回大纲](大纲.md)
