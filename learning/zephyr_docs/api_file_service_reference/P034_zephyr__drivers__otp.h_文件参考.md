---
id: learning.zephyr-docs.api-file-service-reference.page-34
title: zephyr__drivers__otp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/otp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_zephyr\_\_drivers\_\_otp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/otp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

一次性可编程存储器（OTP）驱动API的主头文件。

<a id="details"></a>

```c
#include <stddef.h>
#include <sys/types.h>
#include <zephyr/device.h>
#include <zephyr/types.h>
#include <zephyr/syscalls/otp.h>
```

查看此文件的源码。

一次性可编程存储器（OTP）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 34.1\_数据结构（Data Structures）

<a id="r_otp_5Fdriver_5Fapi"></a>

```c
struct otp_driver_api
```

相关声明：[otp_driver_api](../platform_security_model_reference/P024_otp_driver_api_结构体.md)。

驱动操作（Driver Operations）：一次性可编程存储器（OTP）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 34.2\_类型定义（Typedefs）

<a id="r_ga2dd11aba59cbe417973d98503d67b343"></a>

```c
typedef int(* otp_api_read) (const struct device *dev, off_t offset, void *data, size_t len)
```

相关声明：[otp_api_read](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__backend.html#ga2dd11aba59cbe417973d98503d67b343)、[device](../device_reference/P002_设备对象结构.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

读取一次性可编程存储器（OTP Memory）时使用的回调 API（Callback API）。

<a id="r_gae4eff2ba1959c2817f684a3306427e09"></a>

```c
typedef int(* otp_api_program) (const struct device *dev, off_t offset, const void *data, size_t len)
```

相关声明：[otp_api_program](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__backend.html#gae4eff2ba1959c2817f684a3306427e09)、[device](../device_reference/P002_设备对象结构.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

写入一次性可编程存储器（OTP Memory）时使用的回调 API（Callback API）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 34.3\_函数（Functions）

<a id="r_ga067683279ab5d0e9b5f32f83c6b12630"></a>

```c
int otp_read (const struct device *dev, off_t offset, void *data, size_t len)
```

相关声明：[otp_read](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface.html#ga067683279ab5d0e9b5f32f83c6b12630)、[device](../device_reference/P002_设备对象结构.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

从一次性可编程存储器（OTP Memory）读取数据。

<a id="r_gacaba6f85fb9ba7c0683417b9a2a81a6a"></a>

```c
int otp_program (const struct device *dev, off_t offset, const void *data, size_t len)
```

相关声明：[otp_program](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface.html#gacaba6f85fb9ba7c0683417b9a2a81a6a)、[device](../device_reference/P002_设备对象结构.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

向给定一次性可编程存储器（OTP Memory）编程写入数据。


## 34.4\_原页交叉引用（Cross References）

- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P639_otp.h_源码浏览.md)
- [otp_driver_api](../platform_security_model_reference/P024_otp_driver_api_结构体.md)
- [otp_api_read](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__backend.html#ga2dd11aba59cbe417973d98503d67b343)
- [device](../device_reference/P002_设备对象结构.md)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)
- [otp_api_program](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__backend.html#gae4eff2ba1959c2817f684a3306427e09)
- [otp_read](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface.html#ga067683279ab5d0e9b5f32f83c6b12630)
- [otp_program](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface.html#gacaba6f85fb9ba7c0683417b9a2a81a6a)

<a id="header-details"></a>

---

[上一章](P033_zephyr__bluetooth__mesh__od_priv_proxy_cli.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P035_zephyr__bluetooth__audio__pbp.h_文件参考.md)
