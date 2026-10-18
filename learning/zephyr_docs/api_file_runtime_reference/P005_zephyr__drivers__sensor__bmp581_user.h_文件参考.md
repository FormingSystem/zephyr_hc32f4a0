---
id: learning.zephyr-docs.api-file-runtime-reference.page-5
title: zephyr__drivers__sensor__bmp581_user.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bmp581__user_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_drivers\_\_sensor\_\_bmp581\_user.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bmp581__user_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BMP581传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
#include <zephyr/dt-bindings/sensor/bmp581.h>
```

查看此文件的源码。

BMP581传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="r_ga57c276018d0ac606684751e19784457e"></a>

```c
#define BMP5_ATTR_IIR_CONFIG (SENSOR_ATTR_PRIV_START + 1u)
```

相关声明：[BMP5_ATTR_IIR_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ga57c276018d0ac606684751e19784457e)、[SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)。

压力与温度通道的无限脉冲响应滤波器配置（IIR Configuration）。

<a id="r_ga4f6e56a0a4f9fd984d3993cf819281d8"></a>

```c
#define BMP5_ATTR_POWER_MODE (SENSOR_ATTR_PRIV_START + 2u)
```

相关声明：[BMP5_ATTR_POWER_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ga4f6e56a0a4f9fd984d3993cf819281d8)、[SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)。

电源模式（Power Mode）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.2\_枚举（Enumerations）

<a id="r_gaca06546e057d7295ca4f6ed4298247dc"></a>

```c
enum bmp5_powermode { BMP5_POWERMODE_STANDBY , BMP5_POWERMODE_NORMAL , BMP5_POWERMODE_FORCED , BMP5_POWERMODE_CONTINUOUS , BMP5_POWERMODE_DEEP_STANDBY }
```

相关声明：[bmp5_powermode](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#gaca06546e057d7295ca4f6ed4298247dc)、[BMP5_POWERMODE_STANDBY](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ggaca06546e057d7295ca4f6ed4298247dca8f50ab92ba9607eaeed772ddbe92a15f)、[BMP5_POWERMODE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ggaca06546e057d7295ca4f6ed4298247dcabb75d9c71965843c27724d956ffd1f8c)、[BMP5_POWERMODE_FORCED](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ggaca06546e057d7295ca4f6ed4298247dcaf57d41b2953f1986618de43ac1315b96)、[BMP5_POWERMODE_CONTINUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ggaca06546e057d7295ca4f6ed4298247dca14a304e989e6c079c9b6d668b4fd3e57)、[BMP5_POWERMODE_DEEP_STANDBY](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ggaca06546e057d7295ca4f6ed4298247dca3904b0e3e14b2cad554436ba96fe4bf1)。

BMP581 电源模式（Power Modes）。


## 5.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [zephyr/dt-bindings/sensor/bmp581.h](../api_source_reference/P075_bmp581.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P003_bmp581_user.h_源码浏览.md)
- [BMP5_ATTR_IIR_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ga57c276018d0ac606684751e19784457e)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [BMP5_ATTR_POWER_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ga4f6e56a0a4f9fd984d3993cf819281d8)
- [bmp5_powermode](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#gaca06546e057d7295ca4f6ed4298247dc)
- [BMP5_POWERMODE_STANDBY](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ggaca06546e057d7295ca4f6ed4298247dca8f50ab92ba9607eaeed772ddbe92a15f)
- [BMP5_POWERMODE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ggaca06546e057d7295ca4f6ed4298247dcabb75d9c71965843c27724d956ffd1f8c)
- [BMP5_POWERMODE_FORCED](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ggaca06546e057d7295ca4f6ed4298247dcaf57d41b2953f1986618de43ac1315b96)
- [BMP5_POWERMODE_CONTINUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ggaca06546e057d7295ca4f6ed4298247dca14a304e989e6c079c9b6d668b4fd3e57)
- [BMP5_POWERMODE_DEEP_STANDBY](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ggaca06546e057d7295ca4f6ed4298247dca3904b0e3e14b2cad554436ba96fe4bf1)

<a id="header-details"></a>

---

[上一章](P004_zephyr__bluetooth__mesh__blob.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__drivers__clock_control__clock_control_numicro.h_文件参考.md)
