---
id: learning.zephyr-docs.api-file-serial-motion-reference.page-6
title: zephyr__drivers__sensor__mcux_lpcmp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_drivers\_\_sensor\_\_mcux\_lpcmp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mcux__lpcmp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP MCUX低功耗模拟比较器（LPCMP）的数据结构。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

NXP MCUX低功耗模拟比较器（LPCMP）的数据结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.1\_枚举（Enumerations）

<a id="r_a0afc296fa89b7bdd31105574f459fb5a"></a>

```c
enum sensor_channel_mcux_lpcmp { SENSOR_CHAN_MCUX_LPCMP_OUTPUT = SENSOR_CHAN_PRIV_START }
```

相关声明：[sensor_channel_mcux_lpcmp](#a0afc296fa89b7bdd31105574f459fb5a)、[SENSOR_CHAN_MCUX_LPCMP_OUTPUT](#a0afc296fa89b7bdd31105574f459fb5aad1561ee6f508b72ad743971d60bb9d87)。

低功耗比较器（LPCMP）通道（Channels）。

<a id="r_ad86c67639b0a919fd5ea0b5b6a3d4cd6"></a>

```c
enum sensor_trigger_type_mcux_lpcmp { SENSOR_TRIG_MCUX_LPCMP_OUTPUT_RISING = SENSOR_TRIG_PRIV_START , SENSOR_TRIG_MCUX_LPCMP_OUTPUT_FALLING }
```

相关声明：[sensor_trigger_type_mcux_lpcmp](#ad86c67639b0a919fd5ea0b5b6a3d4cd6)、[SENSOR_TRIG_MCUX_LPCMP_OUTPUT_RISING](#ad86c67639b0a919fd5ea0b5b6a3d4cd6a8a221bd8580a353cd4edf38a3c217e7e)、[SENSOR_TRIG_MCUX_LPCMP_OUTPUT_FALLING](#ad86c67639b0a919fd5ea0b5b6a3d4cd6a002b0d7bd234a6bece9b8baae411f1e9)。

低功耗比较器（LPCMP）触发类型（Trigger Types）。

<a id="r_a8104360e57e8d294fb6bd02812fcc03e"></a>

```c
enum sensor_attribute_mcux_lpcmp { SENSOR_ATTR_MCUX_LPCMP_POSITIVE_MUX_INPUT = SENSOR_ATTR_COMMON_COUNT , SENSOR_ATTR_MCUX_LPCMP_NEGATIVE_MUX_INPUT , SENSOR_ATTR_MCUX_LPCMP_DAC_ENABLE , SENSOR_ATTR_MCUX_LPCMP_DAC_HIGH_POWER_MODE_ENABLE , SENSOR_ATTR_MCUX_LPCMP_DAC_REFERENCE_VOLTAGE_SOURCE , SENSOR_ATTR_MCUX_LPCMP_DAC_OUTPUT_VOLTAGE , SENSOR_ATTR_MCUX_LPCMP_SAMPLE_ENABLE , SENSOR_ATTR_MCUX_LPCMP_FILTER_COUNT , SENSOR_ATTR_MCUX_LPCMP_FILTER_PERIOD , SENSOR_ATTR_MCUX_LPCMP_COUTA_WINDOW_ENABLE , SENSOR_ATTR_MCUX_LPCMP_COUTA_WINDOW_SIGNAL_INVERT_ENABLE , SENSOR_ATTR_MCUX_LPCMP_COUTA_SIGNAL , SENSOR_ATTR_MCUX_LPCMP_COUT_EVENT_TO_CLOSE_WINDOW }
```

相关声明：[sensor_attribute_mcux_lpcmp](#a8104360e57e8d294fb6bd02812fcc03e)、[SENSOR_ATTR_MCUX_LPCMP_POSITIVE_MUX_INPUT](#a8104360e57e8d294fb6bd02812fcc03ea595f556e4cefb69c33cf94e9e0cb8eab)、[SENSOR_ATTR_MCUX_LPCMP_NEGATIVE_MUX_INPUT](#a8104360e57e8d294fb6bd02812fcc03ea121200848c3ec07ced3979af7e186e52)、[SENSOR_ATTR_MCUX_LPCMP_DAC_ENABLE](#a8104360e57e8d294fb6bd02812fcc03ea5a50fc0d49b328f0475e145877922dd7)、[SENSOR_ATTR_MCUX_LPCMP_DAC_HIGH_POWER_MODE_ENABLE](#a8104360e57e8d294fb6bd02812fcc03ea0e0d40713788ceede8492bca750c9574)、[SENSOR_ATTR_MCUX_LPCMP_DAC_REFERENCE_VOLTAGE_SOURCE](#a8104360e57e8d294fb6bd02812fcc03ea5eb0fe730a64c50ca6bfec6b99090b01)、[SENSOR_ATTR_MCUX_LPCMP_DAC_OUTPUT_VOLTAGE](#a8104360e57e8d294fb6bd02812fcc03eabaf75089237d3f692504b7b491bddbd9)、[SENSOR_ATTR_MCUX_LPCMP_SAMPLE_ENABLE](#a8104360e57e8d294fb6bd02812fcc03ea63ae262c76b0def09bebf9f760558d66)、[SENSOR_ATTR_MCUX_LPCMP_FILTER_COUNT](#a8104360e57e8d294fb6bd02812fcc03ea853df07e6a142095a6f64024f7bb9e03)、[SENSOR_ATTR_MCUX_LPCMP_FILTER_PERIOD](#a8104360e57e8d294fb6bd02812fcc03ea19a4a2f184cbb2c32300dd2eb436e4fa)、[SENSOR_ATTR_MCUX_LPCMP_COUTA_WINDOW_ENABLE](#a8104360e57e8d294fb6bd02812fcc03ea788ac8f0f9bbfd215601090d0653b12e)、[SENSOR_ATTR_MCUX_LPCMP_COUTA_WINDOW_SIGNAL_INVERT_ENABLE](#a8104360e57e8d294fb6bd02812fcc03ea620c4eabae0fc9bfaaf2999a4c4b22cf)、[SENSOR_ATTR_MCUX_LPCMP_COUTA_SIGNAL](#a8104360e57e8d294fb6bd02812fcc03ea8189889b48c2cd89feb78fc84d33805a)、[SENSOR_ATTR_MCUX_LPCMP_COUT_EVENT_TO_CLOSE_WINDOW](#a8104360e57e8d294fb6bd02812fcc03ea0b7d5ec19095284f15e55a3054e849b4)。

低功耗比较器（LPCMP）属性类型（Attribute Types）。

## 6.2\_详细说明（Detailed Documentation）

<a id="a8104360e57e8d294fb6bd02812fcc03e"></a>

### `sensor_attribute_mcux_lpcmp`

```c
enum sensor_attribute_mcux_lpcmp
```

低功耗比较器（LPCMP）属性类型（Attribute Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_MCUX_LPCMP_POSITIVE_MUX_INPUT` | LPCMP 正输入多路复用器（Positive Input Mux）。 |
| `SENSOR_ATTR_MCUX_LPCMP_NEGATIVE_MUX_INPUT` | LPCMP 负输入多路复用器（Negative Input Mux）。 |
| `SENSOR_ATTR_MCUX_LPCMP_DAC_ENABLE` | LPCMP 内部数模转换器（DAC）使能。二进制值 `0b` 为禁用，`1b` 为使能。 |
| `SENSOR_ATTR_MCUX_LPCMP_DAC_HIGH_POWER_MODE_ENABLE` | LPCMP 内部数模转换器（DAC）高功率模式禁用（High Power Mode Disabled）设置：二进制值 `0b` 为禁用，`1b` 为使能。译注：原文的“disabled”与后续使能位说明均保留。 |
| `SENSOR_ATTR_MCUX_LPCMP_DAC_REFERENCE_VOLTAGE_SOURCE` | LPCMP 内部数模转换器（DAC）的参考电压源（Voltage Reference Source）。 |
| `SENSOR_ATTR_MCUX_LPCMP_DAC_OUTPUT_VOLTAGE` | LPCMP 内部数模转换器（DAC）的输出电压值（Output Voltage Value）。 |
| `SENSOR_ATTR_MCUX_LPCMP_SAMPLE_ENABLE` | LPCMP 内部滤波器采样使能（Filter Sample Enable）。 |
| `SENSOR_ATTR_MCUX_LPCMP_FILTER_COUNT` | LPCMP 内部滤波器采样数（Filter Sample Count）。 |
| `SENSOR_ATTR_MCUX_LPCMP_FILTER_PERIOD` | LPCMP 内部滤波器采样周期（Filter Sample Period）。 |
| `SENSOR_ATTR_MCUX_LPCMP_COUTA_WINDOW_ENABLE` | LPCMP 窗口信号反相（Window Signal Invert）。 |
| `SENSOR_ATTR_MCUX_LPCMP_COUTA_WINDOW_SIGNAL_INVERT_ENABLE` | LPCMP 窗口信号反相（Window Signal Invert）。 |
| `SENSOR_ATTR_MCUX_LPCMP_COUTA_SIGNAL` | 窗口关闭时 LPCMP COUTA 信号的值：`00b` 为锁存（Latched），`01b` 为置低，`11b` 为置高。 |
| `SENSOR_ATTR_MCUX_LPCMP_COUT_EVENT_TO_CLOSE_WINDOW` | 关闭活动窗口的 LPCMP COUT 事件：`xx0b` 表示 COUT 事件不能关闭活动窗口；`001b` 表示 COUT 上升沿事件关闭活动窗口；`011b` 表示下降沿事件关闭活动窗口；`1x1b` 表示双边沿事件关闭活动窗口。 |

<a id="a0afc296fa89b7bdd31105574f459fb5a"></a>

### `sensor_channel_mcux_lpcmp`

```c
enum sensor_channel_mcux_lpcmp
```

低功耗比较器（LPCMP）通道（Channels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_MCUX_LPCMP_OUTPUT` | LPCMP 输出（Output）。 |

<a id="ad86c67639b0a919fd5ea0b5b6a3d4cd6"></a>

### `sensor_trigger_type_mcux_lpcmp`

```c
enum sensor_trigger_type_mcux_lpcmp
```

低功耗比较器（LPCMP）触发类型（Trigger Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_TRIG_MCUX_LPCMP_OUTPUT_RISING` | LPCMP 输出上升事件触发（Output Rising Event Trigger）。 |
| `SENSOR_TRIG_MCUX_LPCMP_OUTPUT_FALLING` | LPCMP 输出下降事件触发（Output Falling Event Trigger）。 |


## 6.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P511_mcux_lpcmp.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a8104360e57e8d294fb6bd02812fcc03ea595f556e4cefb69c33cf94e9e0cb8eab"></a>
<a id="a8104360e57e8d294fb6bd02812fcc03ea121200848c3ec07ced3979af7e186e52"></a>
<a id="a8104360e57e8d294fb6bd02812fcc03ea5a50fc0d49b328f0475e145877922dd7"></a>
<a id="a8104360e57e8d294fb6bd02812fcc03ea0e0d40713788ceede8492bca750c9574"></a>
<a id="a8104360e57e8d294fb6bd02812fcc03ea5eb0fe730a64c50ca6bfec6b99090b01"></a>
<a id="a8104360e57e8d294fb6bd02812fcc03eabaf75089237d3f692504b7b491bddbd9"></a>
<a id="a8104360e57e8d294fb6bd02812fcc03ea63ae262c76b0def09bebf9f760558d66"></a>
<a id="a8104360e57e8d294fb6bd02812fcc03ea853df07e6a142095a6f64024f7bb9e03"></a>
<a id="a8104360e57e8d294fb6bd02812fcc03ea19a4a2f184cbb2c32300dd2eb436e4fa"></a>
<a id="a8104360e57e8d294fb6bd02812fcc03ea788ac8f0f9bbfd215601090d0653b12e"></a>
<a id="a8104360e57e8d294fb6bd02812fcc03ea620c4eabae0fc9bfaaf2999a4c4b22cf"></a>
<a id="a8104360e57e8d294fb6bd02812fcc03ea8189889b48c2cd89feb78fc84d33805a"></a>
<a id="a8104360e57e8d294fb6bd02812fcc03ea0b7d5ec19095284f15e55a3054e849b4"></a>
<a id="a0afc296fa89b7bdd31105574f459fb5aad1561ee6f508b72ad743971d60bb9d87"></a>
<a id="ad86c67639b0a919fd5ea0b5b6a3d4cd6a8a221bd8580a353cd4edf38a3c217e7e"></a>
<a id="ad86c67639b0a919fd5ea0b5b6a3d4cd6a002b0d7bd234a6bece9b8baae411f1e9"></a>

---

[上一章](P005_zephyr__input__input_kbd_matrix.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__pwm__max31790.h_文件参考.md)
