---
id: learning.zephyr-docs.api-source-reference.page-405
title: intc_xmc4xxx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__xmc4xxx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第405章\_intc\_xmc4xxx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intc__xmc4xxx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intc__xmc4xxx_8h.html)。

## 405.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="agroup__gpio__interface__backend_html_ga4ea6fd78423e6e3004702b599bc7b12d"></a>
<a id="agroup__gpio__interface__backend_html_ga82f0562c44cf0f76cc7e16d606a975db"></a>
<a id="aintc__xmc4xxx_8h_html_a0203ccc3d0edc6be506752682afcc30c"></a>
<a id="aintc__xmc4xxx_8h_html_a1583d09e4b260c07763e5419ca3411d1"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2022 Schlumberger
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_XMC4XXX_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_XMC4XXX_H_


int intc_xmc4xxx_gpio_enable_interrupt(int port_id, int pin, enum gpio_int_mode mode,
                enum gpio_int_trig trig, void (*fn)(const struct device *dev, int pin),
                void *user_data);


int intc_xmc4xxx_gpio_disable_interrupt(int port_id, int pin);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_XMC4XXX_H_ */
```

## 405.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Schlumberger。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 44 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_XMC4XXX_H_`。

## 405.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intc__xmc4xxx_8h.html)
- [intc_xmc4xxx_gpio_enable_interrupt](https://docs.zephyrproject.org/latest/doxygen/html/intc__xmc4xxx_8h.html#a0203ccc3d0edc6be506752682afcc30c)
- [gpio_int_mode](../hardware/P271_GPIO驱动后端.md#ga82f0562c44cf0f76cc7e16d606a975db)
- [gpio_int_trig](../hardware/P271_GPIO驱动后端.md#ga4ea6fd78423e6e3004702b599bc7b12d)
- [device](../device_reference/P002_设备对象结构.md)
- [intc_xmc4xxx_gpio_disable_interrupt](https://docs.zephyrproject.org/latest/doxygen/html/intc__xmc4xxx_8h.html#a1583d09e4b260c07763e5419ca3411d1)

---

[上一章](P404_intc_wkpu_nxp_s32.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P406_intel_vtd.h_源码浏览.md)
