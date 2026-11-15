---
id: learning.zephyr-docs.api-file-configuration-reference.page-25
title: zephyr__drivers__sensor__ens160.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ens160_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_zephyr\_\_drivers\_\_sensor\_\_ens160.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ens160_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ENS160传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

ENS160传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 25.1\_枚举（Enumerations）

<a id="r_ga8d2ba05aa65d222313abb94ea4fbc0a5"></a>

```c
enum sensor_channel_ens160 { SENSOR_CHAN_ENS160_AQI = SENSOR_CHAN_PRIV_START }
```

相关声明：[sensor_channel_ens160](https://docs.zephyrproject.org/latest/doxygen/html/group__ens160__interface.html#ga8d2ba05aa65d222313abb94ea4fbc0a5)、[SENSOR_CHAN_ENS160_AQI](https://docs.zephyrproject.org/latest/doxygen/html/group__ens160__interface.html#gga8d2ba05aa65d222313abb94ea4fbc0a5ac57da55fa36fe09123bba287ea6fef56)。

ENS160 的自定义传感器通道（Custom Sensor Channels）。

<a id="r_ga8005c12c1132ce8b76bd571035a37836"></a>

```c
enum sensor_attribute_ens160 { SENSOR_ATTR_ENS160_TEMP = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_ENS160_RH }
```

相关声明：[sensor_attribute_ens160](https://docs.zephyrproject.org/latest/doxygen/html/group__ens160__interface.html#ga8005c12c1132ce8b76bd571035a37836)、[SENSOR_ATTR_ENS160_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__ens160__interface.html#gga8005c12c1132ce8b76bd571035a37836a09b24e7aae253d6e4ee71fd57e0347be)、[SENSOR_ATTR_ENS160_RH](https://docs.zephyrproject.org/latest/doxygen/html/group__ens160__interface.html#gga8005c12c1132ce8b76bd571035a37836a23a397dcaad8efe37bc66aa54bfd3608)。

ENS160 的自定义传感器属性（Custom Sensor Attributes）。


## 25.2\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P229_ens160.h_源码浏览.md)
- [sensor_channel_ens160](https://docs.zephyrproject.org/latest/doxygen/html/group__ens160__interface.html#ga8d2ba05aa65d222313abb94ea4fbc0a5)
- [SENSOR_CHAN_ENS160_AQI](https://docs.zephyrproject.org/latest/doxygen/html/group__ens160__interface.html#gga8d2ba05aa65d222313abb94ea4fbc0a5ac57da55fa36fe09123bba287ea6fef56)
- [sensor_attribute_ens160](https://docs.zephyrproject.org/latest/doxygen/html/group__ens160__interface.html#ga8005c12c1132ce8b76bd571035a37836)
- [SENSOR_ATTR_ENS160_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__ens160__interface.html#gga8005c12c1132ce8b76bd571035a37836a09b24e7aae253d6e4ee71fd57e0347be)
- [SENSOR_ATTR_ENS160_RH](https://docs.zephyrproject.org/latest/doxygen/html/group__ens160__interface.html#gga8005c12c1132ce8b76bd571035a37836a23a397dcaad8efe37bc66aa54bfd3608)

<a id="header-details"></a>

---

[上一章](P024_zephyr__drivers__emul_stub_device.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P026_zephyr__drivers__sensor__fcx_mldx5.h_文件参考.md)
