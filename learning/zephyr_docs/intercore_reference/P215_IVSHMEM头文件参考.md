---
id: learning.zephyr-docs.intercore_reference.api-215
title: IVSHMEM头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ivshmem_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第215章\_IVSHMEM头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ivshmem_8h.html)。读取日期：2026-10-14；以保存的latest网页为依据，HTML摘要见[来源记录](../SOURCES.md)。

## 215.1\_阅读说明与导航

> 译注：本组说明虚拟机间共享内存（Inter-VM Shared Memory，IVSHMEM）的公共接口、头文件及源码。先结合[门铃示例](../driver_samples/P067_IVSHMEM门铃示例.md)或[以太网示例](../driver_samples/P060_IVSHMEM以太网示例.md)理解数据与通知的关系，再查询各参数和返回值。

本组：[IVSHMEM共享内存接口](P214_IVSHMEM共享内存接口.md) · [IVSHMEM头文件参考](P215_IVSHMEM头文件参考.md) · [IVSHMEM头文件源码](P216_IVSHMEM头文件源码.md)。

```c
#include <zephyr/types.h>
```

```c
#include <stddef.h>
```

```c
#include <zephyr/device.h>
```

```c
#include <zephyr/kernel.h>
```

```c
#include <zephyr/syscalls/ivshmem.h>
```

## 215.2\_函数（Functions）

<a id="r_gaef043cbfbe0aa5061db57f9bbae02eca"></a>

```c
size_t ivshmem_get_mem (const struct device *dev, uintptr_t *memmap)
```

获取虚拟机间共享内存。

相关声明：[ivshmem_get_mem](P214_IVSHMEM共享内存接口.md#gaef043cbfbe0aa5061db57f9bbae02eca)。

<a id="r_gab2f0ccd5a2b8203a54ee5707b3afd6cc"></a>

```c
uint32_t ivshmem_get_id (const struct device *dev)
```

获取本虚拟机（Virtual Machine，VM）的ID。

相关声明：[ivshmem_get_id](P214_IVSHMEM共享内存接口.md#gab2f0ccd5a2b8203a54ee5707b3afd6cc)。

<a id="r_gafee360f2c35abb9a203dd9f4838b8846"></a>

```c
uint16_t ivshmem_get_vectors (const struct device *dev)
```

获取可使用的中断向量（Interrupt Vector）数量。

相关声明：[ivshmem_get_vectors](P214_IVSHMEM共享内存接口.md#gafee360f2c35abb9a203dd9f4838b8846)。

<a id="r_gab4e02271f8b854c783c359aca240d20c"></a>

```c
int ivshmem_int_peer (const struct device *dev, uint32_t peer_id, uint16_t vector)
```

向另一个虚拟机发送中断。

相关声明：[ivshmem_int_peer](P214_IVSHMEM共享内存接口.md#gab4e02271f8b854c783c359aca240d20c)。

<a id="r_ga88aacb71bff0375c10fdb48e34b359fe"></a>

```c
int ivshmem_register_handler (const struct device *dev, struct k_poll_signal *signal, uint16_t vector)
```

注册向量通知（中断）处理程序。

相关声明：[ivshmem_register_handler](P214_IVSHMEM共享内存接口.md#ga88aacb71bff0375c10fdb48e34b359fe)。

<a id="r_ga8b5175861401e5eb5d322f904172b963"></a>

```c
size_t ivshmem_get_rw_mem_section (const struct device *dev, uintptr_t *memmap)
```

获取IVSHMEM读写区（Read/Write Section）；仅适用于ivshmem-v2。

相关声明：[ivshmem_get_rw_mem_section](P214_IVSHMEM共享内存接口.md#ga8b5175861401e5eb5d322f904172b963)。

<a id="r_ga42a6649e852d9b81f8729fb4297043e2"></a>

```c
size_t ivshmem_get_output_mem_section (const struct device *dev, uint32_t peer_id, uintptr_t *memmap)
```

获取某个对端（Peer）的IVSHMEM输出区（Output Section）；仅适用于ivshmem-v2。

相关声明：[ivshmem_get_output_mem_section](P214_IVSHMEM共享内存接口.md#ga42a6649e852d9b81f8729fb4297043e2)。

<a id="r_ga94673f449d111364cfade9192669a5a8"></a>

```c
uint32_t ivshmem_get_state (const struct device *dev, uint32_t peer_id)
```

获取某个对端的状态值；仅适用于ivshmem-v2。

相关声明：[ivshmem_get_state](P214_IVSHMEM共享内存接口.md#ga94673f449d111364cfade9192669a5a8)。

<a id="r_ga144506b762865c6bd451c09f6407fb86"></a>

```c
int ivshmem_set_state (const struct device *dev, uint32_t state)
```

设置本虚拟机的状态；仅适用于ivshmem-v2。

相关声明：[ivshmem_set_state](P214_IVSHMEM共享内存接口.md#ga144506b762865c6bd451c09f6407fb86)。

<a id="r_gaaa7e99f4844f270d1f1d2271b43d607c"></a>

```c
uint32_t ivshmem_get_max_peers (const struct device *dev)
```

获取所支持的最大对端数量；仅适用于ivshmem-v2。

相关声明：[ivshmem_get_max_peers](P214_IVSHMEM共享内存接口.md#gaaa7e99f4844f270d1f1d2271b43d607c)。

<a id="r_ga940ffec4ae0380d774c05107afe41994"></a>

```c
uint16_t ivshmem_get_protocol (const struct device *dev)
```

获取此IVSHMEM实例使用的协议；仅适用于ivshmem-v2。

相关声明：[ivshmem_get_protocol](P214_IVSHMEM共享内存接口.md#ga940ffec4ae0380d774c05107afe41994)。

<a id="r_ga67dc8b24f863c3e9a8ac6a89753fd4c9"></a>

```c
int ivshmem_enable_interrupts (const struct device *dev, bool enable)
```

设置本虚拟机的中断使能状态；仅适用于ivshmem-v2。

相关声明：[ivshmem_enable_interrupts](P214_IVSHMEM共享内存接口.md#ga67dc8b24f863c3e9a8ac6a89753fd4c9)。

## 215.3\_源码跟踪与验证边界

本仓库[对应头文件](../../../include/zephyr/drivers/virtualization/ivshmem.h)、[驱动实现](../../../drivers/virtualization/virt_ivshmem.c)和[系统调用验证包装](../../../drivers/virtualization/virt_ivshmem_handlers.c)可用于源码跟踪；本仓库版本不自动等同于网页版本。本批译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/virtualization/ivshmem.h)、[官方驱动](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/virtualization/virt_ivshmem.c)和[官方包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/virtualization/virt_ivshmem_handlers.c)，摘要见[来源记录](../SOURCES.md)。main分支会变化，以上实现结论不能当作所有版本的接口保证。

项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。本文未安装、构建、运行虚拟机、配置共享内存或进行接线测量。

<a id="header-func-members"></a>
<a id="func-members"></a>

[上一章](P214_IVSHMEM共享内存接口.md) · [返回大纲](大纲.md) · [下一章](P216_IVSHMEM头文件源码.md)
