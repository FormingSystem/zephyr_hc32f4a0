---
id: learning.zephyr-docs.api-file-supplement-reference.page-17
title: zephyr__drivers__clock_control__clock_control_ambiq.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ambiq_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_drivers\_\_clock\_control\_\_clock\_control\_ambiq.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ambiq_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Ambiq设备的时钟子系统标识符（Clock Subsystem Identifiers）。

查看此文件的源码。

<a id="details"></a>

Ambiq设备的时钟子系统标识符（Clock Subsystem Identifiers）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 17.1\_枚举（Enumerations）

<a id="r_gabe05789f4191227f9cbc2e6755e13c8c"></a>

```c
enum clock_control_ambiq_type { CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_BLE , CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_USB , CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_ADC , CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_AUADC , CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_DBGCTRL , CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_CLKGEN_MISC , CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_CLKGEN_CLKOUT , CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_PDM , CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_IIS , CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_IOM , CLOCK_CONTROL_AMBIQ_TYPE_LFXTAL , CLOCK_CONTROL_AMBIQ_TYPE_MAX }
```

相关声明：[clock_control_ambiq_type](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#gabe05789f4191227f9cbc2e6755e13c8c)、[CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_BLE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8ca935745058b3bcd41fab102341573bd83)、[CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_USB](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8ca68bdc3aa9a99d49e46e99bada885b727)、[CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8ca11a81380c22880e5eefff8ae4e73336e)、[CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_AUADC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8ca3383b78c966e6e98d39a784232e91208)、[CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_DBGCTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8ca170229b6f0d44273a5a055a225f8c2e8)、[CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_CLKGEN_MISC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8cabc4feb1ac062903f2289168573a6c3fc)、[CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_CLKGEN_CLKOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8ca93b3569c34d2a50baa0843f43495a4d3)、[CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_PDM](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8cacfe43e2a43499e4c049e6a49492347c3)、[CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_IIS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8cad5dcc388f72556a7334059ee75b772e9)、[CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_IOM](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8ca88af5c919f1e0e118b534734c5b43658)、[CLOCK_CONTROL_AMBIQ_TYPE_LFXTAL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8caccf3220195f88dfd12aaf7e556aa693f)、[CLOCK_CONTROL_AMBIQ_TYPE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html#ggabe05789f4191227f9cbc2e6755e13c8ca7e025623774e3d3b642eede1df96ce5b)。

由 CLOCK 外设（Peripheral）处理的时钟（Clocks）。


## 17.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P099_clock_control_ambiq.h_源码浏览.md)
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

<a id="header-details"></a>

---

[上一章](P016_zephyr__drivers__clock_control__clock_control_adsp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P018_zephyr__drivers__clock_control__clock_control_rpi_pico.h_文件参考.md)
