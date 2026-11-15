---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-17
title: clock_mchp_subsys_osc48m_config_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__osc48m__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_clock\_mchp\_subsys\_osc48m\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__osc48m__config.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

内部 48 MHz 振荡器（OSC48M）配置。

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32cm_jh.h>
```

<a id="details"></a>

内部 48 MHz 振荡器（OSC48M）配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 17.1\_数据成员（Data Fields）

<a id="r_a191da6844eba2d9c20d4b21bedf825da"></a>

```c
bool on_demand_en
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[on_demand_en](#a191da6844eba2d9c20d4b21bedf825da)。

外设请求将振荡器用作时钟源时开启振荡器。

<a id="r_ad5ee1cd0de32cff6c1e3726e56b33efc"></a>

```c
bool run_in_standby_en
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[run_in_standby_en](#ad5ee1cd0de32cff6c1e3726e56b33efc)。

在待机睡眠模式（Standby Sleep Mode）中保持振荡器开启，除非设置了 `on_demand_en`。

<a id="r_aa2e9756157bdb1d71ff586c7baa5d856"></a>

```c
enum clock_mchp_osc48m_divider_freq post_divider_freq
```

相关声明：[clock_mchp_osc48m_divider_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ga4303aa06f4b9a93874f2d26406e788e3)、[post_divider_freq](#aa2e9756157bdb1d71ff586c7baa5d856)。

通过调整分频比控制振荡器频率范围。

## 17.2\_详细说明（Detailed Documentation）

<a id="a191da6844eba2d9c20d4b21bedf825da"></a>

### `on_demand_en`

```c
bool clock_mchp_subsys_osc48m_config::on_demand_en
```

外设请求将振荡器用作时钟源时开启振荡器。

<a id="aa2e9756157bdb1d71ff586c7baa5d856"></a>

### `post_divider_freq`

```c
enum clock_mchp_osc48m_divider_freq clock_mchp_subsys_osc48m_config::post_divider_freq
```

通过调整分频比控制振荡器频率范围。

<a id="ad5ee1cd0de32cff6c1e3726e56b33efc"></a>

### `run_in_standby_en`

```c
bool clock_mchp_subsys_osc48m_config::run_in_standby_en
```

在待机睡眠模式（Standby Sleep Mode）中保持振荡器开启，除非设置了 `on_demand_en`。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_clock_pic32cm_jh.h`

## 17.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_clock_pic32cm_jh.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__jh_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [clock_mchp_osc48m_divider_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cm__jh.html#ga4303aa06f4b9a93874f2d26406e788e3)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P016_clock_mchp_subsys_osc32k_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P018_clock_mchp_subsys_oschf_config_结构体.md)
