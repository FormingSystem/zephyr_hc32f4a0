---
id: learning.zephyr-docs.api-file-management-reference.page-11
title: zephyr__drivers__sensor__tmag5273.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2tmag5273_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_drivers\_\_sensor\_\_tmag5273.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2tmag5273_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TMAG5273传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

TMAG5273传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 角度计算模式（Angle calculation modes）

<a id="r_ga6426061b7a7f444ba7f4d87477144bf0"></a>

```c
#define TMAG5273_ANGLE_CALC_NONE 0
```

相关声明：[TMAG5273_ANGLE_CALC_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga6426061b7a7f444ba7f4d87477144bf0)。

不进行角度计算（angle calculation）。

<a id="r_gac93519e03635876d3b693a0b4a11904a"></a>

```c
#define TMAG5273_ANGLE_CALC_XY 1
```

相关声明：[TMAG5273_ANGLE_CALC_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gac93519e03635876d3b693a0b4a11904a)。

先 X，后 Y。

<a id="r_ga863266f03d298268103d394eb37bbac9"></a>

```c
#define TMAG5273_ANGLE_CALC_YZ 2
```

相关声明：[TMAG5273_ANGLE_CALC_YZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga863266f03d298268103d394eb37bbac9)。

先 Y，后 Z。

<a id="r_ga84e780517b8fec1845fd145dd0b16f0c"></a>

```c
#define TMAG5273_ANGLE_CALC_XZ 3
```

相关声明：[TMAG5273_ANGLE_CALC_XZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga84e780517b8fec1845fd145dd0b16f0c)。

先 X，后 Z。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.2\_枚举（Enumerations）

<a id="r_ga3d91dbb6bc6d7dc90ed889651bc34827"></a>

```c
enum tmag5273_sensor_channel { TMAG5273_CHAN_MAGNITUDE = SENSOR_CHAN_PRIV_START , TMAG5273_CHAN_MAGNITUDE_MSB , TMAG5273_CHAN_ANGLE_MAGNITUDE }
```

相关声明：[tmag5273_sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga3d91dbb6bc6d7dc90ed889651bc34827)、[TMAG5273_CHAN_MAGNITUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gga3d91dbb6bc6d7dc90ed889651bc34827a72c52112337e191ab9ce906aecdff92d)、[TMAG5273_CHAN_MAGNITUDE_MSB](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gga3d91dbb6bc6d7dc90ed889651bc34827a601dad57092c442da3a0a184737d8003)、[TMAG5273_CHAN_ANGLE_MAGNITUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gga3d91dbb6bc6d7dc90ed889651bc34827a2c4ff267102871c1d23353bbb6b30dbc)。

TMAG5273 支持的附加通道（additional channels）。

<a id="r_ga6fadcd6cd3b5fbc9281d27f37bdfe0a2"></a>

```c
enum tmag5273_attribute { TMAG5273_ATTR_ANGLE_MAG_AXIS = SENSOR_ATTR_PRIV_START }
```

相关声明：[tmag5273_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga6fadcd6cd3b5fbc9281d27f37bdfe0a2)、[TMAG5273_ATTR_ANGLE_MAG_AXIS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gga6fadcd6cd3b5fbc9281d27f37bdfe0a2af59c66f9794efa1afa7d7461a134d3d3)。

TMAG5273 支持的附加属性（additional attributes）。


## 11.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P045_tmag5273.h_源码浏览.md)
- [TMAG5273_ANGLE_CALC_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga6426061b7a7f444ba7f4d87477144bf0)
- [TMAG5273_ANGLE_CALC_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gac93519e03635876d3b693a0b4a11904a)
- [TMAG5273_ANGLE_CALC_YZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga863266f03d298268103d394eb37bbac9)
- [TMAG5273_ANGLE_CALC_XZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga84e780517b8fec1845fd145dd0b16f0c)
- [tmag5273_sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga3d91dbb6bc6d7dc90ed889651bc34827)
- [TMAG5273_CHAN_MAGNITUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gga3d91dbb6bc6d7dc90ed889651bc34827a72c52112337e191ab9ce906aecdff92d)
- [TMAG5273_CHAN_MAGNITUDE_MSB](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gga3d91dbb6bc6d7dc90ed889651bc34827a601dad57092c442da3a0a184737d8003)
- [TMAG5273_CHAN_ANGLE_MAGNITUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gga3d91dbb6bc6d7dc90ed889651bc34827a2c4ff267102871c1d23353bbb6b30dbc)
- [tmag5273_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga6fadcd6cd3b5fbc9281d27f37bdfe0a2)
- [TMAG5273_ATTR_ANGLE_MAG_AXIS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gga6fadcd6cd3b5fbc9281d27f37bdfe0a2af59c66f9794efa1afa7d7461a134d3d3)

<a id="header-details"></a>

---

[上一章](P010_zephyr__drivers__mfd__npm2100.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__drivers__haptics__drv2605.h_文件参考.md)
