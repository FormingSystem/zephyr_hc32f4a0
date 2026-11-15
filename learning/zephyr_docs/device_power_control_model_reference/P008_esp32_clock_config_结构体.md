---
id: learning.zephyr-docs.device-power-control-model-reference.page-8
title: esp32_clock_config_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structesp32__clock__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_esp32\_clock\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structesp32__clock__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ESP32的汇总时钟配置（Aggregate Clock Configuration）。

```c
#include <zephyr/drivers/clock_control/esp32_clock_control.h>
```

<a id="details"></a>

ESP32的汇总时钟配置（Aggregate Clock Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_a5cf7a77ea5b5e4780bde683c2cd10526"></a>

```c
struct esp32_cpu_clock_config cpu
```

相关声明：[esp32_cpu_clock_config](P009_esp32_cpu_clock_config_结构体.md)、[cpu](#a5cf7a77ea5b5e4780bde683c2cd10526)。

CPU 时钟配置。

<a id="r_ad42eba0397b1a988357b83a030298078"></a>

```c
struct esp32_rtc_clock_config rtc
```

相关声明：[esp32_rtc_clock_config](P010_esp32_rtc_clock_config_结构体.md)、[rtc](#ad42eba0397b1a988357b83a030298078)。

实时时钟（RTC）时钟配置。

## 8.2\_详细说明（Detailed Documentation）

<a id="a5cf7a77ea5b5e4780bde683c2cd10526"></a>

### `cpu`

```c
struct esp32_cpu_clock_config esp32_clock_config::cpu
```

CPU 时钟配置。

<a id="ad42eba0397b1a988357b83a030298078"></a>

### `rtc`

```c
struct esp32_rtc_clock_config esp32_clock_config::rtc
```

实时时钟（RTC）时钟配置。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/esp32_clock_control.h`

## 8.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/esp32_clock_control.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32__clock__control_8h_source.html)
- [esp32_cpu_clock_config](P009_esp32_cpu_clock_config_结构体.md)
- [esp32_rtc_clock_config](P010_esp32_rtc_clock_config_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_dummy_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P009_esp32_cpu_clock_config_结构体.md)
