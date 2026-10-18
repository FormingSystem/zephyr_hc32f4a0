---
id: learning.zephyr-docs.device-power-control-model-reference.page-64
title: pulse_io_config_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpulse__io__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_pulse\_io\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpulse__io__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通道配置（Channel Configuration）。

```c
#include <zephyr/drivers/pulse_io.h>
```

<a id="details"></a>

通道配置（Channel configuration），传递给 `pulse_io_channel_configure`。与选定 `mode` 或 `dir` 无关的字段会被忽略。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 64.1\_数据成员（Data Fields）

<a id="r_a09ab3fcf00e4bab33f290695d045d9ce"></a>

```c
uint32_t resolution_hz
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[resolution_hz](#a09ab3fcf00e4bab33f290695d045d9ce)。

节拍频率，单位为 Hz。

<a id="r_a0c10cf29df1143a842fdde9cf1d49a42"></a>

```c
uint32_t cell_period_ticks
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cell_period_ticks](#a0c10cf29df1143a842fdde9cf1d49a42)。

仅用于 CELL 模式：单元周期，以节拍计。

<a id="r_a65c6a04405648635c9fea5ac47cf5063"></a>

```c
uint32_t carrier_hz
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[carrier_hz](#a65c6a04405648635c9fea5ac47cf5063)。

发送载波频率，单位为 Hz。

<a id="r_ae767da3eb5f3d4d516262c84972d261f"></a>

```c
uint32_t rx_idle_threshold_ticks
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rx_idle_threshold_ticks](#ae767da3eb5f3d4d516262c84972d261f)。

接收帧结束空闲阈值，以节拍计；`0` 表示禁用。

<a id="r_aef4876ae134c3aa2b1634ac6892f7c5e"></a>

```c
uint32_t rx_filter_ticks
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rx_filter_ticks](#aef4876ae134c3aa2b1634ac6892f7c5e)。

接收毛刺滤波器宽度，以节拍计；`0` 表示禁用。

<a id="r_a0d74c4cf0960039675f3806870c68a2c"></a>

```c
enum pulse_io_mode mode
```

相关声明：[pulse_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga8a69608ee00587642aca6e0d69878b07)、[mode](#a0d74c4cf0960039675f3806870c68a2c)。

通道的提交模式（Submission mode）。

<a id="r_aa0f9d3365b77ff5d80c6f9ec222ff5ff"></a>

```c
enum pulse_io_dir dir
```

相关声明：[pulse_io_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga1188071d39a4018b719f18d019ba6f89)、[dir](#aa0f9d3365b77ff5d80c6f9ec222ff5ff)。

通道方向。

<a id="r_a7466b1968e22a84f4542d0be6ee65304"></a>

```c
uint8_t carrier_duty_pct
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[carrier_duty_pct](#a7466b1968e22a84f4542d0be6ee65304)。

发送载波占空比（Duty cycle），以百分比表示。

<a id="r_a3f378f0c755b40de97c9c601f413b91f"></a>

```c
bool idle_high
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[idle_high](#a3f378f0c755b40de97c9c601f413b91f)。

空闲时的线路状态。

<a id="r_adeee7ddbc94ba628916ac3a6b029d337"></a>

```c
bool carrier_en
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[carrier_en](#adeee7ddbc94ba628916ac3a6b029d337)。

对非空闲电平启用发送载波调制。

<a id="r_a106d88a37daf50fd704a33e6fc49054a"></a>

```c
bool rx_carrier_demod
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[rx_carrier_demod](#a106d88a37daf50fd704a33e6fc49054a)。

接收时对非空闲电平启用硬件载波解调。

## 64.2\_详细说明（Detailed Documentation）

<a id="a7466b1968e22a84f4542d0be6ee65304"></a>

### `carrier_duty_pct`

```c
uint8_t pulse_io_config::carrier_duty_pct
```

发送载波占空比（Duty cycle），以百分比表示。

<a id="adeee7ddbc94ba628916ac3a6b029d337"></a>

### `carrier_en`

```c
bool pulse_io_config::carrier_en
```

对非空闲电平启用发送载波调制。

<a id="a65c6a04405648635c9fea5ac47cf5063"></a>

### `carrier_hz`

```c
uint32_t pulse_io_config::carrier_hz
```

发送载波频率，单位为 Hz。

<a id="a0c10cf29df1143a842fdde9cf1d49a42"></a>

### `cell_period_ticks`

```c
uint32_t pulse_io_config::cell_period_ticks
```

仅用于 CELL 模式：单元周期，以节拍计。

<a id="aa0f9d3365b77ff5d80c6f9ec222ff5ff"></a>

### `dir`

```c
enum pulse_io_dir pulse_io_config::dir
```

通道方向。

<a id="a3f378f0c755b40de97c9c601f413b91f"></a>

### `idle_high`

```c
bool pulse_io_config::idle_high
```

空闲时的线路状态。

对于发送，该值表示帧间及帧结束后线路保持的电平。载波调制和解调作用于非空闲的有效电平。接收捕获本身不依赖极性：收到的符号和单元均显式携带电平信息。

<a id="a0d74c4cf0960039675f3806870c68a2c"></a>

### `mode`

```c
enum pulse_io_mode pulse_io_config::mode
```

通道的提交模式（Submission mode）。

<a id="a09ab3fcf00e4bab33f290695d045d9ce"></a>

### `resolution_hz`

```c
uint32_t pulse_io_config::resolution_hz
```

节拍频率，单位为 Hz。

后端会选择最接近且可实现的值。

<a id="a106d88a37daf50fd704a33e6fc49054a"></a>

### `rx_carrier_demod`

```c
bool pulse_io_config::rx_carrier_demod
```

接收时对非空闲电平启用硬件载波解调。

<a id="aef4876ae134c3aa2b1634ac6892f7c5e"></a>

### `rx_filter_ticks`

```c
uint32_t pulse_io_config::rx_filter_ticks
```

接收毛刺滤波器宽度，以节拍计；`0` 表示禁用。

<a id="ae767da3eb5f3d4d516262c84972d261f"></a>

### `rx_idle_threshold_ticks`

```c
uint32_t pulse_io_config::rx_idle_threshold_ticks
```

接收帧结束空闲阈值，以节拍计；`0` 表示禁用。

本数据类型文档由以下文件生成：

- `zephyr/drivers/pulse_io.h`

## 64.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pulse_io.h](https://docs.zephyrproject.org/latest/doxygen/html/pulse__io_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pulse_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga8a69608ee00587642aca6e0d69878b07)
- [pulse_io_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#ga1188071d39a4018b719f18d019ba6f89)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [pulse_io_channel_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html#gaa3a5b31cb44647823aa60af4416e6d3f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P063_pulse_io_caps_结构体.md) · [返回大纲](大纲.md) · [下一章](P065_pulse_io_decoder_api_结构体.md)
