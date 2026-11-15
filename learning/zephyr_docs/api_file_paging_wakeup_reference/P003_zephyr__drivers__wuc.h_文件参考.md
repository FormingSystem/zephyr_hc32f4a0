---
id: learning.zephyr-docs.api-file-paging-wakeup-reference.page-3
title: zephyr__drivers__wuc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2wuc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_drivers\_\_wuc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2wuc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

唤醒控制器（Wakeup Controller，WUC）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <stddef.h>
#include <zephyr/device.h>
```

查看此文件的源码。

唤醒控制器（Wakeup Controller，WUC）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_wuc_5Fdt_5Fspec"></a>

```c
struct wuc_dt_spec
```

相关声明：[wuc_dt_spec](../device_power_control_model_reference/P103_wuc_dt_spec_结构体.md)。

唤醒控制器（Wakeup Controller）的设备配置。

<a id="r_wuc_5Fdriver_5Fapi"></a>

```c
struct wuc_driver_api
```

相关声明：[wuc_driver_api](../device_power_control_model_reference/P102_wuc_driver_api_结构体.md)。

驱动操作（Driver Operations）：唤醒控制器（WUC）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_gab16abb3ef7b60f6aeb2ada2f426a396b"></a>

```c
#define WUC_DT_SPEC_GET_BY_IDX(node_id, idx)
```

相关声明：[WUC_DT_SPEC_GET_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gab16abb3ef7b60f6aeb2ada2f426a396b)。

`wuc_dt_spec` 的静态初始化器（Static Initializer）。

<a id="r_gaea86f159bca2896a315c4909e4755abb"></a>

```c
#define WUC_DT_SPEC_GET_BY_IDX_OR(node_id, idx, default_value)
```

相关声明：[WUC_DT_SPEC_GET_BY_IDX_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gaea86f159bca2896a315c4909e4755abb)。

类似 `WUC_DT_SPEC_GET_BY_IDX()`，但可回退到默认值（Default Value）。

<a id="r_ga83d434b9c2b26dcd448d0b53c63ff295"></a>

```c
#define WUC_DT_SPEC_GET(node_id)
```

相关声明：[WUC_DT_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga83d434b9c2b26dcd448d0b53c63ff295)。

等价于 `WUC_DT_SPEC_GET_BY_IDX(node_id, 0)`。

<a id="r_ga78290ca0574db5ac06eba7d0218d4de9"></a>

```c
#define WUC_DT_SPEC_GET_OR(node_id, default_value)
```

相关声明：[WUC_DT_SPEC_GET_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga78290ca0574db5ac06eba7d0218d4de9)。

等价于 `WUC_DT_SPEC_GET_BY_IDX_OR(node_id, 0, default_value)`。

<a id="r_ga7605bb886d41618ae57768cfc5f356a1"></a>

```c
#define WUC_DT_SPEC_INST_GET_BY_IDX(inst, idx)
```

相关声明：[WUC_DT_SPEC_INST_GET_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga7605bb886d41618ae57768cfc5f356a1)。

根据 `DT_DRV_COMPAT` 实例的唤醒控制器属性（Wakeup Controller Property）中指定索引处的条目，构造 `wuc_dt_spec` 静态初始化器。

<a id="r_ga73532298336d56886a2d23d67144c9cb"></a>

```c
#define WUC_DT_SPEC_INST_GET_BY_IDX_OR(inst, idx, default_value)
```

相关声明：[WUC_DT_SPEC_INST_GET_BY_IDX_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga73532298336d56886a2d23d67144c9cb)。

根据 `DT_DRV_COMPAT` 实例的 `wakeup-ctrls` 属性中指定索引处的条目，构造 `wuc_dt_spec` 静态初始化器，并提供回退值（Fallback）。

<a id="r_gaa461bbeb02ca0f795104705916a33d76"></a>

```c
#define WUC_DT_SPEC_INST_GET(inst)
```

相关声明：[WUC_DT_SPEC_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gaa461bbeb02ca0f795104705916a33d76)。

等价于 `WUC_DT_SPEC_INST_GET_BY_IDX(inst, 0)`。

<a id="r_gaa3897de51a6f6d2d94b2beeec6cacb6d"></a>

```c
#define WUC_DT_SPEC_INST_GET_OR(inst, default_value)
```

相关声明：[WUC_DT_SPEC_INST_GET_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gaa3897de51a6f6d2d94b2beeec6cacb6d)。

等价于 `WUC_DT_SPEC_INST_GET_BY_IDX_OR(node_id, 0, default_value)`。参数名 `node_id` 按原文保留。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.3\_类型定义（Typedefs）

<a id="r_ga94ca8c28ef9f1328ddddd3a5489204e2"></a>

```c
typedef int(* wuc_api_enable_wakeup_source) (const struct device *dev, uint32_t id)
```

相关声明：[wuc_api_enable_wakeup_source](../api_connection_topic_reference/P023_WUC 驱动后端 API.md#ga94ca8c28ef9f1328ddddd3a5489204e2)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

用于启用唤醒源（wakeup source）的回调 API。

<a id="r_gad36d204bead7c8ce4999858d16dca3ad"></a>

```c
typedef int(* wuc_api_disable_wakeup_source) (const struct device *dev, uint32_t id)
```

相关声明：[wuc_api_disable_wakeup_source](../api_connection_topic_reference/P023_WUC 驱动后端 API.md#gad36d204bead7c8ce4999858d16dca3ad)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

用于禁用唤醒源的回调 API。

<a id="r_ga821a6abcc315fcd10e88e2f45641127e"></a>

```c
typedef int(* wuc_api_check_wakeup_source_triggered) (const struct device *dev, uint32_t id)
```

相关声明：[wuc_api_check_wakeup_source_triggered](../api_connection_topic_reference/P023_WUC 驱动后端 API.md#ga821a6abcc315fcd10e88e2f45641127e)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

用于检查唤醒源是否已触发的回调 API。

<a id="r_ga52c4fa3a73d2f3ef392c61b6c0133f6b"></a>

```c
typedef int(* wuc_api_clear_wakeup_source_triggered) (const struct device *dev, uint32_t id)
```

相关声明：[wuc_api_clear_wakeup_source_triggered](../api_connection_topic_reference/P023_WUC 驱动后端 API.md#ga52c4fa3a73d2f3ef392c61b6c0133f6b)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

用于清除唤醒源触发状态的回调 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.4\_函数（Functions）

<a id="r_ga28999754c6980fcfdae275adb0e811be"></a>

```c
static int wuc_enable_wakeup_source (const struct device *dev, uint32_t id)
```

相关声明：[wuc_enable_wakeup_source](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga28999754c6980fcfdae275adb0e811be)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

启用唤醒源（Wakeup Source）。

<a id="r_gac3747f4707d490e620963d1c46a19af8"></a>

```c
static int wuc_enable_wakeup_source_dt (const struct wuc_dt_spec *spec)
```

相关声明：[wuc_enable_wakeup_source_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gac3747f4707d490e620963d1c46a19af8)、[wuc_dt_spec](../device_power_control_model_reference/P103_wuc_dt_spec_结构体.md)。

使用 `wuc_dt_spec` 启用唤醒源（Wakeup Source）。

<a id="r_gacac1135652beabd7858f3b01683a973b"></a>

```c
static int wuc_disable_wakeup_source (const struct device *dev, uint32_t id)
```

相关声明：[wuc_disable_wakeup_source](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gacac1135652beabd7858f3b01683a973b)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

禁用唤醒源（Wakeup Source）。

<a id="r_ga7c7d2cc85a6b88cf01ce214f4f8e2904"></a>

```c
static int wuc_disable_wakeup_source_dt (const struct wuc_dt_spec *spec)
```

相关声明：[wuc_disable_wakeup_source_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga7c7d2cc85a6b88cf01ce214f4f8e2904)、[wuc_dt_spec](../device_power_control_model_reference/P103_wuc_dt_spec_结构体.md)。

使用 `wuc_dt_spec` 禁用唤醒源（Wakeup Source）。

<a id="r_gac03165353edf5e3a5273b60d7e1a1c8e"></a>

```c
static int wuc_check_wakeup_source_triggered (const struct device *dev, uint32_t id)
```

相关声明：[wuc_check_wakeup_source_triggered](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gac03165353edf5e3a5273b60d7e1a1c8e)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

检查唤醒源（Wakeup Source）是否已触发。

<a id="r_gab4a363a52e46b5d28fc8fb946ea7a29a"></a>

```c
static int wuc_check_wakeup_source_triggered_dt (const struct wuc_dt_spec *spec)
```

相关声明：[wuc_check_wakeup_source_triggered_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gab4a363a52e46b5d28fc8fb946ea7a29a)、[wuc_dt_spec](../device_power_control_model_reference/P103_wuc_dt_spec_结构体.md)。

使用 `wuc_dt_spec` 检查唤醒源（Wakeup Source）是否已触发。

<a id="r_ga4f280e6dc432be25c6a542abcf927b60"></a>

```c
static int wuc_clear_wakeup_source_triggered (const struct device *dev, uint32_t id)
```

相关声明：[wuc_clear_wakeup_source_triggered](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga4f280e6dc432be25c6a542abcf927b60)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

清除唤醒源的已触发状态（Triggered Status）。

<a id="r_gafce93565e572eaddc98006f33f127ef5"></a>

```c
static int wuc_clear_wakeup_source_triggered_dt (const struct wuc_dt_spec *spec)
```

相关声明：[wuc_clear_wakeup_source_triggered_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gafce93565e572eaddc98006f33f127ef5)、[wuc_dt_spec](../device_power_control_model_reference/P103_wuc_dt_spec_结构体.md)。

使用 `wuc_dt_spec` 清除唤醒源的已触发状态（Triggered Status）。


## 3.5\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P184_wuc.h_源码浏览.md)
- [wuc_dt_spec](../device_power_control_model_reference/P103_wuc_dt_spec_结构体.md)
- [wuc_driver_api](../device_power_control_model_reference/P102_wuc_driver_api_结构体.md)
- [WUC_DT_SPEC_GET_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gab16abb3ef7b60f6aeb2ada2f426a396b)
- [WUC_DT_SPEC_GET_BY_IDX_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gaea86f159bca2896a315c4909e4755abb)
- [WUC_DT_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga83d434b9c2b26dcd448d0b53c63ff295)
- [WUC_DT_SPEC_GET_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga78290ca0574db5ac06eba7d0218d4de9)
- [WUC_DT_SPEC_INST_GET_BY_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga7605bb886d41618ae57768cfc5f356a1)
- [WUC_DT_SPEC_INST_GET_BY_IDX_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga73532298336d56886a2d23d67144c9cb)
- [WUC_DT_SPEC_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gaa461bbeb02ca0f795104705916a33d76)
- [WUC_DT_SPEC_INST_GET_OR](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gaa3897de51a6f6d2d94b2beeec6cacb6d)
- [wuc_api_enable_wakeup_source](../api_connection_topic_reference/P023_WUC 驱动后端 API.md#ga94ca8c28ef9f1328ddddd3a5489204e2)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [wuc_api_disable_wakeup_source](../api_connection_topic_reference/P023_WUC 驱动后端 API.md#gad36d204bead7c8ce4999858d16dca3ad)
- [wuc_api_check_wakeup_source_triggered](../api_connection_topic_reference/P023_WUC 驱动后端 API.md#ga821a6abcc315fcd10e88e2f45641127e)
- [wuc_api_clear_wakeup_source_triggered](../api_connection_topic_reference/P023_WUC 驱动后端 API.md#ga52c4fa3a73d2f3ef392c61b6c0133f6b)
- [wuc_enable_wakeup_source](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga28999754c6980fcfdae275adb0e811be)
- [wuc_enable_wakeup_source_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gac3747f4707d490e620963d1c46a19af8)
- [wuc_disable_wakeup_source](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gacac1135652beabd7858f3b01683a973b)
- [wuc_disable_wakeup_source_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga7c7d2cc85a6b88cf01ce214f4f8e2904)
- [wuc_check_wakeup_source_triggered](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gac03165353edf5e3a5273b60d7e1a1c8e)
- [wuc_check_wakeup_source_triggered_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gab4a363a52e46b5d28fc8fb946ea7a29a)
- [wuc_clear_wakeup_source_triggered](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga4f280e6dc432be25c6a542abcf927b60)
- [wuc_clear_wakeup_source_triggered_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gafce93565e572eaddc98006f33f127ef5)

<a id="header-details"></a>

---

[上一章](P002_zephyr__drivers__firmware__scmi__protocol.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__dt-bindings__sensor__afbr_s50.h_文件参考.md)
