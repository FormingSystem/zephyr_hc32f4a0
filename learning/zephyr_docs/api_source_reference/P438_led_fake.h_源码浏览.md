---
id: learning.zephyr-docs.api-source-reference.page-438
title: led_fake.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/led__fake_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第438章\_led\_fake.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/led__fake_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/led__fake_8h.html)。

## 438.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="adrivers_2led_8h_html"></a>
<a id="agroup__led__fake_html_ga1860bf2d9d105ee8ecb7a092e2017b63"></a>
<a id="agroup__led__fake_html_ga276f41b4376784bf588d7785afdffd56"></a>
<a id="agroup__led__fake_html_ga4475c7869fd8ab92c5b7fea4ec3c1a3d"></a>
<a id="agroup__led__fake_html_ga68b14d1f205726941cb591f177ef89af"></a>
<a id="agroup__led__fake_html_gab6d86a816ed9dcd8d393126a8dc3d2dd"></a>
<a id="agroup__led__fake_html_gacf6109ac62eafca13ab6b56fb4676877"></a>
<a id="agroup__led__fake_html_gae4f88da2cfa43c93bc0f2d294b6f848e"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructled__info_html"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 Henrik Brix Andersen <henrik@brixandersen.dk>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_LED_LED_FAKE_H_
#define ZEPHYR_INCLUDE_DRIVERS_LED_LED_FAKE_H_

#include <zephyr/drivers/led.h>
#include <zephyr/fff.h>

#ifdef __cplusplus
extern "C" {
#endif


DECLARE_FAKE_VALUE_FUNC(int, fake_led_on, const struct device *, uint32_t);

DECLARE_FAKE_VALUE_FUNC(int, fake_led_off, const struct device *, uint32_t);

DECLARE_FAKE_VALUE_FUNC(int, fake_led_set_brightness, const struct device *, uint32_t, uint8_t);

DECLARE_FAKE_VALUE_FUNC(int, fake_led_blink, const struct device *, uint32_t, uint32_t, uint32_t);

DECLARE_FAKE_VALUE_FUNC(int, fake_led_get_info, const struct device *, uint32_t,
                        const struct led_info **);

DECLARE_FAKE_VALUE_FUNC(int, fake_led_set_color, const struct device *, uint32_t, uint8_t,
                        const uint8_t *);

DECLARE_FAKE_VALUE_FUNC(int, fake_led_write_channels, const struct device *, uint32_t, uint32_t,
                        const uint8_t *);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_LED_LED_FAKE_H_ */
```

## 438.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 Henrik Brix Andersen <henrik@brixandersen.dk>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 81 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_LED_LED_FAKE_H_`。

## 438.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/led__fake_8h.html)
- [zephyr/drivers/led.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2led_8h.html)
- [fake_led_on](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#gab6d86a816ed9dcd8d393126a8dc3d2dd)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [fake_led_off](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#ga4475c7869fd8ab92c5b7fea4ec3c1a3d)
- [fake_led_set_brightness](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#ga68b14d1f205726941cb591f177ef89af)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [fake_led_blink](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#ga276f41b4376784bf588d7785afdffd56)
- [fake_led_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#gae4f88da2cfa43c93bc0f2d294b6f848e)
- [led_info](../hardware/P204_LED信息结构.md)
- [fake_led_set_color](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#ga1860bf2d9d105ee8ecb7a092e2017b63)
- [fake_led_write_channels](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#gacf6109ac62eafca13ab6b56fb4676877)
- [led.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2led_8h.html)

---

[上一章](P437_lc3.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P439_transceiver.h_源码浏览.md)
