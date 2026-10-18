---
id: learning.zephyr-docs.hardware.gpioextb-4
title: PCAGPIO扩展
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__pca__series__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第286章\_PCAGPIO扩展

原文：[group__gpio__pca__series__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__pca__series__interface.html)。读取日期：2026-10-13，`latest`。

## 286.1\_器件复位

NXP PCA 系列是基于集成电路间总线（Inter-Integrated Circuit，I²C）的输入/输出（Input/Output，I/O）扩展器。本页提供通用输入/输出（General Purpose Input/Output，GPIO）驱动复位接口，声明来自 `zephyr/drivers/gpio/gpio_pca_series.h`。

函数 [`gpio_pca_series_reset()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__pca__series__interface.html#ga6d802f2686a1a2d004d3ae20e361d701) 复位PCA系列设备：

```c
int gpio_pca_series_reset(const struct device *dev);
```

存在复位引脚 `reset_pin` 时，通过驱动该引脚复位器件；否则向设备寄存器写入复位值。`dev` 指向驱动实例的设备结构。成功返回 `0`，原页没有列出其他返回码。

---

[上一章：NCT38XXGPIO扩展](P285_NCT38XXGPIO扩展.md) · [下一章：PCAL64XXAGPIO扩展](P287_PCAL64XXAGPIO扩展.md) · [返回大纲](大纲.md)
