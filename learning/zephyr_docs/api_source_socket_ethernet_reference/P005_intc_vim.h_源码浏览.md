---
id: learning.zephyr-docs.api-source-socket-ethernet-reference.page-5
title: intc_vim.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__vim_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_intc\_vim.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intc__vim_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P167_zephyr__drivers__interrupt_controller__intc_vim.h_文件参考.md)。

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
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
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
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="adevicetree_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="ati-vim_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c
/* Copyright (C) 2023 BeagleBoard.org Foundation
 * Copyright (C) 2023 S Prashanth
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_VIM_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_VIM_H_

#include <stdint.h>

#include <zephyr/devicetree.h>
#include <zephyr/dt-bindings/interrupt-controller/ti-vim.h>
#include <zephyr/sys/util_macro.h>

#define VIM_BASE_ADDR             DT_REG_ADDR(DT_INST(0, ti_vim))

#define VIM_MAX_IRQ_PER_GROUP     (32)
#define VIM_MAX_GROUP_NUM         ((uint32_t)(CONFIG_NUM_IRQS / VIM_MAX_IRQ_PER_GROUP))

#define VIM_GET_IRQ_GROUP_NUM(n)  ((uint32_t)((n) / VIM_MAX_IRQ_PER_GROUP))
#define VIM_GET_IRQ_BIT_NUM(n)    ((uint32_t)((n) % VIM_MAX_IRQ_PER_GROUP))

#define VIM_PRI_INT_MAX           (15)

#define VIM_PID             (VIM_BASE_ADDR + 0x0000)
#define VIM_INFO            (VIM_BASE_ADDR + 0x0004)
#define VIM_PRIIRQ          (VIM_BASE_ADDR + 0x0008)
#define VIM_PRIFIQ          (VIM_BASE_ADDR + 0x000C)
#define VIM_IRQGSTS         (VIM_BASE_ADDR + 0x0010)
#define VIM_FIQGSTS         (VIM_BASE_ADDR + 0x0014)
#define VIM_IRQVEC          (VIM_BASE_ADDR + 0x0018)
#define VIM_FIQVEC          (VIM_BASE_ADDR + 0x001C)
#define VIM_ACTIRQ          (VIM_BASE_ADDR + 0x0020)
#define VIM_ACTFIQ          (VIM_BASE_ADDR + 0x0024)
#define VIM_DEDVEC          (VIM_BASE_ADDR + 0x0030)

#define VIM_RAW(n)          (VIM_BASE_ADDR + (0x400) + ((n) * 0x20))
#define VIM_STS(n)          (VIM_BASE_ADDR + (0x404) + ((n) * 0x20))
#define VIM_INTR_EN_SET(n)  (VIM_BASE_ADDR + (0x408) + ((n) * 0x20))
#define VIM_INTR_EN_CLR(n)  (VIM_BASE_ADDR + (0x40c) + ((n) * 0x20))
#define VIM_IRQSTS(n)       (VIM_BASE_ADDR + (0x410) + ((n) * 0x20))
#define VIM_FIQSTS(n)       (VIM_BASE_ADDR + (0x414) + ((n) * 0x20))
#define VIM_INTMAP(n)       (VIM_BASE_ADDR + (0x418) + ((n) * 0x20))
#define VIM_INTTYPE(n)      (VIM_BASE_ADDR + (0x41c) + ((n) * 0x20))
#define VIM_PRI_INT(n)      (VIM_BASE_ADDR + (0x1000) + ((n) * 0x4))
#define VIM_VEC_INT(n)      (VIM_BASE_ADDR + (0x2000) + ((n) * 0x4))

/* RAW */
#define VIM_GRP_RAW_STS_MASK                 (BIT64_MASK(32))

/* STS */
#define VIM_GRP_STS_MSK_MASK                 (BIT64_MASK(32))

/* INTR_EN_SET */
#define VIM_GRP_INTR_EN_SET_MSK_MASK         (BIT64_MASK(32))

/* INTR_EN_CLR */
#define VIM_GRP_INTR_EN_CLR_MSK_MASK         (BIT64_MASK(32))

/* IRQSTS */
#define VIM_GRP_IRQSTS_MSK_MASK              (BIT64_MASK(32))

/* FIQSTS */
#define VIM_GRP_FIQSTS_MSK_MASK              (BIT64_MASK(32))

/* INTMAP */
#define VIM_GRP_INTMAP_MSK_MASK              (BIT64_MASK(32))

/* INTTYPE */
#define VIM_GRP_INTTYPE_MSK_MASK             (BIT64_MASK(32))

/* INT */
#define VIM_PRI_INT_VAL_MASK                 (BIT_MASK(4))

/* INT */
#define VIM_VEC_INT_VAL_MASK                 (0xFFFFFFFCU)

/* INFO */
#define VIM_INFO_INTERRUPTS_MASK             (BIT_MASK(11))

/* PRIIRQ */
#define VIM_PRIIRQ_VALID_MASK                (0x80000000U)
#define VIM_PRIIRQ_VALID_VAL_TRUE            (0x1U)
#define VIM_PRIIRQ_VALID_VAL_FALSE           (0x0U)
#define VIM_PRIIRQ_PRI_MASK                  (0x000F0000U)
#define VIM_PRIIRQ_NUM_MASK                  (BIT_MASK(10))

/* PRIFIQ */
#define VIM_PRIFIQ_VALID_MASK                (0x80000000U)
#define VIM_PRIFIQ_VALID_VAL_TRUE            (0x1U)
#define VIM_PRIFIQ_VALID_VAL_FALSE           (0x0U)
#define VIM_PRIFIQ_PRI_MASK                  (0x000F0000U)
#define VIM_PRIFIQ_NUM_MASK                  (BIT_MASK(10))

/* IRQGSTS */
#define VIM_IRQGSTS_STS_MASK                 (BIT64_MASK(32))

/* FIQGSTS */
#define VIM_FIQGSTS_STS_MASK                 (BIT64_MASK(32))

/* IRQVEC */
#define VIM_IRQVEC_ADDR_MASK                 (0xFFFFFFFCU)

/* FIQVEC */
#define VIM_FIQVEC_ADDR_MASK                 (0xFFFFFFFCU)

/* ACTIRQ */
#define VIM_ACTIRQ_VALID_MASK                (0x80000000U)
#define VIM_ACTIRQ_VALID_VAL_TRUE            (0x1U)
#define VIM_ACTIRQ_VALID_VAL_FALSE           (0x0U)
#define VIM_ACTIRQ_PRI_MASK                  (0x000F0000U)
#define VIM_ACTIRQ_NUM_MASK                  (BIT_MASK(10))

/* ACTFIQ */
#define VIM_ACTFIQ_VALID_MASK                (0x80000000U)
#define VIM_ACTFIQ_VALID_VAL_TRUE            (0x1U)
#define VIM_ACTFIQ_VALID_VAL_FALSE           (0x0U)
#define VIM_ACTFIQ_PRI_MASK                  (0x000F0000U)
#define VIM_ACTFIQ_NUM_MASK                  (BIT_MASK(10))

/* DEDVEC */
#define VIM_DEDVEC_ADDR_MASK                 (0xFFFFFFFCU)

/*
 * VIM Driver Interface Functions
 */

unsigned int z_vim_irq_get_active(void);

void z_vim_irq_eoi(unsigned int irq);

void z_vim_irq_init(void);

void z_vim_irq_priority_set(unsigned int irq, unsigned int prio, uint32_t flags);

void z_vim_irq_enable(unsigned int irq);

void z_vim_irq_disable(unsigned int irq);

int z_vim_irq_is_enabled(unsigned int irq);

void z_vim_arm_enter_irq(int irq);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_VIM_H_ */
```

## 5.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：(C) 2023 BeagleBoard.org Foundation。

版权（Copyright）：(C) 2023 S Prashanth。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 49 行

`RAW` 寄存器。

### 注释 3：原第 52 行

`STS` 寄存器。

### 注释 4：原第 55 行

`INTR_EN_SET` 寄存器。

### 注释 5：原第 58 行

`INTR_EN_CLR` 寄存器。

### 注释 6：原第 61 行

`IRQSTS` 寄存器。

### 注释 7：原第 64 行

`FIQSTS` 寄存器。

### 注释 8：原第 67 行

`INTMAP` 寄存器。

### 注释 9：原第 70 行

`INTTYPE` 寄存器。

### 注释 10：原第 73 行

`INT` 寄存器。

### 注释 11：原第 76 行

`INT` 寄存器。

### 注释 12：原第 79 行

`INFO` 寄存器。

### 注释 13：原第 82 行

`PRIIRQ` 寄存器。

### 注释 14：原第 89 行

`PRIFIQ` 寄存器。

### 注释 15：原第 96 行

`IRQGSTS` 寄存器。

### 注释 16：原第 99 行

`FIQGSTS` 寄存器。

### 注释 17：原第 102 行

`IRQVEC` 寄存器。

### 注释 18：原第 105 行

`FIQVEC` 寄存器。

### 注释 19：原第 108 行

`ACTIRQ` 寄存器。

### 注释 20：原第 115 行

`ACTFIQ` 寄存器。

### 注释 21：原第 122 行

`DEDVEC` 寄存器。

### 注释 22：原第 125 行

向量中断管理器（VIM）驱动接口函数（Driver Interface Functions）。

### 注释 23：原第 188 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_VIM_H_`。

## 5.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P167_zephyr__drivers__interrupt_controller__intc_vim.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/dt-bindings/interrupt-controller/ti-vim.h](../api_file_runtime_reference/P070_zephyr__dt-bindings__interrupt-controller__ti-vim.h_文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [ti-vim.h](../api_file_runtime_reference/P070_zephyr__dt-bindings__interrupt-controller__ti-vim.h_文件参考.md)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P004_imx_ccm_rev2.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P006_socket.h_源码浏览.md)
