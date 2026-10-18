---
id: learning.zephyr-docs.api-source-reference.page-402
title: intc_rz_tint.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__tint_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第402章\_intc\_rz\_tint.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__tint_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__tint_8h.html)。

## 402.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="foldopen00010"></a>
<a id="l00010"></a>
<a id="l00012"></a>
<a id="l00014"></a>
<a id="l00016"></a>
<a id="l00018"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="aintc__rz__tint_8h_html_a4363ce99eee64656d3bbc520dac8c1c8"></a>
<a id="aintc__rz__tint_8h_html_a4e028397cd25a200c7be779339d3c5cc"></a>
<a id="aintc__rz__tint_8h_html_a60a69e2377b62032b65909d835a1ba6a"></a>
<a id="aintc__rz__tint_8h_html_a61a9005f09428a38ba570b5b47f7381e"></a>
<a id="aintc__rz__tint_8h_html_a905cdb052d714bc9c5a90cfdf1614434"></a>
<a id="aintc__rz__tint_8h_html_a905cdb052d714bc9c5a90cfdf1614434a2f26bfb23aa941ba6c2da19b7387554a"></a>
<a id="aintc__rz__tint_8h_html_a905cdb052d714bc9c5a90cfdf1614434a35bce08a56a20e67fb028ee74c3331ad"></a>
<a id="aintc__rz__tint_8h_html_a905cdb052d714bc9c5a90cfdf1614434a3a8c04fc0458b0a96da9b52f22e36eb6"></a>
<a id="aintc__rz__tint_8h_html_a905cdb052d714bc9c5a90cfdf1614434a4aa5928babb7e7b658be714c5df211c2"></a>
<a id="aintc__rz__tint_8h_html_a905cdb052d714bc9c5a90cfdf1614434a9c3971631e16520443a055139f63f604"></a>
<a id="aintc__rz__tint_8h_html_aa47a09baad3bd3e77a10b90ecda66e9d"></a>
<a id="aintc__rz__tint_8h_html_afee1611e56667148581ed48117cdcfc5"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_RZ_TINT_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_RZ_TINT_H_

enum intc_rz_tint_trigger {
        RZ_TINT_FAILING_EDGE,
        RZ_TINT_RISING_EDGE,
        RZ_TINT_BOTH_EDGE,
        RZ_TINT_LOW_LEVEL,
        RZ_TINT_HIGH_LEVEL,
};

typedef void (*intc_rz_tint_callback_t)(void *arg);

int intc_rz_tint_connect(const struct device *dev, uint8_t port, uint8_t pin);

int intc_rz_tint_set_type(const struct device *dev, enum intc_rz_tint_trigger trig);

int intc_rz_tint_enable(const struct device *dev);

int intc_rz_tint_disable(const struct device *dev);

int intc_rz_tint_set_callback(const struct device *dev, intc_rz_tint_callback_t cb, void *arg);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_RZ_TINT_H_ */
```

## 402.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 71 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_RZ_TINT_H_`。

## 402.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__tint_8h.html)
- [intc_rz_tint_trigger](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__tint_8h.html#a905cdb052d714bc9c5a90cfdf1614434)
- [RZ_TINT_FAILING_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__tint_8h.html#a905cdb052d714bc9c5a90cfdf1614434a4aa5928babb7e7b658be714c5df211c2)
- [RZ_TINT_RISING_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__tint_8h.html#a905cdb052d714bc9c5a90cfdf1614434a35bce08a56a20e67fb028ee74c3331ad)
- [RZ_TINT_BOTH_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__tint_8h.html#a905cdb052d714bc9c5a90cfdf1614434a3a8c04fc0458b0a96da9b52f22e36eb6)
- [RZ_TINT_LOW_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__tint_8h.html#a905cdb052d714bc9c5a90cfdf1614434a9c3971631e16520443a055139f63f604)
- [RZ_TINT_HIGH_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__tint_8h.html#a905cdb052d714bc9c5a90cfdf1614434a2f26bfb23aa941ba6c2da19b7387554a)
- [intc_rz_tint_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__tint_8h.html#aa47a09baad3bd3e77a10b90ecda66e9d)
- [intc_rz_tint_connect](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__tint_8h.html#afee1611e56667148581ed48117cdcfc5)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [intc_rz_tint_set_type](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__tint_8h.html#a4363ce99eee64656d3bbc520dac8c1c8)
- [intc_rz_tint_enable](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__tint_8h.html#a61a9005f09428a38ba570b5b47f7381e)
- [intc_rz_tint_disable](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__tint_8h.html#a60a69e2377b62032b65909d835a1ba6a)
- [intc_rz_tint_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/intc__rz__tint_8h.html#a4e028397cd25a200c7be779339d3c5cc)

---

[上一章](P401_intc_rz_icu.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P403_intc_thejas32.h_源码浏览.md)
