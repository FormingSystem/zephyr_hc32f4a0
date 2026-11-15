---
id: learning.zephyr-docs.device-power-control-model-reference.page-10
title: esp32_rtc_clock_config_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structesp32__rtc__clock__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_esp32\_rtc\_clock\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structesp32__rtc__clock__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ESP32的实时时钟（RTC）配置。

```c
#include <zephyr/drivers/clock_control/esp32_clock_control.h>
```

<a id="details"></a>

ESP32的实时时钟（RTC）配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_a2d4090c4e97f15c4ab04d92905d5119c"></a>

```c
uint32_t rtc_fast_clock_src
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rtc_fast_clock_src](#a2d4090c4e97f15c4ab04d92905d5119c)。

RTC 快速时钟源。

<a id="r_ae04b2762e26a5e8d135c91b6f5d360e9"></a>

```c
uint32_t rtc_slow_clock_src
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rtc_slow_clock_src](#ae04b2762e26a5e8d135c91b6f5d360e9)。

RTC 慢速时钟源。

## 10.2\_详细说明（Detailed Documentation）

<a id="a2d4090c4e97f15c4ab04d92905d5119c"></a>

### `rtc_fast_clock_src`

```c
uint32_t esp32_rtc_clock_config::rtc_fast_clock_src
```

RTC 快速时钟源。

<a id="ae04b2762e26a5e8d135c91b6f5d360e9"></a>

### `rtc_slow_clock_src`

```c
uint32_t esp32_rtc_clock_config::rtc_slow_clock_src
```

RTC 慢速时钟源。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/esp32_clock_control.h`

## 10.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/esp32_clock_control.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32__clock__control_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_esp32_cpu_clock_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P011_fuel_gauge_driver_api_结构体.md)
