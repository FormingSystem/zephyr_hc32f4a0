---
id: learning.zephyr-docs.api-source-network-reference.page-7
title: gpio_intc_stm32.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_gpio\_intc\_stm32.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html)。

## 7.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00049"></a>
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
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="agpio__intc__stm32_8h_html_a03badd2828ca67e3f8adadc75fec2bd2"></a>
<a id="agpio__intc__stm32_8h_html_a0bb3bd355218c41e9173f061f46ec997"></a>
<a id="agpio__intc__stm32_8h_html_a21b0c2213fbcdf179c8b4bdb29561863"></a>
<a id="agpio__intc__stm32_8h_html_a23b9ea466101b4367232237ab5a9a42f"></a>
<a id="agpio__intc__stm32_8h_html_a4a750e87f445487c517f24a0266f6a4b"></a>
<a id="agpio__intc__stm32_8h_html_a52c69f3ce04242217e00981c1315a374"></a>
<a id="agpio__intc__stm32_8h_html_a69ad9c575223c813f484423e56200560"></a>
<a id="agpio__intc__stm32_8h_html_a8f9c3db22937ebe4382215227c410b61"></a>
<a id="agpio__intc__stm32_8h_html_a8f9c3db22937ebe4382215227c410b61a2a13de1280bfac5e1cb484db56843e2c"></a>
<a id="agpio__intc__stm32_8h_html_a8f9c3db22937ebe4382215227c410b61a2d20b462dad9d074ce7bb1479d3066c9"></a>
<a id="agpio__intc__stm32_8h_html_a8f9c3db22937ebe4382215227c410b61a46af906f79e53b4301c50292840bd301"></a>
<a id="agpio__intc__stm32_8h_html_a8f9c3db22937ebe4382215227c410b61a601ac25a6a83f5a01dc8ce8bb8f547ae"></a>
<a id="agpio__intc__stm32_8h_html_a8f9c3db22937ebe4382215227c410b61a961343f06deca1a4ae9288b81e167048"></a>
<a id="agpio__intc__stm32_8h_html_a8f9c3db22937ebe4382215227c410b61adb4cda594aec45886263f14968e6b3d2"></a>
<a id="agpio__intc__stm32_8h_html_ad1c9359de9847ebd2670987302c48f8d"></a>
<a id="agroup__gpio__interface_html_ga38179eb7a46a743c12cfac28f347fb34"></a>
<a id="agroup__gpio__interface_html_ga7f40ed51f14fd8000e9b52ab347b273f"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright (c) 2016 Open-RnD Sp. z o.o.
 * Copyright (c) 2024 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_GPIO_INTC_STM32_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_GPIO_INTC_STM32_H_

#include <zephyr/types.h>
#include <zephyr/drivers/gpio.h>

typedef uint32_t stm32_gpio_irq_line_t;

stm32_gpio_irq_line_t stm32_gpio_intc_get_pin_irq_line(uint32_t port, gpio_pin_t pin);

void stm32_gpio_intc_enable_line(stm32_gpio_irq_line_t line);

void stm32_gpio_intc_disable_line(stm32_gpio_irq_line_t line);

enum stm32_gpio_irq_trigger {
        /* No trigger */
        STM32_GPIO_IRQ_TRIG_NONE  = 0x0,
        /* Trigger on rising edge */
        STM32_GPIO_IRQ_TRIG_RISING  = 0x1,
        /* Trigger on falling edge */
        STM32_GPIO_IRQ_TRIG_FALLING = 0x2,
        /* Trigger on both rising and falling edge */
        STM32_GPIO_IRQ_TRIG_BOTH = 0x3,
        /* Trigger on high level */
        STM32_GPIO_IRQ_TRIG_HIGH_LEVEL = 0x4,
        /* Trigger on low level */
        STM32_GPIO_IRQ_TRIG_LOW_LEVEL = 0x5
};

void stm32_gpio_intc_select_line_trigger(stm32_gpio_irq_line_t line, uint32_t trg);

typedef void (*stm32_gpio_irq_cb_t)(gpio_port_pins_t pin, void *user);

int stm32_gpio_intc_set_irq_callback(stm32_gpio_irq_line_t line,
                                        stm32_gpio_irq_cb_t cb, void *user);

void stm32_gpio_intc_remove_irq_callback(stm32_gpio_irq_line_t line);


#if defined(CONFIG_EXTI_STM32)  /* EXTI-specific extensions */
void stm32_exti_set_line_src_port(gpio_pin_t line, uint32_t port);

uint32_t stm32_exti_get_line_src_port(gpio_pin_t line);
#endif /* CONFIG_EXTI_STM32 */

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_GPIO_INTC_STM32_H_ */
```

## 7.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Open-RnD Sp. z o.o.。

版权（Copyright）：© 2024 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 50 行

不触发（No Trigger）。

### 注释 3：原第 52 行

上升沿触发（Trigger on Rising Edge）。

### 注释 4：原第 54 行

下降沿触发（Trigger on Falling Edge）。

### 注释 5：原第 56 行

上升沿和下降沿均触发（Trigger on Both Edges）。

### 注释 6：原第 58 行

高电平触发（Trigger on High Level）。

### 注释 7：原第 60 行

低电平触发（Trigger on Low Level）。

### 注释 8：原第 102 行

外部中断专用扩展（EXTI-Specific Extensions）。

### 注释 9：原第 118 行

条件编译配置（Configuration）标记：`CONFIG_EXTI_STM32`。

### 注释 10：原第 120 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_GPIO_INTC_STM32_H_`。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [stm32_gpio_irq_line_t](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html#a52c69f3ce04242217e00981c1315a374)
- [stm32_gpio_intc_get_pin_irq_line](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html#a03badd2828ca67e3f8adadc75fec2bd2)
- [gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)
- [stm32_gpio_intc_enable_line](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html#ad1c9359de9847ebd2670987302c48f8d)
- [stm32_gpio_intc_disable_line](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html#a0bb3bd355218c41e9173f061f46ec997)
- [stm32_gpio_irq_trigger](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html#a8f9c3db22937ebe4382215227c410b61)
- [STM32_GPIO_IRQ_TRIG_NONE](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html#a8f9c3db22937ebe4382215227c410b61adb4cda594aec45886263f14968e6b3d2)
- [STM32_GPIO_IRQ_TRIG_RISING](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html#a8f9c3db22937ebe4382215227c410b61a601ac25a6a83f5a01dc8ce8bb8f547ae)
- [STM32_GPIO_IRQ_TRIG_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html#a8f9c3db22937ebe4382215227c410b61a2d20b462dad9d074ce7bb1479d3066c9)
- [STM32_GPIO_IRQ_TRIG_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html#a8f9c3db22937ebe4382215227c410b61a46af906f79e53b4301c50292840bd301)
- [STM32_GPIO_IRQ_TRIG_HIGH_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html#a8f9c3db22937ebe4382215227c410b61a961343f06deca1a4ae9288b81e167048)
- [STM32_GPIO_IRQ_TRIG_LOW_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html#a8f9c3db22937ebe4382215227c410b61a2a13de1280bfac5e1cb484db56843e2c)
- [stm32_gpio_intc_select_line_trigger](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html#a23b9ea466101b4367232237ab5a9a42f)
- [stm32_gpio_irq_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html#a69ad9c575223c813f484423e56200560)
- [gpio_port_pins_t](../hardware/P266_GPIO公共接口.md#ga7f40ed51f14fd8000e9b52ab347b273f)
- [stm32_gpio_intc_set_irq_callback](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html#a4a750e87f445487c517f24a0266f6a4b)
- [stm32_gpio_intc_remove_irq_callback](https://docs.zephyrproject.org/latest/doxygen/html/gpio__intc__stm32_8h.html#a21b0c2213fbcdf179c8b4bdb29561863)
- [gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)

---

[上一章](P006_ethernet_bridge.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P008_i3c.h_源码浏览.md)
