---
id: learning.zephyr-docs.api-source-reference.page-619
title: nxp_flexio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp__flexio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第619章\_nxp\_flexio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nxp__flexio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nxp__flexio_8h.html)。

## 619.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__nxp__flexio__interface_html_ga1208ad4ef70419ff61a87b8b1ff8d446"></a>
<a id="agroup__nxp__flexio__interface_html_ga39b6b8b2eda354b4d3a40da48f41e3d2"></a>
<a id="agroup__nxp__flexio__interface_html_ga3be561d6ee29eb0e23f67ddcf234d22e"></a>
<a id="agroup__nxp__flexio__interface_html_ga7e84a09852b713337d6e124eb2b8df7d"></a>
<a id="agroup__nxp__flexio__interface_html_ga9c5fdb0b5b11dcc04d42c2c7b98b3ffb"></a>
<a id="agroup__nxp__flexio__interface_html_gab5ff53d4ac41321fe4726e2ede175ac2"></a>
<a id="agroup__nxp__flexio__interface_html_gaf11959c4e7c7a5ef56b082fcf0b7f42c"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructnxp__flexio__child__res_html"></a>
<a id="astructnxp__flexio__child__res_html_ad62e4adfc76a26841f613552e871a187"></a>
<a id="astructnxp__flexio__child__res_html_ae1187d65f541a282da4651a53b0626d8"></a>
<a id="astructnxp__flexio__child__res_html_afac825cb54e1dcd093c8ca19a78fa4dd"></a>
<a id="astructnxp__flexio__child__res_html_afd4633d2dbb04c9155f9088206aa5772"></a>
<a id="astructnxp__flexio__child_html"></a>
<a id="astructnxp__flexio__child_html_a1befee43b0d6a378983a8207fdb23b10"></a>
<a id="astructnxp__flexio__child_html_a9490af6c5e89d9994a0419c80757b14e"></a>
<a id="astructnxp__flexio__child_html_ae1c82ed160a226d48dee0ad6607cde34"></a>

```c
/*
 * Copyright (c) 2024, STRIM, ALC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MISC_NXP_FLEXIO_NXP_FLEXIO_H_
#define ZEPHYR_INCLUDE_DRIVERS_MISC_NXP_FLEXIO_NXP_FLEXIO_H_


#include <zephyr/device.h>

struct nxp_flexio_child_res {
        uint8_t *shifter_index;
        uint8_t shifter_count;
        uint8_t *timer_index;
        uint8_t timer_count;
};

typedef int (*nxp_flexio_child_isr_t)(void *user_data);

struct nxp_flexio_child {
        nxp_flexio_child_isr_t isr;
        void *user_data;
        struct nxp_flexio_child_res res;
};

void nxp_flexio_irq_enable(const struct device *dev);

void nxp_flexio_irq_disable(const struct device *dev);

void nxp_flexio_lock(const struct device *dev);

void nxp_flexio_unlock(const struct device *dev);

int nxp_flexio_get_rate(const struct device *dev, uint32_t *rate);

int nxp_flexio_child_attach(const struct device *dev,
        const struct nxp_flexio_child *child);


#endif /* ZEPHYR_INCLUDE_DRIVERS_MISC_NXP_FLEXIO_NXP_FLEXIO_H_ */
```

## 619.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024, STRIM, ALC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 123 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MISC_NXP_FLEXIO_NXP_FLEXIO_H_`。

## 619.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nxp__flexio_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [nxp_flexio_child_res](../platform_security_model_reference/P021_nxp_flexio_child_res_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [shifter_index](../platform_security_model_reference/P021_nxp_flexio_child_res_结构体.md#afd4633d2dbb04c9155f9088206aa5772)
- [shifter_count](../platform_security_model_reference/P021_nxp_flexio_child_res_结构体.md#afac825cb54e1dcd093c8ca19a78fa4dd)
- [timer_index](../platform_security_model_reference/P021_nxp_flexio_child_res_结构体.md#ae1187d65f541a282da4651a53b0626d8)
- [timer_count](../platform_security_model_reference/P021_nxp_flexio_child_res_结构体.md#ad62e4adfc76a26841f613552e871a187)
- [nxp_flexio_child_isr_t](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#gaf11959c4e7c7a5ef56b082fcf0b7f42c)
- [nxp_flexio_child](../platform_security_model_reference/P020_nxp_flexio_child_结构体.md)
- [isr](../platform_security_model_reference/P020_nxp_flexio_child_结构体.md#a1befee43b0d6a378983a8207fdb23b10)
- [user_data](../platform_security_model_reference/P020_nxp_flexio_child_结构体.md#a9490af6c5e89d9994a0419c80757b14e)
- [res](../platform_security_model_reference/P020_nxp_flexio_child_结构体.md#ae1c82ed160a226d48dee0ad6607cde34)
- [nxp_flexio_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#ga7e84a09852b713337d6e124eb2b8df7d)
- [device](../device_reference/P002_设备对象结构.md)
- [nxp_flexio_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#ga39b6b8b2eda354b4d3a40da48f41e3d2)
- [nxp_flexio_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#ga3be561d6ee29eb0e23f67ddcf234d22e)
- [nxp_flexio_unlock](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#gab5ff53d4ac41321fe4726e2ede175ac2)
- [nxp_flexio_get_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#ga9c5fdb0b5b11dcc04d42c2c7b98b3ffb)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [nxp_flexio_child_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#ga1208ad4ef70419ff61a87b8b1ff8d446)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [nxp_flexio_child_res::timer_count](../platform_security_model_reference/P021_nxp_flexio_child_res_结构体.md#ad62e4adfc76a26841f613552e871a187)
- [nxp_flexio_child_res::timer_index](../platform_security_model_reference/P021_nxp_flexio_child_res_结构体.md#ae1187d65f541a282da4651a53b0626d8)
- [nxp_flexio_child_res::shifter_count](../platform_security_model_reference/P021_nxp_flexio_child_res_结构体.md#afac825cb54e1dcd093c8ca19a78fa4dd)
- [nxp_flexio_child_res::shifter_index](../platform_security_model_reference/P021_nxp_flexio_child_res_结构体.md#afd4633d2dbb04c9155f9088206aa5772)
- [nxp_flexio_child::isr](../platform_security_model_reference/P020_nxp_flexio_child_结构体.md#a1befee43b0d6a378983a8207fdb23b10)
- [nxp_flexio_child::user_data](../platform_security_model_reference/P020_nxp_flexio_child_结构体.md#a9490af6c5e89d9994a0419c80757b14e)
- [nxp_flexio_child::res](../platform_security_model_reference/P020_nxp_flexio_child_结构体.md#ae1c82ed160a226d48dee0ad6607cde34)

---

[上一章](P618_nxp_enet.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P620_nxp_irqsteer.h_源码浏览.md)
