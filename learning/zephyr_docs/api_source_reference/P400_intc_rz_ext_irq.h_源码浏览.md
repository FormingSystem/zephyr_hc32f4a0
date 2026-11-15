---
id: learning.zephyr-docs.api-source-reference.page-400
title: intc_rz_ext_irq.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__ext__irq_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第400章\_intc\_rz\_ext\_irq.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__ext__irq_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__ext__irq_8h.html)。

## 400.1\_原始可见代码（Source Code）

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
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="aintc__rz__ext__irq_8h_html_a08eb727b662be3e71d70c5fa88e95b7a"></a>
<a id="aintc__rz__ext__irq_8h_html_a1c6d9f3910b3d82378ab40219828184a"></a>
<a id="aintc__rz__ext__irq_8h_html_a913bfcbf3ff2161da4c2a45a77781452"></a>
<a id="aintc__rz__ext__irq_8h_html_a9a372d975e6507a4d34c0766f22a368a"></a>
<a id="aintc__rz__ext__irq_8h_html_af40022fc3bb2e30df6513c4172672235"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2024-2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_RZ_EXT_IRQ_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_RZ_EXT_IRQ_H_

#define RZ_EXT_IRQ_TRIG_FALLING   0
#define RZ_EXT_IRQ_TRIG_RISING    1
#define RZ_EXT_IRQ_TRIG_BOTH_EDGE 2
#define RZ_EXT_IRQ_TRIG_LEVEL_LOW 3

typedef void (*intc_rz_ext_irq_callback_t)(void *arg);

int intc_rz_ext_irq_enable(const struct device *dev);

int intc_rz_ext_irq_disable(const struct device *dev);

int intc_rz_ext_irq_set_callback(const struct device *dev, intc_rz_ext_irq_callback_t cb,
                                 void *arg);

int intc_rz_ext_irq_set_type(const struct device *dev, uint8_t trig);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_RZ_EXT_IRQ_H_ */
```

## 400.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024-2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 54 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_RZ_EXT_IRQ_H_`。

## 400.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__ext__irq_8h.html)
- [intc_rz_ext_irq_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__ext__irq_8h.html#a1c6d9f3910b3d82378ab40219828184a)
- [intc_rz_ext_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__ext__irq_8h.html#a08eb727b662be3e71d70c5fa88e95b7a)
- [device](../device_reference/P002_设备对象结构.md)
- [intc_rz_ext_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__ext__irq_8h.html#a9a372d975e6507a4d34c0766f22a368a)
- [intc_rz_ext_irq_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__ext__irq_8h.html#af40022fc3bb2e30df6513c4172672235)
- [intc_rz_ext_irq_set_type](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__ext__irq_8h.html#a913bfcbf3ff2161da4c2a45a77781452)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

---

[上一章](P399_intc_renesas_rx_grp_int.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P401_intc_rz_icu.h_源码浏览.md)
