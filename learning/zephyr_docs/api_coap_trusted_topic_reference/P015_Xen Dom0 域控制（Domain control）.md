---
id: learning.zephyr-docs.api-coap-trusted-topic-reference.page-15
title: Xen Dom0 域控制（Domain control）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_Xen Dom0 域控制（Domain control）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

从特权域控制域的生命周期、资源和虚拟 CPU（vCPU）。

<a id="details"></a>

从特权域控制域的生命周期、资源和虚拟 CPU（vCPU）。

<a id="header-files"></a>
<a id="files"></a>

## 15.1\_文件（Files）

<a id="r_domctl_2Eh"></a>

```c
file domctl.h
```

相关声明：[domctl.h](../api_file_secure_value_reference/P005_zephyr__xen__dom0__domctl.h_文件参考.md)。

Xen Dom0的域控制操作（Domain Control Operations）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.2\_数据结构（Data Structures）

<a id="r_xen_5Fdomctl_5Fpt_5Firq"></a>

```c
struct xen_domctl_pt_irq
```

相关声明：[xen_domctl_pt_irq](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md)。

物理中断直通（Physical Interrupt Passthrough）描述符。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.3\_函数（Functions）

<a id="r_ga7045c1f92142eceefe3e4c651708beae"></a>

```c
int xen_domctl_scheduler_op (int domid, struct xen_domctl_scheduler_op *sched_op)
```

相关声明：[xen_domctl_scheduler_op](#ga7045c1f92142eceefe3e4c651708beae)。

对指定域（Domain）执行调度器操作（Scheduler Operation）。

<a id="r_gaff200f6bfe2a31b536337f5bf668fee7"></a>

```c
int xen_domctl_pausedomain (int domid)
```

相关声明：[xen_domctl_pausedomain](#gaff200f6bfe2a31b536337f5bf668fee7)。

在 Xen 虚拟机监控器（Hypervisor）中暂停域（Domain）。

<a id="r_ga89be676e7f2ff66b4dc195e35e374083"></a>

```c
int xen_domctl_unpausedomain (int domid)
```

相关声明：[xen_domctl_unpausedomain](#ga89be676e7f2ff66b4dc195e35e374083)。

在 Xen 虚拟机监控器（Hypervisor）中取消域的暂停（Unpause）。

<a id="r_ga50c40d73171240a047cf6e9b41898c99"></a>

```c
int xen_domctl_resumedomain (int domid)
```

相关声明：[xen_domctl_resumedomain](#ga50c40d73171240a047cf6e9b41898c99)。

恢复域（Resume a Domain）。

<a id="r_ga9040a9ddca3406adc057960b0f423bcd"></a>

```c
int xen_domctl_getvcpucontext (int domid, int vcpu, vcpu_guest_context_t *ctxt)
```

相关声明：[xen_domctl_getvcpucontext](#ga9040a9ddca3406adc057960b0f423bcd)。

获取域内虚拟 CPU（vCPU）的来宾上下文（Guest Context）。

<a id="r_ga66505a6d47e0c5ef3334043c668d6740"></a>

```c
int xen_domctl_setvcpucontext (int domid, int vcpu, vcpu_guest_context_t *ctxt)
```

相关声明：[xen_domctl_setvcpucontext](#ga66505a6d47e0c5ef3334043c668d6740)。

设置域内虚拟 CPU（vCPU）的来宾上下文（Guest Context）。

<a id="r_ga4848541359c3e13358dc39b42b3c142f"></a>

```c
int xen_domctl_getdomaininfo (int domid, xen_domctl_getdomaininfo_t *dom_info)
```

相关声明：[xen_domctl_getdomaininfo](#ga4848541359c3e13358dc39b42b3c142f)。

获取域（Domain）的概要信息（Summary Information）。

<a id="r_ga011ff7f30fa94479d4f1d5f7ed74b113"></a>

```c
int xen_domctl_get_paging_mempool_size (int domid, uint64_t *size)
```

相关声明：[xen_domctl_get_paging_mempool_size](#ga011ff7f30fa94479d4f1d5f7ed74b113)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

获取域的分页内存池大小（Paging Mempool Size）。

<a id="r_gaa5bbda52cad0228ffacc42518fedfdff"></a>

```c
int xen_domctl_set_paging_mempool_size (int domid, uint64_t size)
```

相关声明：[xen_domctl_set_paging_mempool_size](#gaa5bbda52cad0228ffacc42518fedfdff)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置域的分页内存池大小（Paging Mempool Size）。

<a id="r_gacbe8f22573487bcdb8612988da24b68e"></a>

```c
int xen_domctl_max_mem (int domid, uint64_t max_memkb)
```

相关声明：[xen_domctl_max_mem](#gacbe8f22573487bcdb8612988da24b68e)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置分配给域的最大内存（Maximum Memory）。

<a id="r_ga8dee93295a86c5d7b586676a831e1047"></a>

```c
int xen_domctl_set_address_size (int domid, int addr_size)
```

相关声明：[xen_domctl_set_address_size](#ga8dee93295a86c5d7b586676a831e1047)。

设置域使用的地址大小（Address Size）。

<a id="r_ga2a34701f55250140576e8c71607801f8"></a>

```c
int xen_domctl_iomem_permission (int domid, uint64_t first_mfn, uint64_t nr_mfns, uint8_t allow_access)
```

相关声明：[xen_domctl_iomem_permission](#ga2a34701f55250140576e8c71607801f8)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

允许或拒绝域访问 I/O 内存（I/O-memory Access）。

<a id="r_gac945f3330b3b03112f3fa6fb49f42e50"></a>

```c
int xen_domctl_memory_mapping (int domid, uint64_t first_gfn, uint64_t first_mfn, uint64_t nr_mfns, uint32_t add_mapping)
```

相关声明：[xen_domctl_memory_mapping](#gac945f3330b3b03112f3fa6fb49f42e50)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将机器内存范围（Machine-memory Range）映射到来宾页框范围（Guest Frame Range），或解除该映射。

<a id="r_gaf7888bd31df37d449cde69bc693c244f"></a>

```c
int xen_domctl_assign_dt_device (int domid, char *dtdev_path)
```

相关声明：[xen_domctl_assign_dt_device](#gaf7888bd31df37d449cde69bc693c244f)。

将设备树描述的设备（Devicetree-described Device）分配给来宾域（Guest Domain）。

<a id="r_ga4b7f6762c5a83b05501621b2a3c66fc3"></a>

```c
int xen_domctl_deassign_dt_device (int domid, char *dtdev_path)
```

相关声明：[xen_domctl_deassign_dt_device](#ga4b7f6762c5a83b05501621b2a3c66fc3)。

移除来宾域中由设备树描述的设备分配（Device Assignment）。

<a id="r_gad5f80dd7c0a7981f8c5c757b06993dc5"></a>

```c
int xen_domctl_bind_pt_irq (int domid, uint32_t machine_irq, uint8_t irq_type, uint8_t bus, uint8_t device, uint8_t intx, uint8_t isa_irq, uint16_t spi)
```

相关声明：[xen_domctl_bind_pt_irq](#gad5f80dd7c0a7981f8c5c757b06993dc5)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将物理中断（Physical Interrupt）绑定到来宾域（Guest Domain）。

<a id="r_gae29cc4d5d3ffcfe7e13a62030667c885"></a>

```c
int xen_domctl_unbind_pt_irq (int domid, const struct xen_domctl_pt_irq *irq)
```

相关声明：[xen_domctl_unbind_pt_irq](#gae29cc4d5d3ffcfe7e13a62030667c885)、[xen_domctl_pt_irq](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md)。

解除物理中断（Physical Interrupt）与来宾域的绑定。

<a id="r_ga8f954e5a7d1cd633c6d819780bb6372b"></a>

```c
int xen_domctl_max_vcpus (int domid, int max_vcpus)
```

相关声明：[xen_domctl_max_vcpus](#ga8f954e5a7d1cd633c6d819780bb6372b)。

设置域可使用的虚拟 CPU（vCPU）最大数量。

<a id="r_ga6d6b0c6d2baa1520322a595f0179cfa4"></a>

```c
int xen_domctl_createdomain (int *domid, struct xen_domctl_createdomain *config)
```

相关声明：[xen_domctl_createdomain](#ga6d6b0c6d2baa1520322a595f0179cfa4)。

创建新域（Domain）。

<a id="r_gad89ece398fc97a94c5c316066e2c29a5"></a>

```c
int xen_domctl_cacheflush (int domid, struct xen_domctl_cacheflush *cacheflush)
```

相关声明：[xen_domctl_cacheflush](#gad89ece398fc97a94c5c316066e2c29a5)。

对来宾内存范围执行缓存清理和失效（Clean and Invalidate Caches）。

<a id="r_gaba6a1f6e25ac6ee2a7b0d288ca4ab72d"></a>

```c
int xen_domctl_destroydomain (int domid)
```

相关声明：[xen_domctl_destroydomain](#gaba6a1f6e25ac6ee2a7b0d288ca4ab72d)。

销毁域（Domain）。

<a id="r_ga9412b5a996e287dd588e65db373c5b59"></a>

```c
int xen_domctl_getvcpu (int domid, uint32_t vcpu, struct xen_domctl_getvcpuinfo *info)
```

相关声明：[xen_domctl_getvcpu](#ga9412b5a996e287dd588e65db373c5b59)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

查询域内某个虚拟 CPU（vCPU）的运行时信息（Runtime Information）。

## 15.4\_详细说明（Detailed Documentation）

<a id="gaf7888bd31df37d449cde69bc693c244f"></a>

### `xen_domctl_assign_dt_device()`

```c
int xen_domctl_assign_dt_device ( int domid, char * dtdev_path )
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

将设备树描述的设备（Devicetree-described Device）分配给来宾域（Guest Domain）。

在 arm64 上，这主要用于能够充当总线主设备（Bus Masters）的设备，即支持 DMA 的设备。Xen 会在分配（Assignment）过程中配置输入输出内存管理单元（IOMMU）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 目标域标识符（Target Domain Identifier）。 |
| `dtdev_path` | 以 NULL 终止的设备树路径（Devicetree Path），指向该设备。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gad5f80dd7c0a7981f8c5c757b06993dc5"></a>

### `xen_domctl_bind_pt_irq()`

```c
int xen_domctl_bind_pt_irq ( int domid, uint32_t machine_irq, uint8_t irq_type, uint8_t bus, uint8_t device, uint8_t intx, uint8_t isa_irq, uint16_t spi )
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

将物理中断（Physical Interrupt）绑定到来宾域（Guest Domain）。

当前仅支持 PT_IRQ_TYPE_SPI。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 目标域标识符（Target Domain Identifier）。 |
| `machine_irq` | 要绑定的机器 IRQ 编号（Machine IRQ Number）。 |
| `irq_type` | Xen 直通中断类型（Passthrough IRQ type）。 |
| `bus` | PCI 直通模式使用的 PCI 总线号。 |
| `device` | PCI 直通模式使用的 PCI 设备号。 |
| `intx` | PCI 直通模式使用的 PCI INTx 中断线。 |
| `isa_irq` | ISA 直通模式使用的 ISA IRQ 编号。 |
| `spi` | 与 `PT_IRQ_TYPE_SPI` 配合使用的共享外设中断（SPI）编号。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 当前实现不支持 irq_type。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gad89ece398fc97a94c5c316066e2c29a5"></a>

### `xen_domctl_cacheflush()`

```c
int xen_domctl_cacheflush ( int domid, struct xen_domctl_cacheflush * cacheflush )
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

对来宾内存范围执行缓存清理和失效（Clean and Invalidate Caches）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 目标域标识符（Target Domain Identifier）。 |
| `cacheflush` | 缓存刷新请求参数（Cache-flush Request Parameters）。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga6d6b0c6d2baa1520322a595f0179cfa4"></a>

### `xen_domctl_createdomain()`

```c
int xen_domctl_createdomain ( int * domid, struct xen_domctl_createdomain * config )
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

创建新域（Domain）。

domid 是输入／输出参数（IN/OUT Parameter）。如果将其指定为无效值（0 或大于或等于 DOMID_FIRST_RESERVED），Xen 会自动分配一个标识符，并通过 domid 返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in,out] domid` | 域标识符请求与响应缓冲区（Domain Identifier Request and Response Buffer）。 |
| ` config` | 传给 Xen 的域配置（Domain Configuration）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | domid 或 config 为 NULL。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga4b7f6762c5a83b05501621b2a3c66fc3"></a>

### `xen_domctl_deassign_dt_device()`

```c
int xen_domctl_deassign_dt_device ( int domid, char * dtdev_path )
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

移除来宾域中由设备树描述的设备分配（Device Assignment）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 目标域标识符（Target Domain Identifier）。 |
| `dtdev_path` | 以 NULL 终止的设备树路径（Devicetree Path），指向该设备。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaba6a1f6e25ac6ee2a7b0d288ca4ab72d"></a>

### `xen_domctl_destroydomain()`

```c
int xen_domctl_destroydomain ( int domid)
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

销毁域（Domain）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 目标域标识符（Target Domain Identifier）。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga011ff7f30fa94479d4f1d5f7ed74b113"></a>

### `xen_domctl_get_paging_mempool_size()`

```c
int xen_domctl_get_paging_mempool_size ( int domid, uint64_t * size )
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

获取域的分页内存池大小（Paging Mempool Size）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` domid` | 目标域标识符（Target Domain Identifier）。 |
| `[out] size` | 用于接收分页内存池大小（Paging Mempool Size）的缓冲区，大小单位为字节。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga4848541359c3e13358dc39b42b3c142f"></a>

### `xen_domctl_getdomaininfo()`

```c
int xen_domctl_getdomaininfo ( int domid, xen_domctl_getdomaininfo_t * dom_info )
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

获取域（Domain）的概要信息（Summary Information）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` domid` | 要获取其信息的 Xen 域标识符（Domain ID）。 |
| `[out] dom_info` | 指向结构体的指针，用于存储获取的域信息（Domain Information）。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga9412b5a996e287dd588e65db373c5b59"></a>

### `xen_domctl_getvcpu()`

```c
int xen_domctl_getvcpu ( int domid, uint32_t vcpu, struct xen_domctl_getvcpuinfo * info )
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

查询域内某个虚拟 CPU（vCPU）的运行时信息（Runtime Information）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` domid` | 目标域标识符（Target Domain Identifier）。 |
| ` vcpu` | 要查询的虚拟 CPU 索引（vCPU Index）。 |
| `[out] info` | 用于接收虚拟 CPU 信息（vCPU Information）的缓冲区。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga9040a9ddca3406adc057960b0f423bcd"></a>

### `xen_domctl_getvcpucontext()`

```c
int xen_domctl_getvcpucontext ( int domid, int vcpu, vcpu_guest_context_t * ctxt )
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

获取域内虚拟 CPU（vCPU）的来宾上下文（Guest Context）。

- 注意（Attention）：仅在启用 Kconfig 选项 CONFIG_XEN_DOM0 时可用。参数（Parameters）：domid 为域标识符（Domain ID）；vcpu 为虚拟 CPU 标识符（Virtual CPU ID）；[out] ctxt 是指向 vcpu_guest_context_t 结构体的指针，用于存储虚拟 CPU 上下文（Virtual CPU Context）。返回（Returns）：成功时为 0，失败时为负 errno 值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` domid` | 域标识符（Domain ID）。 |
| ` vcpu` | 虚拟 CPU 标识符（Virtual CPU ID）。 |
| `[out] ctxt` | 指向 vcpu_guest_context_t 结构体的指针，用于存储虚拟 CPU 上下文（Virtual CPU Context）。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga2a34701f55250140576e8c71607801f8"></a>

### `xen_domctl_iomem_permission()`

```c
int xen_domctl_iomem_permission ( int domid, uint64_t first_mfn, uint64_t nr_mfns, uint8_t allow_access )
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

允许或拒绝域访问 I/O 内存（I/O-memory Access）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 目标域标识符（Target Domain Identifier）。 |
| `first_mfn` | 范围内的第一个机器页帧号（Machine Frame Number）。 |
| `nr_mfns` | 范围内的机器页帧数量（Number of Machine Frames）。 |
| `allow_access` | 设置为非零值以允许访问（Allow Access），设置为 0 以撤销访问权限（Revoke Access）。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gacbe8f22573487bcdb8612988da24b68e"></a>

### `xen_domctl_max_mem()`

```c
int xen_domctl_max_mem ( int domid, uint64_t max_memkb )
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

设置分配给域的最大内存（Maximum Memory）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 目标域标识符（Target Domain Identifier）。 |
| `max_memkb` | 最大内存（Maximum Memory），单位为 KiB。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga8f954e5a7d1cd633c6d819780bb6372b"></a>

### `xen_domctl_max_vcpus()`

```c
int xen_domctl_max_vcpus ( int domid, int max_vcpus )
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

设置域可使用的虚拟 CPU（vCPU）最大数量。

max_vcpus 必须与传给 XEN_DOMCTL_createdomain 的值一致。此超级调用（Hypercall）正处于移除过程中，将在 domain_create() 的失败处理路径改进后移除，但短期内仍需要用它分配虚拟 CPU（vCPUs）本身。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 目标域标识符（Target Domain Identifier）。 |
| `max_vcpus` | 要分配的 Xen 虚拟 CPU 最大数量（Maximum Number of vCPUs）。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gac945f3330b3b03112f3fa6fb49f42e50"></a>

### `xen_domctl_memory_mapping()`

```c
int xen_domctl_memory_mapping ( int domid, uint64_t first_gfn, uint64_t first_mfn, uint64_t nr_mfns, uint32_t add_mapping )
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

将机器内存范围（Machine-memory Range）映射到来宾页框范围（Guest Frame Range），或解除该映射。

如果 Xen 报告请求过大，实现会自动改用更小的分块（Chunks）重试操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 目标域标识符（Target Domain Identifier）。 |
| `first_gfn` | 目标范围内的第一个客户机页帧号（Guest Frame Number）。 |
| `first_mfn` | 源范围内的第一个机器页帧号（Machine Frame Number）。 |
| `nr_mfns` | 要处理的页帧数量（Number of Frames）。 |
| `add_mapping` | 设置为非零值以添加映射（Mapping），设置为 0 以移除映射。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaff200f6bfe2a31b536337f5bf668fee7"></a>

### `xen_domctl_pausedomain()`

```c
int xen_domctl_pausedomain ( int domid)
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

在 Xen 虚拟机监控器（Hypervisor）中暂停域（Domain）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 要暂停的域标识符（Domain ID）。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga50c40d73171240a047cf6e9b41898c99"></a>

### `xen_domctl_resumedomain()`

```c
int xen_domctl_resumedomain ( int domid)
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

恢复域（Resume a Domain）。

此函数恢复处于关闭状态（Shutdown State）的域的执行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 要恢复执行的域标识符（Domain ID）。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga7045c1f92142eceefe3e4c651708beae"></a>

### `xen_domctl_scheduler_op()`

```c
int xen_domctl_scheduler_op ( int domid, struct xen_domctl_scheduler_op * sched_op )
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

对指定域（Domain）执行调度器操作（Scheduler Operation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` domid` | 要对其执行调度器操作（Scheduler Operation）的域标识符。 |
| `[in,out] sched_op` | 指向 struct xen_domctl_scheduler_op 对象的指针，该对象定义要执行的具体调度器操作（Scheduler Operation）。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga8dee93295a86c5d7b586676a831e1047"></a>

### `xen_domctl_set_address_size()`

```c
int xen_domctl_set_address_size ( int domid, int addr_size )
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

设置域使用的地址大小（Address Size）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 目标域标识符（Target Domain Identifier）。 |
| `addr_size` | Xen 地址大小选择器（Address-size Selector）。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaa5bbda52cad0228ffacc42518fedfdff"></a>

### `xen_domctl_set_paging_mempool_size()`

```c
int xen_domctl_set_paging_mempool_size ( int domid, uint64_t size )
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

设置域的分页内存池大小（Paging Mempool Size）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 目标域标识符（Target Domain Identifier）。 |
| `size` | 新的分页内存池大小（Paging Mempool Size），单位为字节。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga66505a6d47e0c5ef3334043c668d6740"></a>

### `xen_domctl_setvcpucontext()`

```c
int xen_domctl_setvcpucontext ( int domid, int vcpu, vcpu_guest_context_t * ctxt )
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

设置域内虚拟 CPU（vCPU）的来宾上下文（Guest Context）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 域标识符（Domain ID）。 |
| `vcpu` | 虚拟 CPU 标识符（Virtual CPU ID）。 |
| `ctxt` | 指向虚拟 CPU 客户机上下文结构体（Virtual CPU Guest Context Structure）的指针。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gae29cc4d5d3ffcfe7e13a62030667c885"></a>

### `xen_domctl_unbind_pt_irq()`

```c
int xen_domctl_unbind_pt_irq ( int domid, const struct xen_domctl_pt_irq * irq )
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

解除物理中断（Physical Interrupt）与来宾域的绑定。

当前仅支持 PT_IRQ_TYPE_SPI。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 目标域标识符（Target Domain Identifier）。 |
| `irq` | 物理中断直通（Physical Interrupt Passthrough）描述符。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | irq 为 NULL。 |
| `-ENOTSUP` | 当前实现不支持 irq->irq_type。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga89be676e7f2ff66b4dc195e35e374083"></a>

### `xen_domctl_unpausedomain()`

```c
int xen_domctl_unpausedomain ( int domid)
```

```c
#include <zephyr/xen/dom0/domctl.h>
```

在 Xen 虚拟机监控器（Hypervisor）中取消域的暂停（Unpause）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 要解除暂停的域标识符（Domain ID）。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 15.5\_原页交叉引用（Cross References）

- [domctl.h](../api_file_secure_value_reference/P005_zephyr__xen__dom0__domctl.h_文件参考.md)
- [xen_domctl_pt_irq](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [CONFIG_XEN_DOM0](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN_DOM0)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P014_WebSocket的API。.md) · [返回大纲](大纲.md)
