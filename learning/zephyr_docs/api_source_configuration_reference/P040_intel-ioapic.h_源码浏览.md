---
id: learning.zephyr-docs.api-source-configuration-reference.page-40
title: intel-ioapic.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intel-ioapic_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_intel-ioapic.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intel-ioapic_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intel-ioapic_8h.html)。

## 40.1\_原始可见代码（Source Code）

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
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>

```c
/*
 * Copyright (c) 2017 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_INTEL_IOAPIC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_INTEL_IOAPIC_H_


#define IRQ_TYPE_LEVEL                  0x00008000
#define IRQ_TYPE_EDGE                   0x00000000
#define IRQ_TYPE_LOW                    0x00002000
#define IRQ_TYPE_HIGH                   0x00000000
#define IRQ_DELIVERY_LOWEST             0x00000100
#define IRQ_DELIVERY_FIXED              0x00000000

/*
 * for most device interrupts, lowest priority delivery is preferred
 * since this ensures only one CPU gets the interrupt in SMP systems.
 */
#define IRQ_TYPE_LOWEST_EDGE_RISING             (IRQ_DELIVERY_LOWEST | IRQ_TYPE_EDGE | IRQ_TYPE_HIGH)
#define IRQ_TYPE_LOWEST_EDGE_FALLING            (IRQ_DELIVERY_LOWEST | IRQ_TYPE_EDGE | IRQ_TYPE_LOW)
#define IRQ_TYPE_LOWEST_LEVEL_HIGH              (IRQ_DELIVERY_LOWEST | IRQ_TYPE_LEVEL | IRQ_TYPE_HIGH)
#define IRQ_TYPE_LOWEST_LEVEL_LOW               (IRQ_DELIVERY_LOWEST | IRQ_TYPE_LEVEL | IRQ_TYPE_LOW)

/* for interrupts that want to be delivered to all CPUs, e.g. HPET */
#define IRQ_TYPE_FIXED_EDGE_RISING              (IRQ_DELIVERY_FIXED | IRQ_TYPE_EDGE | IRQ_TYPE_HIGH)
#define IRQ_TYPE_FIXED_EDGE_FALLING             (IRQ_DELIVERY_FIXED | IRQ_TYPE_EDGE | IRQ_TYPE_LOW)
#define IRQ_TYPE_FIXED_LEVEL_HIGH               (IRQ_DELIVERY_FIXED | IRQ_TYPE_LEVEL | IRQ_TYPE_HIGH)
#define IRQ_TYPE_FIXED_LEVEL_LOW                (IRQ_DELIVERY_FIXED | IRQ_TYPE_LEVEL | IRQ_TYPE_LOW)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_INTEL_IOAPIC_H_ */
```

## 40.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 41 行

对于大多数设备中断，优先采用最低优先级投递（Lowest priority delivery），因为这样能够确保在对称多处理（SMP）系统中只有一个 CPU 接收到中断。

### 注释 3：原第 54 行

用于希望投递到所有 CPU 的中断，例如高精度事件定时器（HPET）中断。

### 注释 4：原第 66 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_INTEL_IOAPIC_H_`。

## 40.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intel-ioapic_8h.html)

---

[上一章](P039_intc_rx_icu.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P041_intel_socfpga_reset.h_源码浏览.md)
