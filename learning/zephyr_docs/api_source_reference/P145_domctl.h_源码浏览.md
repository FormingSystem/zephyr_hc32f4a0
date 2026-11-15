---
id: learning.zephyr-docs.api-source-reference.page-145
title: domctl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/domctl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第145章\_domctl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/domctl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/domctl_8h.html)。

## 145.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00029"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="foldopen00230"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="ageneric_8h_html"></a>
<a id="agroup__xen__dom0__domain__control_html_ga011ff7f30fa94479d4f1d5f7ed74b113"></a>
<a id="agroup__xen__dom0__domain__control_html_ga2a34701f55250140576e8c71607801f8"></a>
<a id="agroup__xen__dom0__domain__control_html_ga4848541359c3e13358dc39b42b3c142f"></a>
<a id="agroup__xen__dom0__domain__control_html_ga4b7f6762c5a83b05501621b2a3c66fc3"></a>
<a id="agroup__xen__dom0__domain__control_html_ga50c40d73171240a047cf6e9b41898c99"></a>
<a id="agroup__xen__dom0__domain__control_html_ga66505a6d47e0c5ef3334043c668d6740"></a>
<a id="agroup__xen__dom0__domain__control_html_ga6d6b0c6d2baa1520322a595f0179cfa4"></a>
<a id="agroup__xen__dom0__domain__control_html_ga7045c1f92142eceefe3e4c651708beae"></a>
<a id="agroup__xen__dom0__domain__control_html_ga89be676e7f2ff66b4dc195e35e374083"></a>
<a id="agroup__xen__dom0__domain__control_html_ga8dee93295a86c5d7b586676a831e1047"></a>
<a id="agroup__xen__dom0__domain__control_html_ga8f954e5a7d1cd633c6d819780bb6372b"></a>
<a id="agroup__xen__dom0__domain__control_html_ga9040a9ddca3406adc057960b0f423bcd"></a>
<a id="agroup__xen__dom0__domain__control_html_ga9412b5a996e287dd588e65db373c5b59"></a>
<a id="agroup__xen__dom0__domain__control_html_gaa5bbda52cad0228ffacc42518fedfdff"></a>
<a id="agroup__xen__dom0__domain__control_html_gaba6a1f6e25ac6ee2a7b0d288ca4ab72d"></a>
<a id="agroup__xen__dom0__domain__control_html_gac945f3330b3b03112f3fa6fb49f42e50"></a>
<a id="agroup__xen__dom0__domain__control_html_gacbe8f22573487bcdb8612988da24b68e"></a>
<a id="agroup__xen__dom0__domain__control_html_gad5f80dd7c0a7981f8c5c757b06993dc5"></a>
<a id="agroup__xen__dom0__domain__control_html_gad89ece398fc97a94c5c316066e2c29a5"></a>
<a id="agroup__xen__dom0__domain__control_html_gae29cc4d5d3ffcfe7e13a62030667c885"></a>
<a id="agroup__xen__dom0__domain__control_html_gaf7888bd31df37d449cde69bc693c244f"></a>
<a id="agroup__xen__dom0__domain__control_html_gaff200f6bfe2a31b536337f5bf668fee7"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructxen__domctl__pt__irq_html"></a>
<a id="astructxen__domctl__pt__irq_html_a22a173359bdeacec66c8b26208004a43"></a>
<a id="astructxen__domctl__pt__irq_html_a4aa75c8809786e3bec6604e8bf6f7ff2"></a>
<a id="astructxen__domctl__pt__irq_html_a56fa5e12491dbc3b262c93a8773a6339"></a>
<a id="astructxen__domctl__pt__irq_html_a791e52092d506100c8fcb1b7f206e305"></a>
<a id="astructxen__domctl__pt__irq_html_a83da71ec34e53945eeed31b289b87822"></a>
<a id="astructxen__domctl__pt__irq_html_aaf73e967e9436059327c368df28c1436"></a>
<a id="astructxen__domctl__pt__irq_html_ad30d0377c24cb436398c1038116a2640"></a>

```c
/* SPDX-License-Identifier: Apache-2.0 */
/*
 * Copyright (c) 2023 EPAM Systems
 *
 */


#ifndef ZEPHYR_INCLUDE_XEN_DOM0_DOMCTL_H_
#define ZEPHYR_INCLUDE_XEN_DOM0_DOMCTL_H_

#include <xen/public/xen.h>
#include <xen/public/domctl.h>

#include <zephyr/xen/generic.h>

#include <zephyr/kernel.h>


int xen_domctl_scheduler_op(int domid, struct xen_domctl_scheduler_op *sched_op);

int xen_domctl_pausedomain(int domid);

int xen_domctl_unpausedomain(int domid);

int xen_domctl_resumedomain(int domid);

int xen_domctl_getvcpucontext(int domid, int vcpu, vcpu_guest_context_t *ctxt);

int xen_domctl_setvcpucontext(int domid, int vcpu, vcpu_guest_context_t *ctxt);

int xen_domctl_getdomaininfo(int domid, xen_domctl_getdomaininfo_t *dom_info);

int xen_domctl_get_paging_mempool_size(int domid, uint64_t *size);

int xen_domctl_set_paging_mempool_size(int domid, uint64_t size);

int xen_domctl_max_mem(int domid, uint64_t max_memkb);

int xen_domctl_set_address_size(int domid, int addr_size);

int xen_domctl_iomem_permission(int domid, uint64_t first_mfn,
                                uint64_t nr_mfns, uint8_t allow_access);

int xen_domctl_memory_mapping(int domid, uint64_t first_gfn, uint64_t first_mfn,
                              uint64_t nr_mfns, uint32_t add_mapping);

int xen_domctl_assign_dt_device(int domid, char *dtdev_path);

int xen_domctl_deassign_dt_device(int domid, char *dtdev_path);

struct xen_domctl_pt_irq {
        uint32_t machine_irq;
        uint8_t irq_type;
        uint8_t bus;
        uint8_t device;
        uint8_t intx;
        uint8_t isa_irq;
        uint16_t spi;
};

int xen_domctl_bind_pt_irq(int domid, uint32_t machine_irq, uint8_t irq_type, uint8_t bus,
                           uint8_t device, uint8_t intx, uint8_t isa_irq, uint16_t spi);

int xen_domctl_unbind_pt_irq(int domid, const struct xen_domctl_pt_irq *irq);

int xen_domctl_max_vcpus(int domid, int max_vcpus);

int xen_domctl_createdomain(int *domid, struct xen_domctl_createdomain *config);

int xen_domctl_cacheflush(int domid, struct xen_domctl_cacheflush *cacheflush);

int xen_domctl_destroydomain(int domid);

int xen_domctl_getvcpu(int domid, uint32_t vcpu, struct xen_domctl_getvcpuinfo *info);


#endif /* ZEPHYR_INCLUDE_XEN_DOM0_DOMCTL_H_ */
```

## 145.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 2 行

版权（Copyright）：© 2023 EPAM Systems。

### 注释 3：原第 357 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_XEN_DOM0_DOMCTL_H_`。

## 145.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/domctl_8h.html)
- [zephyr/xen/generic.h](https://docs.zephyrproject.org/latest/doxygen/html/generic_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [xen_domctl_scheduler_op](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga7045c1f92142eceefe3e4c651708beae)
- [xen_domctl_pausedomain](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gaff200f6bfe2a31b536337f5bf668fee7)
- [xen_domctl_unpausedomain](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga89be676e7f2ff66b4dc195e35e374083)
- [xen_domctl_resumedomain](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga50c40d73171240a047cf6e9b41898c99)
- [xen_domctl_getvcpucontext](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga9040a9ddca3406adc057960b0f423bcd)
- [xen_domctl_setvcpucontext](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga66505a6d47e0c5ef3334043c668d6740)
- [xen_domctl_getdomaininfo](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga4848541359c3e13358dc39b42b3c142f)
- [xen_domctl_get_paging_mempool_size](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga011ff7f30fa94479d4f1d5f7ed74b113)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [xen_domctl_set_paging_mempool_size](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gaa5bbda52cad0228ffacc42518fedfdff)
- [xen_domctl_max_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gacbe8f22573487bcdb8612988da24b68e)
- [xen_domctl_set_address_size](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga8dee93295a86c5d7b586676a831e1047)
- [xen_domctl_iomem_permission](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga2a34701f55250140576e8c71607801f8)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [xen_domctl_memory_mapping](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gac945f3330b3b03112f3fa6fb49f42e50)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [xen_domctl_assign_dt_device](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gaf7888bd31df37d449cde69bc693c244f)
- [xen_domctl_deassign_dt_device](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga4b7f6762c5a83b05501621b2a3c66fc3)
- [xen_domctl_pt_irq](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md)
- [machine_irq](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md#ad30d0377c24cb436398c1038116a2640)
- [irq_type](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md#a22a173359bdeacec66c8b26208004a43)
- [bus](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md#a56fa5e12491dbc3b262c93a8773a6339)
- [device](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md#a791e52092d506100c8fcb1b7f206e305)
- [intx](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md#a83da71ec34e53945eeed31b289b87822)
- [isa_irq](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md#a4aa75c8809786e3bec6604e8bf6f7ff2)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [spi](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md#aaf73e967e9436059327c368df28c1436)
- [xen_domctl_bind_pt_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gad5f80dd7c0a7981f8c5c757b06993dc5)
- [device](../device_reference/P002_设备对象结构.md)
- [xen_domctl_unbind_pt_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gae29cc4d5d3ffcfe7e13a62030667c885)
- [xen_domctl_max_vcpus](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga8f954e5a7d1cd633c6d819780bb6372b)
- [xen_domctl_createdomain](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga6d6b0c6d2baa1520322a595f0179cfa4)
- [xen_domctl_cacheflush](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gad89ece398fc97a94c5c316066e2c29a5)
- [xen_domctl_destroydomain](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#gaba6a1f6e25ac6ee2a7b0d288ca4ab72d)
- [xen_domctl_getvcpu](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga9412b5a996e287dd588e65db373c5b59)
- [generic.h](https://docs.zephyrproject.org/latest/doxygen/html/generic_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [xen_domctl_pt_irq::irq_type](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md#a22a173359bdeacec66c8b26208004a43)
- [xen_domctl_pt_irq::isa_irq](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md#a4aa75c8809786e3bec6604e8bf6f7ff2)
- [xen_domctl_pt_irq::bus](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md#a56fa5e12491dbc3b262c93a8773a6339)
- [xen_domctl_pt_irq::device](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md#a791e52092d506100c8fcb1b7f206e305)
- [xen_domctl_pt_irq::intx](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md#a83da71ec34e53945eeed31b289b87822)
- [xen_domctl_pt_irq::spi](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md#aaf73e967e9436059327c368df28c1436)
- [xen_domctl_pt_irq::machine_irq](../platform_security_model_reference/P075_xen_domctl_pt_irq_结构体.md#ad30d0377c24cb436398c1038116a2640)

---

[上一章](P144_dns_sd.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P146_dplpmtud.h_源码浏览.md)
