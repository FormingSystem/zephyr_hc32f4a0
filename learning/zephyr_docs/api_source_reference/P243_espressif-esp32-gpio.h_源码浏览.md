---
id: learning.zephyr-docs.api-source-reference.page-243
title: espressif-esp32-gpio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/espressif-esp32-gpio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第243章\_espressif-esp32-gpio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/espressif-esp32-gpio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/espressif-esp32-gpio_8h.html)。

## 243.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>

```c
/*
 * Copyright (c) 2022 Vestas Wind Systems A/S
 * Copyright (c) 2026 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ESPRESSIF_ESP32_GPIO_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ESPRESSIF_ESP32_GPIO_H_

#define ESP32_GPIO_DS_POS 9
#define ESP32_GPIO_DS_MASK (0x3U << ESP32_GPIO_DS_POS)

#define ESP32_GPIO_DS_DFLT (0x0U << ESP32_GPIO_DS_POS)

#define ESP32_GPIO_DS_ALT (0x3U << ESP32_GPIO_DS_POS)



#define ESP32_GPIO_PIN_OUT_EN (1 << 12)

#define ESP32_GPIO_PIN_IN_EN (1 << 13)



#define ESP32_GPIO_SLEEP_HOLD_EN (1 << 14)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ESPRESSIF_ESP32_GPIO_H_ */
```

## 243.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Vestas Wind Systems A/S。

版权（Copyright）：© 2026 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 88 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ESPRESSIF_ESP32_GPIO_H_`。

## 243.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/espressif-esp32-gpio_8h.html)

---

[上一章](P242_espi_realtek_rts5912.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P244_eth_adin2111.h_源码浏览.md)
