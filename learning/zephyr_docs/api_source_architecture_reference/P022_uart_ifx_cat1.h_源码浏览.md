---
id: learning.zephyr-docs.api-source-architecture-reference.page-22
title: uart_ifx_cat1.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__ifx__cat1_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_uart\_ifx\_cat1.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/uart__ifx__cat1_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../hardware/P354_UARTInfineonCAT1扩展.md)。

## 22.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
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
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="adrivers_2uart_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astring_8h_html"></a>

```c
/*
 * Copyright (c) 2025 Cypress Semiconductor Corporation (an Infineon company) or
 * an affiliate of Cypress Semiconductor Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/drivers/uart.h>
#include <string.h>
#include <cy_scb_uart.h>
#include <cy_gpio.h>
#include <cy_syslib.h>
#include <cy_sysint.h>

#define _IFX_CAT1_SCB_BLOCK_ID_INVALID (0xFF)

#if (CY_CPU_CORTEX_M0P != 0)
#define IFX_CAT1_ISR_PRIORITY_DEFAULT (3)
#else
#define IFX_CAT1_ISR_PRIORITY_DEFAULT (7)
#endif /* (CY_CPU_CORTEX_M0P != 0) */

#define IFX_CAT1_IRQ_MUXING (CY_CPU_CORTEX_M0P || CPUSS_SYSTEM_IRQ_PRESENT)

#define IFX_CAT1_IRQ_LEGACY_M0 (CY_CPU_CORTEX_M0P && (1u == CY_IP_M4CPUSS_VERSION))

#if (IFX_CAT1_IRQ_MUXING)
static inline void _ifx_cat1_irq_set_priority(cy_en_intr_t system_irq, uint8_t intr_priority)
#else
static inline void _ifx_cat1_irq_set_priority(IRQn_Type system_irq, uint8_t intr_priority)
#endif
{
#if IFX_CAT1_IRQ_MUXING
#if IFX_CAT1_IRQ_LEGACY_M0
        IRQn_Type irqn = _ifx_cat1_irq_find_cm0(system_irq);
        uint8_t priority_to_set = intr_priority;
#else /* CM0+ on CPUSSv2, or CM4/CM7 on CPUSSv2 with SYSTEM_IRQ_PRESENT */
        IRQn_Type irqn = Cy_SysInt_GetNvicConnection(system_irq);

        _ifx_cat1_system_irq_store_priority(system_irq, intr_priority);
        uint8_t priority_to_set = _ifx_cat1_system_irq_lowest_priority(irqn);
#endif
#else
        IRQn_Type irqn = system_irq;
        uint8_t priority_to_set = intr_priority;
#endif
        NVIC_SetPriority(irqn, priority_to_set);
}

#if (IFX_CAT1_IRQ_MUXING)
cy_rslt_t _ifx_cat1_irq_register(cy_en_intr_t system_intr, uint8_t intr_priority,
                                 cy_israddress irq_handler);
#else
cy_rslt_t _ifx_cat1_irq_register(IRQn_Type system_intr, uint8_t intr_priority,
                                 cy_israddress irq_handler);
#endif

#if (IFX_CAT1_IRQ_MUXING)
void _ifx_cat1_irq_enable(cy_en_intr_t system_irq);
#else
void _ifx_cat1_irq_enable(IRQn_Type system_irq);
#endif

/* Offset for implementation-defined ISR type numbers (IRQ0 = 16) */
#define _IFX_CAT1_UTILS_IRQN_OFFSET (16U)

/* Macro to get the IRQn of the current ISR */
#define _IFX_CAT1_UTILS_GET_CURRENT_IRQN() ((IRQn_Type)(__get_IPSR() - _IFX_CAT1_UTILS_IRQN_OFFSET))

#if (IFX_CAT1_IRQ_MUXING)
static inline cy_en_intr_t _ifx_cat1_irq_get_active(void)
#else
static inline IRQn_Type _ifx_cat1_irq_get_active(void)
#endif
{
        IRQn_Type irqn = _IFX_CAT1_UTILS_GET_CURRENT_IRQN();
#if IFX_CAT1_IRQ_MUXING
#if IFX_CAT1_IRQ_LEGACY_M0
        /* No pre-built functionality for this. Need to see what CPU interrupt is active, then
         * indirect through the NVIC mux to figure out what system IRQ it is mapped to.
         */
        return Cy_SysInt_GetInterruptSource(irqn);
#else /* CM0+ on CPUSSv2, or CM4/CM7 on CPUSSv2 with SYSTEM_IRQ_PRESENT */
        return Cy_SysInt_GetInterruptActive(irqn);
#endif
#else
        return irqn;
#endif
}
```

## 22.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权所有（Copyright）2025 Cypress Semiconductor Corporation（Infineon 旗下公司）或 Cypress Semiconductor Corporation 的关联公司。

SPDX-License-Identifier: Apache-2.0。

### 注释 2：原第 21 行

条件编译（Conditional Compilation）：`CY_CPU_CORTEX_M0P != 0`。

### 注释 3：原第 37 行

CPUSSv2 上的 CM0+，或具有 `SYSTEM_IRQ_PRESENT` 的 CPUSSv2 上的 CM4／CM7。

### 注释 4：原第 64 行

实现定义的中断服务程序类型编号偏移（Implementation-Defined ISR Type Number Offset），其中 IRQ0 = 16。

### 注释 5：原第 67 行

获取当前中断服务程序（ISR）之 `IRQn` 的宏。

### 注释 6：原第 79 行

没有现成的功能（Pre-Built Functionality）完成此操作。需要先确定哪个 CPU 中断当前处于活动状态，再通过嵌套向量中断控制器复用器（NVIC Mux）间接确定它映射到哪个系统中断请求（System IRQ）。

### 注释 7：原第 83 行

CPUSSv2 上的 CM0+，或具有 `SYSTEM_IRQ_PRESENT` 的 CPUSSv2 上的 CM4／CM7。

## 22.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../hardware/P354_UARTInfineonCAT1扩展.md)
- [zephyr/drivers/uart.h](../uart_driver_reference/P001_UART驱动头文件参考.md)
- [string.h](../api_file_reference/P472_____w__zephyr__zephyr__lib__libc__minimal__include__string.h_文件参考.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uart.h](../uart_driver_reference/P001_UART驱动头文件参考.md)

---

[上一章](P021_tc_util.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P023_usb_device.h_源码浏览.md)
