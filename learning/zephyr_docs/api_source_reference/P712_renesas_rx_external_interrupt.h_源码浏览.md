---
id: learning.zephyr-docs.api-source-reference.page-712
title: renesas_rx_external_interrupt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__external__interrupt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第712章\_renesas\_rx\_external\_interrupt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__external__interrupt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__external__interrupt_8h.html)。

## 712.1\_原始可见代码（Source Code）

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
<a id="foldopen00022"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="agroup__gpio__interface__backend_html_ga4ea6fd78423e6e3004702b599bc7b12d"></a>
<a id="agroup__gpio__interface__backend_html_ga82f0562c44cf0f76cc7e16d606a975db"></a>
<a id="agroup__gpio__interface_html_ga38179eb7a46a743c12cfac28f347fb34"></a>
<a id="arenesas__rx__external__interrupt_8h_html_aa4e8687d852850bd1ace1fafba911bce"></a>
<a id="arenesas__rx__external__interrupt_8h_html_aaee6debb5a530f1202bf04f05be3ba98"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructgpio__rx__callback_html"></a>
<a id="astructgpio__rx__callback_html_a325319906ec519a836a1025831d3ca9b"></a>
<a id="astructgpio__rx__callback_html_a3d57065fd5dca68a35e33a1d8c195939"></a>
<a id="astructgpio__rx__callback_html_a46b0d0b6c5a088c8f142f222c1044327"></a>
<a id="astructgpio__rx__callback_html_a7bbf270c50f0ac44dbf5a1a41773ad77"></a>
<a id="astructgpio__rx__callback_html_aa15600e26b37674069c6d3c66aa60d4d"></a>
<a id="astructgpio__rx__callback_html_ad2e07a69f97532116b893554b6841d52"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MISC_RENESAS_RX_EXTERNAL_INTERRUPT_RENESAS_RX_EXTERNAL_INTERRUPT_H_
#define ZEPHYR_INCLUDE_DRIVERS_MISC_RENESAS_RX_EXTERNAL_INTERRUPT_RENESAS_RX_EXTERNAL_INTERRUPT_H_

#include <zephyr/drivers/gpio.h>

struct gpio_rx_callback {
        struct device *port;
        uint8_t port_num;
        uint8_t pin;
        enum gpio_int_trig trigger;
        enum gpio_int_mode mode;
        void (*isr)(const struct device *dev, gpio_pin_t pin);
};

int gpio_rx_interrupt_set(const struct device *dev, struct gpio_rx_callback *callback);

void gpio_rx_interrupt_unset(const struct device *dev, uint8_t port_num, uint8_t pin);


#endif
```

## 712.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 712.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__external__interrupt_8h.html)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [gpio_rx_callback](../device_power_control_model_reference/P015_gpio_rx_callback_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [port](../device_power_control_model_reference/P015_gpio_rx_callback_结构体.md#a3d57065fd5dca68a35e33a1d8c195939)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [port_num](../device_power_control_model_reference/P015_gpio_rx_callback_结构体.md#a46b0d0b6c5a088c8f142f222c1044327)
- [pin](../device_power_control_model_reference/P015_gpio_rx_callback_结构体.md#ad2e07a69f97532116b893554b6841d52)
- [gpio_int_trig](../hardware/P271_GPIO驱动后端.md#ga4ea6fd78423e6e3004702b599bc7b12d)
- [trigger](../device_power_control_model_reference/P015_gpio_rx_callback_结构体.md#a7bbf270c50f0ac44dbf5a1a41773ad77)
- [gpio_int_mode](../hardware/P271_GPIO驱动后端.md#ga82f0562c44cf0f76cc7e16d606a975db)
- [mode](../device_power_control_model_reference/P015_gpio_rx_callback_结构体.md#a325319906ec519a836a1025831d3ca9b)
- [isr](../device_power_control_model_reference/P015_gpio_rx_callback_结构体.md#aa15600e26b37674069c6d3c66aa60d4d)
- [gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)
- [gpio_rx_interrupt_set](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__external__interrupt_8h.html#aaee6debb5a530f1202bf04f05be3ba98)
- [gpio_rx_interrupt_unset](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__external__interrupt_8h.html#aa4e8687d852850bd1ace1fafba911bce)
- [gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [gpio_rx_callback::mode](../device_power_control_model_reference/P015_gpio_rx_callback_结构体.md#a325319906ec519a836a1025831d3ca9b)
- [gpio_rx_callback::port](../device_power_control_model_reference/P015_gpio_rx_callback_结构体.md#a3d57065fd5dca68a35e33a1d8c195939)
- [gpio_rx_callback::port_num](../device_power_control_model_reference/P015_gpio_rx_callback_结构体.md#a46b0d0b6c5a088c8f142f222c1044327)
- [gpio_rx_callback::trigger](../device_power_control_model_reference/P015_gpio_rx_callback_结构体.md#a7bbf270c50f0ac44dbf5a1a41773ad77)
- [gpio_rx_callback::isr](../device_power_control_model_reference/P015_gpio_rx_callback_结构体.md#aa15600e26b37674069c6d3c66aa60d4d)
- [gpio_rx_callback::pin](../device_power_control_model_reference/P015_gpio_rx_callback_结构体.md#ad2e07a69f97532116b893554b6841d52)

---

[上一章](P711_renesas_rx_dtc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P713_renesas_rz_cgc.h_源码浏览.md)
