---
id: learning.zephyr-docs.api-update-memory-topic-reference.page-13
title: PAC194X API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pac194x__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_PAC194X API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pac194x__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Microchip PAC194x 功率监测器（Power monitor）。

<a id="details"></a>

Microchip PAC194x 功率监测器（Power monitor）。

<a id="header-files"></a>
<a id="files"></a>

## 13.1\_文件（Files）

<a id="r_pac194x_2Eh"></a>

```c
file pac194x.h
```

相关声明：[pac194x.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2pac194x_8h.html)。

the Microchip PAC194x power monitor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 13.2\_满量程范围模式（Full-scale Range Mode）

设备树（Devicetree）属性 `microchip,vbus-mode` 和 `microchip,vsense-mode` 的取值。

<a id="r_ga69132e5c34fa02a6bfa36ae4bf1ecd27"></a>

```c
#define PAC_UNIPOLAR_FSR 0
```

相关声明：[PAC_UNIPOLAR_FSR](#ga69132e5c34fa02a6bfa36ae4bf1ecd27)。

单极性满量程范围（Unipolar Full-scale Range）。

<a id="r_gafdc80d9ece34bd9a2d39d649b7971ec1"></a>

```c
#define PAC_BIPOLAR_FSR 1
```

相关声明：[PAC_BIPOLAR_FSR](#gafdc80d9ece34bd9a2d39d649b7971ec1)。

双极性满量程范围（Bipolar Full-scale Range）。

<a id="r_ga4db614817516296166b2524ab78c447f"></a>

```c
#define PAC_BIPOLAR_HALF_FSR 2
```

相关声明：[PAC_BIPOLAR_HALF_FSR](#ga4db614817516296166b2524ab78c447f)。

双极性半量程范围（Bipolar Half Range），即 `FSR / 2`。

## 13.3\_累积数据源（Accumulation Source）

设备树（Devicetree）属性 `microchip,accumulation-mode` 的取值。

<a id="r_ga3090e6340cf34c043924b3a30fea4c79"></a>

```c
#define PAC_ACCUM_VPOWER 0
```

相关声明：[PAC_ACCUM_VPOWER](#ga3090e6340cf34c043924b3a30fea4c79)。

累积功率数据（Power Data）。

<a id="r_ga264aab83fe304ab142ac139a9de53396"></a>

```c
#define PAC_ACCUM_VSENSE 1
```

相关声明：[PAC_ACCUM_VSENSE](#ga264aab83fe304ab142ac139a9de53396)。

累积电流数据，即检测电压（Sense Voltage）数据。

<a id="r_ga12f7026116719fbcdb0ed959ca165025"></a>

```c
#define PAC_ACCUM_VBUS 2
```

相关声明：[PAC_ACCUM_VBUS](#ga12f7026116719fbcdb0ed959ca165025)。

累积总线电压数据（Bus Voltage Data）。

## 13.4\_刷新模式（Refresh Mode）

设备树（Devicetree）属性 `microchip,refresh-mode` 的取值。

<a id="r_ga11c894871e498d98606f96469700fd11"></a>

```c
#define PAC_REFRESH_MANUAL 0
```

相关声明：[PAC_REFRESH_MANUAL](#ga11c894871e498d98606f96469700fd11)。

手动刷新（Manual Refresh）。

<a id="r_ga06fe36ad6ef61554bd1a46d7f0fefe3b"></a>

```c
#define PAC_REFRESH_AUTO_WAIT 1
```

相关声明：[PAC_REFRESH_AUTO_WAIT](#ga06fe36ad6ef61554bd1a46d7f0fefe3b)。

自动刷新（Automatic Refresh），等待有效数据。

<a id="r_ga753b24688d14a0ccac99da1ba7abd308"></a>

```c
#define PAC_REFRESH_AUTO_NOWAIT 2
```

相关声明：[PAC_REFRESH_AUTO_NOWAIT](#ga753b24688d14a0ccac99da1ba7abd308)。

自动刷新（Automatic Refresh），不等待。

## 13.5\_详细说明（Detailed Documentation）

<a id="ga12f7026116719fbcdb0ed959ca165025"></a>

### `PAC_ACCUM_VBUS`

```c
#define PAC_ACCUM_VBUS 2
```

```c
#include <zephyr/dt-bindings/sensor/pac194x.h>
```

累积总线电压数据（Bus Voltage Data）。

<a id="ga3090e6340cf34c043924b3a30fea4c79"></a>

### `PAC_ACCUM_VPOWER`

```c
#define PAC_ACCUM_VPOWER 0
```

```c
#include <zephyr/dt-bindings/sensor/pac194x.h>
```

累积功率数据（Power Data）。

<a id="ga264aab83fe304ab142ac139a9de53396"></a>

### `PAC_ACCUM_VSENSE`

```c
#define PAC_ACCUM_VSENSE 1
```

```c
#include <zephyr/dt-bindings/sensor/pac194x.h>
```

累积电流数据，即检测电压（Sense Voltage）数据。

<a id="gafdc80d9ece34bd9a2d39d649b7971ec1"></a>

### `PAC_BIPOLAR_FSR`

```c
#define PAC_BIPOLAR_FSR 1
```

```c
#include <zephyr/dt-bindings/sensor/pac194x.h>
```

双极性满量程范围（Bipolar Full-scale Range）。

<a id="ga4db614817516296166b2524ab78c447f"></a>

### `PAC_BIPOLAR_HALF_FSR`

```c
#define PAC_BIPOLAR_HALF_FSR 2
```

```c
#include <zephyr/dt-bindings/sensor/pac194x.h>
```

双极性半量程范围（Bipolar Half Range），即 `FSR / 2`。

<a id="ga753b24688d14a0ccac99da1ba7abd308"></a>

### `PAC_REFRESH_AUTO_NOWAIT`

```c
#define PAC_REFRESH_AUTO_NOWAIT 2
```

```c
#include <zephyr/dt-bindings/sensor/pac194x.h>
```

自动刷新（Automatic Refresh），不等待。

<a id="ga06fe36ad6ef61554bd1a46d7f0fefe3b"></a>

### `PAC_REFRESH_AUTO_WAIT`

```c
#define PAC_REFRESH_AUTO_WAIT 1
```

```c
#include <zephyr/dt-bindings/sensor/pac194x.h>
```

自动刷新（Automatic Refresh），等待有效数据。

<a id="ga11c894871e498d98606f96469700fd11"></a>

### `PAC_REFRESH_MANUAL`

```c
#define PAC_REFRESH_MANUAL 0
```

```c
#include <zephyr/dt-bindings/sensor/pac194x.h>
```

手动刷新（Manual Refresh）。

<a id="ga69132e5c34fa02a6bfa36ae4bf1ecd27"></a>

### `PAC_UNIPOLAR_FSR`

```c
#define PAC_UNIPOLAR_FSR 0
```

```c
#include <zephyr/dt-bindings/sensor/pac194x.h>
```

单极性满量程范围（Unipolar Full-scale Range）。


## 13.6\_原页交叉引用（Cross References）

- [pac194x.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2pac194x_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P012_调制解调器点对点协议（Modem PPP）.md) · [返回大纲](大纲.md) · [下一章](P014_共享内存（Shared Memory）.md)
