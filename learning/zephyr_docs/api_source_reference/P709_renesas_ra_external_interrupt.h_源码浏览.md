---
id: learning.zephyr-docs.api-source-reference.page-709
title: renesas_ra_external_interrupt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__external__interrupt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第709章\_renesas\_ra\_external\_interrupt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__external__interrupt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__external__interrupt_8h.html)。

## 709.1\_原始可见代码（Source Code）

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
<a id="foldopen00021"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="agroup__gpio__interface__backend_html_ga4ea6fd78423e6e3004702b599bc7b12d"></a>
<a id="agroup__gpio__interface__backend_html_ga82f0562c44cf0f76cc7e16d606a975db"></a>
<a id="agroup__gpio__interface_html_ga38179eb7a46a743c12cfac28f347fb34"></a>
<a id="arenesas__ra__external__interrupt_8h_html_ab32020826df52c8ae436a1160d5b0605"></a>
<a id="arenesas__ra__external__interrupt_8h_html_ab5b65b767c07a8f2c532e0ad0f3ef450"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructgpio__ra__callback_html"></a>
<a id="astructgpio__ra__callback_html_a5c89f78aba384aa8fcbef25ae48c3bcd"></a>
<a id="astructgpio__ra__callback_html_a5e89aec076339fb4debe3a6b2041cf34"></a>
<a id="astructgpio__ra__callback_html_a78fde66020bebe07d34c63ade045d269"></a>
<a id="astructgpio__ra__callback_html_acb33518d1af46916fbbe0acd666b1bbc"></a>
<a id="astructgpio__ra__callback_html_ae2a5801c1a3f38dbb1c7b83fcf6373d5"></a>
<a id="astructgpio__ra__callback_html_afe6c9d43bf51368103f8210e13b6c550"></a>

```c
/*
 * Copyright (c) 2024 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_MISC_RENESAS_RA_EXTERNAL_INTERRUPT_RENESAS_RA_EXTERNAL_INTERRUPT_H_
#define ZEPHYR_INCLUDE_DRIVERS_MISC_RENESAS_RA_EXTERNAL_INTERRUPT_RENESAS_RA_EXTERNAL_INTERRUPT_H_

#include <zephyr/drivers/gpio.h>

struct gpio_ra_callback {
        struct device *port;
        uint8_t port_num;
        uint8_t pin;
        enum gpio_int_trig trigger;
        enum gpio_int_mode mode;
        void (*isr)(const struct device *dev, gpio_pin_t pin);
};

int gpio_ra_interrupt_set(const struct device *dev, struct gpio_ra_callback *callback);

void gpio_ra_interrupt_unset(const struct device *dev, uint8_t port_num, uint8_t pin);


#endif
```

## 709.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 709.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__external__interrupt_8h.html)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [gpio_ra_callback](../device_power_control_model_reference/P014_gpio_ra_callback_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [port](../device_power_control_model_reference/P014_gpio_ra_callback_结构体.md#ae2a5801c1a3f38dbb1c7b83fcf6373d5)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [port_num](../device_power_control_model_reference/P014_gpio_ra_callback_结构体.md#acb33518d1af46916fbbe0acd666b1bbc)
- [pin](../device_power_control_model_reference/P014_gpio_ra_callback_结构体.md#a5e89aec076339fb4debe3a6b2041cf34)
- [gpio_int_trig](../hardware/P271_GPIO驱动后端.md#ga4ea6fd78423e6e3004702b599bc7b12d)
- [trigger](../device_power_control_model_reference/P014_gpio_ra_callback_结构体.md#a78fde66020bebe07d34c63ade045d269)
- [gpio_int_mode](../hardware/P271_GPIO驱动后端.md#ga82f0562c44cf0f76cc7e16d606a975db)
- [mode](../device_power_control_model_reference/P014_gpio_ra_callback_结构体.md#a5c89f78aba384aa8fcbef25ae48c3bcd)
- [isr](../device_power_control_model_reference/P014_gpio_ra_callback_结构体.md#afe6c9d43bf51368103f8210e13b6c550)
- [gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)
- [gpio_ra_interrupt_set](https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__external__interrupt_8h.html#ab32020826df52c8ae436a1160d5b0605)
- [gpio_ra_interrupt_unset](https://docs.zephyrproject.org/latest/doxygen/html/renesas__ra__external__interrupt_8h.html#ab5b65b767c07a8f2c532e0ad0f3ef450)
- [gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [gpio_ra_callback::mode](../device_power_control_model_reference/P014_gpio_ra_callback_结构体.md#a5c89f78aba384aa8fcbef25ae48c3bcd)
- [gpio_ra_callback::pin](../device_power_control_model_reference/P014_gpio_ra_callback_结构体.md#a5e89aec076339fb4debe3a6b2041cf34)
- [gpio_ra_callback::trigger](../device_power_control_model_reference/P014_gpio_ra_callback_结构体.md#a78fde66020bebe07d34c63ade045d269)
- [gpio_ra_callback::port_num](../device_power_control_model_reference/P014_gpio_ra_callback_结构体.md#acb33518d1af46916fbbe0acd666b1bbc)
- [gpio_ra_callback::port](../device_power_control_model_reference/P014_gpio_ra_callback_结构体.md#ae2a5801c1a3f38dbb1c7b83fcf6373d5)
- [gpio_ra_callback::isr](../device_power_control_model_reference/P014_gpio_ra_callback_结构体.md#afe6c9d43bf51368103f8210e13b6c550)

---

[上一章](P708_renesas_elc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P710_renesas_rx_cgc.h_源码浏览.md)
