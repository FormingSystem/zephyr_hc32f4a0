---
id: learning.zephyr-docs.api-source-compiler-device-reference.page-15
title: intc_exti_stm32.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_intc\_exti\_stm32.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html)。

## 15.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="foldopen00025"></a>
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
<a id="foldopen00039"></a>
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
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aintc__exti__stm32_8h_html_a1ca2a35dc6232df5abb6086d1a5e9264"></a>
<a id="aintc__exti__stm32_8h_html_a5b88085adfd3e17587b7c1f7a2c09501"></a>
<a id="aintc__exti__stm32_8h_html_a7780746237de7f19b5a0457f83b9208f"></a>
<a id="aintc__exti__stm32_8h_html_a7780746237de7f19b5a0457f83b9208fa1440b42239fcd4a958700da120c5de5f"></a>
<a id="aintc__exti__stm32_8h_html_a7780746237de7f19b5a0457f83b9208fa21e081ba1d5f8cc28758ddbd89dcf554"></a>
<a id="aintc__exti__stm32_8h_html_a7780746237de7f19b5a0457f83b9208faabd817ddd666342876a7f45a22599f9c"></a>
<a id="aintc__exti__stm32_8h_html_a7780746237de7f19b5a0457f83b9208fabbb2a1012aa1fea7568a33537702beb6"></a>
<a id="aintc__exti__stm32_8h_html_a86d158bbfe92d326ef6ef9a623bf6b8c"></a>
<a id="aintc__exti__stm32_8h_html_a86d158bbfe92d326ef6ef9a623bf6b8ca013afe4b3bfc4921f30dad835e7f87cc"></a>
<a id="aintc__exti__stm32_8h_html_a86d158bbfe92d326ef6ef9a623bf6b8ca8a53325045c0825c5fd379d83a04f5e4"></a>
<a id="aintc__exti__stm32_8h_html_a86d158bbfe92d326ef6ef9a623bf6b8caa44b00e6dd732140f0c152ec6a5ad0e0"></a>
<a id="aintc__exti__stm32_8h_html_a86d158bbfe92d326ef6ef9a623bf6b8cac1ab9fda0db1fb1a852bfe358c7e6485"></a>
<a id="aintc__exti__stm32_8h_html_a8ff30ebf5f3a25aa21ddc1aae8a0d96b"></a>
<a id="aintc__exti__stm32_8h_html_a9ed083565b9d11549c9841aee10d85fc"></a>
<a id="aintc__exti__stm32_8h_html_aaee82d8a7f1a4e88c507872eb6639e7b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright (c) 2025 Alexander Kozhinov <ak.alexander.kozhinov@gmail.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_EXTI_STM32_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_EXTI_STM32_H_

#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef enum {
        /* No trigger */
        STM32_EXTI_TRIG_NONE  = 0x0,
        /* Trigger on rising edge */
        STM32_EXTI_TRIG_RISING  = 0x1,
        /* Trigger on falling edge */
        STM32_EXTI_TRIG_FALLING = 0x2,
        /* Trigger on both rising and falling edge */
        STM32_EXTI_TRIG_BOTH = 0x3,
} stm32_exti_trigger_type;

typedef enum {
        /* Generate interrupts only */
        STM32_EXTI_MODE_IT  = 0x0,
        /* Generate events only */
        STM32_EXTI_MODE_EVENT  = 0x1,
        /* Generate interrupts and events */
        STM32_EXTI_MODE_BOTH = 0x2,
        /* Disable interrupts and events */
        STM32_EXTI_MODE_NONE = 0x3,
} stm32_exti_mode;

int stm32_exti_enable(uint32_t line_num, stm32_exti_trigger_type trigger,
                                          stm32_exti_mode mode);

int stm32_exti_disable(uint32_t line_num);

bool stm32_exti_is_pending(uint32_t line_num);

int stm32_exti_clear_pending(uint32_t line_num);

int stm32_exti_sw_interrupt(uint32_t line_num);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_EXTI_STM32_H_ */
```

## 15.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Alexander Kozhinov <ak.alexander.kozhinov@gmail.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 26 行

不触发（No Trigger）。

### 注释 3：原第 28 行

上升沿触发（Trigger on Rising Edge）。

### 注释 4：原第 30 行

下降沿触发（Trigger on Falling Edge）。

### 注释 5：原第 32 行

上升沿和下降沿均触发（Trigger on Both Edges）。

### 注释 6：原第 40 行

仅产生中断（interrupts）。

### 注释 7：原第 42 行

仅产生事件（events）。

### 注释 8：原第 44 行

同时产生中断和事件。

### 注释 9：原第 46 行

禁用中断和事件。

### 注释 10：原第 101 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_EXTI_STM32_H_`。

## 15.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [STM32_EXTI_TRIG_NONE](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html#a86d158bbfe92d326ef6ef9a623bf6b8caa44b00e6dd732140f0c152ec6a5ad0e0)
- [STM32_EXTI_TRIG_RISING](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html#a86d158bbfe92d326ef6ef9a623bf6b8cac1ab9fda0db1fb1a852bfe358c7e6485)
- [STM32_EXTI_TRIG_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html#a86d158bbfe92d326ef6ef9a623bf6b8ca8a53325045c0825c5fd379d83a04f5e4)
- [STM32_EXTI_TRIG_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html#a86d158bbfe92d326ef6ef9a623bf6b8ca013afe4b3bfc4921f30dad835e7f87cc)
- [stm32_exti_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html#a86d158bbfe92d326ef6ef9a623bf6b8c)
- [STM32_EXTI_MODE_IT](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html#a7780746237de7f19b5a0457f83b9208fa21e081ba1d5f8cc28758ddbd89dcf554)
- [STM32_EXTI_MODE_EVENT](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html#a7780746237de7f19b5a0457f83b9208faabd817ddd666342876a7f45a22599f9c)
- [STM32_EXTI_MODE_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html#a7780746237de7f19b5a0457f83b9208fabbb2a1012aa1fea7568a33537702beb6)
- [STM32_EXTI_MODE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html#a7780746237de7f19b5a0457f83b9208fa1440b42239fcd4a958700da120c5de5f)
- [stm32_exti_mode](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html#a7780746237de7f19b5a0457f83b9208f)
- [stm32_exti_enable](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html#a9ed083565b9d11549c9841aee10d85fc)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [stm32_exti_disable](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html#a1ca2a35dc6232df5abb6086d1a5e9264)
- [stm32_exti_is_pending](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html#aaee82d8a7f1a4e88c507872eb6639e7b)
- [stm32_exti_clear_pending](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html#a5b88085adfd3e17587b7c1f7a2c09501)
- [stm32_exti_sw_interrupt](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html#a8ff30ebf5f3a25aa21ddc1aae8a0d96b)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)

---

[上一章](P014_types.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P016_mchp_sam_d5x_e5x_clock.h_源码浏览.md)
