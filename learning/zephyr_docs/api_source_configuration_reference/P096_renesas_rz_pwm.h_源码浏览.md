---
id: learning.zephyr-docs.api-source-configuration-reference.page-96
title: renesas_rz_pwm.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rz__pwm_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第96章\_renesas\_rz\_pwm.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rz__pwm_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rz__pwm_8h.html)。

## 96.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2024-2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PWM_RENESAS_RZ_PWM_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PWM_RENESAS_RZ_PWM_H_

/* RZ PWM GPT IO */
#define RZ_PWM_GPT_IO_A 0
#define RZ_PWM_GPT_IO_B 1

/* RZ PWM MTU IO */
#define RZ_PWM_MTIOCxA 0
#define RZ_PWM_MTIOCxB 1

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PWM_RENESAS_RZ_PWM_H_ */
```

## 96.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024-2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 9 行

RZ PWM 的通用 PWM 定时器（GPT）输入/输出。

### 注释 3：原第 13 行

RZ PWM 的多功能定时器单元（MTU）输入/输出。

### 注释 4：原第 17 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PWM_RENESAS_RZ_PWM_H_`。

## 96.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rz__pwm_8h.html)

---

[上一章](P095_renesas_rcar_generic.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P097_rpi-pico-pinctrl-common.h_源码浏览.md)
