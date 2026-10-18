---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-1
title: APDS9253 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__apds9253__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_APDS9253 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9253__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Broadcom APDS9253 RGB 与环境光传感器。

<a id="details"></a>

Broadcom APDS9253 RGB 与环境光传感器。

<a id="header-files"></a>
<a id="files"></a>

## 1.1\_文件（Files）

<a id="r_apds9253_2Eh"></a>

```c
file apds9253.h
```

相关声明：[apds9253.h](https://docs.zephyrproject.org/latest/doxygen/html/apds9253_8h.html)。

the Broadcom APDS9253 light sensor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 1.2\_ADC 分辨率与积分时间（Resolution and Integration Time）

设备树属性（Devicetree Property）`resolution` 的取值。

<a id="r_ga7ad23d39c8dc7ddf7a457e97d70f6177"></a>

```c
#define APDS9253_RESOLUTION_20BIT_400MS 0
```

相关声明：[APDS9253_RESOLUTION_20BIT_400MS](#ga7ad23d39c8dc7ddf7a457e97d70f6177)。

20 位（Bit），400 ms。

<a id="r_ga8a497ca5f4c73858ff7fef856d3a45ac"></a>

```c
#define APDS9253_RESOLUTION_19BIT_200MS BIT(4)
```

相关声明：[APDS9253_RESOLUTION_19BIT_200MS](#ga8a497ca5f4c73858ff7fef856d3a45ac)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

19 位（Bit），200 ms。

<a id="r_gaca7dd96545b1f87a258d8692934eac26"></a>

```c
#define APDS9253_RESOLUTION_18BIT_100MS BIT(5)
```

相关声明：[APDS9253_RESOLUTION_18BIT_100MS](#gaca7dd96545b1f87a258d8692934eac26)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

18 位（Bit），100 ms，默认值（Default）。

<a id="r_ga16dbc6c091d618c92446c45be558793e"></a>

```c
#define APDS9253_RESOLUTION_17BIT_50MS (BIT(5) | BIT(4))
```

相关声明：[APDS9253_RESOLUTION_17BIT_50MS](#ga16dbc6c091d618c92446c45be558793e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

17 位（Bit），50 ms。

<a id="r_ga78feda7057bc90b389dfa7107911324c"></a>

```c
#define APDS9253_RESOLUTION_16BIT_25MS BIT(6)
```

相关声明：[APDS9253_RESOLUTION_16BIT_25MS](#ga78feda7057bc90b389dfa7107911324c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

16 位（Bit），25 ms。

<a id="r_ga1a702ceafbc73c81e1fe3c8ccfc8fb9d"></a>

```c
#define APDS9253_RESOLUTION_13BIT_3MS (BIT(6) | BIT(4))
```

相关声明：[APDS9253_RESOLUTION_13BIT_3MS](#ga1a702ceafbc73c81e1fe3c8ccfc8fb9d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

13 位（Bit），3 ms。

## 1.3\_测量速率（Measurement Rate）

设备树属性（Devicetree Property）`rate` 的取值。

<a id="r_gaeb9d64852128e7186fc29f47148f8472"></a>

```c
#define APDS9253_MEASUREMENT_RATE_2000MS (BIT(2) | BIT(1) | BIT(0))
```

相关声明：[APDS9253_MEASUREMENT_RATE_2000MS](#gaeb9d64852128e7186fc29f47148f8472)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时间：2000 ms。

<a id="r_gad5bf06634bc4a286ea061e52f7b38caf"></a>

```c
#define APDS9253_MEASUREMENT_RATE_1000MS (BIT(2) | BIT(0))
```

相关声明：[APDS9253_MEASUREMENT_RATE_1000MS](#gad5bf06634bc4a286ea061e52f7b38caf)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时间：1000 ms。

<a id="r_gab028d789030caa61cc6576bc512cea51"></a>

```c
#define APDS9253_MEASUREMENT_RATE_500MS BIT(2)
```

相关声明：[APDS9253_MEASUREMENT_RATE_500MS](#gab028d789030caa61cc6576bc512cea51)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时间：500 ms。

<a id="r_ga2c7000f66a61442b67cec8123921de7a"></a>

```c
#define APDS9253_MEASUREMENT_RATE_200MS (BIT(1) | BIT(0))
```

相关声明：[APDS9253_MEASUREMENT_RATE_200MS](#ga2c7000f66a61442b67cec8123921de7a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

200 毫秒（ms）。

<a id="r_gafac03ab9dfcec1352379e8f4843bf2f3"></a>

```c
#define APDS9253_MEASUREMENT_RATE_100MS BIT(1)
```

相关声明：[APDS9253_MEASUREMENT_RATE_100MS](#gafac03ab9dfcec1352379e8f4843bf2f3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

100 毫秒（ms），默认值（Default）。

<a id="r_gaff4512ccaaebc9552566229906a74444"></a>

```c
#define APDS9253_MEASUREMENT_RATE_50MS BIT(0)
```

相关声明：[APDS9253_MEASUREMENT_RATE_50MS](#gaff4512ccaaebc9552566229906a74444)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

50 毫秒（ms）。

<a id="r_ga84fa65b7d6da23e84d9150c9aeca72b1"></a>

```c
#define APDS9253_MEASUREMENT_RATE_25MS 0
```

相关声明：[APDS9253_MEASUREMENT_RATE_25MS](#ga84fa65b7d6da23e84d9150c9aeca72b1)。

25 毫秒（ms）。

## 1.4\_增益范围（Gain Range）

设备树属性（Devicetree Property）`gain` 的取值。

<a id="r_gaa51f4c026e87de98d060f338e7cb020d"></a>

```c
#define APDS9253_GAIN_RANGE_18 BIT(2)
```

相关声明：[APDS9253_GAIN_RANGE_18](#gaa51f4c026e87de98d060f338e7cb020d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

18 倍增益（Gain）。

<a id="r_ga48961f6b63d915eb96ea13b235ca14fa"></a>

```c
#define APDS9253_GAIN_RANGE_9 (BIT(1) | BIT(0))
```

相关声明：[APDS9253_GAIN_RANGE_9](#ga48961f6b63d915eb96ea13b235ca14fa)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

9 倍增益（Gain）。

<a id="r_gadf8d5b7fa484322cb25026a851346a60"></a>

```c
#define APDS9253_GAIN_RANGE_6 BIT(1)
```

相关声明：[APDS9253_GAIN_RANGE_6](#gadf8d5b7fa484322cb25026a851346a60)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

6 倍增益（Gain）。

<a id="r_ga0ae5f62dc95dd84d8310e08bec8902a0"></a>

```c
#define APDS9253_GAIN_RANGE_3 BIT(0)
```

相关声明：[APDS9253_GAIN_RANGE_3](#ga0ae5f62dc95dd84d8310e08bec8902a0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

3 倍增益（Gain），默认值（Default）。

<a id="r_gaefdb9ab4f906ef0ed294f1d20bd52dc2"></a>

```c
#define APDS9253_GAIN_RANGE_1 0
```

相关声明：[APDS9253_GAIN_RANGE_1](#gaefdb9ab4f906ef0ed294f1d20bd52dc2)。

1 倍增益（Gain）。

## 1.5\_详细说明（Detailed Documentation）

<a id="gaefdb9ab4f906ef0ed294f1d20bd52dc2"></a>

### `APDS9253_GAIN_RANGE_1`

```c
#define APDS9253_GAIN_RANGE_1 0
```

```c
#include <zephyr/dt-bindings/sensor/apds9253.h>
```

1 倍增益（Gain）。

<a id="gaa51f4c026e87de98d060f338e7cb020d"></a>

### `APDS9253_GAIN_RANGE_18`

```c
#define APDS9253_GAIN_RANGE_18 BIT(2)
```

```c
#include <zephyr/dt-bindings/sensor/apds9253.h>
```

18 倍增益（Gain）。

<a id="ga0ae5f62dc95dd84d8310e08bec8902a0"></a>

### `APDS9253_GAIN_RANGE_3`

```c
#define APDS9253_GAIN_RANGE_3 BIT(0)
```

```c
#include <zephyr/dt-bindings/sensor/apds9253.h>
```

3 倍增益（Gain），默认值（Default）。

<a id="gadf8d5b7fa484322cb25026a851346a60"></a>

### `APDS9253_GAIN_RANGE_6`

```c
#define APDS9253_GAIN_RANGE_6 BIT(1)
```

```c
#include <zephyr/dt-bindings/sensor/apds9253.h>
```

6 倍增益（Gain）。

<a id="ga48961f6b63d915eb96ea13b235ca14fa"></a>

### `APDS9253_GAIN_RANGE_9`

```c
#define APDS9253_GAIN_RANGE_9 (BIT(1) | BIT(0))
```

```c
#include <zephyr/dt-bindings/sensor/apds9253.h>
```

9 倍增益（Gain）。

<a id="gad5bf06634bc4a286ea061e52f7b38caf"></a>

### `APDS9253_MEASUREMENT_RATE_1000MS`

```c
#define APDS9253_MEASUREMENT_RATE_1000MS (BIT(2) | BIT(0))
```

```c
#include <zephyr/dt-bindings/sensor/apds9253.h>
```

时间：1000 ms。

<a id="gafac03ab9dfcec1352379e8f4843bf2f3"></a>

### `APDS9253_MEASUREMENT_RATE_100MS`

```c
#define APDS9253_MEASUREMENT_RATE_100MS BIT(1)
```

```c
#include <zephyr/dt-bindings/sensor/apds9253.h>
```

100 毫秒（ms），默认值（Default）。

<a id="gaeb9d64852128e7186fc29f47148f8472"></a>

### `APDS9253_MEASUREMENT_RATE_2000MS`

```c
#define APDS9253_MEASUREMENT_RATE_2000MS (BIT(2) | BIT(1) | BIT(0))
```

```c
#include <zephyr/dt-bindings/sensor/apds9253.h>
```

时间：2000 ms。

<a id="ga2c7000f66a61442b67cec8123921de7a"></a>

### `APDS9253_MEASUREMENT_RATE_200MS`

```c
#define APDS9253_MEASUREMENT_RATE_200MS (BIT(1) | BIT(0))
```

```c
#include <zephyr/dt-bindings/sensor/apds9253.h>
```

200 毫秒（ms）。

<a id="ga84fa65b7d6da23e84d9150c9aeca72b1"></a>

### `APDS9253_MEASUREMENT_RATE_25MS`

```c
#define APDS9253_MEASUREMENT_RATE_25MS 0
```

```c
#include <zephyr/dt-bindings/sensor/apds9253.h>
```

25 毫秒（ms）。

<a id="gab028d789030caa61cc6576bc512cea51"></a>

### `APDS9253_MEASUREMENT_RATE_500MS`

```c
#define APDS9253_MEASUREMENT_RATE_500MS BIT(2)
```

```c
#include <zephyr/dt-bindings/sensor/apds9253.h>
```

时间：500 ms。

<a id="gaff4512ccaaebc9552566229906a74444"></a>

### `APDS9253_MEASUREMENT_RATE_50MS`

```c
#define APDS9253_MEASUREMENT_RATE_50MS BIT(0)
```

```c
#include <zephyr/dt-bindings/sensor/apds9253.h>
```

50 毫秒（ms）。

<a id="ga1a702ceafbc73c81e1fe3c8ccfc8fb9d"></a>

### `APDS9253_RESOLUTION_13BIT_3MS`

```c
#define APDS9253_RESOLUTION_13BIT_3MS (BIT(6) | BIT(4))
```

```c
#include <zephyr/dt-bindings/sensor/apds9253.h>
```

13 位（Bit），3 ms。

<a id="ga78feda7057bc90b389dfa7107911324c"></a>

### `APDS9253_RESOLUTION_16BIT_25MS`

```c
#define APDS9253_RESOLUTION_16BIT_25MS BIT(6)
```

```c
#include <zephyr/dt-bindings/sensor/apds9253.h>
```

16 位（Bit），25 ms。

<a id="ga16dbc6c091d618c92446c45be558793e"></a>

### `APDS9253_RESOLUTION_17BIT_50MS`

```c
#define APDS9253_RESOLUTION_17BIT_50MS (BIT(5) | BIT(4))
```

```c
#include <zephyr/dt-bindings/sensor/apds9253.h>
```

17 位（Bit），50 ms。

<a id="gaca7dd96545b1f87a258d8692934eac26"></a>

### `APDS9253_RESOLUTION_18BIT_100MS`

```c
#define APDS9253_RESOLUTION_18BIT_100MS BIT(5)
```

```c
#include <zephyr/dt-bindings/sensor/apds9253.h>
```

18 位（Bit），100 ms，默认值（Default）。

<a id="ga8a497ca5f4c73858ff7fef856d3a45ac"></a>

### `APDS9253_RESOLUTION_19BIT_200MS`

```c
#define APDS9253_RESOLUTION_19BIT_200MS BIT(4)
```

```c
#include <zephyr/dt-bindings/sensor/apds9253.h>
```

19 位（Bit），200 ms。

<a id="ga7ad23d39c8dc7ddf7a457e97d70f6177"></a>

### `APDS9253_RESOLUTION_20BIT_400MS`

```c
#define APDS9253_RESOLUTION_20BIT_400MS 0
```

```c
#include <zephyr/dt-bindings/sensor/apds9253.h>
```

20 位（Bit），400 ms。


## 1.6\_原页交叉引用（Cross References）

- [apds9253.h](https://docs.zephyrproject.org/latest/doxygen/html/apds9253_8h.html)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_公共广播配置文件（Public Broadcast Profile，PBP）.md)
