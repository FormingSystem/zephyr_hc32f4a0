---
id: learning.zephyr-docs.api-source-reference.page-303
title: gpio_sx1509b.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__sx1509b_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第303章\_gpio\_sx1509b.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gpio__sx1509b_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gpio__sx1509b_8h.html)。

## 303.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="adevice_8h_html"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="agroup__gpio__interface_html_ga38179eb7a46a743c12cfac28f347fb34"></a>
<a id="agroup__gpio__sx1509b__interface_html_ga5fe77cf7261b831b4cb010c48da982bf"></a>
<a id="agroup__gpio__sx1509b__interface_html_gac2ed2f915a7e507e49abc82b6f4f09d5"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_SX1509B_H_
#define ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_SX1509B_H_


#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>

#ifdef __cplusplus
extern "C" {
#endif

int sx1509b_led_intensity_pin_configure(const struct device *dev,
                                        gpio_pin_t pin);

int sx1509b_led_intensity_pin_set(const struct device *dev, gpio_pin_t pin,
                                  uint8_t intensity_val);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_SX1509B_H_ */
```

## 303.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 70 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_SX1509B_H_`。

## 303.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gpio__sx1509b_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [sx1509b_led_intensity_pin_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__sx1509b__interface.html#gac2ed2f915a7e507e49abc82b6f4f09d5)
- [device](../device_reference/P002_设备对象结构.md)
- [gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)
- [sx1509b_led_intensity_pin_set](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__sx1509b__interface.html#ga5fe77cf7261b831b4cb010c48da982bf)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)

---

[上一章](P302_gpio_pcal64xxa.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P304_grp.h_源码浏览.md)
