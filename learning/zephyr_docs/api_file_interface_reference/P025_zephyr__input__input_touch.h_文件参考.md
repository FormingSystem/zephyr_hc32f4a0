---
id: learning.zephyr-docs.api-file-interface-reference.page-25
title: zephyr__input__input_touch.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input__touch_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_zephyr\_\_input\_\_input\_touch.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/input__touch_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

触摸事件（Touch Events）API的头文件。

<a id="details"></a>

```c
#include <zephyr/input/input.h>
```

查看此文件的源码。

触摸事件（Touch Events）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 25.1\_数据结构（Data Structures）

<a id="r_input_5Ftouchscreen_5Fcommon_5Fconfig"></a>

```c
struct input_touchscreen_common_config
```

相关声明：[input_touchscreen_common_config](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md)。

通用触摸屏（Touchscreen）配置。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 25.2\_宏定义（Macros）

<a id="r_ga7a96be130c0c6577f4cc835d6634462f"></a>

```c
#define INPUT_TOUCH_OUTPUT_DIM(node_id, dim, prop)
```

相关声明：[INPUT_TOUCH_OUTPUT_DIM](https://docs.zephyrproject.org/latest/doxygen/html/group__touch__events.html#ga7a96be130c0c6577f4cc835d6634462f)。

从显示设备的 phandle 中选择一个输出尺寸（output dimension）；否则使用节点自身的属性。

<a id="r_gae19dc2c40a8e14d28db614dfd4c5e32b"></a>

```c
#define INPUT_TOUCH_DT_COMMON_CONFIG_INIT(node_id)
```

相关声明：[INPUT_TOUCH_DT_COMMON_CONFIG_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__touch__events.html#gae19dc2c40a8e14d28db614dfd4c5e32b)。

根据设备树（devicetree）初始化触摸屏通用配置（common touchscreen config）。

<a id="r_ga354195b719d526cebd63a061e8dc408b"></a>

```c
#define INPUT_TOUCH_DT_INST_COMMON_CONFIG_INIT(inst)
```

相关声明：[INPUT_TOUCH_DT_INST_COMMON_CONFIG_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__touch__events.html#ga354195b719d526cebd63a061e8dc408b)。

根据设备树实例初始化触摸屏通用配置。

<a id="r_ga0b82cc636a4b686ee2948dc704fd06f0"></a>

```c
#define INPUT_TOUCH_STRUCT_CHECK(config)
```

相关声明：[INPUT_TOUCH_STRUCT_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__touch__events.html#ga0b82cc636a4b686ee2948dc704fd06f0)。

验证通用配置结构体的偏移量（offset）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 25.3\_函数（Functions）

<a id="r_ga646bb86aa9f942fc3065381bd19e545c"></a>

```c
void input_touchscreen_report_pos (const struct device *dev, uint32_t x, uint32_t y, k_timeout_t timeout)
```

相关声明：[input_touchscreen_report_pos](https://docs.zephyrproject.org/latest/doxygen/html/group__touch__events.html#ga646bb86aa9f942fc3065381bd19e545c)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

报告触摸屏位置事件（touchscreen position events）的通用工具函数。


## 25.4\_原页交叉引用（Cross References）

- [zephyr/input/input.h](../api_source_reference/P376_input.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P388_input_touch.h_源码浏览.md)
- [input_touchscreen_common_config](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md)
- [INPUT_TOUCH_OUTPUT_DIM](https://docs.zephyrproject.org/latest/doxygen/html/group__touch__events.html#ga7a96be130c0c6577f4cc835d6634462f)
- [INPUT_TOUCH_DT_COMMON_CONFIG_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__touch__events.html#gae19dc2c40a8e14d28db614dfd4c5e32b)
- [INPUT_TOUCH_DT_INST_COMMON_CONFIG_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__touch__events.html#ga354195b719d526cebd63a061e8dc408b)
- [INPUT_TOUCH_STRUCT_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__touch__events.html#ga0b82cc636a4b686ee2948dc704fd06f0)
- [input_touchscreen_report_pos](https://docs.zephyrproject.org/latest/doxygen/html/group__touch__events.html#ga646bb86aa9f942fc3065381bd19e545c)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)

<a id="header-details"></a>

---

[上一章](P024_zephyr__input__input_analog_axis.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P026_zephyr__drivers__interrupt_controller__intc_rz_icu.h_文件参考.md)
