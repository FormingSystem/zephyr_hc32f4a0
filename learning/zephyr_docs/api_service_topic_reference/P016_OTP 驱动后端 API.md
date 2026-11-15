---
id: learning.zephyr-docs.api-service-topic-reference.page-16
title: OTP 驱动后端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_OTP 驱动后端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现一次性可编程存储器驱动（OTP Driver）所需的 API 类型定义（Type Definitions）、回调签名（Callback Signatures）及其他辅助工具（Helpers）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 16.1\_数据结构（Data Structures）

<a id="r_otp_5Fdriver_5Fapi"></a>

```c
struct otp_driver_api
```

相关声明：[otp_driver_api](../platform_security_model_reference/P024_otp_driver_api_结构体.md)。

驱动操作（Driver Operations）：一次性可编程存储器（OTP）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 16.2\_类型定义（Typedefs）

<a id="r_ga2dd11aba59cbe417973d98503d67b343"></a>

```c
typedef int(* otp_api_read) (const struct device *dev, off_t offset, void *data, size_t len)
```

相关声明：[otp_api_read](#ga2dd11aba59cbe417973d98503d67b343)、[device](../device_reference/P002_设备对象结构.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

读取一次性可编程存储器（OTP Memory）时使用的回调 API（Callback API）。

<a id="r_gae4eff2ba1959c2817f684a3306427e09"></a>

```c
typedef int(* otp_api_program) (const struct device *dev, off_t offset, const void *data, size_t len)
```

相关声明：[otp_api_program](#gae4eff2ba1959c2817f684a3306427e09)、[device](../device_reference/P002_设备对象结构.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

写入一次性可编程存储器（OTP Memory）时使用的回调 API（Callback API）。

## 16.3\_详细说明（Detailed Documentation）

<a id="gae4eff2ba1959c2817f684a3306427e09"></a>

### `otp_api_program`

```c
typedef int(* otp_api_program) (const struct device *dev, off_t offset, const void *data, size_t len)
```

```c
#include <zephyr/drivers/otp.h>
```

写入一次性可编程存储器（OTP Memory）时使用的回调 API（Callback API）。

参数说明（Argument Description）参见 `otp_program()`。

<a id="ga2dd11aba59cbe417973d98503d67b343"></a>

### `otp_api_read`

```c
typedef int(* otp_api_read) (const struct device *dev, off_t offset, void *data, size_t len)
```

```c
#include <zephyr/drivers/otp.h>
```

读取一次性可编程存储器（OTP Memory）时使用的回调 API（Callback API）。

参数说明（Argument Description）参见 `otp_read()`。


## 16.4\_原页交叉引用（Cross References）

- [otp_driver_api](../platform_security_model_reference/P024_otp_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)
- [zephyr/drivers/otp.h](../api_file_service_reference/P034_zephyr__drivers__otp.h_文件参考.md)
- [otp_program()](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface.html#gacaba6f85fb9ba7c0683417b9a2a81a6a)
- [otp_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface.html#ga067683279ab5d0e9b5f32f83c6b12630)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P015_能力过滤器（Caps Filters）.md) · [返回大纲](大纲.md) · [下一章](P017_Renesas RA0 引脚控制辅助工具（Pin control helpers）.md)
