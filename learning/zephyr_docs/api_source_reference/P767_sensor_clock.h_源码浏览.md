---
id: learning.zephyr-docs.api-source-reference.page-767
title: sensor_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensor__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第767章\_sensor\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sensor__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sensor__clock_8h.html)。

## 767.1\_原始可见代码（Source Code）

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
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="asensor__clock_8h_html_a337e06f1eecc2700268f803cf2eecefb"></a>
<a id="asensor__clock_8h_html_afe8b63ce73b7a40276996b1ee5408cd6"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>

```c
/*
 * Copyright (c) 2024 Cienet
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_CLOCK_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_CLOCK_H_

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

int sensor_clock_get_cycles(uint64_t *cycles);

uint64_t sensor_clock_cycles_to_ns(uint64_t cycles);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_CLOCK_H_ */
```

## 767.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Cienet。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 45 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_CLOCK_H_`。

## 767.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sensor__clock_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [sensor_clock_get_cycles](https://docs.zephyrproject.org/latest/doxygen/html/sensor__clock_8h.html#a337e06f1eecc2700268f803cf2eecefb)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [sensor_clock_cycles_to_ns](https://docs.zephyrproject.org/latest/doxygen/html/sensor__clock_8h.html#afe8b63ce73b7a40276996b1ee5408cd6)

---

[上一章](P766_sensor_axis_align.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P768_sensor_data_types.h_源码浏览.md)
