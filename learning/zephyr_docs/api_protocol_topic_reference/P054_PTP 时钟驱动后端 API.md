---
id: learning.zephyr-docs.api-protocol-topic-reference.page-54
title: PTP 时钟驱动后端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_PTP 时钟驱动后端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现 PTP 时钟驱动所需的 API 类型定义、回调签名及其他辅助定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 54.1\_数据结构（Data Structures）

<a id="r_ptp_5Fclock_5Fdriver_5Fapi"></a>

```c
struct ptp_clock_driver_api
```

相关声明：[ptp_clock_driver_api](../network_service_model_reference/P054_ptp_clock_driver_api_结构体.md)。

驱动操作（Driver Operations）：精确时间协议时钟（PTP Clock）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 54.2\_类型定义（Typedefs）

<a id="r_gaeda56e624ddc47b5f23ebd090031982a"></a>

```c
typedef int(* ptp_clock_api_set_t) (const struct device *dev, struct net_ptp_time *tm)
```

相关声明：[ptp_clock_api_set_t](#gaeda56e624ddc47b5f23ebd090031982a)、[device](../device_reference/P002_设备对象结构.md)、[net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

设置精确时间协议时钟（PTP Clock）的时间（Time）。

<a id="r_ga59a1c7530e59fd19b3fa25ff6f4e346c"></a>

```c
typedef int(* ptp_clock_api_get_t) (const struct device *dev, struct net_ptp_time *tm)
```

相关声明：[ptp_clock_api_get_t](#ga59a1c7530e59fd19b3fa25ff6f4e346c)、[device](../device_reference/P002_设备对象结构.md)、[net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

获取精确时间协议时钟（PTP Clock）的时间（Time）。

<a id="r_gad3b345ba7db470f274cffa33b1128810"></a>

```c
typedef int(* ptp_clock_api_adjust_t) (const struct device *dev, int increment)
```

相关声明：[ptp_clock_api_adjust_t](#gad3b345ba7db470f274cffa33b1128810)、[device](../device_reference/P002_设备对象结构.md)。

调整精确时间协议时钟（PTP Clock）的时间（Time）。

<a id="r_gae94ee94813969d15f8dc841814562ac3"></a>

```c
typedef int(* ptp_clock_api_rate_adjust_t) (const struct device *dev, double ratio)
```

相关声明：[ptp_clock_api_rate_adjust_t](#gae94ee94813969d15f8dc841814562ac3)、[device](../device_reference/P002_设备对象结构.md)。

基于标称频率（Nominal Frequency）调整精确时间协议时钟（PTP Clock）的速率比（Rate Ratio）。

## 54.3\_详细说明（Detailed Documentation）

<a id="gad3b345ba7db470f274cffa33b1128810"></a>

### `ptp_clock_api_adjust_t`

```c
typedef int(* ptp_clock_api_adjust_t) (const struct device *dev, int increment)
```

```c
#include <zephyr/drivers/ptp_clock.h>
```

调整精确时间协议时钟（PTP Clock）的时间（Time）。

参数说明参见 `ptp_clock_adjust()`。

<a id="ga59a1c7530e59fd19b3fa25ff6f4e346c"></a>

### `ptp_clock_api_get_t`

```c
typedef int(* ptp_clock_api_get_t) (const struct device *dev, struct net_ptp_time *tm)
```

```c
#include <zephyr/drivers/ptp_clock.h>
```

获取精确时间协议时钟（PTP Clock）的时间（Time）。

参数说明参见 `ptp_clock_get()`。

<a id="gae94ee94813969d15f8dc841814562ac3"></a>

### `ptp_clock_api_rate_adjust_t`

```c
typedef int(* ptp_clock_api_rate_adjust_t) (const struct device *dev, double ratio)
```

```c
#include <zephyr/drivers/ptp_clock.h>
```

基于标称频率（Nominal Frequency）调整精确时间协议时钟（PTP Clock）的速率比（Rate Ratio）。

参数说明参见 `ptp_clock_rate_adjust()`。

<a id="gaeda56e624ddc47b5f23ebd090031982a"></a>

### `ptp_clock_api_set_t`

```c
typedef int(* ptp_clock_api_set_t) (const struct device *dev, struct net_ptp_time *tm)
```

```c
#include <zephyr/drivers/ptp_clock.h>
```

设置精确时间协议时钟（PTP Clock）的时间（Time）。

参数说明参见 `ptp_clock_set()`。


## 54.4\_原页交叉引用（Cross References）

- [ptp_clock_driver_api](../network_service_model_reference/P054_ptp_clock_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)
- [tm](../posix_system_model_reference/P025_tm_结构体.md)
- [zephyr/drivers/ptp_clock.h](../api_file_service_reference/P042_zephyr__drivers__ptp_clock.h_文件参考.md)
- [ptp_clock_adjust()](P053_精确时间协议时钟（PTP Clock）.md#gabd11d19b5ec5491e5813bf7cb74ab9b0)
- [ptp_clock_get()](P053_精确时间协议时钟（PTP Clock）.md#ga443f97ef2766e87c0b42c6ad6f7b63b4)
- [ptp_clock_rate_adjust()](P053_精确时间协议时钟（PTP Clock）.md#ga310ee4974e6f3b01c4aa1b985194e57a)
- [ptp_clock_set()](P053_精确时间协议时钟（PTP Clock）.md#ga41123183be722b3423d5e993d3cde7c2)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P053_精确时间协议时钟（PTP Clock）.md) · [返回大纲](大纲.md) · [下一章](P055_PTP 时间.md)
