---
id: learning.zephyr-docs.api-source-reference.page-404
title: intc_wkpu_nxp_s32.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__wkpu__nxp__s32_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第404章\_intc\_wkpu\_nxp\_s32.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intc__wkpu__nxp__s32_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intc__wkpu__nxp__s32_8h.html)。

## 404.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="foldopen00020"></a>
<a id="l00020"></a>
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="aintc__wkpu__nxp__s32_8h_html_a3a62c3d569d106117713c307838bdbe5"></a>
<a id="aintc__wkpu__nxp__s32_8h_html_a64c7cee403cb060a5dfe4dc9ef9a9f2f"></a>
<a id="aintc__wkpu__nxp__s32_8h_html_a6717ad2b39f6dcd91ebb16271f8bd103"></a>
<a id="aintc__wkpu__nxp__s32_8h_html_a7440f457f38303fdc829933f897ebbd6"></a>
<a id="aintc__wkpu__nxp__s32_8h_html_a7440f457f38303fdc829933f897ebbd6a1aa475b8f106d699419b85c226075207"></a>
<a id="aintc__wkpu__nxp__s32_8h_html_a7440f457f38303fdc829933f897ebbd6a24ed3d6d41e75d8f97acf883d91301de"></a>
<a id="aintc__wkpu__nxp__s32_8h_html_a7440f457f38303fdc829933f897ebbd6a8aa0f7310ec4a6a87d6e50366dbf2ec3"></a>
<a id="aintc__wkpu__nxp__s32_8h_html_ae9a4815602689b1543d83d45929735a7"></a>
<a id="aintc__wkpu__nxp__s32_8h_html_af465c77abcefe103e4d3de6c864513b9"></a>
<a id="aintc__wkpu__nxp__s32_8h_html_af79abeafd030150ec908a868ab2cad15"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright 2023-2024 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_WKPU_NXP_S32_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_WKPU_NXP_S32_H_

typedef void (*wkpu_nxp_s32_callback_t)(uint8_t pin, void *arg);

enum wkpu_nxp_s32_trigger {
        WKPU_NXP_S32_RISING_EDGE,
        WKPU_NXP_S32_FALLING_EDGE,
        WKPU_NXP_S32_BOTH_EDGES,
};

void wkpu_nxp_s32_unset_callback(const struct device *dev, uint8_t irq);

int wkpu_nxp_s32_set_callback(const struct device *dev, uint8_t irq, uint8_t pin,
                              wkpu_nxp_s32_callback_t cb,  void *arg);

void wkpu_nxp_s32_enable_interrupt(const struct device *dev, uint8_t irq,
                                   enum wkpu_nxp_s32_trigger trigger);

void wkpu_nxp_s32_disable_interrupt(const struct device *dev, uint8_t irq);

uint64_t wkpu_nxp_s32_get_pending(const struct device *dev);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_WKPU_NXP_S32_H_ */
```

## 404.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023-2024 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 78 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_WKPU_NXP_S32_H_`。

## 404.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intc__wkpu__nxp__s32_8h.html)
- [wkpu_nxp_s32_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/intc__wkpu__nxp__s32_8h.html#af465c77abcefe103e4d3de6c864513b9)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [wkpu_nxp_s32_trigger](https://docs.zephyrproject.org/latest/doxygen/html/intc__wkpu__nxp__s32_8h.html#a7440f457f38303fdc829933f897ebbd6)
- [WKPU_NXP_S32_RISING_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/intc__wkpu__nxp__s32_8h.html#a7440f457f38303fdc829933f897ebbd6a1aa475b8f106d699419b85c226075207)
- [WKPU_NXP_S32_FALLING_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/intc__wkpu__nxp__s32_8h.html#a7440f457f38303fdc829933f897ebbd6a8aa0f7310ec4a6a87d6e50366dbf2ec3)
- [WKPU_NXP_S32_BOTH_EDGES](https://docs.zephyrproject.org/latest/doxygen/html/intc__wkpu__nxp__s32_8h.html#a7440f457f38303fdc829933f897ebbd6a24ed3d6d41e75d8f97acf883d91301de)
- [wkpu_nxp_s32_unset_callback](https://docs.zephyrproject.org/latest/doxygen/html/intc__wkpu__nxp__s32_8h.html#a3a62c3d569d106117713c307838bdbe5)
- [device](../device_reference/P002_设备对象结构.md)
- [wkpu_nxp_s32_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/intc__wkpu__nxp__s32_8h.html#a64c7cee403cb060a5dfe4dc9ef9a9f2f)
- [wkpu_nxp_s32_enable_interrupt](https://docs.zephyrproject.org/latest/doxygen/html/intc__wkpu__nxp__s32_8h.html#a6717ad2b39f6dcd91ebb16271f8bd103)
- [wkpu_nxp_s32_disable_interrupt](https://docs.zephyrproject.org/latest/doxygen/html/intc__wkpu__nxp__s32_8h.html#af79abeafd030150ec908a868ab2cad15)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [wkpu_nxp_s32_get_pending](https://docs.zephyrproject.org/latest/doxygen/html/intc__wkpu__nxp__s32_8h.html#ae9a4815602689b1543d83d45929735a7)

---

[上一章](P403_intc_thejas32.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P405_intc_xmc4xxx.h_源码浏览.md)
