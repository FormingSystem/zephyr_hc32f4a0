---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-15
title: clock_mchp_subsys_mclkcpu_config_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__mclkcpu__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_clock\_mchp\_subsys\_mclkcpu\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__mclkcpu__config.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

主时钟（MCLK）配置结构体。

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h>
```

<a id="details"></a>

主时钟（MCLK）配置结构体，供 `CLOCK_MCHP_SUBSYS_TYPE_MCLKDOMAIN` 和 `CLOCK_MCHP_SUBSYS_TYPE_MCLKCPU` 使用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_a380cc94c6ed19143a29f2590af21f672"></a>

```c
enum clock_mchp_mclk_cpu_div division_factor
```

相关声明：[clock_mchp_mclk_cpu_div](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ga5835567db8d16c4eeb7a03b843ac6254)、[division_factor](#a380cc94c6ed19143a29f2590af21f672)。

CPU 的 MCLK 预分频器（Prescaler）分频比。

## 15.2\_详细说明（Detailed Documentation）

<a id="a380cc94c6ed19143a29f2590af21f672"></a>

### `division_factor`

```c
enum clock_mchp_mclk_cpu_div clock_mchp_subsys_mclkcpu_config::division_factor
```

CPU 的 MCLK 预分频器（Prescaler）分频比。

CPU 的 MCLK 预分频器分频比。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h`
- `zephyr/drivers/clock_control/mchp_clock_pic32cm_jh.h`
- `zephyr/drivers/clock_control/mchp_clock_pic32cm_sg_gc.h`
- `zephyr/drivers/clock_control/mchp_clock_pic32cz_ca.h`
- `zephyr/drivers/clock_control/mchp_clock_sam_d5x_e5x.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h_source.html)
- [clock_mchp_mclk_cpu_div](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#ga5835567db8d16c4eeb7a03b843ac6254)
- [mchp_clock_pic32cm_jh.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__jh_8h_source.html)
- [mchp_clock_pic32cm_sg_gc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h_source.html)
- [mchp_clock_pic32cz_ca.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cz__ca_8h_source.html)
- [mchp_clock_sam_d5x_e5x.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__sam__d5x__e5x_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P014_clock_mchp_subsys_gclkperiph_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P016_clock_mchp_subsys_osc32k_config_结构体.md)
