---
id: learning.zephyr-docs.api-source-reference.page-376
title: input.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第376章\_input.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/input_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/input_8h.html)。

## 376.1\_原始可见代码（Source Code）

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
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="foldopen00091"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="foldopen00115"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="foldopen00134"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="foldopen00150"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="foldopen00169"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__input__events_html_ga02de6c85efab3d21eb81e88e54d58e03"></a>
<a id="agroup__input__events_html_ga4a517c31bdbdd1bd82ba456d256ef1f1"></a>
<a id="agroup__input__events_html_gaa6bcd6755fbdb3eb103f03a72759ce4f"></a>
<a id="agroup__input__interface_html_ga401a03bb89dd59d518f7466a035571da"></a>
<a id="agroup__input__interface_html_gaeb9fa2d4bb990e67ab0a2bd20a141d20"></a>
<a id="agroup__input__interface_html_gaf94bdc8ca673de7947e011872f64ce6c"></a>
<a id="agroup__input__interface_html_gafe511e2ca9402ff539ebd05b8f28929e"></a>
<a id="agroup__input__interface_html_gaffbf85b82d0cede81410dda8ed559201"></a>
<a id="ainput-event-codes_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructinput__callback_html"></a>
<a id="astructinput__callback_html_a1f50a902f5f1ce10ee9131fcd1e7865d"></a>
<a id="astructinput__callback_html_a353255145aabf43c92faab719b8f524c"></a>
<a id="astructinput__callback_html_afe8fa2362e5c2ad35a00e05f33498a20"></a>
<a id="astructinput__event_html"></a>
<a id="astructinput__event_html_a015732c5d67a5374b93e980282a2a9d7"></a>
<a id="astructinput__event_html_a4022d0ddf8ca5be9b478cd0b2758d067"></a>
<a id="astructinput__event_html_a5abe903fbf3b29643578be85c17ba6aa"></a>
<a id="astructinput__event_html_af18b63e5263e73fce8e38838e37d2bae"></a>
<a id="astructinput__event_html_af74a1741fef30ee375d4a71628a9656e"></a>
<a id="astructk__timeout__t_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright 2023 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_INPUT_INPUT_H_
#define ZEPHYR_INCLUDE_INPUT_INPUT_H_


#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/dt-bindings/input/input-event-codes.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/iterable_sections.h>

#ifdef __cplusplus
extern "C" {
#endif

struct input_event {
        const struct device *dev;
        uint8_t sync;
        uint8_t type;
        uint16_t code;
        int32_t value;
};

int input_report(const struct device *dev,
                 uint8_t type, uint16_t code, int32_t value, bool sync,
                 k_timeout_t timeout);

static inline int input_report_key(const struct device *dev,
                                   uint16_t code, int32_t value, bool sync,
                                   k_timeout_t timeout)
{
        return input_report(dev, INPUT_EV_KEY, code, !!value, sync, timeout);
}

static inline int input_report_rel(const struct device *dev,
                                   uint16_t code, int32_t value, bool sync,
                                   k_timeout_t timeout)
{
        return input_report(dev, INPUT_EV_REL, code, value, sync, timeout);
}

static inline int input_report_abs(const struct device *dev,
                                   uint16_t code, int32_t value, bool sync,
                                   k_timeout_t timeout)
{
        return input_report(dev, INPUT_EV_ABS, code, value, sync, timeout);
}

bool input_queue_empty(void);

struct input_callback {
        const struct device *dev;
        void (*callback)(struct input_event *evt, void *user_data);
        void *user_data;
};

#define INPUT_CALLBACK_DEFINE_NAMED(_dev, _callback, _user_data, name)         \
        static const STRUCT_SECTION_ITERABLE(input_callback,                   \
                                             _input_callback__##name) = {      \
                .dev = _dev,                                                   \
                .callback = _callback,                                         \
                .user_data = _user_data,                                       \
        }

#define INPUT_CALLBACK_DEFINE(_dev, _callback, _user_data)                     \
        INPUT_CALLBACK_DEFINE_NAMED(_dev, _callback, _user_data, _callback)

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_INPUT_INPUT_H_ */
```

## 376.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 178 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_INPUT_INPUT_H_`。

## 376.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/input_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/dt-bindings/input/input-event-codes.h](https://docs.zephyrproject.org/latest/doxygen/html/input-event-codes_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [input_event](../system_service_model_reference/P053_input_event_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [dev](../system_service_model_reference/P053_input_event_结构体.md#a4022d0ddf8ca5be9b478cd0b2758d067)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sync](../system_service_model_reference/P053_input_event_结构体.md#a015732c5d67a5374b93e980282a2a9d7)
- [type](../system_service_model_reference/P053_input_event_结构体.md#af74a1741fef30ee375d4a71628a9656e)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [code](../system_service_model_reference/P053_input_event_结构体.md#a5abe903fbf3b29643578be85c17ba6aa)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [value](../system_service_model_reference/P053_input_event_结构体.md#af18b63e5263e73fce8e38838e37d2bae)
- [input_report](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#gafe511e2ca9402ff539ebd05b8f28929e)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [input_report_key](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#gaeb9fa2d4bb990e67ab0a2bd20a141d20)
- [INPUT_EV_KEY](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#ga4a517c31bdbdd1bd82ba456d256ef1f1)
- [input_report_rel](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#gaffbf85b82d0cede81410dda8ed559201)
- [INPUT_EV_REL](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#ga02de6c85efab3d21eb81e88e54d58e03)
- [input_report_abs](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#gaf94bdc8ca673de7947e011872f64ce6c)
- [INPUT_EV_ABS](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#gaa6bcd6755fbdb3eb103f03a72759ce4f)
- [input_queue_empty](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#ga401a03bb89dd59d518f7466a035571da)
- [input_callback](../system_service_model_reference/P052_input_callback_结构体.md)
- [dev](../system_service_model_reference/P052_input_callback_结构体.md#afe8fa2362e5c2ad35a00e05f33498a20)
- [callback](../system_service_model_reference/P052_input_callback_结构体.md#a1f50a902f5f1ce10ee9131fcd1e7865d)
- [user_data](../system_service_model_reference/P052_input_callback_结构体.md#a353255145aabf43c92faab719b8f524c)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [input-event-codes.h](https://docs.zephyrproject.org/latest/doxygen/html/input-event-codes_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [input_callback::callback](../system_service_model_reference/P052_input_callback_结构体.md#a1f50a902f5f1ce10ee9131fcd1e7865d)
- [input_callback::user_data](../system_service_model_reference/P052_input_callback_结构体.md#a353255145aabf43c92faab719b8f524c)
- [input_callback::dev](../system_service_model_reference/P052_input_callback_结构体.md#afe8fa2362e5c2ad35a00e05f33498a20)
- [input_event::sync](../system_service_model_reference/P053_input_event_结构体.md#a015732c5d67a5374b93e980282a2a9d7)
- [input_event::dev](../system_service_model_reference/P053_input_event_结构体.md#a4022d0ddf8ca5be9b478cd0b2758d067)
- [input_event::code](../system_service_model_reference/P053_input_event_结构体.md#a5abe903fbf3b29643578be85c17ba6aa)
- [input_event::value](../system_service_model_reference/P053_input_event_结构体.md#af18b63e5263e73fce8e38838e37d2bae)
- [input_event::type](../system_service_model_reference/P053_input_event_结构体.md#af74a1741fef30ee375d4a71628a9656e)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P375_infineon_mxcryptolite.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P377_input_analog_axis.h_源码浏览.md)
