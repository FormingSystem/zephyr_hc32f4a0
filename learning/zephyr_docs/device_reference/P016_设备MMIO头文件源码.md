---
id: learning.zephyr-docs.device-reference.page-16
title: 设备MMIO头文件源码
kind: reference
status: maintained
domains: [zephyr, device, mmio, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/device__mmio_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_设备MMIO头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/device__mmio_8h_source.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。原网页省略了用于生成接口文档的部分注释，因此原行号会跳跃；这里的“全部可见代码”不等于包含所有文档注释的原始文件。接口说明、参数与返回值见[对应头文件参考](P015_设备MMIO头文件参考.md)及[本册大纲](大纲.md)。

## 16.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
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
<a id="l00058"></a>
<a id="l00059"></a>
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
<a id="l00096"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00128"></a>
<a id="foldopen00129"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00186"></a>
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
<a id="l00268"></a>
<a id="l00269"></a>
<a id="foldopen00279"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="foldopen00304"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00323"></a>
<a id="foldopen00324"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00358"></a>
<a id="l00368"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="foldopen00420"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="foldopen00501"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="foldopen00542"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00571"></a>
<a id="foldopen00572"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00602"></a>
<a id="foldopen00603"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00611"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00647"></a>
<a id="foldopen00648"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00674"></a>
<a id="l00675"></a>
<a id="foldopen00676"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00681"></a>
<a id="l00682"></a>
<a id="l00683"></a>
<a id="l00698"></a>
<a id="foldopen00699"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="l00705"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00752"></a>
<a id="foldopen00753"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="l00756"></a>
<a id="l00757"></a>
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00771"></a>
<a id="foldopen00772"></a>
<a id="l00772"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="agroup__device-mmio_html_ga16070be695cec4ebc01915a3dbc1adf8"></a>
<a id="agroup__device-mmio_html_ga6b4a9841a5176104e1b63f7475d3d2a2"></a>
<a id="agroup__kernel__memory__management_html_ga36c4d2ede2f91490bc20ec399df663be"></a>
<a id="agroup__kernel__memory__management_html_gab9ea94b7155e276f0b653bc1a081866e"></a>
<a id="agroup__kernel__mm__internal__apis_html_gaa2c52222198f4c7362c183e1397a4e5c"></a>
<a id="agroup__kernel__mm__internal__apis_html_gae713c4eb253302d06f758f87503cf5dd"></a>
<a id="agroup__mm__drv__apis_html_gaabbc2184a44f8c5c8cd98bf09a2cdc0f"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>
<a id="agroup__sys__io__apis_html_ga7bcfa789a44940bccc5b9b98642744b0"></a>
<a id="amm_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="asections_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="asys_2sys__io_8h_html"></a>
<a id="asystem__mm_8h_html"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright (c) 2020 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_SYS_DEVICE_MMIO_H
#define ZEPHYR_INCLUDE_SYS_DEVICE_MMIO_H

#include <zephyr/toolchain.h>
#include <zephyr/linker/sections.h>


/* Storing MMIO addresses in RAM is a system-wide decision based on
 * configuration. This is just used to simplify some other definitions.
 *
 * If we have an MMU enabled, all physical MMIO regions must be mapped into
 * the kernel's virtual address space at runtime, this is a hard requirement.
 *
 * If we have PCIE enabled, this does mean that non-PCIE drivers may waste
 * a bit of RAM, but systems with PCI express are not RAM constrained.
 */
#if defined(CONFIG_MMU) || defined(CONFIG_PCIE) || defined(CONFIG_EXTERNAL_ADDRESS_TRANSLATION)
#define DEVICE_MMIO_IS_IN_RAM
#endif

#if defined(CONFIG_EXTERNAL_ADDRESS_TRANSLATION)
#include <zephyr/drivers/mm/system_mm.h>
#endif

#ifndef _ASMLANGUAGE
#include <stdint.h>
#include <stddef.h>
#include <zephyr/kernel/mm.h>
#include <zephyr/sys/sys_io.h>

#ifdef DEVICE_MMIO_IS_IN_RAM
/* Store the physical address and size from DTS, we'll memory
 * map into the virtual address space at runtime. This is not applicable
 * to PCIe devices, which must query the bus for BAR information.
 */
struct z_device_mmio_rom {
        uintptr_t phys_addr;

        size_t size;
};

#define Z_DEVICE_MMIO_ROM_INITIALIZER(node_id) \
        { \
                .phys_addr = DT_REG_ADDR(node_id), \
                .size = DT_REG_SIZE(node_id) \
        }

#define Z_DEVICE_MMIO_NAMED_ROM_INITIALIZER(name, node_id) \
        { \
                .phys_addr = DT_REG_ADDR_BY_NAME(node_id, name), \
                .size = DT_REG_SIZE_BY_NAME(node_id, name) \
        }

__boot_func
static inline void device_map(mm_reg_t *virt_addr, uintptr_t phys_addr,
                              size_t size, uint32_t flags)
{
#ifdef CONFIG_MMU
        /* Pass along flags and add that we want supervisor mode
         * read-write access.
         */
        if (IS_ENABLED(CONFIG_KERNEL_DIRECT_MAP)) {
                flags |= K_MEM_DIRECT_MAP;
        }
        k_mem_map_phys_bare((uint8_t **)virt_addr, phys_addr, size,
                            flags | K_MEM_PERM_RW);
#else
        ARG_UNUSED(size);
        ARG_UNUSED(flags);
#ifdef CONFIG_EXTERNAL_ADDRESS_TRANSLATION
        sys_mm_drv_page_phys_get((void *) phys_addr, virt_addr);
#else
        *virt_addr = phys_addr;
#endif /* CONFIG_EXTERNAL_ADDRESS_TRANSLATION */
#endif /* CONFIG_MMU */
}

__boot_func
static inline void device_unmap(mm_reg_t virt_addr, size_t size)
{
#ifdef CONFIG_MMU
        k_mem_unmap_phys_bare((uint8_t *)virt_addr, size);
#else
        ARG_UNUSED(virt_addr);
        ARG_UNUSED(size);
#endif /* CONFIG_MMU */
}
#else
/* No MMU or PCIe. Just store the address from DTS and treat as a linear
 * address
 */
struct z_device_mmio_rom {
        mm_reg_t addr;
};

#define Z_DEVICE_MMIO_ROM_INITIALIZER(node_id) \
        { \
                .addr = (mm_reg_t)DT_REG_ADDR_U64(node_id) \
        }

#define Z_DEVICE_MMIO_NAMED_ROM_INITIALIZER(name, node_id) \
        { \
                .addr = (mm_reg_t)DT_REG_ADDR_BY_NAME_U64(node_id, name) \
        }

__boot_func
static inline void device_map(mm_reg_t *virt_addr, uintptr_t phys_addr,
                              size_t size, uint32_t flags)
{
        ARG_UNUSED(size);
        ARG_UNUSED(flags);
        *virt_addr = phys_addr;
}

__boot_func
static inline void device_unmap(mm_reg_t virt_addr, size_t size)
{
        ARG_UNUSED(virt_addr);
        ARG_UNUSED(size);
}

#endif /* DEVICE_MMIO_IS_IN_RAM */
#endif /* !_ASMLANGUAGE */


#ifdef DEVICE_MMIO_IS_IN_RAM
#define DEVICE_MMIO_RAM                 mm_reg_t _mmio
#else
#define DEVICE_MMIO_RAM
#endif

#ifdef DEVICE_MMIO_IS_IN_RAM
#define DEVICE_MMIO_RAM_PTR(device)     (mm_reg_t *)((device)->data)
#endif /* DEVICE_MMIO_IS_IN_RAM */

#define DEVICE_MMIO_ROM         struct z_device_mmio_rom _mmio

#define DEVICE_MMIO_ROM_PTR(dev) \
        ((struct z_device_mmio_rom *)((dev)->config))

#define DEVICE_MMIO_ROM_INIT(node_id) \
        ._mmio = Z_DEVICE_MMIO_ROM_INITIALIZER(node_id)

#ifdef DEVICE_MMIO_IS_IN_RAM
#define DEVICE_MMIO_MAP(dev, flags) \
        device_map(DEVICE_MMIO_RAM_PTR(dev), \
                   DEVICE_MMIO_ROM_PTR(dev)->phys_addr, \
                   DEVICE_MMIO_ROM_PTR(dev)->size, \
                   (flags))
#else
#define DEVICE_MMIO_MAP(dev, flags) do { } while (false)
#endif

#ifdef DEVICE_MMIO_IS_IN_RAM
#define DEVICE_MMIO_GET(dev)    (*DEVICE_MMIO_RAM_PTR(dev))
#else
#define DEVICE_MMIO_GET(dev)    (DEVICE_MMIO_ROM_PTR(dev)->addr)
#endif


#ifdef DEVICE_MMIO_IS_IN_RAM
#define DEVICE_MMIO_NAMED_RAM(name)     mm_reg_t name
#else
#define DEVICE_MMIO_NAMED_RAM(name)
#endif /* DEVICE_MMIO_IS_IN_RAM */

#ifdef DEVICE_MMIO_IS_IN_RAM
#define DEVICE_MMIO_NAMED_RAM_PTR(dev, name) \
                (&(DEV_DATA(dev)->name))
#endif /* DEVICE_MMIO_IS_IN_RAM */

#define DEVICE_MMIO_NAMED_ROM(name) struct z_device_mmio_rom name

#define DEVICE_MMIO_NAMED_ROM_PTR(dev, name) (&(DEV_CFG(dev)->name))

#define DEVICE_MMIO_NAMED_ROM_INIT(name, node_id) \
        .name = Z_DEVICE_MMIO_ROM_INITIALIZER(node_id)

#define DEVICE_MMIO_NAMED_ROM_INIT_BY_NAME(name, node_id) \
        .name = Z_DEVICE_MMIO_NAMED_ROM_INITIALIZER(name, node_id)

#ifdef DEVICE_MMIO_IS_IN_RAM
#define DEVICE_MMIO_NAMED_MAP(dev, name, flags) \
        device_map(DEVICE_MMIO_NAMED_RAM_PTR((dev), name), \
                   (DEVICE_MMIO_NAMED_ROM_PTR((dev), name)->phys_addr), \
                   (DEVICE_MMIO_NAMED_ROM_PTR((dev), name)->size), \
                   (flags))
#else
#define DEVICE_MMIO_NAMED_MAP(dev, name, flags) do { } while (false)
#endif

#ifdef DEVICE_MMIO_IS_IN_RAM
#define DEVICE_MMIO_NAMED_GET(dev, name) \
                (*DEVICE_MMIO_NAMED_RAM_PTR((dev), name))
#else
#define DEVICE_MMIO_NAMED_GET(dev, name) \
                ((DEVICE_MMIO_NAMED_ROM_PTR((dev), name))->addr)
#endif /* DEVICE_MMIO_IS_IN_RAM */



 #define Z_TOPLEVEL_ROM_NAME(name) _CONCAT(z_mmio_rom__, name)
 #define Z_TOPLEVEL_RAM_NAME(name) _CONCAT(z_mmio_ram__, name)

#ifdef DEVICE_MMIO_IS_IN_RAM
#define DEVICE_MMIO_TOPLEVEL(name, node_id) \
        \
        mm_reg_t Z_TOPLEVEL_RAM_NAME(name); \
        \
        const struct z_device_mmio_rom Z_TOPLEVEL_ROM_NAME(name) = \
                Z_DEVICE_MMIO_ROM_INITIALIZER(node_id)
#else
#define DEVICE_MMIO_TOPLEVEL(name, node_id) \
        \
        const struct z_device_mmio_rom Z_TOPLEVEL_ROM_NAME(name) = \
                Z_DEVICE_MMIO_ROM_INITIALIZER(node_id)
#endif /* DEVICE_MMIO_IS_IN_RAM */


#ifdef DEVICE_MMIO_IS_IN_RAM
#define DEVICE_MMIO_TOPLEVEL_DECLARE(name) \
        extern mm_reg_t Z_TOPLEVEL_RAM_NAME(name); \
        extern const struct z_device_mmio_rom Z_TOPLEVEL_ROM_NAME(name)
#else
#define DEVICE_MMIO_TOPLEVEL_DECLARE(name) \
        extern const struct z_device_mmio_rom Z_TOPLEVEL_ROM_NAME(name)
#endif /* DEVICE_MMIO_IS_IN_RAM */

#ifdef DEVICE_MMIO_IS_IN_RAM
#define DEVICE_MMIO_TOPLEVEL_STATIC(name, node_id) \
        \
        static mm_reg_t Z_TOPLEVEL_RAM_NAME(name); \
        \
        static const struct z_device_mmio_rom Z_TOPLEVEL_ROM_NAME(name) = \
                Z_DEVICE_MMIO_ROM_INITIALIZER(node_id)
#else
#define DEVICE_MMIO_TOPLEVEL_STATIC(name, node_id) \
        \
        static const struct z_device_mmio_rom Z_TOPLEVEL_ROM_NAME(name) = \
                Z_DEVICE_MMIO_ROM_INITIALIZER(node_id)
#endif /* DEVICE_MMIO_IS_IN_RAM */

#ifdef DEVICE_MMIO_IS_IN_RAM
#define DEVICE_MMIO_TOPLEVEL_RAM_PTR(name) &Z_TOPLEVEL_RAM_NAME(name)
#endif /* DEVICE_MMIO_IS_IN_RAM */

#define DEVICE_MMIO_TOPLEVEL_ROM_PTR(name) &Z_TOPLEVEL_ROM_NAME(name)

#ifdef DEVICE_MMIO_IS_IN_RAM
#define DEVICE_MMIO_TOPLEVEL_MAP(name, flags) \
        device_map(&Z_TOPLEVEL_RAM_NAME(name), \
                   Z_TOPLEVEL_ROM_NAME(name).phys_addr, \
                   Z_TOPLEVEL_ROM_NAME(name).size, (flags))
#else
#define DEVICE_MMIO_TOPLEVEL_MAP(name, flags) do { } while (false)
#endif

#ifdef DEVICE_MMIO_IS_IN_RAM
#define DEVICE_MMIO_TOPLEVEL_GET(name)  \
                ((mm_reg_t)Z_TOPLEVEL_RAM_NAME(name))
#else
#define DEVICE_MMIO_TOPLEVEL_GET(name)  \
                ((mm_reg_t)Z_TOPLEVEL_ROM_NAME(name).addr)
#endif

#endif /* ZEPHYR_INCLUDE_SYS_DEVICE_MMIO_H */
```

## 16.2\_可见注释译文（Comments）

1. 版权为2020年Intel Corporation，许可证为Apache-2.0；法律署名保持原样。

2. 是否将MMIO地址保存在RAM，是由配置决定的全系统选择，这里用于简化其他定义。启用MMU时，必须在运行时把所有物理MMIO区域映射到内核虚拟地址空间，这是硬性要求。启用PCIe时，非PCIe驱动可能额外占用少量RAM，但原文认为具有PCI Express的系统通常不受RAM容量约束。

3. 保存来自DTS的物理地址和大小，以便在运行时映射到虚拟地址空间。这不适用于PCIe设备，后者必须查询总线以取得基地址寄存器（Base Address Register，BAR）信息。

4. 转发flags，并增加监督者模式读写访问要求。

5. 结束CONFIG_EXTERNAL_ADDRESS_TRANSLATION条件分支。

6. 结束CONFIG_MMU条件分支。

7. 结束CONFIG_MMU条件分支。

8. 没有MMU或PCIe时，直接保存DTS提供的地址，并把它作为线性地址。

9. 结束DEVICE_MMIO_IS_IN_RAM条件分支。

10. 结束非汇编语言模式（!_ASMLANGUAGE）条件块。

11. 结束DEVICE_MMIO_IS_IN_RAM条件分支。

12. 结束DEVICE_MMIO_IS_IN_RAM条件分支。

13. 结束DEVICE_MMIO_IS_IN_RAM条件分支。

14. 结束DEVICE_MMIO_IS_IN_RAM条件分支。

15. 结束DEVICE_MMIO_IS_IN_RAM条件分支。

16. 结束DEVICE_MMIO_IS_IN_RAM条件分支。

17. 结束DEVICE_MMIO_IS_IN_RAM条件分支。

18. 结束DEVICE_MMIO_IS_IN_RAM条件分支。

19. 结束ZEPHYR_INCLUDE_SYS_DEVICE_MMIO_H头文件包含保护（Header Include Guard）。

## 16.3\_源码跟踪译注

> 译注——存储选择：DEVICE_MMIO_IS_IN_RAM由MMU、PCIe或外部地址转换配置任一启用决定；需要运行时地址时，ROM保存phys_addr与size，RAM保存可访问地址，否则ROM直接保存addr。这里选择的是地址元数据的存储，不会将MMIO寄存器内容搬入RAM。

> 译注——映射路径：MMU分支调用k_mem_map_phys_bare；无MMU的外部转换分支调用sys_mm_drv_page_phys_get且不检查返回值，其他分支直接赋值。device_unmap在无MMU时为空操作，也不会清除调用者保存的地址。接口名称、权限转发与外部查询方向的区别见[管理概述](P011_设备MMIO管理概述.md)。

> 译注——布局与命名：单区域指针辅助宏直接转换dev->data／config起始位置，要求MMIO成员位于首部；命名区域通过DEV_DATA／DEV_CFG取得具体类型后访问指定成员，允许多个区域。NAMED_ROM_INIT的name只命名C成员，BY_NAME版本才按reg-names选项定位；两者不能混用。

> 译注——PCIe与顶层：当前单区域、命名区域及顶层MAP宏都不执行PCI探测；需要先取得PCIe BAR信息，再按实际路径调用device_map。TOPLEVEL与STATIC定义的链接可见性不同，DECLARE不能把另一个文件的static对象变成可外部访问对象。

仓库相对定位：[include/zephyr/sys/device_mmio.h](../../../include/zephyr/sys/device_mmio.h)；本次核对的[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/device_mmio.h)摘要见[来源记录](../SOURCES.md)。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致；不能把这种一致性推广到以后滚动更新的main。

本批未构建、烧录、擦写或实板运行；代码阅读和文档核验不代表硬件操作通过。

## 16.4\_原页交叉引用（Cross References）

- [查看此文件参考说明](P015_设备MMIO头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zephyr/linker/sections.h](https://docs.zephyrproject.org/latest/doxygen/html/sections_8h.html)
- [zephyr/drivers/mm/system_mm.h](https://docs.zephyrproject.org/latest/doxygen/html/system__mm_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/kernel/mm.h](https://docs.zephyrproject.org/latest/doxygen/html/mm_8h.html)
- [zephyr/sys/sys_io.h](P021_系统IO头文件参考.md)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [device_map](P011_设备MMIO管理概述.md#ga6b4a9841a5176104e1b63f7475d3d2a2)
- [mm_reg_t](P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)
- [K_MEM_DIRECT_MAP](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#ga36c4d2ede2f91490bc20ec399df663be)
- [k_mem_map_phys_bare](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#gaa2c52222198f4c7362c183e1397a4e5c)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [K_MEM_PERM_RW](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__memory__management.html#gab9ea94b7155e276f0b653bc1a081866e)
- [sys_mm_drv_page_phys_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__apis.html#gaabbc2184a44f8c5c8cd98bf09a2cdc0f)
- [device_unmap](P011_设备MMIO管理概述.md#ga16070be695cec4ebc01915a3dbc1adf8)
- [k_mem_unmap_phys_bare](https://docs.zephyrproject.org/latest/doxygen/html/group__kernel__mm__internal__apis.html#gae713c4eb253302d06f758f87503cf5dd)

---

[上一章](P015_设备MMIO头文件参考.md) · [返回大纲](大纲.md) · [下一章](P017_系统IO公共接口.md)
