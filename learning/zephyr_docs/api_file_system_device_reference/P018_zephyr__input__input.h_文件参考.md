---
id: learning.zephyr-docs.api-file-system-device-reference.page-18
title: zephyr__input__input.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_input\_\_input.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/input_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

输入（Input）驱动API的主头文件。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/dt-bindings/input/input-event-codes.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/iterable_sections.h>
```

查看此文件的源码。

输入（Input）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 18.1\_数据结构（Data Structures）

<a id="r_input_5Fevent"></a>

```c
struct input_event
```

相关声明：[input_event](../system_service_model_reference/P053_input_event_结构体.md)。

输入事件（Input Event）结构。

<a id="r_input_5Fcallback"></a>

```c
struct input_callback
```

相关声明：[input_callback](../system_service_model_reference/P052_input_callback_结构体.md)。

输入（Input）的回调结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 18.2\_宏定义（Macros）

<a id="r_gad3e7310625b14db2e6930f66dfd879a7"></a>

```c
#define INPUT_CALLBACK_DEFINE_NAMED(_dev, _callback, _user_data, name)
```

相关声明：[INPUT_CALLBACK_DEFINE_NAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#gad3e7310625b14db2e6930f66dfd879a7)。

使用自定义名称注册输入事件（input events）的回调结构体。

<a id="r_gac986cdf392f9aa0a771c8e4e92c479a3"></a>

```c
#define INPUT_CALLBACK_DEFINE(_dev, _callback, _user_data)
```

相关声明：[INPUT_CALLBACK_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#gac986cdf392f9aa0a771c8e4e92c479a3)。

注册输入事件的回调结构体。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 18.3\_函数（Functions）

<a id="r_gafe511e2ca9402ff539ebd05b8f28929e"></a>

```c
int input_report (const struct device *dev, uint8_t type, uint16_t code, int32_t value, bool sync, k_timeout_t timeout)
```

相关声明：[input_report](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#gafe511e2ca9402ff539ebd05b8f28929e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

上报新的输入事件。

<a id="r_gaeb9fa2d4bb990e67ab0a2bd20a141d20"></a>

```c
static int input_report_key (const struct device *dev, uint16_t code, int32_t value, bool sync, k_timeout_t timeout)
```

相关声明：[input_report_key](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#gaeb9fa2d4bb990e67ab0a2bd20a141d20)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

上报新的 `INPUT_EV_KEY` 输入事件；注意，`value` 会转换为 0 或 1。

<a id="r_gaffbf85b82d0cede81410dda8ed559201"></a>

```c
static int input_report_rel (const struct device *dev, uint16_t code, int32_t value, bool sync, k_timeout_t timeout)
```

相关声明：[input_report_rel](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#gaffbf85b82d0cede81410dda8ed559201)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

上报新的 `INPUT_EV_REL` 输入事件。

<a id="r_gaf94bdc8ca673de7947e011872f64ce6c"></a>

```c
static int input_report_abs (const struct device *dev, uint16_t code, int32_t value, bool sync, k_timeout_t timeout)
```

相关声明：[input_report_abs](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#gaf94bdc8ca673de7947e011872f64ce6c)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

上报新的 `INPUT_EV_ABS` 输入事件。

<a id="r_ga401a03bb89dd59d518f7466a035571da"></a>

```c
bool input_queue_empty (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[input_queue_empty](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#ga401a03bb89dd59d518f7466a035571da)。

输入队列（input queue）为空时返回 true。


## 18.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/dt-bindings/input/input-event-codes.h](../api_source_runtime_reference/P033_input-event-codes.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P376_input.h_源码浏览.md)
- [input_event](../system_service_model_reference/P053_input_event_结构体.md)
- [input_callback](../system_service_model_reference/P052_input_callback_结构体.md)
- [INPUT_CALLBACK_DEFINE_NAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#gad3e7310625b14db2e6930f66dfd879a7)
- [INPUT_CALLBACK_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#gac986cdf392f9aa0a771c8e4e92c479a3)
- [input_report](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#gafe511e2ca9402ff539ebd05b8f28929e)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [input_report_key](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#gaeb9fa2d4bb990e67ab0a2bd20a141d20)
- [INPUT_EV_KEY](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#ga4a517c31bdbdd1bd82ba456d256ef1f1)
- [input_report_rel](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#gaffbf85b82d0cede81410dda8ed559201)
- [INPUT_EV_REL](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#ga02de6c85efab3d21eb81e88e54d58e03)
- [input_report_abs](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#gaf94bdc8ca673de7947e011872f64ce6c)
- [INPUT_EV_ABS](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#gaa6bcd6755fbdb3eb103f03a72759ce4f)
- [input_queue_empty](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#ga401a03bb89dd59d518f7466a035571da)

<a id="header-details"></a>

---

[上一章](P017_zephyr__dsp__types.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__drivers__interrupt_controller__intc_irqmp.h_文件参考.md)
