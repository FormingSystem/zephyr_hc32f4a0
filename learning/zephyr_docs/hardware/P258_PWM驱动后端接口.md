---
id: learning.zephyr-docs.hardware.pwmbackend-0
title: PWM驱动后端接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第258章\_PWM驱动后端接口

原文：[group__pwm__interface__backend](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface__backend.html)。读取日期：2026-10-13，`latest`。

## 258.1\_用途

本组提供实现 **脉宽调制（Pulse Width Modulation，PWM）**驱动所需的 **应用程序编程接口（Application Programming Interface，API）**类型、回调签名（Callback Signature）及辅助内容，声明来自 `zephyr/drivers/pwm.h`。

驱动通过[PWM驱动函数表](P259_PWM驱动函数表.md)提供操作，公共参数语义见[PWM公共接口](P255_PWM公共接口.md)。

## 258.2\_回调类型

以下均为函数指针类型定义（Function Pointer Typedef）。

<a id="ga284f0aa783ab2f457b2239a87a9c1671"></a>

**类型 [`pwm_set_cycles_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface__backend.html#ga284f0aa783ab2f457b2239a87a9c1671)：配置引脚周期（Period）与脉宽（Pulse Width）。** 参数说明见函数 [`pwm_set_cycles()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gaff280789f7b45fdefc354b3f841fe3ef)。

```c
typedef int(* pwm_set_cycles_t) (const struct device *dev, uint32_t channel, uint32_t period_cycles, uint32_t pulse_cycles, pwm_flags_t flags);
```

<a id="ga6330ac4e97604ab4510c16a3c4d0437f"></a>

**类型 [`pwm_get_cycles_per_sec_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface__backend.html#ga6330ac4e97604ab4510c16a3c4d0437f)：取得每秒时钟周期数，即时钟频率（Clock Rate）。** 参数说明见函数 [`pwm_get_cycles_per_sec()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga310d416087a619f90e946222668135af)。

```c
typedef int(* pwm_get_cycles_per_sec_t) (const struct device *dev, uint32_t channel, uint64_t *cycles);
```

<a id="ga8dedee6071801685cb618bacd8b51c57"></a>

**类型 [`pwm_configure_capture_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface__backend.html#ga8dedee6071801685cb618bacd8b51c57)：配置单个输入的周期/脉宽捕获（Capture）。** 参数说明见函数 [`pwm_configure_capture()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga9603146d7f9c2690c1e1983113d6c6bb)。

```c
typedef int(* pwm_configure_capture_t) (const struct device *dev, uint32_t channel, pwm_flags_t flags, pwm_capture_callback_handler_t cb, void *user_data);
```

<a id="gaae83bb7862c019492c8bc154015f8e8c"></a>

**类型 [`pwm_enable_capture_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface__backend.html#gaae83bb7862c019492c8bc154015f8e8c)：启用单个输入的周期/脉宽捕获。** 参数说明见函数 [`pwm_enable_capture()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gad14ca53862a465d1789e8936ce394f9a)。

```c
typedef int(* pwm_enable_capture_t) (const struct device *dev, uint32_t channel);
```

<a id="ga471b1f0ed9992e372f1f01683b68f456"></a>

**类型 [`pwm_disable_capture_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface__backend.html#ga471b1f0ed9992e372f1f01683b68f456)：禁用单个输入的周期/脉宽捕获。** 参数说明见函数 [`pwm_disable_capture()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga1df2bb40af2fa3ce945cc9cd67edc2bf)。

```c
typedef int(* pwm_disable_capture_t) (const struct device *dev, uint32_t channel);
```

<a id="ga70ab8cd3c6d7b43890655405b3e6db3f"></a>

**类型 [`pwm_manage_event_callback_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface__backend.html#ga70ab8cd3c6d7b43890655405b3e6db3f)：管理事件回调（Event Callback）。** 参数说明见函数 [`pwm_add_event_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga09d1b358df32e798e0345cd647450d54) 与 [`pwm_remove_event_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga83d9ec60d3fef69c97602365b979aece)。

```c
typedef int(* pwm_manage_event_callback_t) (const struct device *dev, struct pwm_event_callback *callback, bool set);
```


---

[上一章：PWM事件回调结构](P257_PWM事件回调结构.md) · [下一章：PWM驱动函数表](P259_PWM驱动函数表.md) · [返回大纲](大纲.md)
