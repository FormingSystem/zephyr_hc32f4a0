---
id: learning.zephyr-docs.api-source-compiler-device-reference.page-24
title: wch_exti.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wch__exti_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_wch\_exti.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/wch__exti_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P495_zephyr__drivers__interrupt_controller__wch_exti.h_文件参考.md)。

## 24.1\_原始可见代码（Source Code）

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
<a id="foldopen00017"></a>
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
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="autil__macro_8h_html"></a>
<a id="awch__exti_8h_html_a2b90b358d0ee8445e1257c636cfbd931"></a>
<a id="awch__exti_8h_html_a36723b918e6ddb225e05c041a6127369"></a>
<a id="awch__exti_8h_html_a7ff8c5c40b36a6974c535e54fbff311f"></a>
<a id="awch__exti_8h_html_aa1c9d73d6337b6fd8dc95187f739b768"></a>
<a id="awch__exti_8h_html_aa7c5d9dff440158faad0c33da28f8777"></a>
<a id="awch__exti_8h_html_ab41aa3ea720735eb77fc4aaa59659db1"></a>
<a id="awch__exti_8h_html_ab41aa3ea720735eb77fc4aaa59659db1a3b2c0bd85bbfed5d0bed4d495534e518"></a>
<a id="awch__exti_8h_html_ab41aa3ea720735eb77fc4aaa59659db1ac64106e333e2172f25bcbf5c201acb28"></a>

```c
/*
 * Copyright (c) 2025 Michael Hope <michaelh@juju.nz>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_WCH_EXTI_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_WCH_EXTI_H_

#include <stdint.h>

#include <zephyr/sys/util_macro.h>

/* Callback for EXTI interrupt. */
typedef void (*wch_exti_callback_handler_t)(uint8_t line, void *user);

enum wch_exti_trigger {
        /*
         * Note that this is a flag set and these values can be ORed to trigger on
         * both edges.
         */

        /* Trigger on rising edge */
        WCH_EXTI_TRIGGER_RISING_EDGE = BIT(0),
        /* Trigger on falling edge */
        WCH_EXTI_TRIGGER_FALLING_EDGE = BIT(1),
};

/* Enable the EXTI interrupt for `line` */
void wch_exti_enable(uint8_t line);

/* Disable the EXTI interrupt for `line` */
void wch_exti_disable(uint8_t line);

/* Set the trigger mode for `line` */
void wch_exti_set_trigger(uint8_t line, enum wch_exti_trigger trigger);

/* Register a callback for `line` */
int wch_exti_configure(uint8_t line, wch_exti_callback_handler_t callback, void *user);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_WCH_EXTI_H_ */
```

## 24.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Michael Hope <michaelh@juju.nz>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 14 行

外部中断（EXTI）的回调。

### 注释 3：原第 18 行

注意，这是标志集合（flag set）；可对这些值执行按位或（OR），以在双边沿触发。

### 注释 4：原第 23 行

上升沿触发（Trigger on Rising Edge）。

### 注释 5：原第 25 行

下降沿触发（Trigger on Falling Edge）。

### 注释 6：原第 29 行

为 `line` 启用 EXTI 中断。

### 注释 7：原第 32 行

为 `line` 禁用 EXTI 中断。

### 注释 8：原第 35 行

设置 `line` 的触发模式（trigger mode）。

### 注释 9：原第 38 行

为 `line` 注册回调（callback）。

### 注释 10：原第 41 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_WCH_EXTI_H_`。

## 24.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P495_zephyr__drivers__interrupt_controller__wch_exti.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [wch_exti_callback_handler_t](../api_file_reference/P495_zephyr__drivers__interrupt_controller__wch_exti.h_文件参考.md#aa1c9d73d6337b6fd8dc95187f739b768)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [wch_exti_trigger](../api_file_reference/P495_zephyr__drivers__interrupt_controller__wch_exti.h_文件参考.md#ab41aa3ea720735eb77fc4aaa59659db1)
- [WCH_EXTI_TRIGGER_RISING_EDGE](../api_file_reference/P495_zephyr__drivers__interrupt_controller__wch_exti.h_文件参考.md#ab41aa3ea720735eb77fc4aaa59659db1ac64106e333e2172f25bcbf5c201acb28)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [WCH_EXTI_TRIGGER_FALLING_EDGE](../api_file_reference/P495_zephyr__drivers__interrupt_controller__wch_exti.h_文件参考.md#ab41aa3ea720735eb77fc4aaa59659db1a3b2c0bd85bbfed5d0bed4d495534e518)
- [wch_exti_enable](../api_file_reference/P495_zephyr__drivers__interrupt_controller__wch_exti.h_文件参考.md#a36723b918e6ddb225e05c041a6127369)
- [wch_exti_disable](../api_file_reference/P495_zephyr__drivers__interrupt_controller__wch_exti.h_文件参考.md#a2b90b358d0ee8445e1257c636cfbd931)
- [wch_exti_set_trigger](../api_file_reference/P495_zephyr__drivers__interrupt_controller__wch_exti.h_文件参考.md#aa7c5d9dff440158faad0c33da28f8777)
- [wch_exti_configure](../api_file_reference/P495_zephyr__drivers__interrupt_controller__wch_exti.h_文件参考.md#a7ff8c5c40b36a6974c535e54fbff311f)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P023_toolchain.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P025_xspi.h_源码浏览.md)
