---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-20
title: VEML6031 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_VEML6031 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Vishay VEML6031 高精度环境光传感器（High Accuracy Ambient Light Sensor）。

<a id="details"></a>

Vishay VEML6031 高精度环境光传感器（High Accuracy Ambient Light Sensor）。

<a id="header-files"></a>
<a id="files"></a>

## 20.1\_文件（Files）

<a id="r_veml6031_2Eh"></a>

```c
file veml6031.h
```

相关声明：[veml6031.h](../api_file_runtime_reference/P072_zephyr__drivers__sensor__veml6031.h_文件参考.md)。

VEML6031传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 20.2\_枚举（Enumerations）

<a id="r_ga8fdeb1ef880fb5a03c121f8d6456a738"></a>

```c
enum veml6031_div4 { VEML6031_SIZE_4_4 = 0x00 , VEML6031_SIZE_1_4 = 0x01 }
```

相关声明：[veml6031_div4](#ga8fdeb1ef880fb5a03c121f8d6456a738)、[VEML6031_SIZE_4_4](#gga8fdeb1ef880fb5a03c121f8d6456a738a42ddf6981430a245dbeac297a125f022)、[VEML6031_SIZE_1_4](#gga8fdeb1ef880fb5a03c121f8d6456a738a761d4cb4dfbf7678f2ea6587e24474c3)。

VEML6031 环境光测量（Ambient Light Measurements）的尺寸选项（Size Options）。

<a id="r_gae442c85062217115e03dcebf4fb3cacc"></a>

```c
enum sensor_attribute_veml6031 { SENSOR_ATTR_VEML6031_IT = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_VEML6031_DIV4 , SENSOR_ATTR_VEML6031_GAIN , SENSOR_ATTR_VEML6031_PERS }
```

相关声明：[sensor_attribute_veml6031](#gae442c85062217115e03dcebf4fb3cacc)、[SENSOR_ATTR_VEML6031_IT](#ggae442c85062217115e03dcebf4fb3cacca413d3609d2a3c20959d5aa48ae542e80)、[SENSOR_ATTR_VEML6031_DIV4](#ggae442c85062217115e03dcebf4fb3cacca1a103d0756ba6235e9bdc56e5f4ee68c)、[SENSOR_ATTR_VEML6031_GAIN](#ggae442c85062217115e03dcebf4fb3caccaed21ce91c964265a40b0e6ed7395e67a)、[SENSOR_ATTR_VEML6031_PERS](#ggae442c85062217115e03dcebf4fb3caccae4c3adafe31112e0ea708ab9e1cf8a07)。

VEML6031 传感器的自定义属性（Custom Sensor Attributes）。

<a id="r_gaf62d29159c2a40cbd8cd1e3d7522afb9"></a>

```c
enum sensor_channel_veml6031 { SENSOR_CHAN_VEML6031_ALS_RAW_COUNTS = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_VEML6031_IR_RAW_COUNTS }
```

相关声明：[sensor_channel_veml6031](#gaf62d29159c2a40cbd8cd1e3d7522afb9)、[SENSOR_CHAN_VEML6031_ALS_RAW_COUNTS](#ggaf62d29159c2a40cbd8cd1e3d7522afb9a778749581356d6568c03aa510a36370d)、[SENSOR_CHAN_VEML6031_IR_RAW_COUNTS](#ggaf62d29159c2a40cbd8cd1e3d7522afb9ac2834dbc5ba2a39d86461b34d5e06e65)。

VEML6031 传感器的自定义通道（Custom Sensor Channels）。

## 20.3\_详细说明（Detailed Documentation）

<a id="gae442c85062217115e03dcebf4fb3cacc"></a>

### `sensor_attribute_veml6031`

```c
enum sensor_attribute_veml6031
```

```c
#include <zephyr/drivers/sensor/veml6031.h>
```

VEML6031 传感器的自定义属性（Custom Sensor Attributes）。

配置阈值窗口的上下限（Threshold Window，ALS_WH_L、ALS_WH_H、ALS_WL_L 和 ALS_WL_H）时，使用通用属性 SENSOR_ATTR_UPPER_THRESH 和 SENSOR_ATTR_LOWER_THRESH，并提供 16 位无符号整数值。两个阈值均以勒克斯（Lux）为单位，由驱动转换为传感器兼容的值。转换依赖当前增益（Gain）、积分时间（Integration Time）和有效光电二极管尺寸（Effective Photodiode Size）设置。因此，改变这些设置通常需要更新阈值窗口。为向传感器写入正确阈值，应在改变增益或积分时间之后再更新阈值。

所有属性（Attributes）都必须针对 SENSOR_CHAN_LIGHT 通道设置。

传感器进入饱和（Saturation）状态时返回 -E2BIG；即原始环境光（ALS）值达到最大值 0xFFFF。此时由用户降低以下一个或多个属性，使传感器回到最佳测量范围：

- SENSOR_ATTR_VEML6031_GAIN（增益，Gain）
- SENSOR_ATTR_VEML6031_IT（积分时间，Integration Time）
- SENSOR_ATTR_VEML6031_DIV4（有效光电二极管尺寸，Effective Photodiode Size）

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_VEML6031_IT` | 环境光测量（ALS Measurements）的积分时间（Integration Time，IT）设置。属性值使用 enum veml6031_it。 |
| `SENSOR_ATTR_VEML6031_DIV4` | 有效光电二极管尺寸（Effective Photodiode Size，DIV4）。属性值使用 enum veml6031_div4。 |
| `SENSOR_ATTR_VEML6031_GAIN` | 环境光测量（ALS Measurements）的增益（Gain，GAIN）设置。属性值使用 enum veml6031_gain。 |
| `SENSOR_ATTR_VEML6031_PERS` | 环境光（ALS）持续性保护计数（Persistence Protect Number，PERS）设置。属性值使用 enum veml6031_pers。 |

<a id="gaf62d29159c2a40cbd8cd1e3d7522afb9"></a>

### `sensor_channel_veml6031`

```c
enum sensor_channel_veml6031
```

```c
#include <zephyr/drivers/sensor/veml6031.h>
```

VEML6031 传感器的自定义通道（Custom Sensor Channels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_VEML6031_ALS_RAW_COUNTS` | 原始环境光传感器值通道（Raw ALS Sensor Values）。此通道表示传感器 ALS 寄存器提供的原始测量计数。在获取与读取模式（Fetch and Get Mode）下，可用于估算合适的积分时间（Integration Time）、有效光电二极管尺寸（Effective Photodiode Size）和增益（Gain）属性值。对于未来使用触发器（Triggers）的实现，也可用于估算处理传感器中断所需的阈值窗口属性（Threshold Window Attributes）。不能直接采集此通道。其值通过 SENSOR_CHAN_LIGHT 隐式采集。尝试将此枚举值作为参数调用 sensor_sample_fetch_chan 会返回 -ENOTSUP。 |
| `SENSOR_CHAN_VEML6031_IR_RAW_COUNTS` | 红外传感器值通道（IR Sensor Values）。此通道为传感器的原始红外通道计数（Raw IR Channel Count）输出。采集方式与 SENSOR_CHAN_VEML6031_ALS_RAW_COUNTS 相同。 |

<a id="ga8fdeb1ef880fb5a03c121f8d6456a738"></a>

### `veml6031_div4`

```c
enum veml6031_div4
```

```c
#include <zephyr/drivers/sensor/veml6031.h>
```

VEML6031 环境光测量（Ambient Light Measurements）的尺寸选项（Size Options）。

自定义属性 SENSOR_ATTR_VEML6031_DIV4 的可选值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VEML6031_SIZE_4_4` | 光电二极管尺寸（Photodiode Size）：4/4。 |
| `VEML6031_SIZE_1_4` | 光电二极管尺寸（Photodiode Size）：1/4。 |


## 20.4\_原页交叉引用（Cross References）

- [veml6031.h](../api_file_runtime_reference/P072_zephyr__drivers__sensor__veml6031.h_文件参考.md)
- [SENSOR_ATTR_UPPER_THRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b)
- [SENSOR_ATTR_LOWER_THRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa)
- [SENSOR_CHAN_LIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e91196c11d080c3f5df55fda190e19d)
- [sensor_sample_fetch_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gac16192826432438a15274cf28d66e8a6)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggae442c85062217115e03dcebf4fb3cacca413d3609d2a3c20959d5aa48ae542e80"></a>
<a id="ggae442c85062217115e03dcebf4fb3cacca1a103d0756ba6235e9bdc56e5f4ee68c"></a>
<a id="ggae442c85062217115e03dcebf4fb3caccaed21ce91c964265a40b0e6ed7395e67a"></a>
<a id="ggae442c85062217115e03dcebf4fb3caccae4c3adafe31112e0ea708ab9e1cf8a07"></a>
<a id="ggaf62d29159c2a40cbd8cd1e3d7522afb9a778749581356d6568c03aa510a36370d"></a>
<a id="ggaf62d29159c2a40cbd8cd1e3d7522afb9ac2834dbc5ba2a39d86461b34d5e06e65"></a>
<a id="gga8fdeb1ef880fb5a03c121f8d6456a738a42ddf6981430a245dbeac297a125f022"></a>
<a id="gga8fdeb1ef880fb5a03c121f8d6456a738a761d4cb4dfbf7678f2ea6587e24474c3"></a>

---

[上一章](P019_USB Type-C 电源路径控制器（Power Path Controller）.md) · [返回大纲](大纲.md) · [下一章](P021_VEML6046 API主题.md)
