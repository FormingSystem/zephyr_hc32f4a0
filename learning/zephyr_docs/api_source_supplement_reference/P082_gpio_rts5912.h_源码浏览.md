---
id: learning.zephyr-docs.api-source-supplement-reference.page-82
title: gpio_rts5912.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__rts5912_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第82章\_gpio\_rts5912.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gpio__rts5912_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gpio__rts5912_8h.html)。

## 82.1\_原始可见代码（Source Code）

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
<a id="adevice_8h_html"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="agpio__rts5912_8h_html_a62065211bcb72d822eeccccc6e51dc51"></a>
<a id="agpio__rts5912_8h_html_a8640c6a53deb21cee7bc6be80b1581df"></a>
<a id="agpio__rts5912_8h_html_a955c6e7b8922a236de987c66596d28b2"></a>
<a id="agpio__rts5912_8h_html_acfacb1e55d774da53cab6e9fda59c25b"></a>
<a id="agroup__devicetree-generic-id_html_gab7d23294a6bf7fd44a98b48ec47d8a79"></a>
<a id="agroup__devicetree-reg-prop_html_gac6d8279c32351ced4c0ac7f32270974e"></a>
<a id="agroup__gpio__interface_html_ga38179eb7a46a743c12cfac28f347fb34"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructgpio__dt__spec_html"></a>

```c
/*
 * SPDX-License-Identifier: Apache-2.0
 *
 * Copyright (c) 2024 Realtek Semiconductor Corporation, SIBG-SD7
 * Author: Lin Yu-Cheng <lin_yu_cheng@realtek.com>
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_RTS5912_H_
#define ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_RTS5912_H_

#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>
#include <reg/reg_gpio.h>

#ifdef __cplusplus
extern "C" {
#endif

gpio_pin_t gpio_rts5912_get_intr_pin(volatile uint32_t *reg_base);

static ALWAYS_INLINE void gpio_rts5912_set_wakeup_pin(uint32_t pin_num)
{
        volatile uint32_t *gcr =
                (volatile uint32_t *)(((uint32_t *)(DT_REG_ADDR(DT_NODELABEL(gpioa)))) + pin_num);

        *gcr &= ~(GPIO_GCR_MFCTRL_Msk | GPIO_GCR_DIR_Msk);
        *gcr |= BIT(GPIO_GCR_INTCTRL_Pos) | GPIO_GCR_INTSTS_Msk | GPIO_GCR_INTEN_Msk |
                GPIO_GCR_INDETEN_Msk;
}

int gpio_rts5912_get_pin_num(const struct gpio_dt_spec *gpio);

uint32_t *gpio_rts5912_get_port_address(const struct gpio_dt_spec *gpio);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_RTS5912_H_ */
```

## 82.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

版权（Copyright）：© 2024 Realtek Semiconductor Corporation, SIBG-SD7。

作者（Author）：Lin Yu-Cheng <lin_yu_cheng@realtek.com>。

### 注释 2：原第 39 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_RTS5912_H_`。

## 82.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gpio__rts5912_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)
- [gpio_rts5912_get_intr_pin](https://docs.zephyrproject.org/latest/doxygen/html/gpio__rts5912_8h.html#acfacb1e55d774da53cab6e9fda59c25b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [gpio_rts5912_set_wakeup_pin](https://docs.zephyrproject.org/latest/doxygen/html/gpio__rts5912_8h.html#a8640c6a53deb21cee7bc6be80b1581df)
- [DT_REG_ADDR](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac6d8279c32351ced4c0ac7f32270974e)
- [DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [gpio_rts5912_get_pin_num](https://docs.zephyrproject.org/latest/doxygen/html/gpio__rts5912_8h.html#a955c6e7b8922a236de987c66596d28b2)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [gpio_rts5912_get_port_address](https://docs.zephyrproject.org/latest/doxygen/html/gpio__rts5912_8h.html#a62065211bcb72d822eeccccc6e51dc51)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)

---

[上一章](P081_goep.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P083_grow_r502a.h_源码浏览.md)
