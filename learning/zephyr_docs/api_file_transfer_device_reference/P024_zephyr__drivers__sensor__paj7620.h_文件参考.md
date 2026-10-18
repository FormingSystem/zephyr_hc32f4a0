---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-24
title: zephyr__drivers__sensor__paj7620.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/paj7620_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_zephyr\_\_drivers\_\_sensor\_\_paj7620.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/paj7620_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PAJ7620传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

PAJ7620传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 24.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 手势标志（Gesture Flags）

<a id="r_gaa63753ca7c5f4bc1f478fc72fa3c320f"></a>

```c
#define PAJ7620_FLAG_GES_UP BIT(0)
```

相关声明：[PAJ7620_FLAG_GES_UP](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#gaa63753ca7c5f4bc1f478fc72fa3c320f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

“向上”（Up）手势。

<a id="r_ga492ae48e3a532d921422c1e9a7ef7e2e"></a>

```c
#define PAJ7620_FLAG_GES_DOWN BIT(1)
```

相关声明：[PAJ7620_FLAG_GES_DOWN](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#ga492ae48e3a532d921422c1e9a7ef7e2e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

“向下”（Down）手势。

<a id="r_gae61616e99b14af9949eb65d7aa09187e"></a>

```c
#define PAJ7620_FLAG_GES_LEFT BIT(2)
```

相关声明：[PAJ7620_FLAG_GES_LEFT](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#gae61616e99b14af9949eb65d7aa09187e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

“向左”（Left）手势。

<a id="r_ga99ad889dfebad0ae277f5bea821a5551"></a>

```c
#define PAJ7620_FLAG_GES_RIGHT BIT(3)
```

相关声明：[PAJ7620_FLAG_GES_RIGHT](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#ga99ad889dfebad0ae277f5bea821a5551)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

“向右”（Right）手势。

<a id="r_gaeb6cd5bb1f28cae139daf6cddf344d00"></a>

```c
#define PAJ7620_FLAG_GES_FORWARD BIT(4)
```

相关声明：[PAJ7620_FLAG_GES_FORWARD](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#gaeb6cd5bb1f28cae139daf6cddf344d00)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

“向前”（Forward）手势。

<a id="r_ga564c0b02bb0b4606e6b58bb030ac765f"></a>

```c
#define PAJ7620_FLAG_GES_BACKWARD BIT(5)
```

相关声明：[PAJ7620_FLAG_GES_BACKWARD](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#ga564c0b02bb0b4606e6b58bb030ac765f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

“向后”（Backward）手势。

<a id="r_ga80db26a635c1af0ea0cbf79b841c37af"></a>

```c
#define PAJ7620_FLAG_GES_CLOCKWISE BIT(6)
```

相关声明：[PAJ7620_FLAG_GES_CLOCKWISE](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#ga80db26a635c1af0ea0cbf79b841c37af)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

“顺时针”（Clockwise）手势。

<a id="r_gaa992028736388f241425c9d210f43213"></a>

```c
#define PAJ7620_FLAG_GES_COUNTERCLOCKWISE BIT(7)
```

相关声明：[PAJ7620_FLAG_GES_COUNTERCLOCKWISE](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#gaa992028736388f241425c9d210f43213)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

“逆时针”（Counterclockwise）手势。

<a id="r_ga17c3e6864957600d440263f5861b8598"></a>

```c
#define PAJ7620_FLAG_GES_WAVE BIT(8)
```

相关声明：[PAJ7620_FLAG_GES_WAVE](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#ga17c3e6864957600d440263f5861b8598)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

“挥手”（Wave）手势。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 24.2\_枚举（Enumerations）

<a id="r_gaee838947e01367f4a31b54798ca8231b"></a>

```c
enum sensor_channel_paj7620 { SENSOR_CHAN_PAJ7620_GESTURES = SENSOR_CHAN_PRIV_START }
```

相关声明：[sensor_channel_paj7620](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#gaee838947e01367f4a31b54798ca8231b)、[SENSOR_CHAN_PAJ7620_GESTURES](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#ggaee838947e01367f4a31b54798ca8231ba6d3555eeca40737b0cc96e731d9374d2)。

PAJ7620 自定义传感器通道（Custom Sensor Channels）。


## 24.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P140_paj7620.h_源码浏览.md)
- [PAJ7620_FLAG_GES_UP](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#gaa63753ca7c5f4bc1f478fc72fa3c320f)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [PAJ7620_FLAG_GES_DOWN](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#ga492ae48e3a532d921422c1e9a7ef7e2e)
- [PAJ7620_FLAG_GES_LEFT](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#gae61616e99b14af9949eb65d7aa09187e)
- [PAJ7620_FLAG_GES_RIGHT](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#ga99ad889dfebad0ae277f5bea821a5551)
- [PAJ7620_FLAG_GES_FORWARD](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#gaeb6cd5bb1f28cae139daf6cddf344d00)
- [PAJ7620_FLAG_GES_BACKWARD](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#ga564c0b02bb0b4606e6b58bb030ac765f)
- [PAJ7620_FLAG_GES_CLOCKWISE](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#ga80db26a635c1af0ea0cbf79b841c37af)
- [PAJ7620_FLAG_GES_COUNTERCLOCKWISE](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#gaa992028736388f241425c9d210f43213)
- [PAJ7620_FLAG_GES_WAVE](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#ga17c3e6864957600d440263f5861b8598)
- [sensor_channel_paj7620](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#gaee838947e01367f4a31b54798ca8231b)
- [SENSOR_CHAN_PAJ7620_GESTURES](../api_security_memory_topic_reference/P010_PAJ7620 API主题.md#ggaee838947e01367f4a31b54798ca8231ba6d3555eeca40737b0cc96e731d9374d2)

<a id="header-details"></a>

---

[上一章](P023_zephyr__net__lwm2m_send_scheduler.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P025_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rza-common.h_文件参考.md)
