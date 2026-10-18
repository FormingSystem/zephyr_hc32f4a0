---
id: learning.zephyr-docs.api-device-topic-reference.page-9
title: FPGA 驱动后端 API（Driver Backend API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_FPGA 驱动后端 API（Driver Backend API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现现场可编程门阵列（FPGA）驱动所需的 API 类型定义、回调签名及其他辅助定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_fpga_5Fdriver_5Fapi"></a>

```c
struct fpga_driver_api
```

相关声明：[fpga_driver_api](../peripheral_bus_storage_model_reference/P018_fpga_driver_api_结构体.md)。

驱动操作（Driver Operations）：现场可编程门阵列（FPGA）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.2\_类型定义（Typedefs）

<a id="r_ga02d71e7a82f446220d67664d4cc7a5c9"></a>

```c
typedef enum FPGA_status(* fpga_api_get_status) (const struct device *dev)
```

相关声明：[FPGA_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#ga0bbacdfdac79bace1786bb2a1627bb1e)、[fpga_api_get_status](#ga02d71e7a82f446220d67664d4cc7a5c9)、[device](../device_reference/P002_设备对象结构.md)。

读取 FPGA 状态的回调 API。

<a id="r_ga9860c64bbc2cfb89df9b51da655691b6"></a>

```c
typedef int(* fpga_api_load) (const struct device *dev, uint32_t *image_ptr, uint32_t img_size)
```

相关声明：[fpga_api_load](#ga9860c64bbc2cfb89df9b51da655691b6)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

加载位流（Bitstream）并配置 FPGA 的回调 API。

<a id="r_ga3c53b90b9d0b50c44c01a534c61e9212"></a>

```c
typedef int(* fpga_api_reset) (const struct device *dev)
```

相关声明：[fpga_api_reset](#ga3c53b90b9d0b50c44c01a534c61e9212)、[device](../device_reference/P002_设备对象结构.md)。

复位 FPGA 的回调 API。

<a id="r_gaf3e8ea5d443fd09352e2b63f82a459be"></a>

```c
typedef int(* fpga_api_on) (const struct device *dev)
```

相关声明：[fpga_api_on](#gaf3e8ea5d443fd09352e2b63f82a459be)、[device](../device_reference/P002_设备对象结构.md)。

开启 FPGA 的回调 API。

<a id="r_ga872a8d75bb46de50a41b56170804ed27"></a>

```c
typedef int(* fpga_api_off) (const struct device *dev)
```

相关声明：[fpga_api_off](#ga872a8d75bb46de50a41b56170804ed27)、[device](../device_reference/P002_设备对象结构.md)。

关闭 FPGA 的回调 API。

<a id="r_ga24fd6ce4832b960b79914f42010774aa"></a>

```c
typedef const char *(* fpga_api_get_info) (const struct device *dev)
```

相关声明：[fpga_api_get_info](#ga24fd6ce4832b960b79914f42010774aa)、[device](../device_reference/P002_设备对象结构.md)。

返回 FPGA 信息的回调 API。

## 9.3\_详细说明（Detailed Documentation）

<a id="ga24fd6ce4832b960b79914f42010774aa"></a>

### `fpga_api_get_info`

```c
typedef const char *(* fpga_api_get_info) (const struct device *dev)
```

```c
#include <zephyr/drivers/fpga.h>
```

返回 FPGA 信息的回调 API。

参数说明参见 `fpga_get_info()`。

<a id="ga02d71e7a82f446220d67664d4cc7a5c9"></a>

### `fpga_api_get_status`

```c
typedef enum FPGA_status(* fpga_api_get_status) (const struct device *dev)
```

```c
#include <zephyr/drivers/fpga.h>
```

读取 FPGA 状态的回调 API。

参数说明参见 `fpga_get_status()`。

<a id="ga9860c64bbc2cfb89df9b51da655691b6"></a>

### `fpga_api_load`

```c
typedef int(* fpga_api_load) (const struct device *dev, uint32_t *image_ptr, uint32_t img_size)
```

```c
#include <zephyr/drivers/fpga.h>
```

加载位流（Bitstream）并配置 FPGA 的回调 API。

参数说明参见 `fpga_load()`。

<a id="ga872a8d75bb46de50a41b56170804ed27"></a>

### `fpga_api_off`

```c
typedef int(* fpga_api_off) (const struct device *dev)
```

```c
#include <zephyr/drivers/fpga.h>
```

关闭 FPGA 的回调 API。

参数说明参见 `fpga_off()`。

<a id="gaf3e8ea5d443fd09352e2b63f82a459be"></a>

### `fpga_api_on`

```c
typedef int(* fpga_api_on) (const struct device *dev)
```

```c
#include <zephyr/drivers/fpga.h>
```

开启 FPGA 的回调 API。

参数说明参见 `fpga_on()`。

<a id="ga3c53b90b9d0b50c44c01a534c61e9212"></a>

### `fpga_api_reset`

```c
typedef int(* fpga_api_reset) (const struct device *dev)
```

```c
#include <zephyr/drivers/fpga.h>
```

复位 FPGA 的回调 API。

参数说明参见 `fpga_reset()`。


## 9.4\_原页交叉引用（Cross References）

- [fpga_driver_api](../peripheral_bus_storage_model_reference/P018_fpga_driver_api_结构体.md)
- [FPGA_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#ga0bbacdfdac79bace1786bb2a1627bb1e)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/drivers/fpga.h](../peripheral_bus_storage_header_reference/P006_zephyr__drivers__fpga.h_头文件参考.md)
- [fpga_get_info()](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gab887999e8728bcc335a784afbdbbee8f)
- [fpga_get_status()](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#ga1a1e78a46df9f4bd374cf5ecc2449360)
- [fpga_load()](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#ga1cace6c7cc44705bf861d7aa5e863e16)
- [fpga_off()](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gaa161c7a7006db24793c1a1ecdea25b5c)
- [fpga_on()](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gad9093bd96c6a62cd958718d1e01e3f37)
- [fpga_reset()](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gadfc8d6c24cb1b1640393017a462011c9)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P008_ENS160 API主题.md) · [返回大纲](大纲.md) · [下一章](P010_FT8xx 通用函数.md)
