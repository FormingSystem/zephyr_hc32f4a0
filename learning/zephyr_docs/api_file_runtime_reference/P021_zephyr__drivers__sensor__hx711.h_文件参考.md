---
id: learning.zephyr-docs.api-file-runtime-reference.page-21
title: zephyr__drivers__sensor__hx711.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hx711_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_drivers\_\_sensor\_\_hx711.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hx711_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HX711传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

HX711传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 21.1\_枚举（Enumerations）

<a id="r_ga16ab3a4dd1f68f004c9c7797c4ec8f54"></a>

```c
enum sensor_channel_hx711 { SENSOR_CHAN_HX711_MASS = SENSOR_CHAN_PRIV_START }
```

相关声明：[sensor_channel_hx711](https://docs.zephyrproject.org/latest/doxygen/html/group__hx711__interface.html#ga16ab3a4dd1f68f004c9c7797c4ec8f54)、[SENSOR_CHAN_HX711_MASS](https://docs.zephyrproject.org/latest/doxygen/html/group__hx711__interface.html#gga16ab3a4dd1f68f004c9c7797c4ec8f54a997baee9556ec5b48df2616cdcf948ed)。

HX711 的自定义传感器通道（Custom Sensor Channels）。

<a id="r_ga33e13fc2924e2c67ff411d8518290c88"></a>

```c
enum sensor_attribute_hx711 { SENSOR_ATTR_HX711_CONV_FACTOR = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_HX711_OFFSET = SENSOR_ATTR_PRIV_START + 1 }
```

相关声明：[sensor_attribute_hx711](https://docs.zephyrproject.org/latest/doxygen/html/group__hx711__interface.html#ga33e13fc2924e2c67ff411d8518290c88)、[SENSOR_ATTR_HX711_CONV_FACTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__hx711__interface.html#gga33e13fc2924e2c67ff411d8518290c88a694d02d0b2176db2d89d74eb000ae6c5)、[SENSOR_ATTR_HX711_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__hx711__interface.html#gga33e13fc2924e2c67ff411d8518290c88ab089a0bc563d1fe0b918749b6b08f801)。

HX711 的自定义传感器属性（Custom Sensor Attributes）。

<a id="r_ga807b05c9730fdb0e79190d8fac16b938"></a>

```c
enum hx711_gain { HX711_GAIN_64 , HX711_GAIN_128 }
```

相关声明：[hx711_gain](https://docs.zephyrproject.org/latest/doxygen/html/group__hx711__interface.html#ga807b05c9730fdb0e79190d8fac16b938)、[HX711_GAIN_64](https://docs.zephyrproject.org/latest/doxygen/html/group__hx711__interface.html#gga807b05c9730fdb0e79190d8fac16b938a5b75889f23c354d713ceb2d60fcece7b)、[HX711_GAIN_128](https://docs.zephyrproject.org/latest/doxygen/html/group__hx711__interface.html#gga807b05c9730fdb0e79190d8fac16b938a6cd55f3c3fd69bac247085ed15058da9)。

下次读取操作（Read Operation）的增益选项（Gain Options）。


## 21.2\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P326_hx711.h_源码浏览.md)
- [sensor_channel_hx711](https://docs.zephyrproject.org/latest/doxygen/html/group__hx711__interface.html#ga16ab3a4dd1f68f004c9c7797c4ec8f54)
- [SENSOR_CHAN_HX711_MASS](https://docs.zephyrproject.org/latest/doxygen/html/group__hx711__interface.html#gga16ab3a4dd1f68f004c9c7797c4ec8f54a997baee9556ec5b48df2616cdcf948ed)
- [sensor_attribute_hx711](https://docs.zephyrproject.org/latest/doxygen/html/group__hx711__interface.html#ga33e13fc2924e2c67ff411d8518290c88)
- [SENSOR_ATTR_HX711_CONV_FACTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__hx711__interface.html#gga33e13fc2924e2c67ff411d8518290c88a694d02d0b2176db2d89d74eb000ae6c5)
- [SENSOR_ATTR_HX711_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__hx711__interface.html#gga33e13fc2924e2c67ff411d8518290c88ab089a0bc563d1fe0b918749b6b08f801)
- [hx711_gain](https://docs.zephyrproject.org/latest/doxygen/html/group__hx711__interface.html#ga807b05c9730fdb0e79190d8fac16b938)
- [HX711_GAIN_64](https://docs.zephyrproject.org/latest/doxygen/html/group__hx711__interface.html#gga807b05c9730fdb0e79190d8fac16b938a5b75889f23c354d713ceb2d60fcece7b)
- [HX711_GAIN_128](https://docs.zephyrproject.org/latest/doxygen/html/group__hx711__interface.html#gga807b05c9730fdb0e79190d8fac16b938a6cd55f3c3fd69bac247085ed15058da9)

<a id="header-details"></a>

---

[上一章](P020_zephyr__bluetooth__mesh__heartbeat.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P022_zephyr__drivers__mfd__infineon_mxcrypto.h_文件参考.md)
