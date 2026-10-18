---
id: learning.zephyr-docs.api-source-reference.page-165
title: nxp_rtxxx_dsp_ctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第165章\_nxp\_rtxxx\_dsp\_ctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.html)。

## 165.1\_原始可见代码（Source Code）

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
<a id="foldopen00016"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00064"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="foldopen00074"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="adevice_8h_html"></a>
<a id="adrivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h_html_a1230a21b6c11930f80fc5f12605de762"></a>
<a id="adrivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h_html_a1230a21b6c11930f80fc5f12605de762a8c63b3117b7c525e96be2b054395cfff"></a>
<a id="adrivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h_html_a1230a21b6c11930f80fc5f12605de762aa43ff75c06ea161e322d77b8dede7791"></a>
<a id="adrivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h_html_a1230a21b6c11930f80fc5f12605de762ab0c726ddfdf30c89075fcf9c7b4586e7"></a>
<a id="adrivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h_html_a17b3a647a7798b34c820366916b2a1c5"></a>
<a id="adrivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h_html_a2efeac2828998f896f2e1bfb532700cd"></a>
<a id="adrivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h_html_a561283f2992839e0191d2fcfef12d989"></a>
<a id="adrivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h_html_a9cc6dd311f29f2e7c79fc74c39658041"></a>
<a id="adrivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h_html_ab6ed31cfcaa45744f960bc19d89f642f"></a>
<a id="adrivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h_html_af1bd0005fe3a6d46d559b249b3ff8ca8"></a>
<a id="adt-bindings_2misc_2nxp__rtxxx__dsp__ctrl_8h_html"></a>
<a id="adt-bindings_2misc_2nxp__rtxxx__dsp__ctrl_8h_html_a2ae85fcd536b453408eca1cba00b308b"></a>
<a id="adt-bindings_2misc_2nxp__rtxxx__dsp__ctrl_8h_html_a70bd7dc09d64c9f7ed92d743a900d068"></a>
<a id="adt-bindings_2misc_2nxp__rtxxx__dsp__ctrl_8h_html_abb4669be96440c29192dc3cf707fce65"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a4a2e6a2cfeb6efed7d5383c33458f46d"></a>
<a id="astructnxp__rtxxx__dsp__ctrl__api_html"></a>
<a id="astructnxp__rtxxx__dsp__ctrl__api_html_a234285d700833f09ca73d80d35d13a87"></a>
<a id="astructnxp__rtxxx__dsp__ctrl__api_html_a2c98dc2c0d65b1004b94be86d99778c5"></a>
<a id="astructnxp__rtxxx__dsp__ctrl__api_html_a5c8bbe71bd90f2a375011ac15695de1d"></a>

```c
/*
 * Copyright 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_MISC_NXP_RTXXX_DSP_CTRL_NXP_RTXXX_DSP_CTRL_H_
#define ZEPHYR_INCLUDE_DRIVERS_MISC_NXP_RTXXX_DSP_CTRL_NXP_RTXXX_DSP_CTRL_H_

#include <zephyr/device.h>
#include <zephyr/dt-bindings/misc/nxp_rtxxx_dsp_ctrl.h>

enum nxp_rtxxx_dsp_ctrl_section_type {
        NXP_RTXXX_DSP_CTRL_SECTION_RESET = NXP_RTXXX_DSP_REGION_RESET,
        NXP_RTXXX_DSP_CTRL_SECTION_TEXT = NXP_RTXXX_DSP_REGION_TEXT,
        NXP_RTXXX_DSP_CTRL_SECTION_DATA = NXP_RTXXX_DSP_REGION_DATA
};

typedef int (*nxp_rtxxx_dsp_ctrl_api_load_section)(
        const struct device *,
        const void *,
        size_t,
        enum nxp_rtxxx_dsp_ctrl_section_type
);
typedef void (*nxp_rtxxx_dsp_ctrl_api_enable)(const struct device *dev);
typedef void (*nxp_rtxxx_dsp_ctrl_api_disable)(const struct device *dev);

struct nxp_rtxxx_dsp_ctrl_api {
        nxp_rtxxx_dsp_ctrl_api_load_section load_section;
        nxp_rtxxx_dsp_ctrl_api_enable enable;
        nxp_rtxxx_dsp_ctrl_api_disable disable;
};

static inline int nxp_rtxxx_dsp_ctrl_load_section(
        const struct device *dev,
        const void *base,
        size_t length,
        enum nxp_rtxxx_dsp_ctrl_section_type section
)
{
        return ((struct nxp_rtxxx_dsp_ctrl_api *)dev->api)
                ->load_section(dev, base, length, section);
}

static inline void nxp_rtxxx_dsp_ctrl_enable(const struct device *dev)
{
        ((struct nxp_rtxxx_dsp_ctrl_api *)dev->api)->enable(dev);
}

static inline void nxp_rtxxx_dsp_ctrl_disable(const struct device *dev)
{
        ((struct nxp_rtxxx_dsp_ctrl_api *)dev->api)->disable(dev);
}

#endif /* ZEPHYR_INCLUDE_DRIVERS_MISC_NXP_RTXXX_DSP_CTRL_NXP_RTXXX_DSP_CTRL_H_ */
```

## 165.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 79 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MISC_NXP_RTXXX_DSP_CTRL_NXP_RTXXX_DSP_CTRL_H_`。

## 165.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/dt-bindings/misc/nxp_rtxxx_dsp_ctrl.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2misc_2nxp__rtxxx__dsp__ctrl_8h.html)
- [nxp_rtxxx_dsp_ctrl_section_type](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.html#a1230a21b6c11930f80fc5f12605de762)
- [NXP_RTXXX_DSP_CTRL_SECTION_RESET](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.html#a1230a21b6c11930f80fc5f12605de762a8c63b3117b7c525e96be2b054395cfff)
- [NXP_RTXXX_DSP_REGION_RESET](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2misc_2nxp__rtxxx__dsp__ctrl_8h.html#abb4669be96440c29192dc3cf707fce65)
- [NXP_RTXXX_DSP_CTRL_SECTION_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.html#a1230a21b6c11930f80fc5f12605de762ab0c726ddfdf30c89075fcf9c7b4586e7)
- [NXP_RTXXX_DSP_REGION_TEXT](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2misc_2nxp__rtxxx__dsp__ctrl_8h.html#a2ae85fcd536b453408eca1cba00b308b)
- [NXP_RTXXX_DSP_CTRL_SECTION_DATA](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.html#a1230a21b6c11930f80fc5f12605de762aa43ff75c06ea161e322d77b8dede7791)
- [NXP_RTXXX_DSP_REGION_DATA](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2misc_2nxp__rtxxx__dsp__ctrl_8h.html#a70bd7dc09d64c9f7ed92d743a900d068)
- [nxp_rtxxx_dsp_ctrl_api_load_section](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.html#ab6ed31cfcaa45744f960bc19d89f642f)
- [device](../device_reference/P002_设备对象结构.md)
- [nxp_rtxxx_dsp_ctrl_api_enable](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.html#a561283f2992839e0191d2fcfef12d989)
- [nxp_rtxxx_dsp_ctrl_api_disable](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.html#a17b3a647a7798b34c820366916b2a1c5)
- [nxp_rtxxx_dsp_ctrl_api](../platform_security_model_reference/P023_nxp_rtxxx_dsp_ctrl_api_结构体.md)
- [load_section](../platform_security_model_reference/P023_nxp_rtxxx_dsp_ctrl_api_结构体.md#a5c8bbe71bd90f2a375011ac15695de1d)
- [enable](../platform_security_model_reference/P023_nxp_rtxxx_dsp_ctrl_api_结构体.md#a234285d700833f09ca73d80d35d13a87)
- [disable](../platform_security_model_reference/P023_nxp_rtxxx_dsp_ctrl_api_结构体.md#a2c98dc2c0d65b1004b94be86d99778c5)
- [nxp_rtxxx_dsp_ctrl_load_section](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.html#af1bd0005fe3a6d46d559b249b3ff8ca8)
- [api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [nxp_rtxxx_dsp_ctrl_enable](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.html#a9cc6dd311f29f2e7c79fc74c39658041)
- [nxp_rtxxx_dsp_ctrl_disable](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.html#a2efeac2828998f896f2e1bfb532700cd)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [nxp_rtxxx_dsp_ctrl.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2misc_2nxp__rtxxx__dsp__ctrl_8h.html)
- [device::api](../device_reference/P002_设备对象结构.md#a4a2e6a2cfeb6efed7d5383c33458f46d)
- [nxp_rtxxx_dsp_ctrl_api::enable](../platform_security_model_reference/P023_nxp_rtxxx_dsp_ctrl_api_结构体.md#a234285d700833f09ca73d80d35d13a87)
- [nxp_rtxxx_dsp_ctrl_api::disable](../platform_security_model_reference/P023_nxp_rtxxx_dsp_ctrl_api_结构体.md#a2c98dc2c0d65b1004b94be86d99778c5)
- [nxp_rtxxx_dsp_ctrl_api::load_section](../platform_security_model_reference/P023_nxp_rtxxx_dsp_ctrl_api_结构体.md#a5c8bbe71bd90f2a375011ac15695de1d)

---

[上一章](P164_mipi_dbi.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P166_devicetree.h_源码浏览.md)
