---
id: learning.zephyr-docs.api-file-secure-value-reference.page-5
title: zephyr__xen__dom0__domctl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/domctl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_xen\_\_dom0\_\_domctl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/domctl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Xen Dom0的域控制操作（Domain Control Operations）。

<a id="details"></a>

```c
#include <xen/public/xen.h>
#include <xen/public/domctl.h>
#include <zephyr/xen/generic.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

Xen Dom0的域控制操作（Domain Control Operations）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_xen_5Fdomctl_5Fpt_5Firq"></a>

```c
struct xen_domctl_pt_irq
```

相关声明：[xen_domctl_pt_irq](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md)。

物理中断直通（Physical Interrupt Passthrough）描述符。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.2\_函数（Functions）

<a id="r_ga7045c1f92142eceefe3e4c651708beae"></a>

```c
int xen_domctl_scheduler_op (int domid, struct xen_domctl_scheduler_op *sched_op)
```

相关声明：[xen_domctl_scheduler_op](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga7045c1f92142eceefe3e4c651708beae)。

对指定域（Domain）执行调度器操作（Scheduler Operation）。

<a id="r_gaff200f6bfe2a31b536337f5bf668fee7"></a>

```c
int xen_domctl_pausedomain (int domid)
```

相关声明：[xen_domctl_pausedomain](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gaff200f6bfe2a31b536337f5bf668fee7)。

在 Xen 虚拟机监控器（Hypervisor）中暂停域（Domain）。

<a id="r_ga89be676e7f2ff66b4dc195e35e374083"></a>

```c
int xen_domctl_unpausedomain (int domid)
```

相关声明：[xen_domctl_unpausedomain](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga89be676e7f2ff66b4dc195e35e374083)。

在 Xen 虚拟机监控器（Hypervisor）中取消域的暂停（Unpause）。

<a id="r_ga50c40d73171240a047cf6e9b41898c99"></a>

```c
int xen_domctl_resumedomain (int domid)
```

相关声明：[xen_domctl_resumedomain](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga50c40d73171240a047cf6e9b41898c99)。

恢复域（Resume a Domain）。

<a id="r_ga9040a9ddca3406adc057960b0f423bcd"></a>

```c
int xen_domctl_getvcpucontext (int domid, int vcpu, vcpu_guest_context_t *ctxt)
```

相关声明：[xen_domctl_getvcpucontext](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga9040a9ddca3406adc057960b0f423bcd)。

获取域内虚拟 CPU（vCPU）的来宾上下文（Guest Context）。

<a id="r_ga66505a6d47e0c5ef3334043c668d6740"></a>

```c
int xen_domctl_setvcpucontext (int domid, int vcpu, vcpu_guest_context_t *ctxt)
```

相关声明：[xen_domctl_setvcpucontext](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga66505a6d47e0c5ef3334043c668d6740)。

设置域内虚拟 CPU（vCPU）的来宾上下文（Guest Context）。

<a id="r_ga4848541359c3e13358dc39b42b3c142f"></a>

```c
int xen_domctl_getdomaininfo (int domid, xen_domctl_getdomaininfo_t *dom_info)
```

相关声明：[xen_domctl_getdomaininfo](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga4848541359c3e13358dc39b42b3c142f)。

获取域（Domain）的概要信息（Summary Information）。

<a id="r_ga011ff7f30fa94479d4f1d5f7ed74b113"></a>

```c
int xen_domctl_get_paging_mempool_size (int domid, uint64_t *size)
```

相关声明：[xen_domctl_get_paging_mempool_size](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga011ff7f30fa94479d4f1d5f7ed74b113)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

获取域的分页内存池大小（Paging Mempool Size）。

<a id="r_gaa5bbda52cad0228ffacc42518fedfdff"></a>

```c
int xen_domctl_set_paging_mempool_size (int domid, uint64_t size)
```

相关声明：[xen_domctl_set_paging_mempool_size](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gaa5bbda52cad0228ffacc42518fedfdff)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置域的分页内存池大小（Paging Mempool Size）。

<a id="r_gacbe8f22573487bcdb8612988da24b68e"></a>

```c
int xen_domctl_max_mem (int domid, uint64_t max_memkb)
```

相关声明：[xen_domctl_max_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gacbe8f22573487bcdb8612988da24b68e)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置分配给域的最大内存（Maximum Memory）。

<a id="r_ga8dee93295a86c5d7b586676a831e1047"></a>

```c
int xen_domctl_set_address_size (int domid, int addr_size)
```

相关声明：[xen_domctl_set_address_size](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga8dee93295a86c5d7b586676a831e1047)。

设置域使用的地址大小（Address Size）。

<a id="r_ga2a34701f55250140576e8c71607801f8"></a>

```c
int xen_domctl_iomem_permission (int domid, uint64_t first_mfn, uint64_t nr_mfns, uint8_t allow_access)
```

相关声明：[xen_domctl_iomem_permission](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga2a34701f55250140576e8c71607801f8)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

允许或拒绝域访问 I/O 内存（I/O-memory Access）。

<a id="r_gac945f3330b3b03112f3fa6fb49f42e50"></a>

```c
int xen_domctl_memory_mapping (int domid, uint64_t first_gfn, uint64_t first_mfn, uint64_t nr_mfns, uint32_t add_mapping)
```

相关声明：[xen_domctl_memory_mapping](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gac945f3330b3b03112f3fa6fb49f42e50)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将机器内存范围（Machine-memory Range）映射到来宾页框范围（Guest Frame Range），或解除该映射。

<a id="r_gaf7888bd31df37d449cde69bc693c244f"></a>

```c
int xen_domctl_assign_dt_device (int domid, char *dtdev_path)
```

相关声明：[xen_domctl_assign_dt_device](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gaf7888bd31df37d449cde69bc693c244f)。

将设备树描述的设备（Devicetree-described Device）分配给来宾域（Guest Domain）。

<a id="r_ga4b7f6762c5a83b05501621b2a3c66fc3"></a>

```c
int xen_domctl_deassign_dt_device (int domid, char *dtdev_path)
```

相关声明：[xen_domctl_deassign_dt_device](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga4b7f6762c5a83b05501621b2a3c66fc3)。

移除来宾域中由设备树描述的设备分配（Device Assignment）。

<a id="r_gad5f80dd7c0a7981f8c5c757b06993dc5"></a>

```c
int xen_domctl_bind_pt_irq (int domid, uint32_t machine_irq, uint8_t irq_type, uint8_t bus, uint8_t device, uint8_t intx, uint8_t isa_irq, uint16_t spi)
```

相关声明：[xen_domctl_bind_pt_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gad5f80dd7c0a7981f8c5c757b06993dc5)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将物理中断（Physical Interrupt）绑定到来宾域（Guest Domain）。

<a id="r_gae29cc4d5d3ffcfe7e13a62030667c885"></a>

```c
int xen_domctl_unbind_pt_irq (int domid, const struct xen_domctl_pt_irq *irq)
```

相关声明：[xen_domctl_unbind_pt_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gae29cc4d5d3ffcfe7e13a62030667c885)、[xen_domctl_pt_irq](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md)。

解除物理中断（Physical Interrupt）与来宾域的绑定。

<a id="r_ga8f954e5a7d1cd633c6d819780bb6372b"></a>

```c
int xen_domctl_max_vcpus (int domid, int max_vcpus)
```

相关声明：[xen_domctl_max_vcpus](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga8f954e5a7d1cd633c6d819780bb6372b)。

设置域可使用的虚拟 CPU（vCPU）最大数量。

<a id="r_ga6d6b0c6d2baa1520322a595f0179cfa4"></a>

```c
int xen_domctl_createdomain (int *domid, struct xen_domctl_createdomain *config)
```

相关声明：[xen_domctl_createdomain](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga6d6b0c6d2baa1520322a595f0179cfa4)。

创建新域（Domain）。

<a id="r_gad89ece398fc97a94c5c316066e2c29a5"></a>

```c
int xen_domctl_cacheflush (int domid, struct xen_domctl_cacheflush *cacheflush)
```

相关声明：[xen_domctl_cacheflush](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gad89ece398fc97a94c5c316066e2c29a5)。

对来宾内存范围执行缓存清理和失效（Clean and Invalidate Caches）。

<a id="r_gaba6a1f6e25ac6ee2a7b0d288ca4ab72d"></a>

```c
int xen_domctl_destroydomain (int domid)
```

相关声明：[xen_domctl_destroydomain](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gaba6a1f6e25ac6ee2a7b0d288ca4ab72d)。

销毁域（Domain）。

<a id="r_ga9412b5a996e287dd588e65db373c5b59"></a>

```c
int xen_domctl_getvcpu (int domid, uint32_t vcpu, struct xen_domctl_getvcpuinfo *info)
```

相关声明：[xen_domctl_getvcpu](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga9412b5a996e287dd588e65db373c5b59)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

查询域内某个虚拟 CPU（vCPU）的运行时信息（Runtime Information）。


## 5.3\_原页交叉引用（Cross References）

- [zephyr/xen/generic.h](../api_source_supplement_reference/P078_generic.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P145_domctl.h_源码浏览.md)
- [xen_domctl_pt_irq](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md)
- [xen_domctl_scheduler_op](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga7045c1f92142eceefe3e4c651708beae)
- [xen_domctl_pausedomain](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gaff200f6bfe2a31b536337f5bf668fee7)
- [xen_domctl_unpausedomain](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga89be676e7f2ff66b4dc195e35e374083)
- [xen_domctl_resumedomain](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga50c40d73171240a047cf6e9b41898c99)
- [xen_domctl_getvcpucontext](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga9040a9ddca3406adc057960b0f423bcd)
- [xen_domctl_setvcpucontext](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga66505a6d47e0c5ef3334043c668d6740)
- [xen_domctl_getdomaininfo](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga4848541359c3e13358dc39b42b3c142f)
- [xen_domctl_get_paging_mempool_size](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga011ff7f30fa94479d4f1d5f7ed74b113)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [xen_domctl_set_paging_mempool_size](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gaa5bbda52cad0228ffacc42518fedfdff)
- [xen_domctl_max_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gacbe8f22573487bcdb8612988da24b68e)
- [xen_domctl_set_address_size](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga8dee93295a86c5d7b586676a831e1047)
- [xen_domctl_iomem_permission](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga2a34701f55250140576e8c71607801f8)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [xen_domctl_memory_mapping](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gac945f3330b3b03112f3fa6fb49f42e50)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [xen_domctl_assign_dt_device](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gaf7888bd31df37d449cde69bc693c244f)
- [xen_domctl_deassign_dt_device](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga4b7f6762c5a83b05501621b2a3c66fc3)
- [xen_domctl_bind_pt_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gad5f80dd7c0a7981f8c5c757b06993dc5)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [xen_domctl_unbind_pt_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gae29cc4d5d3ffcfe7e13a62030667c885)
- [xen_domctl_max_vcpus](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga8f954e5a7d1cd633c6d819780bb6372b)
- [xen_domctl_createdomain](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga6d6b0c6d2baa1520322a595f0179cfa4)
- [xen_domctl_cacheflush](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gad89ece398fc97a94c5c316066e2c29a5)
- [xen_domctl_destroydomain](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gaba6a1f6e25ac6ee2a7b0d288ca4ab72d)
- [xen_domctl_getvcpu](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga9412b5a996e287dd588e65db373c5b59)

<a id="header-details"></a>

---

[上一章](P004_zephyr__drivers__firmware__scmi__clk.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__drivers__regulator__max20362.h_文件参考.md)
