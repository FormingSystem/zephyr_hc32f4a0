---
id: learning.zephyr-docs.api-source-reference.page-176
title: it8xxx2_vcmp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2it8xxx2__vcmp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第176章\_it8xxx2\_vcmp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2it8xxx2__vcmp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2it8xxx2__vcmp_8h.html)。

## 176.1\_原始可见代码（Source Code）

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
<a id="foldopen00016"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="aadc__cmp__npcx_8h_html_a87c321b131ecec52103cc63b22c0018aa8a66a89764bff1e455273a02da29903d"></a>
<a id="aadc__cmp__npcx_8h_html_a87c321b131ecec52103cc63b22c0018aaaaadca90015c5516321259b8921cedc3"></a>
<a id="adrivers_2sensor_2it8xxx2__vcmp_8h_html_acd4ae03345c06203e80ad4f535098165"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3"></a>
<a id="asensor_8h_html"></a>

```c
/*
 * Copyright (c) 2022 ITE Technology Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_IT8XXX2_VCMP_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_IT8XXX2_VCMP_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/drivers/sensor.h>

enum it8xxx2_vcmp_sensor_attribute {
        SENSOR_ATTR_LOWER_VOLTAGE_THRESH = SENSOR_ATTR_PRIV_START,
        SENSOR_ATTR_UPPER_VOLTAGE_THRESH,
};

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_IT8XXX2_VCMP_H_ */
```

## 176.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 ITE Technology Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 25 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_IT8XXX2_VCMP_H_`。

## 176.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2it8xxx2__vcmp_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [it8xxx2_vcmp_sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2it8xxx2__vcmp_8h.html#acd4ae03345c06203e80ad4f535098165)
- [SENSOR_ATTR_LOWER_VOLTAGE_THRESH](https://docs.zephyrproject.org/latest/doxygen/html/adc__cmp__npcx_8h.html#a87c321b131ecec52103cc63b22c0018aa8a66a89764bff1e455273a02da29903d)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [SENSOR_ATTR_UPPER_VOLTAGE_THRESH](https://docs.zephyrproject.org/latest/doxygen/html/adc__cmp__npcx_8h.html#a87c321b131ecec52103cc63b22c0018aaaaadca90015c5516321259b8921cedc3)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P175_icm566xx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P177_lis2dh.h_源码浏览.md)
