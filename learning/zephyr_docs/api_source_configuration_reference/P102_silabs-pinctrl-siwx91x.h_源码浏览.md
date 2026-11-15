---
id: learning.zephyr-docs.api-source-configuration-reference.page-102
title: silabs-pinctrl-siwx91x.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-siwx91x_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第102章\_silabs-pinctrl-siwx91x.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-siwx91x_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-siwx91x_8h.html)。

## 102.1\_原始可见代码（Source Code）

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
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00033"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="adt-util_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Silicon Laboratories Inc.
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SILABS_PINCTRL_SIWX91X_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SILABS_PINCTRL_SIWX91X_H_

#include <zephyr/dt-bindings/dt-util.h>

#if !defined(FIELD_PREP)
/* Upstream does not make these macros available to DeviceTree */
#define LSB_GET(value)          ((value) & -(value))
#define FIELD_GET(mask, value)  (((value) & (mask)) / LSB_GET(mask))
#define FIELD_PREP(mask, value) (((value) * LSB_GET(mask)) & (mask))
#endif

#define SIWX91X_PINCTRL_PORT_MASK    0x0000000FUL
#define SIWX91X_PINCTRL_PIN_MASK     0x000000F0UL
#define SIWX91X_PINCTRL_ULPPIN_MASK  0x00000F00UL
#define SIWX91X_PINCTRL_MODE_MASK    0x0003F000UL
#define SIWX91X_PINCTRL_ULPMODE_MASK 0x00FC0000UL
#define SIWX91X_PINCTRL_PAD_MASK     0xFF000000UL

/* Declare an integer representing the pinctrl/gpio state of a signal on SiWx91x.
 * @param mode          HP GPIO mode, 0xFF if HP GPIO mux isn't used
 * @param ulpmode       ULP GPIO mode, 0xFF if ULP GPIO mux isn't used
 * @param pad           HP pad number, 0xFF if HP pad isn't used, 0 if host pad
 * @param port          GPIO port number (0-4)
 * @param pin           HP GPIO pin number, value is unused if mode is 0xFF
 * @param ulppin        ULP GPIO pin number, value is unused if ulpmode is 0xFF
 */
#define SIWX91X_GPIO(mode, ulpmode, pad, port, pin, ulppin)                                        \
        (FIELD_PREP(SIWX91X_PINCTRL_PORT_MASK, port) | FIELD_PREP(SIWX91X_PINCTRL_PIN_MASK, pin) | \
         FIELD_PREP(SIWX91X_PINCTRL_ULPPIN_MASK, ulppin) |                                         \
         FIELD_PREP(SIWX91X_PINCTRL_MODE_MASK, mode) |                                             \
         FIELD_PREP(SIWX91X_PINCTRL_ULPMODE_MASK, ulpmode) |                                       \
         FIELD_PREP(SIWX91X_PINCTRL_PAD_MASK, pad))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SILABS_PINCTRL_SIWX91X_H_ */
```

## 102.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Silicon Laboratories Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 12 行

上游没有将这些宏提供给设备树（DeviceTree）使用。

### 注释 3：原第 25 行

声明一个整数，表示 SiWx91x 上某个信号的引脚控制/GPIO 状态。

参数（Parameters）：

- `mode`：高性能（HP）GPIO 模式；未使用 HP GPIO 复用器时为 `0xFF`。
- `ulpmode`：超低功耗（ULP）GPIO 模式；未使用 ULP GPIO 复用器时为 `0xFF`。
- `pad`：HP 焊盘（Pad）编号；未使用 HP 焊盘时为 `0xFF`，主机焊盘时为 0。
- `port`：GPIO 端口编号，范围为 0–4。
- `pin`：HP GPIO 引脚编号；`mode` 为 `0xFF` 时不使用此值。
- `ulppin`：ULP GPIO 引脚编号；`ulpmode` 为 `0xFF` 时不使用此值。

### 注释 4：原第 40 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SILABS_PINCTRL_SIWX91X_H_`。

## 102.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-siwx91x_8h.html)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P101_silabs-acmp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P103_six301-clock.h_源码浏览.md)
