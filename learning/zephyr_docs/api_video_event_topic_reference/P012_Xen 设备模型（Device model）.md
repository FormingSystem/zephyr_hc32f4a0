---
id: learning.zephyr-docs.api-video-event-topic-reference.page-12
title: Xen 设备模型（Device model）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_Xen 设备模型（Device model）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__device__model.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

管理 Xen I/O 请求服务器及相关的设备模型状态。

<a id="details"></a>

管理 Xen I/O 请求服务器及相关的设备模型状态。

<a id="header-files"></a>
<a id="files"></a>

## 12.1\_文件（Files）

<a id="r_dmop_2Eh"></a>

```c
file dmop.h
```

相关声明：[dmop.h](../api_file_system_device_reference/P008_zephyr__xen__dmop.h_文件参考.md)。

Xen设备模型（Device Model）的操作。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.2\_函数（Functions）

<a id="r_ga40415eef4694532cc74e9072c4dbf932"></a>

```c
int dmop_create_ioreq_server (domid_t domid, uint8_t handle_bufioreq, ioservid_t *id)
```

相关声明：[dmop_create_ioreq_server](#ga40415eef4694532cc74e9072c4dbf932)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在指定 Xen 域（domain）中创建 I/O 请求服务器（I/O request server）。

<a id="r_ga446b7e88737168d3f9664209a8aec7ea"></a>

```c
int dmop_destroy_ioreq_server (domid_t domid, ioservid_t id)
```

相关声明：[dmop_destroy_ioreq_server](#ga446b7e88737168d3f9664209a8aec7ea)。

销毁先前创建的 I/O 请求服务器。

<a id="r_gac0649dea8445c2dc0767f559924ebb42"></a>

```c
int dmop_map_io_range_to_ioreq_server (domid_t domid, ioservid_t id, uint32_t type, uint64_t start, uint64_t end)
```

相关声明：[dmop_map_io_range_to_ioreq_server](#gac0649dea8445c2dc0767f559924ebb42)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

将指定 I/O 地址范围映射到已有 I/O 请求服务器。

<a id="r_ga4c1fd9b02e326c62ccd04b97647e8fff"></a>

```c
int dmop_unmap_io_range_from_ioreq_server (domid_t domid, ioservid_t id, uint32_t type, uint64_t start, uint64_t end)
```

相关声明：[dmop_unmap_io_range_from_ioreq_server](#ga4c1fd9b02e326c62ccd04b97647e8fff)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

从 I/O 请求服务器解除 I/O 地址范围的映射。

<a id="r_ga2d5158224201ab0e00f5bc646aeac6d7"></a>

```c
int dmop_set_ioreq_server_state (domid_t domid, ioservid_t id, uint8_t enabled)
```

相关声明：[dmop_set_ioreq_server_state](#ga2d5158224201ab0e00f5bc646aeac6d7)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

启用或禁用已有 I/O 请求服务器。

<a id="r_ga11aa8e4e414cd36de158467c602d0648"></a>

```c
int dmop_nr_vcpus (domid_t domid)
```

相关声明：[dmop_nr_vcpus](#ga11aa8e4e414cd36de158467c602d0648)。

查询 Xen 域中的虚拟 CPU（vCPU）数量。

<a id="r_ga6c806ca662b075fa0ff7efec4ac114ee"></a>

```c
int dmop_set_irq_level (domid_t domid, uint32_t irq, uint8_t level)
```

相关声明：[dmop_set_irq_level](#ga6c806ca662b075fa0ff7efec4ac114ee)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 Xen 域中指定 IRQ 的中断电平（interrupt level）。

## 12.3\_详细说明（Detailed Documentation）

<a id="ga40415eef4694532cc74e9072c4dbf932"></a>

### `dmop_create_ioreq_server()`

```c
int dmop_create_ioreq_server ( domid_t domid, uint8_t handle_bufioreq, ioservid_t * id )
```

```c
#include <zephyr/xen/dmop.h>
```

在指定 Xen 域（domain）中创建 I/O 请求服务器（I/O request server）。

此函数发出 `XEN_DMOP_create_ioreq_server` 超级调用（Hypercall），创建一个代来宾域（Guest Domain）处理输入／输出请求（I/O Requests）的服务器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` domid` | 创建服务器所在的 Xen 域标识符（Domain Identifier）。 |
| ` handle_bufioreq` | 指示是否处理带缓冲的输入／输出请求（Buffered I/O Requests）的标志。设为非零值以启用缓冲处理。 |
| `[out] id` | 输出指针，用于接收新创建的服务器 ID（Server ID）。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_DMOP` 时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga446b7e88737168d3f9664209a8aec7ea"></a>

### `dmop_destroy_ioreq_server()`

```c
int dmop_destroy_ioreq_server ( domid_t domid, ioservid_t id )
```

```c
#include <zephyr/xen/dmop.h>
```

销毁先前创建的 I/O 请求服务器。

发出 `XEN_DMOP_destroy_ioreq_server` 超级调用（Hypercall），拆除指定的输入／输出请求服务器（I/O Request Server）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 服务器所在的 Xen 域标识符（Domain Identifier）。 |
| `id` | `dmop_create_ioreq_server()` 返回的输入／输出请求服务器 ID（I/O Request Server ID）。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_DMOP` 时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gac0649dea8445c2dc0767f559924ebb42"></a>

### `dmop_map_io_range_to_ioreq_server()`

```c
int dmop_map_io_range_to_ioreq_server ( domid_t domid, ioservid_t id, uint32_t type, uint64_t start, uint64_t end )
```

```c
#include <zephyr/xen/dmop.h>
```

将指定 I/O 地址范围映射到已有 I/O 请求服务器。

此函数发出 `XEN_DMOP_map_io_range_to_ioreq_server` 超级调用（Hypercall），授予指定服务器访问所给 I/O 地址范围的权限。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 应用映射的 Xen 域标识符（Domain Identifier）。 |
| `id` | `dmop_create_ioreq_server()` 返回的输入／输出请求服务器 ID（I/O Request Server ID）。 |
| `type` | 输入／输出范围的类型标识符（I/O Range Type Identifier），例如内存映射输入输出（MMIO）或端口 I/O。 |
| `start` | 输入／输出范围（I/O Range）的起始物理地址。 |
| `end` | 输入／输出范围（I/O Range）的结束物理地址，包含此地址。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_DMOP` 时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga11aa8e4e414cd36de158467c602d0648"></a>

### `dmop_nr_vcpus()`

```c
int dmop_nr_vcpus ( domid_t domid)
```

```c
#include <zephyr/xen/dmop.h>
```

查询 Xen 域中的虚拟 CPU（vCPU）数量。

此函数发出 `XEN_DMOP_nr_vcpus` 超级调用（Hypercall），获取指定域当前的虚拟 CPU（vCPU）数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 要查询的 Xen 域标识符（Domain Identifier）。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_DMOP` 时可用。

**返回（Returns）**：返回值：成功返回虚拟 CPU（vCPU）数量，失败返回负 errno 值。

<a id="ga2d5158224201ab0e00f5bc646aeac6d7"></a>

### `dmop_set_ioreq_server_state()`

```c
int dmop_set_ioreq_server_state ( domid_t domid, ioservid_t id, uint8_t enabled )
```

```c
#include <zephyr/xen/dmop.h>
```

启用或禁用已有 I/O 请求服务器。

此函数发出 `XEN_DMOP_set_ioreq_server_state` 超级调用（Hypercall），改变指定输入／输出请求服务器（I/O Request Server）的运行状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | Xen 域标识符（Domain Identifier）。 |
| `id` | 要修改的输入／输出请求服务器 ID（I/O Request Server ID）。 |
| `enabled` | 非零值启用服务器，0 禁用服务器。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_DMOP` 时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga6c806ca662b075fa0ff7efec4ac114ee"></a>

### `dmop_set_irq_level()`

```c
int dmop_set_irq_level ( domid_t domid, uint32_t irq, uint8_t level )
```

```c
#include <zephyr/xen/dmop.h>
```

设置 Xen 域中指定 IRQ 的中断电平（interrupt level）。

此函数发出 `XEN_DMOP_set_irq_level` 超级调用（Hypercall），调整所给中断请求线（IRQ Line）的信号电平，使其有效（Assert）或无效（Deassert）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | Xen 域标识符（Domain Identifier）。 |
| `irq` | 要设置电平的中断请求（IRQ）编号。 |
| `level` | 非零值使 IRQ 有效，即拉高；0 使 IRQ 无效，即拉低。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_DMOP` 时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga4c1fd9b02e326c62ccd04b97647e8fff"></a>

### `dmop_unmap_io_range_from_ioreq_server()`

```c
int dmop_unmap_io_range_from_ioreq_server ( domid_t domid, ioservid_t id, uint32_t type, uint64_t start, uint64_t end )
```

```c
#include <zephyr/xen/dmop.h>
```

从 I/O 请求服务器解除 I/O 地址范围的映射。

发出 `XEN_DMOP_unmap_io_range_from_ioreq_server` 超级调用（Hypercall），撤销对先前已映射 I/O 地址范围的访问权限。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 执行解除映射（Unmapping）的 Xen 域标识符（Domain Identifier）。 |
| `id` | `dmop_create_ioreq_server()` 返回的输入／输出请求服务器 ID（I/O Request Server ID）。 |
| `type` | 输入／输出范围的类型标识符（I/O Range Type Identifier），例如内存映射输入输出（MMIO）或端口 I/O。 |
| `start` | 输入／输出范围（I/O Range）的起始物理地址。 |
| `end` | 输入／输出范围（I/O Range）的结束物理地址，包含此地址。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_DMOP` 时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 12.4\_原页交叉引用（Cross References）

- [dmop.h](../api_file_system_device_reference/P008_zephyr__xen__dmop.h_文件参考.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [CONFIG_XEN_DMOP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN_DMOP)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P011_视频驱动后端 API.md) · [返回大纲](大纲.md) · [下一章](P013_Xen 事件通道（Event channels）.md)
