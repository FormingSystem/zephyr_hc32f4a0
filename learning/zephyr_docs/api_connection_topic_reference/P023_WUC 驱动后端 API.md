---
id: learning.zephyr-docs.api-connection-topic-reference.page-23
title: WUC 驱动后端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_WUC 驱动后端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现唤醒控制器（WUC）驱动所需的 API 类型定义、回调签名及其他辅助定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 23.1\_数据结构（Data Structures）

<a id="r_wuc_5Fdriver_5Fapi"></a>

```c
struct wuc_driver_api
```

相关声明：[wuc_driver_api](../device_power_control_model_reference/P102_wuc_driver_api_结构体.md)。

驱动操作（Driver Operations）：唤醒控制器（WUC）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 23.2\_类型定义（Typedefs）

<a id="r_ga94ca8c28ef9f1328ddddd3a5489204e2"></a>

```c
typedef int(* wuc_api_enable_wakeup_source) (const struct device *dev, uint32_t id)
```

相关声明：[wuc_api_enable_wakeup_source](#ga94ca8c28ef9f1328ddddd3a5489204e2)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

用于启用唤醒源（wakeup source）的回调 API。

<a id="r_gad36d204bead7c8ce4999858d16dca3ad"></a>

```c
typedef int(* wuc_api_disable_wakeup_source) (const struct device *dev, uint32_t id)
```

相关声明：[wuc_api_disable_wakeup_source](#gad36d204bead7c8ce4999858d16dca3ad)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

用于禁用唤醒源的回调 API。

<a id="r_ga821a6abcc315fcd10e88e2f45641127e"></a>

```c
typedef int(* wuc_api_check_wakeup_source_triggered) (const struct device *dev, uint32_t id)
```

相关声明：[wuc_api_check_wakeup_source_triggered](#ga821a6abcc315fcd10e88e2f45641127e)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

用于检查唤醒源是否已触发的回调 API。

<a id="r_ga52c4fa3a73d2f3ef392c61b6c0133f6b"></a>

```c
typedef int(* wuc_api_clear_wakeup_source_triggered) (const struct device *dev, uint32_t id)
```

相关声明：[wuc_api_clear_wakeup_source_triggered](#ga52c4fa3a73d2f3ef392c61b6c0133f6b)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

用于清除唤醒源触发状态的回调 API。

## 23.3\_详细说明（Detailed Documentation）

<a id="ga821a6abcc315fcd10e88e2f45641127e"></a>

### `wuc_api_check_wakeup_source_triggered`

```c
typedef int(* wuc_api_check_wakeup_source_triggered) (const struct device *dev, uint32_t id)
```

```c
#include <zephyr/drivers/wuc.h>
```

用于检查唤醒源是否已触发的回调 API。

参数说明参见 `wuc_check_wakeup_source_triggered()`。

<a id="ga52c4fa3a73d2f3ef392c61b6c0133f6b"></a>

### `wuc_api_clear_wakeup_source_triggered`

```c
typedef int(* wuc_api_clear_wakeup_source_triggered) (const struct device *dev, uint32_t id)
```

```c
#include <zephyr/drivers/wuc.h>
```

用于清除唤醒源触发状态的回调 API。

参数说明参见 `wuc_clear_wakeup_source_triggered()`。

<a id="gad36d204bead7c8ce4999858d16dca3ad"></a>

### `wuc_api_disable_wakeup_source`

```c
typedef int(* wuc_api_disable_wakeup_source) (const struct device *dev, uint32_t id)
```

```c
#include <zephyr/drivers/wuc.h>
```

用于禁用唤醒源的回调 API。

参数说明参见 `wuc_disable_wakeup_source()`。

<a id="ga94ca8c28ef9f1328ddddd3a5489204e2"></a>

### `wuc_api_enable_wakeup_source`

```c
typedef int(* wuc_api_enable_wakeup_source) (const struct device *dev, uint32_t id)
```

```c
#include <zephyr/drivers/wuc.h>
```

用于启用唤醒源（wakeup source）的回调 API。

参数说明参见 `wuc_enable_wakeup_source()`。


## 23.4\_原页交叉引用（Cross References）

- [wuc_driver_api](../device_power_control_model_reference/P102_wuc_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/drivers/wuc.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2wuc_8h.html)
- [wuc_check_wakeup_source_triggered()](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gac03165353edf5e3a5273b60d7e1a1c8e)
- [wuc_clear_wakeup_source_triggered()](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga4f280e6dc432be25c6a542abcf927b60)
- [wuc_disable_wakeup_source()](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#gacac1135652beabd7858f3b01683a973b)
- [wuc_enable_wakeup_source()](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html#ga28999754c6980fcfdae275adb0e811be)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P022_按字粒度访问内存 API（Word Granular Access Memory APIs）.md) · [返回大纲](大纲.md) · [下一章](P024_Xen 安全模块 FLASK（Xen XSM FLASK）.md)
