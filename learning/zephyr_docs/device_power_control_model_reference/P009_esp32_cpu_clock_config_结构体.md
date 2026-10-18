---
id: learning.zephyr-docs.device-power-control-model-reference.page-9
title: esp32_cpu_clock_config_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structesp32__cpu__clock__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_esp32\_cpu\_clock\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structesp32__cpu__clock__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ESP32的CPU时钟配置。

```c
#include <zephyr/drivers/clock_control/esp32_clock_control.h>
```

<a id="details"></a>

ESP32的CPU时钟配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

<a id="r_a7496bee5adc8d235bd4df9b93d791576"></a>

```c
int clk_src
```

相关声明：[clk_src](#a7496bee5adc8d235bd4df9b93d791576)。

CPU 时钟源（Clock source）。

<a id="r_a181474dc51b7ddca51bc9b56e7a935e4"></a>

```c
uint32_t cpu_freq
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cpu_freq](#a181474dc51b7ddca51bc9b56e7a935e4)。

目标 CPU 频率，单位为 MHz。

<a id="r_a6b7de043a1282e7ea73a2b81b5f0abfd"></a>

```c
uint32_t xtal_freq
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[xtal_freq](#a6b7de043a1282e7ea73a2b81b5f0abfd)。

外部晶体频率，单位为 MHz。

## 9.2\_详细说明（Detailed Documentation）

<a id="a7496bee5adc8d235bd4df9b93d791576"></a>

### `clk_src`

```c
int esp32_cpu_clock_config::clk_src
```

CPU 时钟源（Clock source）。

<a id="a181474dc51b7ddca51bc9b56e7a935e4"></a>

### `cpu_freq`

```c
uint32_t esp32_cpu_clock_config::cpu_freq
```

目标 CPU 频率，单位为 MHz。

<a id="a6b7de043a1282e7ea73a2b81b5f0abfd"></a>

### `xtal_freq`

```c
uint32_t esp32_cpu_clock_config::xtal_freq
```

外部晶体频率，单位为 MHz。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/esp32_clock_control.h`

## 9.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/esp32_clock_control.h](https://docs.zephyrproject.org/latest/doxygen/html/esp32__clock__control_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_esp32_clock_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P010_esp32_rtc_clock_config_结构体.md)
