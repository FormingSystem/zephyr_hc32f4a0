---
id: learning.zephyr-docs.api-device-topic-reference.page-3
title: BQ274XX API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bq274xx__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_BQ274XX API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bq274xx__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Texas Instruments BQ274xx 电池电量计（Battery fuel gauge）。

<a id="details"></a>

Texas Instruments BQ274xx 电池电量计（Battery fuel gauge）。

<a id="header-files"></a>
<a id="files"></a>

## 3.1\_文件（Files）

<a id="r_bq274xx_2Eh"></a>

```c
file bq274xx.h
```

相关声明：[bq274xx.h](https://docs.zephyrproject.org/latest/doxygen/html/bq274xx_8h.html)。

the TI BQ274xx fuel gauges的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 3.2\_BQ27427 化学特性标识符（chemistry IDs）

设备树 `chemistry-id` 属性的取值。

<a id="r_gafd885c85ac533a7640f93e97fec8ccb9"></a>

```c
#define BQ27427_CHEM_ID_A 0x3230
```

相关声明：[BQ27427_CHEM_ID_A](#gafd885c85ac533a7640f93e97fec8ccb9)。

电池化学特性配置 A（Chemistry profile A），4.35 V。

<a id="r_gaafd294ad5ecf988c816ed258e61fa781"></a>

```c
#define BQ27427_CHEM_ID_B 0x1202
```

相关声明：[BQ27427_CHEM_ID_B](#gaafd294ad5ecf988c816ed258e61fa781)。

电池化学特性配置 B（Chemistry profile B），4.2 V，默认配置。

<a id="r_gac932a2d227876901d5a001a46b0aba07"></a>

```c
#define BQ27427_CHEM_ID_C 0x3142
```

相关声明：[BQ27427_CHEM_ID_C](#gac932a2d227876901d5a001a46b0aba07)。

电池化学特性配置 C（Chemistry profile C），4.4 V。

## 3.3\_BQ27421 化学特性标识符（chemistry IDs）

设备树 `chemistry-id` 属性的取值。

<a id="r_ga8f812e864a406e7ac743bedeecc9ddf3"></a>

```c
#define BQ27421_G1A_CHEM_ID 0x0128
```

相关声明：[BQ27421_G1A_CHEM_ID](#ga8f812e864a406e7ac743bedeecc9ddf3)。

BQ27421-G1A 的化学特性标识符（chemistry ID）。

<a id="r_gaf337b60f20d3c986c353293596d7c2f6"></a>

```c
#define BQ27421_G1B_CHEM_ID 0x0312
```

相关声明：[BQ27421_G1B_CHEM_ID](#gaf337b60f20d3c986c353293596d7c2f6)。

BQ27421-G1B 的化学特性标识符（chemistry ID）。

<a id="r_ga3f58b290a4556f6a74da8b4759262fc0"></a>

```c
#define BQ27421_G1D_CHEM_ID 0x3142
```

相关声明：[BQ27421_G1D_CHEM_ID](#ga3f58b290a4556f6a74da8b4759262fc0)。

BQ27421-G1D 的化学特性标识符（chemistry ID）。

## 3.4\_详细说明（Detailed Documentation）

<a id="ga8f812e864a406e7ac743bedeecc9ddf3"></a>

### `BQ27421_G1A_CHEM_ID`

```c
#define BQ27421_G1A_CHEM_ID 0x0128
```

```c
#include <zephyr/dt-bindings/sensor/bq274xx.h>
```

BQ27421-G1A 的化学特性标识符（chemistry ID）。

<a id="gaf337b60f20d3c986c353293596d7c2f6"></a>

### `BQ27421_G1B_CHEM_ID`

```c
#define BQ27421_G1B_CHEM_ID 0x0312
```

```c
#include <zephyr/dt-bindings/sensor/bq274xx.h>
```

BQ27421-G1B 的化学特性标识符（chemistry ID）。

<a id="ga3f58b290a4556f6a74da8b4759262fc0"></a>

### `BQ27421_G1D_CHEM_ID`

```c
#define BQ27421_G1D_CHEM_ID 0x3142
```

```c
#include <zephyr/dt-bindings/sensor/bq274xx.h>
```

BQ27421-G1D 的化学特性标识符（chemistry ID）。

<a id="gafd885c85ac533a7640f93e97fec8ccb9"></a>

### `BQ27427_CHEM_ID_A`

```c
#define BQ27427_CHEM_ID_A 0x3230
```

```c
#include <zephyr/dt-bindings/sensor/bq274xx.h>
```

电池化学特性配置 A（Chemistry profile A），4.35 V。

<a id="gaafd294ad5ecf988c816ed258e61fa781"></a>

### `BQ27427_CHEM_ID_B`

```c
#define BQ27427_CHEM_ID_B 0x1202
```

```c
#include <zephyr/dt-bindings/sensor/bq274xx.h>
```

电池化学特性配置 B（Chemistry profile B），4.2 V，默认配置。

<a id="gac932a2d227876901d5a001a46b0aba07"></a>

### `BQ27427_CHEM_ID_C`

```c
#define BQ27427_CHEM_ID_C 0x3142
```

```c
#include <zephyr/dt-bindings/sensor/bq274xx.h>
```

电池化学特性配置 C（Chemistry profile C），4.4 V。


## 3.5\_原页交叉引用（Cross References）

- [bq274xx.h](https://docs.zephyrproject.org/latest/doxygen/html/bq274xx_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P002_数字麦克风驱动后端 API（Digital Microphone Driver Backend API）.md) · [返回大纲](大纲.md) · [下一章](P004_即时警报服务（Immediate Alert Service，IAS）.md)
