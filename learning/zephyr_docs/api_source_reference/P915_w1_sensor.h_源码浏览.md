---
id: learning.zephyr-docs.api-source-reference.page-915
title: w1_sensor.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/w1__sensor_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第915章\_w1\_sensor.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/w1__sensor_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/w1__sensor_8h.html)。

## 915.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00015"></a>
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
<a id="l00033"></a>
<a id="foldopen00037"></a>
<a id="l00037"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00059"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="foldopen00072"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3"></a>
<a id="agroup__sys-util_html_ga1a138896caafcb2429a6483ea7412d12"></a>
<a id="agroup__w1__sensor_html_ga3c0b20580be768bcc45f93a4c01ee9db"></a>
<a id="agroup__w1__sensor_html_ga947aea2687107b1b3471c3e9eded7504"></a>
<a id="agroup__w1__sensor_html_gae6c6848f94bde562a95f5f987a8c76fc"></a>
<a id="agroup__w1__sensor_html_ggae6c6848f94bde562a95f5f987a8c76fcaa5456effd0254882ece02da5d25cec36"></a>
<a id="asensor_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructsensor__value_html"></a>
<a id="astructsensor__value_html_a91f81bd0f5da69084cf3c629fde68a1b"></a>
<a id="astructsensor__value_html_af21dddb084da4c42a7e77b48edf26fbe"></a>
<a id="astructw1__rom_html"></a>
<a id="asys_2byteorder_8h_html_a3e0d2e4e85249497011f5f9ea0d2987c"></a>
<a id="asys_2byteorder_8h_html_ad8e00ff5c0b9e394291936d1a570c215"></a>
<a id="aw1_8h_html"></a>

```c
/*
 * Copyright (c) 2022, Thomas Stranger
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_W1_SENSOR_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_W1_SENSOR_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/drivers/sensor.h>
#include <zephyr/drivers/w1.h>


enum sensor_attribute_w1 {
        SENSOR_ATTR_W1_ROM = SENSOR_ATTR_PRIV_START,
};

static inline void w1_rom_to_sensor_value(const struct w1_rom *rom,
                                          struct sensor_value *val)
{
        val->val1 = sys_get_be64((uint8_t *)rom) & BIT64_MASK(32);
        val->val2 = sys_get_be64((uint8_t *)rom) >> 32;
}

static inline void w1_sensor_value_to_rom(const struct sensor_value *val,
                                          struct w1_rom *rom)
{
        uint64_t temp64 = ((uint64_t)((uint32_t)val->val2) << 32)
                          | (uint32_t)val->val1;
        sys_put_be64(temp64, (uint8_t *)rom);
}


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_W1_SENSOR_H_ */
```

## 915.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022, Thomas Stranger。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 88 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_W1_SENSOR_H_`。

## 915.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/w1__sensor_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [zephyr/drivers/w1.h](../peripheral_bus_storage_header_reference/P029_zephyr__drivers__w1.h_头文件参考.md)
- [sensor_attribute_w1](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html#gae6c6848f94bde562a95f5f987a8c76fc)
- [SENSOR_ATTR_W1_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html#ggae6c6848f94bde562a95f5f987a8c76fcaa5456effd0254882ece02da5d25cec36)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [w1_rom_to_sensor_value](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html#ga947aea2687107b1b3471c3e9eded7504)
- [w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)
- [sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)
- [val1](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#af21dddb084da4c42a7e77b48edf26fbe)
- [sys_get_be64](../byteorder_reference/P001_系统字节序头文件参考.md#ad8e00ff5c0b9e394291936d1a570c215)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BIT64_MASK](../util_reference/P001_通用工具公共接口.md#ga1a138896caafcb2429a6483ea7412d12)
- [val2](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#a91f81bd0f5da69084cf3c629fde68a1b)
- [w1_sensor_value_to_rom](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html#ga3c0b20580be768bcc45f93a4c01ee9db)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sys_put_be64](../byteorder_reference/P001_系统字节序头文件参考.md#a3e0d2e4e85249497011f5f9ea0d2987c)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_value::val2](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#a91f81bd0f5da69084cf3c629fde68a1b)
- [sensor_value::val1](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#af21dddb084da4c42a7e77b48edf26fbe)
- [w1.h](../peripheral_bus_storage_header_reference/P029_zephyr__drivers__w1.h_头文件参考.md)

---

[上一章](P914_vocs.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P916_websocket.h_源码浏览.md)
