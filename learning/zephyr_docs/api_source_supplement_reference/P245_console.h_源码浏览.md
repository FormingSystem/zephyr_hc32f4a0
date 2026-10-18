---
id: learning.zephyr-docs.api-source-supplement-reference.page-245
title: console.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/xen_2console_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第245章\_console.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/xen_2console_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/xen_2console_8h.html)。

## 245.1\_原始可见代码（Source Code）

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
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00027"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="adevice_8h_html"></a>
<a id="adevice__mmio_8h_html"></a>
<a id="adrivers_2uart_8h_html"></a>
<a id="agroup__device-mmio-single_html_ga47e037f86108c8da12d8a9b9a35e6ad5"></a>
<a id="agroup__uart__interrupt_html_gad7a26b1a1d6212d7d39c05c8ad4ec926"></a>
<a id="agroup__xen__console__driver_html_ga6e114bd3611c8d2e10541011f0c7c65e"></a>
<a id="ainit_8h_html"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2021 EPAM Systems
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_XEN_CONSOLE_H_
#define ZEPHYR_INCLUDE_XEN_CONSOLE_H_

#include <zephyr/init.h>
#include <zephyr/device.h>
#include <zephyr/drivers/uart.h>
#include <zephyr/sys/device_mmio.h>


struct hvc_xen_data {
        DEVICE_MMIO_RAM;        /* should be first */
        const struct device *dev;
        struct xencons_interface *intf;
        uint64_t evtchn;

#ifdef CONFIG_UART_INTERRUPT_DRIVEN
        uart_irq_callback_user_data_t irq_cb;
        void *irq_cb_data;
#endif /* CONFIG_UART_INTERRUPT_DRIVEN */
};

int xen_console_init(const struct device *dev);


#endif /* ZEPHYR_INCLUDE_XEN_CONSOLE_H_ */
```

## 245.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 EPAM Systems。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 33 行

应放在首位。

### 注释 3：原第 41 行

条件编译配置（Configuration）标记：`CONFIG_UART_INTERRUPT_DRIVEN`。

### 注释 4：原第 56 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_XEN_CONSOLE_H_`。

## 245.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/xen_2console_8h.html)
- [zephyr/init.h](../device_reference/P009_系统初始化头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/uart.h](../uart_driver_reference/P001_UART驱动头文件参考.md)
- [zephyr/sys/device_mmio.h](../device_reference/P015_设备MMIO头文件参考.md)
- [DEVICE_MMIO_RAM](../device_reference/P012_设备单区域MMIO.md#ga47e037f86108c8da12d8a9b9a35e6ad5)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [uart_irq_callback_user_data_t](../hardware/P333_UART中断驱动接口.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)
- [xen_console_init](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__console__driver.html#ga6e114bd3611c8d2e10541011f0c7c65e)
- [device](../device_reference/P002_设备对象结构.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [device_mmio.h](../device_reference/P015_设备MMIO头文件参考.md)
- [uart.h](../uart_driver_reference/P001_UART驱动头文件参考.md)
- [init.h](../device_reference/P009_系统初始化头文件参考.md)

---

[上一章](P244_worldsemi_ws2812c.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P246_xg21-pinctrl.h_源码浏览.md)
