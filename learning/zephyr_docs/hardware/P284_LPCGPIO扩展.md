---
id: learning.zephyr-docs.hardware.gpioextb-2
title: LPCGPIO扩展
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__mcux__lpc__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第284章\_LPCGPIO扩展

原文：[group__gpio__mcux__lpc__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__mcux__lpc__interface.html)。读取日期：2026-10-13，`latest`。

## 284.1\_触发引脚回调

本页为 NXP MCUX LPC 通用输入/输出（General Purpose Input/Output，GPIO）控制器提供扩展，头文件为 `zephyr/drivers/gpio/gpio_mcux_lpc.h`。

函数 [`gpio_mcux_lpc_trigger_cb()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__mcux__lpc__interface.html#ga6ce1efd70bb2996ac993f2a322d74ac3) 为给定引脚触发回调（Callback），允许其他驱动发起这些引脚的回调：

```c
void gpio_mcux_lpc_trigger_cb(const struct device *dev, uint32_t pins);
```

`dev` 指向驱动实例的设备结构，`pins` 为实际触发中断的引脚掩码（Pin Mask）。函数没有返回值。

---

[上一章：BL61xGPIO线输出](P283_BL61xGPIO线输出.md) · [下一章：NCT38XXGPIO扩展](P285_NCT38XXGPIO扩展.md) · [返回大纲](大纲.md)
