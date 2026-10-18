---
id: learning.zephyr-docs.api-file-system-device-reference.page-8
title: zephyr__xen__dmop.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dmop_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_xen\_\_dmop.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dmop_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Xen设备模型（Device Model）的操作。

<a id="details"></a>

```c
#include <xen/public/hvm/dm_op.h>
```

查看此文件的源码。

Xen设备模型（Device Model）的操作。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.1\_函数（Functions）

<a id="r_ga40415eef4694532cc74e9072c4dbf932"></a>

```c
int dmop_create_ioreq_server (domid_t domid, uint8_t handle_bufioreq, ioservid_t *id)
```

相关声明：[dmop_create_ioreq_server](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#ga40415eef4694532cc74e9072c4dbf932)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在指定 Xen 域（domain）中创建 I/O 请求服务器（I/O request server）。

<a id="r_ga446b7e88737168d3f9664209a8aec7ea"></a>

```c
int dmop_destroy_ioreq_server (domid_t domid, ioservid_t id)
```

相关声明：[dmop_destroy_ioreq_server](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#ga446b7e88737168d3f9664209a8aec7ea)。

销毁先前创建的 I/O 请求服务器。

<a id="r_gac0649dea8445c2dc0767f559924ebb42"></a>

```c
int dmop_map_io_range_to_ioreq_server (domid_t domid, ioservid_t id, uint32_t type, uint64_t start, uint64_t end)
```

相关声明：[dmop_map_io_range_to_ioreq_server](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#gac0649dea8445c2dc0767f559924ebb42)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

将指定 I/O 地址范围映射到已有 I/O 请求服务器。

<a id="r_ga4c1fd9b02e326c62ccd04b97647e8fff"></a>

```c
int dmop_unmap_io_range_from_ioreq_server (domid_t domid, ioservid_t id, uint32_t type, uint64_t start, uint64_t end)
```

相关声明：[dmop_unmap_io_range_from_ioreq_server](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#ga4c1fd9b02e326c62ccd04b97647e8fff)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

从 I/O 请求服务器解除 I/O 地址范围的映射。

<a id="r_ga2d5158224201ab0e00f5bc646aeac6d7"></a>

```c
int dmop_set_ioreq_server_state (domid_t domid, ioservid_t id, uint8_t enabled)
```

相关声明：[dmop_set_ioreq_server_state](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#ga2d5158224201ab0e00f5bc646aeac6d7)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

启用或禁用已有 I/O 请求服务器。

<a id="r_ga11aa8e4e414cd36de158467c602d0648"></a>

```c
int dmop_nr_vcpus (domid_t domid)
```

相关声明：[dmop_nr_vcpus](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#ga11aa8e4e414cd36de158467c602d0648)。

查询 Xen 域中的虚拟 CPU（vCPU）数量。

<a id="r_ga6c806ca662b075fa0ff7efec4ac114ee"></a>

```c
int dmop_set_irq_level (domid_t domid, uint32_t irq, uint8_t level)
```

相关声明：[dmop_set_irq_level](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#ga6c806ca662b075fa0ff7efec4ac114ee)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 Xen 域中指定 IRQ 的中断电平（interrupt level）。


## 8.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P143_dmop.h_源码浏览.md)
- [dmop_create_ioreq_server](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#ga40415eef4694532cc74e9072c4dbf932)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [dmop_destroy_ioreq_server](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#ga446b7e88737168d3f9664209a8aec7ea)
- [dmop_map_io_range_to_ioreq_server](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#gac0649dea8445c2dc0767f559924ebb42)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [dmop_unmap_io_range_from_ioreq_server](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#ga4c1fd9b02e326c62ccd04b97647e8fff)
- [dmop_set_ioreq_server_state](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#ga2d5158224201ab0e00f5bc646aeac6d7)
- [dmop_nr_vcpus](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#ga11aa8e4e414cd36de158467c602d0648)
- [dmop_set_irq_level](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html#ga6c806ca662b075fa0ff7efec4ac114ee)

<a id="header-details"></a>

---

[上一章](P007_zephyr__storage__disk_access.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__drivers__mdio.h_文件参考.md)
