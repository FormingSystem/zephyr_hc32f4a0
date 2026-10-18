---
id: learning.zephyr-docs.api-source-reference.page-329
title: i2c_nrfx_twim.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/i2c__nrfx__twim_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第329章\_i2c\_nrfx\_twim.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/i2c__nrfx__twim_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/i2c__nrfx__twim_8h.html)。

## 329.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="adrivers_2i2c_8h_html"></a>
<a id="ai2c__nrfx__twim_8h_html_a465c42f64eb7d2dd4c5e173f9ae11745"></a>
<a id="ai2c__nrfx__twim_8h_html_a924fddc00479f92f98b05a91d08fa7da"></a>
<a id="akernel_8h_html"></a>
<a id="astructdevice_html"></a>
<a id="astructk__timeout__t_html"></a>

```c
/*
 * Copyright (c) 2025 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_I2C_NRFX_TWIM_H
#define ZEPHYR_INCLUDE_DRIVERS_I2C_NRFX_TWIM_H

#include <zephyr/kernel.h>
#include <zephyr/drivers/i2c.h>

int i2c_nrfx_twim_exclusive_access_acquire(const struct device *dev, k_timeout_t timeout);

void i2c_nrfx_twim_exclusive_access_release(const struct device *dev);

#endif /* ZEPHYR_INCLUDE_DRIVERS_I2C_NRFX_TWIM_H */
```

## 329.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 34 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_I2C_NRFX_TWIM_H`。

## 329.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/i2c__nrfx__twim_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/drivers/i2c.h](../i2c_driver_reference/P001_I2C驱动头文件参考.md)
- [i2c_nrfx_twim_exclusive_access_acquire](https://docs.zephyrproject.org/latest/doxygen/html/i2c__nrfx__twim_8h.html#a465c42f64eb7d2dd4c5e173f9ae11745)
- [device](../device_reference/P002_设备对象结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [i2c_nrfx_twim_exclusive_access_release](https://docs.zephyrproject.org/latest/doxygen/html/i2c__nrfx__twim_8h.html#a924fddc00479f92f98b05a91d08fa7da)
- [i2c.h](../i2c_driver_reference/P001_I2C驱动头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

---

[上一章](P328_i2c_emul.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P330_iar.h_源码浏览.md)
