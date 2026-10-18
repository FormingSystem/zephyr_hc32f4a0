---
id: learning.zephyr-docs.pwm-driver-reference.page-1
title: PWM驱动头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pwm_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_PWM驱动头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pwm_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入PWM驱动主头文件参考与源码浏览页，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

PWM（脉宽调制，Pulse Width Modulation）驱动 API 的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/sys/clock.h>
#include <zephyr/sys/math_extras.h>
#include <zephyr/sys/slist.h>
#include <zephyr/toolchain.h>
#include <zephyr/dt-bindings/pwm/pwm.h>
#include <zephyr/syscalls/pwm.h>
```

查看此文件的源码。

PWM（脉宽调制，Pulse Width Modulation）驱动 API 的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_pwm_5Fdt_5Fspec"></a>

```c
struct pwm_dt_spec
```

相关声明：[pwm_dt_spec](../hardware/P256_PWM设备树描述.md)。

保存设备树（Devicetree）中指定的 PWM 信息的容器。

<a id="r_pwm_5Fevent_5Fcallback"></a>

```c
struct pwm_event_callback
```

相关声明：[pwm_event_callback](../hardware/P257_PWM事件回调结构.md)。

PWM 事件回调（Event Callback）结构。

<a id="r_pwm_5Fdriver_5Fapi"></a>

```c
struct pwm_driver_api
```

相关声明：[pwm_driver_api](../hardware/P259_PWM驱动函数表.md)。

驱动操作（Driver Operations）：PWM 驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_ga88b92c580860441c83d1b03db25fc4f1"></a>

```c
#define PWM_DT_SPEC_GET_BY_NAME(node_id, name)
```

相关声明：[PWM_DT_SPEC_GET_BY_NAME](../hardware/P255_PWM公共接口.md#ga88b92c580860441c83d1b03db25fc4f1)。

`struct pwm_dt_spec` 的静态初始化器（Static Initializer）。

<a id="r_ga104a81a3481362d2da9046c0e93a8cd0"></a>

```c
#define PWM_DT_SPEC_INST_GET_BY_NAME(inst, name)
```

相关声明：[PWM_DT_SPEC_INST_GET_BY_NAME](../hardware/P255_PWM公共接口.md#ga104a81a3481362d2da9046c0e93a8cd0)。

根据 `DT_DRV_COMPAT` 对应实例构造 `struct pwm_dt_spec` 的静态初始化器。

<a id="r_ga5557add2123a7138b64997cd070e0ee6"></a>

```c
#define PWM_DT_SPEC_GET_BY_NAME_OR(node_id, name, default_value)
```

相关声明：[PWM_DT_SPEC_GET_BY_NAME_OR](../hardware/P255_PWM公共接口.md#ga5557add2123a7138b64997cd070e0ee6)。

类似 `PWM_DT_SPEC_GET_BY_NAME()`，但提供默认值回退。

<a id="r_gac00e53eccaf9eb515aed0921404adb31"></a>

```c
#define PWM_DT_SPEC_INST_GET_BY_NAME_OR(inst, name, default_value)
```

相关声明：[PWM_DT_SPEC_INST_GET_BY_NAME_OR](../hardware/P255_PWM公共接口.md#gac00e53eccaf9eb515aed0921404adb31)。

类似 `PWM_DT_SPEC_INST_GET_BY_NAME()`，但提供默认值回退。

<a id="r_ga7e8375bcf95ae6a9500ce3aba4586de4"></a>

```c
#define PWM_DT_SPEC_GET_BY_IDX(node_id, idx)
```

相关声明：[PWM_DT_SPEC_GET_BY_IDX](../hardware/P255_PWM公共接口.md#ga7e8375bcf95ae6a9500ce3aba4586de4)。

`struct pwm_dt_spec` 的静态初始化器（Static Initializer）。

<a id="r_ga3c1c557fa4461e61f4a147fc72f87f8d"></a>

```c
#define PWM_DT_SPEC_INST_GET_BY_IDX(inst, idx)
```

相关声明：[PWM_DT_SPEC_INST_GET_BY_IDX](../hardware/P255_PWM公共接口.md#ga3c1c557fa4461e61f4a147fc72f87f8d)。

根据 `DT_DRV_COMPAT` 对应实例构造 `struct pwm_dt_spec` 的静态初始化器。

<a id="r_gaf5808fd88b101208681820b53bca33e1"></a>

```c
#define PWM_DT_SPEC_GET_BY_IDX_OR(node_id, idx, default_value)
```

相关声明：[PWM_DT_SPEC_GET_BY_IDX_OR](../hardware/P255_PWM公共接口.md#gaf5808fd88b101208681820b53bca33e1)。

类似 `PWM_DT_SPEC_GET_BY_IDX()`，但提供默认值回退。

<a id="r_ga7eeef648c3142fced48b7ab52c9c1ead"></a>

```c
#define PWM_DT_SPEC_INST_GET_BY_IDX_OR(inst, idx, default_value)
```

相关声明：[PWM_DT_SPEC_INST_GET_BY_IDX_OR](../hardware/P255_PWM公共接口.md#ga7eeef648c3142fced48b7ab52c9c1ead)。

类似 `PWM_DT_SPEC_INST_GET_BY_IDX()`，但提供默认值回退。

<a id="r_ga59a79f0b77c5b71252bde126f333a84b"></a>

```c
#define PWM_DT_SPEC_GET(node_id)
```

相关声明：[PWM_DT_SPEC_GET](../hardware/P255_PWM公共接口.md#ga59a79f0b77c5b71252bde126f333a84b)。

等价于 `PWM_DT_SPEC_GET_BY_IDX(node_id, 0)`。

<a id="r_gaa346428c6cb1f11aafaa6306486e8a4b"></a>

```c
#define PWM_DT_SPEC_INST_GET(inst)
```

相关声明：[PWM_DT_SPEC_INST_GET](../hardware/P255_PWM公共接口.md#gaa346428c6cb1f11aafaa6306486e8a4b)。

等价于 `PWM_DT_SPEC_INST_GET_BY_IDX(inst, 0)`。

<a id="r_ga82f8efe8f0bc088fdda58c09dd4be4ff"></a>

```c
#define PWM_DT_SPEC_GET_OR(node_id, default_value)
```

相关声明：[PWM_DT_SPEC_GET_OR](../hardware/P255_PWM公共接口.md#ga82f8efe8f0bc088fdda58c09dd4be4ff)。

等价于 `PWM_DT_SPEC_GET_BY_IDX_OR(node_id, 0, default_value)`。

<a id="r_ga6bd84121715beb62a3ca2672dfae0630"></a>

```c
#define PWM_DT_SPEC_INST_GET_OR(inst, default_value)
```

相关声明：[PWM_DT_SPEC_INST_GET_OR](../hardware/P255_PWM公共接口.md#ga6bd84121715beb62a3ca2672dfae0630)。

等价于 `PWM_DT_SPEC_INST_GET_BY_IDX_OR(inst, 0, default_value)`。

<a id="define-members-0"></a>

### PWM捕获配置标志（Capture Configuration Flags）



<a id="r_ga5b4b41ccdf8810a77f71c2155a521f44"></a>

```c
#define PWM_CAPTURE_TYPE_PERIOD (1U << PWM_CAPTURE_TYPE_SHIFT)
```

相关声明：[PWM_CAPTURE_TYPE_PERIOD](../hardware/P255_PWM公共接口.md#ga5b4b41ccdf8810a77f71c2155a521f44)。

PWM 引脚捕获功能采集周期（Period）。

<a id="r_gab883b83cc5418555a437ce128f32ab01"></a>

```c
#define PWM_CAPTURE_TYPE_PULSE (2U << PWM_CAPTURE_TYPE_SHIFT)
```

相关声明：[PWM_CAPTURE_TYPE_PULSE](../hardware/P255_PWM公共接口.md#gab883b83cc5418555a437ce128f32ab01)。

PWM 引脚捕获功能采集脉宽（Pulse Width）。

<a id="r_ga76175b0c2d5187ded5bbd314dc798bd5"></a>

```c
#define PWM_CAPTURE_TYPE_BOTH
```

相关声明：[PWM_CAPTURE_TYPE_BOTH](../hardware/P255_PWM公共接口.md#ga76175b0c2d5187ded5bbd314dc798bd5)。

PWM 引脚捕获功能同时采集周期与脉宽。

<a id="r_gad59fe75340facda843cad06993cf1814"></a>

```c
#define PWM_CAPTURE_MODE_SINGLE (0U << PWM_CAPTURE_MODE_SHIFT)
```

相关声明：[PWM_CAPTURE_MODE_SINGLE](../hardware/P255_PWM公共接口.md#gad59fe75340facda843cad06993cf1814)。

PWM 引脚捕获功能采集单次周期／脉宽。

<a id="r_gabe9bbff9832b4fa40faa057fad8fdaa9"></a>

```c
#define PWM_CAPTURE_MODE_CONTINUOUS (1U << PWM_CAPTURE_MODE_SHIFT)
```

相关声明：[PWM_CAPTURE_MODE_CONTINUOUS](../hardware/P255_PWM公共接口.md#gabe9bbff9832b4fa40faa057fad8fdaa9)。

PWM 引脚捕获功能连续采集周期／脉宽。

<a id="define-members-1"></a>

### PWM事件类型（Event Types）



<a id="r_ga94f1e31fe6b935569698e8f404955bd6"></a>

```c
#define PWM_EVENT_TYPE_SHIFT 0U
```

相关声明：[PWM_EVENT_TYPE_SHIFT](../hardware/P255_PWM公共接口.md#ga94f1e31fe6b935569698e8f404955bd6)。

<a id="r_gac438636e8379df41970b601fdf8a038a"></a>

```c
#define PWM_EVENT_TYPE_PERIOD (1U << PWM_EVENT_TYPE_SHIFT)
```

相关声明：[PWM_EVENT_TYPE_PERIOD](../hardware/P255_PWM公共接口.md#gac438636e8379df41970b601fdf8a038a)、[PWM_EVENT_TYPE_SHIFT](../hardware/P255_PWM公共接口.md#ga94f1e31fe6b935569698e8f404955bd6)。

将事件配置为在每个 PWM 周期结束时触发。

<a id="r_ga70e0635a1187061921f559646a6e2456"></a>

```c
#define PWM_EVENT_TYPE_FAULT (2U << PWM_EVENT_TYPE_SHIFT)
```

相关声明：[PWM_EVENT_TYPE_FAULT](../hardware/P255_PWM公共接口.md#ga70e0635a1187061921f559646a6e2456)、[PWM_EVENT_TYPE_SHIFT](../hardware/P255_PWM公共接口.md#ga94f1e31fe6b935569698e8f404955bd6)。

将事件配置为在发生故障（Fault）时触发。

<a id="r_ga4e1b5b2c0a6b489eba876a8317acda45"></a>

```c
#define PWM_EVENT_TYPE_COMPARE_CAPTURE (4U << PWM_EVENT_TYPE_SHIFT)
```

相关声明：[PWM_EVENT_TYPE_COMPARE_CAPTURE](../hardware/P255_PWM公共接口.md#ga4e1b5b2c0a6b489eba876a8317acda45)、[PWM_EVENT_TYPE_SHIFT](../hardware/P255_PWM公共接口.md#ga94f1e31fe6b935569698e8f404955bd6)。

将事件配置为在比较／捕获匹配（Compare/Capture Match）时触发。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.3\_类型定义（Typedefs）

<a id="r_gae1dcfb878163da76041efcedf0960fa0"></a>

```c
typedef uint16_t pwm_flags_t
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)。

提供保存 PWM 配置标志的类型。

<a id="r_ga5bc9607de7643cb78476ed354c51560b"></a>

```c
typedef uint16_t pwm_events_t
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pwm_events_t](../hardware/P255_PWM公共接口.md#ga5bc9607de7643cb78476ed354c51560b)。

提供保存 PWM 事件的类型。

<a id="r_ga2395ef29b77674d9f1b56d8091b8695a"></a>

```c
typedef void(* pwm_capture_callback_handler_t) (const struct device *dev, uint32_t channel, uint32_t period_cycles, uint32_t pulse_cycles, int status, void *user_data)
```

相关声明：[pwm_capture_callback_handler_t](../hardware/P255_PWM公共接口.md#ga2395ef29b77674d9f1b56d8091b8695a)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

PWM 捕获回调处理函数（Capture Callback Handler）的签名。

<a id="r_gaedacc300332a9c01da48671f92bf0097"></a>

```c
typedef void(* pwm_event_callback_handler_t) (const struct device *dev, struct pwm_event_callback *callback, uint32_t channel, pwm_events_t events)
```

相关声明：[pwm_event_callback_handler_t](../hardware/P255_PWM公共接口.md#gaedacc300332a9c01da48671f92bf0097)、[device](../device_reference/P002_设备对象结构.md)、[pwm_event_callback](../hardware/P257_PWM事件回调结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pwm_events_t](../hardware/P255_PWM公共接口.md#ga5bc9607de7643cb78476ed354c51560b)。

PWM 事件回调处理函数的签名。

<a id="r_ga284f0aa783ab2f457b2239a87a9c1671"></a>

```c
typedef int(* pwm_set_cycles_t) (const struct device *dev, uint32_t channel, uint32_t period_cycles, uint32_t pulse_cycles, pwm_flags_t flags)
```

相关声明：[pwm_set_cycles_t](../hardware/P258_PWM驱动后端接口.md#ga284f0aa783ab2f457b2239a87a9c1671)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

配置 PWM 引脚周期与脉宽的回调 API。

<a id="r_ga6330ac4e97604ab4510c16a3c4d0437f"></a>

```c
typedef int(* pwm_get_cycles_per_sec_t) (const struct device *dev, uint32_t channel, uint64_t *cycles)
```

相关声明：[pwm_get_cycles_per_sec_t](../hardware/P258_PWM驱动后端接口.md#ga6330ac4e97604ab4510c16a3c4d0437f)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

取得 PWM 每秒周期数，即时钟频率的回调 API。

<a id="r_ga8dedee6071801685cb618bacd8b51c57"></a>

```c
typedef int(* pwm_configure_capture_t) (const struct device *dev, uint32_t channel, pwm_flags_t flags, pwm_capture_callback_handler_t cb, void *user_data)
```

相关声明：[pwm_configure_capture_t](../hardware/P258_PWM驱动后端接口.md#ga8dedee6071801685cb618bacd8b51c57)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[pwm_capture_callback_handler_t](../hardware/P255_PWM公共接口.md#ga2395ef29b77674d9f1b56d8091b8695a)。

配置 PWM 捕获功能的回调 API。

<a id="r_gaae83bb7862c019492c8bc154015f8e8c"></a>

```c
typedef int(* pwm_enable_capture_t) (const struct device *dev, uint32_t channel)
```

相关声明：[pwm_enable_capture_t](../hardware/P258_PWM驱动后端接口.md#gaae83bb7862c019492c8bc154015f8e8c)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

启用 PWM 捕获功能的回调 API。

<a id="r_ga471b1f0ed9992e372f1f01683b68f456"></a>

```c
typedef int(* pwm_disable_capture_t) (const struct device *dev, uint32_t channel)
```

相关声明：[pwm_disable_capture_t](../hardware/P258_PWM驱动后端接口.md#ga471b1f0ed9992e372f1f01683b68f456)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

禁用 PWM 捕获功能的回调 API。

<a id="r_ga70ab8cd3c6d7b43890655405b3e6db3f"></a>

```c
typedef int(* pwm_manage_event_callback_t) (const struct device *dev, struct pwm_event_callback *callback, bool set)
```

相关声明：[pwm_manage_event_callback_t](../hardware/P258_PWM驱动后端接口.md#ga70ab8cd3c6d7b43890655405b3e6db3f)、[device](../device_reference/P002_设备对象结构.md)、[pwm_event_callback](../hardware/P257_PWM事件回调结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

管理事件回调的回调 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.4\_函数（Functions）

<a id="r_gaff280789f7b45fdefc354b3f841fe3ef"></a>

```c
int pwm_set_cycles (const struct device *dev, uint32_t channel, uint32_t period, uint32_t pulse, pwm_flags_t flags)
```

相关声明：[pwm_set_cycles](../hardware/P255_PWM公共接口.md#gaff280789f7b45fdefc354b3f841fe3ef)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

为单个 PWM 输出设置周期与脉宽。

<a id="r_ga310d416087a619f90e946222668135af"></a>

```c
int pwm_get_cycles_per_sec (const struct device *dev, uint32_t channel, uint64_t *cycles)
```

相关声明：[pwm_get_cycles_per_sec](../hardware/P255_PWM公共接口.md#ga310d416087a619f90e946222668135af)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

取得单个 PWM 输出的时钟速率，即每秒周期数。

<a id="r_gadd9049c9a56cd9419736b3514e42dc01"></a>

```c
static int pwm_set (const struct device *dev, uint32_t channel, uint32_t period, uint32_t pulse, pwm_flags_t flags)
```

相关声明：[pwm_set](../hardware/P255_PWM公共接口.md#gadd9049c9a56cd9419736b3514e42dc01)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

以纳秒（Nanoseconds）为单位设置单个 PWM 输出的周期与脉宽。

<a id="r_ga225ce58ceb3de3d76df3e03439d655b9"></a>

```c
static int pwm_set_dt (const struct pwm_dt_spec *spec, uint32_t period, uint32_t pulse)
```

相关声明：[pwm_set_dt](../hardware/P255_PWM公共接口.md#ga225ce58ceb3de3d76df3e03439d655b9)、[pwm_dt_spec](../hardware/P256_PWM设备树描述.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

根据 `struct pwm_dt_spec` 以纳秒设置周期与脉宽，其中周期由调用方自定义。

<a id="r_ga8ff263177143d33c6d0a284b837bc4da"></a>

```c
static int pwm_set_pulse_dt (const struct pwm_dt_spec *spec, uint32_t pulse)
```

相关声明：[pwm_set_pulse_dt](../hardware/P255_PWM公共接口.md#ga8ff263177143d33c6d0a284b837bc4da)、[pwm_dt_spec](../hardware/P256_PWM设备树描述.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

根据 `struct pwm_dt_spec` 以纳秒设置周期与脉宽。

<a id="r_gae57fb205e43dde82d96abe79966539a9"></a>

```c
static int pwm_cycles_to_usec (const struct device *dev, uint32_t channel, uint32_t cycles, uint64_t *usec)
```

相关声明：[pwm_cycles_to_usec](../hardware/P255_PWM公共接口.md#gae57fb205e43dde82d96abe79966539a9)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

将 PWM 时钟周期数转换为微秒（Microseconds）。

<a id="r_ga6f0281398611dd876386c66a63373a2e"></a>

```c
static int pwm_cycles_to_nsec (const struct device *dev, uint32_t channel, uint32_t cycles, uint64_t *nsec)
```

相关声明：[pwm_cycles_to_nsec](../hardware/P255_PWM公共接口.md#ga6f0281398611dd876386c66a63373a2e)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

将 PWM 时钟周期数转换为纳秒。

<a id="r_ga9603146d7f9c2690c1e1983113d6c6bb"></a>

```c
static int pwm_configure_capture (const struct device *dev, uint32_t channel, pwm_flags_t flags, pwm_capture_callback_handler_t cb, void *user_data)
```

相关声明：[pwm_configure_capture](../hardware/P255_PWM公共接口.md#ga9603146d7f9c2690c1e1983113d6c6bb)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[pwm_capture_callback_handler_t](../hardware/P255_PWM公共接口.md#ga2395ef29b77674d9f1b56d8091b8695a)。

为单个 PWM 输入配置周期／脉宽捕获。

<a id="r_gad14ca53862a465d1789e8936ce394f9a"></a>

```c
int pwm_enable_capture (const struct device *dev, uint32_t channel)
```

相关声明：[pwm_enable_capture](../hardware/P255_PWM公共接口.md#gad14ca53862a465d1789e8936ce394f9a)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

为单个 PWM 输入启用周期／脉宽捕获。

<a id="r_ga1df2bb40af2fa3ce945cc9cd67edc2bf"></a>

```c
int pwm_disable_capture (const struct device *dev, uint32_t channel)
```

相关声明：[pwm_disable_capture](../hardware/P255_PWM公共接口.md#ga1df2bb40af2fa3ce945cc9cd67edc2bf)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

为单个 PWM 输入禁用周期／脉宽捕获。

<a id="r_ga09767ae3c8d970675dbf9e3e50291743"></a>

```c
int pwm_capture_cycles (const struct device *dev, uint32_t channel, pwm_flags_t flags, uint32_t *period, uint32_t *pulse, k_timeout_t timeout)
```

相关声明：[pwm_capture_cycles](../hardware/P255_PWM公共接口.md#ga09767ae3c8d970675dbf9e3e50291743)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为单个 PWM 输入捕获一次周期／脉宽，以时钟周期数表示。

<a id="r_ga3a1552ea924eeec21477396da6d3890b"></a>

```c
static int pwm_capture_usec (const struct device *dev, uint32_t channel, pwm_flags_t flags, uint64_t *period, uint64_t *pulse, k_timeout_t timeout)
```

相关声明：[pwm_capture_usec](../hardware/P255_PWM公共接口.md#ga3a1552ea924eeec21477396da6d3890b)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为单个 PWM 输入捕获一次周期／脉宽，以微秒表示。

<a id="r_ga6489095d890224d23c5ed05bc884d24a"></a>

```c
static int pwm_capture_nsec (const struct device *dev, uint32_t channel, pwm_flags_t flags, uint64_t *period, uint64_t *pulse, k_timeout_t timeout)
```

相关声明：[pwm_capture_nsec](../hardware/P255_PWM公共接口.md#ga6489095d890224d23c5ed05bc884d24a)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为单个 PWM 输入捕获一次周期／脉宽，以纳秒表示。

<a id="r_gaf87ef431d50a482910e77e49d52a2e13"></a>

```c
static void pwm_init_event_callback (struct pwm_event_callback *callback, pwm_event_callback_handler_t handler, uint32_t channel, pwm_events_t event_mask)
```

相关声明：[pwm_init_event_callback](../hardware/P255_PWM公共接口.md#gaf87ef431d50a482910e77e49d52a2e13)、[pwm_event_callback](../hardware/P257_PWM事件回调结构.md)、[pwm_event_callback_handler_t](../hardware/P255_PWM公共接口.md#gaedacc300332a9c01da48671f92bf0097)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pwm_events_t](../hardware/P255_PWM公共接口.md#ga5bc9607de7643cb78476ed354c51560b)。

帮助正确初始化 `struct pwm_event_callback` 的辅助函数。

<a id="r_ga09d1b358df32e798e0345cd647450d54"></a>

```c
static int pwm_add_event_callback (const struct device *dev, struct pwm_event_callback *callback)
```

相关声明：[pwm_add_event_callback](../hardware/P255_PWM公共接口.md#ga09d1b358df32e798e0345cd647450d54)、[device](../device_reference/P002_设备对象结构.md)、[pwm_event_callback](../hardware/P257_PWM事件回调结构.md)。

添加应用事件回调。

<a id="r_ga83d9ec60d3fef69c97602365b979aece"></a>

```c
static int pwm_remove_event_callback (const struct device *dev, struct pwm_event_callback *callback)
```

相关声明：[pwm_remove_event_callback](../hardware/P255_PWM公共接口.md#ga83d9ec60d3fef69c97602365b979aece)、[device](../device_reference/P002_设备对象结构.md)、[pwm_event_callback](../hardware/P257_PWM事件回调结构.md)。

移除应用事件回调。

<a id="r_ga70aad0d88e8041c880499e7cdaa9ae57"></a>

```c
static bool pwm_is_ready_dt (const struct pwm_dt_spec *spec)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[pwm_is_ready_dt](../hardware/P255_PWM公共接口.md#ga70aad0d88e8041c880499e7cdaa9ae57)、[pwm_dt_spec](../hardware/P256_PWM设备树描述.md)。

验证 PWM 设备是否就绪（Ready）。

## 1.5\_源码定位与版本边界

相对源码定位：[PWM驱动头文件](../../../include/zephyr/drivers/pwm.h)、[PWM绑定常量](../../../include/zephyr/dt-bindings/pwm/pwm.h)、[PWM设备树宏](../../../include/zephyr/devicetree/pwms.h)、[PWM配置选项](../../../drivers/pwm/Kconfig)和[控制器公共绑定](../../../dts/bindings/pwm/pwm-controller.yaml)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：设备树对象与回退：pwm_dt_spec静态初始化器保存设备指针、通道、纳秒周期和标志，不启动PWM。BY_NAME_OR和BY_IDX_OR都只检查节点是否具有pwms属性；属性存在但名称或索引无效时，不会自动选择default_value。实例版静态初始化宏先转换为节点再调用节点版，flags因而经过DT_PWMS_FLAGS_BY_NAME／BY_IDX的缺省0路径，不能与直接调用DT_INST_PWMS_FLAGS系列混为一谈。

> 译注——源码核对：单位与数值：pwm_set_cycles接收硬件时钟周期数，公共实现先拒绝pulse大于period。pwm_set接收纳秒，查询驱动时钟速率后做整数乘除，结果超过32位周期计数时返回-ENOTSUP；整数除法可能截断，因此最终波形受硬件分辨率约束。pwm_set_dt采用调用方周期，pwm_set_pulse_dt采用spec中的周期，二者均沿用spec标志。

> 译注——源码核对：换算与错误：pwm_cycles_to_usec／nsec先查询时钟速率，再以u64_mul_overflow检查乘法，溢出返回-ERANGE，否则整数除法换算。驱动返回的时钟速率必须可用于除法；这些包装函数没有独立的零频率检查。捕获的usec／nsec包装先取得周期计数，再依次换算周期与脉宽；失败时立即返回，不保证两个输出均已更新。按当前可见实现，不应把NULL输出指针当作这些时间单位包装函数通用支持的省略方式。

> 译注——源码核对：编译选项与驱动实现：捕获相关操作受CONFIG_PWM_CAPTURE约束，事件操作受CONFIG_PWM_EVENT约束；__DOXYGEN__分支让文档能展示可选接口，不代表当前固件已开启它们。当前Kconfig将PWM_EVENT标为实验功能（Experimental）。configure_capture、enable_capture、disable_capture和manage_event_callback在包装层检查空函数指针并可返回-ENOSYS；基础set_cycles和get_cycles_per_sec则按必需驱动操作直接调用。

> 译注——源码核对：事件回调与就绪：pwm_init_event_callback检查回调及处理函数并写入handler、channel、event_mask，不注册回调，也不分配回调对象。添加／删除函数分别把true／false传给驱动的manage_event_callback；对象生存期和驱动行为仍需遵守完整API约定。pwm_is_ready_dt只调用device_is_ready(spec->dev)，不验证通道范围、周期可实现性、输出引脚连接或捕获支持。

> 译注——源码核对：版本边界：本批记录驱动主头文件、PWM绑定常量、PWM设备树宏、驱动Kconfig及控制器公共绑定五份官方源码摘要。源码页非注释代码与读取的原始头文件一致；latest、滚动main和仓库参照版本不自动等同。仓库链接仅作相对源码定位，未构建固件、输出波形或操作硬件。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 1.6\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [zephyr/sys/clock.h](../timer_reference/P091_系统时钟头文件源码.md)
- [zephyr/sys/math_extras.h](../math_reference/P003_数学辅助头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [zephyr/dt-bindings/pwm/pwm.h](../dt_pwm_binding_reference/P004_PWM绑定常量头文件源码.md)
- [查看此文件的源码](P002_PWM驱动头文件源码.md)
- [pwm_dt_spec](../hardware/P256_PWM设备树描述.md)
- [pwm_event_callback](../hardware/P257_PWM事件回调结构.md)
- [pwm_driver_api](../hardware/P259_PWM驱动函数表.md)
- [PWM_DT_SPEC_GET_BY_NAME](../hardware/P255_PWM公共接口.md#ga88b92c580860441c83d1b03db25fc4f1)
- [PWM_DT_SPEC_INST_GET_BY_NAME](../hardware/P255_PWM公共接口.md#ga104a81a3481362d2da9046c0e93a8cd0)
- [PWM_DT_SPEC_GET_BY_NAME_OR](../hardware/P255_PWM公共接口.md#ga5557add2123a7138b64997cd070e0ee6)
- [PWM_DT_SPEC_INST_GET_BY_NAME_OR](../hardware/P255_PWM公共接口.md#gac00e53eccaf9eb515aed0921404adb31)
- [PWM_DT_SPEC_GET_BY_IDX](../hardware/P255_PWM公共接口.md#ga7e8375bcf95ae6a9500ce3aba4586de4)
- [PWM_DT_SPEC_INST_GET_BY_IDX](../hardware/P255_PWM公共接口.md#ga3c1c557fa4461e61f4a147fc72f87f8d)
- [PWM_DT_SPEC_GET_BY_IDX_OR](../hardware/P255_PWM公共接口.md#gaf5808fd88b101208681820b53bca33e1)
- [PWM_DT_SPEC_INST_GET_BY_IDX_OR](../hardware/P255_PWM公共接口.md#ga7eeef648c3142fced48b7ab52c9c1ead)
- [PWM_DT_SPEC_GET](../hardware/P255_PWM公共接口.md#ga59a79f0b77c5b71252bde126f333a84b)
- [PWM_DT_SPEC_INST_GET](../hardware/P255_PWM公共接口.md#gaa346428c6cb1f11aafaa6306486e8a4b)
- [PWM_DT_SPEC_GET_OR](../hardware/P255_PWM公共接口.md#ga82f8efe8f0bc088fdda58c09dd4be4ff)
- [PWM_DT_SPEC_INST_GET_OR](../hardware/P255_PWM公共接口.md#ga6bd84121715beb62a3ca2672dfae0630)
- [PWM_CAPTURE_TYPE_PERIOD](../hardware/P255_PWM公共接口.md#ga5b4b41ccdf8810a77f71c2155a521f44)
- [PWM_CAPTURE_TYPE_PULSE](../hardware/P255_PWM公共接口.md#gab883b83cc5418555a437ce128f32ab01)
- [PWM_CAPTURE_TYPE_BOTH](../hardware/P255_PWM公共接口.md#ga76175b0c2d5187ded5bbd314dc798bd5)
- [PWM_CAPTURE_MODE_SINGLE](../hardware/P255_PWM公共接口.md#gad59fe75340facda843cad06993cf1814)
- [PWM_CAPTURE_MODE_CONTINUOUS](../hardware/P255_PWM公共接口.md#gabe9bbff9832b4fa40faa057fad8fdaa9)
- [PWM_EVENT_TYPE_SHIFT](../hardware/P255_PWM公共接口.md#ga94f1e31fe6b935569698e8f404955bd6)
- [PWM_EVENT_TYPE_PERIOD](../hardware/P255_PWM公共接口.md#gac438636e8379df41970b601fdf8a038a)
- [PWM_EVENT_TYPE_FAULT](../hardware/P255_PWM公共接口.md#ga70e0635a1187061921f559646a6e2456)
- [PWM_EVENT_TYPE_COMPARE_CAPTURE](../hardware/P255_PWM公共接口.md#ga4e1b5b2c0a6b489eba876a8317acda45)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)
- [pwm_events_t](../hardware/P255_PWM公共接口.md#ga5bc9607de7643cb78476ed354c51560b)
- [pwm_capture_callback_handler_t](../hardware/P255_PWM公共接口.md#ga2395ef29b77674d9f1b56d8091b8695a)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pwm_event_callback_handler_t](../hardware/P255_PWM公共接口.md#gaedacc300332a9c01da48671f92bf0097)
- [pwm_set_cycles_t](../hardware/P258_PWM驱动后端接口.md#ga284f0aa783ab2f457b2239a87a9c1671)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [pwm_get_cycles_per_sec_t](../hardware/P258_PWM驱动后端接口.md#ga6330ac4e97604ab4510c16a3c4d0437f)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [pwm_configure_capture_t](../hardware/P258_PWM驱动后端接口.md#ga8dedee6071801685cb618bacd8b51c57)
- [pwm_enable_capture_t](../hardware/P258_PWM驱动后端接口.md#gaae83bb7862c019492c8bc154015f8e8c)
- [pwm_disable_capture_t](../hardware/P258_PWM驱动后端接口.md#ga471b1f0ed9992e372f1f01683b68f456)
- [pwm_manage_event_callback_t](../hardware/P258_PWM驱动后端接口.md#ga70ab8cd3c6d7b43890655405b3e6db3f)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [pwm_set_cycles](../hardware/P255_PWM公共接口.md#gaff280789f7b45fdefc354b3f841fe3ef)
- [pwm_get_cycles_per_sec](../hardware/P255_PWM公共接口.md#ga310d416087a619f90e946222668135af)
- [pwm_set](../hardware/P255_PWM公共接口.md#gadd9049c9a56cd9419736b3514e42dc01)
- [pwm_set_dt](../hardware/P255_PWM公共接口.md#ga225ce58ceb3de3d76df3e03439d655b9)
- [pwm_set_pulse_dt](../hardware/P255_PWM公共接口.md#ga8ff263177143d33c6d0a284b837bc4da)
- [pwm_cycles_to_usec](../hardware/P255_PWM公共接口.md#gae57fb205e43dde82d96abe79966539a9)
- [pwm_cycles_to_nsec](../hardware/P255_PWM公共接口.md#ga6f0281398611dd876386c66a63373a2e)
- [pwm_configure_capture](../hardware/P255_PWM公共接口.md#ga9603146d7f9c2690c1e1983113d6c6bb)
- [pwm_enable_capture](../hardware/P255_PWM公共接口.md#gad14ca53862a465d1789e8936ce394f9a)
- [pwm_disable_capture](../hardware/P255_PWM公共接口.md#ga1df2bb40af2fa3ce945cc9cd67edc2bf)
- [pwm_capture_cycles](../hardware/P255_PWM公共接口.md#ga09767ae3c8d970675dbf9e3e50291743)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [pwm_capture_usec](../hardware/P255_PWM公共接口.md#ga3a1552ea924eeec21477396da6d3890b)
- [pwm_capture_nsec](../hardware/P255_PWM公共接口.md#ga6489095d890224d23c5ed05bc884d24a)
- [pwm_init_event_callback](../hardware/P255_PWM公共接口.md#gaf87ef431d50a482910e77e49d52a2e13)
- [pwm_add_event_callback](../hardware/P255_PWM公共接口.md#ga09d1b358df32e798e0345cd647450d54)
- [pwm_remove_event_callback](../hardware/P255_PWM公共接口.md#ga83d9ec60d3fef69c97602365b979aece)
- [pwm_is_ready_dt](../hardware/P255_PWM公共接口.md#ga70aad0d88e8041c880499e7cdaa9ae57)

<a id="PWM_CAPTURE_FLAGS"></a>
<a id="PWM_EVENT_TYPES"></a>
<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_PWM驱动头文件源码.md)
