---
id: learning.zephyr-docs.api-security-memory-topic-reference.page-1
title: Ambiq API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_Ambiq API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__ambiq.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 1.1\_文件（Files）

<a id="r_clock_5Fcontrol_5Fambiq_2Eh"></a>

```c
file clock_control_ambiq.h
```

相关声明：[clock_control_ambiq.h](../api_file_supplement_reference/P017_zephyr__drivers__clock_control__clock_control_ambiq.h_文件参考.md)。

Ambiq设备的时钟子系统标识符（Clock Subsystem Identifiers）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.2\_枚举（Enumerations）

<a id="r_gabe05789f4191227f9cbc2e6755e13c8c"></a>

```c
enum clock_control_ambiq_type { CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_BLE , CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_USB , CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_ADC , CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_AUADC , CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_DBGCTRL , CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_CLKGEN_MISC , CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_CLKGEN_CLKOUT , CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_PDM , CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_IIS , CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_IOM , CLOCK_CONTROL_AMBIQ_TYPE_LFXTAL , CLOCK_CONTROL_AMBIQ_TYPE_MAX }
```

相关声明：[clock_control_ambiq_type](#gabe05789f4191227f9cbc2e6755e13c8c)、[CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_BLE](#ggabe05789f4191227f9cbc2e6755e13c8ca935745058b3bcd41fab102341573bd83)、[CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_USB](#ggabe05789f4191227f9cbc2e6755e13c8ca68bdc3aa9a99d49e46e99bada885b727)、[CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_ADC](#ggabe05789f4191227f9cbc2e6755e13c8ca11a81380c22880e5eefff8ae4e73336e)、[CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_AUADC](#ggabe05789f4191227f9cbc2e6755e13c8ca3383b78c966e6e98d39a784232e91208)、[CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_DBGCTRL](#ggabe05789f4191227f9cbc2e6755e13c8ca170229b6f0d44273a5a055a225f8c2e8)、[CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_CLKGEN_MISC](#ggabe05789f4191227f9cbc2e6755e13c8cabc4feb1ac062903f2289168573a6c3fc)、[CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_CLKGEN_CLKOUT](#ggabe05789f4191227f9cbc2e6755e13c8ca93b3569c34d2a50baa0843f43495a4d3)、[CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_PDM](#ggabe05789f4191227f9cbc2e6755e13c8cacfe43e2a43499e4c049e6a49492347c3)、[CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_IIS](#ggabe05789f4191227f9cbc2e6755e13c8cad5dcc388f72556a7334059ee75b772e9)、[CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_IOM](#ggabe05789f4191227f9cbc2e6755e13c8ca88af5c919f1e0e118b534734c5b43658)、[CLOCK_CONTROL_AMBIQ_TYPE_LFXTAL](#ggabe05789f4191227f9cbc2e6755e13c8caccf3220195f88dfd12aaf7e556aa693f)、[CLOCK_CONTROL_AMBIQ_TYPE_MAX](#ggabe05789f4191227f9cbc2e6755e13c8ca7e025623774e3d3b642eede1df96ce5b)。

由 CLOCK 外设（Peripheral）处理的时钟（Clocks）。

## 1.3\_详细说明（Detailed Documentation）

<a id="gabe05789f4191227f9cbc2e6755e13c8c"></a>

### `clock_control_ambiq_type`

```c
enum clock_control_ambiq_type
```

```c
#include <zephyr/drivers/clock_control/clock_control_ambiq.h>
```

由 CLOCK 外设（Peripheral）处理的时钟（Clocks）。

用作 `clock_control` API 的 `sys` 参数。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_BLE` | 蓝牙低功耗（BLE）控制器的 HFXTAL 时钟。 |
| `CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_USB` | USB 的 HFXTAL 时钟。 |
| `CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_ADC` | 模数转换器（ADC）的 HFXTAL 时钟。 |
| `CLOCK_CONTROL_AMBIQ_TYPE_HFXTAL_AUADC` | 音频模数转换器（Audio ADC）的 HFXTAL 时钟。 |
| `CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_DBGCTRL` | 调试控制（Debug Control）的 HCXTAL 时钟。 |
| `CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_CLKGEN_MISC` | 时钟发生器其他功能（Clock Generator Misc）的 HCXTAL 时钟。 |
| `CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_CLKGEN_CLKOUT` | 时钟输出（Clock Output）的 HCXTAL 时钟。 |
| `CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_PDM` | 脉冲密度调制（PDM）的 HCXTAL 时钟。 |
| `CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_IIS` | 音频总线（I2S）的 HCXTAL 时钟。 |
| `CLOCK_CONTROL_AMBIQ_TYPE_HCXTAL_IOM` | 输入输出主机（I/O Master）的 HCXTAL 时钟。 |
| `CLOCK_CONTROL_AMBIQ_TYPE_LFXTAL` | 低频晶体振荡器（Low-frequency Crystal Oscillator）。 |
| `CLOCK_CONTROL_AMBIQ_TYPE_MAX` | 时钟子系统类型（Clock Subsystem Types）的数量。 |


## 1.4\_原页交叉引用（Cross References）

- [clock_control_ambiq.h](../api_file_supplement_reference/P017_zephyr__drivers__clock_control__clock_control_ambiq.h_文件参考.md)
- [clock_control](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface__backend.html#ga459b95cb726892b95537d15273413099)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggabe05789f4191227f9cbc2e6755e13c8ca935745058b3bcd41fab102341573bd83"></a>
<a id="ggabe05789f4191227f9cbc2e6755e13c8ca68bdc3aa9a99d49e46e99bada885b727"></a>
<a id="ggabe05789f4191227f9cbc2e6755e13c8ca11a81380c22880e5eefff8ae4e73336e"></a>
<a id="ggabe05789f4191227f9cbc2e6755e13c8ca3383b78c966e6e98d39a784232e91208"></a>
<a id="ggabe05789f4191227f9cbc2e6755e13c8ca170229b6f0d44273a5a055a225f8c2e8"></a>
<a id="ggabe05789f4191227f9cbc2e6755e13c8cabc4feb1ac062903f2289168573a6c3fc"></a>
<a id="ggabe05789f4191227f9cbc2e6755e13c8ca93b3569c34d2a50baa0843f43495a4d3"></a>
<a id="ggabe05789f4191227f9cbc2e6755e13c8cacfe43e2a43499e4c049e6a49492347c3"></a>
<a id="ggabe05789f4191227f9cbc2e6755e13c8cad5dcc388f72556a7334059ee75b772e9"></a>
<a id="ggabe05789f4191227f9cbc2e6755e13c8ca88af5c919f1e0e118b534734c5b43658"></a>
<a id="ggabe05789f4191227f9cbc2e6755e13c8caccf3220195f88dfd12aaf7e556aa693f"></a>
<a id="ggabe05789f4191227f9cbc2e6755e13c8ca7e025623774e3d3b642eede1df96ce5b"></a>

---

[返回大纲](大纲.md) · [下一章](P002_CoAP的受限RESTful环境对象安全（OSCORE）API。.md)
