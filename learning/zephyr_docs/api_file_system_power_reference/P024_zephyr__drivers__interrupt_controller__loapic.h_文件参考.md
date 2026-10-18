---
id: learning.zephyr-docs.api-file-system-power-reference.page-24
title: zephyr__drivers__interrupt_controller__loapic.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_loapic.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/arch/cpu.h>
#include <zephyr/arch/x86/msr.h>
#include <zephyr/sys/device_mmio.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 24.1\_宏定义（Macros）

<a id="r_aabaee35aa87c8c7e9dbd8e4ca04ec5fa"></a>

```c
#define LOAPIC_ID 0x020 /* Local APIC ID Reg */
```

相关声明：[LOAPIC_ID](#aabaee35aa87c8c7e9dbd8e4ca04ec5fa)。

<a id="r_a6865f3d12fa22ca44d37c555595f9a82"></a>

```c
#define LOAPIC_VER 0x030 /* Local APIC Version Reg */
```

相关声明：[LOAPIC_VER](#a6865f3d12fa22ca44d37c555595f9a82)。

<a id="r_ab821cf0c98ad7eaa74e682de764f8802"></a>

```c
#define LOAPIC_TPR 0x080 /* Task Priority Reg */
```

相关声明：[LOAPIC_TPR](#ab821cf0c98ad7eaa74e682de764f8802)。

<a id="r_a22b09ea2abe05d6dc693d9891b1b10dc"></a>

```c
#define LOAPIC_APR 0x090 /* Arbitration Priority Reg */
```

相关声明：[LOAPIC_APR](#a22b09ea2abe05d6dc693d9891b1b10dc)。

<a id="r_ab2ffcef005ced8514635a628ca13462f"></a>

```c
#define LOAPIC_PPR 0x0a0 /* Processor Priority Reg */
```

相关声明：[LOAPIC_PPR](#ab2ffcef005ced8514635a628ca13462f)。

<a id="r_a5cc8ffe88a717189312314661d489e52"></a>

```c
#define LOAPIC_EOI 0x0b0 /* EOI Reg */
```

相关声明：[LOAPIC_EOI](#a5cc8ffe88a717189312314661d489e52)。

<a id="r_abc2a39fa145706f72295cd34a5e89862"></a>

```c
#define LOAPIC_LDR 0x0d0 /* Logical Destination Reg */
```

相关声明：[LOAPIC_LDR](#abc2a39fa145706f72295cd34a5e89862)。

<a id="r_a43f1bb7e6e9492bddfe8dd00ab789f51"></a>

```c
#define LOAPIC_DFR 0x0e0 /* Destination Format Reg */
```

相关声明：[LOAPIC_DFR](#a43f1bb7e6e9492bddfe8dd00ab789f51)。

<a id="r_abf0572a04563cff27b01acde823b75d0"></a>

```c
#define LOAPIC_SVR 0x0f0 /* Spurious Interrupt Reg */
```

相关声明：[LOAPIC_SVR](#abf0572a04563cff27b01acde823b75d0)。

<a id="r_acba6145af5fd413d8985f700b7376881"></a>

```c
#define LOAPIC_ISR 0x100 /* In-service Reg */
```

相关声明：[LOAPIC_ISR](#acba6145af5fd413d8985f700b7376881)。

<a id="r_a8c2a2d604d222ecd9d1e91ebd1793877"></a>

```c
#define LOAPIC_TMR 0x180 /* Trigger Mode Reg */
```

相关声明：[LOAPIC_TMR](#a8c2a2d604d222ecd9d1e91ebd1793877)。

<a id="r_a98b3ebb077835af6b185953a260ee62c"></a>

```c
#define LOAPIC_IRR 0x200 /* Interrupt Request Reg */
```

相关声明：[LOAPIC_IRR](#a98b3ebb077835af6b185953a260ee62c)。

<a id="r_a610671b710fafe94cc41631d8275d4b5"></a>

```c
#define LOAPIC_ESR 0x280 /* Error Status Reg */
```

相关声明：[LOAPIC_ESR](#a610671b710fafe94cc41631d8275d4b5)。

<a id="r_a29270aa4461ff9a94bda5ef2dd59e950"></a>

```c
#define LOAPIC_ICRLO 0x300 /* Interrupt Command Reg */
```

相关声明：[LOAPIC_ICRLO](#a29270aa4461ff9a94bda5ef2dd59e950)。

<a id="r_a5d5cd6ba2e4ca22fc15f666e0231bc6e"></a>

```c
#define LOAPIC_ICRHI 0x310 /* Interrupt Command Reg */
```

相关声明：[LOAPIC_ICRHI](#a5d5cd6ba2e4ca22fc15f666e0231bc6e)。

<a id="r_ad2c049f84d86360481bf39f1c769d33a"></a>

```c
#define LOAPIC_TIMER 0x320 /* LVT (Timer) */
```

相关声明：[LOAPIC_TIMER](#ad2c049f84d86360481bf39f1c769d33a)。

<a id="r_a909c6e0ee5fc88de8f444436ea3cfdac"></a>

```c
#define LOAPIC_THERMAL 0x330 /* LVT (Thermal) */
```

相关声明：[LOAPIC_THERMAL](#a909c6e0ee5fc88de8f444436ea3cfdac)。

<a id="r_a3eb80c82f8f006729add8777f99d545b"></a>

```c
#define LOAPIC_PMC 0x340 /* LVT (PMC) */
```

相关声明：[LOAPIC_PMC](#a3eb80c82f8f006729add8777f99d545b)。

<a id="r_a1353f571e91132ca48eec99b9de70803"></a>

```c
#define LOAPIC_LINT0 0x350 /* LVT (LINT0) */
```

相关声明：[LOAPIC_LINT0](#a1353f571e91132ca48eec99b9de70803)。

<a id="r_a7293b3baa5944f0f8ef80533483a8b58"></a>

```c
#define LOAPIC_LINT1 0x360 /* LVT (LINT1) */
```

相关声明：[LOAPIC_LINT1](#a7293b3baa5944f0f8ef80533483a8b58)。

<a id="r_ab7911822a48695ea33abe3321623fe98"></a>

```c
#define LOAPIC_ERROR 0x370 /* LVT (ERROR) */
```

相关声明：[LOAPIC_ERROR](#ab7911822a48695ea33abe3321623fe98)。

<a id="r_a32f96a18492f74193e60ed7b58c66018"></a>

```c
#define LOAPIC_TIMER_ICR 0x380 /* Timer Initial Count Reg */
```

相关声明：[LOAPIC_TIMER_ICR](#a32f96a18492f74193e60ed7b58c66018)。

<a id="r_a33fd2d6104705d5b222d7a40133608b9"></a>

```c
#define LOAPIC_TIMER_CCR 0x390 /* Timer Current Count Reg */
```

相关声明：[LOAPIC_TIMER_CCR](#a33fd2d6104705d5b222d7a40133608b9)。

<a id="r_a9033fab28d4760b5861984890a31589e"></a>

```c
#define LOAPIC_TIMER_CONFIG 0x3e0 /* Timer Divide Config Reg */
```

相关声明：[LOAPIC_TIMER_CONFIG](#a9033fab28d4760b5861984890a31589e)。

<a id="r_aeea0b064b955e73205f882cd80132455"></a>

```c
#define LOAPIC_SELF_IPI 0x3f0 /* Self IPI Reg, only support in X2APIC mode */
```

相关声明：[LOAPIC_SELF_IPI](#aeea0b064b955e73205f882cd80132455)。

<a id="r_a7a95e68934f45e785ac88345d751ef00"></a>

```c
#define LOAPIC_ICR_BUSY 0x00001000U /* delivery status: 1 = busy */
```

相关声明：[LOAPIC_ICR_BUSY](#a7a95e68934f45e785ac88345d751ef00)。

<a id="r_a282cbda65290890f29eacd0f13ac2265"></a>

```c
#define LOAPIC_ICR_IPI_SPECIFIC 0x00004000U /* target IPI to specific CPU */
```

相关声明：[LOAPIC_ICR_IPI_SPECIFIC](#a282cbda65290890f29eacd0f13ac2265)。

<a id="r_af2037e08d1e66a8ac00b71c944bc36aa"></a>

```c
#define LOAPIC_ICR_IPI_OTHERS 0x000C4000U /* normal IPI to other CPUs */
```

相关声明：[LOAPIC_ICR_IPI_OTHERS](#af2037e08d1e66a8ac00b71c944bc36aa)。

<a id="r_aeda0d6d2a4bc948dc97c1b548e0b424a"></a>

```c
#define LOAPIC_ICR_IPI_INIT 0x00004500U
```

相关声明：[LOAPIC_ICR_IPI_INIT](#aeda0d6d2a4bc948dc97c1b548e0b424a)。

<a id="r_a256c3ccf1e2dd2f7dd0f6c7006aab99c"></a>

```c
#define LOAPIC_ICR_IPI_STARTUP 0x00004600U
```

相关声明：[LOAPIC_ICR_IPI_STARTUP](#a256c3ccf1e2dd2f7dd0f6c7006aab99c)。

<a id="r_a4da1bd27f6148a30f40eebe70c890a4b"></a>

```c
#define LOAPIC_LVT_MASKED 0x00010000U /* mask */
```

相关声明：[LOAPIC_LVT_MASKED](#a4da1bd27f6148a30f40eebe70c890a4b)。

<a id="r_a83cfcf18004022e6f77a5db51a7521cc"></a>

```c
#define LOAPIC_REGS_STR loapic_regs /* mmio device name */
```

相关声明：[LOAPIC_REGS_STR](#a83cfcf18004022e6f77a5db51a7521cc)、[device](../device_reference/P002_设备对象结构.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 24.2\_函数（Functions）

<a id="r_a6fab4c5cc1444a7f69cc0ae005e6c582"></a>

```c
DEVICE_MMIO_TOPLEVEL_DECLARE (loapic_regs)
```

相关声明：[DEVICE_MMIO_TOPLEVEL_DECLARE](#a6fab4c5cc1444a7f69cc0ae005e6c582)。

<a id="r_a797471308f74780dfcec277b18853fca"></a>

```c
static uint64_t x86_read_x2apic (unsigned int reg)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[x86_read_x2apic](#a797471308f74780dfcec277b18853fca)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

在 x2APIC 模式下从本地 APIC（Local APIC）读取 64 位值。

<a id="r_a4807ae47f62151774877f21939fafeab"></a>

```c
static uint32_t x86_read_xapic (unsigned int reg)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[x86_read_xapic](#a4807ae47f62151774877f21939fafeab)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

在 xAPIC（MMIO）模式下从本地 APIC（Local APIC）读取 32 位值。

<a id="r_a6ba00d305469ab62f89888cf0aa64033"></a>

```c
static uint32_t x86_read_loapic (unsigned int reg)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[x86_read_loapic](#a6ba00d305469ab62f89888cf0aa64033)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

使用默认模式（Default Mode）从本地 APIC（Local APIC）读取值。

<a id="r_a060a375336bf44c2dde9537d32f9416d"></a>

```c
static void x86_write_x2apic (unsigned int reg, uint64_t val)
```

相关声明：[x86_write_x2apic](#a060a375336bf44c2dde9537d32f9416d)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在 x2APIC 模式下向本地 APIC（Local APIC）写入 64 位值。

<a id="r_a9d7e889e4e4718d2205f647af172762a"></a>

```c
static void x86_write_xapic (unsigned int reg, uint32_t val)
```

相关声明：[x86_write_xapic](#a9d7e889e4e4718d2205f647af172762a)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在 xAPIC（MMIO）模式下向本地 APIC（Local APIC）写入 32 位值。

<a id="r_a884390389c9c7cef65801bba00395e4d"></a>

```c
static void x86_write_loapic (unsigned int reg, uint32_t val)
```

相关声明：[x86_write_loapic](#a884390389c9c7cef65801bba00395e4d)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

使用默认模式（Default Mode）向本地 APIC（Local APIC）写入 32 位值。

## 24.3\_详细说明（Detailed Documentation）

<a id="a22b09ea2abe05d6dc693d9891b1b10dc"></a>

### `LOAPIC_APR`

```c
#define LOAPIC_APR 0x090 /* Arbitration Priority Reg */
```

<a id="a43f1bb7e6e9492bddfe8dd00ab789f51"></a>

### `LOAPIC_DFR`

```c
#define LOAPIC_DFR 0x0e0 /* Destination Format Reg */
```

<a id="a5cc8ffe88a717189312314661d489e52"></a>

### `LOAPIC_EOI`

```c
#define LOAPIC_EOI 0x0b0 /* EOI Reg */
```

<a id="ab7911822a48695ea33abe3321623fe98"></a>

### `LOAPIC_ERROR`

```c
#define LOAPIC_ERROR 0x370 /* LVT (ERROR) */
```

<a id="a610671b710fafe94cc41631d8275d4b5"></a>

### `LOAPIC_ESR`

```c
#define LOAPIC_ESR 0x280 /* Error Status Reg */
```

<a id="a7a95e68934f45e785ac88345d751ef00"></a>

### `LOAPIC_ICR_BUSY`

```c
#define LOAPIC_ICR_BUSY 0x00001000U /* delivery status: 1 = busy */
```

<a id="aeda0d6d2a4bc948dc97c1b548e0b424a"></a>

### `LOAPIC_ICR_IPI_INIT`

```c
#define LOAPIC_ICR_IPI_INIT 0x00004500U
```

<a id="af2037e08d1e66a8ac00b71c944bc36aa"></a>

### `LOAPIC_ICR_IPI_OTHERS`

```c
#define LOAPIC_ICR_IPI_OTHERS 0x000C4000U /* normal IPI to other CPUs */
```

<a id="a282cbda65290890f29eacd0f13ac2265"></a>

### `LOAPIC_ICR_IPI_SPECIFIC`

```c
#define LOAPIC_ICR_IPI_SPECIFIC 0x00004000U /* target IPI to specific CPU */
```

<a id="a256c3ccf1e2dd2f7dd0f6c7006aab99c"></a>

### `LOAPIC_ICR_IPI_STARTUP`

```c
#define LOAPIC_ICR_IPI_STARTUP 0x00004600U
```

<a id="a5d5cd6ba2e4ca22fc15f666e0231bc6e"></a>

### `LOAPIC_ICRHI`

```c
#define LOAPIC_ICRHI 0x310 /* Interrupt Command Reg */
```

<a id="a29270aa4461ff9a94bda5ef2dd59e950"></a>

### `LOAPIC_ICRLO`

```c
#define LOAPIC_ICRLO 0x300 /* Interrupt Command Reg */
```

<a id="aabaee35aa87c8c7e9dbd8e4ca04ec5fa"></a>

### `LOAPIC_ID`

```c
#define LOAPIC_ID 0x020 /* Local APIC ID Reg */
```

<a id="a98b3ebb077835af6b185953a260ee62c"></a>

### `LOAPIC_IRR`

```c
#define LOAPIC_IRR 0x200 /* Interrupt Request Reg */
```

<a id="acba6145af5fd413d8985f700b7376881"></a>

### `LOAPIC_ISR`

```c
#define LOAPIC_ISR 0x100 /* In-service Reg */
```

<a id="abc2a39fa145706f72295cd34a5e89862"></a>

### `LOAPIC_LDR`

```c
#define LOAPIC_LDR 0x0d0 /* Logical Destination Reg */
```

<a id="a1353f571e91132ca48eec99b9de70803"></a>

### `LOAPIC_LINT0`

```c
#define LOAPIC_LINT0 0x350 /* LVT (LINT0) */
```

<a id="a7293b3baa5944f0f8ef80533483a8b58"></a>

### `LOAPIC_LINT1`

```c
#define LOAPIC_LINT1 0x360 /* LVT (LINT1) */
```

<a id="a4da1bd27f6148a30f40eebe70c890a4b"></a>

### `LOAPIC_LVT_MASKED`

```c
#define LOAPIC_LVT_MASKED 0x00010000U /* mask */
```

<a id="a3eb80c82f8f006729add8777f99d545b"></a>

### `LOAPIC_PMC`

```c
#define LOAPIC_PMC 0x340 /* LVT (PMC) */
```

<a id="ab2ffcef005ced8514635a628ca13462f"></a>

### `LOAPIC_PPR`

```c
#define LOAPIC_PPR 0x0a0 /* Processor Priority Reg */
```

<a id="a83cfcf18004022e6f77a5db51a7521cc"></a>

### `LOAPIC_REGS_STR`

```c
#define LOAPIC_REGS_STR loapic_regs /* mmio device name */
```

<a id="aeea0b064b955e73205f882cd80132455"></a>

### `LOAPIC_SELF_IPI`

```c
#define LOAPIC_SELF_IPI 0x3f0 /* Self IPI Reg, only support in X2APIC mode */
```

<a id="abf0572a04563cff27b01acde823b75d0"></a>

### `LOAPIC_SVR`

```c
#define LOAPIC_SVR 0x0f0 /* Spurious Interrupt Reg */
```

<a id="a909c6e0ee5fc88de8f444436ea3cfdac"></a>

### `LOAPIC_THERMAL`

```c
#define LOAPIC_THERMAL 0x330 /* LVT (Thermal) */
```

<a id="ad2c049f84d86360481bf39f1c769d33a"></a>

### `LOAPIC_TIMER`

```c
#define LOAPIC_TIMER 0x320 /* LVT (Timer) */
```

<a id="a33fd2d6104705d5b222d7a40133608b9"></a>

### `LOAPIC_TIMER_CCR`

```c
#define LOAPIC_TIMER_CCR 0x390 /* Timer Current Count Reg */
```

<a id="a9033fab28d4760b5861984890a31589e"></a>

### `LOAPIC_TIMER_CONFIG`

```c
#define LOAPIC_TIMER_CONFIG 0x3e0 /* Timer Divide Config Reg */
```

<a id="a32f96a18492f74193e60ed7b58c66018"></a>

### `LOAPIC_TIMER_ICR`

```c
#define LOAPIC_TIMER_ICR 0x380 /* Timer Initial Count Reg */
```

<a id="a8c2a2d604d222ecd9d1e91ebd1793877"></a>

### `LOAPIC_TMR`

```c
#define LOAPIC_TMR 0x180 /* Trigger Mode Reg */
```

<a id="ab821cf0c98ad7eaa74e682de764f8802"></a>

### `LOAPIC_TPR`

```c
#define LOAPIC_TPR 0x080 /* Task Priority Reg */
```

<a id="a6865f3d12fa22ca44d37c555595f9a82"></a>

### `LOAPIC_VER`

```c
#define LOAPIC_VER 0x030 /* Local APIC Version Reg */
```

<a id="a6fab4c5cc1444a7f69cc0ae005e6c582"></a>

### `DEVICE_MMIO_TOPLEVEL_DECLARE()`

```c
DEVICE_MMIO_TOPLEVEL_DECLARE ( loapic_regs )
```

<a id="a6ba00d305469ab62f89888cf0aa64033"></a>

### `x86_read_loapic()`

```c
uint32_t x86_read_loapic ( unsigned int reg)
```

声明属性：`inline`、`static`。

使用默认模式（Default Mode）从本地 APIC（Local APIC）读取值。

使用由 `CONFIG_X2APIC` 决定的访问方式（xAPIC 或 x2APIC），返回从本地 APIC 读取的 32 位值。注意：只有 x2APIC 模式允许 64 位读取，而且必须直接调用 `x86_read_x2apic()` 才能完成；这是有意的设计。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `reg` | 要读取的本地 APIC 寄存器编号（LOAPIC Register Number），即 `LOAPIC_*`。 |

<a id="a797471308f74780dfcec277b18853fca"></a>

### `x86_read_x2apic()`

```c
uint64_t x86_read_x2apic ( unsigned int reg)
```

声明属性：`inline`、`static`。

在 x2APIC 模式下从本地 APIC（Local APIC）读取 64 位值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `reg` | 要读取的本地 APIC 寄存器编号（LOAPIC Register Number），即 `LOAPIC_*`。 |

<a id="a4807ae47f62151774877f21939fafeab"></a>

### `x86_read_xapic()`

```c
uint32_t x86_read_xapic ( unsigned int reg)
```

声明属性：`inline`、`static`。

在 xAPIC（MMIO）模式下从本地 APIC（Local APIC）读取 32 位值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `reg` | 要读取的本地 APIC 寄存器编号（LOAPIC Register Number），即 `LOAPIC_*`。 |

<a id="a884390389c9c7cef65801bba00395e4d"></a>

### `x86_write_loapic()`

```c
void x86_write_loapic ( unsigned int reg, uint32_t val )
```

声明属性：`inline`、`static`。

使用默认模式（Default Mode）向本地 APIC（Local APIC）写入 32 位值。

使用由 `CONFIG_X2APIC` 决定的访问方式（xAPIC 或 x2APIC），向本地 APIC 写入 32 位值。注意：只有 x2APIC 模式支持 64 位写入，而且必须直接调用 `x86_write_x2apic()` 才能完成；这是有意的设计。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `reg` | 要写入的本地 APIC 寄存器编号（LOAPIC Register Number），取 `LOAPIC_*` 中的一个值。 |
| `val` | 要写入的 32 位值（32-bit Value）。 |

<a id="a060a375336bf44c2dde9537d32f9416d"></a>

### `x86_write_x2apic()`

```c
void x86_write_x2apic ( unsigned int reg, uint64_t val )
```

声明属性：`inline`、`static`。

在 x2APIC 模式下向本地 APIC（Local APIC）写入 64 位值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `reg` | 要写入的本地 APIC 寄存器编号（LOAPIC Register Number），取 `LOAPIC_*` 中的一个值。 |
| `val` | 要写入的 64 位值（64-bit Value）。 |

<a id="a9d7e889e4e4718d2205f647af172762a"></a>

### `x86_write_xapic()`

```c
void x86_write_xapic ( unsigned int reg, uint32_t val )
```

声明属性：`inline`、`static`。

在 xAPIC（MMIO）模式下向本地 APIC（Local APIC）写入 32 位值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `reg` | 要写入的本地 APIC 寄存器编号（LOAPIC Register Number），取 `LOAPIC_*` 中的一个值。 |
| `val` | 要写入的 32 位值（32-bit Value）。 |


## 24.4\_原页交叉引用（Cross References）

- [zephyr/arch/cpu.h](../api_source_supplement_reference/P009_cpu.h_源码浏览.md)
- [zephyr/sys/device_mmio.h](../device_reference/P016_设备MMIO头文件源码.md)
- [查看此文件的源码。](../api_source_scheduler_interrupt_reference/P005_loapic.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P023_zephyr__dt-bindings__sensor__lis2ds12.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P025_zephyr__drivers__loopback_disk.h_文件参考.md)
