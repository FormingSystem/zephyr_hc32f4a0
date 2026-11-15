---
id: learning.zephyr-docs.api-file-supplement-reference.page-110
title: zephyr__drivers__sensor__tle9104.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensor_2tle9104_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第110章\_zephyr\_\_drivers\_\_sensor\_\_tle9104.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sensor_2tle9104_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TLE9104传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

TLE9104传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 110.1\_枚举（Enumerations）

<a id="r_ga24f1803a4c7ab65b58e76f200e2bd62e"></a>

```c
enum sensor_channel_tle9104 { SENSOR_CHAN_TLE9104_OPEN_LOAD = SENSOR_ATTR_PRIV_START , SENSOR_CHAN_TLE9104_OVER_CURRENT }
```

相关声明：[sensor_channel_tle9104](https://docs.zephyrproject.org/latest/doxygen/html/group__tle9104__interface.html#ga24f1803a4c7ab65b58e76f200e2bd62e)、[SENSOR_CHAN_TLE9104_OPEN_LOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__tle9104__interface.html#gga24f1803a4c7ab65b58e76f200e2bd62ea0b1bb727075f758b96fe1b07b94d6002)、[SENSOR_CHAN_TLE9104_OVER_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__tle9104__interface.html#gga24f1803a4c7ab65b58e76f200e2bd62ea12ea98989e21cd00c983ede2b4dd28f2)。

TLE9104 的自定义传感器通道（Custom Sensor Channels）。


## 110.2\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P764_tle9104.h_源码浏览.md)
- [sensor_channel_tle9104](https://docs.zephyrproject.org/latest/doxygen/html/group__tle9104__interface.html#ga24f1803a4c7ab65b58e76f200e2bd62e)
- [SENSOR_CHAN_TLE9104_OPEN_LOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__tle9104__interface.html#gga24f1803a4c7ab65b58e76f200e2bd62ea0b1bb727075f758b96fe1b07b94d6002)
- [SENSOR_CHAN_TLE9104_OVER_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__tle9104__interface.html#gga24f1803a4c7ab65b58e76f200e2bd62ea12ea98989e21cd00c983ede2b4dd28f2)

<a id="header-details"></a>

---

[上一章](P109_zephyr__drivers__sensor__max31790.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P111_zephyr__mgmt__mcumgr__grp__settings_mgmt__settings_mgmt_callbacks.h_文件参考.md)
