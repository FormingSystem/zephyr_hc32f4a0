---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-10
title: _input_（输入）。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_\_input\_（输入）。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

输入设备接口。

<a id="details"></a>

输入设备接口（Interfaces for Input Devices）。**引入版本（Since）：**3.4。**版本（Version）：**0.1.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 10.1\_主题（Topics）

<a id="r_input_5Fanalog_5Faxis"></a>

相关声明：[模拟轴（Analog axis）](../api_network_time_topic_reference/P016_模拟轴（Analog axis）.md)。

<a id="r_input_5Finterface_5Fext"></a>

相关声明：[设备专用输入 API 扩展（Device-specific Input API extensions）](../api_topic_reference/P040_设备专用输入 API 扩展（Device-specific Input API extensions）.md)。

具有标准输入 API 之外扩展功能的输入设备接口。

<a id="r_input_5Fevents"></a>

相关声明：[输入事件定义（Input Event Definitions）](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html)。

<a id="r_input_5Fkbd_5Fmatrix"></a>

相关声明：[键盘矩阵（Keyboard Matrix）](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html)。

<a id="r_input_5Fkeymap"></a>

相关声明：[键位映射实用工具（Keymap utilities）](../api_device_topic_reference/P012_键位映射实用工具（Keymap utilities）.md)。

<a id="r_lvgl_5Fkeypad_5Fdt"></a>

相关声明：[LVGL 键盘按键（Keypad keys）](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md)。

供设备树（Devicetree）使用的预定义 LVGL 按键。

<a id="r_touch_5Fevents"></a>

相关声明：[触摸屏事件（Touchscreen Events）](../api_network_time_topic_reference/P025_触摸屏事件（Touchscreen Events）.md)。

<a id="header-files"></a>
<a id="files"></a>

## 10.2\_文件（Files）

<a id="r_input_2Eh"></a>

```c
file input.h
```

相关声明：[input.h](../api_file_system_device_reference/P018_zephyr__input__input.h_文件参考.md)。

输入（Input）驱动API的主头文件。

<a id="r_input_5Fhid_2Eh"></a>

```c
file input_hid.h
```

相关声明：[input_hid.h](../api_file_configuration_reference/P042_zephyr__input__input_hid.h_文件参考.md)。

输入代码到HID代码/修饰键（Code / Modifier）转换工具的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.3\_数据结构（Data Structures）

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

## 10.4\_宏定义（Macros）

<a id="r_gad3e7310625b14db2e6930f66dfd879a7"></a>

```c
#define INPUT_CALLBACK_DEFINE_NAMED(_dev, _callback, _user_data, name)
```

相关声明：[INPUT_CALLBACK_DEFINE_NAMED](#gad3e7310625b14db2e6930f66dfd879a7)。

使用自定义名称注册输入事件（input events）的回调结构体。

<a id="r_gac986cdf392f9aa0a771c8e4e92c479a3"></a>

```c
#define INPUT_CALLBACK_DEFINE(_dev, _callback, _user_data)
```

相关声明：[INPUT_CALLBACK_DEFINE](#gac986cdf392f9aa0a771c8e4e92c479a3)。

注册输入事件的回调结构体。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.5\_函数（Functions）

<a id="r_gafe511e2ca9402ff539ebd05b8f28929e"></a>

```c
int input_report (const struct device *dev, uint8_t type, uint16_t code, int32_t value, bool sync, k_timeout_t timeout)
```

相关声明：[input_report](#gafe511e2ca9402ff539ebd05b8f28929e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

上报新的输入事件。

<a id="r_gaeb9fa2d4bb990e67ab0a2bd20a141d20"></a>

```c
static int input_report_key (const struct device *dev, uint16_t code, int32_t value, bool sync, k_timeout_t timeout)
```

相关声明：[input_report_key](#gaeb9fa2d4bb990e67ab0a2bd20a141d20)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

上报新的 `INPUT_EV_KEY` 输入事件；注意，`value` 会转换为 0 或 1。

<a id="r_gaffbf85b82d0cede81410dda8ed559201"></a>

```c
static int input_report_rel (const struct device *dev, uint16_t code, int32_t value, bool sync, k_timeout_t timeout)
```

相关声明：[input_report_rel](#gaffbf85b82d0cede81410dda8ed559201)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

上报新的 `INPUT_EV_REL` 输入事件。

<a id="r_gaf94bdc8ca673de7947e011872f64ce6c"></a>

```c
static int input_report_abs (const struct device *dev, uint16_t code, int32_t value, bool sync, k_timeout_t timeout)
```

相关声明：[input_report_abs](#gaf94bdc8ca673de7947e011872f64ce6c)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

上报新的 `INPUT_EV_ABS` 输入事件。

<a id="r_ga401a03bb89dd59d518f7466a035571da"></a>

```c
bool input_queue_empty (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[input_queue_empty](#ga401a03bb89dd59d518f7466a035571da)。

输入队列（input queue）为空时返回 true。

<a id="r_ga094b3ccfc2e111c4b2a000e9c2fe133c"></a>

```c
int16_t input_to_hid_code (uint16_t input_code)
```

相关声明：[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[input_to_hid_code](#ga094b3ccfc2e111c4b2a000e9c2fe133c)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将输入代码（Input Code）转换为人机接口设备代码（HID Code）。

<a id="r_ga86ac2267d08e91bcc09c5b091042cfde"></a>

```c
uint8_t input_to_hid_modifier (uint16_t input_code)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[input_to_hid_modifier](#ga86ac2267d08e91bcc09c5b091042cfde)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将输入代码（Input Code）转换为人机接口设备修饰符（HID Modifier）。

## 10.6\_详细说明（Detailed Documentation）

<a id="gac986cdf392f9aa0a771c8e4e92c479a3"></a>

### `INPUT_CALLBACK_DEFINE`

```c
#define INPUT_CALLBACK_DEFINE ( _dev, _callback, _user_data )
```

```c
#include <zephyr/input/input.h>
```

展开值（Value）：

```c
INPUT_CALLBACK_DEFINE_NAMED(_dev, _callback, _user_data, _callback)
```

注册输入事件的回调结构体。

`_dev` 字段可用于仅在指定设备生成事件时调用回调；将 `dev` 设为 `NULL` 会对每个事件调用回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_dev` | 设备指针或 `NULL`。 |
| `_callback` | 回调函数。 |
| `_user_data` | 指向用户指定数据（User-specified Data）的指针。 |

<a id="gad3e7310625b14db2e6930f66dfd879a7"></a>

### `INPUT_CALLBACK_DEFINE_NAMED`

```c
#define INPUT_CALLBACK_DEFINE_NAMED ( _dev, _callback, _user_data, name )
```

```c
#include <zephyr/input/input.h>
```

展开值（Value）：

```c
static const STRUCT_SECTION_ITERABLE(input_callback,                   \
                                     _input_callback__##name) = {      \
        .dev = _dev,                                                   \
        .callback = _callback,                                         \
        .user_data = _user_data,                                       \
}
```

使用自定义名称注册输入事件（input events）的回调结构体。

与 `INPUT_CALLBACK_DEFINE` 相同，但允许为回调结构体指定自定义名称（Custom Name）。同一回调函数对应多个回调时很有用。

<a id="ga401a03bb89dd59d518f7466a035571da"></a>

### `input_queue_empty()`

```c
bool input_queue_empty ( void )
```

```c
#include <zephyr/input/input.h>
```

输入队列（input queue）为空时返回 true。

可用于批量处理输入事件（Input Events），直到整个队列清空。启用 `CONFIG_INPUT_MODE_SYNCHRONOUS` 时始终返回 `true`。

<a id="gafe511e2ca9402ff539ebd05b8f28929e"></a>

### `input_report()`

```c
int input_report ( const struct device * dev, uint8_t type, uint16_t code, int32_t value, bool sync, k_timeout_t timeout )
```

```c
#include <zephyr/input/input.h>
```

上报新的输入事件。

使指定设备的全部回调被执行；可以同步执行，也可以在使用输入线程（Input Thread）时经该线程执行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 产生事件的设备，或者 `NULL`。 |
| `type` | 事件类型，参见 `INPUT_EV_CODES`。 |
| `code` | 事件代码，参见 `INPUT_KEY_CODES`、`INPUT_BTN_CODES`、`INPUT_ABS_CODES`、`INPUT_REL_CODES` 和 `INPUT_MSC_CODES`。 |
| `value` | 事件值。 |
| `sync` | 设置事件的同步位（Synchronization Bit）。 |
| `timeout` | 报告事件的超时时间（Timeout）；使用 `CONFIG_INPUT_MODE_SYNCHRONOUS` 时忽略。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 消息已处理（Processed）时。 |
| `<0` | 启用 `CONFIG_INPUT_MODE_THREAD` 且消息入队失败时为负值。 |

<a id="gaf94bdc8ca673de7947e011872f64ce6c"></a>

### `input_report_abs()`

```c
int input_report_abs ( const struct device * dev, uint16_t code, int32_t value, bool sync, k_timeout_t timeout )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/input/input.h>
```

上报新的 `INPUT_EV_ABS` 输入事件。

绝对坐标事件（Absolute Coordinate Event）。

**参阅（See Also）**：**另见（See Also）：**更多细节参见 `input_report()`。

<a id="gaeb9fa2d4bb990e67ab0a2bd20a141d20"></a>

### `input_report_key()`

```c
int input_report_key ( const struct device * dev, uint16_t code, int32_t value, bool sync, k_timeout_t timeout )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/input/input.h>
```

上报新的 `INPUT_EV_KEY` 输入事件；注意，`value` 会转换为 0 或 1。

按键事件（Key Event）。

**参阅（See Also）**：**另见（See Also）：**更多细节参见 `input_report()`。

<a id="gaffbf85b82d0cede81410dda8ed559201"></a>

### `input_report_rel()`

```c
int input_report_rel ( const struct device * dev, uint16_t code, int32_t value, bool sync, k_timeout_t timeout )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/input/input.h>
```

上报新的 `INPUT_EV_REL` 输入事件。

相对坐标事件（Relative Coordinate Event）。

**参阅（See Also）**：**另见（See Also）：**更多细节参见 `input_report()`。

<a id="ga094b3ccfc2e111c4b2a000e9c2fe133c"></a>

### `input_to_hid_code()`

```c
int16_t input_to_hid_code ( uint16_t input_code)
```

```c
#include <zephyr/input/input_hid.h>
```

将输入代码（Input Code）转换为人机接口设备代码（HID Code）。

接受输入代码（Input Code），返回对应 HID 代码。找不到时返回 `-1`；找到时返回值可安全转换为 `uint8_t`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `input_code` | 事件代码（Event Code），参见 `INPUT_KEY_CODES`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-1` | 指定输入代码没有对应 HID 代码时。 |

**返回（Returns）**：**返回值（Returns）：**输入代码对应的 HID 代码。

<a id="ga86ac2267d08e91bcc09c5b091042cfde"></a>

### `input_to_hid_modifier()`

```c
uint8_t input_to_hid_modifier ( uint16_t input_code)
```

```c
#include <zephyr/input/input_hid.h>
```

将输入代码（Input Code）转换为人机接口设备修饰符（HID Modifier）。

接受输入代码（Input Code），返回对应 HID 修饰键（Modifier），或返回 `0`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `input_code` | 事件代码（Event Code），参见 `INPUT_KEY_CODES`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 指定输入代码没有对应 HID 修饰键（Modifier）时。 |

**返回（Returns）**：**返回值（Returns）：**输入代码对应的 HID 修饰键（Modifier）。


## 10.7\_原页交叉引用（Cross References）

- [模拟轴（Analog axis）](../api_network_time_topic_reference/P016_模拟轴（Analog axis）.md)
- [设备专用输入 API 扩展（Device-specific Input API extensions）](../api_topic_reference/P040_设备专用输入 API 扩展（Device-specific Input API extensions）.md)
- [输入事件定义（Input Event Definitions）](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html)
- [键盘矩阵（Keyboard Matrix）](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html)
- [键位映射实用工具（Keymap utilities）](../api_device_topic_reference/P012_键位映射实用工具（Keymap utilities）.md)
- [LVGL 键盘按键（Keypad keys）](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md)
- [触摸屏事件（Touchscreen Events）](../api_network_time_topic_reference/P025_触摸屏事件（Touchscreen Events）.md)
- [input.h](../api_file_system_device_reference/P018_zephyr__input__input.h_文件参考.md)
- [input_hid.h](../api_file_configuration_reference/P042_zephyr__input__input_hid.h_文件参考.md)
- [input_event](../system_service_model_reference/P053_input_event_结构体.md)
- [input_callback](../system_service_model_reference/P052_input_callback_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [INPUT_EV_KEY](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#ga4a517c31bdbdd1bd82ba456d256ef1f1)
- [INPUT_EV_REL](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#ga02de6c85efab3d21eb81e88e54d58e03)
- [INPUT_EV_ABS](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#gaa6bcd6755fbdb3eb103f03a72759ce4f)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)
- [CONFIG_INPUT_MODE_SYNCHRONOUS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_MODE_SYNCHRONOUS)
- [INPUT_EV_CODES](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#INPUT_EV_CODES)
- [INPUT_KEY_CODES](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#INPUT_KEY_CODES)
- [INPUT_BTN_CODES](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#INPUT_BTN_CODES)
- [INPUT_ABS_CODES](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#INPUT_ABS_CODES)
- [INPUT_REL_CODES](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#INPUT_REL_CODES)
- [INPUT_MSC_CODES](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html#INPUT_MSC_CODES)
- [CONFIG_INPUT_MODE_THREAD](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_MODE_THREAD)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__input__interface_html_gad3e7310625b14db2e6930f66dfd879a7"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructinput__callback_html"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P009_IEEE 802.15.4 二层（L2）.md) · [返回大纲](大纲.md) · [下一章](P011_LSM6DSO API主题.md)
