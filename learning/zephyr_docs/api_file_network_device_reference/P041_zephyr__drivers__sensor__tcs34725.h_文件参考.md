---
id: learning.zephyr-docs.api-file-network-device-reference.page-41
title: zephyr__drivers__sensor__tcs34725.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tcs34725_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_zephyr\_\_drivers\_\_sensor\_\_tcs34725.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tcs34725_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TCS34725颜色传感器（Color Sensor）的公共头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

TCS34725颜色传感器（Color Sensor）的公共头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 41.1\_枚举（Enumerations）

<a id="r_af83b5fad1e199c52a170010fb104804a"></a>

```c
enum tcs34725_channel { SENSOR_CHAN_TCS34725_LUX = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_TCS34725_COLOR_TEMP }
```

相关声明：[tcs34725_channel](#af83b5fad1e199c52a170010fb104804a)、[SENSOR_CHAN_TCS34725_LUX](#af83b5fad1e199c52a170010fb104804aa66e34f6c35c1afd60b3a2b93cf7399ad)、[SENSOR_CHAN_TCS34725_COLOR_TEMP](#af83b5fad1e199c52a170010fb104804aafcdfd37095d5365ce7fb43282d1b2c5e)。

TCS34725 驱动专用传感器通道标识符（Sensor Channel Identifiers）。

## 41.2\_详细说明（Detailed Documentation）

<a id="af83b5fad1e199c52a170010fb104804a"></a>

### `tcs34725_channel`

```c
enum tcs34725_channel
```

TCS34725 驱动专用传感器通道标识符（Sensor Channel Identifiers）。

这些通道提供使用 ams DN40 算法，根据原始全光谱（Clear）、红、绿、蓝 ADC 读数计算得到的派生值（Derived Values）：

- `SENSOR_CHAN_TCS34725_LUX`：照度（Illuminance），单位为勒克斯（lux）。
- `SENSOR_CHAN_TCS34725_COLOR_TEMP`：相关色温（Correlated Color Temperature），单位为开尔文（Kelvin）。

对于这两个通道，应用程序使用 `val->val1` 前必须始终检查 `val->val2`。原始 `SENSOR_CHAN_RED/GREEN/BLUE/LIGHT` 通道始终有效，且不使用 `val->val2`，这些通道的该字段始终为 0。

成功调用 `sensor_sample_fetch()` 后，可在 `sensor_channel_get()` 中使用这些标识符。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_TCS34725_LUX` | 由 DN40 算法计算的照度（Illuminance），单位为勒克斯（lux）。 |
| `SENSOR_CHAN_TCS34725_COLOR_TEMP` | 计算得到的相关色温（Correlated Color Temperature，CT），单位为开尔文（Kelvin）。 |

**说明（Note）**：**注意（Note）——有效性标志（Validity Flag）：**对于这两个通道，`sensor_channel_get()` 在 `val->val1` 中返回结果，在 `val->val2` 中返回有效性标志。

- `val->val2 == 1`：DN40 计算成功，`val->val1` 为真实、可信的测量值。
- `val->val2 == 0`：计算无法产生可靠结果，可能是 RGBC 通道饱和、全光谱（Clear）通道低于可用下限，或更常见的高度饱和／纯单色光超出 DN40 公式的有效输入域。此时 `val->val1` 始终为 0，绝不能把它当作真实测量值；它不表示“零勒克斯”或“0 开尔文”。


## 41.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P859_tcs34725.h_源码浏览.md)
- [sensor_channel_get()](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga9e0e6c1408d32c52267984bae7cb268d)
- [sensor_sample_fetch()](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaa75e25d93ee7cac0bf38399f3c006dff)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="af83b5fad1e199c52a170010fb104804aa66e34f6c35c1afd60b3a2b93cf7399ad"></a>
<a id="af83b5fad1e199c52a170010fb104804aafcdfd37095d5365ce7fb43282d1b2c5e"></a>

---

[上一章](P040_zephyr__dt-bindings__pwm__stm32_pwm.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P042_zephyr__drivers__sensor__vl53l0x.h_文件参考.md)
