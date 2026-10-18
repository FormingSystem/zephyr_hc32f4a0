---
id: learning.zephyr-docs.hardware.gpioextb-0
title: AmbiqGPIO扩展
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__ambiq__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第282章\_AmbiqGPIO扩展

原文：[group__gpio__ambiq__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__ambiq__interface.html)。读取日期：2026-10-13，`latest`。

## 282.1\_实际引脚编号

本页为 Ambiq 通用输入/输出（General Purpose Input/Output，GPIO）控制器提供扩展。头文件为 `zephyr/drivers/gpio/gpio_ambiq.h`。

函数 [`ambiq_gpio_get_pinnum()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__ambiq__interface.html#gaaaf57fd1692176a44714852f7593913d) 取得实际GPIO引脚编号：

```c
gpio_pin_t ambiq_gpio_get_pinnum(const struct device *dev, gpio_pin_t pin);
```

`dev` 指向驱动实例的设备结构，`pin` 是所选GPIO组中的引脚编号。返回实际引脚号。

---

[上一章：nPM6001GPIO标志](P281_nPM6001GPIO标志.md) · [下一章：BL61xGPIO线输出](P283_BL61xGPIO线输出.md) · [返回大纲](大纲.md)
