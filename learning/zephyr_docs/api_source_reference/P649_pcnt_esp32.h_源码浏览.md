---
id: learning.zephyr-docs.api-source-reference.page-649
title: pcnt_esp32.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pcnt__esp32_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第649章\_pcnt\_esp32.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pcnt__esp32_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pcnt__esp32_8h.html)。

## 649.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00022"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3"></a>
<a id="apcnt__esp32_8h_html_a72fbc07d3bc92e1bfbba0c4aa47edbc8"></a>
<a id="apcnt__esp32_8h_html_a72fbc07d3bc92e1bfbba0c4aa47edbc8a29611b47f17dbee835dc48e8aedfc9d4"></a>
<a id="asensor_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_PCNT_ESP32_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_PCNT_ESP32_H_

#include <zephyr/drivers/sensor.h>


#define SENSOR_CHAN_PCNT_ESP32_UNIT(n) ((enum sensor_channel)(SENSOR_CHAN_PRIV_START + (n)))

enum sensor_attribute_pcnt_esp32 {
        SENSOR_ATTR_PCNT_ESP32_RESET = SENSOR_ATTR_PRIV_START,
};

#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_PCNT_ESP32_H_ */
```

## 649.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 44 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_PCNT_ESP32_H_`。

## 649.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pcnt__esp32_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_attribute_pcnt_esp32](https://docs.zephyrproject.org/latest/doxygen/html/pcnt__esp32_8h.html#a72fbc07d3bc92e1bfbba0c4aa47edbc8)
- [SENSOR_ATTR_PCNT_ESP32_RESET](https://docs.zephyrproject.org/latest/doxygen/html/pcnt__esp32_8h.html#a72fbc07d3bc92e1bfbba0c4aa47edbc8a29611b47f17dbee835dc48e8aedfc9d4)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P648_pca9422.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P650_pinctrl-ra.h_源码浏览.md)
