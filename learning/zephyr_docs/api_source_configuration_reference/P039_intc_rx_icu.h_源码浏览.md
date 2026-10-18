---
id: learning.zephyr-docs.api-source-configuration-reference.page-39
title: intc_rx_icu.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_intc\_rx\_icu.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h.html)。

## 39.1\_原始可见代码（Source Code）

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
<a id="foldopen00014"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="foldopen00022"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="foldopen00027"></a>
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
<a id="aintc__rx__icu_8h_html_a03cc2d22194251dd8942e2d95c3b3451"></a>
<a id="aintc__rx__icu_8h_html_a32aadebfbc450fa354d6d176289fec0d"></a>
<a id="aintc__rx__icu_8h_html_a43836995901c04ab8c734f28c4e57e73"></a>
<a id="aintc__rx__icu_8h_html_a4b89ff23dc526521af51a61f6d34431a"></a>
<a id="aintc__rx__icu_8h_html_a4b89ff23dc526521af51a61f6d34431aab7d4f4d93c7097db340059c2f786a81d"></a>
<a id="aintc__rx__icu_8h_html_a4b89ff23dc526521af51a61f6d34431aad3a3540fce0ec8126751c4389993ba01"></a>
<a id="aintc__rx__icu_8h_html_ac9bdc620911c67f607cf9ec5a49fd1b1"></a>
<a id="aintc__rx__icu_8h_html_ae5e7618b4871363e4b9443cbe01ef86d"></a>
<a id="aintc__rx__icu_8h_html_aea25818bb1e7cf4bc3d1a6fce309207e"></a>
<a id="aintc__rx__icu_8h_html_aea25818bb1e7cf4bc3d1a6fce309207ea0d5c2ec086858519e4457ac46015d1a3"></a>
<a id="aintc__rx__icu_8h_html_aea25818bb1e7cf4bc3d1a6fce309207ea3d05da80f76b235919b656535bf83650"></a>
<a id="aintc__rx__icu_8h_html_aea25818bb1e7cf4bc3d1a6fce309207eae3add732d10a107ec6be56d181e4cad4"></a>
<a id="aintc__rx__icu_8h_html_aea25818bb1e7cf4bc3d1a6fce309207eaf18832e32784f7f1a0291da77a31a432"></a>
<a id="aintc__rx__icu_8h_html_aea25818bb1e7cf4bc3d1a6fce309207eaffba1ca9f0f29872c1381311465ac6e8"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructrx__irq__dig__filt__s_html"></a>
<a id="astructrx__irq__dig__filt__s_html_a9338cdaf9596b591bc6ddd27a3a8cb97"></a>
<a id="astructrx__irq__dig__filt__s_html_a97fcdaa2ec47cb1714c48e5f67e4b069"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_RX_ICU_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_RX_ICU_H_

#define IRQ_CFG_PCLK_DIV1  (0)
#define IRQ_CFG_PCLK_DIV8  (1)
#define IRQ_CFG_PCLK_DIV32 (2)
#define IRQ_CFG_PCLK_DIV64 (3)

enum icu_irq_mode {
        ICU_LOW_LEVEL,
        ICU_FALLING,
        ICU_RISING,
        ICU_BOTH_EDGE,
        ICU_MODE_NONE,
};

enum icu_dig_filt {
        DISENABLE_DIG_FILT,
        ENABLE_DIG_FILT,
};

typedef struct rx_irq_dig_filt_s {
        uint8_t filt_clk_div; /* PCLK divisor setting for the input pin digital filter. */
        uint8_t filt_enable;  /* Filter enable setting for the input pin digital filter. */
} rx_irq_dig_filt_t;

extern void rx_icu_clear_ir_flag(unsigned int irqn);
extern int rx_icu_get_ir_flag(unsigned int irqn);
extern int rx_icu_set_irq_control(unsigned int pin_irqn, enum icu_irq_mode mode);
extern void rx_icu_set_irq_dig_filt(unsigned int pin_irqn, rx_irq_dig_filt_t dig_filt);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_RX_ICU_H_ */
```

## 39.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 28 行

输入引脚数字滤波器的 PCLK 分频设置。

### 注释 3：原第 29 行

输入引脚数字滤波器的滤波使能设置。

### 注释 4：原第 37 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_RX_ICU_H_`。

## 39.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h.html)
- [icu_irq_mode](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h.html#aea25818bb1e7cf4bc3d1a6fce309207e)
- [ICU_LOW_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h.html#aea25818bb1e7cf4bc3d1a6fce309207eae3add732d10a107ec6be56d181e4cad4)
- [ICU_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h.html#aea25818bb1e7cf4bc3d1a6fce309207eaf18832e32784f7f1a0291da77a31a432)
- [ICU_RISING](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h.html#aea25818bb1e7cf4bc3d1a6fce309207ea0d5c2ec086858519e4457ac46015d1a3)
- [ICU_BOTH_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h.html#aea25818bb1e7cf4bc3d1a6fce309207ea3d05da80f76b235919b656535bf83650)
- [ICU_MODE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h.html#aea25818bb1e7cf4bc3d1a6fce309207eaffba1ca9f0f29872c1381311465ac6e8)
- [icu_dig_filt](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h.html#a4b89ff23dc526521af51a61f6d34431a)
- [DISENABLE_DIG_FILT](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h.html#a4b89ff23dc526521af51a61f6d34431aad3a3540fce0ec8126751c4389993ba01)
- [ENABLE_DIG_FILT](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h.html#a4b89ff23dc526521af51a61f6d34431aab7d4f4d93c7097db340059c2f786a81d)
- [rx_irq_dig_filt_s](../device_power_control_model_reference/P077_rx_irq_dig_filt_s_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [filt_clk_div](../device_power_control_model_reference/P077_rx_irq_dig_filt_s_结构体.md#a97fcdaa2ec47cb1714c48e5f67e4b069)
- [filt_enable](../device_power_control_model_reference/P077_rx_irq_dig_filt_s_结构体.md#a9338cdaf9596b591bc6ddd27a3a8cb97)
- [rx_irq_dig_filt_t](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h.html#ae5e7618b4871363e4b9443cbe01ef86d)
- [rx_icu_clear_ir_flag](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h.html#a03cc2d22194251dd8942e2d95c3b3451)
- [rx_icu_get_ir_flag](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h.html#a43836995901c04ab8c734f28c4e57e73)
- [rx_icu_set_irq_control](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h.html#a32aadebfbc450fa354d6d176289fec0d)
- [rx_icu_set_irq_dig_filt](https://docs.zephyrproject.org/latest/doxygen/html/intc__rx__icu_8h.html#ac9bdc620911c67f607cf9ec5a49fd1b1)
- [rx_irq_dig_filt_s::filt_enable](../device_power_control_model_reference/P077_rx_irq_dig_filt_s_结构体.md#a9338cdaf9596b591bc6ddd27a3a8cb97)
- [rx_irq_dig_filt_s::filt_clk_div](../device_power_control_model_reference/P077_rx_irq_dig_filt_s_结构体.md#a97fcdaa2ec47cb1714c48e5f67e4b069)

---

[上一章](P038_inspect.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P040_intel-ioapic.h_源码浏览.md)
