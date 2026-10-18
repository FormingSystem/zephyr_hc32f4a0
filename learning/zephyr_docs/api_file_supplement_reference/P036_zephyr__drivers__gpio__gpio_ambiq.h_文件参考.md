---
id: learning.zephyr-docs.api-file-supplement-reference.page-36
title: zephyr__drivers__gpio__gpio_ambiq.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__ambiq_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_zephyr\_\_drivers\_\_gpio\_\_gpio\_ambiq.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gpio__ambiq_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Ambiq GPIO驱动的头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>
```

查看此文件的源码。

Ambiq GPIO驱动的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 36.1\_函数（Functions）

<a id="r_gaaaf57fd1692176a44714852f7593913d"></a>

```c
gpio_pin_t ambiq_gpio_get_pinnum (const struct device *dev, gpio_pin_t pin)
```

相关声明：[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)、[ambiq_gpio_get_pinnum](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__ambiq__interface.html#gaaaf57fd1692176a44714852f7593913d)、[device](../device_reference/P002_设备对象结构.md)、[gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)。

获取实际的通用输入输出引脚编号（GPIO Pin Number）。


## 36.2\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P295_gpio_ambiq.h_源码浏览.md)
- [gpio_pin_t](../hardware/P266_GPIO公共接口.md#ga38179eb7a46a743c12cfac28f347fb34)
- [ambiq_gpio_get_pinnum](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__ambiq__interface.html#gaaaf57fd1692176a44714852f7593913d)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>

---

[上一章](P035_zephyr__drivers__interrupt_controller__gicv3_its.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P037_zephyr__drivers__gpio__gpio_mcux_lpc.h_文件参考.md)
