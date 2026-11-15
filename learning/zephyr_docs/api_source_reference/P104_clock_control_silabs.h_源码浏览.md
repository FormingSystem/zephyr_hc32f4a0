---
id: learning.zephyr-docs.api-source-reference.page-104
title: clock_control_silabs.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__silabs_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第104章\_clock\_control\_silabs.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__silabs_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__silabs_8h.html)。

## 104.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="foldopen00045"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="foldopen00079"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="aclock__control_8h_html"></a>
<a id="asix301-clock_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructsilabs__clock__control__cmu__config_html"></a>
<a id="astructsilabs__clock__control__cmu__config_html_a5792da0cf4363d3127cff97562763f45"></a>
<a id="astructsilabs__clock__control__cmu__config_html_a8e9a65a261eae1fefcf0d697a8a59bf9"></a>
<a id="axg21-clock_8h_html"></a>
<a id="axg22-clock_8h_html"></a>
<a id="axg23-clock_8h_html"></a>
<a id="axg24-clock_8h_html"></a>
<a id="axg26-clock_8h_html"></a>
<a id="axg27-clock_8h_html"></a>
<a id="axg28-clock_8h_html"></a>
<a id="axg29-clock_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Silicon Laboratories Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_SILABS_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_SILABS_H_

#include <zephyr/drivers/clock_control.h>


#if defined(CONFIG_SOC_FAMILY_SILABS_S2_XG21)
#include <zephyr/dt-bindings/clock/silabs/xg21-clock.h>
#elif defined(CONFIG_SOC_FAMILY_SILABS_S2_XG22)
#include <zephyr/dt-bindings/clock/silabs/xg22-clock.h>
#elif defined(CONFIG_SOC_FAMILY_SILABS_S2_XG23)
#include <zephyr/dt-bindings/clock/silabs/xg23-clock.h>
#elif defined(CONFIG_SOC_FAMILY_SILABS_S2_XG24)
#include <zephyr/dt-bindings/clock/silabs/xg24-clock.h>
#elif defined(CONFIG_SOC_FAMILY_SILABS_S2_XG26)
#include <zephyr/dt-bindings/clock/silabs/xg26-clock.h>
#elif defined(CONFIG_SOC_FAMILY_SILABS_S2_XG27)
#include <zephyr/dt-bindings/clock/silabs/xg27-clock.h>
#elif defined(CONFIG_SOC_FAMILY_SILABS_S2_XG28)
#include <zephyr/dt-bindings/clock/silabs/xg28-clock.h>
#elif defined(CONFIG_SOC_FAMILY_SILABS_S2_XG29)
#include <zephyr/dt-bindings/clock/silabs/xg29-clock.h>
#elif defined(CONFIG_SOC_FAMILY_SILABS_S3_SIX301)
#include <zephyr/dt-bindings/clock/silabs/six301-clock.h>
#endif

struct silabs_clock_control_cmu_config {
        uint32_t bus_clock;
        uint8_t branch;
};

#define SILABS_DT_CLOCK_CFG(node_id)                                                               \
        {                                                                                          \
                .bus_clock = DT_CLOCKS_CELL(node_id, enable),                                      \
                .branch = DT_CLOCKS_CELL(node_id, branch),                                         \
        }

#define SILABS_DT_INST_CLOCK_CFG(inst)                                                             \
        {                                                                                          \
                .bus_clock = DT_INST_CLOCKS_CELL(inst, enable),                                    \
                .branch = DT_INST_CLOCKS_CELL(inst, branch),                                       \
        }

#define SILABS_DT_CLOCK_CFG_BY_NAME(node_id, name)                                                 \
        {                                                                                          \
                .bus_clock = DT_CLOCKS_CELL_BY_NAME(node_id, name, enable),                        \
                .branch = DT_CLOCKS_CELL_BY_NAME(node_id, name, branch),                           \
        }


#define SILABS_DT_INST_CLOCK_CFG_BY_NAME(inst, name)                                               \
        {                                                                                          \
                .bus_clock = DT_INST_CLOCKS_CELL_BY_NAME(inst, name, enable),                      \
                .branch = DT_INST_CLOCKS_CELL_BY_NAME(inst, name, branch),                         \
        }


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_SILABS_H_ */
```

## 104.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Silicon Laboratories Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 101 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_CLOCK_CONTROL_SILABS_H_`。

## 104.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__silabs_8h.html)
- [zephyr/drivers/clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [zephyr/dt-bindings/clock/silabs/xg21-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/xg21-clock_8h.html)
- [zephyr/dt-bindings/clock/silabs/xg22-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/xg22-clock_8h.html)
- [zephyr/dt-bindings/clock/silabs/xg23-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/xg23-clock_8h.html)
- [zephyr/dt-bindings/clock/silabs/xg24-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/xg24-clock_8h.html)
- [zephyr/dt-bindings/clock/silabs/xg26-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/xg26-clock_8h.html)
- [zephyr/dt-bindings/clock/silabs/xg27-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/xg27-clock_8h.html)
- [zephyr/dt-bindings/clock/silabs/xg28-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/xg28-clock_8h.html)
- [zephyr/dt-bindings/clock/silabs/xg29-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/xg29-clock_8h.html)
- [zephyr/dt-bindings/clock/silabs/six301-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/six301-clock_8h.html)
- [silabs_clock_control_cmu_config](../device_power_control_model_reference/P087_silabs_clock_control_cmu_config_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bus_clock](../device_power_control_model_reference/P087_silabs_clock_control_cmu_config_结构体.md#a5792da0cf4363d3127cff97562763f45)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [branch](../device_power_control_model_reference/P087_silabs_clock_control_cmu_config_结构体.md#a8e9a65a261eae1fefcf0d697a8a59bf9)
- [clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [six301-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/six301-clock_8h.html)
- [silabs_clock_control_cmu_config::bus_clock](../device_power_control_model_reference/P087_silabs_clock_control_cmu_config_结构体.md#a5792da0cf4363d3127cff97562763f45)
- [silabs_clock_control_cmu_config::branch](../device_power_control_model_reference/P087_silabs_clock_control_cmu_config_结构体.md#a8e9a65a261eae1fefcf0d697a8a59bf9)
- [xg21-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/xg21-clock_8h.html)
- [xg22-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/xg22-clock_8h.html)
- [xg23-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/xg23-clock_8h.html)
- [xg24-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/xg24-clock_8h.html)
- [xg26-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/xg26-clock_8h.html)
- [xg27-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/xg27-clock_8h.html)
- [xg28-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/xg28-clock_8h.html)
- [xg29-clock.h](https://docs.zephyrproject.org/latest/doxygen/html/xg29-clock_8h.html)

---

[上一章](P103_clock_control_rpi_pico.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P105_clock_control_silabs_siwx91x.h_源码浏览.md)
