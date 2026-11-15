---
id: learning.zephyr-docs.api-source-scheduler-interrupt-reference.page-5
title: loapic.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_loapic.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html)。

## 5.1\_原始可见代码（Source Code）

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
<a id="foldopen00075"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="foldopen00086"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="foldopen00118"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="foldopen00130"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="foldopen00148"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
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
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="aarch_2cpu_8h_html"></a>
<a id="adevice__mmio_8h_html"></a>
<a id="agroup__device-mmio-toplevel_html_ga8a712886defe59972f4cf00bb2266f95"></a>
<a id="agroup__device-mmio-toplevel_html_gaad7ad99277cf2be684bd70c46d358338"></a>
<a id="agroup__sys__io__apis_html_ga7bcfa789a44940bccc5b9b98642744b0"></a>
<a id="agroup__sys__io__mmio__apis_html_gac742e54d030b90f98400cb1248b14ca8"></a>
<a id="agroup__sys__io__mmio__apis_html_gafebb790883d604c1ddbdbbd8314876d7"></a>
<a id="aloapic_8h_html_a060a375336bf44c2dde9537d32f9416d"></a>
<a id="aloapic_8h_html_a29270aa4461ff9a94bda5ef2dd59e950"></a>
<a id="aloapic_8h_html_a4807ae47f62151774877f21939fafeab"></a>
<a id="aloapic_8h_html_a5d5cd6ba2e4ca22fc15f666e0231bc6e"></a>
<a id="aloapic_8h_html_a6ba00d305469ab62f89888cf0aa64033"></a>
<a id="aloapic_8h_html_a797471308f74780dfcec277b18853fca"></a>
<a id="aloapic_8h_html_a7a95e68934f45e785ac88345d751ef00"></a>
<a id="aloapic_8h_html_a83cfcf18004022e6f77a5db51a7521cc"></a>
<a id="aloapic_8h_html_a884390389c9c7cef65801bba00395e4d"></a>
<a id="aloapic_8h_html_a9d7e889e4e4718d2205f647af172762a"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>

```c
/* loapic.h - public LOAPIC APIs */

/*
 * Copyright (c) 2015 Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_LOAPIC_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_LOAPIC_H_

#include <zephyr/arch/cpu.h>
#include <zephyr/arch/x86/msr.h>
#include <zephyr/sys/device_mmio.h>

/* Local APIC Register Offset */

#define LOAPIC_ID 0x020           /* Local APIC ID Reg */
#define LOAPIC_VER 0x030          /* Local APIC Version Reg */
#define LOAPIC_TPR 0x080          /* Task Priority Reg */
#define LOAPIC_APR 0x090          /* Arbitration Priority Reg */
#define LOAPIC_PPR 0x0a0          /* Processor Priority Reg */
#define LOAPIC_EOI 0x0b0          /* EOI Reg */
#define LOAPIC_LDR 0x0d0          /* Logical Destination Reg */
#define LOAPIC_DFR 0x0e0          /* Destination Format Reg */
#define LOAPIC_SVR 0x0f0          /* Spurious Interrupt Reg */
#define LOAPIC_ISR 0x100          /* In-service Reg */
#define LOAPIC_TMR 0x180          /* Trigger Mode Reg */
#define LOAPIC_IRR 0x200          /* Interrupt Request Reg */
#define LOAPIC_ESR 0x280          /* Error Status Reg */
#define LOAPIC_ICRLO 0x300      /* Interrupt Command Reg */
#define LOAPIC_ICRHI 0x310      /* Interrupt Command Reg */
#define LOAPIC_TIMER 0x320      /* LVT (Timer) */
#define LOAPIC_THERMAL 0x330      /* LVT (Thermal) */
#define LOAPIC_PMC 0x340          /* LVT (PMC) */
#define LOAPIC_LINT0 0x350      /* LVT (LINT0) */
#define LOAPIC_LINT1 0x360      /* LVT (LINT1) */
#define LOAPIC_ERROR 0x370      /* LVT (ERROR) */
#define LOAPIC_TIMER_ICR 0x380    /* Timer Initial Count Reg */
#define LOAPIC_TIMER_CCR 0x390    /* Timer Current Count Reg */
#define LOAPIC_TIMER_CONFIG 0x3e0 /* Timer Divide Config Reg */
#define LOAPIC_SELF_IPI 0x3f0   /* Self IPI Reg, only support in X2APIC mode */

#define LOAPIC_ICR_BUSY         0x00001000U     /* delivery status: 1 = busy */

#define LOAPIC_ICR_IPI_SPECIFIC 0x00004000U     /* target IPI to specific CPU */
#define LOAPIC_ICR_IPI_OTHERS   0x000C4000U     /* normal IPI to other CPUs */
#define LOAPIC_ICR_IPI_INIT     0x00004500U
#define LOAPIC_ICR_IPI_STARTUP  0x00004600U

#define LOAPIC_LVT_MASKED 0x00010000U  /* mask */

/* Defined in intc_loapic.c */
#define LOAPIC_REGS_STR                         loapic_regs     /* mmio device name */

#ifndef _ASMLANGUAGE

#ifdef __cplusplus
extern "C" {
#endif

DEVICE_MMIO_TOPLEVEL_DECLARE(LOAPIC_REGS_STR);

uint32_t z_loapic_irq_base(void);
void z_loapic_enable(unsigned char cpu_number);
void z_loapic_int_vec_set(unsigned int irq, unsigned int vector);
void z_loapic_irq_enable(unsigned int irq);
void z_loapic_irq_disable(unsigned int irq);

static inline uint64_t x86_read_x2apic(unsigned int reg)
{
        reg >>= 4;
        return z_x86_msr_read(X86_X2APIC_BASE_MSR + reg);
}

static inline uint32_t x86_read_xapic(unsigned int reg)
{
        mm_reg_t base;
        base = DEVICE_MMIO_TOPLEVEL_GET(LOAPIC_REGS_STR);
        return sys_read32(base + reg);
}

static inline uint32_t x86_read_loapic(unsigned int reg)
{
#ifdef CONFIG_X2APIC
        return x86_read_x2apic(reg);
#else
        return x86_read_xapic(reg);
#endif
}

static inline void x86_write_x2apic(unsigned int reg, uint64_t val)
{
        reg >>= 4;
        z_x86_msr_write(X86_X2APIC_BASE_MSR + reg, val);
}

static inline void x86_write_xapic(unsigned int reg, uint32_t val)
{
        mm_reg_t base;
        base = DEVICE_MMIO_TOPLEVEL_GET(LOAPIC_REGS_STR);
        sys_write32(val, base + reg);
}

static inline void x86_write_loapic(unsigned int reg, uint32_t val)
{
#ifdef CONFIG_X2APIC
        x86_write_x2apic(reg, val);
#else
        x86_write_xapic(reg, val);
#endif
}

static inline void z_loapic_ipi(uint8_t apic_id, uint32_t ipi, uint8_t vector)
{
        ipi |= (uint32_t)vector;

#ifndef CONFIG_X2APIC

        uint32_t icrhi = ((uint32_t)apic_id) << 24U;

        /*
         * Legacy xAPIC mode: first wait for any previous IPI to be delivered.
         */

        while (x86_read_xapic(LOAPIC_ICRLO) & LOAPIC_ICR_BUSY) {
        }

        x86_write_xapic(LOAPIC_ICRHI, icrhi);
        x86_write_xapic(LOAPIC_ICRLO, ipi);
#else
        /*
         * x2APIC mode is greatly simplified: one write, no delivery status.
         */

        x86_write_x2apic(LOAPIC_ICRLO, (((uint64_t) apic_id) << 32) | ipi);
#endif
}

#ifdef __cplusplus
}
#endif

#endif /* _ASMLANGUAGE */

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_LOAPIC_H_ */
```

## 5.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`loapic.h`：公开的本地高级可编程中断控制器（LOAPIC）API。

### 注释 2：原第 3 行

版权（Copyright）：© 2015 Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 16 行

本地 APIC 寄存器偏移（Local APIC Register Offset）。

### 注释 4：原第 18 行

本地 APIC 标识寄存器（Local APIC ID Register）。

### 注释 5：原第 19 行

本地 APIC 版本寄存器（Local APIC Version Register）。

### 注释 6：原第 20 行

任务优先级寄存器（Task Priority Register）。

### 注释 7：原第 21 行

仲裁优先级寄存器（Arbitration Priority Register）。

### 注释 8：原第 22 行

处理器优先级寄存器（Processor Priority Register）。

### 注释 9：原第 23 行

中断结束寄存器（EOI Register）。

### 注释 10：原第 24 行

逻辑目标寄存器（Logical Destination Register）。

### 注释 11：原第 25 行

目标格式寄存器（Destination Format Register）。

### 注释 12：原第 26 行

伪中断寄存器（Spurious Interrupt Register）。

### 注释 13：原第 27 行

服务中寄存器（In-service Register）。

### 注释 14：原第 28 行

触发模式寄存器（Trigger Mode Register）。

### 注释 15：原第 29 行

中断请求寄存器（Interrupt Request Register）。

### 注释 16：原第 30 行

错误状态寄存器（Error Status Register）。

### 注释 17：原第 31 行

中断命令寄存器（Interrupt Command Register）。

### 注释 18：原第 32 行

中断命令寄存器（Interrupt Command Register）。

### 注释 19：原第 33 行

本地向量表（LVT）定时器（Timer）项。

### 注释 20：原第 34 行

本地向量表（LVT）热管理（Thermal）项。

### 注释 21：原第 35 行

本地向量表（LVT）性能监测计数器（PMC）项。

### 注释 22：原第 36 行

本地向量表（LVT）的 LINT0 项。

### 注释 23：原第 37 行

本地向量表（LVT）的 LINT1 项。

### 注释 24：原第 38 行

本地向量表（LVT）错误（ERROR）项。

### 注释 25：原第 39 行

定时器初始计数寄存器（Timer Initial Count Register）。

### 注释 26：原第 40 行

定时器当前计数寄存器（Timer Current Count Register）。

### 注释 27：原第 41 行

定时器分频配置寄存器（Timer Divide Configuration Register）。

### 注释 28：原第 42 行

自发处理器间中断寄存器（Self IPI Register），仅在 X2APIC 模式下支持。

### 注释 29：原第 44 行

投递状态（Delivery Status）：1 表示忙。

### 注释 30：原第 46 行

将处理器间中断（IPI）定向发送到指定 CPU。

### 注释 31：原第 47 行

向其他 CPU 发送普通处理器间中断（IPI）。

### 注释 32：原第 51 行

掩码（Mask）。

### 注释 33：原第 53 行

定义在 `intc_loapic.c` 中。

### 注释 34：原第 54 行

内存映射输入输出（MMIO）设备名称。

### 注释 35：原第 172 行

传统 xAPIC 模式（Legacy xAPIC Mode）：先等待之前的处理器间中断（IPI）完成投递。

### 注释 36：原第 182 行

x2APIC 模式大为简化：一次写入，没有投递状态（Delivery Status）。

### 注释 37：原第 194 行

条件编译标记：`_ASMLANGUAGE`。

### 注释 38：原第 196 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_LOAPIC_H_`。

## 5.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html)
- [zephyr/arch/cpu.h](../api_file_reference/P013_zephyr__arch__cpu.h_文件参考.md)
- [zephyr/sys/device_mmio.h](../device_reference/P015_设备MMIO头文件参考.md)
- [DEVICE_MMIO_TOPLEVEL_DECLARE](../device_reference/P014_顶层MMIO区域.md#ga8a712886defe59972f4cf00bb2266f95)
- [LOAPIC_REGS_STR](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html#a83cfcf18004022e6f77a5db51a7521cc)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [x86_read_x2apic](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html#a797471308f74780dfcec277b18853fca)
- [x86_read_xapic](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html#a4807ae47f62151774877f21939fafeab)
- [mm_reg_t](../device_reference/P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)
- [DEVICE_MMIO_TOPLEVEL_GET](../device_reference/P014_顶层MMIO区域.md#gaad7ad99277cf2be684bd70c46d358338)
- [sys_read32](../device_reference/P019_内存映射寄存器IO接口.md#gac742e54d030b90f98400cb1248b14ca8)
- [x86_read_loapic](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html#a6ba00d305469ab62f89888cf0aa64033)
- [x86_write_x2apic](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html#a060a375336bf44c2dde9537d32f9416d)
- [x86_write_xapic](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html#a9d7e889e4e4718d2205f647af172762a)
- [sys_write32](../device_reference/P019_内存映射寄存器IO接口.md#gafebb790883d604c1ddbdbbd8314876d7)
- [x86_write_loapic](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html#a884390389c9c7cef65801bba00395e4d)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [LOAPIC_ICRLO](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html#a29270aa4461ff9a94bda5ef2dd59e950)
- [LOAPIC_ICR_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html#a7a95e68934f45e785ac88345d751ef00)
- [LOAPIC_ICRHI](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html#a5d5cd6ba2e4ca22fc15f666e0231bc6e)
- [cpu.h](../api_file_reference/P013_zephyr__arch__cpu.h_文件参考.md)
- [device_mmio.h](../device_reference/P015_设备MMIO头文件参考.md)

---

[上一章](P004_kernel_structs.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P006_pinctrl-r8a78000.h_源码浏览.md)
