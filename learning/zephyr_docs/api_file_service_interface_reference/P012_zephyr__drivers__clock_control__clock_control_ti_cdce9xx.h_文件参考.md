---
id: learning.zephyr-docs.api-file-service-interface-reference.page-12
title: zephyr__drivers__clock_control__clock_control_ti_cdce9xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ti__cdce9xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_drivers\_\_clock\_control\_\_clock\_control\_ti\_cdce9xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__ti__cdce9xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TI cdce9xx设备的时钟控制定义（Clock Control Definitions）。

<a id="details"></a>

```c
#include <zephyr/drivers/clock_control.h>
```

查看此文件的源码。

TI cdce9xx设备的时钟控制定义（Clock Control Definitions）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.1\_宏定义（Macros）

<a id="r_gae4415e893a54419a53ad75dfdcec79df"></a>

```c
#define CLOCK_CONTROL_TI_CDCE9XX_ALL (CLOCK_CONTROL_SUBSYS_ALL)
```

相关声明：[CLOCK_CONTROL_TI_CDCE9XX_ALL](../api_network_time_topic_reference/P007_德州仪器（TI）.md#gae4415e893a54419a53ad75dfdcec79df)、[CLOCK_CONTROL_SUBSYS_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#ga9aa9a4e00c1e7985a1fea6bed235003e)。

指代所有输出（ALL outputs）。

<a id="r_ga44fb15e0911d4e68afb6cf7ed0eec787"></a>

```c
#define CLOCK_CONTROL_TI_CDCE9XX_Y1 ((clock_control_subsys_t)1)
```

相关声明：[CLOCK_CONTROL_TI_CDCE9XX_Y1](../api_network_time_topic_reference/P007_德州仪器（TI）.md#ga44fb15e0911d4e68afb6cf7ed0eec787)、[clock_control_subsys_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gaa7d3935eaaf18902801a7d94859483db)。

选择 Y1 输出。

<a id="r_ga01a16dfba52df443e0e8c327bc042e75"></a>

```c
#define CLOCK_CONTROL_TI_CDCE9XX_Y2 ((clock_control_subsys_t)2)
```

相关声明：[CLOCK_CONTROL_TI_CDCE9XX_Y2](../api_network_time_topic_reference/P007_德州仪器（TI）.md#ga01a16dfba52df443e0e8c327bc042e75)、[clock_control_subsys_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gaa7d3935eaaf18902801a7d94859483db)。

选择 Y2 输出。

<a id="r_ga7c0b3c0e0c89fd579d1f6ee773de34cd"></a>

```c
#define CLOCK_CONTROL_TI_CDCE9XX_Y3 ((clock_control_subsys_t)3)
```

相关声明：[CLOCK_CONTROL_TI_CDCE9XX_Y3](../api_network_time_topic_reference/P007_德州仪器（TI）.md#ga7c0b3c0e0c89fd579d1f6ee773de34cd)、[clock_control_subsys_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gaa7d3935eaaf18902801a7d94859483db)。

选择 Y3 输出。

<a id="r_gad85c20f3b626ab2397a2a8bfaa21c5b4"></a>

```c
#define CLOCK_CONTROL_TI_CDCE9XX_Y4 ((clock_control_subsys_t)4)
```

相关声明：[CLOCK_CONTROL_TI_CDCE9XX_Y4](../api_network_time_topic_reference/P007_德州仪器（TI）.md#gad85c20f3b626ab2397a2a8bfaa21c5b4)、[clock_control_subsys_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gaa7d3935eaaf18902801a7d94859483db)。

选择 Y4 输出。

<a id="r_ga14f39e492b1089370ea416f72afea002"></a>

```c
#define CLOCK_CONTROL_TI_CDCE9XX_Y5 ((clock_control_subsys_t)5)
```

相关声明：[CLOCK_CONTROL_TI_CDCE9XX_Y5](../api_network_time_topic_reference/P007_德州仪器（TI）.md#ga14f39e492b1089370ea416f72afea002)、[clock_control_subsys_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gaa7d3935eaaf18902801a7d94859483db)。

选择 Y5 输出。

<a id="r_ga675c0e9d6e2eaa2514c108077a67d842"></a>

```c
#define CLOCK_CONTROL_TI_CDCE9XX_Y6 ((clock_control_subsys_t)6)
```

相关声明：[CLOCK_CONTROL_TI_CDCE9XX_Y6](../api_network_time_topic_reference/P007_德州仪器（TI）.md#ga675c0e9d6e2eaa2514c108077a67d842)、[clock_control_subsys_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gaa7d3935eaaf18902801a7d94859483db)。

选择 Y6 输出。

<a id="r_ga9794cc5ee0e2931d4fde4716fa6dfa0e"></a>

```c
#define CLOCK_CONTROL_TI_CDCE9XX_Y7 ((clock_control_subsys_t)7)
```

相关声明：[CLOCK_CONTROL_TI_CDCE9XX_Y7](../api_network_time_topic_reference/P007_德州仪器（TI）.md#ga9794cc5ee0e2931d4fde4716fa6dfa0e)、[clock_control_subsys_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gaa7d3935eaaf18902801a7d94859483db)。

选择 Y7 输出。

<a id="r_ga23c94a467ee684793fa552156e739609"></a>

```c
#define CLOCK_CONTROL_TI_CDCE9XX_Y8 ((clock_control_subsys_t)8)
```

相关声明：[CLOCK_CONTROL_TI_CDCE9XX_Y8](../api_network_time_topic_reference/P007_德州仪器（TI）.md#ga23c94a467ee684793fa552156e739609)、[clock_control_subsys_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gaa7d3935eaaf18902801a7d94859483db)。

选择 Y8 输出。

<a id="r_ga707dd310cee34972dd5e0b7824763f65"></a>

```c
#define CLOCK_CONTROL_TI_CDCE9XX_Y9 ((clock_control_subsys_t)9)
```

相关声明：[CLOCK_CONTROL_TI_CDCE9XX_Y9](../api_network_time_topic_reference/P007_德州仪器（TI）.md#ga707dd310cee34972dd5e0b7824763f65)、[clock_control_subsys_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gaa7d3935eaaf18902801a7d94859483db)。

选择 Y9 输出。


## 12.2\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control.h](../timer_reference/P096_时钟控制完整头文件.md)
- [查看此文件的源码。](../api_source_supplement_reference/P030_clock_control_ti_cdce9xx.h_源码浏览.md)
- [CLOCK_CONTROL_TI_CDCE9XX_ALL](../api_network_time_topic_reference/P007_德州仪器（TI）.md#gae4415e893a54419a53ad75dfdcec79df)
- [CLOCK_CONTROL_SUBSYS_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#ga9aa9a4e00c1e7985a1fea6bed235003e)
- [CLOCK_CONTROL_TI_CDCE9XX_Y1](../api_network_time_topic_reference/P007_德州仪器（TI）.md#ga44fb15e0911d4e68afb6cf7ed0eec787)
- [clock_control_subsys_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gaa7d3935eaaf18902801a7d94859483db)
- [CLOCK_CONTROL_TI_CDCE9XX_Y2](../api_network_time_topic_reference/P007_德州仪器（TI）.md#ga01a16dfba52df443e0e8c327bc042e75)
- [CLOCK_CONTROL_TI_CDCE9XX_Y3](../api_network_time_topic_reference/P007_德州仪器（TI）.md#ga7c0b3c0e0c89fd579d1f6ee773de34cd)
- [CLOCK_CONTROL_TI_CDCE9XX_Y4](../api_network_time_topic_reference/P007_德州仪器（TI）.md#gad85c20f3b626ab2397a2a8bfaa21c5b4)
- [CLOCK_CONTROL_TI_CDCE9XX_Y5](../api_network_time_topic_reference/P007_德州仪器（TI）.md#ga14f39e492b1089370ea416f72afea002)
- [CLOCK_CONTROL_TI_CDCE9XX_Y6](../api_network_time_topic_reference/P007_德州仪器（TI）.md#ga675c0e9d6e2eaa2514c108077a67d842)
- [CLOCK_CONTROL_TI_CDCE9XX_Y7](../api_network_time_topic_reference/P007_德州仪器（TI）.md#ga9794cc5ee0e2931d4fde4716fa6dfa0e)
- [CLOCK_CONTROL_TI_CDCE9XX_Y8](../api_network_time_topic_reference/P007_德州仪器（TI）.md#ga23c94a467ee684793fa552156e739609)
- [CLOCK_CONTROL_TI_CDCE9XX_Y9](../api_network_time_topic_reference/P007_德州仪器（TI）.md#ga707dd310cee34972dd5e0b7824763f65)

<a id="header-details"></a>

---

[上一章](P011_zephyr__drivers__uart__cdc_acm.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__modem__cmux.h_文件参考.md)
