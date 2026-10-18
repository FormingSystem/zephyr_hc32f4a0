---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-23
title: riscv_imsic.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/riscv__imsic_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_riscv\_imsic.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/riscv__imsic_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/riscv__imsic_8h.html)。

## 23.1\_原始可见代码（Source Code）

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
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="adevice_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="ariscv__imsic_8h_html_a17f09878019d36a36f4b0c22b0998388"></a>
<a id="ariscv__imsic_8h_html_a66a14691a7401d228fbf4a9b2fa1a632"></a>
<a id="ariscv__imsic_8h_html_a7673e9f4387c4af457d5ca9dad8b0530"></a>
<a id="ariscv__imsic_8h_html_a88ef50b869732abc82f05e09d607d4a3"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright (c) 2025 Synopsys, Inc.
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_RISCV_IMSIC_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_RISCV_IMSIC_H_

#include <zephyr/device.h>
#include <zephyr/types.h>
#include <zephyr/arch/riscv/csr.h>

/* IMSIC direct CSRs (M-mode) */
#define CSR_MTOPEI      0x35C
#define CSR_MTOPI       0xFB0
#define CSR_MISELECT    0x350
#define CSR_MIREG       0x351
#define CSR_SETEIPNUM_M 0xFC0 /* Write EIID to set pending bit */
#define CSR_CLREIPNUM_M 0xFC1 /* Write EIID to clear pending bit */

/* MTOPEI register field masks */
#define MTOPEI_EIID_MASK  0x7FF /* Bits [10:0]: External Interrupt ID (0-2047) */
#define MTOPEI_PRIO_SHIFT 16    /* Bits [23:16]: Priority level */
#define MTOPEI_PRIO_MASK  (0xFF << MTOPEI_PRIO_SHIFT)

/* IMSIC indirect CSR addresses (per privilege file) */
#define ICSR_EIDELIVERY 0x70
#define ICSR_EITHRESH   0x72
#define ICSR_EIP0       0x80
#define ICSR_EIP1       0x81
#define ICSR_EIP2       0x82
#define ICSR_EIP3       0x83
#define ICSR_EIP4       0x84
#define ICSR_EIP5       0x85
#define ICSR_EIP6       0x86
#define ICSR_EIP7       0x87
#define ICSR_EIE0       0xC0
#define ICSR_EIE1       0xC1
#define ICSR_EIE2       0xC2
#define ICSR_EIE3       0xC3
#define ICSR_EIE4       0xC4
#define ICSR_EIE5       0xC5
#define ICSR_EIE6       0xC6
#define ICSR_EIE7       0xC7

#define EIDELIVERY_ENABLE    BIT(0)
#define EIDELIVERY_MODE_MMSI (0U << 29) /* MMSI only: 00 = 0x00000000 */

/* IMSIC API functions (implemented by drivers) */
uint32_t riscv_imsic_claim(void);

void riscv_imsic_enable_eiid(uint32_t eiid);

void riscv_imsic_disable_eiid(uint32_t eiid);

int riscv_imsic_is_enabled(uint32_t eiid);

#if defined(CONFIG_SMP)
void z_riscv_imsic_secondary_init(void);
#endif /* CONFIG_SMP */

#endif
```

## 23.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Synopsys, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 13 行

传入消息信号中断控制器（IMSIC）的直接控制与状态寄存器（CSRs），用于机器模式（M-mode）。

### 注释 3：原第 18 行

写入外部中断标识符（EIID），以置位挂起位（pending bit）。

### 注释 4：原第 19 行

写入外部中断标识符（EIID），以清除挂起位。

### 注释 5：原第 21 行

`MTOPEI` 寄存器字段掩码（field masks）。

### 注释 6：原第 22 行

位 `[10:0]`：外部中断标识符（External Interrupt ID），取值为 0–2047。

### 注释 7：原第 23 行

位 `[23:16]`：优先级（priority level）。

### 注释 8：原第 26 行

IMSIC 间接 CSR 地址，每个特权中断文件（privilege file）各自使用。

### 注释 9：原第 47 行

仅适用于 MMSI：`00 = 0x00000000`。

### 注释 10：原第 49 行

IMSIC API 函数，由驱动程序实现。

### 注释 11：原第 96 行

条件编译配置（Configuration）标记：`CONFIG_SMP`。

## 23.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/riscv__imsic_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [riscv_imsic_claim](https://docs.zephyrproject.org/latest/doxygen/html/riscv__imsic_8h.html#a7673e9f4387c4af457d5ca9dad8b0530)
- [riscv_imsic_enable_eiid](https://docs.zephyrproject.org/latest/doxygen/html/riscv__imsic_8h.html#a88ef50b869732abc82f05e09d607d4a3)
- [riscv_imsic_disable_eiid](https://docs.zephyrproject.org/latest/doxygen/html/riscv__imsic_8h.html#a66a14691a7401d228fbf4a9b2fa1a632)
- [riscv_imsic_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/riscv__imsic_8h.html#a17f09878019d36a36f4b0c22b0998388)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)

---

[上一章](P022_renesas_rz_dma.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P024_sensor.h_源码浏览.md)
