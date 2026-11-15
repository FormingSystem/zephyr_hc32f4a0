---
id: learning.zephyr-docs.api-connection-topic-reference.page-15
title: MSPI 驱动后端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_MSPI 驱动后端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现多位串行外设接口（MSPI）驱动所需的 API 类型定义、回调签名及其他辅助定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.1\_数据结构（Data Structures）

<a id="r_mspi_5Fdriver_5Fapi"></a>

```c
struct mspi_driver_api
```

相关声明：[mspi_driver_api](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md)。

驱动操作（Driver Operations）：MSPI驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 15.2\_类型定义（Typedefs）

<a id="r_ga2ff9209634fb241e2f7323e749df612e"></a>

```c
typedef int(* mspi_api_config) (const struct mspi_dt_spec *spec)
```

相关声明：[mspi_api_config](#ga2ff9209634fb241e2f7323e749df612e)、[mspi_dt_spec](../peripheral_bus_storage_model_reference/P043_mspi_dt_spec_结构体.md)。

配置 MSPI 控制器。

<a id="r_ga7e3bae501067b045e9ed8d0efbe6e61d"></a>

```c
typedef int(* mspi_api_dev_config) (const struct device *controller, const struct mspi_dev_id *dev_id, const enum mspi_dev_cfg_mask param_mask, const struct mspi_dev_cfg *cfg)
```

相关声明：[mspi_api_dev_config](#ga7e3bae501067b045e9ed8d0efbe6e61d)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_dev_cfg_mask](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#ga71c447d059acf7a8055c380243f3a647)、[mspi_dev_cfg](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md)。

使用设备特定参数配置 MSPI 控制器。

<a id="r_gadd66b118b76a4ee7ef252afc6b830bfa"></a>

```c
typedef int(* mspi_api_get_channel_status) (const struct device *controller, uint8_t ch)
```

相关声明：[mspi_api_get_channel_status](#gadd66b118b76a4ee7ef252afc6b830bfa)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

查询通道是否就绪。

<a id="r_ga17b551f4d9f980fde8eabcaae3318617"></a>

```c
typedef int(* mspi_api_transceive) (const struct device *controller, const struct mspi_dev_id *dev_id, const struct mspi_xfer *req)
```

相关声明：[mspi_api_transceive](#ga17b551f4d9f980fde8eabcaae3318617)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_xfer](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md)。

通过 MSPI 执行传输请求。

<a id="r_gad6d65ef0d523f22592ff17c04698f663"></a>

```c
typedef int(* mspi_api_register_callback) (const struct device *controller, const struct mspi_dev_id *dev_id, const enum mspi_bus_event evt_type, mspi_callback_handler_t cb, struct mspi_callback_context *ctx)
```

相关声明：[mspi_api_register_callback](#gad6d65ef0d523f22592ff17c04698f663)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_bus_event](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#ga4cd05950729893e08ef0d4a12e2242d5)、[mspi_callback_handler_t](../api_protocol_topic_reference/P037_MSPI 回调 API（MSPI callback API）.md#ga29421f748fdb89c823e1a48ff69cf0f4)、[mspi_callback_context](../peripheral_bus_storage_model_reference/P037_mspi_callback_context_结构体.md)。

注册 MSPI 回调函数。

<a id="r_ga002c5d3cc7d6691130dee0f42b928894"></a>

```c
typedef int(* mspi_api_memmap_config) (const struct device *controller, const struct mspi_dev_id *dev_id, const struct mspi_memmap_cfg *memmap_cfg)
```

相关声明：[mspi_api_memmap_config](#ga002c5d3cc7d6691130dee0f42b928894)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_memmap_cfg](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md)。

配置 MSPI 内存映射（Memory map）设置。

<a id="r_ga092c8bb0879977a8cc8eea5d1662c34b"></a>

```c
typedef int(* mspi_api_scramble_config) (const struct device *controller, const struct mspi_dev_id *dev_id, const struct mspi_scramble_cfg *scramble_cfg)
```

相关声明：[mspi_api_scramble_config](#ga092c8bb0879977a8cc8eea5d1662c34b)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_scramble_cfg](../peripheral_bus_storage_model_reference/P048_mspi_scramble_cfg_结构体.md)。

配置 MSPI 扰码（Scrambling）设置。

<a id="r_ga407713e07f23756564814402342c9c97"></a>

```c
typedef int(* mspi_api_timing_config) (const struct device *controller, const struct mspi_dev_id *dev_id, const uint32_t param_mask, void *timing_cfg)
```

相关声明：[mspi_api_timing_config](#ga407713e07f23756564814402342c9c97)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

配置 MSPI 时序（Timing）设置。

## 15.3\_详细说明（Detailed Documentation）

<a id="ga2ff9209634fb241e2f7323e749df612e"></a>

### `mspi_api_config`

```c
typedef int(* mspi_api_config) (const struct mspi_dt_spec *spec)
```

```c
#include <zephyr/drivers/mspi.h>
```

配置 MSPI 控制器。

参数说明参见 `mspi_config()`。

<a id="ga7e3bae501067b045e9ed8d0efbe6e61d"></a>

### `mspi_api_dev_config`

```c
typedef int(* mspi_api_dev_config) (const struct device *controller, const struct mspi_dev_id *dev_id, const enum mspi_dev_cfg_mask param_mask, const struct mspi_dev_cfg *cfg)
```

```c
#include <zephyr/drivers/mspi.h>
```

使用设备特定参数配置 MSPI 控制器。

参数说明参见 `mspi_dev_config()`。

<a id="gadd66b118b76a4ee7ef252afc6b830bfa"></a>

### `mspi_api_get_channel_status`

```c
typedef int(* mspi_api_get_channel_status) (const struct device *controller, uint8_t ch)
```

```c
#include <zephyr/drivers/mspi.h>
```

查询通道是否就绪。

参数说明参见 `mspi_get_channel_status()`。

<a id="ga002c5d3cc7d6691130dee0f42b928894"></a>

### `mspi_api_memmap_config`

```c
typedef int(* mspi_api_memmap_config) (const struct device *controller, const struct mspi_dev_id *dev_id, const struct mspi_memmap_cfg *memmap_cfg)
```

```c
#include <zephyr/drivers/mspi.h>
```

配置 MSPI 内存映射（Memory map）设置。

参数说明参见 `mspi_memmap_config()`。

<a id="gad6d65ef0d523f22592ff17c04698f663"></a>

### `mspi_api_register_callback`

```c
typedef int(* mspi_api_register_callback) (const struct device *controller, const struct mspi_dev_id *dev_id, const enum mspi_bus_event evt_type, mspi_callback_handler_t cb, struct mspi_callback_context *ctx)
```

```c
#include <zephyr/drivers/mspi.h>
```

注册 MSPI 回调函数。

参数说明参见 `mspi_register_callback()`。

<a id="ga092c8bb0879977a8cc8eea5d1662c34b"></a>

### `mspi_api_scramble_config`

```c
typedef int(* mspi_api_scramble_config) (const struct device *controller, const struct mspi_dev_id *dev_id, const struct mspi_scramble_cfg *scramble_cfg)
```

```c
#include <zephyr/drivers/mspi.h>
```

配置 MSPI 扰码（Scrambling）设置。

参数说明参见 `mspi_scramble_config()`。

<a id="ga407713e07f23756564814402342c9c97"></a>

### `mspi_api_timing_config`

```c
typedef int(* mspi_api_timing_config) (const struct device *controller, const struct mspi_dev_id *dev_id, const uint32_t param_mask, void *timing_cfg)
```

```c
#include <zephyr/drivers/mspi.h>
```

配置 MSPI 时序（Timing）设置。

参数说明参见 `mspi_timing_config()`。

<a id="ga17b551f4d9f980fde8eabcaae3318617"></a>

### `mspi_api_transceive`

```c
typedef int(* mspi_api_transceive) (const struct device *controller, const struct mspi_dev_id *dev_id, const struct mspi_xfer *req)
```

```c
#include <zephyr/drivers/mspi.h>
```

通过 MSPI 执行传输请求。

参数说明参见 `mspi_transceive()`。


## 15.4\_原页交叉引用（Cross References）

- [mspi_driver_api](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md)
- [mspi_dt_spec](../peripheral_bus_storage_model_reference/P043_mspi_dt_spec_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)
- [mspi_dev_cfg_mask](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#ga71c447d059acf7a8055c380243f3a647)
- [mspi_dev_cfg](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mspi_xfer](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md)
- [mspi_bus_event](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#ga4cd05950729893e08ef0d4a12e2242d5)
- [mspi_callback_handler_t](../api_protocol_topic_reference/P037_MSPI 回调 API（MSPI callback API）.md#ga29421f748fdb89c823e1a48ff69cf0f4)
- [mspi_callback_context](../peripheral_bus_storage_model_reference/P037_mspi_callback_context_结构体.md)
- [mspi_memmap_cfg](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md)
- [mspi_scramble_cfg](../peripheral_bus_storage_model_reference/P048_mspi_scramble_cfg_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/drivers/mspi.h](../peripheral_bus_storage_header_reference/P017_zephyr__drivers__mspi.h_头文件参考.md)
- [mspi_config()](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#ga46c2b98e99ecea045c1ecac4bdf3f087)
- [mspi_dev_config()](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gaa3c1eae8b3000c9bafcc26f14a8beb8b)
- [mspi_get_channel_status()](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#ga957b6ecd96c9f942f75bbe500898930d)
- [mspi_memmap_config()](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gac025129882f814b59d5726c01f0138ce)
- [mspi_register_callback()](../api_protocol_topic_reference/P037_MSPI 回调 API（MSPI callback API）.md#ga967f5fed63f08ac2d5a88625b030cd14)
- [mspi_scramble_config()](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gacf287e08b6ce4898524884e8de22b806)
- [mspi_timing_config()](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gaff82af1cfc99b9e78cec17ea27f79ab6)
- [mspi_transceive()](P016_MSPI 传输 API（MSPI Transfer API）.md#ga8c98c73e322c575b759ce911cc115129)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P014_组播监听发现（Multicast Listener Discovery）的API。.md) · [返回大纲](大纲.md) · [下一章](P016_MSPI 传输 API（MSPI Transfer API）.md)
