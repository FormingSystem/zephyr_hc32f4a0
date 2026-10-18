---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-23
title: clock_mchp_subsys_xosc_config_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__xosc__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_clock\_mchp\_subsys\_xosc\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__xosc__config.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

外部晶体振荡器（External Crystal Oscillator）配置结构体。

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h>
```

<a id="details"></a>

外部晶体振荡器配置结构体，用于外部振荡器（XOSC）配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 23.1\_数据成员（Data Fields）

<a id="r_a51e27943063374fa67b03509d8d8b962"></a>

```c
bool on_demand_en
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[on_demand_en](#a51e27943063374fa67b03509d8d8b962)。

外设请求将振荡器用作时钟源时，配置振荡器开启。

<a id="r_a298c2524a043091ab6f591759d03c72b"></a>

```c
bool run_in_standby_en
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[run_in_standby_en](#a298c2524a043091ab6f591759d03c72b)。

在待机睡眠模式（Standby Sleep Mode）中保持振荡器开启，除非设置了 `on_demand_en`。

## 23.2\_详细说明（Detailed Documentation）

<a id="a51e27943063374fa67b03509d8d8b962"></a>

### `on_demand_en`

```c
bool clock_mchp_subsys_xosc_config::on_demand_en
```

外设请求将振荡器用作时钟源时，配置振荡器开启。

外设请求将振荡器用作时钟源时开启振荡器。

<a id="a298c2524a043091ab6f591759d03c72b"></a>

### `run_in_standby_en`

```c
bool clock_mchp_subsys_xosc_config::run_in_standby_en
```

在待机睡眠模式（Standby Sleep Mode）中保持振荡器开启，除非设置了 `on_demand_en`。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h`
- `zephyr/drivers/clock_control/mchp_clock_pic32cm_jh.h`
- `zephyr/drivers/clock_control/mchp_clock_pic32cm_sg_gc.h`
- `zephyr/drivers/clock_control/mchp_clock_pic32cz_ca.h`
- `zephyr/drivers/clock_control/mchp_clock_sam_d5x_e5x.h`

## 23.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [mchp_clock_pic32cm_jh.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__jh_8h_source.html)
- [mchp_clock_pic32cm_sg_gc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h_source.html)
- [mchp_clock_pic32cz_ca.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cz__ca_8h_source.html)
- [mchp_clock_sam_d5x_e5x.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__sam__d5x__e5x_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P022_clock_mchp_subsys_xosc32k_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P024_cmsis_rtos_event_cb_结构体.md)
