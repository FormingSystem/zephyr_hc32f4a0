---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-18
title: clock_mchp_subsys_oschf_config_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__oschf__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_clock\_mchp\_subsys\_oschf\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__oschf__config.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

高频振荡器（High-frequency Oscillator，OSCHF）子系统配置。

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32cm_pl.h>
```

<a id="details"></a>

高频振荡器（High-frequency Oscillator，OSCHF）子系统配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

<a id="r_a4980adab90c8f75a0b72de691a9f3b54"></a>

```c
bool on_demand_en
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[on_demand_en](#a4980adab90c8f75a0b72de691a9f3b54)。

外设请求将振荡器用作时钟源时，配置振荡器开启。

## 18.2\_详细说明（Detailed Documentation）

<a id="a4980adab90c8f75a0b72de691a9f3b54"></a>

### `on_demand_en`

```c
bool clock_mchp_subsys_oschf_config::on_demand_en
```

外设请求将振荡器用作时钟源时，配置振荡器开启。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_clock_pic32cm_pl.h`

## 18.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_clock_pic32cm_pl.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__pl_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_clock_mchp_subsys_osc48m_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P019_clock_mchp_subsys_pll_config_结构体.md)
