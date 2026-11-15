---
id: learning.zephyr-docs.api-source-supplement-reference.page-178
title: silabs-pinctrl-dbus.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-dbus_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第178章\_silabs-pinctrl-dbus.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-dbus_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-dbus_8h.html)。

## 178.1\_原始可见代码（Source Code）

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
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="adt-util_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Silicon Labs
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SILABS_PINCTRL_DBUS_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SILABS_PINCTRL_DBUS_H_

#include <zephyr/dt-bindings/dt-util.h>

/*
 * Silabs Series 2 DBUS configuration is encoded in a 32-bit bitfield organized as follows:
 *
 * 31    : Whether the configuration represents an analog pin
 * If digital (bit 31 == 0):
 * 30    : Reserved
 * 29    : Route register presence (fixed routes have no route register)
 * 28..24: Route register offset in words from peripheral config (offset of <fun>ROUTE
 *         register in GPIO_<periph>ROUTE_TypeDef)
 * 23..19: Enable bit (offset into ROUTEEN register for given function)
 * 18    : Enable bit presence (some inputs are auto-enabled)
 * 17..8 : Peripheral config offset in words from DBUS base within GPIO (offset of <periph>ROUTE[n]
 *         register in GPIO_TypeDef minus offset of first route register [DBGROUTEPEN, 0x440])
 *  7..4 : GPIO pin
 *  3..0 : GPIO port
 * If analog (bit 31 == 1):
 * 15..14: Bus selection (A, B, CD)
 * 13..12: Bus selection (EVEN0, EVEN1, ODD0, ODD1)
 * 11..8 : Peripheral selection (bit in GPIO_nBUSALLOC bitfield)
 * 7 ..0 : Reserved
 */

#define SILABS_PINCTRL_GPIO_PORT_MASK   0x0000000FUL
#define SILABS_PINCTRL_GPIO_PIN_MASK    0x000000F0UL
#define SILABS_PINCTRL_PERIPH_BASE_MASK 0x0003FF00UL
#define SILABS_PINCTRL_HAVE_EN_MASK     0x00040000UL
#define SILABS_PINCTRL_EN_BIT_MASK      0x00F80000UL
#define SILABS_PINCTRL_ROUTE_MASK       0x1F000000UL
#define SILABS_PINCTRL_HAVE_ROUTE_MASK  0x20000000UL

#define SILABS_PINCTRL_ANALOG_MASK      0x80000000UL
#define SILABS_PINCTRL_ABUS_BUS_MASK    0x0000C000UL
#define SILABS_PINCTRL_ABUS_PARITY_MASK 0x00003000UL
#define SILABS_PINCTRL_ABUS_PERIPH_MASK 0x00000F00UL

#define SILABS_PINCTRL_UNUSED 0xFF
#define SILABS_PINCTRL_ANALOG 0xAA

#define SILABS_DBUS(port, pin, periph_base, en_present, en_bit, route)                             \
        (FIELD_PREP(SILABS_PINCTRL_GPIO_PORT_MASK, port) |                                         \
         FIELD_PREP(SILABS_PINCTRL_GPIO_PIN_MASK, pin) |                                           \
         FIELD_PREP(SILABS_PINCTRL_PERIPH_BASE_MASK, periph_base) |                                \
         FIELD_PREP(SILABS_PINCTRL_HAVE_EN_MASK, en_present) |                                     \
         FIELD_PREP(SILABS_PINCTRL_EN_BIT_MASK, en_bit) |                                          \
         FIELD_PREP(SILABS_PINCTRL_ROUTE_MASK, route) |                                            \
         FIELD_PREP(SILABS_PINCTRL_HAVE_ROUTE_MASK, 1))

#define SILABS_FIXED_ROUTE(port, pin, periph_base, en_bit)                                         \
        (FIELD_PREP(SILABS_PINCTRL_GPIO_PORT_MASK, port) |                                         \
         FIELD_PREP(SILABS_PINCTRL_GPIO_PIN_MASK, pin) |                                           \
         FIELD_PREP(SILABS_PINCTRL_PERIPH_BASE_MASK, periph_base) |                                \
         FIELD_PREP(SILABS_PINCTRL_HAVE_EN_MASK, 1) |                                              \
         FIELD_PREP(SILABS_PINCTRL_EN_BIT_MASK, en_bit) |                                          \
         FIELD_PREP(SILABS_PINCTRL_HAVE_ROUTE_MASK, 0))

#define SILABS_ABUS(bus, parity, peripheral)                                                       \
        (FIELD_PREP(SILABS_PINCTRL_ANALOG_MASK, 1) |                                               \
         FIELD_PREP(SILABS_PINCTRL_ABUS_BUS_MASK, bus) |                                           \
         FIELD_PREP(SILABS_PINCTRL_ABUS_PARITY_MASK, parity) |                                     \
         FIELD_PREP(SILABS_PINCTRL_ABUS_PERIPH_MASK, peripheral))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SILABS_PINCTRL_DBUS_H_ */
```

## 178.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Silicon Labs。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 11 行

Silabs Series 2 的 DBUS 配置编码在一个 32 位位域（Bitfield）中，组织如下：

- 位 `31`：该配置是否表示模拟引脚。

如果为数字引脚（位 31 为 0）：

- 位 `30`：保留。
- 位 `29`：是否存在路由寄存器；固定路由没有路由寄存器。
- 位 `28..24`：路由寄存器相对于外设配置的偏移量，以字为单位，即 `GPIO_<periph>ROUTE_TypeDef` 中 `<fun>ROUTE` 寄存器的偏移量。
- 位 `23..19`：使能位，即给定功能在 `ROUTEEN` 寄存器中的位偏移。
- 位 `18`：是否存在使能位；某些输入自动启用。
- 位 `17..8`：外设配置相对于 GPIO 内 DBUS 基址的偏移量，以字为单位，即 `GPIO_TypeDef` 中 `<periph>ROUTE[n]` 寄存器的偏移量，减去第一个路由寄存器 `DBGROUTEPEN` 的偏移量 `0x440`。
- 位 `7..4`：GPIO 引脚。
- 位 `3..0`：GPIO 端口。

如果为模拟引脚（位 31 为 1）：

- 位 `15..14`：总线选择，A、B、CD。
- 位 `13..12`：总线选择，EVEN0、EVEN1、ODD0、ODD1。
- 位 `11..8`：外设选择，即 `GPIO_nBUSALLOC` 位域中的位。
- 位 `7..0`：保留。

### 注释 3：原第 72 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SILABS_PINCTRL_DBUS_H_`。

## 178.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-dbus_8h.html)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P177_serial_test.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P179_simulator.h_源码浏览.md)
