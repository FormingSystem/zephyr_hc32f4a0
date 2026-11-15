---
id: learning.zephyr-docs.api-source-reference.page-527
title: microchip-smartfusion2-irq.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/microchip-smartfusion2-irq_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第527章\_microchip-smartfusion2-irq.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/microchip-smartfusion2-irq_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/microchip-smartfusion2-irq_8h.html)。

## 527.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00173"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright Bavariamatic GmbH
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_MICROCHIP_SMARTFUSION2_IRQ_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_MICROCHIP_SMARTFUSION2_IRQ_H_



#define IRQ_TYPE_NONE                      0
#define IRQ_TYPE_EDGE_RISING               1
#define IRQ_TYPE_EDGE_FALLING              2
#define IRQ_TYPE_EDGE_BOTH                 (IRQ_TYPE_EDGE_FALLING | IRQ_TYPE_EDGE_RISING)
#define IRQ_TYPE_LEVEL_HIGH                4
#define IRQ_TYPE_LEVEL_LOW                 8

#define SMARTFUSION2_IRQ_WDOG_WAKEUP      0
#define SMARTFUSION2_IRQ_RTC_WAKEUP       1
#define SMARTFUSION2_IRQ_SPI0             2
#define SMARTFUSION2_IRQ_SPI1             3
#define SMARTFUSION2_IRQ_I2C0             4
#define SMARTFUSION2_IRQ_I2C1             7
#define SMARTFUSION2_IRQ_UART0            10
#define SMARTFUSION2_IRQ_UART1            11
#define SMARTFUSION2_IRQ_ETHERNET_MAC     12
#define SMARTFUSION2_IRQ_PDMA             13
#define SMARTFUSION2_IRQ_TIMER1           14
#define SMARTFUSION2_IRQ_TIMER2           15
#define SMARTFUSION2_IRQ_CAN              16
#define SMARTFUSION2_IRQ_COMBLK           19
#define SMARTFUSION2_IRQ_USB              20
#define SMARTFUSION2_IRQ_USB_DMA          21
#define SMARTFUSION2_IRQ_PLL_LOCK         22
#define SMARTFUSION2_IRQ_PLL_LOCK_LOST    23
#define SMARTFUSION2_IRQ_COMM_SWITCH_ERR  24
#define SMARTFUSION2_IRQ_CACHE_ERROR      25
#define SMARTFUSION2_IRQ_DDR              26
#define SMARTFUSION2_IRQ_HPDMA_COMPLETE   27
#define SMARTFUSION2_IRQ_HPDMA_ERROR      28
#define SMARTFUSION2_IRQ_ECC_ERROR        29
#define SMARTFUSION2_IRQ_MDDR_IO_CALIB    30
#define SMARTFUSION2_IRQ_FAB_PLL_LOCK     31
#define SMARTFUSION2_IRQ_FAB_PLL_LOCK_LOST 32
#define SMARTFUSION2_IRQ_FIC64            33
#define SMARTFUSION2_IRQ_GPIO0            50

#define M2S_IRQ_WDOG                      SMARTFUSION2_IRQ_WDOG_WAKEUP
#define M2S_IRQ_RTC_WAKEUP                SMARTFUSION2_IRQ_RTC_WAKEUP
#define M2S_IRQ_RTC_MATCH                 SMARTFUSION2_IRQ_RTC_WAKEUP
#define M2S_IRQ_SPI0                      SMARTFUSION2_IRQ_SPI0
#define M2S_IRQ_SPI1                      SMARTFUSION2_IRQ_SPI1
#define M2S_IRQ_I2C0_MAIN                 SMARTFUSION2_IRQ_I2C0
#define M2S_IRQ_I2C0_ALERT                SMARTFUSION2_IRQ_I2C0
#define M2S_IRQ_I2C0_SUS                  SMARTFUSION2_IRQ_I2C0
#define M2S_IRQ_I2C1_MAIN                 SMARTFUSION2_IRQ_I2C1
#define M2S_IRQ_I2C1_ALERT                SMARTFUSION2_IRQ_I2C1
#define M2S_IRQ_I2C1_SUS                  SMARTFUSION2_IRQ_I2C1
#define M2S_IRQ_UART0                     SMARTFUSION2_IRQ_UART0
#define M2S_IRQ_UART1                     SMARTFUSION2_IRQ_UART1
#define M2S_IRQ_MAC0                      SMARTFUSION2_IRQ_ETHERNET_MAC
#define M2S_IRQ_DMA                       SMARTFUSION2_IRQ_PDMA
#define M2S_IRQ_TIMER1                    SMARTFUSION2_IRQ_TIMER1
#define M2S_IRQ_TIMER2                    SMARTFUSION2_IRQ_TIMER2
#define M2S_IRQ_CAN0                      SMARTFUSION2_IRQ_CAN
#define M2S_IRQ_CAN1                      SMARTFUSION2_IRQ_CAN
#define M2S_IRQ_USB_MC                    SMARTFUSION2_IRQ_USB
#define M2S_IRQ_USB_DMA                   SMARTFUSION2_IRQ_USB_DMA
#define M2S_IRQ_GPIO0                     SMARTFUSION2_IRQ_GPIO0



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_MICROCHIP_SMARTFUSION2_IRQ_H_ */
```

## 527.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright Bavariamatic GmbH。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 173 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_MICROCHIP_SMARTFUSION2_IRQ_H_`。

## 527.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/microchip-smartfusion2-irq_8h.html)

---

[上一章](P526_microchip-smartfusion2-clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P528_midi2.h_源码浏览.md)
