---
id: learning.zephyr-docs.api-source-reference.page-656
title: pinctrl_esp32_common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__esp32__common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第656章\_pinctrl\_esp32\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__esp32__common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__esp32__common_8h.html)。

## 656.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00011"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>

```c
/*
 * Copyright (c) 2022-2026 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_ESP32_COMMON_H_
#define ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_ESP32_COMMON_H_


#define ESP32_PIN_NUM(_mux) (((_mux) >> ESP32_PIN_NUM_SHIFT) & ESP32_PIN_NUM_MASK)

#define ESP32_PIN_SIGI(_mux) (((_mux) >> ESP32_PIN_SIGI_SHIFT) & ESP32_PIN_SIGI_MASK)

#define ESP32_PIN_SIGO(_mux) (((_mux) >> ESP32_PIN_SIGO_SHIFT) & ESP32_PIN_SIGO_MASK)

#define ESP32_PIN_BIAS(_cfg) (((_cfg) >> ESP32_PIN_BIAS_SHIFT) & ESP32_PIN_BIAS_MASK)

#define ESP32_PIN_DRV(_cfg) (((_cfg) >> ESP32_PIN_DRV_SHIFT) & ESP32_PIN_DRV_MASK)

#define ESP32_PIN_MODE_OUT(_cfg) (((_cfg) >> ESP32_PIN_OUT_SHIFT) & ESP32_PIN_OUT_MASK)

#define ESP32_PIN_EN_DIR(_cfg) (((_cfg) >> ESP32_PIN_EN_DIR_SHIFT) & ESP32_PIN_EN_DIR_MASK)

#define ESP32_PIN_SLEEP_HOLD(_cfg)                                                                 \
        (((_cfg) >> ESP32_PIN_SLEEP_HOLD_SHIFT) & ESP32_PIN_SLEEP_HOLD_MASK)


#endif /* ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_ESP32_COMMON_H_ */
```

## 656.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022-2026 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 39 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PINCTRL_PINCTRL_ESP32_COMMON_H_`。

## 656.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__esp32__common_8h.html)

---

[上一章](P655_pinctrl-zynq.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P657_pinctrl_nxp_siul2_common.h_源码浏览.md)
