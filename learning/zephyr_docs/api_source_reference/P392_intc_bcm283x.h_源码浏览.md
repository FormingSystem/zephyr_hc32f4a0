---
id: learning.zephyr-docs.api-source-reference.page-392
title: intc_bcm283x.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__bcm283x_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第392章\_intc\_bcm283x.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intc__bcm283x_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intc__bcm283x_8h.html)。

## 392.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00056"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="agroup__intc__bcm283x_html_ga2c44c3f942a7cc764fadf1502b9ecc49"></a>
<a id="agroup__intc__bcm283x_html_ga2fe5a8b685d905243c05558a13212b3b"></a>
<a id="agroup__intc__bcm283x_html_ga4ed816681fd685c63a9b602f5390da97"></a>
<a id="agroup__intc__bcm283x_html_ga53c43b0af32be13e55f15dfb4adaa5b0"></a>
<a id="agroup__intc__bcm283x_html_ga747b5793762f454f37f2aea5a0a98367"></a>
<a id="agroup__intc__bcm283x_html_ga75f8a727ac5a2f6a303031ca916c6552"></a>
<a id="agroup__intc__bcm283x_html_ga8172bde4064553565f1a2f004e7246a9"></a>
<a id="agroup__intc__bcm283x_html_gaa413beb6b63102a3f8fe61d7d1e96a8d"></a>
<a id="agroup__intc__bcm283x_html_gacfe08085a3ca52ac0fb3123d0213359c"></a>
<a id="agroup__intc__bcm283x_html_gaea4d0829c483de09258ff7500d49973a"></a>
<a id="astdint_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Jonathan Elliot Peace <jep@alphabetiq.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_DRIVERS_INTERRUPT_CONTROLLER_INTC_BCM283X_H_
#define ZEPHYR_DRIVERS_INTERRUPT_CONTROLLER_INTC_BCM283X_H_

#include <stdint.h>


#define BCM283X_ARMC_IRQ_BASE   32U

#define BCM283X_ARMC_IRQ_LIMIT  (BCM283X_ARMC_IRQ_BASE + 96U)

#define BCM283X_IRQ_IS_L1(irq)    ((irq) < BCM283X_ARMC_IRQ_BASE)

#define BCM283X_IRQ_IS_ARMC(irq)  ((irq) >= BCM283X_ARMC_IRQ_BASE && \
                                   (irq) < BCM283X_ARMC_IRQ_LIMIT)

#define BCM2836_L1_IRQ_GPU_BIT   8U

#define BCM2836_L1_IRQ_PMU_BIT   9U

void bcm2836_l1_intc_init(void);

void bcm2836_l1_intc_irq_enable(unsigned int irq);

void bcm2836_l1_intc_irq_disable(unsigned int irq);

int  bcm2836_l1_intc_irq_is_enabled(unsigned int irq);

unsigned int bcm2836_l1_intc_irq_get_active(void);

void bcm2835_armctrl_ic_init(void);

void bcm2835_armctrl_ic_irq_enable(unsigned int irq);

void bcm2835_armctrl_ic_irq_disable(unsigned int irq);

int  bcm2835_armctrl_ic_irq_is_enabled(unsigned int irq);

unsigned int bcm2835_armctrl_ic_irq_get_active(void);


#endif /* ZEPHYR_DRIVERS_INTERRUPT_CONTROLLER_INTC_BCM283X_H_ */
```

## 392.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Jonathan Elliot Peace <jep@alphabetiq.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 170 行

头文件保护宏（Header guard）标记：`ZEPHYR_DRIVERS_INTERRUPT_CONTROLLER_INTC_BCM283X_H_`。

## 392.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intc__bcm283x_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [bcm2836_l1_intc_init](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#gaea4d0829c483de09258ff7500d49973a)
- [bcm2836_l1_intc_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga747b5793762f454f37f2aea5a0a98367)
- [bcm2836_l1_intc_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga8172bde4064553565f1a2f004e7246a9)
- [bcm2836_l1_intc_irq_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga2fe5a8b685d905243c05558a13212b3b)
- [bcm2836_l1_intc_irq_get_active](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#gacfe08085a3ca52ac0fb3123d0213359c)
- [bcm2835_armctrl_ic_init](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga53c43b0af32be13e55f15dfb4adaa5b0)
- [bcm2835_armctrl_ic_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#gaa413beb6b63102a3f8fe61d7d1e96a8d)
- [bcm2835_armctrl_ic_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga2c44c3f942a7cc764fadf1502b9ecc49)
- [bcm2835_armctrl_ic_irq_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga75f8a727ac5a2f6a303031ca916c6552)
- [bcm2835_armctrl_ic_irq_get_active](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html#ga4ed816681fd685c63a9b602f5390da97)

---

[上一章](P391_instr_mem.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P393_intc_irqmp.h_源码浏览.md)
