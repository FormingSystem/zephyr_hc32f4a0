---
id: learning.zephyr-docs.api-source-reference.page-99
title: clock_control_ambiq.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ambiq_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第99章\_clock\_control\_ambiq.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ambiq_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ambiq_8h.html)。

## 99.1\_原始可见代码（Source Code）

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
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="agroup__clock__control__ambiq_html_gabe05789f4191227f9cbc2e6755e13c8c"></a>
<a id="agroup__clock__control__ambiq_html_ggabe05789f4191227f9cbc2e6755e13c8ca11a81380c22880e5eefff8ae4e73336e"></a>
<a id="agroup__clock__control__ambiq_html_ggabe05789f4191227f9cbc2e6755e13c8ca170229b6f0d44273a5a055a225f8c2e8"></a>
<a id="agroup__clock__control__ambiq_html_ggabe05789f4191227f9cbc2e6755e13c8ca3383b78c966e6e98d39a784232e91208"></a>
<a id="agroup__clock__control__ambiq_html_ggabe05789f4191227f9cbc2e6755e13c8ca68bdc3aa9a99d49e46e99bada885b727"></a>
<a id="agroup__clock__control__ambiq_html_ggabe05789f4191227f9cbc2e6755e13c8ca7e025623774e3d3b642eede1df96ce5b"></a>
<a id="agroup__clock__control__ambiq_html_ggabe05789f4191227f9cbc2e6755e13c8ca88af5c919f1e0e118b534734c5b43658"></a>
<a id="agroup__clock__control__ambiq_html_ggabe05789f4191227f9cbc2e6755e13c8ca935745058b3bcd41fab102341573bd83"></a>
<a id="agroup__clock__control__ambiq_html_ggabe05789f4191227f9cbc2e6755e13c8ca93b3569c34d2a50baa0843f43495a4d3"></a>
<a id="agroup__clock__control__ambiq_html_ggabe05789f4191227f9cbc2e6755e13c8cabc4feb1ac062903f2289168573a6c3fc"></a>
<a id="agroup__clock__control__ambiq_html_ggabe05789f4191227f9cbc2e6755e13c8caccf3220195f88dfd12aaf7e556aa693f"></a>
<a id="agroup__clock__control__ambiq_html_ggabe05789f4191227f9cbc2e6755e13c8cacfe43e2a43499e4c049e6a49492347c3"></a>
<a id="agroup__clock__control__ambiq_html_ggabe05789f4191227f9cbc2e6755e13c8cad5dcc388f72556a7334059ee75b772e9"></a>

```c
/*
 * Copyright (c) 2023 Ambiq Micro Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_AMBIQ_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_AMBIQ_H_


#ifdef __cplusplus
extern "C" {
#endif

enum clock_control_ambiq_type {
        CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_BLE,
        CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_USB,
        CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_ADC,
        CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_AUADC,
        CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_DBGCTRL,
        CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_CLKGEN_MISC,
        CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_CLKGEN_CLKOUT,
        CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_PDM,
        CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_IIS,
        CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_IOM,
        CLOCK_CONTROL_AMBIQ_TYPE_LFXTAL,
        CLOCK_CONTROL_AMBIQ_TYPE_MAX
};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_AMBIQ_H_ */
```

## 99.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Ambiq Micro Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 51 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_AMBIQ_H_`。

## 99.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ambiq_8h.html)
- [clock_control_ambiq_type](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#gabe05789f4191227f9cbc2e6755e13c8c)
- [CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_BLE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8ca935745058b3bcd41fab102341573bd83)
- [CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_USB](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8ca68bdc3aa9a99d49e46e99bada885b727)
- [CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8ca11a81380c22880e5eefff8ae4e73336e)
- [CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_AUADC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8ca3383b78c966e6e98d39a784232e91208)
- [CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_DBGCTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8ca170229b6f0d44273a5a055a225f8c2e8)
- [CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_CLKGEN_MISC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8cabc4feb1ac062903f2289168573a6c3fc)
- [CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_CLKGEN_CLKOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8ca93b3569c34d2a50baa0843f43495a4d3)
- [CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_PDM](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8cacfe43e2a43499e4c049e6a49492347c3)
- [CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_IIS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8cad5dcc388f72556a7334059ee75b772e9)
- [CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_IOM](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8ca88af5c919f1e0e118b534734c5b43658)
- [CLOCK_CONTROL_AMBIQ_TYPE_LFXTAL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8caccf3220195f88dfd12aaf7e556aa693f)
- [CLOCK_CONTROL_AMBIQ_TYPE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8ca7e025623774e3d3b642eede1df96ce5b)

---

[上一章](P098_clock_control_adsp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P100_clock_control_ifx.h_源码浏览.md)
