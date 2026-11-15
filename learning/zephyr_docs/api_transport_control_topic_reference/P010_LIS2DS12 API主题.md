---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-10
title: LIS2DS12 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lis2ds12__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_LIS2DS12 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2ds12__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics LIS2DS12 三轴加速度计（3-axis accelerometer）。

<a id="details"></a>

STMicroelectronics LIS2DS12 三轴加速度计（3-axis accelerometer）。

<a id="header-files"></a>
<a id="files"></a>

## 10.1\_文件（Files）

<a id="r_lis2ds12_2Eh"></a>

```c
file lis2ds12.h
```

相关声明：[lis2ds12.h](https://docs.zephyrproject.org/latest/doxygen/html/lis2ds12_8h.html)。

the ST LIS2DS12 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 10.2\_电源模式（Power Modes）

设备树属性（Devicetree Property）`power-mode` 的取值。

<a id="r_gaebfdbefbdc2f17440413ba44911e8f3c"></a>

```c
#define LIS2DS12_DT_POWER_DOWN 0
```

相关声明：[LIS2DS12_DT_POWER_DOWN](#gaebfdbefbdc2f17440413ba44911e8f3c)。

掉电（Power-down）。

<a id="r_ga93264cc6b09ef363a51a77d81e365083"></a>

```c
#define LIS2DS12_DT_LOW_POWER 1
```

相关声明：[LIS2DS12_DT_LOW_POWER](#ga93264cc6b09ef363a51a77d81e365083)。

低功耗模式（Low-power Mode）。

<a id="r_gaa94a782ff303956dbbc99dbcf59819f8"></a>

```c
#define LIS2DS12_DT_HIGH_RESOLUTION 2
```

相关声明：[LIS2DS12_DT_HIGH_RESOLUTION](#gaa94a782ff303956dbbc99dbcf59819f8)。

高分辨率模式（High-resolution Mode）。

<a id="r_gac66a29d7065bb2b94b471f704cd6ca58"></a>

```c
#define LIS2DS12_DT_HIGH_FREQUENCY 3
```

相关声明：[LIS2DS12_DT_HIGH_FREQUENCY](#gac66a29d7065bb2b94b471f704cd6ca58)。

高频模式（High-frequency Mode）。

## 10.3\_输出数据率选项（Output data rate options）

设备树 `odr` 属性的取值。

LP：低功耗（Low-power）；HR：高分辨率（High-resolution）；HF：高频模式（High-frequency Mode）。

<a id="r_ga18ee240515cce324ee31ff7d8201a933"></a>

```c
#define LIS2DS12_DT_ODR_OFF 0
```

相关声明：[LIS2DS12_DT_ODR_OFF](#ga18ee240515cce324ee31ff7d8201a933)。

掉电（Power-down）。

<a id="r_gab222c78221c0a9d4ab1ce502c09103a5"></a>

```c
#define LIS2DS12_DT_ODR_1Hz_LP 1
```

相关声明：[LIS2DS12_DT_ODR_1Hz_LP](#gab222c78221c0a9d4ab1ce502c09103a5)。

1 Hz（仅适用于低功耗（LP）模式）。

<a id="r_ga304edbdda283cb5274988054c969ca43"></a>

```c
#define LIS2DS12_DT_ODR_12Hz5 2
```

相关声明：[LIS2DS12_DT_ODR_12Hz5](#ga304edbdda283cb5274988054c969ca43)。

12.5 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="r_gad37986618e794a9f7d59f521972ebc3b"></a>

```c
#define LIS2DS12_DT_ODR_25Hz 3
```

相关声明：[LIS2DS12_DT_ODR_25Hz](#gad37986618e794a9f7d59f521972ebc3b)。

25 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="r_ga428a9dea9f3bbd9e60ad533cdae334f8"></a>

```c
#define LIS2DS12_DT_ODR_50Hz 4
```

相关声明：[LIS2DS12_DT_ODR_50Hz](#ga428a9dea9f3bbd9e60ad533cdae334f8)。

50 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="r_ga07c6d9c6b044b749eed4db77d899d5ce"></a>

```c
#define LIS2DS12_DT_ODR_100Hz 5
```

相关声明：[LIS2DS12_DT_ODR_100Hz](#ga07c6d9c6b044b749eed4db77d899d5ce)。

100 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="r_gafc77b3b419461fa4744a83643ece77d4"></a>

```c
#define LIS2DS12_DT_ODR_200Hz 6
```

相关声明：[LIS2DS12_DT_ODR_200Hz](#gafc77b3b419461fa4744a83643ece77d4)。

200 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="r_ga97749570c84f44060280b17b1b42b19b"></a>

```c
#define LIS2DS12_DT_ODR_400Hz 7
```

相关声明：[LIS2DS12_DT_ODR_400Hz](#ga97749570c84f44060280b17b1b42b19b)。

400 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="r_gab7d0fb3bc0c15b714bda52d6e3435afc"></a>

```c
#define LIS2DS12_DT_ODR_800Hz 8
```

相关声明：[LIS2DS12_DT_ODR_800Hz](#gab7d0fb3bc0c15b714bda52d6e3435afc)。

800 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="r_ga11f5aede52debdbc639791b28777504a"></a>

```c
#define LIS2DS12_DT_ODR_1600Hz 9
```

相关声明：[LIS2DS12_DT_ODR_1600Hz](#ga11f5aede52debdbc639791b28777504a)。

1600 Hz（仅适用于高频（HF）模式）。

<a id="r_ga191a8680a6dff5ed459fbfd24aa04c2f"></a>

```c
#define LIS2DS12_DT_ODR_3200Hz_HF 10
```

相关声明：[LIS2DS12_DT_ODR_3200Hz_HF](#ga191a8680a6dff5ed459fbfd24aa04c2f)。

3200 Hz（仅适用于高频（HF）模式）。

<a id="r_ga3e06d2a0811d0aa1544e77eb5ee6a4a9"></a>

```c
#define LIS2DS12_DT_ODR_6400Hz_HF 11
```

相关声明：[LIS2DS12_DT_ODR_6400Hz_HF](#ga3e06d2a0811d0aa1544e77eb5ee6a4a9)。

6400 Hz（仅适用于高频（HF）模式）。

## 10.4\_详细说明（Detailed Documentation）

<a id="gac66a29d7065bb2b94b471f704cd6ca58"></a>

### `LIS2DS12_DT_HIGH_FREQUENCY`

```c
#define LIS2DS12_DT_HIGH_FREQUENCY 3
```

```c
#include <zephyr/dt-bindings/sensor/lis2ds12.h>
```

高频模式（High-frequency Mode）。

<a id="gaa94a782ff303956dbbc99dbcf59819f8"></a>

### `LIS2DS12_DT_HIGH_RESOLUTION`

```c
#define LIS2DS12_DT_HIGH_RESOLUTION 2
```

```c
#include <zephyr/dt-bindings/sensor/lis2ds12.h>
```

高分辨率模式（High-resolution Mode）。

<a id="ga93264cc6b09ef363a51a77d81e365083"></a>

### `LIS2DS12_DT_LOW_POWER`

```c
#define LIS2DS12_DT_LOW_POWER 1
```

```c
#include <zephyr/dt-bindings/sensor/lis2ds12.h>
```

低功耗模式（Low-power Mode）。

<a id="ga07c6d9c6b044b749eed4db77d899d5ce"></a>

### `LIS2DS12_DT_ODR_100Hz`

```c
#define LIS2DS12_DT_ODR_100Hz 5
```

```c
#include <zephyr/dt-bindings/sensor/lis2ds12.h>
```

100 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="ga304edbdda283cb5274988054c969ca43"></a>

### `LIS2DS12_DT_ODR_12Hz5`

```c
#define LIS2DS12_DT_ODR_12Hz5 2
```

```c
#include <zephyr/dt-bindings/sensor/lis2ds12.h>
```

12.5 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="ga11f5aede52debdbc639791b28777504a"></a>

### `LIS2DS12_DT_ODR_1600Hz`

```c
#define LIS2DS12_DT_ODR_1600Hz 9
```

```c
#include <zephyr/dt-bindings/sensor/lis2ds12.h>
```

1600 Hz（仅适用于高频（HF）模式）。

<a id="gab222c78221c0a9d4ab1ce502c09103a5"></a>

### `LIS2DS12_DT_ODR_1Hz_LP`

```c
#define LIS2DS12_DT_ODR_1Hz_LP 1
```

```c
#include <zephyr/dt-bindings/sensor/lis2ds12.h>
```

1 Hz（仅适用于低功耗（LP）模式）。

<a id="gafc77b3b419461fa4744a83643ece77d4"></a>

### `LIS2DS12_DT_ODR_200Hz`

```c
#define LIS2DS12_DT_ODR_200Hz 6
```

```c
#include <zephyr/dt-bindings/sensor/lis2ds12.h>
```

200 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="gad37986618e794a9f7d59f521972ebc3b"></a>

### `LIS2DS12_DT_ODR_25Hz`

```c
#define LIS2DS12_DT_ODR_25Hz 3
```

```c
#include <zephyr/dt-bindings/sensor/lis2ds12.h>
```

25 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="ga191a8680a6dff5ed459fbfd24aa04c2f"></a>

### `LIS2DS12_DT_ODR_3200Hz_HF`

```c
#define LIS2DS12_DT_ODR_3200Hz_HF 10
```

```c
#include <zephyr/dt-bindings/sensor/lis2ds12.h>
```

3200 Hz（仅适用于高频（HF）模式）。

<a id="ga97749570c84f44060280b17b1b42b19b"></a>

### `LIS2DS12_DT_ODR_400Hz`

```c
#define LIS2DS12_DT_ODR_400Hz 7
```

```c
#include <zephyr/dt-bindings/sensor/lis2ds12.h>
```

400 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="ga428a9dea9f3bbd9e60ad533cdae334f8"></a>

### `LIS2DS12_DT_ODR_50Hz`

```c
#define LIS2DS12_DT_ODR_50Hz 4
```

```c
#include <zephyr/dt-bindings/sensor/lis2ds12.h>
```

50 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="ga3e06d2a0811d0aa1544e77eb5ee6a4a9"></a>

### `LIS2DS12_DT_ODR_6400Hz_HF`

```c
#define LIS2DS12_DT_ODR_6400Hz_HF 11
```

```c
#include <zephyr/dt-bindings/sensor/lis2ds12.h>
```

6400 Hz（仅适用于高频（HF）模式）。

<a id="gab7d0fb3bc0c15b714bda52d6e3435afc"></a>

### `LIS2DS12_DT_ODR_800Hz`

```c
#define LIS2DS12_DT_ODR_800Hz 8
```

```c
#include <zephyr/dt-bindings/sensor/lis2ds12.h>
```

800 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="ga18ee240515cce324ee31ff7d8201a933"></a>

### `LIS2DS12_DT_ODR_OFF`

```c
#define LIS2DS12_DT_ODR_OFF 0
```

```c
#include <zephyr/dt-bindings/sensor/lis2ds12.h>
```

掉电（Power-down）。

<a id="gaebfdbefbdc2f17440413ba44911e8f3c"></a>

### `LIS2DS12_DT_POWER_DOWN`

```c
#define LIS2DS12_DT_POWER_DOWN 0
```

```c
#include <zephyr/dt-bindings/sensor/lis2ds12.h>
```

掉电（Power-down）。


## 10.5\_原页交叉引用（Cross References）

- [lis2ds12.h](https://docs.zephyrproject.org/latest/doxygen/html/lis2ds12_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P009_IPv4 套接字选项（Socket options）.md) · [返回大纲](大纲.md) · [下一章](P011_串行传输（Serial transport）.md)
