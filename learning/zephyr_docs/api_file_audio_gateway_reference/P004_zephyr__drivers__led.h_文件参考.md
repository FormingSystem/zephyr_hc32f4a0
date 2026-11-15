---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-4
title: zephyr__drivers__led.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2led_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_drivers\_\_led.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2led_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

发光二极管（LED）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/syscalls/led.h>
```

查看此文件的源码。

发光二极管（LED）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_led_5Finfo"></a>

```c
struct led_info
```

相关声明：[led_info](../hardware/P204_LED信息结构.md)。

LED信息结构（Information Structure）。

<a id="r_led_5Fdriver_5Fapi"></a>

```c
struct led_driver_api
```

相关声明：[led_driver_api](../hardware/P206_LED驱动函数表.md)。

驱动操作（Driver Operations）：发光二极管（LED）驱动操作。

<a id="r_led_5Fdt_5Fspec"></a>

```c
struct led_dt_spec
```

相关声明：[led_dt_spec](../hardware/P203_LED设备树描述结构.md)。

设备树（Devicetree）所指定LED信息的容器。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_ga7bb18ca9f746ebcfbfc397886643f16d"></a>

```c
#define LED_BRIGHTNESS_MAX 100u
```

相关声明：[LED_BRIGHTNESS_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga7bb18ca9f746ebcfbfc397886643f16d)。

最大亮度等级（Brightness Level），范围为 0～100。

<a id="r_ga537f733ae3070fbe279834c76cda35ae"></a>

```c
#define LED_DT_SPEC_GET(node_id)
```

相关声明：[LED_DT_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga537f733ae3070fbe279834c76cda35ae)。

struct led_dt_spec 的静态初始化器（Static Initializer）。

<a id="r_gade3059194ce428783ea3e9900ed0be52"></a>

```c
#define LED_DT_SPEC_GET_OR(node_id, default_value)
```

相关声明：[LED_DT_SPEC_GET_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gade3059194ce428783ea3e9900ed0be52)。

类似 LED_DT_SPEC_GET()，但节点不存在时使用回退值（Fallback Value）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.3\_类型定义（Typedefs）

<a id="r_gad3c655794f58045459cbd910592d2cdd"></a>

```c
typedef int(* led_api_blink) (const struct device *dev, uint32_t led, uint32_t delay_on, uint32_t delay_off)
```

相关声明：[led_api_blink](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#gad3c655794f58045459cbd910592d2cdd)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

使 LED 闪烁（Blink）的回调 API。

<a id="r_ga3828b1e544a2f64378d5c3bfbbaa0c77"></a>

```c
typedef int(* led_api_get_info) (const struct device *dev, uint32_t led, const struct led_info **info)
```

相关声明：[led_api_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga3828b1e544a2f64378d5c3bfbbaa0c77)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[led_info](../hardware/P204_LED信息结构.md)。

获取 LED 信息（Information）的可选 API 回调。

<a id="r_gae24caa14f6aa41c2a509d2eaf468463f"></a>

```c
typedef int(* led_api_set_brightness) (const struct device *dev, uint32_t led, uint8_t value)
```

相关声明：[led_api_set_brightness](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#gae24caa14f6aa41c2a509d2eaf468463f)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 LED 亮度（Brightness）的回调 API。

<a id="r_ga977317f3208d5336463edf9979def4ae"></a>

```c
typedef int(* led_api_set_color) (const struct device *dev, uint32_t led, uint8_t num_colors, const uint8_t *color)
```

相关声明：[led_api_set_color](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga977317f3208d5336463edf9979def4ae)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 LED 颜色（Colors）的可选 API 回调。

<a id="r_gad13f55702668133575658d2ccc295339"></a>

```c
typedef int(* led_api_on) (const struct device *dev, uint32_t led)
```

相关声明：[led_api_on](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#gad13f55702668133575658d2ccc295339)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

点亮 LED 的回调 API。

<a id="r_ga5ae67fe64f97b0e716f9eb2f3a34f1fd"></a>

```c
typedef int(* led_api_off) (const struct device *dev, uint32_t led)
```

相关声明：[led_api_off](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga5ae67fe64f97b0e716f9eb2f3a34f1fd)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

熄灭 LED 的回调 API。

<a id="r_ga66dac12510c3a2281378d532ba6db2ae"></a>

```c
typedef int(* led_api_write_channels) (const struct device *dev, uint32_t start_channel, uint32_t num_channels, const uint8_t *buf)
```

相关声明：[led_api_write_channels](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga66dac12510c3a2281378d532ba6db2ae)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入一组连续 LED 通道（Strip of LED Channels）的回调 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.4\_函数（Functions）

<a id="r_ga4f31fecd215e5597999be4d16b0d2dd5"></a>

```c
int led_blink (const struct device *dev, uint32_t led, uint32_t delay_on, uint32_t delay_off)
```

相关声明：[led_blink](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga4f31fecd215e5597999be4d16b0d2dd5)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

使 LED 闪烁（Blink）。

<a id="r_ga9925483b97073354f7be6b40aa2dad1a"></a>

```c
int led_get_info (const struct device *dev, uint32_t led, const struct led_info **info)
```

相关声明：[led_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga9925483b97073354f7be6b40aa2dad1a)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[led_info](../hardware/P204_LED信息结构.md)。

获取 LED 信息（Information）。

<a id="r_gaca479fd77518331f4fc84f788e345882"></a>

```c
int led_set_brightness (const struct device *dev, uint32_t led, uint8_t value)
```

相关声明：[led_set_brightness](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gaca479fd77518331f4fc84f788e345882)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 LED 亮度（Brightness）。

<a id="r_ga24d4007f81483d0fe8b9988288adf59a"></a>

```c
int led_write_channels (const struct device *dev, uint32_t start_channel, uint32_t num_channels, const uint8_t *buf)
```

相关声明：[led_write_channels](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga24d4007f81483d0fe8b9988288adf59a)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入／更新一组连续 LED 通道（Strip of LED Channels）。

<a id="r_ga717bdbe76331b6286c58feb6e3e214dd"></a>

```c
int led_set_channel (const struct device *dev, uint32_t channel, uint8_t value)
```

相关声明：[led_set_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga717bdbe76331b6286c58feb6e3e214dd)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置单个 LED 通道（Channel）。

<a id="r_ga94dd46cc96f6ade5cebaa46a5f7ca5ea"></a>

```c
int led_set_color (const struct device *dev, uint32_t led, uint8_t num_colors, const uint8_t *color)
```

相关声明：[led_set_color](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga94dd46cc96f6ade5cebaa46a5f7ca5ea)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 LED 颜色（Color）。

<a id="r_gad4daafd7fcab22d1d68745b7264d0f73"></a>

```c
int led_on (const struct device *dev, uint32_t led)
```

相关声明：[led_on](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gad4daafd7fcab22d1d68745b7264d0f73)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

点亮 LED。

<a id="r_ga22c9dbe76f06fec327aebe06448d1542"></a>

```c
int led_off (const struct device *dev, uint32_t led)
```

相关声明：[led_off](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga22c9dbe76f06fec327aebe06448d1542)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

熄灭 LED。

<a id="r_gab3581c7571b4623696ad57d25d6bd96f"></a>

```c
static int led_blink_dt (const struct led_dt_spec *spec, uint32_t delay_on, uint32_t delay_off)
```

相关声明：[led_blink_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gab3581c7571b4623696ad57d25d6bd96f)、[led_dt_spec](../hardware/P203_LED设备树描述结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

根据 led_dt_spec 使 LED 闪烁（Blink）。

<a id="r_ga01ee05a71058adf86e950805524865a0"></a>

```c
static int led_get_info_dt (const struct led_dt_spec *spec, const struct led_info **info)
```

相关声明：[led_get_info_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga01ee05a71058adf86e950805524865a0)、[led_dt_spec](../hardware/P203_LED设备树描述结构.md)、[led_info](../hardware/P204_LED信息结构.md)。

根据 led_dt_spec 获取 LED 信息（Information）。

<a id="r_gaecc33acfc2b1dde870b411d7f30eed82"></a>

```c
static int led_set_brightness_dt (const struct led_dt_spec *spec, uint8_t value)
```

相关声明：[led_set_brightness_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gaecc33acfc2b1dde870b411d7f30eed82)、[led_dt_spec](../hardware/P203_LED设备树描述结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据 led_dt_spec 设置 LED 亮度（Brightness）。

<a id="r_ga4a30a26f21d80f40ce3364880e0dfee3"></a>

```c
static int led_set_color_dt (const struct led_dt_spec *spec, uint8_t num_colors, const uint8_t *color)
```

相关声明：[led_set_color_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga4a30a26f21d80f40ce3364880e0dfee3)、[led_dt_spec](../hardware/P203_LED设备树描述结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据 struct led_dt_spec 设置 LED 颜色（Color）。

<a id="r_gaa2b262a309e4ede4cb5715c69d900804"></a>

```c
static int led_on_dt (const struct led_dt_spec *spec)
```

相关声明：[led_on_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gaa2b262a309e4ede4cb5715c69d900804)、[led_dt_spec](../hardware/P203_LED设备树描述结构.md)。

根据 struct led_dt_spec 点亮 LED。

<a id="r_ga8b6618e4fea4f44f218f95fd16abc16b"></a>

```c
static int led_off_dt (const struct led_dt_spec *spec)
```

相关声明：[led_off_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga8b6618e4fea4f44f218f95fd16abc16b)、[led_dt_spec](../hardware/P203_LED设备树描述结构.md)。

根据 struct led_dt_spec 熄灭 LED。

<a id="r_gaa2994b959c730dad3432481bba278497"></a>

```c
static bool led_is_ready_dt (const struct led_dt_spec *spec)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[led_is_ready_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gaa2994b959c730dad3432481bba278497)、[led_dt_spec](../hardware/P203_LED设备树描述结构.md)。

验证 LED 设备已就绪（Ready）。


## 4.5\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P042_led.h_源码浏览.md)
- [led_info](../hardware/P204_LED信息结构.md)
- [led_driver_api](../hardware/P206_LED驱动函数表.md)
- [led_dt_spec](../hardware/P203_LED设备树描述结构.md)
- [LED_BRIGHTNESS_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga7bb18ca9f746ebcfbfc397886643f16d)
- [LED_DT_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga537f733ae3070fbe279834c76cda35ae)
- [LED_DT_SPEC_GET_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gade3059194ce428783ea3e9900ed0be52)
- [led_api_blink](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#gad3c655794f58045459cbd910592d2cdd)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [led_api_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga3828b1e544a2f64378d5c3bfbbaa0c77)
- [led_api_set_brightness](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#gae24caa14f6aa41c2a509d2eaf468463f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [led_api_set_color](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga977317f3208d5336463edf9979def4ae)
- [led_api_on](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#gad13f55702668133575658d2ccc295339)
- [led_api_off](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga5ae67fe64f97b0e716f9eb2f3a34f1fd)
- [led_api_write_channels](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface__backend.html#ga66dac12510c3a2281378d532ba6db2ae)
- [led_blink](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga4f31fecd215e5597999be4d16b0d2dd5)
- [led_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga9925483b97073354f7be6b40aa2dad1a)
- [led_set_brightness](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gaca479fd77518331f4fc84f788e345882)
- [led_write_channels](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga24d4007f81483d0fe8b9988288adf59a)
- [led_set_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga717bdbe76331b6286c58feb6e3e214dd)
- [led_set_color](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga94dd46cc96f6ade5cebaa46a5f7ca5ea)
- [led_on](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gad4daafd7fcab22d1d68745b7264d0f73)
- [led_off](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga22c9dbe76f06fec327aebe06448d1542)
- [led_blink_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gab3581c7571b4623696ad57d25d6bd96f)
- [led_get_info_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga01ee05a71058adf86e950805524865a0)
- [led_set_brightness_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gaecc33acfc2b1dde870b411d7f30eed82)
- [led_set_color_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga4a30a26f21d80f40ce3364880e0dfee3)
- [led_on_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gaa2b262a309e4ede4cb5715c69d900804)
- [led_off_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga8b6618e4fea4f44f218f95fd16abc16b)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [led_is_ready_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gaa2994b959c730dad3432481bba278497)

<a id="header-details"></a>

---

[上一章](P003_zephyr__drivers__bluetooth.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__dt-bindings__clock__esp32_clock.h_文件参考.md)
