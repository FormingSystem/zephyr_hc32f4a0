---
id: learning.zephyr-docs.api-source-reference.page-299
title: gpio_nct38xx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__nct38xx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第299章\_gpio\_nct38xx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gpio__nct38xx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gpio__nct38xx_8h.html)。

## 299.1\_原始可见代码（Source Code）

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
<a id="l00026"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="agroup__gpio__nct38xx__interface_html_ga05e658cb957b13402371054aa9f59302"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2021 Nuvoton Technology Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_NCT38XX_H_
#define ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_NCT38XX_H_


#ifdef __cplusplus
extern "C" {
#endif

void nct38xx_gpio_alert_handler(const struct device *dev);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_NCT38XX_H_ */
```

## 299.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Nuvoton Technology Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 42 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_NCT38XX_H_`。

## 299.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gpio__nct38xx_8h.html)
- [nct38xx_gpio_alert_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__nct38xx__interface.html#ga05e658cb957b13402371054aa9f59302)
- [device](../device_reference/P002_设备对象结构.md)

---

[上一章](P298_gpio_mcux_lpc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P300_gpio_nrf.h_源码浏览.md)
