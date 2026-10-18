---
id: learning.zephyr-docs.api-device-topic-reference.page-21
title: 一次性可编程存储器（One Time Programmable Memory）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_一次性可编程存储器（One Time Programmable Memory）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

一次性可编程（One Time Programmable，OTP）存储器接口。

<a id="details"></a>

一次性可编程存储器接口（One Time Programmable Memory，OTP）。自 Zephyr 4.4 起提供；API 版本为 0.1.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 21.1\_主题（Topics）

<a id="r_otp_5Finterface_5Fbackend"></a>

相关声明：[OTP 驱动后端 API](../api_service_topic_reference/P016_OTP 驱动后端 API.md)。

<a id="r_otp_5Finterface_5Fnpm10xx"></a>

相关声明：[nPM10xx OTP 接口](../api_extension_topic_reference/P021_nPM10xx OTP 接口.md)。

<a id="header-files"></a>
<a id="files"></a>

## 21.2\_文件（Files）

<a id="r_otp_2Eh"></a>

```c
file otp.h
```

相关声明：[otp.h](../api_file_service_reference/P034_zephyr__drivers__otp.h_文件参考.md)。

一次性可编程存储器（OTP）驱动API的主头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.3\_函数（Functions）

<a id="r_ga067683279ab5d0e9b5f32f83c6b12630"></a>

```c
int otp_read (const struct device *dev, off_t offset, void *data, size_t len)
```

相关声明：[otp_read](#ga067683279ab5d0e9b5f32f83c6b12630)、[device](../device_reference/P002_设备对象结构.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

从一次性可编程存储器（OTP Memory）读取数据。

<a id="r_gacaba6f85fb9ba7c0683417b9a2a81a6a"></a>

```c
int otp_program (const struct device *dev, off_t offset, const void *data, size_t len)
```

相关声明：[otp_program](#gacaba6f85fb9ba7c0683417b9a2a81a6a)、[device](../device_reference/P002_设备对象结构.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

向给定一次性可编程存储器（OTP Memory）编程写入数据。

## 21.4\_详细说明（Detailed Documentation）

<a id="gacaba6f85fb9ba7c0683417b9a2a81a6a"></a>

### `otp_program()`

```c
int otp_program ( const struct device * dev, off_t offset, const void * data, size_t len )
```

```c
#include <zephyr/drivers/otp.h>
```

向给定一次性可编程存储器（OTP Memory）编程写入数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | OTP 设备。 |
| `offset` | 要编程写入数据的地址偏移量。 |
| `data` | 包含待编程写入数据的缓冲区。 |
| `len` | 要编程的字节数。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga067683279ab5d0e9b5f32f83c6b12630"></a>

### `otp_read()`

```c
int otp_read ( const struct device * dev, off_t offset, void * data, size_t len )
```

```c
#include <zephyr/drivers/otp.h>
```

从一次性可编程存储器（OTP Memory）读取数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | OTP 设备。 |
| `offset` | 要读取的地址偏移量。 |
| `data` | 用于保存所读数据的缓冲区。 |
| `len` | 要读取的字节数。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。


## 21.5\_原页交叉引用（Cross References）

- [OTP 驱动后端 API](../api_service_topic_reference/P016_OTP 驱动后端 API.md)
- [nPM10xx OTP 接口](../api_extension_topic_reference/P021_nPM10xx OTP 接口.md)
- [otp.h](../api_file_service_reference/P034_zephyr__drivers__otp.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P020_卸载型网络设备（Offloaded Net Devices）.md) · [返回大纲](大纲.md) · [下一章](P022_传感器坐标轴对齐（Sensor axis alignment）.md)
