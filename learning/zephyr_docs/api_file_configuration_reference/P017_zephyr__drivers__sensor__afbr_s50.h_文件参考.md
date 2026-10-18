---
id: learning.zephyr-docs.api-file-configuration-reference.page-17
title: zephyr__drivers__sensor__afbr_s50.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2afbr__s50_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_drivers\_\_sensor\_\_afbr\_s50.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2afbr__s50_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

AFBR-S50传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

AFBR-S50传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 17.1\_宏定义（Macros）

<a id="r_ga026e02d538d6e283b7b1136470e6e478"></a>

```c
#define AFBR_PIXEL_INVALID_VALUE 0x80000000
```

相关声明：[AFBR_PIXEL_INVALID_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__afbr__s50__interface.html#ga026e02d538d6e283b7b1136470e6e478)。

若像素读数（Pixel Reading）包含此值，则忽略该读数。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 17.2\_枚举（Enumerations）

<a id="r_ga2be1db0094a49e8e59310b8c8137e54f"></a>

```c
enum sensor_channel_afbr_s50 { SENSOR_CHAN_AFBR_S50_PIXELS = SENSOR_CHAN_PRIV_START + 1 }
```

相关声明：[sensor_channel_afbr_s50](https://docs.zephyrproject.org/latest/doxygen/html/group__afbr__s50__interface.html#ga2be1db0094a49e8e59310b8c8137e54f)、[SENSOR_CHAN_AFBR_S50_PIXELS](https://docs.zephyrproject.org/latest/doxygen/html/group__afbr__s50__interface.html#gga2be1db0094a49e8e59310b8c8137e54fa46394738feb65f3bcc76ecd343448de7)。

AFBR-S50 的自定义传感器通道（Custom Sensor Channels）。


## 17.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P173_afbr_s50.h_源码浏览.md)
- [AFBR_PIXEL_INVALID_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__afbr__s50__interface.html#ga026e02d538d6e283b7b1136470e6e478)
- [sensor_channel_afbr_s50](https://docs.zephyrproject.org/latest/doxygen/html/group__afbr__s50__interface.html#ga2be1db0094a49e8e59310b8c8137e54f)
- [SENSOR_CHAN_AFBR_S50_PIXELS](https://docs.zephyrproject.org/latest/doxygen/html/group__afbr__s50__interface.html#gga2be1db0094a49e8e59310b8c8137e54fa46394738feb65f3bcc76ecd343448de7)

<a id="header-details"></a>

---

[上一章](P016_zephyr__drivers__dma__dma_smartbond.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P018_zephyr__drivers__sensor__lis2dh.h_文件参考.md)
