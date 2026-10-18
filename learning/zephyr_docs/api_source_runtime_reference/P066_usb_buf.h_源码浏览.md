---
id: learning.zephyr-docs.api-source-runtime-reference.page-66
title: usb_buf.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__buf_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_usb\_buf.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usb__buf_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/usb__buf_8h.html)。

## 66.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00026"></a>
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
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="foldopen00084"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00095"></a>
<a id="l00096"></a>
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
<a id="l00117"></a>
<a id="foldopen00132"></a>
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
<a id="l00143"></a>
<a id="l00144"></a>
<a id="foldopen00159"></a>
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
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="foldopen00212"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="foldopen00219"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="akernel_8h_html"></a>
<a id="anet__buf_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_USB_BUF_H
#define ZEPHYR_INCLUDE_USB_BUF_H

#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>


#if defined(CONFIG_UDC_BUF_FORCE_NOCACHE) || defined(CONFIG_UHC_BUF_FORCE_NOCACHE)
#define USB_BUF_FORCE_NOCACHE           1
#else
#define USB_BUF_FORCE_NOCACHE           0
#endif

#if defined(CONFIG_DCACHE_LINE_SIZE) && !USB_BUF_FORCE_NOCACHE
/*
 * Here we try to get DMA-safe buffers, but we lack a consistent source of
 * information about data cache properties, such as line cache size, and a
 * consistent source of information about what part of memory is DMA'able.
 * For now, we simply assume that all available memory is DMA'able and use
 * Kconfig option DCACHE_LINE_SIZE for alignment and granularity.
 */
#define USB_PRIV_BUFALIGN               CONFIG_DCACHE_LINE_SIZE
#define USB_PRIV_BUFGRANULARITY         CONFIG_DCACHE_LINE_SIZE
#else
/*
 * Default alignment and granularity to pointer size if the platform does not
 * have a data cache or buffers are placed in nocache memory region.
 */
#define USB_PRIV_BUFALIGN               sizeof(void *)
#define USB_PRIV_BUFGRANULARITY         sizeof(void *)
#endif


#if USB_BUF_FORCE_NOCACHE
/*
 * The usb transfer buffer needs to be in __nocache section
 */
#define USB_PRIV_BUFSECTION     __nocache
#else
#define USB_PRIV_BUFSECTION
#endif

#define USB_BUF_ALIGN           USB_PRIV_BUFALIGN

#define USB_BUF_GRANULARITY     USB_PRIV_BUFGRANULARITY

#define USB_BUF_ROUND_UP(size)  ROUND_UP(size, USB_PRIV_BUFGRANULARITY)

#define USB_STATIC_BUF_DEFINE(name, size)                                       \
        static uint8_t USB_PRIV_BUFSECTION __aligned(USB_BUF_ALIGN)             \
        name[USB_BUF_ROUND_UP(size)];

#define IS_USB_BUF_ALIGNED(buf) IS_ALIGNED(buf, USB_BUF_ALIGN)

#define USB_BUF_HEAP_DEFINE(name, bytes, in_section)                            \
        uint8_t in_section __aligned(USB_BUF_ALIGN)                             \
                kheap_##name[MAX(bytes, Z_HEAP_MIN_SIZE)];                      \
        STRUCT_SECTION_ITERABLE(k_heap, name) = {                               \
                .heap = {                                                       \
                        .init_mem = kheap_##name,                               \
                        .init_bytes = MAX(bytes, Z_HEAP_MIN_SIZE),              \
                 },                                                             \
        }

#define USB_BUF_K_HEAP_DEFINE(name, size)                                       \
        COND_CODE_1(USB_BUF_FORCE_NOCACHE,                                      \
                    (USB_BUF_HEAP_DEFINE(name, size, __nocache)),               \
                    (USB_BUF_HEAP_DEFINE(name, size, __noinit)))

extern const struct net_buf_data_cb net_buf_dma_cb;

#define USB_BUF_POOL_VAR_DEFINE(pname, count, size, ud_size, fdestroy)          \
        _NET_BUF_ARRAY_DEFINE(pname, count, ud_size);                           \
        USB_BUF_K_HEAP_DEFINE(net_buf_mem_pool_##pname, size);                  \
        static const struct net_buf_data_alloc net_buf_data_alloc_##pname = {   \
                .cb = &net_buf_dma_cb,                                          \
                .alloc_data = &net_buf_mem_pool_##pname,                        \
                .max_alloc_size = 0,                                            \
        };                                                                      \
        static STRUCT_SECTION_ITERABLE(net_buf_pool, pname) =                   \
                NET_BUF_POOL_INITIALIZER(pname, &net_buf_data_alloc_##pname,    \
                                         _net_buf_##pname, count, ud_size,      \
                                         fdestroy)

#define USB_BUF_POOL_DEFINE(pname, count, size, ud_size, fdestroy)              \
        _NET_BUF_ARRAY_DEFINE(pname, count, ud_size);                           \
        BUILD_ASSERT((USB_BUF_GRANULARITY) % (USB_BUF_ALIGN) == 0,              \
                     "Code assumes granurality is multiple of alignment");      \
        static uint8_t USB_PRIV_BUFSECTION __aligned(USB_BUF_ALIGN)             \
                net_buf_data_##pname[count][USB_BUF_ROUND_UP(size)];            \
        static const struct net_buf_pool_fixed net_buf_fixed_##pname = {        \
                .data_pool = (uint8_t *)net_buf_data_##pname,                   \
        };                                                                      \
        static const struct net_buf_data_alloc net_buf_fixed_alloc_##pname = {  \
                .cb = &net_buf_fixed_cb,                                        \
                .alloc_data = (void *)&net_buf_fixed_##pname,                   \
                .max_alloc_size = USB_BUF_ROUND_UP(size),                       \
        };                                                                      \
        static STRUCT_SECTION_ITERABLE(net_buf_pool, pname) =                   \
                NET_BUF_POOL_INITIALIZER(pname, &net_buf_fixed_alloc_##pname,   \
                                         _net_buf_##pname, count, ud_size,      \
                                         fdestroy)

#define UDC_BUF_ALIGN           USB_BUF_ALIGN

#define UDC_BUF_GRANULARITY     USB_BUF_GRANULARITY

#define UDC_ROUND_UP(size)      USB_BUF_ROUND_UP(size)

#define UDC_STATIC_BUF_DEFINE(name, size) USB_STATIC_BUF_DEFINE(name, size)

#define IS_UDC_ALIGNED(buf)     IS_USB_BUF_ALIGNED(buf)

#define UDC_BUF_POOL_VAR_DEFINE(pname, count, size, ud_size, fdestroy)          \
        USB_BUF_POOL_VAR_DEFINE(pname, count, size, ud_size, fdestroy)

#define UDC_BUF_POOL_DEFINE(pname, count, size, ud_size, fdestroy)              \
        USB_BUF_POOL_DEFINE(pname, count, size, ud_size, fdestroy)


#endif /* ZEPHYR_INCLUDE_UDC_BUF_H */
```

## 66.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 37 行

这里尝试获得可安全用于 DMA 的缓冲区，但缺乏一致的数据缓存属性信息来源，例如缓存行大小，也缺乏关于哪些内存区域能够用于 DMA 的一致信息来源。目前简单地假定所有可用内存都可用于 DMA，并使用 Kconfig 选项 `DCACHE_LINE_SIZE` 指定对齐和粒度。

### 注释 3：原第 47 行

如果平台没有数据缓存，或缓冲区放在不缓存的内存区域（Nocache memory region），则默认将对齐和粒度设为指针大小。

### 注释 4：原第 57 行

USB 传输缓冲区需要位于 `__nocache` 段（Section）。

### 注释 5：原第 225 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_UDC_BUF_H`。

## 66.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/usb__buf_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)

---

[上一章](P065_uart_intel_lw.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P067_wifi.h_源码浏览.md)
