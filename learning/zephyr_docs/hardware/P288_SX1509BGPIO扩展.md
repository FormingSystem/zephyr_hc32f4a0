---
id: learning.zephyr-docs.hardware.gpioextb-6
title: SX1509BGPIO扩展
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__sx1509b__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第288章\_SX1509BGPIO扩展

原文：[group__gpio__sx1509b__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__sx1509b__interface.html)。读取日期：2026-10-13，`latest`。

## 288.1\_LED亮度模式

Semtech SX1509B 是低电压、电平转换（Level-shifting）通用输入/输出（General Purpose Input/Output，GPIO）控制器。接口来自 `zephyr/drivers/gpio/gpio_sx1509b.h`，用于发光二极管（Light-emitting Diode，LED）亮度（Intensity）控制。

函数 [`sx1509b_led_intensity_pin_configure()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__sx1509b__interface.html#gac2ed2f915a7e507e49abc82b6f4f09d5) 将引脚配置为由SX1509B LED驱动的亮度功能控制：

```c
int sx1509b_led_intensity_pin_configure(const struct device *dev,
                                       gpio_pin_t pin);
```

`dev` 指向驱动实例的设备结构，`pin` 为引脚号。要恢复普通GPIO功能，使用标准GPIO接口重新配置引脚。

成功返回 `0`；从中断服务程序（Interrupt Service Routine，ISR）调用返回 `-EWOULDBLOCK`；引脚号越界返回 `-ERANGE`；集成电路间总线（Inter-Integrated Circuit，I²C）操作失败返回 `-EIO`。

## 288.2\_设置亮度

函数 [`sx1509b_led_intensity_pin_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__sx1509b__interface.html#ga5fe77cf7261b831b4cb010c48da982bf) 设置选定引脚的LED亮度：

```c
int sx1509b_led_intensity_pin_set(const struct device *dev, gpio_pin_t pin,
                                 uint8_t intensity_val);
```

`dev` 指向驱动实例，`pin` 为引脚号，`intensity_val` 为亮度值。成功返回 `0`，I²C操作失败返回 `-EIO`。

---

[上一章：PCAL64XXAGPIO扩展](P287_PCAL64XXAGPIO扩展.md) · [下一章：BL61x线输出配置](P289_BL61x线输出配置.md) · [返回大纲](大纲.md)
