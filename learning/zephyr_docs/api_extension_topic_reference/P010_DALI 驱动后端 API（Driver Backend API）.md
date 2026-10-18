---
id: learning.zephyr-docs.api-extension-topic-reference.page-10
title: DALI 驱动后端 API（Driver Backend API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_DALI 驱动后端 API（Driver Backend API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现数字可寻址照明接口驱动（DALI Driver）所需的 API 类型定义（Type Definitions）、回调签名（Callback Signatures）及其他辅助工具（Helpers）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.1\_数据结构（Data Structures）

<a id="r_dali_5Fdriver_5Fapi"></a>

```c
struct dali_driver_api
```

相关声明：[dali_driver_api](../peripheral_bus_storage_model_reference/P001_dali_driver_api_结构体.md)。

驱动操作（Driver Operations）：数字可寻址照明接口（DALI）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 10.2\_类型定义（Typedefs）

<a id="r_ga00ceb1581576430fa6864a073eaa73b0"></a>

```c
typedef int(* dali_api_set_receive_callback_t) (const struct device *dev, dali_receive_callback_t callback, void *user_data)
```

相关声明：[dali_api_set_receive_callback_t](#ga00ceb1581576430fa6864a073eaa73b0)、[device](../device_reference/P002_设备对象结构.md)、[dali_receive_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga7fc3646c3814fb3bebba8e77e0c0d424)。

用于接收 DALI 帧的 API。

<a id="r_gac6b54d7e448fd97e8936d4fd04177da0"></a>

```c
typedef int(* dali_api_transmit_t) (const struct device *dev, const struct dali_frame *frame, dali_transmit_callback_t callback, void *user_data)
```

相关声明：[dali_api_transmit_t](#gac6b54d7e448fd97e8936d4fd04177da0)、[device](../device_reference/P002_设备对象结构.md)、[dali_frame](../peripheral_bus_storage_model_reference/P002_dali_frame_结构体.md)、[dali_transmit_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga7ab4bdd2312ee38e473e7a2b56983166)。

用于发送 DALI 帧的 API。

## 10.3\_详细说明（Detailed Documentation）

<a id="ga00ceb1581576430fa6864a073eaa73b0"></a>

### `dali_api_set_receive_callback_t`

```c
typedef int(* dali_api_set_receive_callback_t) (const struct device *dev, dali_receive_callback_t callback, void *user_data)
```

```c
#include <zephyr/drivers/dali.h>
```

用于接收 DALI 帧的 API。

**参阅（See Also）**：另请参见（See Also）`dali_set_receive_callback()` 的参数说明（Argument Description）。

<a id="gac6b54d7e448fd97e8936d4fd04177da0"></a>

### `dali_api_transmit_t`

```c
typedef int(* dali_api_transmit_t) (const struct device *dev, const struct dali_frame *frame, dali_transmit_callback_t callback, void *user_data)
```

```c
#include <zephyr/drivers/dali.h>
```

用于发送 DALI 帧的 API。

**参阅（See Also）**：另请参见（See Also）`dali_transmit()` 的参数说明（Argument Description）。


## 10.4\_原页交叉引用（Cross References）

- [dali_driver_api](../peripheral_bus_storage_model_reference/P001_dali_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [dali_receive_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga7fc3646c3814fb3bebba8e77e0c0d424)
- [dali_frame](../peripheral_bus_storage_model_reference/P002_dali_frame_结构体.md)
- [dali_transmit_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga7ab4bdd2312ee38e473e7a2b56983166)
- [zephyr/drivers/dali.h](../peripheral_bus_storage_header_reference/P001_zephyr__drivers__dali.h_头文件参考.md)
- [dali_set_receive_callback()](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga79f624e680f364a0790119b3d5e09083)
- [dali_transmit()](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#gac25513281a022dce8bfe4a2fe46b609e)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P009_CY8CMBR3xxx API主题.md) · [返回大纲](大纲.md) · [下一章](P011_Xilinx ADMA 专用功能（Specifics）.md)
