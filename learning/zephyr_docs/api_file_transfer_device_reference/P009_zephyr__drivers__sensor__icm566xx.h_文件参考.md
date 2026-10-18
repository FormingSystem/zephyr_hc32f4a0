---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-9
title: zephyr__drivers__sensor__icm566xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2icm566xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_drivers\_\_sensor\_\_icm566xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2icm566xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ICM566XX微机电系统（MEMS）传感器的扩展公共API。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

ICM566XX 微机电系统（MEMS）传感器的扩展公共 API（Extended Public API）。此传感器的部分能力与运行要求无法通过传感器驱动抽象层（Sensor Driver Abstraction）表达。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.1\_宏定义（Macros）

<a id="r_a2324756a1178758ee5c80fbe5517fc51"></a>

```c
#define ICM566XX_LOW_NOISE_MODE (0)
```

相关声明：[ICM566XX_LOW_NOISE_MODE](#a2324756a1178758ee5c80fbe5517fc51)。

ICM566XX 低噪声电源模式（Low Noise Power Mode）。

<a id="r_a3c7e5257d12143d56b83d1cbf0db7b6d"></a>

```c
#define ICM566XX_LOW_POWER_MODE (1)
```

相关声明：[ICM566XX_LOW_POWER_MODE](#a3c7e5257d12143d56b83d1cbf0db7b6d)。

ICM566XX 低功耗模式（Low Power Mode）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 9.2\_枚举（Enumerations）

<a id="r_a727f9f1bf2e18d3669e8c172af5fcb0f"></a>

```c
enum sensor_attribute_icm566xx { SENSOR_ATTR_BW_FILTER_LPF = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_AVERAGING }
```

相关声明：[sensor_attribute_icm566xx](#a727f9f1bf2e18d3669e8c172af5fcb0f)、[SENSOR_ATTR_BW_FILTER_LPF](#a727f9f1bf2e18d3669e8c172af5fcb0fabf09c4a7c9f18b6f0ac7273282cbc48c)、[SENSOR_ATTR_AVERAGING](#a727f9f1bf2e18d3669e8c172af5fcb0fa8a469c0e9236ce771ad4165670d3842d)。

ICM566XX MEMS 传感器的扩展传感器属性（Extended Sensor Attributes）。

## 9.3\_详细说明（Detailed Documentation）

<a id="a2324756a1178758ee5c80fbe5517fc51"></a>

### `ICM566XX_LOW_NOISE_MODE`

```c
#define ICM566XX_LOW_NOISE_MODE (0)
```

ICM566XX 低噪声电源模式（Low Noise Power Mode）。

<a id="a3c7e5257d12143d56b83d1cbf0db7b6d"></a>

### `ICM566XX_LOW_POWER_MODE`

```c
#define ICM566XX_LOW_POWER_MODE (1)
```

ICM566XX 低功耗模式（Low Power Mode）。

<a id="a727f9f1bf2e18d3669e8c172af5fcb0f"></a>

### `sensor_attribute_icm566xx`

```c
enum sensor_attribute_icm566xx
```

ICM566XX MEMS 传感器的扩展传感器属性（Extended Sensor Attributes）。

这里公开 ICM566XX 的属性，可用于设置信号路径滤波参数（Signal Path Filtering Parameters）。

信号路径（Signal Path）从陀螺仪和加速度计的模数转换器（ADC）开始。加速度计提供低噪声模式（Low-Noise Mode）和低功耗模式（Low-Power Mode），陀螺仪仅提供低噪声模式。

在低噪声模式下，ADC 输出先经过抗混叠滤波器（Anti-Alias Filter，AAF）。其系数固定，用户不能配置，也不能旁路。随后经过一阶低通滤波器（Low Pass Filter，LPF），用户可选择滤波带宽。

在低功耗模式下，加速度计 ADC 输出经过平均滤波器（Average Filter），平均滤波设置可由用户配置。低噪声模式下一阶 LPF 的输出，或低功耗模式下平均滤波器的输出，再按用户选择的输出数据率（ODR）输出。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_BW_FILTER_LPF` | 带宽滤波（BW Filtering），低通滤波器配置（Low-pass Filter Configuration）。 |
| `SENSOR_ATTR_AVERAGING` | 平均滤波配置（Averaging Configuration）。 |


## 9.4\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P175_icm566xx.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a727f9f1bf2e18d3669e8c172af5fcb0fabf09c4a7c9f18b6f0ac7273282cbc48c"></a>
<a id="a727f9f1bf2e18d3669e8c172af5fcb0fa8a469c0e9236ce771ad4165670d3842d"></a>

---

[上一章](P008_zephyr__drivers__mfd__npm13xx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__drivers__sensor__tmp11x.h_文件参考.md)
