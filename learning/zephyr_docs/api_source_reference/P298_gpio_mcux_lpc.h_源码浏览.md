---
id: learning.zephyr-docs.api-source-reference.page-298
title: gpio_mcux_lpc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__mcux__lpc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第298章\_gpio\_mcux\_lpc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gpio__mcux__lpc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gpio__mcux__lpc_8h.html)。

## 298.1\_原始可见代码（Source Code）

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
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="adevice_8h_html"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="agroup__gpio__mcux__lpc__interface_html_ga6ce1efd70bb2996ac993f2a322d74ac3"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright 2024 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_MCUX_LPC_H_
#define ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_MCUX_LPC_H_


#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>

void gpio_mcux_lpc_trigger_cb(const struct device *dev, uint32_t pins);


#endif /* ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_MCUX_LPC_H_ */
```

## 298.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 41 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_MCUX_LPC_H_`。

## 298.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gpio__mcux__lpc_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [gpio_mcux_lpc_trigger_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__mcux__lpc__interface.html#ga6ce1efd70bb2996ac993f2a322d74ac3)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)

---

[上一章](P297_gpio_intel.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P299_gpio_nct38xx.h_源码浏览.md)
