---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-25
title: VEML60XX API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_VEML60XX API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__veml60xx__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Vishay VEML60xx 传感器系列的公共属性。

<a id="details"></a>

Vishay VEML60xx 传感器系列的公共属性。

<a id="header-files"></a>
<a id="files"></a>

## 25.1\_文件（Files）

<a id="r_veml60xx-common_2Eh"></a>

```c
file veml60xx-common.h
```

相关声明：[veml60xx-common.h](../api_file_runtime_reference/P074_zephyr__drivers__sensor__veml60xx-common.h_文件参考.md)。

VEML60xx传感器系列的扩展API头文件（Extended Sensor API Header）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 25.2\_数据结构（Data Structures）

<a id="r_veml60xx_5Fit_5Fdata"></a>

```c
struct veml60xx_it_data
```

相关声明：[veml60xx_it_data](../sensor_navigation_model_reference/P073_veml60xx_it_data_结构体.md)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 25.3\_枚举（Enumerations）

<a id="r_ga8945da51940f67ee875a729d6de4d287"></a>

```c
enum veml60xx_it { VEML60XX_IT_3_125 , VEML60XX_IT_6_25 , VEML60XX_IT_12_5 , VEML60XX_IT_25 , VEML60XX_IT_50 , VEML60XX_IT_100 , VEML60XX_IT_200 , VEML60XX_IT_400 }
```

相关声明：[veml60xx_it](#ga8945da51940f67ee875a729d6de4d287)、[VEML60XX_IT_3_125](#gga8945da51940f67ee875a729d6de4d287ac7a765f90c553870f710ae8897c92965)、[VEML60XX_IT_6_25](#gga8945da51940f67ee875a729d6de4d287aa18934d815766e1d45ddbaca63856888)、[VEML60XX_IT_12_5](#gga8945da51940f67ee875a729d6de4d287a62b1fdbf8ba56ec030d84adeb2c7e7fa)、[VEML60XX_IT_25](#gga8945da51940f67ee875a729d6de4d287a6afc3f891825df56cd9b5c5da73b2144)、[VEML60XX_IT_50](#gga8945da51940f67ee875a729d6de4d287a3176b08da4de3a380d9a5d5fe90ccd77)、[VEML60XX_IT_100](#gga8945da51940f67ee875a729d6de4d287a8ee263a50188580a4c8911b3985af636)、[VEML60XX_IT_200](#gga8945da51940f67ee875a729d6de4d287ae6dcaf0b5b132be10a2b049c713c0e0b)、[VEML60XX_IT_400](#gga8945da51940f67ee875a729d6de4d287adf8374ac010d4be484d680649ee15e93)。

VEML60xx 环境光测量（Ambient Light Measurements）的积分时间选项（Integration Time Options）。

<a id="r_gacf7907b21bea0f35196db039a709aae2"></a>

```c
enum veml60xx_gain { VEML60XX_GAIN_1 = 0x00 , VEML60XX_GAIN_2 = 0x01 , VEML60XX_GAIN_0_66 = 0x02 , VEML60XX_GAIN_0_5 = 0x03 }
```

相关声明：[veml60xx_gain](#gacf7907b21bea0f35196db039a709aae2)、[VEML60XX_GAIN_1](#ggacf7907b21bea0f35196db039a709aae2ac5283d652e5c1f8b90cd5cd61f7d1a2b)、[VEML60XX_GAIN_2](#ggacf7907b21bea0f35196db039a709aae2a9629a32182ea0b1d30ab6b617de8c1f5)、[VEML60XX_GAIN_0_66](#ggacf7907b21bea0f35196db039a709aae2ace0a1901fbb7eaa844836ab8d8045d0f)、[VEML60XX_GAIN_0_5](#ggacf7907b21bea0f35196db039a709aae2a44a29c15556bdadda3fc2094b37376c4)。

VEML60xx 环境光测量（Ambient Light Measurements）的增益选项（Gain Options）。

<a id="r_gacb2554bb01df63048cdcc1894903dd73"></a>

```c
enum veml60xx_pers { VEML60XX_PERS_1 = 0x00 , VEML60XX_PERS_2 = 0x01 , VEML60XX_PERS_4 = 0x02 , VEML60XX_PERS_8 = 0x03 }
```

相关声明：[veml60xx_pers](#gacb2554bb01df63048cdcc1894903dd73)、[VEML60XX_PERS_1](#ggacb2554bb01df63048cdcc1894903dd73a5e9eb5eb2a246c0ec010d7e919a6e7d1)、[VEML60XX_PERS_2](#ggacb2554bb01df63048cdcc1894903dd73aa0702d230730c0b9c773d92286caa0da)、[VEML60XX_PERS_4](#ggacb2554bb01df63048cdcc1894903dd73a263545540e87c4000fe7dc3d6bf24393)、[VEML60XX_PERS_8](#ggacb2554bb01df63048cdcc1894903dd73a2a0f5a62380a9690d53cd42e90e92ec4)。

VEML60xx 环境光传感器（ALS）中断持续性保护次数选项（Interrupt Persistence Protect Number Options）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 25.4\_函数（Functions）

<a id="r_gaba51cd71795a34af85d21da10cba5b44"></a>

```c
static bool veml60xx_gain_in_range (int32_t gain)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[veml60xx_gain_in_range](#gaba51cd71795a34af85d21da10cba5b44)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

<a id="r_ga2635095ab9ddf8ffd8e25cbaf08b824a"></a>

```c
static bool veml60xx_it_in_range (int32_t it)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[veml60xx_it_in_range](#ga2635095ab9ddf8ffd8e25cbaf08b824a)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

<a id="r_ga030b4553bb1982a3f470dcfe70a74636"></a>

```c
static bool veml60xx_pers_in_range (int32_t pers)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[veml60xx_pers_in_range](#ga030b4553bb1982a3f470dcfe70a74636)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 25.5\_变量（Variables）

<a id="r_ga95d24f44c42ba4d71df013ace6c6d613"></a>

```c
static const struct veml60xx_it_data veml60xx_it_values [VEML60XX_IT_COUNT]
```

相关声明：[veml60xx_it_data](../sensor_navigation_model_reference/P073_veml60xx_it_data_结构体.md)、[veml60xx_it_values](#ga95d24f44c42ba4d71df013ace6c6d613)。

## 25.6\_详细说明（Detailed Documentation）

<a id="gacf7907b21bea0f35196db039a709aae2"></a>

### `veml60xx_gain`

```c
enum veml60xx_gain
```

```c
#include <zephyr/drivers/sensor/veml60xx-common.h>
```

VEML60xx 环境光测量（Ambient Light Measurements）的增益选项（Gain Options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VEML60XX_GAIN_1` | 1 倍增益（Gain）。 |
| `VEML60XX_GAIN_2` | 2 倍增益（Gain）。 |
| `VEML60XX_GAIN_0_66` | 0.66 倍增益（Gain）。 |
| `VEML60XX_GAIN_0_5` | 0.5 倍增益（Gain）。 |

<a id="ga8945da51940f67ee875a729d6de4d287"></a>

### `veml60xx_it`

```c
enum veml60xx_it
```

```c
#include <zephyr/drivers/sensor/veml60xx-common.h>
```

VEML60xx 环境光测量（Ambient Light Measurements）的积分时间选项（Integration Time Options）。

自定义属性（Custom Attribute）`SENSOR_ATTR_VEML6031_IT` 和 `SENSOR_ATTR_VEML6046_IT` 的可用取值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VEML60XX_IT_3_125` | 3.125 毫秒（ms）。 |
| `VEML60XX_IT_6_25` | 6.25 毫秒（ms）。 |
| `VEML60XX_IT_12_5` | 12.5 毫秒（ms）。 |
| `VEML60XX_IT_25` | 25 毫秒（ms）。 |
| `VEML60XX_IT_50` | 50 毫秒（ms）。 |
| `VEML60XX_IT_100` | 100 毫秒（ms）。 |
| `VEML60XX_IT_200` | 200 毫秒（ms）。 |
| `VEML60XX_IT_400` | 400 毫秒（ms）。 |

<a id="gacb2554bb01df63048cdcc1894903dd73"></a>

### `veml60xx_pers`

```c
enum veml60xx_pers
```

```c
#include <zephyr/drivers/sensor/veml60xx-common.h>
```

VEML60xx 环境光传感器（ALS）中断持续性保护次数选项（Interrupt Persistence Protect Number Options）。

自定义属性（Custom Attribute）`SENSOR_ATTR_VEML6031_PERS` 和 `SENSOR_ATTR_VEML6046_PERS` 的可用取值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VEML60XX_PERS_1` | 1 次测量（Measurements）。 |
| `VEML60XX_PERS_2` | 2 次测量（Measurements）。 |
| `VEML60XX_PERS_4` | 4 次测量（Measurements）。 |
| `VEML60XX_PERS_8` | 8 次测量（Measurements）。 |

<a id="gaba51cd71795a34af85d21da10cba5b44"></a>

### `veml60xx_gain_in_range()`

```c
bool veml60xx_gain_in_range ( int32_t gain)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor/veml60xx-common.h>
```

<a id="ga2635095ab9ddf8ffd8e25cbaf08b824a"></a>

### `veml60xx_it_in_range()`

```c
bool veml60xx_it_in_range ( int32_t it)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor/veml60xx-common.h>
```

<a id="ga030b4553bb1982a3f470dcfe70a74636"></a>

### `veml60xx_pers_in_range()`

```c
bool veml60xx_pers_in_range ( int32_t pers)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor/veml60xx-common.h>
```

<a id="ga95d24f44c42ba4d71df013ace6c6d613"></a>

### `veml60xx_it_values`

```c
const struct veml60xx_it_data veml60xx_it_values[VEML60XX_IT_COUNT]
```

声明属性：`static`。

```c
#include <zephyr/drivers/sensor/veml60xx-common.h>
```

原始示例（Example）：

```c
                                    = {
        {VEML60XX_IT_3_125, 0x00, 3125},
        {VEML60XX_IT_6_25, 0x01, 6250},
        {VEML60XX_IT_12_5, 0x02, 12500},
        {VEML60XX_IT_25, 0x03, 25000},
        {VEML60XX_IT_50, 0x04, 50000},
        {VEML60XX_IT_100, 0x05, 100000},
        {VEML60XX_IT_200, 0x06, 200000},
        {VEML60XX_IT_400, 0x07, 400000},
}
```


## 25.7\_原页交叉引用（Cross References）

- [veml60xx-common.h](../api_file_runtime_reference/P074_zephyr__drivers__sensor__veml60xx-common.h_文件参考.md)
- [veml60xx_it_data](../sensor_navigation_model_reference/P073_veml60xx_it_data_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [SENSOR_ATTR_VEML6031_IT](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#ggae442c85062217115e03dcebf4fb3cacca413d3609d2a3c20959d5aa48ae542e80)
- [SENSOR_ATTR_VEML6046_IT](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ggaa2daffcfea5560747a19e84e42c6c335a6b7ba7f1343d8310b836b21eaeea7c25)
- [SENSOR_ATTR_VEML6031_PERS](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#ggae442c85062217115e03dcebf4fb3caccae4c3adafe31112e0ea708ab9e1cf8a07)
- [SENSOR_ATTR_VEML6046_PERS](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ggaa2daffcfea5560747a19e84e42c6c335ad63cec22680ee6e843c6c9d0fec824cf)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggacf7907b21bea0f35196db039a709aae2ac5283d652e5c1f8b90cd5cd61f7d1a2b"></a>
<a id="ggacf7907b21bea0f35196db039a709aae2a9629a32182ea0b1d30ab6b617de8c1f5"></a>
<a id="ggacf7907b21bea0f35196db039a709aae2ace0a1901fbb7eaa844836ab8d8045d0f"></a>
<a id="ggacf7907b21bea0f35196db039a709aae2a44a29c15556bdadda3fc2094b37376c4"></a>
<a id="gga8945da51940f67ee875a729d6de4d287ac7a765f90c553870f710ae8897c92965"></a>
<a id="gga8945da51940f67ee875a729d6de4d287aa18934d815766e1d45ddbaca63856888"></a>
<a id="gga8945da51940f67ee875a729d6de4d287a62b1fdbf8ba56ec030d84adeb2c7e7fa"></a>
<a id="gga8945da51940f67ee875a729d6de4d287a6afc3f891825df56cd9b5c5da73b2144"></a>
<a id="gga8945da51940f67ee875a729d6de4d287a3176b08da4de3a380d9a5d5fe90ccd77"></a>
<a id="gga8945da51940f67ee875a729d6de4d287a8ee263a50188580a4c8911b3985af636"></a>
<a id="gga8945da51940f67ee875a729d6de4d287ae6dcaf0b5b132be10a2b049c713c0e0b"></a>
<a id="gga8945da51940f67ee875a729d6de4d287adf8374ac010d4be484d680649ee15e93"></a>
<a id="ggacb2554bb01df63048cdcc1894903dd73a5e9eb5eb2a246c0ec010d7e919a6e7d1"></a>
<a id="ggacb2554bb01df63048cdcc1894903dd73aa0702d230730c0b9c773d92286caa0da"></a>
<a id="ggacb2554bb01df63048cdcc1894903dd73a263545540e87c4000fe7dc3d6bf24393"></a>
<a id="ggacb2554bb01df63048cdcc1894903dd73a2a0f5a62380a9690d53cd42e90e92ec4"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="doc-var-members"></a>
<a id="header-doc-var-members"></a>
<a id="agroup__veml60xx__interface_html_gga8945da51940f67ee875a729d6de4d287a3176b08da4de3a380d9a5d5fe90ccd77"></a>
<a id="agroup__veml60xx__interface_html_gga8945da51940f67ee875a729d6de4d287a62b1fdbf8ba56ec030d84adeb2c7e7fa"></a>
<a id="agroup__veml60xx__interface_html_gga8945da51940f67ee875a729d6de4d287a6afc3f891825df56cd9b5c5da73b2144"></a>
<a id="agroup__veml60xx__interface_html_gga8945da51940f67ee875a729d6de4d287a8ee263a50188580a4c8911b3985af636"></a>
<a id="agroup__veml60xx__interface_html_gga8945da51940f67ee875a729d6de4d287aa18934d815766e1d45ddbaca63856888"></a>
<a id="agroup__veml60xx__interface_html_gga8945da51940f67ee875a729d6de4d287ac7a765f90c553870f710ae8897c92965"></a>
<a id="agroup__veml60xx__interface_html_gga8945da51940f67ee875a729d6de4d287adf8374ac010d4be484d680649ee15e93"></a>
<a id="agroup__veml60xx__interface_html_gga8945da51940f67ee875a729d6de4d287ae6dcaf0b5b132be10a2b049c713c0e0b"></a>

---

[上一章](P024_USB 电力传输电源数据对象（USB Power Delivery Power Data Objects）.md) · [返回大纲](大纲.md) · [下一章](P026_视频能力（Video Capabilities）.md)
