---
id: learning.zephyr-docs.api-file-system-power-reference.page-37
title: zephyr__drivers__sensor__mcux_acmp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_zephyr\_\_drivers\_\_sensor\_\_mcux\_acmp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2mcux__acmp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP MCUX模拟比较器（Analog Comparator，ACMP）的扩展公共API。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

NXP MCUX模拟比较器（Analog Comparator，ACMP）的扩展公共API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 37.1\_宏定义（Macros）

<a id="r_a25badb86c21dac89b1fdf3462726e487"></a>

```c
#define MCUX_ACMP_HAS_INPSEL 0
```

相关声明：[MCUX_ACMP_HAS_INPSEL](#a25badb86c21dac89b1fdf3462726e487)。

<a id="r_a7d2ec98ad2d468666974905de3593852"></a>

```c
#define MCUX_ACMP_HAS_INNSEL 0
```

相关声明：[MCUX_ACMP_HAS_INNSEL](#a7d2ec98ad2d468666974905de3593852)。

<a id="r_a600499ad6c1ab652febb864c90c17574"></a>

```c
#define MCUX_ACMP_HAS_OFFSET 0
```

相关声明：[MCUX_ACMP_HAS_OFFSET](#a600499ad6c1ab652febb864c90c17574)。

<a id="r_ab8101cc404679700315d6a4fea729e24"></a>

```c
#define MCUX_ACMP_HAS_DISCRETE_MODE 0
```

相关声明：[MCUX_ACMP_HAS_DISCRETE_MODE](#ab8101cc404679700315d6a4fea729e24)。

<a id="r_ab2efc4cf8c2b85a7b8616faadaeee583"></a>

```c
#define MCUX_ACMP_HAS_HYSTCTR 0
```

相关声明：[MCUX_ACMP_HAS_HYSTCTR](#ab2efc4cf8c2b85a7b8616faadaeee583)。

<a id="r_a3812ab6ca2b30a83bf843532088ee7c6"></a>

```c
#define MCUX_ACMP_HAS_WINDOW_MODE 1
```

相关声明：[MCUX_ACMP_HAS_WINDOW_MODE](#a3812ab6ca2b30a83bf843532088ee7c6)。

<a id="r_aa96532dd9f8483bf86f345e4eeb4828b"></a>

```c
#define MCUX_ACMP_HAS_SAMPLE_CLOCK_SELECTION 1
```

相关声明：[MCUX_ACMP_HAS_SAMPLE_CLOCK_SELECTION](#aa96532dd9f8483bf86f345e4eeb4828b)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 37.2\_枚举（Enumerations）

<a id="r_a017d1a028479db7f49a1327814fe72da"></a>

```c
enum sensor_channel_mcux_acmp { SENSOR_CHAN_MCUX_ACMP_OUTPUT = SENSOR_CHAN_PRIV_START }
```

相关声明：[sensor_channel_mcux_acmp](#a017d1a028479db7f49a1327814fe72da)、[SENSOR_CHAN_MCUX_ACMP_OUTPUT](#a017d1a028479db7f49a1327814fe72daa249515617e8c5017591017dcc076614d)。

<a id="r_af10919d10852c60efa9fb8d3fa56c829"></a>

```c
enum sensor_trigger_type_mcux_acmp { SENSOR_TRIG_MCUX_ACMP_OUTPUT_RISING = SENSOR_TRIG_PRIV_START , SENSOR_TRIG_MCUX_ACMP_OUTPUT_FALLING }
```

相关声明：[sensor_trigger_type_mcux_acmp](#af10919d10852c60efa9fb8d3fa56c829)、[SENSOR_TRIG_MCUX_ACMP_OUTPUT_RISING](#af10919d10852c60efa9fb8d3fa56c829a808392257cdee8941e5cbafe480e4697)、[SENSOR_TRIG_MCUX_ACMP_OUTPUT_FALLING](#af10919d10852c60efa9fb8d3fa56c829a6e0dd402df6647c13d0312cea7d4972d)。

<a id="r_a1e7a45b41695dede14a6b432ceb36daf"></a>

```c
enum sensor_attribute_mcux_acmp { SENSOR_ATTR_MCUX_ACMP_OFFSET_LEVEL = SENSOR_ATTR_COMMON_COUNT , SENSOR_ATTR_MCUX_ACMP_HYSTERESIS_LEVEL , SENSOR_ATTR_MCUX_ACMP_DAC_VOLTAGE_REFERENCE , SENSOR_ATTR_MCUX_ACMP_DAC_VALUE , SENSOR_ATTR_MCUX_ACMP_POSITIVE_PORT_INPUT , SENSOR_ATTR_MCUX_ACMP_POSITIVE_MUX_INPUT , SENSOR_ATTR_MCUX_ACMP_NEGATIVE_PORT_INPUT , SENSOR_ATTR_MCUX_ACMP_NEGATIVE_MUX_INPUT }
```

相关声明：[sensor_attribute_mcux_acmp](#a1e7a45b41695dede14a6b432ceb36daf)、[SENSOR_ATTR_MCUX_ACMP_OFFSET_LEVEL](#a1e7a45b41695dede14a6b432ceb36dafa2775a96b5738be33bead0d429edeb250)、[SENSOR_ATTR_MCUX_ACMP_HYSTERESIS_LEVEL](#a1e7a45b41695dede14a6b432ceb36dafaf1f98be88dedc82ac02d8ac363a8e30c)、[SENSOR_ATTR_MCUX_ACMP_DAC_VOLTAGE_REFERENCE](#a1e7a45b41695dede14a6b432ceb36dafaef555e4535128d33d66a31041758b361)、[SENSOR_ATTR_MCUX_ACMP_DAC_VALUE](#a1e7a45b41695dede14a6b432ceb36dafa5b0fc158891b4f5da15d22cf46b8038d)、[SENSOR_ATTR_MCUX_ACMP_POSITIVE_PORT_INPUT](#a1e7a45b41695dede14a6b432ceb36dafa94b2b5d9ea4809c533f4c4f02f4f0000)、[SENSOR_ATTR_MCUX_ACMP_POSITIVE_MUX_INPUT](#a1e7a45b41695dede14a6b432ceb36dafab865cc40646af2eb05f0400e6d89c1a2)、[SENSOR_ATTR_MCUX_ACMP_NEGATIVE_PORT_INPUT](#a1e7a45b41695dede14a6b432ceb36dafa224855d60b92abd37e7418b7f73bbee6)、[SENSOR_ATTR_MCUX_ACMP_NEGATIVE_MUX_INPUT](#a1e7a45b41695dede14a6b432ceb36dafac3713c38d4654d0a9dd68f711d0c348b)。

## 37.3\_详细说明（Detailed Documentation）

<a id="ab8101cc404679700315d6a4fea729e24"></a>

### `MCUX_ACMP_HAS_DISCRETE_MODE`

```c
#define MCUX_ACMP_HAS_DISCRETE_MODE 0
```

<a id="ab2efc4cf8c2b85a7b8616faadaeee583"></a>

### `MCUX_ACMP_HAS_HYSTCTR`

```c
#define MCUX_ACMP_HAS_HYSTCTR 0
```

<a id="a7d2ec98ad2d468666974905de3593852"></a>

### `MCUX_ACMP_HAS_INNSEL`

```c
#define MCUX_ACMP_HAS_INNSEL 0
```

<a id="a25badb86c21dac89b1fdf3462726e487"></a>

### `MCUX_ACMP_HAS_INPSEL`

```c
#define MCUX_ACMP_HAS_INPSEL 0
```

<a id="a600499ad6c1ab652febb864c90c17574"></a>

### `MCUX_ACMP_HAS_OFFSET`

```c
#define MCUX_ACMP_HAS_OFFSET 0
```

<a id="aa96532dd9f8483bf86f345e4eeb4828b"></a>

### `MCUX_ACMP_HAS_SAMPLE_CLOCK_SELECTION`

```c
#define MCUX_ACMP_HAS_SAMPLE_CLOCK_SELECTION 1
```

<a id="a3812ab6ca2b30a83bf843532088ee7c6"></a>

### `MCUX_ACMP_HAS_WINDOW_MODE`

```c
#define MCUX_ACMP_HAS_WINDOW_MODE 1
```

<a id="a1e7a45b41695dede14a6b432ceb36daf"></a>

### `sensor_attribute_mcux_acmp`

```c
enum sensor_attribute_mcux_acmp
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_MCUX_ACMP_OFFSET_LEVEL` | 模拟比较器硬件模块偏移量（Analog Comparator Hard Block Offset）。 |
| `SENSOR_ATTR_MCUX_ACMP_HYSTERESIS_LEVEL` | 模拟比较器迟滞级别（Analog Comparator Hysteresis Level）。 |
| `SENSOR_ATTR_MCUX_ACMP_DAC_VOLTAGE_REFERENCE` | 模拟比较器数模转换器（DAC）的电压参考源（Voltage Reference Source）。 |
| `SENSOR_ATTR_MCUX_ACMP_DAC_VALUE` | 模拟比较器数模转换器值（Analog Comparator DAC Value）。 |
| `SENSOR_ATTR_MCUX_ACMP_POSITIVE_PORT_INPUT` | 模拟比较器正端端口输入（Positive Port Input）。 |
| `SENSOR_ATTR_MCUX_ACMP_POSITIVE_MUX_INPUT` | 模拟比较器正端多路复用输入（Positive Mux Input）。 |
| `SENSOR_ATTR_MCUX_ACMP_NEGATIVE_PORT_INPUT` | 模拟比较器负端端口输入（Negative Port Input）。 |
| `SENSOR_ATTR_MCUX_ACMP_NEGATIVE_MUX_INPUT` | 模拟比较器负端多路复用输入（Negative Mux Input）。 |

<a id="a017d1a028479db7f49a1327814fe72da"></a>

### `sensor_channel_mcux_acmp`

```c
enum sensor_channel_mcux_acmp
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_MCUX_ACMP_OUTPUT` | 模拟比较器输出（Analog Comparator Output）。 |

<a id="af10919d10852c60efa9fb8d3fa56c829"></a>

### `sensor_trigger_type_mcux_acmp`

```c
enum sensor_trigger_type_mcux_acmp
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_TRIG_MCUX_ACMP_OUTPUT_RISING` | 模拟比较器输出的上升事件触发（Output Rising Event Trigger）。 |
| `SENSOR_TRIG_MCUX_ACMP_OUTPUT_FALLING` | 模拟比较器输出的下降事件触发（Output Falling Event Trigger）。 |


## 37.4\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P763_mcux_acmp.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a1e7a45b41695dede14a6b432ceb36dafa2775a96b5738be33bead0d429edeb250"></a>
<a id="a1e7a45b41695dede14a6b432ceb36dafaf1f98be88dedc82ac02d8ac363a8e30c"></a>
<a id="a1e7a45b41695dede14a6b432ceb36dafaef555e4535128d33d66a31041758b361"></a>
<a id="a1e7a45b41695dede14a6b432ceb36dafa5b0fc158891b4f5da15d22cf46b8038d"></a>
<a id="a1e7a45b41695dede14a6b432ceb36dafa94b2b5d9ea4809c533f4c4f02f4f0000"></a>
<a id="a1e7a45b41695dede14a6b432ceb36dafab865cc40646af2eb05f0400e6d89c1a2"></a>
<a id="a1e7a45b41695dede14a6b432ceb36dafa224855d60b92abd37e7418b7f73bbee6"></a>
<a id="a1e7a45b41695dede14a6b432ceb36dafac3713c38d4654d0a9dd68f711d0c348b"></a>
<a id="a017d1a028479db7f49a1327814fe72daa249515617e8c5017591017dcc076614d"></a>
<a id="af10919d10852c60efa9fb8d3fa56c829a808392257cdee8941e5cbafe480e4697"></a>
<a id="af10919d10852c60efa9fb8d3fa56c829a6e0dd402df6647c13d0312cea7d4972d"></a>

---

[上一章](P036_zephyr__arch__common__semihost.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P038_zephyr__mgmt__mcumgr__transport__smp_dummy.h_文件参考.md)
