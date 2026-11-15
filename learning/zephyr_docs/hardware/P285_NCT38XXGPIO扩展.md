---
id: learning.zephyr-docs.hardware.gpioextb-3
title: NCT38XXGPIO扩展
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__nct38xx__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第285章\_NCT38XXGPIO扩展

原文：[group__gpio__nct38xx__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__nct38xx__interface.html)。读取日期：2026-10-13，`latest`。

## 285.1\_分发端口中断

Nuvoton NCT38XX 系列是基于集成电路间总线（Inter-Integrated Circuit，I²C）的通用输入/输出（General Purpose Input/Output，GPIO）扩展器。扩展声明来自 `zephyr/drivers/gpio/gpio_nct38xx.h`。

函数 [`nct38xx_gpio_alert_handler()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__nct38xx__interface.html#ga05e658cb957b13402371054aa9f59302) 分发NCT38XX设备所有GPIO端口的中断服务程序（Interrupt Service Routine，ISR）：

```c
void nct38xx_gpio_alert_handler(const struct device *dev);
```

`dev` 指向NCT38XX设备。函数没有返回值。

---

[上一章：LPCGPIO扩展](P284_LPCGPIO扩展.md) · [下一章：PCAGPIO扩展](P286_PCAGPIO扩展.md) · [返回大纲](大纲.md)
