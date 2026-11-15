---
id: learning.zephyr-docs.intercore_reference.api-216
title: IVSHMEM头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ivshmem_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第216章\_IVSHMEM头文件源码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ivshmem_8h_source.html)。读取日期：2026-10-14；以保存的latest网页为依据，HTML摘要见[来源记录](../SOURCES.md)。

## 216.1\_阅读说明与导航

> 译注：本组说明虚拟机间共享内存（Inter-VM Shared Memory，IVSHMEM）的公共接口、头文件及源码。先结合[门铃示例](../driver_samples/P067_IVSHMEM门铃示例.md)或[以太网示例](../driver_samples/P060_IVSHMEM以太网示例.md)理解数据与通知的关系，再查询各参数和返回值。

本组：[IVSHMEM共享内存接口](P214_IVSHMEM共享内存接口.md) · [IVSHMEM头文件参考](P215_IVSHMEM头文件参考.md) · [IVSHMEM头文件源码](P216_IVSHMEM头文件源码.md)。

下方保留官方Doxygen源码浏览页的全部代码、标识符和版权／许可注释，仅移除展示行号、还原不换行空格并清除行尾空白。网页本身省略了部分用于生成API说明的注释；这里不把展示代码冒充完整原始头文件。被省略的接口说明在本组参考页中翻译。

## 216.2\_官方源码展示

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__ivshmem_html_ga144506b762865c6bd451c09f6407fb86"></a>
<a id="agroup__ivshmem_html_ga42a6649e852d9b81f8729fb4297043e2"></a>
<a id="agroup__ivshmem_html_ga67dc8b24f863c3e9a8ac6a89753fd4c9"></a>
<a id="agroup__ivshmem_html_ga88aacb71bff0375c10fdb48e34b359fe"></a>
<a id="agroup__ivshmem_html_ga8b5175861401e5eb5d322f904172b963"></a>
<a id="agroup__ivshmem_html_ga940ffec4ae0380d774c05107afe41994"></a>
<a id="agroup__ivshmem_html_ga94673f449d111364cfade9192669a5a8"></a>
<a id="agroup__ivshmem_html_gaaa7e99f4844f270d1f1d2271b43d607c"></a>
<a id="agroup__ivshmem_html_gab2f0ccd5a2b8203a54ee5707b3afd6cc"></a>
<a id="agroup__ivshmem_html_gab4e02271f8b854c783c359aca240d20c"></a>
<a id="agroup__ivshmem_html_gaef043cbfbe0aa5061db57f9bbae02eca"></a>
<a id="agroup__ivshmem_html_gafee360f2c35abb9a203dd9f4838b8846"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="asignal_8h_html_a5d326f119f87d0facaa662520f8c322a"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructk__poll__signal_html"></a>

```c
/*
 * Copyright (c) 2020 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_VIRTUALIZATION_IVSHMEM_H_
#define ZEPHYR_INCLUDE_DRIVERS_VIRTUALIZATION_IVSHMEM_H_


#include <zephyr/types.h>
#include <stddef.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif


#define IVSHMEM_V2_PROTO_UNDEFINED      0x0000
#define IVSHMEM_V2_PROTO_NET            0x0001

typedef size_t (*ivshmem_get_mem_f)(const struct device *dev,
                                    uintptr_t *memmap);

typedef uint32_t (*ivshmem_get_id_f)(const struct device *dev);

typedef uint16_t (*ivshmem_get_vectors_f)(const struct device *dev);

typedef int (*ivshmem_int_peer_f)(const struct device *dev,
                                  uint32_t peer_id, uint16_t vector);

typedef int (*ivshmem_register_handler_f)(const struct device *dev,
                                          struct k_poll_signal *signal,
                                          uint16_t vector);

#ifdef CONFIG_IVSHMEM_V2

typedef size_t (*ivshmem_get_rw_mem_section_f)(const struct device *dev,
                                               uintptr_t *memmap);

typedef size_t (*ivshmem_get_output_mem_section_f)(const struct device *dev,
                                                   uint32_t peer_id,
                                                   uintptr_t *memmap);

typedef uint32_t (*ivshmem_get_state_f)(const struct device *dev,
                                        uint32_t peer_id);

typedef int (*ivshmem_set_state_f)(const struct device *dev,
                                   uint32_t state);

typedef uint32_t (*ivshmem_get_max_peers_f)(const struct device *dev);

typedef uint16_t (*ivshmem_get_protocol_f)(const struct device *dev);

typedef int (*ivshmem_enable_interrupts_f)(const struct device *dev,
                                           bool enable);

#endif /* CONFIG_IVSHMEM_V2 */

__subsystem struct ivshmem_driver_api {
        ivshmem_get_mem_f get_mem;
        ivshmem_get_id_f get_id;
        ivshmem_get_vectors_f get_vectors;
        ivshmem_int_peer_f int_peer;
        ivshmem_register_handler_f register_handler;
#ifdef CONFIG_IVSHMEM_V2
        ivshmem_get_rw_mem_section_f get_rw_mem_section;
        ivshmem_get_output_mem_section_f get_output_mem_section;
        ivshmem_get_state_f get_state;
        ivshmem_set_state_f set_state;
        ivshmem_get_max_peers_f get_max_peers;
        ivshmem_get_protocol_f get_protocol;
        ivshmem_enable_interrupts_f enable_interrupts;
#endif
};


__syscall size_t ivshmem_get_mem(const struct device *dev,
                                 uintptr_t *memmap);

static inline size_t z_impl_ivshmem_get_mem(const struct device *dev,
                                            uintptr_t *memmap)
{
        return DEVICE_API_GET(ivshmem, dev)->get_mem(dev, memmap);
}

__syscall uint32_t ivshmem_get_id(const struct device *dev);

static inline uint32_t z_impl_ivshmem_get_id(const struct device *dev)
{
        return DEVICE_API_GET(ivshmem, dev)->get_id(dev);
}

__syscall uint16_t ivshmem_get_vectors(const struct device *dev);

static inline uint16_t z_impl_ivshmem_get_vectors(const struct device *dev)
{
        return DEVICE_API_GET(ivshmem, dev)->get_vectors(dev);
}

__syscall int ivshmem_int_peer(const struct device *dev,
                               uint32_t peer_id, uint16_t vector);

static inline int z_impl_ivshmem_int_peer(const struct device *dev,
                                          uint32_t peer_id, uint16_t vector)
{
        return DEVICE_API_GET(ivshmem, dev)->int_peer(dev, peer_id, vector);
}

__syscall int ivshmem_register_handler(const struct device *dev,
                                       struct k_poll_signal *signal,
                                       uint16_t vector);

static inline int z_impl_ivshmem_register_handler(const struct device *dev,
                                                  struct k_poll_signal *signal,
                                                  uint16_t vector)
{
        return DEVICE_API_GET(ivshmem, dev)->register_handler(dev, signal, vector);
}

#if defined(CONFIG_IVSHMEM_V2) || defined(__DOXYGEN__)
__syscall size_t ivshmem_get_rw_mem_section(const struct device *dev,
                                            uintptr_t *memmap);

static inline size_t z_impl_ivshmem_get_rw_mem_section(const struct device *dev,
                                                       uintptr_t *memmap)
{
        return DEVICE_API_GET(ivshmem, dev)->get_rw_mem_section(dev, memmap);
}

__syscall size_t ivshmem_get_output_mem_section(const struct device *dev,
                                                uint32_t peer_id,
                                                uintptr_t *memmap);

static inline size_t z_impl_ivshmem_get_output_mem_section(const struct device *dev,
                                                           uint32_t peer_id,
                                                           uintptr_t *memmap)
{
        return DEVICE_API_GET(ivshmem, dev)->get_output_mem_section(dev, peer_id, memmap);
}

__syscall uint32_t ivshmem_get_state(const struct device *dev,
                                     uint32_t peer_id);

static inline uint32_t z_impl_ivshmem_get_state(const struct device *dev,
                                                uint32_t peer_id)
{
        return DEVICE_API_GET(ivshmem, dev)->get_state(dev, peer_id);
}

__syscall int ivshmem_set_state(const struct device *dev,
                                uint32_t state);

static inline int z_impl_ivshmem_set_state(const struct device *dev,
                                           uint32_t state)
{
        return DEVICE_API_GET(ivshmem, dev)->set_state(dev, state);
}

__syscall uint32_t ivshmem_get_max_peers(const struct device *dev);

static inline uint32_t z_impl_ivshmem_get_max_peers(const struct device *dev)
{
        return DEVICE_API_GET(ivshmem, dev)->get_max_peers(dev);
}

__syscall uint16_t ivshmem_get_protocol(const struct device *dev);

static inline uint16_t z_impl_ivshmem_get_protocol(const struct device *dev)
{
        return DEVICE_API_GET(ivshmem, dev)->get_protocol(dev);
}

__syscall int ivshmem_enable_interrupts(const struct device *dev,
                                        bool enable);

static inline int z_impl_ivshmem_enable_interrupts(const struct device *dev,
                                                   bool enable)
{
        return DEVICE_API_GET(ivshmem, dev)->enable_interrupts(dev, enable);
}

#endif /* CONFIG_IVSHMEM_V2 */

#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/ivshmem.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_VIRTUALIZATION_IVSHMEM_H_ */
```

## 216.3\_注释与条件说明

版权为2020年Intel Corporation；许可证标识为`Apache-2.0`，原署名保持不变。包含保护宏为`ZEPHYR_INCLUDE_DRIVERS_VIRTUALIZATION_IVSHMEM_H_`；`CONFIG_IVSHMEM_V2`控制v2回调类型和驱动结构成员，公共v2声明的展示条件另含`__DOXYGEN__`。因此文档能展示接口不代表当前固件已启用它。`z_impl_*`通过驱动API表转发调用；`extern "C"`用于C++调用方的C链接约定，末尾包含生成的系统调用头文件。

## 216.4\_源码跟踪与验证边界

本仓库[对应头文件](../../../include/zephyr/drivers/virtualization/ivshmem.h)、[驱动实现](../../../drivers/virtualization/virt_ivshmem.c)和[系统调用验证包装](../../../drivers/virtualization/virt_ivshmem_handlers.c)可用于源码跟踪；本仓库版本不自动等同于网页版本。本批译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/virtualization/ivshmem.h)、[官方驱动](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/virtualization/virt_ivshmem.c)和[官方包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/virtualization/virt_ivshmem_handlers.c)，摘要见[来源记录](../SOURCES.md)。main分支会变化，以上实现结论不能当作所有版本的接口保证。

项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。本文未安装、构建、运行虚拟机、配置共享内存或进行接线测量。

[上一章](P215_IVSHMEM头文件参考.md) · [返回大纲](大纲.md)
