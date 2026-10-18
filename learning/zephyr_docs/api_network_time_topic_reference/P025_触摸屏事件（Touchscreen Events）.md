---
id: learning.zephyr-docs.api-network-time-topic-reference.page-25
title: 触摸屏事件（Touchscreen Events）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__touch__events.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_触摸屏事件（Touchscreen Events）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__touch__events.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

自 Zephyr 3.7 起提供；API 版本为 0.1.0。

<a id="header-files"></a>
<a id="files"></a>

## 25.1\_文件（Files）

<a id="r_input_5Ftouch_2Eh"></a>

```c
file input_touch.h
```

相关声明：[input_touch.h](../api_file_interface_reference/P025_zephyr__input__input_touch.h_文件参考.md)。

触摸事件（Touch Events）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 25.2\_数据结构（Data Structures）

<a id="r_input_5Ftouchscreen_5Fcommon_5Fconfig"></a>

```c
struct input_touchscreen_common_config
```

相关声明：[input_touchscreen_common_config](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md)。

通用触摸屏（Touchscreen）配置。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 25.3\_宏定义（Macros）

<a id="r_ga7a96be130c0c6577f4cc835d6634462f"></a>

```c
#define INPUT_TOUCH_OUTPUT_DIM(node_id, dim, prop)
```

相关声明：[INPUT_TOUCH_OUTPUT_DIM](#ga7a96be130c0c6577f4cc835d6634462f)。

从显示设备的 phandle 中选择一个输出尺寸（output dimension）；否则使用节点自身的属性。

<a id="r_gae19dc2c40a8e14d28db614dfd4c5e32b"></a>

```c
#define INPUT_TOUCH_DT_COMMON_CONFIG_INIT(node_id)
```

相关声明：[INPUT_TOUCH_DT_COMMON_CONFIG_INIT](#gae19dc2c40a8e14d28db614dfd4c5e32b)。

根据设备树（devicetree）初始化触摸屏通用配置（common touchscreen config）。

<a id="r_ga354195b719d526cebd63a061e8dc408b"></a>

```c
#define INPUT_TOUCH_DT_INST_COMMON_CONFIG_INIT(inst)
```

相关声明：[INPUT_TOUCH_DT_INST_COMMON_CONFIG_INIT](#ga354195b719d526cebd63a061e8dc408b)。

根据设备树实例初始化触摸屏通用配置。

<a id="r_ga0b82cc636a4b686ee2948dc704fd06f0"></a>

```c
#define INPUT_TOUCH_STRUCT_CHECK(config)
```

相关声明：[INPUT_TOUCH_STRUCT_CHECK](#ga0b82cc636a4b686ee2948dc704fd06f0)。

验证通用配置结构体的偏移量（offset）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 25.4\_函数（Functions）

<a id="r_ga646bb86aa9f942fc3065381bd19e545c"></a>

```c
void input_touchscreen_report_pos (const struct device *dev, uint32_t x, uint32_t y, k_timeout_t timeout)
```

相关声明：[input_touchscreen_report_pos](#ga646bb86aa9f942fc3065381bd19e545c)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

报告触摸屏位置事件（touchscreen position events）的通用工具函数。

## 25.5\_详细说明（Detailed Documentation）

<a id="gae19dc2c40a8e14d28db614dfd4c5e32b"></a>

### `INPUT_TOUCH_DT_COMMON_CONFIG_INIT`

```c
#define INPUT_TOUCH_DT_COMMON_CONFIG_INIT ( node_id)
```

```c
#include <zephyr/input/input_touch.h>
```

展开值（Value）：

```c
{                                                               \
        .screen_width = DT_PROP(node_id, screen_width),         \
        .screen_height = DT_PROP(node_id, screen_height),       \
        .inverted_x = DT_PROP(node_id, inverted_x),             \
        .inverted_y = DT_PROP(node_id, inverted_y),             \
        .swapped_x_y = DT_PROP(node_id, swapped_x_y),           \
        .output_width = INPUT_TOUCH_OUTPUT_DIM(node_id, width, output_width),   \
        .output_height = INPUT_TOUCH_OUTPUT_DIM(node_id, height, output_height),        \
}
```

根据设备树（devicetree）初始化触摸屏通用配置（common touchscreen config）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符。 |

<a id="ga354195b719d526cebd63a061e8dc408b"></a>

### `INPUT_TOUCH_DT_INST_COMMON_CONFIG_INIT`

```c
#define INPUT_TOUCH_DT_INST_COMMON_CONFIG_INIT ( inst)
```

```c
#include <zephyr/input/input_touch.h>
```

展开值（Value）：

```c
INPUT_TOUCH_DT_COMMON_CONFIG_INIT(DT_DRV_INST(inst))
```

根据设备树实例初始化触摸屏通用配置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例（instance）。 |

<a id="ga7a96be130c0c6577f4cc835d6634462f"></a>

### `INPUT_TOUCH_OUTPUT_DIM`

```c
#define INPUT_TOUCH_OUTPUT_DIM ( node_id, dim, prop )
```

```c
#include <zephyr/input/input_touch.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_PROP(node_id, display),                 \
        (DT_PROP(DT_PHANDLE(node_id, display), dim)),           \
        (DT_PROP_OR(node_id, prop, 0)))
```

从显示设备的 phandle 中选择一个输出尺寸（output dimension）；否则使用节点自身的属性。

优先使用 `display` 引用句柄（phandle）所指节点的宽度／高度；未设置 `display` 时回退到本节点自身的 `output-width`／`output-height`；两者均不存在时回退到 0，从而禁用缩放（scaling）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符。 |
| `dim` | 显示控制器尺寸属性，`width` 或 `height`。 |
| `prop` | 触摸屏回退属性（fallback property），`output_width` 或 `output_height`。 |

<a id="ga0b82cc636a4b686ee2948dc704fd06f0"></a>

### `INPUT_TOUCH_STRUCT_CHECK`

```c
#define INPUT_TOUCH_STRUCT_CHECK ( config)
```

```c
#include <zephyr/input/input_touch.h>
```

展开值（Value）：

```c
BUILD_ASSERT(offsetof(config, common) == 0, \
             "struct input_touchscreen_common_config must be placed first");
```

验证通用配置结构体的偏移量（offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `config` | 配置结构体（config structure）的名称。 |

<a id="ga646bb86aa9f942fc3065381bd19e545c"></a>

### `input_touchscreen_report_pos()`

```c
void input_touchscreen_report_pos ( const struct device * dev, uint32_t x, uint32_t y, k_timeout_t timeout )
```

```c
#include <zephyr/input/input_touch.h>
```

报告触摸屏位置事件（touchscreen position events）的通用工具函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 触摸屏控制器（touchscreen controller）。 |
| `x` | 控制器上报的 X 坐标。 |
| `y` | 控制器上报的 Y 坐标。 |
| `timeout` | 上报事件的超时。 |


## 25.6\_原页交叉引用（Cross References）

- [input_touch.h](../api_file_interface_reference/P025_zephyr__input__input_touch.h_文件参考.md)
- [input_touchscreen_common_config](../system_service_model_reference/P057_input_touchscreen_common_config_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [DT_NODE_HAS_PROP](../dt_identity_reference/P002_设备树存在性与状态宏.md#gacce67bf20541cd2d07d8540058964692)
- [DT_PHANDLE](../dt_property_reference/P001_设备树属性读取宏.md#ga7bd77c49472ba4547d87f00f40fd7171)
- [DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>
<a id="agroup__touch__events_html_ga7a96be130c0c6577f4cc835d6634462f"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__touch__events_html_gae19dc2c40a8e14d28db614dfd4c5e32b"></a>
<a id="agroup__devicetree-generic-exist_html_gacce67bf20541cd2d07d8540058964692"></a>
<a id="agroup__devicetree-generic-prop_html_ga5e5bfc9b1a6627b3f73014329e96340f"></a>
<a id="agroup__devicetree-generic-prop_html_ga7bd77c49472ba4547d87f00f40fd7171"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P024_基础协议（Base Protocol）.md) · [返回大纲](大纲.md) · [下一章](P026_USB-C 总线电源（VBUS）API.md)
