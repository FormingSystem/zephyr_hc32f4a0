---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-1
title: zephyr__dt-bindings__sensor__apds9253.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/apds9253_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_dt-bindings\_\_sensor\_\_apds9253.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/apds9253_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the Broadcom APDS9253 light sensor的设备树绑定常量（Devicetree Binding Constants）。

<a id="details"></a>

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

the Broadcom APDS9253 light sensor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="define-members-0"></a>

### ADC 分辨率与积分时间（Resolution and Integration Time）

设备树属性（Devicetree Property）`resolution` 的取值。

<a id="r_ga7ad23d39c8dc7ddf7a457e97d70f6177"></a>

```c
#define APDS9253_RESOLUTION_20BIT_400MS 0
```

相关声明：[APDS9253_RESOLUTION_20BIT_400MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#ga7ad23d39c8dc7ddf7a457e97d70f6177)。

20 位（Bit），400 ms。

<a id="r_ga8a497ca5f4c73858ff7fef856d3a45ac"></a>

```c
#define APDS9253_RESOLUTION_19BIT_200MS BIT(4)
```

相关声明：[APDS9253_RESOLUTION_19BIT_200MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#ga8a497ca5f4c73858ff7fef856d3a45ac)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

19 位（Bit），200 ms。

<a id="r_gaca7dd96545b1f87a258d8692934eac26"></a>

```c
#define APDS9253_RESOLUTION_18BIT_100MS BIT(5)
```

相关声明：[APDS9253_RESOLUTION_18BIT_100MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#gaca7dd96545b1f87a258d8692934eac26)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

18 位（Bit），100 ms，默认值（Default）。

<a id="r_ga16dbc6c091d618c92446c45be558793e"></a>

```c
#define APDS9253_RESOLUTION_17BIT_50MS (BIT(5) | BIT(4))
```

相关声明：[APDS9253_RESOLUTION_17BIT_50MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#ga16dbc6c091d618c92446c45be558793e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

17 位（Bit），50 ms。

<a id="r_ga78feda7057bc90b389dfa7107911324c"></a>

```c
#define APDS9253_RESOLUTION_16BIT_25MS BIT(6)
```

相关声明：[APDS9253_RESOLUTION_16BIT_25MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#ga78feda7057bc90b389dfa7107911324c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

16 位（Bit），25 ms。

<a id="r_ga1a702ceafbc73c81e1fe3c8ccfc8fb9d"></a>

```c
#define APDS9253_RESOLUTION_13BIT_3MS (BIT(6) | BIT(4))
```

相关声明：[APDS9253_RESOLUTION_13BIT_3MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#ga1a702ceafbc73c81e1fe3c8ccfc8fb9d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

13 位（Bit），3 ms。

<a id="define-members-1"></a>

### 测量速率（Measurement Rate）

设备树属性（Devicetree Property）`rate` 的取值。

<a id="r_gaeb9d64852128e7186fc29f47148f8472"></a>

```c
#define APDS9253_MEASUREMENT_RATE_2000MS (BIT(2) | BIT(1) | BIT(0))
```

相关声明：[APDS9253_MEASUREMENT_RATE_2000MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#gaeb9d64852128e7186fc29f47148f8472)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时间：2000 ms。

<a id="r_gad5bf06634bc4a286ea061e52f7b38caf"></a>

```c
#define APDS9253_MEASUREMENT_RATE_1000MS (BIT(2) | BIT(0))
```

相关声明：[APDS9253_MEASUREMENT_RATE_1000MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#gad5bf06634bc4a286ea061e52f7b38caf)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时间：1000 ms。

<a id="r_gab028d789030caa61cc6576bc512cea51"></a>

```c
#define APDS9253_MEASUREMENT_RATE_500MS BIT(2)
```

相关声明：[APDS9253_MEASUREMENT_RATE_500MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#gab028d789030caa61cc6576bc512cea51)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时间：500 ms。

<a id="r_ga2c7000f66a61442b67cec8123921de7a"></a>

```c
#define APDS9253_MEASUREMENT_RATE_200MS (BIT(1) | BIT(0))
```

相关声明：[APDS9253_MEASUREMENT_RATE_200MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#ga2c7000f66a61442b67cec8123921de7a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

200 毫秒（ms）。

<a id="r_gafac03ab9dfcec1352379e8f4843bf2f3"></a>

```c
#define APDS9253_MEASUREMENT_RATE_100MS BIT(1)
```

相关声明：[APDS9253_MEASUREMENT_RATE_100MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#gafac03ab9dfcec1352379e8f4843bf2f3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

100 毫秒（ms），默认值（Default）。

<a id="r_gaff4512ccaaebc9552566229906a74444"></a>

```c
#define APDS9253_MEASUREMENT_RATE_50MS BIT(0)
```

相关声明：[APDS9253_MEASUREMENT_RATE_50MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#gaff4512ccaaebc9552566229906a74444)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

50 毫秒（ms）。

<a id="r_ga84fa65b7d6da23e84d9150c9aeca72b1"></a>

```c
#define APDS9253_MEASUREMENT_RATE_25MS 0
```

相关声明：[APDS9253_MEASUREMENT_RATE_25MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#ga84fa65b7d6da23e84d9150c9aeca72b1)。

25 毫秒（ms）。

<a id="define-members-2"></a>

### 增益范围（Gain Range）

设备树属性（Devicetree Property）`gain` 的取值。

<a id="r_gaa51f4c026e87de98d060f338e7cb020d"></a>

```c
#define APDS9253_GAIN_RANGE_18 BIT(2)
```

相关声明：[APDS9253_GAIN_RANGE_18](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#gaa51f4c026e87de98d060f338e7cb020d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

18 倍增益（Gain）。

<a id="r_ga48961f6b63d915eb96ea13b235ca14fa"></a>

```c
#define APDS9253_GAIN_RANGE_9 (BIT(1) | BIT(0))
```

相关声明：[APDS9253_GAIN_RANGE_9](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#ga48961f6b63d915eb96ea13b235ca14fa)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

9 倍增益（Gain）。

<a id="r_gadf8d5b7fa484322cb25026a851346a60"></a>

```c
#define APDS9253_GAIN_RANGE_6 BIT(1)
```

相关声明：[APDS9253_GAIN_RANGE_6](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#gadf8d5b7fa484322cb25026a851346a60)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

6 倍增益（Gain）。

<a id="r_ga0ae5f62dc95dd84d8310e08bec8902a0"></a>

```c
#define APDS9253_GAIN_RANGE_3 BIT(0)
```

相关声明：[APDS9253_GAIN_RANGE_3](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#ga0ae5f62dc95dd84d8310e08bec8902a0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

3 倍增益（Gain），默认值（Default）。

<a id="r_gaefdb9ab4f906ef0ed294f1d20bd52dc2"></a>

```c
#define APDS9253_GAIN_RANGE_1 0
```

相关声明：[APDS9253_GAIN_RANGE_1](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#gaefdb9ab4f906ef0ed294f1d20bd52dc2)。

1 倍增益（Gain）。


## 1.2\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P032_apds9253.h_源码浏览.md)
- [APDS9253_RESOLUTION_20BIT_400MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#ga7ad23d39c8dc7ddf7a457e97d70f6177)
- [APDS9253_RESOLUTION_19BIT_200MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#ga8a497ca5f4c73858ff7fef856d3a45ac)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [APDS9253_RESOLUTION_18BIT_100MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#gaca7dd96545b1f87a258d8692934eac26)
- [APDS9253_RESOLUTION_17BIT_50MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#ga16dbc6c091d618c92446c45be558793e)
- [APDS9253_RESOLUTION_16BIT_25MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#ga78feda7057bc90b389dfa7107911324c)
- [APDS9253_RESOLUTION_13BIT_3MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#ga1a702ceafbc73c81e1fe3c8ccfc8fb9d)
- [APDS9253_MEASUREMENT_RATE_2000MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#gaeb9d64852128e7186fc29f47148f8472)
- [APDS9253_MEASUREMENT_RATE_1000MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#gad5bf06634bc4a286ea061e52f7b38caf)
- [APDS9253_MEASUREMENT_RATE_500MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#gab028d789030caa61cc6576bc512cea51)
- [APDS9253_MEASUREMENT_RATE_200MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#ga2c7000f66a61442b67cec8123921de7a)
- [APDS9253_MEASUREMENT_RATE_100MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#gafac03ab9dfcec1352379e8f4843bf2f3)
- [APDS9253_MEASUREMENT_RATE_50MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#gaff4512ccaaebc9552566229906a74444)
- [APDS9253_MEASUREMENT_RATE_25MS](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#ga84fa65b7d6da23e84d9150c9aeca72b1)
- [APDS9253_GAIN_RANGE_18](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#gaa51f4c026e87de98d060f338e7cb020d)
- [APDS9253_GAIN_RANGE_9](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#ga48961f6b63d915eb96ea13b235ca14fa)
- [APDS9253_GAIN_RANGE_6](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#gadf8d5b7fa484322cb25026a851346a60)
- [APDS9253_GAIN_RANGE_3](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#ga0ae5f62dc95dd84d8310e08bec8902a0)
- [APDS9253_GAIN_RANGE_1](../api_lifecycle_capability_topic_reference/P001_APDS9253 API主题.md#gaefdb9ab4f906ef0ed294f1d20bd52dc2)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__dt-bindings__clock__bflb_bl60x_clock.h_文件参考.md)
