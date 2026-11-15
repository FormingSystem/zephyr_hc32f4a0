---
id: learning.zephyr-docs.api-file-configuration-reference.page-34
title: zephyr__drivers__gpio__gpio_sx1509b.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__sx1509b_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_zephyr\_\_drivers\_\_gpio\_\_gpio\_sx1509b.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gpio__sx1509b_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SX1509B GPIO驱动的头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>
```

查看此文件的源码。

SX1509B GPIO驱动的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 34.1\_函数（Functions）

<a id="r_gac2ed2f915a7e507e49abc82b6f4f09d5"></a>

```c
int sx1509b_led_intensity_pin_configure (const struct device *dev, gpio_pin_t pin)
```

相关声明：[sx1509b_led_intensity_pin_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__sx1509b__interface.html#gac2ed2f915a7e507e49abc82b6f4f09d5)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)。

将引脚（Pin）配置为用于 LED 亮度（Intensity）控制。

<a id="r_ga5fe77cf7261b831b4cb010c48da982bf"></a>

```c
int sx1509b_led_intensity_pin_set (const struct device *dev, gpio_pin_t pin, uint8_t intensity_val)
```

相关声明：[sx1509b_led_intensity_pin_set](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__sx1509b__interface.html#ga5fe77cf7261b831b4cb010c48da982bf)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置所选引脚（Pin）的 LED 亮度（Intensity）。


## 34.2\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P303_gpio_sx1509b.h_源码浏览.md)
- [sx1509b_led_intensity_pin_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__sx1509b__interface.html#gac2ed2f915a7e507e49abc82b6f4f09d5)
- [device](../device_reference/P002_设备对象结构.md)
- [gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)
- [sx1509b_led_intensity_pin_set](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__sx1509b__interface.html#ga5fe77cf7261b831b4cb010c48da982bf)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>

---

[上一章](P033_zephyr__drivers__gnss__gnss_publish.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P035_zephyr__mgmt__mcumgr__mgmt__handlers.h_文件参考.md)
