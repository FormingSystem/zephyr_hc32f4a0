---
id: learning.zephyr-docs.api-file-supplement-reference.page-57
title: zephyr__drivers__sensor__lm95234.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lm95234_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_zephyr\_\_drivers\_\_sensor\_\_lm95234.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lm95234_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LM95234传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

LM95234传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 57.1\_枚举（Enumerations）

<a id="r_gac9be5b7dd4705d9a2de2ca102943637d"></a>

```c
enum sensor_channel_lm95234 { SENSOR_CHAN_LM95234_REMOTE_TEMP_1 = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_LM95234_REMOTE_TEMP_2 , SENSOR_CHAN_LM95234_REMOTE_TEMP_3 , SENSOR_CHAN_LM95234_REMOTE_TEMP_4 }
```

相关声明：[sensor_channel_lm95234](https://docs.zephyrproject.org/latest/doxygen/html/group__lm95234__interface.html#gac9be5b7dd4705d9a2de2ca102943637d)、[SENSOR_CHAN_LM95234_REMOTE_TEMP_1](https://docs.zephyrproject.org/latest/doxygen/html/group__lm95234__interface.html#ggac9be5b7dd4705d9a2de2ca102943637dae4c495a1c560dc22899d5fbfdbfe3818)、[SENSOR_CHAN_LM95234_REMOTE_TEMP_2](https://docs.zephyrproject.org/latest/doxygen/html/group__lm95234__interface.html#ggac9be5b7dd4705d9a2de2ca102943637da11ccf81167550f39556fb0bfbed7e214)、[SENSOR_CHAN_LM95234_REMOTE_TEMP_3](https://docs.zephyrproject.org/latest/doxygen/html/group__lm95234__interface.html#ggac9be5b7dd4705d9a2de2ca102943637da7256e03d9f0e5177af20880193348d4a)、[SENSOR_CHAN_LM95234_REMOTE_TEMP_4](https://docs.zephyrproject.org/latest/doxygen/html/group__lm95234__interface.html#ggac9be5b7dd4705d9a2de2ca102943637da395619c35328ae6fbc2d7b8d3517a2b8)。

LM95234 的自定义传感器通道（Custom Sensor Channels）。


## 57.2\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P448_lm95234.h_源码浏览.md)
- [sensor_channel_lm95234](https://docs.zephyrproject.org/latest/doxygen/html/group__lm95234__interface.html#gac9be5b7dd4705d9a2de2ca102943637d)
- [SENSOR_CHAN_LM95234_REMOTE_TEMP_1](https://docs.zephyrproject.org/latest/doxygen/html/group__lm95234__interface.html#ggac9be5b7dd4705d9a2de2ca102943637dae4c495a1c560dc22899d5fbfdbfe3818)
- [SENSOR_CHAN_LM95234_REMOTE_TEMP_2](https://docs.zephyrproject.org/latest/doxygen/html/group__lm95234__interface.html#ggac9be5b7dd4705d9a2de2ca102943637da11ccf81167550f39556fb0bfbed7e214)
- [SENSOR_CHAN_LM95234_REMOTE_TEMP_3](https://docs.zephyrproject.org/latest/doxygen/html/group__lm95234__interface.html#ggac9be5b7dd4705d9a2de2ca102943637da7256e03d9f0e5177af20880193348d4a)
- [SENSOR_CHAN_LM95234_REMOTE_TEMP_4](https://docs.zephyrproject.org/latest/doxygen/html/group__lm95234__interface.html#ggac9be5b7dd4705d9a2de2ca102943637da395619c35328ae6fbc2d7b8d3517a2b8)

<a id="header-details"></a>

---

[上一章](P056_zephyr__bluetooth__mesh__large_comp_data_srv.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P058_zephyr__drivers__clock_control__lpc11u6x_clock_control.h_文件参考.md)
