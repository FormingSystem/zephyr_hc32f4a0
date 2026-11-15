---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-14
title: clock_mchp_subsys_gclkperiph_config_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__gclkperiph__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_clock\_mchp\_subsys\_gclkperiph\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__gclkperiph__config.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

通用时钟外设（GCLK Peripheral）配置结构体。

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h>
```

<a id="details"></a>

通用时钟外设（GCLK Peripheral）配置结构体，用于外设 GCLK 通道配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_a1727b4df3eb0dcff7365909002cef636"></a>

```c
enum clock_mchp_gclkgen src
```

相关声明：[clock_mchp_gclkgen](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gaab34442b0d6c171691ae299675542777)、[src](#a1727b4df3eb0dcff7365909002cef636)。

外设时钟使用的 GCLK 发生器源。

## 14.2\_详细说明（Detailed Documentation）

<a id="a1727b4df3eb0dcff7365909002cef636"></a>

### `src`

```c
enum clock_mchp_gclkgen clock_mchp_subsys_gclkperiph_config::src
```

外设时钟使用的 GCLK 发生器源。

为外设时钟供源的 GCLK 发生器。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h`
- `zephyr/drivers/clock_control/mchp_clock_pic32cm_jh.h`
- `zephyr/drivers/clock_control/mchp_clock_pic32cm_sg_gc.h`
- `zephyr/drivers/clock_control/mchp_clock_pic32cz_ca.h`
- `zephyr/drivers/clock_control/mchp_clock_sam_d5x_e5x.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h_source.html)
- [clock_mchp_gclkgen](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__sam__d5x__e5x.html#gaab34442b0d6c171691ae299675542777)
- [mchp_clock_pic32cm_jh.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__jh_8h_source.html)
- [mchp_clock_pic32cm_sg_gc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h_source.html)
- [mchp_clock_pic32cz_ca.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cz__ca_8h_source.html)
- [mchp_clock_sam_d5x_e5x.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__sam__d5x__e5x_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_clock_mchp_subsys_gclkgen_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_clock_mchp_subsys_mclkcpu_config_结构体.md)
