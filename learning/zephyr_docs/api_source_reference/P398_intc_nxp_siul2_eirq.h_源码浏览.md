---
id: learning.zephyr-docs.api-source-reference.page-398
title: intc_nxp_siul2_eirq.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__siul2__eirq_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第398章\_intc\_nxp\_siul2\_eirq.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__siul2__eirq_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__siul2__eirq_8h.html)。

## 398.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="foldopen00021"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="aintc__nxp__siul2__eirq_8h_html_a6fbebceceeaaf6f46be6bba383b2dd6c"></a>
<a id="aintc__nxp__siul2__eirq_8h_html_ab54c32d27a6250745a2360a5bccc962d"></a>
<a id="aintc__nxp__siul2__eirq_8h_html_ad8e4a39add66c073c73c58a37f347e6f"></a>
<a id="aintc__nxp__siul2__eirq_8h_html_ae8a16d2e88c75e823638169b467f7d29"></a>
<a id="aintc__nxp__siul2__eirq_8h_html_ae8a16d2e88c75e823638169b467f7d29a3430a77e48f7a96ef93a59eab4ba8d1c"></a>
<a id="aintc__nxp__siul2__eirq_8h_html_ae8a16d2e88c75e823638169b467f7d29abab4d5ba43ada8f041951d47665fcdaf"></a>
<a id="aintc__nxp__siul2__eirq_8h_html_ae8a16d2e88c75e823638169b467f7d29abdd4797bd8ece4c9a09e159edc8d2205"></a>
<a id="aintc__nxp__siul2__eirq_8h_html_aed12dd6e76bb74f716b7f4c868b3bf28"></a>
<a id="aintc__nxp__siul2__eirq_8h_html_aedfa3141aa28e62852ebc8cb60f1f1ff"></a>
<a id="aintc__nxp__siul2__eirq_8h_html_aedfc2594ff5bc5e324464cbeb9c5ee8d"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright 2022, 2024-2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_NXP_SIUL2_EIRQ_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_NXP_SIUL2_EIRQ_H_

typedef void (*nxp_siul2_eirq_callback_t)(uint8_t pin, void *arg);

enum nxp_siul2_eirq_trigger {
        NXP_SIUl2_EIRQ_RISING_EDGE,
        NXP_SIUl2_EIRQ_FALLING_EDGE,
        NXP_SIUl2_EIRQ_BOTH_EDGES,
};

void nxp_siul2_eirq_unset_callback(const struct device *dev, uint8_t irq);

int nxp_siul2_eirq_set_callback(const struct device *dev, uint8_t irq, uint8_t pin,
                                nxp_siul2_eirq_callback_t cb, void *arg);

void nxp_siul2_eirq_enable_interrupt(const struct device *dev, uint8_t irq,
                                     enum nxp_siul2_eirq_trigger trigger);

void nxp_siul2_eirq_disable_interrupt(const struct device *dev, uint8_t irq);

uint32_t nxp_siul2_eirq_get_pending(const struct device *dev);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_NXP_SIUL2_EIRQ_H_ */
```

## 398.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022, 2024-2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 79 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_NXP_SIUL2_EIRQ_H_`。

## 398.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__siul2__eirq_8h.html)
- [nxp_siul2_eirq_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__siul2__eirq_8h.html#ad8e4a39add66c073c73c58a37f347e6f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [nxp_siul2_eirq_trigger](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__siul2__eirq_8h.html#ae8a16d2e88c75e823638169b467f7d29)
- [NXP_SIUl2_EIRQ_RISING_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__siul2__eirq_8h.html#ae8a16d2e88c75e823638169b467f7d29a3430a77e48f7a96ef93a59eab4ba8d1c)
- [NXP_SIUl2_EIRQ_FALLING_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__siul2__eirq_8h.html#ae8a16d2e88c75e823638169b467f7d29abab4d5ba43ada8f041951d47665fcdaf)
- [NXP_SIUl2_EIRQ_BOTH_EDGES](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__siul2__eirq_8h.html#ae8a16d2e88c75e823638169b467f7d29abdd4797bd8ece4c9a09e159edc8d2205)
- [nxp_siul2_eirq_unset_callback](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__siul2__eirq_8h.html#aedfa3141aa28e62852ebc8cb60f1f1ff)
- [device](../device_reference/P002_设备对象结构.md)
- [nxp_siul2_eirq_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__siul2__eirq_8h.html#aed12dd6e76bb74f716b7f4c868b3bf28)
- [nxp_siul2_eirq_enable_interrupt](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__siul2__eirq_8h.html#aedfc2594ff5bc5e324464cbeb9c5ee8d)
- [nxp_siul2_eirq_disable_interrupt](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__siul2__eirq_8h.html#a6fbebceceeaaf6f46be6bba383b2dd6c)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [nxp_siul2_eirq_get_pending](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__siul2__eirq_8h.html#ab54c32d27a6250745a2360a5bccc962d)

---

[上一章](P397_intc_nxp_gint.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P399_intc_renesas_rx_grp_int.h_源码浏览.md)
