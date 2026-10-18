---
id: learning.zephyr-docs.api-source-reference.page-684
title: pwm_fake.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pwm__fake_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第684章\_pwm\_fake.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pwm__fake_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pwm__fake_8h.html)。

## 684.1\_原始可见代码（Source Code）

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
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="adrivers_2pwm_8h_html"></a>
<a id="agroup__pwm__fake_html_ga2dc0e23bd07cecf5ec38bf37b576ff57"></a>
<a id="agroup__pwm__interface_html_gae1dcfb878163da76041efcedf0960fa0"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2024, Kickmaker
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_PWM_PWM_FAKE_H_
#define ZEPHYR_INCLUDE_DRIVERS_PWM_PWM_FAKE_H_

#include <zephyr/drivers/pwm.h>
#include <zephyr/fff.h>

#ifdef __cplusplus
extern "C" {
#endif


DECLARE_FAKE_VALUE_FUNC(int, fake_pwm_set_cycles, const struct device *, uint32_t, uint32_t,
                        uint32_t, pwm_flags_t);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_PWM_PWM_FAKE_H_ */
```

## 684.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024, Kickmaker。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 56 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PWM_PWM_FAKE_H_`。

## 684.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pwm__fake_8h.html)
- [zephyr/drivers/pwm.h](../pwm_driver_reference/P001_PWM驱动头文件参考.md)
- [fake_pwm_set_cycles](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__fake.html#ga2dc0e23bd07cecf5ec38bf37b576ff57)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)
- [pwm.h](../pwm_driver_reference/P001_PWM驱动头文件参考.md)

---

[上一章](P683_max31790.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P685_pwm_utils.h_源码浏览.md)
