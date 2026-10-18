---
id: learning.zephyr-docs.api-source-interrupt-modem-reference.page-1
title: bcm2835-armctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bcm2835-armctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_bcm2835-armctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bcm2835-armctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_supplement_reference/P005_zephyr__dt-bindings__interrupt-controller__bcm2835-armctrl.h_文件参考.md)。

## 1.1\_原始可见代码（Source Code）

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
<a id="l00093"></a>
<a id="l00094"></a>

```c
/*
 * Copyright (c) 2026 Jonathan Elliot Peace <jep@alphabetiq.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_BCM2835_ARMCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_BCM2835_ARMCTRL_H_


/*
 * Zephyr IRQ-number layout for the BCM2710 SoC (BCM2836 L1 intc +
 * BCM2835 ARMC peripheral intc cascaded behind it):
 *
 *     0..31     reserved for the L1 ARM-local intc (only 0..9 used --
 *               see <zephyr/dt-bindings/interrupt-controller/bcm2836-l1.h>).
 *               IRQ 8 (L1 GPU IRQ) is the cascade entry; the SoC IRQ
 *               glue resolves it transparently inside z_soc_irq_get_active
 *               so it is never seen by application ISRs.
 *
 *     32 + (bank << 5) + bit        -- ARMC peripheral IRQs:
 *         bank 0 (basic):           32..39   (IRQ_BASIC_PENDING bits 0..7)
 *         bank 1 (PEND1, GPU 0..31): 64..95
 *         bank 2 (PEND2, GPU 32..63): 96..127
 *
 * The bank-shift encoding (offset by +32 for the L1 reservation)
 * keeps the SoC-layer shortcut/cascade decode a straightforward
 * arithmetic mapping of the BCM2835 ARMC pending-register layout.
 */
#define BCM2835_IRQ_BASE        32

#define BCM2835_HWIRQ(bank, n)  (BCM2835_IRQ_BASE + ((bank) << 5) + (n))

#define BCM2835_BASIC_IRQ(n)    BCM2835_HWIRQ(0, n)   /* 32..39 */
#define BCM2835_BANK1(n)        BCM2835_HWIRQ(1, n)   /* 64..95 */
#define BCM2835_BANK2(n)        BCM2835_HWIRQ(2, n)   /* 96..127 */

/* basic bank shortcuts */
#define BCM2835_IRQ_ARM_TIMER       BCM2835_BASIC_IRQ(0)
#define BCM2835_IRQ_ARM_MAILBOX     BCM2835_BASIC_IRQ(1)
#define BCM2835_IRQ_ARM_DOORBELL0   BCM2835_BASIC_IRQ(2)
#define BCM2835_IRQ_ARM_DOORBELL1   BCM2835_BASIC_IRQ(3)
#define BCM2835_IRQ_GPU0_HALT       BCM2835_BASIC_IRQ(4)
#define BCM2835_IRQ_GPU1_HALT       BCM2835_BASIC_IRQ(5)
#define BCM2835_IRQ_ILLEGAL_TYPE0   BCM2835_BASIC_IRQ(6)
#define BCM2835_IRQ_ILLEGAL_TYPE1   BCM2835_BASIC_IRQ(7)

/* GPU PEND1 (peripheral lower bank) */
#define BCM2835_IRQ_TIMER0          BCM2835_BANK1(0)
#define BCM2835_IRQ_TIMER1          BCM2835_BANK1(1)
#define BCM2835_IRQ_TIMER2          BCM2835_BANK1(2)
#define BCM2835_IRQ_TIMER3          BCM2835_BANK1(3)
/* USB OTG (Synopsys DWC2). GPU IRQ 9 per the BCM2835 ARM Peripherals
 * datasheet ch. 7 "ARM peripherals interrupts table".
 */
#define BCM2835_IRQ_USB             BCM2835_BANK1(9)  /* DWC2 USB OTG */
/* DMA channel IRQs: channels 0..10 have dedicated lines at PEND1 bits
 * 16..26; channels 11..14 share bit 27. (PEND1 bit 28, the "any DMA
 * channel" line, is not exposed.)
 */
#define BCM2835_IRQ_DMA(n)          BCM2835_BANK1(16 + (n)) /* n = 0..10 */
#define BCM2835_IRQ_DMA_SHARED      BCM2835_BANK1(27)       /* channels 11..14 */
#define BCM2835_IRQ_AUX             BCM2835_BANK1(29) /* mini-UART, SPI1, SPI2 */

/* GPU PEND2 (peripheral upper bank) */
#define BCM2835_IRQ_I2C_SPI_SLV     BCM2835_BANK2(11)
#define BCM2835_IRQ_GPIO0           BCM2835_BANK2(17)
#define BCM2835_IRQ_GPIO1           BCM2835_BANK2(18)
#define BCM2835_IRQ_GPIO2           BCM2835_BANK2(19)
#define BCM2835_IRQ_GPIO3           BCM2835_BANK2(20)
#define BCM2835_IRQ_I2C             BCM2835_BANK2(21)
#define BCM2835_IRQ_SPI             BCM2835_BANK2(22)
#define BCM2835_IRQ_PCM             BCM2835_BANK2(23)
#define BCM2835_IRQ_SDHOST          BCM2835_BANK2(24) /* Legacy SDHost (microSD slot) */
#define BCM2835_IRQ_UART            BCM2835_BANK2(25) /* PL011 UART0 */
#define BCM2835_IRQ_ARASAN_SDIO     BCM2835_BANK2(30) /* Arasan SDHCI / EMMC */

#ifndef IRQ_TYPE_LEVEL
#define IRQ_TYPE_LEVEL  2
#endif
#ifndef IRQ_TYPE_EDGE
#define IRQ_TYPE_EDGE   4
#endif


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_BCM2835_ARMCTRL_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Jonathan Elliot Peace <jep@alphabetiq.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 18 行

BCM2710 片上系统（SoC）的 Zephyr 中断请求（IRQ）编号布局：BCM2836 一级 ARM 本地中断控制器（L1 intc），其后级联 BCM2835 ARMC 外设中断控制器。

编号 0–31 保留给一级 ARM 本地中断控制器，实际仅使用 0–9，参见 `zephyr/dt-bindings/interrupt-controller/bcm2836-l1.h`。IRQ 8（一级 GPU IRQ）是级联入口；SoC 中断衔接代码在 `z_soc_irq_get_active` 内透明解析它，因此应用程序的中断服务程序（ISR）不会看到该编号。

ARMC 外设 IRQ 通过 `32 + (bank << 5) + bit` 编码：

| 寄存器组（bank） | IRQ 范围 | 对应位置 |
| --- | --- | --- |
| 0，基本组（basic） | 32–39 | `IRQ_BASIC_PENDING` 位 0–7 |
| 1，PEND1，GPU 0–31 | 64–95 | PEND1 |
| 2，PEND2，GPU 32–63 | 96–127 | PEND2 |

这种寄存器组移位编码（bank-shift encoding）为一级控制器保留区加上 32 的偏移，使 SoC 层的快捷／级联解码保持为对 BCM2835 ARMC 挂起寄存器布局的直接算术映射。

### 注释 3：原第 41 行

编号范围：32–39。

### 注释 4：原第 42 行

编号范围：64–95。

### 注释 5：原第 43 行

编号范围：96–127。

### 注释 6：原第 45 行

基本寄存器组快捷入口（basic bank shortcuts）。

### 注释 7：原第 55 行

GPU PEND1，外设低位寄存器组（peripheral lower bank）。

### 注释 8：原第 60 行

USB OTG，采用 Synopsys DWC2。根据 BCM2835 ARM Peripherals 数据手册第 7 章“ARM 外设中断表”（ARM peripherals interrupts table），它对应 GPU IRQ 9。

### 注释 9：原第 63 行

DWC2 USB OTG。

### 注释 10：原第 64 行

DMA 通道中断（channel IRQs）：通道 0–10 分别使用 PEND1 位 16–26 的专用中断线；通道 11–14 共享位 27。PEND1 位 28 对应“任意 DMA 通道”（any DMA channel）中断线，但此处未提供它。

### 注释 11：原第 68 行

`n` 的取值为 0–10。

### 注释 12：原第 69 行

通道（channels）11–14。

### 注释 13：原第 70 行

mini-UART、SPI1、SPI2 外设。

### 注释 14：原第 72 行

GPU PEND2，外设高位寄存器组（peripheral upper bank）。

### 注释 15：原第 81 行

传统 SDHost（Legacy SDHost），连接 microSD 卡槽。

### 注释 16：原第 82 行

PL011 UART0 外设。

### 注释 17：原第 83 行

Arasan SD 主机控制器接口（SDHCI）／EMMC。

### 注释 18：原第 94 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_BCM2835_ARMCTRL_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_supplement_reference/P005_zephyr__dt-bindings__interrupt-controller__bcm2835-armctrl.h_文件参考.md)

---

[返回大纲](大纲.md) · [下一章](P002_chat.h_源码浏览.md)
