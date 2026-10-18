---
id: learning.zephyr-docs.api-source-reference.page-568
title: mspm0_clock_control.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mspm0__clock__control_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第568章\_mspm0\_clock\_control.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__clock__control_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__clock__control_8h.html)。

## 568.1\_原始可见代码（Source Code）

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
<a id="foldopen00025"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="amspm0__clock_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructmspm0__sys__clock_html"></a>
<a id="astructmspm0__sys__clock_html_ac48292bef828c08f7da17a376e491c79"></a>

```c
/*
 * Copyright (c) 2025 Texas Instruments Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MSPM0_CLOCK_CONTROL_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MSPM0_CLOCK_CONTROL_H_

#include <zephyr/dt-bindings/clock/mspm0_clock.h>


struct mspm0_sys_clock {
        uint32_t clk;
};

#define MSPM0_CLOCK_SUBSYS_FN(index) {.clk = DT_INST_CLOCKS_CELL(index, clk)}


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MSPM0_CLOCK_CONTROL_H_ */
```

## 568.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Texas Instruments Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 38 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_MSPM0_CLOCK_CONTROL_H_`。

## 568.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__clock__control_8h.html)
- [zephyr/dt-bindings/clock/mspm0_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__clock_8h.html)
- [mspm0_sys_clock](../device_power_control_model_reference/P043_mspm0_sys_clock_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [clk](../device_power_control_model_reference/P043_mspm0_sys_clock_结构体.md#ac48292bef828c08f7da17a376e491c79)
- [mspm0_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__clock_8h.html)
- [mspm0_sys_clock::clk](../device_power_control_model_reference/P043_mspm0_sys_clock_结构体.md#ac48292bef828c08f7da17a376e491c79)

---

[上一章](P567_mspi_emul.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P569_mspm0_uart.h_源码浏览.md)
