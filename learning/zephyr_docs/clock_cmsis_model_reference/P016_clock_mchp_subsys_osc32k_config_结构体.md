---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-16
title: clock_mchp_subsys_osc32k_config_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__osc32k__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_clock\_mchp\_subsys\_osc32k\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__osc32k__config.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

32 kHz 内部振荡器（OSC32K）配置。

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32cm_jh.h>
```

<a id="details"></a>

32 kHz 内部振荡器（OSC32K）配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 16.1\_数据成员（Data Fields）

<a id="r_ace2f42ea255ec213ed207b18538a2a2d"></a>

```c
bool on_demand_en
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[on_demand_en](#ace2f42ea255ec213ed207b18538a2a2d)。

外设请求将振荡器用作时钟源时开启振荡器。

<a id="r_a8343157fa2c56424b9fc9768237e1922"></a>

```c
bool run_in_standby_en
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[run_in_standby_en](#a8343157fa2c56424b9fc9768237e1922)。

在待机睡眠模式（Standby Sleep Mode）中保持振荡器开启，除非设置了 `on_demand_en`。

## 16.2\_详细说明（Detailed Documentation）

<a id="ace2f42ea255ec213ed207b18538a2a2d"></a>

### `on_demand_en`

```c
bool clock_mchp_subsys_osc32k_config::on_demand_en
```

外设请求将振荡器用作时钟源时开启振荡器。

<a id="a8343157fa2c56424b9fc9768237e1922"></a>

### `run_in_standby_en`

```c
bool clock_mchp_subsys_osc32k_config::run_in_standby_en
```

在待机睡眠模式（Standby Sleep Mode）中保持振荡器开启，除非设置了 `on_demand_en`。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_clock_pic32cm_jh.h`

## 16.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_clock_pic32cm_jh.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__jh_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P015_clock_mchp_subsys_mclkcpu_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P017_clock_mchp_subsys_osc48m_config_结构体.md)
