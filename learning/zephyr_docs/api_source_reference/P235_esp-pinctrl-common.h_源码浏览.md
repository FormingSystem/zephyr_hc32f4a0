---
id: learning.zephyr-docs.api-source-reference.page-235
title: esp-pinctrl-common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp-pinctrl-common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第235章\_esp-pinctrl-common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/esp-pinctrl-common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/esp-pinctrl-common_8h.html)。

## 235.1\_原始可见代码（Source Code）

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
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00094"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="adt-util_8h_html"></a>

```c
/*
 * Copyright (c) 2022-2026 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP_PINCTRL_COMMON_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP_PINCTRL_COMMON_H_

#include <zephyr/dt-bindings/dt-util.h>

#define ESP32_PIN_NUM_SHIFT 0U
#define ESP32_PIN_NUM_MASK  0x3FU

#define ESP32_PIN_SIGI_MASK  0x1FFU
#define ESP32_PIN_SIGI_SHIFT 6U
#define ESP32_PIN_SIGO_MASK  0x1FFU
#define ESP32_PIN_SIGO_SHIFT 15U
#define ESP_SIG_INVAL        ESP32_PIN_SIGI_MASK

#define ESP32_PINMUX(pin, sig_i, sig_o)                                                            \
        (((pin & ESP32_PIN_NUM_MASK) << ESP32_PIN_NUM_SHIFT) |                                     \
         ((sig_i & ESP32_PIN_SIGI_MASK) << ESP32_PIN_SIGI_SHIFT) |                                 \
         ((sig_o & ESP32_PIN_SIGO_MASK) << ESP32_PIN_SIGO_SHIFT))

#define ESP32_RMII_SLOT_SHIFT 24U
#define ESP32_RMII_SLOT_MASK  0xFU
#define ESP32_RMII_MARKER     BIT(30)

#define ESP_RMII_CLK        0
#define ESP_RMII_TX_EN      1
#define ESP_RMII_TXD0       2
#define ESP_RMII_TXD1       3
#define ESP_RMII_CRS_DV     4
#define ESP_RMII_RXD0       5
#define ESP_RMII_RXD1       6
#define ESP_RMII_SLOT_COUNT 7

#define ESP32_RMII_PINMUX(pin, slot)                                                               \
        (ESP32_RMII_MARKER | (((slot) & ESP32_RMII_SLOT_MASK) << ESP32_RMII_SLOT_SHIFT) |          \
         (((pin) & ESP32_PIN_NUM_MASK) << ESP32_PIN_NUM_SHIFT))


#define ESP32_PIN_BIAS_SHIFT       0U
#define ESP32_PIN_BIAS_MASK        0x3U
#define ESP32_PIN_DRV_SHIFT        2U
#define ESP32_PIN_DRV_MASK         0x3U
#define ESP32_PIN_OUT_SHIFT        4U
#define ESP32_PIN_OUT_MASK         0x3U
#define ESP32_PIN_EN_DIR_SHIFT     6U
#define ESP32_PIN_EN_DIR_MASK      0x3U
#define ESP32_PIN_SLEEP_HOLD_SHIFT 8U
#define ESP32_PIN_SLEEP_HOLD_MASK  0x1U

#define ESP32_NO_PULL   0x1
#define ESP32_PULL_UP   0x2
#define ESP32_PULL_DOWN 0x3

#define ESP32_PUSH_PULL  0x1
#define ESP32_OPEN_DRAIN 0x2

#define ESP32_PIN_OUT_HIGH 0x1
#define ESP32_PIN_OUT_LOW  0x2

#define ESP32_PIN_OUT_EN 0x1
#define ESP32_PIN_IN_EN  0x2

#define ESP32_PIN_SLEEP_HOLD_EN 0x1

#define ESP32_NO_PULL_FLAG      BIT(0)
#define ESP32_PULL_UP_FLAG      BIT(1)
#define ESP32_PULL_DOWN_FLAG    BIT(2)
#define ESP32_PUSH_PULL_FLAG    BIT(3)
#define ESP32_OPEN_DRAIN_FLAG   BIT(4)
#define ESP32_DIR_INP_FLAG      BIT(5)
#define ESP32_DIR_OUT_FLAG      BIT(6)
#define ESP32_PIN_OUT_HIGH_FLAG BIT(7)
#define ESP32_PIN_OUT_LOW_FLAG  BIT(8)
#define ESP32_PIN_OUT_EN_FLAG   BIT(9)
#define ESP32_PIN_IN_EN_FLAG    BIT(10)
#define ESP32_SLEEP_HOLD_FLAG   BIT(11)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP_PINCTRL_COMMON_H_ */
```

## 235.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022-2026 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 174 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP_PINCTRL_COMMON_H_`。

## 235.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/esp-pinctrl-common_8h.html)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P234_esp-esp32c61-intmux.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P236_esp32c2-gpio-sigmap.h_源码浏览.md)
